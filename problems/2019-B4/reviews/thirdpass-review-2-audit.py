#!/usr/bin/env python3
"""Post-construction full artifact audit; never imports the author's code."""
import argparse
import collections
import functools
import hashlib
import importlib.util
import json
import pathlib
import time

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
COMP = ROOT/'problems/2019-B4/computations'
spec = importlib.util.spec_from_file_location('independent_checker', HERE/'thirdpass-review-2-check.py')
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)
C.START = time.monotonic()


def load(path):
    return json.loads(path.read_text())


def counts(rows, n, terminal=None):
    v = [0]*len(rows)
    v[0] = 1
    out = []
    for k in range(n+1):
        out.append(sum(v) if terminal is None else v[terminal])
        w = [0]*len(rows)
        for i, row in enumerate(rows):
            for j in row:
                if j >= 0:
                    w[j] += v[i]
        v = w
    return out


def least_history(word):
    u, v = C.pi(word)
    @functools.lru_cache(None)
    def possible(i, j):
        t = i+j
        if t == len(word):
            return True
        return ((i < len(u) and u[i] == t%2 and possible(i+1, j)) or
                (j < len(v) and v[j] == t%2 and possible(i, j+1)))
    assert possible(0, 0)
    i = j = 0
    result = ''
    while len(result) < len(word):
        t = len(result)
        if i < len(u) and u[i] == t%2 and possible(i+1, j):
            result += 'L'
            i += 1
        else:
            assert j < len(v) and v[j] == t%2 and possible(i, j+1)
            result += 'R'
            j += 1
    return result


def min_width(word):
    u, v = C.pi(word)
    base = [0]
    for letter in word:
        base.append(base[-1]+(letter == 'L'))
    best = {(0, 0): 0}
    for t in range(1, len(word)+1):
        for i in range(max(0, t-len(v)), min(len(u), t)+1):
            j = t-i
            d = i-base[t]
            if t < len(word) and d <= 0:
                continue
            if t == len(word) and d != 0:
                continue
            choices = []
            if i and u[i-1] == (t-1)%2 and (i-1, j) in best:
                choices.append(best[i-1, j])
            if j and v[j-1] == (t-1)%2 and (i, j-1) in best:
                choices.append(best[i, j-1])
            if choices:
                best[i, j] = max(d, min(choices))
    return best.get((len(u), len(v)))


