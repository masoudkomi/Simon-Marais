#!/usr/bin/env python3
"""Independent, bounded finite checks for the 2019 B4(b) v1 review.

Written from the mathematical specification without reading the author's
computation scripts or any other review. Uses Python's standard library only.
Nothing in this script is a proof of an unrestricted asymptotic statement.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import os
import platform
import time
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
PROBLEM = HERE.parent
START = time.monotonic()
EXPECTED_PROOF_HASH = "227cff77dc63aba6125494e6e39e3feb687fe4b8a3ff90d4392d72b4133e5a1e"
FORBIDDEN = ("RRLL", "RRLRRLRLLRLL")
REPLACEMENTS = ("LLRR", "LLRLLRLRRLRR")
WEIGHTS = (
    1000000000000, 837605905420, 539189558215, 451628358102,
    829914937903, 525056590887, 425657533878, 782190797941,
    912301838575, 838845340670, 541467151750, 455813677432,
)
DISPLAYED_SLACKS = (
    409458000000, 342964384620, 220775446615, 184922881622,
    339815293183, 214988686007, 174288855158, 320274236101,
    373549380575, 343471859870, 221708031750, 186636581752,
)
Q = Fraction(183761, 100000)


def checkpoint(message: str) -> None:
    elapsed = time.monotonic() - START
    print(f"elapsed={elapsed:.3f}s {message}", flush=True)
    if elapsed > 120:
        raise TimeoutError("Independent check exceeded its 120-second inner budget")


def context(history: str, first: int = 0) -> tuple[str, str]:
    """Chronological left additions are reversed; right additions are not."""
    left, right = [], []
    for t, move in enumerate(history):
        bit = str(first ^ (t & 1))
        (left if move == "L" else right).append(bit)
    return "".join(reversed(left)), "".join(right)


def apply(history: str, first: int = 0, seed: str = "1") -> str:
    word = seed
    for t, move in enumerate(history):
        bit = str(first ^ (t & 1))
        word = bit + word if move == "L" else word + bit
    return word


def histories(t: int):
    return map("".join, itertools.product("LR", repeat=t))


def avoids(history: str) -> bool:
    return all(f not in history for f in FORBIDDEN)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    checkpoint(f"pid={os.getpid()} Python={platform.python_version()}")
    proof_hash = digest(PROBLEM / "proof.md")
    assert proof_hash == EXPECTED_PROOF_HASH, (proof_hash, EXPECTED_PROOF_HASH)
    cert_path = PROBLEM / "computations/upper-certificate-2026-10-16.json"
    enum_path = PROBLEM / "computations/enumeration-2026-10-16.json"
    cert = json.loads(cert_path.read_text())
    enumeration = json.loads(enum_path.read_text())

    # Exact universal context identities for both possible starting parities.
    relation_checks = []
    for old, new in zip(FORBIDDEN, REPLACEMENTS):
        assert len(old) == len(new) and new < old
        for first in (0, 1):
            old_context, new_context = context(old, first), context(new, first)
            assert old_context == new_context
            # Also use a deliberately non-binary marked core, independently
            # checking that the direct update routine has the same orientation.
            assert apply(old, first, "<CORE>") == apply(new, first, "<CORE>")
            relation_checks.append({
                "old": old, "new": new, "first_bit": first,
                "left": old_context[0], "right": old_context[1],
            })
    checkpoint("both context identities verified at both bit parities")

    # Construct the full prefix/suffix machine from the forbidden strings,
    # without copying the author's transition table.
    prefixes = {f[:i] for f in FORBIDDEN for i in range(len(f))}
    states = sorted(prefixes, key=lambda s: (len(s), s))
    index = {s: i for i, s in enumerate(states)}
    transitions = []
    matrix = [[0] * len(states) for _ in states]
    for i, s in enumerate(states):
        row = {}
        for letter in "LR":
            extended = s + letter
            if any(extended.endswith(f) for f in FORBIDDEN):
                row[letter] = None
            else:
                target = max((p for p in states if extended.endswith(p)), key=len)
                row[letter] = target
                matrix[i][index[target]] += 1
        transitions.append(row)
    assert states == cert["states"]
    assert transitions == cert["transitions"]
    assert matrix == cert["matrix"]
    assert list(FORBIDDEN) == cert["forbidden"]
    assert list(WEIGHTS) == cert["positive_integer_weights"]
    assert cert["q_numerator"] == Q.numerator
    assert cert["q_denominator"] == Q.denominator
    av = [sum(a * v for a, v in zip(row, WEIGHTS)) for row in matrix]
    slacks = [Q.numerator * v - Q.denominator * a for v, a in zip(WEIGHTS, av)]
    assert tuple(slacks) == DISPLAYED_SLACKS
    assert slacks == cert["strict_integer_slacks"]
    assert min(slacks) > 0 and min(WEIGHTS) > 0
    ratios = [Fraction(a, v) for a, v in zip(av, WEIGHTS)]
    qprime = max(ratios)
    assert 0 < qprime < Q
    p_q = Q**3 - Q**2 - Q - 1
    assert p_q < 0 and Q > 1
    checkpoint(f"12-state machine, every integer slack, and qprime={qprime} checked")

    # Brute-force all histories through 16 moves. Each accepted history has
    # exactly the independently expected longest suffix; accepted counts are
    # compared to exact matrix iteration. For t <= 14, recover each word's
    # lexicographically first history and check avoidance directly.
    rows = []
    continuation_counts = [1] * len(states)
    history_checks = 0
    lex_word_checks = 0
    for t in range(17):
        accepted = 0
        first_history = {}
        for h in histories(t):
            history_checks += 1
            state = ""
            for letter in h:
                state = transitions[index[state]][letter]
                if state is None:
                    break
            good = avoids(h)
            assert (state is not None) == good, (t, h, state)
            if good:
                accepted += 1
                assert state == max((p for p in states if h.endswith(p)), key=len)
            if t <= 14:
                first_history.setdefault(apply(h), h)
        assert accepted == continuation_counts[0]
        record = {"moves": t, "avoiding_histories": accepted}
        if t <= 14:
            assert all(avoids(h) for h in first_history.values())
            assert len(first_history) == enumeration["b_n"][str(t + 1)]
            record["distinct_words"] = len(first_history)
            lex_word_checks += len(first_history)
        rows.append(record)
        continuation_counts = [sum(a * d for a, d in zip(row, continuation_counts)) for row in matrix]
    checkpoint(f"all {history_checks} histories through 16 moves checked")

    # Independent 12+12 meet-in-the-middle enumeration. Each half starts
    # with bit zero, because 12 additions preserve odd starting length.
    # Deduplicate half-contexts from all 2^12 histories, then compose all
    # 2030^2 context pairs. Discarding each fixed-position set before moving
    # on bounds memory, and no 24-move word-generation routine is reused.
    half_by_position = [set() for _ in range(13)]
    for h in histories(12):
        pair = context(h)
        assert apply(h) == pair[0] + "1" + pair[1]
        half_by_position[len(pair[0])].add(pair)
    half_counts = [len(group) for group in half_by_position]
    assert sum(half_counts) == 2030
    expected_row = next(row for row in enumeration["marked_context_rows"] if row["moves"] == 24)
    position_counts = []
    products_total = 0
    central_digest = None
    for p in range(25):
        complete = set()
        products = 0
        for a in range(max(0, p - 12), min(12, p) + 1):
            b = p - a
            for left1, right1 in half_by_position[a]:
                for left2, right2 in half_by_position[b]:
                    products += 1
                    complete.add((left2 + left1, right1 + right2))
        products_total += products
        count = len(complete)
        assert count == expected_row["position_counts"][p], (p, count)
        position_counts.append(count)
        if p == 12:
            central_digest = hashlib.sha256(
                "".join(l + ":" + r + "\n" for l, r in sorted(complete)).encode()
            ).hexdigest()
        checkpoint(f"24-move position {p}: products={products} distinct={count}")
        del complete
    assert products_total == sum(half_counts)**2 == 4120900
    assert sum(position_counts) == 2985943
    assert max(position_counts) == 395397
    assert [p for p, c in enumerate(position_counts) if c == max(position_counts)] == [12]

    result = {
        "status": "independent finite evidence only; not an unrestricted proof",
        "reviewer": "review-1; initially blind to all other review reports",
        "python": platform.python_version(),
        "pid": os.getpid(),
        "elapsed_seconds": time.monotonic() - START,
        "input_sha256": {
            "proof.md": proof_hash,
            str(cert_path.relative_to(PROBLEM)): digest(cert_path),
            str(enum_path.relative_to(PROBLEM)): digest(enum_path),
        },
        "relation_checks": relation_checks,
        "states": states,
        "transitions": transitions,
        "matrix": matrix,
        "Av": av,
        "strict_integer_slacks": slacks,
        "qprime_exact": str(qprime),
        "qprime_maximizing_state_indices": [i for i, r in enumerate(ratios) if r == qprime],
        "qprime_numerical_evidence_only": float(qprime),
        "q_minus_qprime_exact": str(Q - qprime),
        "published_cubic_at_q_exact": str(p_q),
        "histories_checked_through_16_moves": history_checks,
        "least_word_histories_checked_through_14_moves": lex_word_checks,
        "small_history_rows": rows,
        "meet_in_middle": {
            "half_moves": 12,
            "half_histories_examined": 4096,
            "distinct_half_contexts": sum(half_counts),
            "half_position_counts": half_counts,
            "composed_context_pairs_examined": products_total,
            "moves": 24,
            "position_counts": position_counts,
            "marked_contexts": sum(position_counts),
            "max_fixed_position_contexts": max(position_counts),
            "maximizing_left_lengths": [12],
            "p12_pairs_lexicographically_sorted_colon_separated_sha256": central_digest,
        },
    }
    output = HERE / "review-1-check-output.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    checkpoint(f"PASS: exact finite report written to {output.name}")


if __name__ == "__main__":
    main()
