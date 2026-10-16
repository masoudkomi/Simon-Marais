#!/usr/bin/env python3
"""Independent R1 verifier, written from the candidate's mathematical definitions.

Initial version written before inspecting any third-pass author source or data.
Alphabet 0=L, 1=R. Queues are integers, oldest bit in the low position.
Queue update processes the input event and then the competitor event, then
normalizes to the next source phase. The grid verifier uses actual tape bits
and vertices and shares no queue transition logic.
"""
import argparse
import collections
import functools
import hashlib
import importlib.util
import json
import platform
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
PREFIX = 'thirdpass-review-1'

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, obj):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def freeze(label):
    manifest = ROOT / 'problems/2019-B4/notes/thirdpass-v1-manifest.json'
    obj = json.loads(manifest.read_text())
    entries = obj['files']
    rows = []
    for f in entries:
        p = ROOT / f['path']
        actual = {'path': f['path'], 'bytes': p.stat().st_size, 'sha256': digest(p)}
        actual['matches'] = (actual['bytes'] == f['bytes'] and actual['sha256'] == f['sha256'])
        rows.append(actual)
    result = {'label': label, 'manifest_sha256': digest(manifest), 'file_count': len(rows),
              'all_match': all(r['matches'] for r in rows), 'files': rows,
              'verifier_sha256': digest(__file__), 'python': sys.version,
              'platform': platform.platform(), 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}
    save(OUT / f'{PREFIX}-{label}-freeze.json', result)
    print(json.dumps({k: v for k, v in result.items() if k != 'files'}), flush=True)

def one_events(state, letter, limit):
    """Derive all other-path next events by FIFO reads/writes, not a table."""
    d, left, right = state
    ans = []
    for other in (0, 1):
        # h consumes its next bit 0 on the selected tape.
        dl, dr, u, v = d, d, left, right
        if letter == 0:
            if u & 1:
                continue
            u >>= 1
            dl -= 1
        else:
            # Append a zero: high zero bit changes length but not integer.
            dr += 1
        # g consumes its next bit 0. Left consumption puts it ahead;
        # right consumption must read h's FIFO.
        if other == 0:
            dl += 1
        else:
            if v & 1:
                continue
            v >>= 1
            dr -= 1
        assert dl == dr
        if dl > limit:
            continue
        if dl == 0:
            ans.append(None)
        else:
            mask = (1 << dl) - 1
            ans.append((dl, u ^ mask, v ^ mask))
    return tuple(ans)

def minimize(trans):
    """Hopcroft refinement, including a real rejecting sink; BFS quotient."""
    n = len(trans)
    rows = [tuple(n if t < 0 else t for t in row) for row in trans] + [(n, n)]
    blocks = {0: set(range(n)), 1: {n}}
    belongs = [0] * n + [1]
    inverse = [[set() for _ in range(n + 1)] for _ in range(2)]
    for s, row in enumerate(rows):
        for ch, target in enumerate(row):
            inverse[ch][target].add(s)
    todo = collections.deque([(1, 0), (1, 1)])
    pending = set(todo)
    fresh = 2
    while todo:
        bid, ch = todo.popleft()
        if (bid, ch) not in pending:
            continue
        pending.remove((bid, ch))
        pred = set()
        for target in blocks[bid]:
            pred.update(inverse[ch][target])
        hit = collections.defaultdict(set)
        for s in pred:
            hit[belongs[s]].add(s)
        for old, part in hit.items():
            if len(part) == len(blocks[old]):
                continue
            rest = blocks[old] - part
            blocks[old] = rest
            new = fresh
            fresh += 1
            blocks[new] = part
            for s in part:
                belongs[s] = new
            for a in (0, 1):
                if (old, a) in pending:
                    todo.append((new, a))
                    pending.add((new, a))
                else:
                    small = old if len(rest) < len(part) else new
                    if (small, a) not in pending:
                        todo.append((small, a))
                        pending.add((small, a))
    initial = belongs[0]
    sink = belongs[n]
    order = [initial]
    number = {initial: 0}
    quotient = []
    for bid in order:
        rep = next(iter(blocks[bid]))
        targets = []
        for target in rows[rep]:
            block = belongs[target]
            if block == sink:
                targets.append(-1)
            else:
                if block not in number:
                    number[block] = len(order)
                    order.append(block)
                targets.append(number[block])
        quotient.append(targets)
    # Verify every raw transition descends to the quotient, including sink.
    for s, row in enumerate(rows):
        if belongs[s] == sink:
            assert s == n
            continue
        qrow = quotient[number[belongs[s]]]
        for a, target in enumerate(row):
            mapped = -1 if belongs[target] == sink else number[belongs[target]]
            assert mapped == qrow[a]
    return quotient, [number[belongs[s]] for s in range(n)], len(blocks)

