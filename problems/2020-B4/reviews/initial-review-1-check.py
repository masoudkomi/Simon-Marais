#!/usr/bin/env python3
"""Independent finite checks for the frozen 2020 B4(b) partial package.

This file is review evidence, not a proof of the unrestricted classification.
Uses only the Python standard library. Run through initial-review-1-run.py.
"""

from collections import Counter, deque
from datetime import datetime, timezone
from itertools import combinations
from math import gcd, isqrt
from pathlib import Path
import importlib.util
import json
import os
import platform
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
REVIEW = Path(__file__).resolve().parent
COMPUTATIONS = ROOT / 'problems/2020-B4/computations'
sys.path.insert(0, str(COMPUTATIONS))
import exact_search as author
import residual_orders as residual

OUT = {'started_utc': datetime.now(timezone.utc).isoformat(),
       'pid': os.getpid(), 'python': platform.python_version(),
       'dependencies': 'Python standard library only',
       'scope': '2020 B4(b); no prime-order preliminary construction',
       'checks': {}}


def checkpoint(name, value):
    OUT['checks'][name] = value
    print(json.dumps({'checkpoint': name, 'result': value}, sort_keys=True), flush=True)
    (REVIEW / 'initial-review-1-evidence.json').write_text(
        json.dumps(OUT, indent=2, sort_keys=True) + '\n')


def factors(n):
    result = {}
    for d in range(2, isqrt(n) + 1):
        if d * d > n:
            break
        if n % d:
            continue
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        result[d] = e
    if n > 1:
        result[n] = 1
    return result


