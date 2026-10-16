#!/usr/bin/env python3
"""Candidate zero-set automaton, exact standard-library GF(2) arithmetic.

Builds a bounded reachable graph of linear subspaces of a 16-dimensional
Laurent-polynomial numerator space.  Closure is reported explicitly;
an incomplete graph supplies no complete zero-set classification.
"""

import argparse
import hashlib
import json
import os
import platform
import time
from pathlib import Path


HERE = Path(__file__).resolve().parent
MONOMIALS = tuple((i, j) for i in range(4) for j in range(-1, 3))
INDEX = {term: index for index, term in enumerate(MONOMIALS)}
K = ((0, 0), (2, 0), (3, -1), (3, 1), (4, 2))


def encode(terms):
    answer = 0
    for term in terms:
        answer ^= 1 << INDEX[term]
    return answer


def basis(rows):
    """Unique reduced binary row basis, descending leading-bit order."""
    pivots = {}
    for row in rows:
        for pivot in sorted(pivots, reverse=True):
            if row >> pivot & 1:
                row ^= pivots[pivot]
        if row:
            pivot = row.bit_length() - 1
            for old in tuple(pivots):
                if pivots[old] >> pivot & 1:
                    pivots[old] ^= row
            pivots[pivot] = row
    return tuple(pivots[pivot] for pivot in sorted(pivots, reverse=True))


def make_operators():
    operators = {}
    for r in (0, 1):
        for t in (0, 1):
            columns = []
            for i, j in MONOMIALS:
                terms = []
                for a, b in K:
                    if (i + a) % 2 == r and (j + b) % 2 == t:
                        term = ((i + a - r) // 2, (j + b - t) // 2)
                        assert term in INDEX, (r, t, (i, j), term)
                        terms.append(term)
                columns.append(encode(terms))
            operators[(r, t)] = tuple(columns)
    return operators


def linear_image(row, columns):
    result = 0
    while row:
        bit = row & -row
        result ^= columns[bit.bit_length() - 1]
        row ^= bit
    return result


def transition(state, r, operators):
    return basis(linear_image(row, operators[(r, t)])
                 for row in state for t in (0, 1))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--state-cap', type=int, default=20000)
    parser.add_argument('--seconds', type=float, default=40.0)
    parser.add_argument('--prefix', default='zero-automaton-v1')
    args = parser.parse_args()
    start = time.monotonic()
    print('candidate proof - unverified; no independent reviews', flush=True)
    print(json.dumps({'pid': os.getpid(), 'python': platform.python_version(),
                      'state_cap': args.state_cap, 'internal_seconds': args.seconds,
                      'dependencies': 'Python standard library only'}), flush=True)
    operators = make_operators()
    initial = basis([encode(((0, 0), (1, 0), (2, 1)))])
    states = [initial]
    lookup = {initial: 0}
    edges = []
    complete = True
    stop_reason = 'transition-closed reachable graph'
    cursor = 0
    next_report = start + 2
    while cursor < len(states):
        if time.monotonic() - start >= args.seconds:
            complete = False
            stop_reason = 'internal time bound'
            break
        row_edges = []
        for r in (0, 1):
            target = transition(states[cursor], r, operators)
            if target not in lookup:
                if len(states) >= args.state_cap:
                    complete = False
                    stop_reason = 'state cap'
                    break
                lookup[target] = len(states)
                states.append(target)
            row_edges.append(lookup[target])
        if not complete:
            break
        edges.append(row_edges)
        cursor += 1
        if time.monotonic() >= next_report or cursor % 1000 == 0:
            print(json.dumps({'processed': cursor, 'discovered': len(states),
                              'elapsed_seconds': time.monotonic() - start}), flush=True)
            next_report = time.monotonic() + 2
    constant_mask = (1 << 4) - 1
    accepts = [all(row & constant_mask == 0 for row in state) for state in states]
    dimensions = {}
    for state in states:
        dimensions[str(len(state))] = dimensions.get(str(len(state)), 0) + 1
    result = {
        'status': 'candidate proof - unverified; no independent adversarial audits',
        'complete': complete,
        'stop_reason': stop_reason,
        'elapsed_seconds': time.monotonic() - start,
        'parameters': vars(args),
        'monomial_bit_order': [list(term) for term in MONOMIALS],
        'k_monomials': [list(term) for term in K],
        'operators_columns': {f'{r}{t}': list(columns)
                              for (r, t), columns in operators.items()},
        'initial_state': 0,
        'binary_read_order': 'least significant bit first; empty word represents j=0',
        'states_rref': [list(state) for state in states],
        'transitions': edges,
        'accepting': accepts,
        'discovered_state_count': len(states),
        'processed_state_count': cursor,
        'dimension_counts': dimensions,
        'accepting_state_count': sum(accepts),
        'script_sha256': digest(Path(__file__)),
        'dependencies': 'Python standard library only',
        'python': platform.python_version(),
        'pid': os.getpid(),
        'interpretation': 'Acceptance concerns the identically zero formal Laurent coefficient of (1+z+b*z^2)/K; no claim about other factors or full B4(b).',
    }
    destination = HERE / (args.prefix + '-graph.json')
    destination.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in (
        'complete', 'stop_reason', 'elapsed_seconds', 'discovered_state_count',
        'processed_state_count', 'dimension_counts', 'accepting_state_count')}), flush=True)
    print('Wrote', destination.name, 'SHA256', digest(destination), flush=True)


if __name__ == '__main__':
    main()
