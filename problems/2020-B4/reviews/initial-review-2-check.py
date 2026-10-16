#!/usr/bin/env python3
"""Blind R2 arithmetic evidence; no project modules, construction, or CAS.

This checks finite identities and necessary-condition bookkeeping, not an
unrestricted classification. Run only through initial-review-2-run.py, which
records the child PID, uses a subprocess timeout, and keeps checkpoints.
"""

from collections import Counter, deque
from datetime import datetime, timezone
from math import gcd, isqrt
from pathlib import Path
import json
import platform
import random
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
START = time.monotonic()
RESULT = {
    "recorded_utc": datetime.now(timezone.utc).isoformat(),
    "python": platform.python_version(),
    "dependencies": "Python standard library only; no project imports",
    "seed": 20201016,
    "warning": "Finite evidence only. No preliminary construction or unrestricted proof.",
}


def checkpoint(stage, detail):
    print(json.dumps({"stage": stage, "elapsed_seconds": time.monotonic()-START,
                      "detail": detail}, sort_keys=True), flush=True)


def factors(n):
    answer = {}
    t = 2
    while t*t <= n:
        if n % t == 0:
            e = 0
            while n % t == 0:
                n //= t
                e += 1
            answer[t] = e
        t = 3 if t == 2 else t+2
    if n > 1:
        answer[n] = 1
    return answer


def divisors(n):
    answer = [1]
    for p, e in factors(n).items():
        answer = [d*p**j for d in answer for j in range(e+1)]
    return sorted(answer)


def phi(n):
    answer = n
    for p in factors(n):
        answer -= answer//p
    return answer


def closure(generators, modulus):
    # Finite semigroup closure of units is their generated subgroup, including
    # inverses. The group modulo 1 has its unique element represented by 0.
    known = {1 % modulus}
    pending = deque(known)
    while pending:
        x = pending.popleft()
        for g in generators:
            y = x*g % modulus
            if y not in known:
                known.add(y)
                pending.append(y)
    return known


