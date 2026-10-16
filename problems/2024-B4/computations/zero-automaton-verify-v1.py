#!/usr/bin/env python3
"""Second implementation of the fixed-factor zero-set certificate.

This implementation does not import the constructor.  It uses polynomial
supports and complete sets of vectors for subspaces, without Gaussian
elimination.  It then checks the entire closed graph, a quotient graph,
and finite (explicitly nonproof) coefficient evidence.
"""

import hashlib
import json
import os
import platform
import time
from collections import deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
GRAPH = HERE / 'zero-automaton-v1-graph.json'
OUT = HERE / 'zero-automaton-v1-verification.json'
ZERO = frozenset()


def expand_span(rows):
    vectors = {ZERO}
    for row in rows:
        vectors.update(vector ^ row for vector in tuple(vectors))
    return frozenset(vectors)


def product(p, q):
    answer = set()
    for i, j in p:
        for a, b in q:
            term = (i + a, j + b)
            if term in answer:
                answer.remove(term)
            else:
                answer.add(term)
    return frozenset(answer)


def section(p, r, t):
    return frozenset(((i - r) // 2, (j - t) // 2)
                     for i, j in p if i % 2 == r and j % 2 == t)


def independent_transition(space, r):
    # Reconstruct the denominator from its displayed Laurent expression.
    denominator = frozenset({(0, 0), (2, 0), (3, 1), (3, -1), (4, 2)})
    # Use every vector, rather than the constructor's RREF basis.
    return expand_span(section(product(p, denominator), r, t)
                       for p in space for t in (0, 1))


def actual_bridge_checks():
    # A separate support implementation over GF(2)[x,y,z].
    def multiply(p, q):
        answer = set()
        for a in p:
            for b in q:
                term = tuple(a[k] + b[k] for k in range(3))
                answer.symmetric_difference_update({term})
        return frozenset(answer)

    def square(p):
        return frozenset(tuple(2 * a for a in term) for term in p)

    def monomial(variable, power):
        return frozenset({tuple(power if k == variable else 0 for k in range(3))})

    x, y, z = (monomial(k, 1) for k in range(3))
    q = square(x) ^ square(y) ^ square(z) ^ multiply(x, y) ^ multiply(y, z) ^ multiply(z, x)
    r = multiply(multiply(x ^ y, y ^ z), z ^ x)
    d = multiply(multiply(multiply(x, y), z), x ^ y ^ z)
    u = square(r)
    leading = [max(p) for p in (q, u, d)]
    assert leading == [(2, 0, 0), (4, 2, 0), (2, 1, 1)]
    # The rows are the exponent vectors; determinant is unchanged by transpose.
    a, b, c = leading
    determinant = (a[0] * (b[1]*c[2] - b[2]*c[1])
                   - a[1] * (b[0]*c[2] - b[2]*c[0])
                   + a[2] * (b[0]*c[1] - b[1]*c[0]))
    assert determinant == 4
    zero_relations = []
    for variable in range(3):
        residual = (monomial(variable, 8)
                    ^ multiply(square(q), monomial(variable, 4))
                    ^ multiply(u, monomial(variable, 2)) ^ square(d))
        assert not residual
        zero_relations.append(True)
    return {'leading_monomial_exponents_Q_R2_D': leading,
            'exponent_matrix_determinant_over_Z': determinant,
            'squared_quartic_zero_for_each_of_x_y_z': zero_relations,
            'limitation': 'Finite polynomial identities support the separate general injectivity/integrality/normality argument; they do not themselves prove divisibility descent.'}


def main():
    start = time.monotonic()
    print('candidate proof - unverified; second implementation is not an independent reviewer', flush=True)
    print('PID', os.getpid(), 'Python', platform.python_version(), 'standard library only', flush=True)
    graph = json.loads(GRAPH.read_text())
    assert graph['complete']
    monomials = tuple(tuple(p) for p in graph['monomial_bit_order'])
    assert monomials == tuple((i, j) for i in range(4) for j in (-1, 0, 1, 2))

    def decode(mask):
        assert 0 <= mask < 1 << 16
        return frozenset(term for k, term in enumerate(monomials) if mask >> k & 1)

    def encode(p):
        return sum(1 << monomials.index(term) for term in p)

    # All 64 operator columns, including negative b exponents, are rebuilt.
    denominator = frozenset({(0, 0), (2, 0), (3, 1), (3, -1), (4, 2)})
    for r in (0, 1):
        for t in (0, 1):
            for column, monomial in enumerate(monomials):
                transformed = section(product(frozenset({monomial}), denominator), r, t)
                assert transformed <= frozenset(monomials)
                assert encode(transformed) == graph['operators_columns'][f'{r}{t}'][column]
    print('All 64 operator columns match direct Laurent-polynomial multiplication/section.', flush=True)

    spaces = []
    for rows in graph['states_rref']:
        pivots = [row.bit_length() - 1 for row in rows]
        assert pivots == sorted(pivots, reverse=True)
        assert len(pivots) == len(set(pivots))
        assert all(((row >> pivot) & 1) == int(i == j)
                   for i, row in enumerate(rows) for j, pivot in enumerate(pivots))
        space = expand_span(map(decode, rows))
        assert len(space) == 1 << len(rows)
        spaces.append(space)
    assert len(set(spaces)) == 48
    assert len(graph['transitions']) == 48
    assert spaces[0] == expand_span([frozenset({(0, 0), (1, 0), (2, 1)})])

    independent_spaces = [spaces[0]]
    independent_lookup = {spaces[0]: 0}
    independent_edges = []
    for index, space in enumerate(independent_spaces):
        row = []
        for r in (0, 1):
            target = independent_transition(space, r)
            assert all(p <= frozenset(monomials) for p in target)
            if target not in independent_lookup:
                independent_lookup[target] = len(independent_spaces)
                independent_spaces.append(target)
            row.append(independent_lookup[target])
        independent_edges.append(row)
        assert independent_spaces[index] == spaces[index]
        assert row == graph['transitions'][index]
        expected_acceptance = all(not any(i == 0 for i, j in p) for p in space)
        assert expected_acceptance == graph['accepting'][index]
        if (index + 1) % 12 == 0:
            print('Rebuilt', index + 1, 'subspace states and both outgoing transitions.', flush=True)
    assert len(independent_spaces) == len(spaces) == len(independent_edges)
    print('Independent full-span BFS closes at the same 48 states and 96 edges.', flush=True)

    # Moore refinement uses only the now-reconstructed graph.
    classes = [int(a) for a in graph['accepting']]
    rounds = 0
    while True:
        keys = [(classes[i], classes[a], classes[b])
                for i, (a, b) in enumerate(independent_edges)]
        names = {key: i for i, key in enumerate(sorted(set(keys)))}
        refined = [names[key] for key in keys]
        rounds += 1
        if refined == classes:
            break
        assert rounds <= len(spaces)
        classes = refined
    assert len(set(classes)) == 8
    members = [[i for i, c in enumerate(classes) if c == cls]
               for cls in sorted(set(classes))]
    quotient = []
    for group in members:
        i = group[0]
        transitions = [classes[a] for a in independent_edges[i]]
        assert all([classes[a] for a in independent_edges[j]] == transitions for j in group)
        assert all(graph['accepting'][j] == graph['accepting'][i] for j in group)
        quotient.append({'class': classes[i], 'members': group,
                         'accepting': graph['accepting'][i], 'transitions': transitions})
    expected = [[0, 0], [0, 2], [3, 0], [0, 5], [4, 0], [6, 0], [7, 0], [4, 3]]
    assert [q['transitions'] for q in quotient] == expected
    assert [q['accepting'] for q in quotient] == [False]*4 + [True]*4
    assert classes[0] == 1
    print('Exact quotient graph has eight states; candidate LSB language 101(0011)*0*.', flush=True)

    def accepted(index):
        state = 0
        while index:
            state = independent_edges[state][index & 1]
            index >>= 1
        return graph['accepting'][state]

    # Exact finite Laurent recurrence.  Fixed offset is ample: every step
    # can lower a b exponent by at most 1 and there are at most horizon steps.
    horizon = 65535
    offset = horizon + 2
    history = [0] * 4
    zeros = []
    for index in range(horizon + 1):
        value = (1 << offset) if index in (0, 1) else ((1 << (offset + 1)) if index == 2 else 0)
        if index >= 2:
            value ^= history[(index - 2) % 4]
        if index >= 3:
            previous = history[(index - 3) % 4]
            value ^= (previous << 1) ^ (previous >> 1)
        if index >= 4:
            value ^= history[(index - 4) % 4] << 2
        history[index % 4] = value
        assert accepted(index) == (value == 0), index
        if not value:
            zeros.append(index)
        if index and index % 16384 == 0:
            print('Finite recurrence comparisons through j =', index, flush=True)
    expected_zeros = []
    m = 0
    while (j := (32 * 16**m - 7) // 5) <= horizon:
        expected_zeros.append(j)
        m += 1
    assert zeros == expected_zeros
    print('Finite recurrence evidence through j =', horizon, 'zeros =', zeros, flush=True)
    bridge = actual_bridge_checks()
    print('Actual-ring leading monomials and all three squared-quartic identities pass.', flush=True)
    report = {
        'status': 'candidate proof - unverified; two fresh independent adversarial audits required',
        'dependencies': 'Python standard library only',
        'python': platform.python_version(), 'pid': os.getpid(),
        'method': 'Second implementation uses polynomial supports and complete vector sets; no constructor import and no Gaussian elimination.',
        'all_64_operator_columns_match': True,
        'all_48_states_rebuilt_by_independent_bfs': True,
        'all_96_transitions_match': True,
        'all_acceptance_outputs_match': True,
        'canonical_basis_checks': True,
        'moore_refinement_rounds_including_fixed_round': rounds,
        'quotient_initial_class': classes[0],
        'quotient_classes': quotient,
        'candidate_exact_lsb_language': '101(0011)*0*',
        'candidate_canonical_lsb_language': '101(0011)*',
        'finite_recurrence_evidence_only': {'j_interval_inclusive': [0, horizon],
                                           'zero_indices': zeros,
                                           'all_indices_match_graph': True,
                                           'laurent_offset': offset},
        'actual_bridge_finite_checks': bridge,
        'elapsed_seconds': time.monotonic() - start,
        'input_graph_sha256': hashlib.sha256(GRAPH.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('Wrote', OUT.name, 'SHA256', hashlib.sha256(OUT.read_bytes()).hexdigest(), flush=True)


if __name__ == '__main__':
    main()