def verify_data(independent, author, D):
    rows = independent['transitions']
    assert rows == author['edges'], ('all row comparison', D)
    assert author['start'] == 0
    assert len(rows) == author['minimal_states']
    assert independent['raw_states'] == author['construction']['states']
    assert independent['max_active'] == author['construction']['max_active_competitors']
    raw = independent['raw_transitions']
    part = independent['partition']
    assert len(raw) == len(part)
    for i, row in enumerate(raw):
        for letter, target in enumerate(row):
            assert rows[part[i]][letter] == (-1 if target < 0 else part[target])
    n = len(author['counts'])-1
    assert counts(rows, n) == author['counts']
    v = [1]*len(rows)
    for _ in range(author['parameters']['power_steps']):
        v = [sum(v[j] for j in row if j >= 0) for row in rows]
    assert v == author['positive_vector']
    mf_states, mf_rows = C.mf_machine(rows)
    minimal_file = COMP/f'thirdpass-minimal{D}.json'
    result = {'D': D, 'all_rows_equal': len(rows), 'all_raw_partition_edges_checked': 2*len(raw),
              'all_counts_equal_through': n, 'positive_vector_entries_equal': len(v),
              'mf_states': len(mf_rows)}
    if minimal_file.exists():
        saved = load(minimal_file)
        assert mf_rows == saved['edges']
        assert saved['start'] == 0 and saved['terminal'] == 1
        assert len(mf_rows) == saved['construction']['states']
        f = counts(mf_rows, len(saved['coefficients'])-1, terminal=1)
        assert f == saved['coefficients']
        # All available renewal coefficients, with multiplicity included.
        for n in range(1, len(author['counts'])):
            assert author['counts'][n] == 2*author['counts'][n-1]-sum(f[j]*author['counts'][n-j] for j in range(1, n+1))
        result['all_mf_rows_equal'] = len(mf_rows)
        result['all_mf_counts_equal_through'] = len(f)-1
        result['all_available_renewal_coefficients_equal'] = len(author['counts'])-1
    if D == 7:
        av = [sum(v[j] for j in row if j >= 0) for row in rows]
        slack = [1834856083*x-1000000000*y for x, y in zip(v, av)]
        assert min(v) > 0 and min(slack) > 0
        result['strict_certificate'] = {'positive_entries': len(v), 'all_strict_rows': len(slack),
            'minimum_slack': str(min(slack)), 'minimum_vector_entry': str(min(v)),
            'slack_sha256': hashlib.sha256(json.dumps(slack, separators=(',', ':')).encode()).hexdigest()}
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--out', required=True)
    a = p.parse_args()
    out = {'source_manifest': [], 'comparison': [], 'boundary': []}
    manifest_path = ROOT/'problems/2019-B4/notes/thirdpass-v1-manifest.json'
    manifest = load(manifest_path)
    for item in manifest['files']:
        data = (ROOT/item['path']).read_bytes()
        assert len(data) == item['bytes']
        assert hashlib.sha256(data).hexdigest() == item['sha256']
        out['source_manifest'].append({'path': item['path'], 'sha256': item['sha256']})
    C.pulse('all_frozen_files_verified', files=len(out['source_manifest']))
    matrices = {}
    for D in range(1, 8):
        if D in (3, 4, 7):
            name = 'd7' if D == 7 else f'grid{D}'
            own = load(HERE/f'thirdpass-review-2-{name}.json')
        else:
            raw, edges = C.build(D)
            rows, part = C.minimize(edges)
            own = {'D': D, 'raw_states': len(raw), 'max_active': max(map(len, raw)),
                   'transitions': rows, 'raw_transitions': edges, 'partition': part}
        matrices[D] = own['transitions']
        if D <= 2:
            if D == 1:
                assert matrices[D] == [[0, 0]]
                out['boundary'].append({'D': 1, 'language': 'all histories', 'states': 1})
            else:
                out['boundary'].append(C.small_oracle(matrices[D], D, 12))
            continue
        author = load(COMP/f'thirdpass-delay{D}{"-exact" if D == 7 else ""}.json')
        out['comparison'].append(verify_data(own, author, D))
        C.pulse('all_saved_data_verified', D=D, states=len(matrices[D]))
    known = load(COMP/'secondpass-full-obstruction24-v2.json')['all_minimal_forbidden_in_complete_layers']
    savedwidth = {x['history']: x['minimum_separation'] for x in load(COMP/'thirdpass-crosscheck15.json')['obstruction_widths']}
    out['factors'] = []
    dist = collections.Counter()
    for item in known:
        word = item['larger']
        lower = least_history(word)
        assert lower < word
        assert least_history(word[:-1]) == word[:-1]
        assert least_history(word[1:]) == word[1:]
        width = min_width(word)
        assert width == savedwidth[word]
        for D, rows in matrices.items():
            assert C.accepted(rows, word) == (width > D)
        dist[len(word), width] += 1
        out['factors'].append({'word': word, 'lex_least_equal_context_history': lower, 'min_width': width})
    assert len(known) == len(savedwidth) == 143
    out['width_distribution'] = [{'length': n, 'width': w, 'count': count} for (n, w), count in sorted(dist.items())]
    C.pulse('all_known_factors_verified', factors=len(known))
    # Symbolic D3 solve is small, timed externally like the other jobs.
    import sympy as s
    z = s.symbols('z')
    rows = matrices[3]
    M = s.eye(len(rows))
    for i, row in enumerate(rows):
        for j in row:
            if j >= 0:
                M[i, j] -= z
    result = M.inv()*s.ones(len(rows), 1)
    rational = s.cancel(result[0])
    expected = (z**8+2*z**5-1)/(z**8-4*z**6+2*z**5-z**4+2*z-1)
    F = z**4+z**12/(1-2*z**5-z**8)
    assert s.cancel(rational-expected) == 0
    assert s.cancel(1/rational-1+2*z-F) == 0
    out['D3_symbolic'] = {'sympy': s.__version__, 'A3': str(rational), 'F3': str(s.factor(F)),
                          'transfer_equals_claim': True, 'renewal_equals_grammar': True}
    out['grammar'] = C.grammar_equivalence(matrices[3])
    pathlib.Path(a.out).write_text(json.dumps(out, indent=2)+'\n')
    C.pulse('complete', output=a.out)


if __name__ == '__main__':
    main()