def build(delay, cap):
    started = time.monotonic()
    states = [frozenset()]
    number = {states[0]: 0}
    rows = []
    cached = {}
    for i, active in enumerate(states):
        row = []
        for letter in (0, 1):
            successors = set()
            rejected = False
            for residue in active:
                key = (residue, letter)
                if key not in cached:
                    cached[key] = one_events(residue, letter, delay)
                for target in cached[key]:
                    if target is None:
                        rejected = True
                        break
                    successors.add(target)
                if rejected:
                    break
            if rejected:
                row.append(-1)
                continue
            if letter:
                successors.add((1, 1, 1))
            frozen = frozenset(successors)
            if frozen not in number:
                if len(states) >= cap:
                    raise RuntimeError('explicit state cap reached')
                number[frozen] = len(states)
                states.append(frozen)
            row.append(number[frozen])
        rows.append(row)
        if i % 2000 == 0:
            print(json.dumps({'stage': 'build', 'D': delay, 'processed': i + 1,
                              'discovered': len(states), 'seconds': time.monotonic()-started}), flush=True)
    qrows, mapping, block_count = minimize(rows)
    v = [1] * len(qrows)
    for _ in range(200):
        v = [sum(v[t] for t in row if t >= 0) for row in qrows]
    av = [sum(v[t] for t in row if t >= 0) for row in qrows]
    slack = [1834856083*x - 1000000000*y for x, y in zip(v, av)]
    result = {'D': delay, 'raw_states': len(rows), 'quotient_states': len(qrows),
              'max_active': max(map(len, states)), 'queue_transition_count': len(cached),
              'block_count_with_sink': block_count,
              'raw_transition': rows, 'raw_to_quotient': mapping,
              'quotient_transition': qrows, 'v200': v, 'av200': av,
              'min_slack_1834856083': min(slack), 'all_positive': min(v) > 0,
              'all_strict_slack': min(slack) > 0,
              'seconds': time.monotonic()-started, 'verifier_sha256': digest(__file__)}
    save(OUT / f'{PREFIX}-d{delay}.json', result)
    print(json.dumps({k: v for k, v in result.items() if k not in
                      {'raw_transition','raw_to_quotient','quotient_transition','v200','av200'}}), flush=True)

def tapes(word, phase=0):
    parts = [[], []]
    for t, ch in enumerate(word):
        parts[ch].append((t + phase) % 2)
    return tuple(tuple(p) for p in parts)

def grid_bubble(word, delay):
    """Actual fixed-tape grid DP, allowing a divergence at every base vertex."""
    u, v = tapes(word)
    base = 0
    active = set()
    for t, ch in enumerate(word):
        nextbase = base + (ch == 0)
        nxt = set()
        for i in active | {base}:
            j = t - i
            if i < len(u) and u[i] == t % 2:
                d = i + 1 - nextbase
                if i in active and d == 0:
                    return True
                if 1 <= d <= delay:
                    nxt.add(i + 1)
            if 0 <= j < len(v) and v[j] == t % 2:
                d = i - nextbase
                if i in active and d == 0:
                    return True
                if 1 <= d <= delay:
                    nxt.add(i)
        base = nextbase
        active = nxt
    return False

def min_width(word):
    u, v = tapes(word)
    base = 0
    costs = {0: 0}
    n = len(word)
    for t, ch in enumerate(word):
        base += (ch == 0)
        nxt = {}
        for i, cost in costs.items():
            j = t - i
            for newi, legal in ((i+1, i < len(u) and u[i] == t%2),
                                (i, 0 <= j < len(v) and v[j] == t%2)):
                d = newi - base
                if legal and ((t+1 == n and d == 0) or (t+1 < n and d > 0)):
                    val = max(cost, d)
                    nxt[newi] = min(nxt.get(newi, n+1), val)
        costs = nxt
    return costs.get(base)

def history_info(word):
    u, v = tapes(word)
    @functools.lru_cache(None)
    def paths(i, j):
        if i == len(u) and j == len(v):
            return 1
        bit = (i+j)%2
        return ((paths(i+1,j) if i < len(u) and u[i] == bit else 0) +
                (paths(i,j+1) if j < len(v) and v[j] == bit else 0))
    count = paths(0,0)
    i = j = 0
    least = []
    while i+j < len(word):
        bit = (i+j)%2
        if i < len(u) and u[i] == bit and paths(i+1,j):
            least.append(0)
            i += 1
        else:
            assert j < len(v) and v[j] == bit and paths(i,j+1)
            least.append(1)
            j += 1
    return tuple(least), count

