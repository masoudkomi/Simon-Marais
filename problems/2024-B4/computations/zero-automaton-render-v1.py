#!/usr/bin/env python3
"""Render the complete finite exact certificate as a readable Markdown table."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GRAPH = HERE / 'zero-automaton-v1-graph.json'
VERIFY = HERE / 'zero-automaton-v1-verification.json'
DESTINATION = HERE.parent / 'notes' / 'zero-automaton-certificate-v1.md'
graph = json.loads(GRAPH.read_text())
verified = json.loads(VERIFY.read_text())
assert graph['complete'] and verified['all_96_transitions_match']
assert verified['input_graph_sha256'] == hashlib.sha256(GRAPH.read_bytes()).hexdigest()
class_names = ['X', 'S', 'A', 'B', 'Z', 'C', 'D', 'E']
classes = {state: class_names[entry['class']]
           for entry in verified['quotient_classes'] for state in entry['members']}
lines = [
    '# Complete 48-state fixed-factor certificate, v1',
    '',
    '**Candidate proof - unverified.** Generated 2026-10-16. This is an exact',
    'finite algebraic certificate supporting `zero-automaton-criterion-v1.md`.',
    'A second implementation is not an independent adversarial agent review.',
    '',
    'All integers encode F2 vectors. Bit k represents the monomial in row k',
    'of the first table; XOR is vector addition. A listed basis has descending',
    'pivot bits, and every pivot bit is zero in the other rows. The full',
    'subspace consists of all XOR sums of subsets of that basis.',
    '',
    'The denominator is K=1+z^2+(b+b^-1)z^3+b^2*z^4. Each operator column',
    'is the encoded numerator C_(r,t)(monomial*K). Both parity residues are',
    'in {0,1}, including for negative b exponents. The bit reading order',
    'for state transitions is least significant first.',
    '',
    '| Bit | z exponent | b exponent | L00 column | L01 column | L10 column | L11 column |',
    '|---:|---:|---:|---:|---:|---:|---:|',
]
for bit, (i, j) in enumerate(graph['monomial_bit_order']):
    columns = [graph['operators_columns'][key][bit] for key in ('00', '01', '10', '11')]
    lines.append('| ' + ' | '.join(map(str, [bit, i, j, *columns])) + ' |')
lines += [
    '',
    'The initial state is state 0, span(1058)=span(1+z+b*z^2). To compute',
    'the r successor, apply L_(r,0) and L_(r,1) to each listed basis row',
    'and span the resulting vectors. A state accepts exactly when every',
    'basis row has zero bottom four bits, i.e. no z^0 coefficient.',
    '',
    '| State | Basis row masks | 0 successor | 1 successor | Accept? | Quotient class |',
    '|---:|---|---:|---:|---|---|',
]
for state, rows in enumerate(graph['states_rref']):
    zero, one = graph['transitions'][state]
    lines.append(f'| {state} | ' + ', '.join(map(str, rows))
                 + f' | {zero} | {one} | ' + ('yes' if graph['accepting'][state] else 'no')
                 + f' | {classes[state]} |')
lines += [
    '',
    'Every row and both outgoing transitions were reconstructed by the',
    'separate full-subspace implementation, which enumerates all vectors',
    'rather than performing Gaussian elimination. Its largest full space',
    'has 64 vectors, including zero. The 48 spaces are distinct and the',
    'graph is transition-closed. The quotient table and its unrestricted',
    'language argument appear in the candidate theorem note.',
    '',
    'Input graph SHA256: `' + hashlib.sha256(GRAPH.read_bytes()).hexdigest() + '`.',
    '',
    'Verification report SHA256: `' + hashlib.sha256(VERIFY.read_bytes()).hexdigest() + '`.',
    '',
    'Renderer source SHA256: `' + hashlib.sha256(Path(__file__).read_bytes()).hexdigest() + '`.',
    '',
]
DESTINATION.write_text('\n'.join(lines))
print('Wrote', DESTINATION)
print('SHA256', hashlib.sha256(DESTINATION.read_bytes()).hexdigest())
