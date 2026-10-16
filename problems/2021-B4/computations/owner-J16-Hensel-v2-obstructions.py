#!/usr/bin/env python3
"""Extract small left-kernel certificates and check the 90->14->0 chain.

Constructor post-check only. Runtime is bounded by exactly 104 rows,
three 2x2 determinants and three scalar products per row; no CAS.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import time

HERE=Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


start=time.monotonic()
source=HERE/'owner-J16-Hensel-v2-certificates.jsonl'
assert sha(source)=='e5f4ebc407434d8337d108e95807140887f00eab8cc7ced06d26341405124c94'
old=HERE/'owner-J16-Hensel-v1-postcheck-result.json'
assert sha(old)=='6eee254cd548d78c68c02348945fac4b42dffeea78f7c622da23019561c27f0b'
expected={tuple(s['key']) for s in json.loads(old.read_text())['states']}
assert len(expected)==90
rows=[json.loads(s) for s in source.read_text().splitlines()]
assert len(rows)==104
certificates=[]
hist=Counter()
for precision in (4,5):
    layer=[r for r in rows if r['input_precision']==precision]
    actual={tuple(r['key']) for r in layer}
    assert len(actual)==len(layer) and actual==expected
    children=[]
    for row in layer:
        m=row['jacobian_mod19']
        c=row['affine_constants']
        det=lambda i,j:(m[i][0]*m[j][1]-m[i][1]*m[j][0])%19
        lam=[det(1,2),det(2,0),det(0,1)]
        assert any(lam)
        assert all(sum(lam[i]*m[i][j] for i in range(3))%19==0 for j in range(2))
        obstruction=sum(lam[i]*c[i] for i in range(3))%19
        assert bool(row['children'])==(obstruction==0)
        assert len(row['children'])<=1
        children+=row['children']
        hist[f'precision{precision}_obstruction'+str(obstruction!=0)]+=1
        certificates.append({'key':row['key'],'input_precision':precision,
                             'matrix':m,'constants':c,'left_kernel':lam,
                             'obstruction_mod19':obstruction,
                             'digits':row['digits'],'children':row['children']})
    assert len(set(map(tuple,children)))==len(children)
    expected=set(map(tuple,children))
assert not expected
result={'status':'candidate finite obstruction extraction; constructor post-check only',
        'input_hashes':{p.name:sha(p) for p in (source,old)},
        'chain':[90,14,0],'rows':104,'histogram':dict(hist),
        'certificates':certificates,'elapsed_seconds':time.monotonic()-start}
out=HERE/'owner-J16-Hensel-v2-obstructions-result.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('certificates','input_hashes')}),flush=True)