def accepted(word, rows, start=0):
    s = start
    for ch in word:
        s = rows[s][ch]
        if s < 0:
            return False
    return True

def small(maxn):
    started = time.monotonic()
    monitors = {d: json.loads((OUT / f'{PREFIX}-d{d}.json').read_text())['quotient_transition'] for d in (3,7)}
    records = []
    allwords = [()]
    bset = {'1'}
    for n in range(maxn+1):
        contexts = {}
        totals = {d: 0 for d in monitors}
        for h in allwords:
            pair = tapes(h)
            if pair not in contexts:
                contexts[pair] = h
            # Complement phase changes tape bits, never context equivalence.
            assert tapes(h,1) == tuple(tuple(1-x for x in p) for p in pair)
            for d, rows in monitors.items():
                keep = accepted(h,rows)
                assert keep == (not grid_bubble(h,d)), (n,h,d)
                totals[d] += keep
                if contexts[pair] == h:
                    assert keep
            if n <= 10:
                assert history_info(h)[0] == contexts[pair]
        actual = {''.join(map(str,p[0][::-1])) + '1' + ''.join(map(str,p[1])) for p in contexts}
        assert actual == bset
        record = {'moves': n, 'histories': len(allwords), 'contexts': len(contexts),
                  'distinct_strings_length_n_plus_1': len(bset), 'accepted': totals}
        records.append(record)
        print(json.dumps(record), flush=True)
        allwords = [h+(ch,) for h in allwords for ch in (0,1)]
        bit = str(n%2)
        bset = {r for s in bset for r in (bit+s,s+bit)}
    result = {'max_moves': maxn, 'total_histories': sum(2**n for n in range(maxn+1)),
              'records': records, 'seconds': time.monotonic()-started,
              'verifier_sha256': digest(__file__)}
    save(OUT / f'{PREFIX}-small.json', result)

def load_json(name):
    return json.loads((ROOT/'problems/2019-B4/computations'/name).read_text())

def canonical_bfs(rows, start):
    order = [start]
    number = {start: 0}
    out = []
    for s in order:
        row = []
        for target in rows[s]:
            if target < 0:
                row.append(-1)
            else:
                if target not in number:
                    number[target] = len(order)
                    order.append(target)
                row.append(number[target])
        out.append(row)
    return out, order

def compare():
    """Only added after the frozen independent implementation and D7 run."""
    source = ROOT/'problems/2019-B4/computations/thirdpass-delay-automaton.py'
    spec = importlib.util.spec_from_file_location('author_monitor_for_comparison',source)
    author = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(author)
    records = []
    for d, name in ((3,'thirdpass-delay3.json'),(7,'thirdpass-delay7-exact.json')):
        own = json.loads((OUT/f'{PREFIX}-d{d}.json').read_text())
        saved = load_json(name)
        canonical, order = canonical_bfs(saved['edges'],saved['start'])
        assert len(order) == len(saved['edges'])
        assert canonical == own['quotient_transition']
        # Every saved integer vector entry is compared under the verified
        # state isomorphism, not just extremal values.
        assert [saved['positive_vector'][i] for i in order] == own['v200']
        raw, meta = author.monitor(d,40000)
        states, rows = raw
        assert meta['complete']
        assert rows == own['raw_transition']
        # Recover the independent queue-set semantics along each BFS edge,
        # and compare every authored raw state under bit-string encoding.
        ownstates = [frozenset()]
        ids = {ownstates[0]:0}
        for s, active in enumerate(ownstates):
            for ch in (0,1):
                nxt = set()
                bad = False
                for residue in active:
                    for target in one_events(residue,ch,d):
                        if target is None:
                            bad = True
                        else:
                            nxt.add(target)
                if bad:
                    assert own['raw_transition'][s][ch] == -1
                    continue
                if ch:
                    nxt.add((1,1,1))
                key = frozenset(nxt)
                if key not in ids:
                    ids[key] = len(ownstates)
                    ownstates.append(key)
                assert own['raw_transition'][s][ch] == ids[key]
            def encode(residue):
                width,u,v = residue
                return (''.join(str((u>>j)&1) for j in range(width)),
                        ''.join(str((v>>j)&1) for j in range(width)))
            assert frozenset(map(encode,active)) == states[s]
        assert len(ownstates) == len(states) == own['raw_states']
        residues = sorted(set().union(*states))
        assert list(map(list,residues)) == saved['individual_competitors']
        # Check all saved length counts, respecting letter multiplicities.
        counts = [1]
        vector = [0]*len(canonical)
        vector[0] = 1
        for _ in saved['counts'][1:]:
            new = [0]*len(vector)
            for s,row in enumerate(canonical):
                for target in row:
                    if target >= 0:
                        new[target] += vector[s]
            vector = new
            counts.append(sum(vector))
        assert counts == saved['counts']
        cross = load_json('thirdpass-crosscheck15.json')
        if d == 7:
            cert = cross['upper_certificate']
            assert cert['strict_integer_inequalities'] == len(canonical)
            assert cert['minimum_slack'] == own['min_slack_1834856083']
            assert cert['min_vector_entry'] == min(own['v200'])
        record = {'D':d,'raw_states_and_all_transitions_match':len(states),
                  'quotient_states_and_all_transitions_match':len(canonical),
                  'distinct_residues_match':len(residues),
                  'every_vector_entry_match':len(canonical),
                  'all_length_counts_match':len(counts),
                  'data_sha256':digest(ROOT/'problems/2019-B4/computations'/name)}
        print(json.dumps(record),flush=True)
        records.append(record)
    save(OUT/f'{PREFIX}-compare.json',{'records':records,'author_source_sha256':digest(source),
                                     'verifier_sha256':digest(__file__)})