def predicted_strata(v, generators):
    answer = {}
    for d in divisors(v):
        length = len(closure(generators, d))
        assert phi(d) % length == 0
        answer[d] = {"length": length, "count": phi(d)//length}
    return answer


def histogram(strata):
    answer = Counter()
    for info in strata.values():
        answer[info["length"]] += info["count"]
    return dict(sorted(answer.items()))


def reachable(hist, target):
    # Independent plain set dynamic programming, without the author's
    # bitvector/binary splitting implementation.
    states = {0}
    for length, count in sorted(hist.items()):
        next_states = set()
        for subtotal in states:
            for amount in range(min(count, (target-subtotal)//length)+1):
                next_states.add(subtotal+amount*length)
        states = next_states
    return target in states


for q in range(1, 5001):
    v = q*q+q+1
    assert v % 2 == 1
    assert gcd(q, v) == gcd(q+1, v) == 1
    assert (-(q+1)*q) % v == 1
RESULT["normalization_units"] = {"q_min": 1, "q_max": 5000, "passed": True}
checkpoint("normalization_units", RESULT["normalization_units"])

# Check P4's quotient contraction for arbitrary subsets. These are not
# difference-set searches, and no vertex witness or tautness decision is made.
rng = random.Random(20201016)
quotient_cases = 0
for q in (6, 10, 12, 28, 55):
    v, k = q*q+q+1, q+1
    for sample in range(12):
        sample_set = rng.sample(range(v), k)
        for d in divisors(v):
            occupancy = Counter(x % d for x in sample_set)
            by_pairs = Counter((x-y) % d for x in sample_set for y in sample_set)
            by_occupancy = [sum(occupancy[i]*occupancy[(i-r) % d]
                                for i in occupancy) for r in range(d)]
            assert by_occupancy == [by_pairs[r] for r in range(d)]
            assert sum(by_occupancy) == k*k
            quotient_cases += 1
RESULT["quotient_contraction"] = {"q": [6, 10, 12, 28, 55],
    "random_subsets_per_q": 12, "divisor_cases": quotient_cases, "passed": True}
checkpoint("quotient_contraction", RESULT["quotient_contraction"])

norm_residue_pairs = 0
norm_primes = []
for p in range(2, 258):
    if p % 3 != 2 or factors(p) != {p: 1}:
        continue
    norm_primes.append(p)
    roots = [(x, y) for x in range(p) for y in range(p)
             if (x*x-x*y+y*y) % p == 0]
    assert roots == [(0, 0)]
    norm_residue_pairs += p*p
for x in range(-50, 51):
    for y in range(-50, 51):
        value = x*x-x*y+y*y
        if value:
            assert all(e % 2 == 0 for p, e in factors(value).items() if p % 3 == 2)
RESULT["norm_local_obstruction"] = {"primes_2_mod_3_through_257": norm_primes,
    "residue_pairs": norm_residue_pairs, "integer_box": [-50, 50], "passed": True}
checkpoint("norm_local_obstruction", RESULT["norm_local_obstruction"])

occupancy_summary = []
for q in range(1, 201, 3):
    k, h = q+1, (q*q+q+1)//3
    direct = {(a, b, k-a-b) for a in range(k+1) for b in range(k-a+1)
              if a*a+b*b+(k-a-b)**2 == q+h}
    norm_based = set()
    bound = isqrt(4*q//3)+1
    for x in range(-bound, bound+1):
        for y in range(-bound, bound+1):
            if x*x-x*y+y*y != q or (k-x-y) % 3:
                continue
            c = (k-x-y)//3
            a, b = c+x, c+y
            if min(a, b, c) >= 0:
                norm_based.add((a, b, c))
    assert direct == norm_based
    for a, b, c in direct:
        assert a*b+b*c+c*a == h
    occupancy_summary.append({"q": q, "vectors": len(direct)})
    if q in (10, 55):
        assert not direct
RESULT["occupancy_vs_norm"] = {"q_1_mod_3_min": 1, "q_max": 199,
    "results": occupancy_summary, "passed": True}
checkpoint("occupancy_vs_norm", {"cases": len(occupancy_summary), "passed": True})

orbit_cases = 0
for v in range(3, 172, 2):
    generators = [g for g in (2, 3, 5, 7, 11) if gcd(g, v) == 1]
    strata = predicted_strata(v, generators)
    actual = {d: Counter() for d in divisors(v)}
    unseen = set(range(v))
    while unseen:
        x = min(unseen)
        orbit = {x}
        pending = deque([x])
        while pending:
            a = pending.popleft()
            for g in generators:
                b = a*g % v
                if b not in orbit:
                    orbit.add(b)
                    pending.append(b)
        assert orbit <= unseen
        unseen.difference_update(orbit)
        d = v//gcd(x, v)
        assert all(v//gcd(a, v) == d for a in orbit)
        actual[d][len(orbit)] += 1
    for d, info in strata.items():
        assert actual[d] == {info["length"]: info["count"]}
    assert strata[1] == {"length": 1, "count": 1}
    orbit_cases += 1
RESULT["direct_small_orbits"] = {"odd_moduli_min": 3, "odd_moduli_max": 171,
    "cases": orbit_cases, "generators": "2,3,5,7,11 when coprime to modulus",
    "passed": True}
checkpoint("direct_small_orbits", RESULT["direct_small_orbits"])

saved_residual = json.loads((ROOT/"problems/2020-B4/computations/residual-orders.json").read_text())
residuals = []
for saved in saved_residual["results"]:
    q = saved["q"]
    v = q*q+q+1
    generators = list(factors(q))
    strata = predicted_strata(v, generators)
    hist = histogram(strata)
    assert sum(length*count for length, count in hist.items()) == v
    expected_hist = {int(length): count for length, count in saved["orbit_length_histogram"].items()}
    assert hist == expected_hist
    is_reachable = reachable(hist, q+1)
    assert is_reachable == saved["size_q_plus_one_reachable"]
    assert len(closure(generators, v)) == saved["multiplier_group_order"]
    residuals.append({"q": q, "v": v, "v_factors": factors(v),
        "strata": strata, "histogram": hist, "size_reachable": is_reachable,
        "matches_saved": True})
    checkpoint("residual_orbits", {"q": q, "matches_saved": True,
               "size_reachable": is_reachable})
RESULT["residual_orbits"] = residuals


def multiplicative_order_by_loop(x, modulus):
    if modulus == 1:
        return 1
    assert gcd(x, modulus) == 1
    value, power = x % modulus, 1
    while value != 1:
        value = value*x % modulus
        power += 1
        assert power <= modulus
    return power


ancillary = []
for saved in saved_residual["results"]:
    q, v = saved["q"], saved["v"]
    rows = []
    for p, exponent in factors(v).items():
        if exponent != 1:
            continue
        h = v//p
        assert gcd(p, h) == 1
        for m in factors(q):
            s = multiplicative_order_by_loop(m, h)
            t = pow(m, s, v)
            o = multiplicative_order_by_loop(t, p)
            if o == 1:
                continue
            solutions = [[a, q+1-a*o] for a in range((q+1)//o+1)
                if 0 <= q+1-a*o <= h
                and (q+1-a*o)*(q-a*o) <= h-1
                and a*o*(o-1) <= p-1]
            rows.append({"p": p, "h": h, "m": m, "s": s,
                "m_to_s_mod_v": t, "o": o,
                "nonnegative_solutions_a_b": solutions, "excluded": not solutions})
    assert rows == saved["Arasu_Gordon_diagnostics"]
    ancillary.append({"q": q, "rows": rows, "matches_saved": True})
RESULT["ancillary_arasu"] = ancillary
# Source's literal 'positive' cannot be used to discard b=0. This arithmetic
# model is enough to flag the distinction without constructing a difference set.
assert [1, 0] in [[a, 3-3*a] for a in range(2)
                 if 0 <= 3-3*a <= 1 and (3-3*a)*(2-3*a) <= 0
                 and a*3*2 <= 6]
RESULT["ancillary_zero_case"] = {"parameters": {"p": 7, "h": 1, "k": 3, "o": 3},
    "nonnegative_solution": [1, 0], "passed": True}
checkpoint("ancillary_arasu", {"cases": len(ancillary), "matches_saved": True,
    "zero_case_retained": True})

RESULT["square_descent_arithmetic"] = {"q": 2304, "m": 48,
    "m_squared_equals_q": 48*48 == 2304, "three_divides_m_once": 48 % 3 == 0 and 48 % 9 != 0,
    "m_not_three": 48 != 3}
assert all(v for key, v in RESULT["square_descent_arithmetic"].items() if isinstance(v, bool))
RESULT["elapsed_seconds"] = time.monotonic()-START
RESULT["all_checks_passed"] = True
output = HERE/"initial-review-2-evidence.json"
output.write_text(json.dumps(RESULT, indent=2, sort_keys=True)+"\n")
checkpoint("complete", {"all_checks_passed": True, "output": str(output)})
