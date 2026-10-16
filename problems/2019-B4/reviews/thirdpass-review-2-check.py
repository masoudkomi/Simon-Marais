#!/usr/bin/env python3
"""Independent adversarial check, written before inspecting constructor code.

Only the frozen mathematical description and previously accepted definitions
were inputs. Queue updates use emit/consume operations, not a copied table.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import platform
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent


def pulse(event, **kw):
    print(json.dumps({"event": event, "elapsed": time.monotonic()-START, **kw}), flush=True)


def pi(word, phase=0):
    tapes = [[], []]
    for t, letter in enumerate(word):
        tapes[letter == 'R'].append((t+phase) % 2)
    return tuple(map(tuple, tapes))


def segments(word, D):
    """Independent grid oracle: all candidate factors and legal upper paths.

    For each segment, legal edges read its actual fixed tapes at source time.
    DP counts strictly upper partial witnesses, killed on premature return.
    """
    for begin in range(len(word)):
        for end in range(begin+1, len(word)+1):
            part = word[begin:end]
            left, right = pi(part, begin % 2)
            hleft = 0
            active = {0}
            for t, move in enumerate(part):
                hleft += (move == 'L')
                nxt = set()
                for i in active:
                    j = t-i
                    for side in (0, 1):
                        tape, pos = (left, i) if side == 0 else (right, j)
                        if pos >= len(tape) or tape[pos] != (begin+t) % 2:
                            continue
                        ni = i + (side == 0)
                        gap = ni-hleft
                        if t+1 == len(part):
                            if gap == 0:
                                # first differing move is enforced by positive
                                # intermediate gaps, except the impossible n=1.
                                if len(part) > 1:
                                    return (begin, end)
                        elif 1 <= gap <= D:
                            nxt.add(ni)
                active = nxt
                if not active:
                    break
    return None


def competitor(pair, hmove, gmove, D):
    """A simultaneous step by generic FIFO consumption and emission."""
    u, v = map(list, pair)
    if hmove == 'L':
        if not u or u.pop(0) != 0:
            return None
    else:
        v.append(0)
    if gmove == 'R':
        if not v or v.pop(0) != 0:
            return None
    else:
        u.append(0)
    assert len(u) == len(v)
    if len(u) > D:
        return None
    if not u:
        return 'RETURN'
    return (tuple(1-x for x in u), tuple(1-x for x in v))


def step(state, letter, D):
    new = set()
    for pair in state:
        for other in 'LR':
            value = competitor(pair, letter, other, D)
            if value == 'RETURN':
                return None
            if value is not None:
                new.add(value)
    if letter == 'R':
        new.add(((1,), (1,)))
    return frozenset(new)


def build(D, cap=30000):
    states = [frozenset()]
    index = {states[0]: 0}
    trans = []
    for state in states:
        row = []
        for letter in 'LR':
            nxt = step(state, letter, D)
            if nxt is None:
                row.append(-1)
            else:
                if nxt not in index:
                    assert len(states) < cap, ('CAP', D, len(states))
                    index[nxt] = len(states)
                    states.append(nxt)
                row.append(index[nxt])
        trans.append(row)
        if len(trans) % 2000 == 0:
            pulse('build', D=D, processed=len(trans), discovered=len(states))
    pulse('built', D=D, raw_states=len(states), max_active=max(map(len, states)))
    return states, trans


def minimize(rows):
    n = len(rows)
    complete = [[j if j >= 0 else n for j in row] for row in rows]+[[n, n]]
    part = [0]*n+[1]
    rounds = 0
    while True:
        signatures = {}
        new = []
        for i, row in enumerate(complete):
            sig = (i == n, part[row[0]], part[row[1]])
            if sig not in signatures:
                signatures[sig] = len(signatures)
            new.append(signatures[sig])
        rounds += 1
        if new == part:
            break
        part = new
    reps = {}
    for i, block in enumerate(part):
        reps.setdefault(block, i)
    blocks = [part[0]]
    bindex = {blocks[0]: 0}
    minimal = []
    for block in blocks:
        row = []
        for letter in range(2):
            target = part[complete[reps[block]][letter]]
            if target == part[n]:
                row.append(-1)
            else:
                if target not in bindex:
                    bindex[target] = len(blocks)
                    blocks.append(target)
                row.append(bindex[target])
        minimal.append(row)
    pulse('minimized', states=len(minimal), rounds=rounds)
    return minimal, [bindex.get(part[i], -1) for i in range(n)]


def accepted(rows, word):
    state = 0
    for letter in word:
        state = rows[state][letter == 'R']
        if state < 0:
            return False
    return True


def mf_machine(rows):
    # Initial state is separate because the suffix omits the first letter.
    # Terminal 1 is accepting and has no outgoing successful continuation.
    states = [('INITIAL',), ('TERMINAL',)]
    index = {value: i for i, value in enumerate(states)}
    transitions = []
    for current in states:
        row = []
        for letter in range(2):
            if current == ('TERMINAL',):
                row.append(-1)
                continue
            if current == ('INITIAL',):
                p, q = rows[0][letter], 0
            else:
                p, q = (rows[current[0]][letter], rows[current[1]][letter])
            if q < 0:
                row.append(-1)
            elif p < 0:
                row.append(1)
            else:
                pair = (p, q)
                if pair not in index:
                    index[pair] = len(states)
                    states.append(pair)
                row.append(index[pair])
        transitions.append(row)
    return states, transitions


def grammar_nfa():
    # Thompson-free word-labelled graph expanded to fresh private paths.
    adj = collections.defaultdict(lambda: collections.defaultdict(set))
    nextstate = 4
    def path(src, dst, word):
        nonlocal nextstate
        for i, letter in enumerate(word):
            dest = dst if i+1 == len(word) else nextstate
            if dest == nextstate:
                nextstate += 1
            adj[src][letter == 'R'].add(dest)
            src = dest
    # 0 start; 1 accept; 2 loop junction; 3 spare (no epsilon needed).
    path(0, 1, 'RRLL')
    path(0, 2, 'RRLRRLRL')
    for word in ('RRLRL', 'LRLRL', 'LRLRRLRL'):
        path(2, 2, word)
    path(2, 1, 'LRLL')
    return adj, 0, 1


def grammar_equivalence(rows):
    states, mf = mf_machine(rows)
    adj, start, final = grammar_nfa()
    pairs = [(0, frozenset([start]))]
    seen = {pairs[0]}
    for p, subset in pairs:
        assert (p == 1) == (final in subset), ('grammar mismatch', p, sorted(subset))
        for letter in range(2):
            q = mf[p][letter] if p >= 0 else -1
            target = frozenset(x for i in subset for x in adj[i][letter])
            pair = q, target
            if pair not in seen:
                seen.add(pair)
                pairs.append(pair)
    coaccessible = {1}
    while True:
        more = coaccessible | {i for i, row in enumerate(mf) if any(j in coaccessible for j in row)}
        if more == coaccessible:
            break
        coaccessible = more
    pulse('grammar_verified', product_pairs=len(pairs), mf_states=len(states), trim_states=len(coaccessible))
    return {'equivalent': True, 'product_pairs': len(pairs), 'mf_states': len(states),
            'trim_states': len(coaccessible),
            'trim_graph': {str(i): {'state': states[i], 'LR': row} for i, row in enumerate(mf) if i in coaccessible}}


def small_oracle(rows, D, maxn):
    counts = []
    examined = 0
    for n in range(maxn+1):
        count = 0
        for letters in itertools.product('LR', repeat=n):
            word = ''.join(letters)
            expected = segments(word, D) is None
            actual = accepted(rows, word)
            assert expected == actual, ('grid mismatch', D, word, expected, actual)
            count += actual
            examined += 1
        counts.append(count)
        pulse('grid_length', D=D, n=n, words=2**n, accepted=count)
    return {'D': D, 'maxn': maxn, 'examined': examined, 'counts': counts}


def vector(rows, power=200):
    v = [1]*len(rows)
    for k in range(power):
        v = [sum(v[j] for j in row if j >= 0) for row in rows]
    av = [sum(v[j] for j in row if j >= 0) for row in rows]
    slack = [1834856083*x-1000000000*y for x, y in zip(v, av)]
    assert min(v) > 0 and min(slack) > 0
    pulse('all_row_signs', rows=len(rows), min_slack=str(min(slack)))
    return v, {'power': power, 'positive_entries': len(v), 'strict_rows': len(slack),
               'min_slack': str(min(slack)), 'min_slack_index': slack.index(min(slack)),
               'p': 1834856083, 'q': 1000000000}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--D', type=int, required=True)
    parser.add_argument('--grid', type=int, default=0)
    parser.add_argument('--grammar', action='store_true')
    parser.add_argument('--vector', action='store_true')
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    START = time.monotonic()
    raw, trans = build(args.D)
    rows, partition = minimize(trans)
    result = {'provenance': 'independent implementation before reading constructor code/tables',
              'python': platform.python_version(), 'D': args.D, 'complete': True,
              'raw_states': len(raw), 'max_active': max(map(len, raw)),
              'states': len(rows), 'transitions': rows, 'raw_transitions': trans,
              'partition': partition}
    if args.grid:
        result['grid'] = small_oracle(rows, args.D, args.grid)
    if args.grammar:
        result['grammar'] = grammar_equivalence(rows)
    if args.vector:
        result['vector'], result['signs'] = vector(rows)
    pathlib.Path(args.out).write_text(json.dumps(result, indent=2)+'\n')
    pulse('complete', out=args.out)