def minimal_language(rows):
    # Need full prefix to remain accepted until its first rejection, and
    # suffix after dropping first letter to remain accepted at that step.
    initial = (None,0)
    terminal = ('terminal',0)
    pairs = [initial,terminal]
    ids = {initial:0,terminal:1}
    out = []
    for pair in pairs:
        row = []
        for ch in (0,1):
            if pair == terminal:
                row.append(-1)
                continue
            full,suffix = pair
            q = rows[0 if full is None else full][ch]
            r = 0 if full is None else rows[suffix][ch]
            if r < 0:
                row.append(-1)
                continue
            target = terminal if q < 0 else (q,r)
            if target not in ids:
                ids[target] = len(pairs)
                pairs.append(target)
            row.append(ids[target])
        out.append(row)
    return out,0,1

def grammar():
    own = json.loads((OUT/f'{PREFIX}-d3.json').read_text())
    expected = [[0,1],[0,2],[3,2],[-1,4],[0,5],[6,2],[-1,7],[8,5],[4,4]]
    assert own['quotient_transition'] == expected
    mf,start,terminal = minimal_language(expected)
    saved = load_json('thirdpass-minimal3.json')
    assert mf == saved['edges'] and start == saved['start'] and terminal == saved['terminal']
    assert len(mf) == 23
    # Thompson-style word paths: no imported regex package or author code.
    arcs = collections.defaultdict(lambda:collections.defaultdict(set))
    nextstate = 3
    for src,text,dst in ((0,'RRLL',1),(0,'RRLRRLRL',2),
                         (2,'RRLRL',2),(2,'LRLRL',2),(2,'LRLRRLRL',2),(2,'LRLL',1)):
        last = src
        for j,c in enumerate(text):
            target = dst if j+1 == len(text) else nextstate
            nextstate += (j+1 < len(text))
            arcs[last][c=='R'].add(target)
            last = target
    todo = [(start,frozenset([0]))]
    seen = set(todo)
    for q,ss in todo:
        assert (q==terminal) == (1 in ss)
        for ch in (0,1):
            q1 = -1 if q < 0 else mf[q][ch]
            s1 = frozenset(t for s in ss for t in arcs[s][ch])
            pair = (q1,s1)
            if pair not in seen:
                seen.add(pair)
                todo.append(pair)
    assert len(seen)==31 and nextstate==31
    # Independent deterministic prefix-trie code parser, including the
    # terminating word. Its equivalence is a second complete finite test.
    trie = [{},{}]  # initial root, looping root; accept node 2
    trie.append({})
    for src,text,dst in ((0,'RRLL',2),(0,'RRLRRLRL',1),
                         (1,'RRLRL',1),(1,'LRLRL',1),(1,'LRLRRLRL',1),(1,'LRLL',2)):
        node = src
        for j,c in enumerate(text):
            ch = (c=='R')
            if j+1 == len(text):
                assert ch not in trie[node]
                trie[node][ch] = dst
            else:
                if ch not in trie[node]:
                    trie[node][ch] = len(trie)
                    trie.append({})
                node = trie[node][ch]
    seen2={(start,0)}
    todo2=list(seen2)
    for q,s in todo2:
        assert (q==terminal)==(s==2)
        for ch in (0,1):
            pair=(-1 if q<0 else mf[q][ch], -1 if s<0 else trie[s].get(ch,-1))
            if pair not in seen2:
                seen2.add(pair)
                todo2.append(pair)
    # Exact recurrence coefficients for F_3, then renewal for A_3.
    length=100
    loop=[0]*(length+1)
    loop[0]=1
    for n in range(1,length+1):
        loop[n]=(2*loop[n-5] if n>=5 else 0)+(loop[n-8] if n>=8 else 0)
    formula=[(1 if n==4 else 0)+(loop[n-12] if n>=12 else 0) for n in range(length+1)]
    v=[0]*len(mf)
    v[start]=1
    counted=[]
    for _ in range(length+1):
        counted.append(v[terminal])
        w=[0]*len(v)
        for s,row in enumerate(mf):
            for t in row:
                if t>=0:w[t]+=v[s]
        v=w
    assert formula==counted
    # Verify A3 formula by rational polynomial multiplication, in ascending
    # degree; no symbolic package or numerical roots.
    den_renewal=[1,-2,0,0,1]
    loops_den=[1,0,0,0,0,-2,0,0,-1]
    product=[0]*13
    for i,a in enumerate(den_renewal):
        for j,b in enumerate(loops_den):product[i+j]+=a*b
    product[12]+=1
    expected_den=[1,-2,0,0,1,-2,4,0,-1]
    assert product[:9]==expected_den and product[9:]==[0]*4
    result={'nine_state_table_exact':True,'minimal_factor_DFA_states':len(mf),
            'NFA_states':nextstate,'DFA_NFA_product_states':len(seen),
            'all_product_acceptance_pairs_equal':True,'deterministic_trie_states':len(trie),
            'DFA_trie_product_states':len(seen2),'formula_coefficients_checked':length+1,
            'rational_identity_exact':True,'verifier_sha256':digest(__file__)}
    save(OUT/f'{PREFIX}-grammar.json',result)
    print(json.dumps(result),flush=True)

