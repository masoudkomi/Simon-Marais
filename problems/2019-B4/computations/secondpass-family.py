#!/usr/bin/env python3
"""An infinite verified collision family and its finite avoidance certificate.

The unrestricted derivation is a candidate argument in the accompanying note.
Floating-point power iteration only selects a rational bound; all displayed
certificate inequalities are checked again with exact integers.
"""
from __future__ import annotations

from collections import defaultdict, deque
from fractions import Fraction
import argparse
import itertools
import json
import math
import os
import time

from importlib.machinery import SourceFileLoader
probe = SourceFileLoader("secondpass_probe", __file__.replace("family.py", "probe.py")).load_module()


def family(p: int, q: int) -> tuple[str, str]:
    large = "RRL" + "R" * (2 * p) + "LR" + "L" * (2 * q) + "RLL"
    small = "LLR" + "L" * (2 * q) + "RL" + "R" * (2 * p) + "LRR"
    return large, small


def forbidden_nfa(extra: list[str]):
    # q0 is restarted after every input letter.  q14 is the reject state.
    # The first branch accepts RRL R^(2p) LR L^(2q) RLL, p,q >= 1.
    arcs = defaultdict(set)
    base = [(0,"R",1),(1,"R",2),(2,"L",3),(3,"R",4),(4,"R",5),
            (5,"R",6),(6,"R",5),(5,"L",7),(7,"R",8),(8,"L",9),
            (9,"L",10),(10,"L",11),(11,"L",10),(10,"R",12),
            (12,"L",13),(13,"L",14), (2,"L",15),(15,"L",14)]
    for a,c,b in base:
        arcs[a,c].add(b)
    fresh = 16
    for word in extra:
        current = 0
        for i, c in enumerate(word):
            target = 14 if i == len(word)-1 else fresh
            if target != 14:
                fresh += 1
            arcs[current,c].add(target)
            current = target
    return arcs, 14, fresh


def determinize(extra: list[str], cap: int):
    arcs, reject, nfa_size = forbidden_nfa(extra)
    states = [frozenset({0})]
    indices = {states[0]: 0}
    transitions = []
    for state in states:
        row = []
        for c in "LR":
            target = {0}
            for source in state:
                target.update(arcs[source,c])
            if reject in target:
                row.append(None)
            else:
                key = frozenset(target)
                if key not in indices:
                    assert len(states) < cap, "DFA state cap reached"
                    indices[key] = len(states)
                    states.append(key)
                row.append(indices[key])
        transitions.append(row)
    return states, transitions, nfa_size


def certificate(transitions):
    vector = [1.0] * len(transitions)
    for _ in range(1500):
        image = [sum(vector[j] for j in row if j is not None) for row in transitions]
        ratios = [a/b for a,b in zip(image, vector)]
        scale = max(image)
        vector = [a / scale for a in image]
    denominator = 10**8
    numerator = math.ceil(max(ratios) * denominator) + 1
    weights = [max(1, round(v * 10**15)) for v in vector]
    slacks = [numerator * w - denominator * sum(weights[j] for j in row if j is not None)
              for w,row in zip(weights, transitions)]
    assert min(slacks) > 0
    return {"q_numerator": numerator, "q_denominator": denominator,
            "q_decimal": numerator/denominator,
            "positive_integer_weights": weights, "strict_integer_slacks": slacks,
            "numerical_eigenvalue_evidence_only": [min(ratios), max(ratios)]}


def accepts(history, transitions):
    s = 0
    for c in history:
        s = transitions[s][c == "R"]
        if s is None:
            return False
    return True


def history_count(u, v):
    counts = [[0]*(len(v)+1) for _ in range(len(u)+1)]
    counts[0][0] = 1
    for i in range(len(u)+1):
        for j in range(len(v)+1):
            bit = str((i+j)%2)
            if i<len(u) and u[i] == bit:
                counts[i+1][j] += counts[i][j]
            if j<len(v) and v[j] == bit:
                counts[i][j+1] += counts[i][j]
    return counts[-1][-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--state-cap", type=int, default=20000)
    a = ap.parse_args()
    start = time.monotonic()
    data = json.load(open(a.probe))
    for row in data["minimal_forbidden"]:
        large, small = row["larger"], row["smaller"]
        assert small < large and len(small) == len(large)
        for phase in (0, 1):
            assert probe.context(large, phase) == probe.context(small, phase)
    family_checks = []
    for p,q in itertools.product(range(1, 9), repeat=2):
        large, small = family(p,q)
        expected = ("011" + "01" * (q-1) + "001", "011" + "01" * (p-1) + "001")
        assert small < large and len(small) == len(large)
        assert probe.context(large) == probe.context(small) == expected
        assert probe.context(large, 1) == probe.context(small, 1)
        count = history_count(*expected)
        assert count == 2
        family_checks.append({"p":p,"q":q,"moves":len(large),"total_histories_for_tapes":count})
    out = {"status": "candidate proof - unverified; finite exact certificates",
           "parameters": vars(a), "family_checks":family_checks,
           "finite_obstruction_history_counts":[{"larger":r["larger"],"history_count":history_count(*r["tapes"])} for r in data["minimal_forbidden"]],
           "automata":[]}
    for mode in ("family_only", "family_plus_finite_obstructions"):
        extra = [] if mode == "family_only" else [r["larger"] for r in data["minimal_forbidden"]]
        states, transitions, nfa_size = determinize(extra, a.state_cap)
        print(json.dumps({"checkpoint":mode,"pid":os.getpid(),"DFA_states":len(states)}),flush=True)
        finite_comparisons = []
        for n in range(15):
            # Exhaustive DFA/regular-expression comparison is small and independent.
            count = 0
            for choices in itertools.product("LR", repeat=n):
                h = "".join(choices)
                expected = "RRLL" not in h and not any(
                    family(p,q)[0] in h for p in range(1, n//2+1) for q in range(1, n//2+1))
                expected = expected and not any(f in h for f in extra)
                got = accepts(h, transitions)
                assert expected == got
                count += got
            finite_comparisons.append({"moves":n,"avoiding":count})
        still_avoiding = [r for r in data["minimal_forbidden"] if accepts(r["larger"], transitions)]
        row = {"mode":mode,"extra_finite_forbidden":extra,"NFA_states":nfa_size,
               "DFA_states":[sorted(s) for s in states], "transitions_LR":transitions,
               "finite_regex_comparisons":finite_comparisons,
               "known_nonminimal_histories_still_accepted":still_avoiding}
        row.update(certificate(transitions))
        out["automata"].append(row)
    out["elapsed_seconds"] = time.monotonic()-start
    with open(a.output,"w") as f:
        json.dump(out,f,indent=2)
        f.write("\n")
    print(json.dumps({"finished":True,"seconds":out["elapsed_seconds"],
                      "bounds":[x["q_decimal"] for x in out["automata"]]}),flush=True)


if __name__ == "__main__":
    main()