def divisors(n):
    low, high = [], []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            if d * d != n:
                high.append(n // d)
    return low + high[::-1]


def phi(n):
    ans = n
    for p in factors(n):
        ans -= ans // p
    return ans


def group_generated(q, limit=None):
    v = q * q + q + 1
    generators = tuple(factors(q))
    result, frontier = {1}, [1]
    while frontier:
        value = frontier.pop()
        for p in generators:
            new = value * p % v
            if new not in result:
                result.add(new)
                frontier.append(new)
                if limit is not None and len(result) >= limit:
                    return result, False
    return result, True


def diff_counts(D, v):
    return Counter((a - b) % v for a in D for b in D if a != b)


def is_ds(D, v):
    return diff_counts(D, v) == Counter({r: 1 for r in range(1, v)})


def folded_distances_distinct(D, v):
    diffs = [min((a - b) % v, (b - a) % v) for a, b in combinations(D, 2)]
    return len(diffs) == len(set(diffs))


all_sets = 0
valid_q4 = []
for D in combinations(range(21), 5):
    all_sets += 1
    distance_condition = folded_distances_distinct(D, 21)
    difference_condition = is_ds(D, 21)
    assert distance_condition == difference_condition
    if difference_condition:
        valid_q4.append(D)
assert all_sets == 20349
assert len(valid_q4) > 0
checkpoint('P1_all_5_subsets_mod_21', {'subsets_checked': all_sets,
    'difference_sets_found': len(valid_q4), 'equivalence_mismatches': 0})

recorded_small = json.loads((COMPUTATIONS / 'small-search.json').read_text())['results']
witnesses = {r['q']: tuple(r['witness']) for r in recorded_small if r['witness'] is not None}
for q, D in witnesses.items():
    assert q in (1, 4, 8, 9)
    assert len(D) == q + 1 and len(set(D)) == q + 1
    assert is_ds(D, q*q + q + 1)
checkpoint('recorded_witnesses_independent_signed_counts', {'orders': sorted(witnesses),
    'all_valid': True, 'preliminary_prime_orders_constructed': []})

plane_checks = []
for q in (4, 8, 9):
    D = witnesses[q]
    v, k = q*q + q + 1, q + 1
    lines = [frozenset((d+t) % v for d in D) for t in range(v)]
    assert len(set(lines)) == v
    point_line_counts = Counter(x for L in lines for x in L)
    assert set(point_line_counts.values()) == {k}
    assert all(len(L & K) == 1 for L, K in combinations(lines, 2))
    pairs = Counter(pair for L in lines for pair in combinations(sorted(L), 2))
    assert len(pairs) == v*(v-1)//2 and set(pairs.values()) == {1}
    L = lines[0]
    A, B = sorted(L)[:2]
    P = next(x for x in range(v) if x not in L)
    AP = next(K for K in lines if A in K and P in K)
    BP = next(K for K in lines if B in K and P in K)
    union = L | AP | BP
    assert len(union) == 3*q
    Q = next(x for x in range(v) if x not in union)
    assert all(not (set(triple) <= K) for triple in combinations([A,B,P,Q],3) for K in lines)
    plane_checks.append({'q': q, 'v': v, 'four_point_witness': [A,B,P,Q],
                         'triangle_union_size': len(union)})
assert 7 - 3*2 == (2-1)**2 == 1
assert all(gcd(q+1, q*q+q+1) == 1 for q in range(1, 5001))
checkpoint('P2_incidence_and_nondegeneracy', {'incidence_checks': plane_checks,
    'q2_triangle_complement_size': 1, 'q1_has_only_three_points': True,
    'line_stabilizer_coprimality_q1_through_5000': True})

multiplier_checks = 0
normalization_01_checks = 0
full_group_q4 = None
for D in valid_q4:
    v, k = 21, 5
    c = -sum(D) * pow(k, -1, v) % v
    N = frozenset((d+c) % v for d in D)
    assert sum(N) % v == 0
    assert sum(1 for a in range(v) if sum((d+a) % v for d in D) % v == 0) == 1
    for a, b in combinations(D, 2):
        if (a-b) % v == 1:
            S = {(d-b) % v for d in D}
            assert 0 in S and 1 in S
            normalization_01_checks += 1
        elif (b-a) % v == 1:
            S = {(d-a) % v for d in D}
            assert 0 in S and 1 in S
            normalization_01_checks += 1
    translates = {frozenset((d+a) % v for d in D) for a in range(v)}
    mults = []
    for t in range(v):
        if gcd(t, v) != 1:
            continue
        if frozenset(t*d % v for d in D) in translates:
            mults.append(t)
            assert frozenset(t*d % v for d in N) == N
            multiplier_checks += 1
    assert len(mults) == 6
    full_group_q4 = mults
assert normalization_01_checks == len(valid_q4)
checkpoint('P3_simultaneous_normalization', {'all_q4_sets_checked': len(valid_q4),
    'multipliers_checked': multiplier_checks, 'zero_sum_translate_unique': True,
    'all_sets_have_a_translate_containing_0_and_1': True,
    'q4_full_multiplier_group': full_group_q4,
    'q4_exception_exceeds_q_plus_one': len(full_group_q4) > 5})

quotient_cases = 0
for q, D in [(4,D) for D in valid_q4] + list(witnesses.items()):
    v, k = q*q + q + 1, q + 1
    coeffs = Counter((a-b) % v for a in D for b in D)
    assert coeffs == Counter({r: 1 + (q if r == 0 else 0) for r in range(v)})
    for d in divisors(v):
        h = v // d
        a = Counter(x % d for x in D)
        assert sum(a.values()) == k
        assert sum(a[i]*a[i] for i in range(d)) == q+h
        assert all(sum(a[i]*a[(i-r)%d] for i in range(d)) == h for r in range(1,d))
        quotient_cases += 1
checkpoint('P4_quotient_and_group_ring_coefficients', {'quotients_checked': quotient_cases,
    'd1_and_dv_included': True, 'equation_failures': 0})

local_pairs_checked = 0
prime_tests = []
for p in range(2, 100):
    if len(factors(p)) != 1 or factors(p).get(p) != 1 or p % 3 != 2:
        continue
    zeros = [(x,y) for x in range(p) for y in range(p) if (x*x-x*y+y*y) % p == 0]
    assert zeros == [(0,0)]
    local_pairs_checked += p*p
    prime_tests.append(p)
positive_norms_checked = 0
for x in range(-40, 41):
    for y in range(-40, 41):
        q = x*x-x*y+y*y
        if q == 0:
            continue
        assert all(e % 2 == 0 for p,e in factors(q).items() if p % 3 == 2)
        positive_norms_checked += 1
occupancies = []
for q in (10,28,52,55,91,100):
    v, k = q*q+q+1, q+1
    found = []
    for a in range(k+1):
        for b in range(k-a+1):
            c = k-a-b
            if a*a+b*b+c*c == q+v//3:
                assert a*b+b*c+c*a == v//3
                assert (a-c)**2-(a-c)*(b-c)+(b-c)**2 == q
                found.append([a,b,c])
    occupancies.append({'q':q,'count':len(found),'vectors':found})
saved_occupancies = json.loads((COMPUTATIONS/'quotient-counts.json').read_text())['results']
assert all(r['vectors'] == s['count_vectors'] for r,s in zip(occupancies,saved_occupancies))
assert occupancies[0]['count'] == 0
assert [13,9,7] in occupancies[1]['vectors']
checkpoint('P5_norm', {'local_primes_tested': prime_tests,
    'local_pairs_checked': local_pairs_checked, 'positive_integer_norms_checked': positive_norms_checked,
    'occupancy_checks': occupancies, 'q28_occupancy_pass_is_not_existence': [13,9,7]})


def explicit_orbit_histogram(q):
    v = q*q+q+1
    gens = tuple(factors(q))
    seen = bytearray(v)
    hist = Counter()
    for x in range(v):
        if seen[x]:
            continue
        stack = [x]
        seen[x] = 1
        length = 0
        while stack:
            y = stack.pop()
            length += 1
            for g in gens:
                z = y*g % v
                if not seen[z]:
                    seen[z] = 1
                    stack.append(z)
        hist[length] += 1
    assert sum(size*count for size,count in hist.items()) == v
    return dict(sorted(hist.items()))


def arithmetic_histogram(q, group):
    v = q*q+q+1
    hist = Counter()
    for d in divisors(v):
        projected_size = len({a % d for a in group})
        assert phi(d) % projected_size == 0
        hist[projected_size] += phi(d) // projected_size
    return dict(sorted(hist.items()))


def bounded_sums(hist, target):
    reachable = {0}
    for weight,count in hist.items():
        reachable = {old + c*weight for old in reachable
                     for c in range(min(count, (target-old)//weight)+1)}
    return reachable


subset_checks = 0
for w in range(1, 9):
    for c in range(0, 14):
        for z in range(0, 7):
            hist = {w:c, w+1:z}
            good = bounded_sums(hist, 50)
            for target in range(51):
                assert residual.subset_sum(hist, target) == (target in good)
                subset_checks += 1
checkpoint('P6_bounded_subset_sum_algorithm', {'comparisons': subset_checks,
    'zero_multiplicities_and_target_zero_included': True, 'mismatches': 0})

orbit_results = []
for q in (1,4,6,8,9,10,12,323,1944,2304,2435):
    begin = time.monotonic()
    group, complete = group_generated(q)
    assert complete
    expected = arithmetic_histogram(q, group)
    actual = explicit_orbit_histogram(q)
    assert expected == actual == residual.orbit_histogram(q, group)
    reachable = q+1 in bounded_sums(actual, q+1)
    assert reachable == residual.subset_sum(actual, q+1)
    row = {'q':q,'v':q*q+q+1,'histogram':actual,'group_order':len(group),
           'size_q_plus_one_reachable':reachable,
           'elapsed_seconds':round(time.monotonic()-begin,6)}
    orbit_results.append(row)
    checkpoint('P6_orbits_q_'+str(q),row)
assert not orbit_results[-3]['size_q_plus_one_reachable']
assert orbit_results[-2]['size_q_plus_one_reachable']
assert not orbit_results[-1]['size_q_plus_one_reachable']
assert 1+1080+540+360+216+60+36+12 == 2305


def independent_filter_reason(q, fs):
    if q % 4 in (1,2) and any(p % 4 == 3 and e % 2 for p,e in fs.items()):
        return 'Bruck_Ryser'
    if q % 2 == 0 and q > 4 and q % 8:
        return 'Jungnickel_Vedder_even_order'
    if q % 3 == 0 and q != 3 and q % 9:
        return 'Wilbrink_three_divisibility'
    if isqrt(q)**2 != q:
        for r in factors(q*q+q+1):
            assert r % 2 and all(gcd(p,r) == 1 for p in fs)
            for p in fs:
                if pow(p, (r-1)//2, r) != 1:
                    return 'Mann_quadratic_nonresidue'
    return None


tally, remaining, examples = Counter(), [], {}
for q in range(2,5001):
    fs = factors(q)
    assert fs == author.factor(q)
    if len(fs) == 1:
        tally['prime_power_skipped_as_established_context'] += 1
        continue
    reason = independent_filter_reason(q,fs)
    assert reason == author.basic_exclusion(q,fs)
    if reason is None:
        group, complete = group_generated(q,q+2)
        if not complete or len(group) > q+1:
            reason = 'multiplier_group_size_bound'
        elif q <= 500:
            hist = explicit_orbit_histogram(q)
            if q+1 not in bounded_sums(hist,q+1):
                reason = 'multiplier_orbit_size_subset_sum'
    if reason is None:
        remaining.append(q)
        reason = 'not_excluded_by_implemented_filters'
    else:
        examples.setdefault(reason,q)
    tally[reason] += 1
saved_filters = json.loads((COMPUTATIONS/'filters-q5000.json').read_text())['results']
assert dict(tally) == saved_filters['tallies']
assert remaining == saved_filters['residual_non_prime_power_orders']
assert examples == saved_filters['first_example_per_exclusion']
assert sum(tally.values()) == 4999
checkpoint('filters_2_through_5000', {'tallies':dict(tally),'residual_orders':remaining,
    'first_examples':examples,'all_stored_values_agree':True,
    'q4_exception_bypassed_as_prime_power':True})


def independent_arasu(q):
    v, k = q*q+q+1,q+1
    rows=[]
    for p,e in factors(v).items():
        if e != 1:
            continue
        h=v//p
        assert gcd(p,h) == 1
        for m in factors(q):
            if h == 1:
                s=1
            else:
                s,x=1,m % h
                while x != 1:
                    x=x*m % h
                    s+=1
            u=pow(m,s,v)
            o,x=1,u % p
            while x != 1:
                x=x*u % p
                o+=1
            if o <= 1:
                continue
            solutions=[]
            for b in range(min(k,h)+1):
                if (k-b) % o:
                    continue
                a=(k-b)//o
                if b*(b-1) <= h-1 and a*o*(o-1) <= p-1:
                    solutions.append([a,b])
            rows.append({'p':p,'h':h,'m':m,'s':s,'m_to_s_mod_v':u,'o':o,
                         'nonnegative_solutions_a_b':sorted(solutions),
                         'excluded':not solutions})
    return rows


arasu_rows=[]
for q in (4,8,9,1944,2304,2435):
    rows=independent_arasu(q)
    assert rows == residual.arasu_diagnostics(q)
    if q in witnesses:
        assert all(not row['excluded'] for row in rows)
    arasu_rows.append({'q':q,'diagnostics':rows})
zero_row=next(row for row in independent_arasu(8) if row['p']==73 and row['m']==2)
assert zero_row['nonnegative_solutions_a_b']==[[1,0]]
assert zero_row['o']==9 and zero_row['h']==1
zero_shift=-sum(witnesses[8])*pow(9,-1,73) % 73
zero_normalized=sorted((d+zero_shift) % 73 for d in witnesses[8])
assert 0 not in zero_normalized
assert sorted(2*d % 73 for d in zero_normalized)==zero_normalized
checkpoint('Arasu_inequalities_independent_b_first_enumeration', {'results':arasu_rows,
    'actual_q8_requires_b_zero':zero_row,
    'q8_zero_sum_translation':zero_shift,'q8_zero_sum_difference_set':zero_normalized,
    'q2304_no_nontrivial_test_is_retained':independent_arasu(2304)==[]})


def independent_negative_search(n):
    v=n*n-n+1
    nodes=0
    def visit(D, used):
        nonlocal nodes
        nodes+=1
        if len(D)==n:
            return tuple(D)
        for x in range(D[-1]+1,v):
            if v-x < n-len(D):
                break
            new=[(x-y)%v for y in D]+[(y-x)%v for y in D]
            S=set(new)
            if len(S)!=2*len(D) or S & used:
                continue
            ans=visit(D+[x],used|S)
            if ans is not None:
                return ans
        return None
    return visit([0,1],{1,v-1}),nodes


negative,nodes=independent_negative_search(7)
assert negative is None
assert nodes==next(r['nodes'] for r in recorded_small if r['n']==7)
forced_incomplete=author.direct_search(7,10.0,1)
assert forced_incomplete['status']=='incomplete_limit_reached'
checkpoint('finite_negative_search_and_limit_status', {'n':7,'q':6,'independent_nodes':nodes,
    'completed_exhaustively_no_witness':True,
    'forced_node_limit_status':forced_incomplete['status']})

assert 48**2==2304 and 48%3==0 and 48!=3 and 48%9!=0
assert 48**2+48+1 == 2353 and 5310721 % 2353 == 0
checkpoint('square_descent_arithmetic_only', {'q':2304,'descended_order':48,
    'descended_group_order':2353,'cyclic_subgroup_divisibility':True,
    'Wilbrink_hypothesis_v3_of_48':1,
    'theorem_import_not_reproved':True})
OUT['completed_utc']=datetime.now(timezone.utc).isoformat()
OUT['all_assertions_passed']=True
(REVIEW/'initial-review-1-evidence.json').write_text(json.dumps(OUT,indent=2,sort_keys=True)+'\n')
print('COMPLETE all assertions passed',flush=True)