def factors():
    saved=load_json('secondpass-full-obstruction24-v2.json')
    words=saved['all_minimal_forbidden_in_complete_layers']
    cross=load_json('thirdpass-crosscheck15.json')
    widths={x['history']:x['minimum_separation'] for x in cross['obstruction_widths']}
    monitors={d:load_json(f'thirdpass-delay{d}'+('-exact' if d==7 else '')+'.json')['edges'] for d in range(3,8)}
    records=[]
    counter=collections.Counter()
    triples=[]
    for f in words:
        text=f['larger']
        h=tuple(int(c=='R') for c in text)
        least,multiplicity=history_info(h)
        assert least<h
        assert ''.join('LR'[c] for c in least)==f['smaller']
        assert history_info(h[:-1])[0]==h[:-1]
        assert history_info(h[1:])[0]==h[1:]
        assert tuple(''.join(map(str,p)) for p in tapes(h))==tuple(f['tapes'])
        width=min_width(h)
        assert width==widths[text] and width is not None
        for d,rows in monitors.items():
            assert accepted(h,rows)==(width>d)
        if len(h)==19 and multiplicity==3:
            triples.append(text)
        counter[(len(h),width)]+=1
        records.append({'history':text,'length':len(h),'minimum_width':width,
                        'complete_history_count':multiplicity,
                        'canonical_prefix_and_suffix':True})
    assert len(records)==len(widths)==143
    assert len(triples)==4
    result={'count':len(records),'records':records,'length_width_distribution':
            [{'length':n,'width':w,'count':count} for (n,w),count in sorted(counter.items())],
            'length19_three_history_factors':triples,
            'all_minimality_width_and_monitor_checks_pass':True,'verifier_sha256':digest(__file__),
            'accepted_factor_data_sha256':digest(ROOT/'problems/2019-B4/computations/secondpass-full-obstruction24-v2.json'),
            'author_crosscheck_sha256':digest(ROOT/'problems/2019-B4/computations/thirdpass-crosscheck15.json')}
    save(OUT/f'{PREFIX}-factors.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in {'records','length_width_distribution'}}),flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['freeze','build','small','compare','grammar','factors'])
    parser.add_argument('--label',default='before')
    parser.add_argument('--delay',type=int,default=3)
    parser.add_argument('--cap',type=int,default=40000)
    parser.add_argument('--maxn',type=int,default=15)
    a = parser.parse_args()
    if a.mode == 'freeze':
        freeze(a.label)
    elif a.mode == 'build':
        build(a.delay,a.cap)
    elif a.mode == 'small':
        small(a.maxn)
    elif a.mode == 'compare':
        compare()
    elif a.mode == 'grammar':
        grammar()
    else:
        factors()

if __name__ == '__main__':
    main()
