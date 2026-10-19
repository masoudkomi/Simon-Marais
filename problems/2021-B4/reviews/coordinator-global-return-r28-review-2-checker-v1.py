"""NEW reviewer checker. Certificate mode is MATHEMATICAL finite verification.

It uses factorial-scaled Appell coefficients and direct power evaluation,
independently of the author's binomial-array/Horner implementation.
Other modes are documentary SHA/JSON only. No old/author/source code runs.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
from math import factorial
import hashlib
import json
import os
import platform
import re
import subprocess
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P = 'problems/2021-B4/reviews/coordinator-global-return-r28-review-2-'
A = 'problems/2021-B4/notes/coordinator-global-return-r28-'
PAYLOADS = [P+s for s in ['initial-v1.md', 'sources-v1.json', 'checker-v1.py', 'certificate-v1.json', 'baseline-v1.json']]
MF = P+'manifest-v1.json'
PARENT = {'path': 'problems/2024-B4/reviews/reasoning-frontier-return-r15-review-1-manifest-v1.json',
          'bytes': 2084, 'sha256': '6937f7762ecfd5a8f11a317129ccb5aca1b8a779acdfbc1caa45b3dccc399137'}
NAMES = ['reasoning-deep-return-r24', 'coordinator-dyadic-return-r26', 'coordinator-contact-return-r27']

def utc():
    return datetime.now(timezone.utc).isoformat()

def read(path):
    return json.loads((ROOT/path).read_text())

def row(path):
    data=(ROOT/path).read_bytes()
    return {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def new(path, value):
    assert path.startswith(P)
    with (ROOT/path).open('x', encoding='utf-8') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write('\n')

def certificate_child():
    # C_j=A_j/j!, represented sparsely in h. In E_j/j! the monomial
    # multiplier is z^(j-i)/(j-i)!, not the author's binomial recurrence.
    low={0:{0:1}, 1:{1:-1}, 3:{3:2}, 6:{6:-35},
         7:{0:-1,1:7,3:-70,6:245}, 8:{0:7,1:-48,3:448,6:-980}}
    c=[{} for _ in range(21)]
    for j, poly in low.items():
        c[j]={d:Fraction(v,factorial(j)) for d,v in poly.items()}
    print('NEW factorial-scaled exact reconstruction; fixed degree20/prime37 only', file=sys.stderr, flush=True)
    degrees={}
    for j in range(11,19):
        poly={}
        for i in range(j):
            shift=j-i if j in (11,12,13,15,17) else 0
            for d,v in c[i].items():
                poly[d+shift]=poly.get(d+shift,Fraction(0))-v/factorial(j-i)
        c[j]={d:v for d,v in poly.items() if v}
        degrees[str(j)]=max(c[j],default=-1)
    q={}
    for i in range(19):
        multiplier=Fraction(factorial(20),factorial(20-i))
        for d,v in c[i].items():
            q[d]=q.get(d,Fraction(0))+multiplier*v
    q={d:v for d,v in q.items() if v}
    assert max(q)==17 and all(v.denominator==1 and v.numerator%2==0 for v in q.values())
    qi=[int(q.get(d,0)) for d in range(17,-1,-1)]
    wi=[-v//2 for v in qi]
    residues=[v%37 for v in wi]
    # Deliberately direct power sums, not author Horner code.
    values=[sum(v*pow(x,17-k,37) for k,v in enumerate(wi))%37 for x in range(37)]
    declared=read(A+'sources-v1.json')['mathematical_computation']['complete_standalone_stdout_record']
    assert wi==declared['integer_coefficients_descending']
    assert residues==declared['coefficients_descending_mod_prime']
    assert values==declared['values_at_0_through_36']
    assert residues[0]==27 and all(v!=0 for v in values)
    print(json.dumps({'status': 'PASS fixed finite certificate ONLY; hand domain/rational-root/gcd proof still required',
                      'independent_algorithm': 'C_j=A_j/j! sparse Fraction polynomials; factorial convolution; direct modular power sums',
                      'degree': 17, 'prime': 37, 'high_row_degrees': degrees,
                      'Q_integer_coefficients_descending': qi,
                      'W_integer_coefficients_descending': wi,
                      'W_coefficients_descending_mod37': residues,
                      'W_values_at_0_through_36': values,
                      'leading_coefficient_mod37': residues[0], 'all37_nonzero': True,
                      'declared_full_integer_coefficients_and_values_match': True,
                      'author_code_executed': False, 'prime_depth_height_search': False,
                      'dependencies': 'Python standard library fractions/math/json only'}))

def certificate():
    started=utc()
    command=[sys.executable,str(Path(__file__).resolve()),'certificate-child']
    child=subprocess.Popen(command,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
    print(json.dumps({'started_UTC':started,'child_PID':child.pid,'timeout_seconds':15,'command':command}),flush=True)
    try:
        stdout,stderr=child.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        child.terminate()
        try:
            stdout,stderr=child.communicate(timeout=3)
        except subprocess.TimeoutExpired:
            child.kill();stdout,stderr=child.communicate()
        new(P+'certificate-v1.json',{'status':'INCOMPLETE timeout','started_UTC':started,'finished_UTC':utc(),
                                    'child_PID':child.pid,'timeout_seconds':15,'reaped':True,
                                    'stdout':stdout,'stderr':stderr,'command':command})
        raise SystemExit(2)
    assert child.returncode==0,(child.returncode,stdout,stderr)
    result=json.loads(stdout)
    output={'started_UTC':started,'finished_UTC':utc(),'child_PID':child.pid,'timeout_seconds':15,
            'child_exit_code':child.returncode,'reaped':True,'command':command,
            'Python_version':platform.python_version(),'complete_stderr':stderr,
            'complete_child_result':result,'runs_of_THIS_fresh_verifier':1}
    new(P+'certificate-v1.json',output)
    print(json.dumps(output,indent=2),flush=True)

def labels():
    ids=re.findall(r'^\|R28R2-(\d\d)\|',(ROOT/PAYLOADS[0]).read_text(),re.M)
    assert ids==[str(i).zfill(2) for i in range(1,25)],ids

def prepare():
    af=A+'freeze-v1.json'
    author=read(af)
    paths=['AGENTS.md','problems/2021-B4/statement.md',af]+[r['path'] for r in author['payloads']]
    pairs=[]
    for name in NAMES:
        proof='problems/2021-B4/proofs/reviewed-'+name+'-v1.1.md'
        authority='problems/2021-B4/reviews/'+name+'-acceptance'
        paths += [proof,authority+'.md',authority+'.json']
        pairs.append((proof,authority+'.json'))
    paths.append(PARENT['path'])
    assert len(paths)==len(set(paths))==18
    guards=[row(p) for p in paths]
    bound={r['path']:r for r in guards}
    assert bound[af]=={'path':af,'bytes':2159,'sha256':'c2818ceba47100e3276c85d3937bd3a3f4ac887343c52b1fa96114d2a2743029'}
    for declared in author['payloads']:
        assert bound[declared['path']]==declared
    for proof,authority in pairs:
        assert bound[proof]==read(authority)['accepted_copy']
    assert bound[PARENT['path']]==PARENT
    new(P+'baseline-v1.json',{'prepared_UTC':utc(),'necessary_immutable_guards_ONCE':guards,
                             'guard_occurrences':18,'guard_unique_paths':18,'ONE_exact_OWN_parent':PARENT,
                             'recursive_inventory_expansion':False,'mutable_map_guards':False,
                             'hashes_not_MODEL_read_claims':True})
    print(json.dumps({'status':'PASS documentary identities only','baseline':row(P+'baseline-v1.json')}))

def freeze():
    assert '--FULL-final-ALL5-MODEL-readbacks-completed' in sys.argv
    labels();base=read(P+'baseline-v1.json');cert=read(P+'certificate-v1.json')
    assert cert['reaped'] and cert['child_exit_code']==0
    new(MF,{'frozen_UTC':utc(),'status':'sealed OTHER independent WHOLE2 initial; not promotion',
            'reviewer':'/root/review_2022_complexity_r2','constructor_excluded':True,
            'claims':['R28A','R28B'],'ENTIRE_files':6,'ALL_obligations':24,'payloads':[row(p) for p in PAYLOADS],
            'guard_occurrences':18,'guard_unique_paths':18,'ONE_exact_OWN_parent':PARENT,
            'FULL_final_ALL5_payload_MODEL_readbacks_completed':True,
            'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
            'findings_sealed_until_explicit_BOTH':True,'corresponding_NEW_peer_access':False,
            'fresh_fixed_finite_certificate_verifier_used':True,'author_old_source_code_executed':False,
            'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
            'independent_effective_backend_readback':None,
            'quota_start':{'usedPercent':86,'observed_UTC':'2026-10-19 04:00:39 UTC','resetsAt':1792874445,
                           'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False}})
    print(json.dumps({'manifest':row(MF)}))

def verify():
    m=read(MF)
    for declared in m['payloads']:
        assert row(declared['path'])==declared,declared['path']
    labels();base=read(P+'baseline-v1.json')
    assert m['ONE_exact_OWN_parent']==base['ONE_exact_OWN_parent']==PARENT
    assert len(m['payloads'])==5 and m['ALL_obligations']==24
    print(json.dumps({'SEPARATE_readonly_verify_UTC':utc(),'status':'PASS','ENTIRE_files':6,
                      'literal_obligations':24,'once_bound_necessary_paths':18,'manifest':row(MF),
                      'writes':0,'mathematics_certified_by_documentary_mode':False}))

if __name__=='__main__':
    {'certificate-child':certificate_child,'certificate':certificate,'prepare':prepare,
     'freeze':freeze,'verify':verify}[sys.argv[1]]()
