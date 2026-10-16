#!/usr/bin/env python3
"""Candidate fixed precision-eight extension with a proved 90-node bound.

Explicit co-constructor reuse of frozen v1 scalar helpers, cross-checked
against full integer Horner evaluation and exact quotient-ring remainders.
Not an independent audit; all mathematical conclusions remain unreviewed.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import datetime
import hashlib
import importlib.util
import json
import math
import os
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
V1=HERE/'owner-J16-Hensel-v1.py'
V1_HASH='acb811b279c11def4c82a1e156e9906007c313d78341ede722e00e1a70a2ee06'
STATES=HERE/'owner-J16-Hensel-v1-postcheck-result.json'
STATES_HASH='6eee254cd548d78c68c02348945fac4b42dffeea78f7c622da23019561c27f0b'
V1_MANIFEST=HERE.parent/'notes/owner-J16-Hensel-v1-manifest.json'
V1_MANIFEST_HASH='2f5eec6a98e0ff8c264259a508868c3d0e5f5befa8de833a9434dfd7fc069f6a'
TARGET=8
CAP=90


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def emit(row):
    print(json.dumps(row,sort_keys=True),flush=True)


def exact_state(key):
    mask,um,vm,nu,U,V=key
    q=19**nu
    u,v=q*U,q*V
    a=[1,-1]
    for j in range(2,19):
        bit=1<<(j-2)
        w=1 if mask&bit else u if um&bit else v if vm&bit else 0
        val=0
        for h in range(j):
            val=(val+math.comb(j,h)*a[h])*w
        a.append(-val)
    f=[math.comb(20,18-e)*a[18-e] for e in range(17)]+[-20,1]
    r1=r0=0
    for c in reversed(f):
        r1,r0=r0+(u+v)*r1,c-u*v*r1
    e=[Fraction(sum(f),19*q),Fraction(r0,19*q*10),Fraction(r1,19*q)]
    assert all(x.denominator%19 for x in e)
    return a,f,[r0,r1],e


def child(benchmark):
    prefix='owner-J16-Hensel-v2'+('-benchmark' if benchmark else '')
    start=time.monotonic()
    assert sha(V1)==V1_HASH and sha(STATES)==STATES_HASH
    assert sha(V1_MANIFEST)==V1_MANIFEST_HASH
    spec=importlib.util.spec_from_file_location('owner_j16_hensel_v1_frozen',V1)
    v1=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(v1)
    frozen=json.loads(STATES.read_text())
    assert frozen['nodes']==CAP and frozen['all_rank_two']
    nodes=[]
    matrices={}
    for state in frozen['states']:
        key=state['key']
        assert state['rank']==2
        matrix=state['jacobian_mod19']
        assert matrix==[list(row) for row in v1.jacobian(key)]
        assert any(d for i,j,d in state['two_by_two_minors'])
        family=tuple(key[:3])
        if family in matrices:
            assert matrices[family]==matrix
        matrices[family]=matrix
        nodes.append(key)
    assert len(nodes)==len(set(map(tuple,nodes)))==CAP
    result={'status':'running candidate construction; unverified','pid':os.getpid(),
            'requested_model':'gpt-6.1-sol','requested_reasoning':'max',
            'effective_setting_readback':'unavailable',
            'input_precision':4,'target_precision':TARGET,'node_cap_per_level':CAP,
            'benchmark':benchmark,'structural_bound':'all 90 input states have constant rank-2 Jacobian; at most one child each at every later precision',
            'explicit_constructor_reuse':{'source':str(V1.relative_to(ROOT)),'sha256':V1_HASH},
            'input_sha256':{str(p.relative_to(ROOT)):sha(p) for p in (STATES,V1_MANIFEST)},
            'levels':[]}
    result_path=HERE/(prefix+'-result.json')
    cert_path=HERE/(prefix+'-certificates.jsonl')
    digest=hashlib.sha256()
    with cert_path.open('wb') as certs:
        for k in range(4,TARGET):
            assert len(nodes)<=CAP
            before=len(nodes)
            next_nodes=[]
            hist=Counter()
            mask_input=Counter()
            mask_output=Counter()
            for i,key in enumerate(nodes,1):
                mask_input[key[0]]+=1
                matrix=matrices[tuple(key[:3])]
                a,f,r,e=exact_state(key)
                emod=19**(k+1)
                E=[x.numerator*pow(x.denominator,-1,emod)%emod for x in e]
                small_e,small_a,amod=v1.residual(key,k)
                assert small_e==E and small_a==[x%amod for x in a]
                base=19**k
                assert all(x%base==0 for x in E)
                constants=[x//base for x in E]
                rank,digits,rref=v1.affine_digits(matrix,constants)
                assert rank==2 and len(digits)<=1
                # A separate all-pairs check costs at most 360*361 tiny
                # operations and checks the imported digit solver here.
                brute=[[du,dv] for du in range(19) for dv in range(19)
                       if all((x*du+y*dv+c)%19==0
                              for (x,y),c in zip(matrix,constants))]
                assert digits==brute
                hist['consistent' if digits else 'inconsistent']+=1
                children=[key[:4]+[key[4]+base*du,key[5]+base*dv] for du,dv in digits]
                next_nodes+=children
                assert len(next_nodes)<=CAP
                mask_output[key[0]]+=len(children)
                row={'key':key,'input_precision':k,'integer_a':a,'integer_F':f,
                     'integer_R0_R1':r,
                     'exact_E':[[x.numerator,x.denominator] for x in e],
                     'E_modulus':emod,'E_mod':E,'jacobian_mod19':matrix,
                     'affine_constants':constants,'rank':rank,'rref':rref,
                     'digits':digits,'children':children}
                encoded=(json.dumps(row,separators=(',',':'))+'\n').encode()
                certs.write(encoded)
                digest.update(encoded)
                if i%10==0 or i==before:
                    certs.flush()
                    emit({'precision':k,'visited':i,'expected':before,
                          'generated':len(next_nodes),'pid':os.getpid(),
                          'elapsed_seconds':time.monotonic()-start})
            assert len(set(map(tuple,next_nodes)))==len(next_nodes)
            level={'input_precision':k,'input_nodes':before,'output_precision':k+1,
                   'output_nodes':len(next_nodes),'histogram':dict(hist),
                   'input_mask_counts':dict(mask_input),'output_mask_counts':dict(mask_output),
                   'complete_input_traversal':True,'output_states':next_nodes}
            result['levels'].append(level)
            result['last_complete_precision']=k+1
            result['last_output_nodes']=len(next_nodes)
            result['candidate_masks_at_last_complete_precision']=sorted(mask_output.keys()) if next_nodes else []
            # Remove zero-valued keys introduced by Counter += 0.
            result['candidate_masks_at_last_complete_precision']=sorted(m for m,n in mask_output.items() if n)
            result_path.write_text(json.dumps(result,indent=2)+'\n')
            emit({'level_complete':k,'next_nodes':len(next_nodes),
                  'masks':result['candidate_masks_at_last_complete_precision'],
                  'histogram':dict(hist)})
            if benchmark or not next_nodes:
                break
            nodes=next_nodes
    result['elapsed_seconds']=time.monotonic()-start
    result['certificate']={'path':str(cert_path.relative_to(ROOT)),
                           'rows':sum(l['input_nodes'] for l in result['levels']),
                           'bytes':cert_path.stat().st_size,'sha256':sha(cert_path),
                           'stream_sha256':digest.hexdigest()}
    result['status']='complete fixed first-level benchmark; precision-eight traversal incomplete' if benchmark else (
        'complete candidate exclusion of input cover; no residue nodes remain' if not result['last_output_nodes'] else
        'complete necessary construction through fixed precision eight; unverified survivors')
    result_path.write_text(json.dumps(result,indent=2)+'\n')
    emit({k:v for k,v in result.items() if k not in ('levels','input_sha256','certificate')})


def main():
    benchmark='--benchmark' in sys.argv
    if '--child' in sys.argv:
        child(benchmark)
        return
    prefix='owner-J16-Hensel-v2'+('-benchmark' if benchmark else '')
    out,err,job=[HERE/(prefix+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    if benchmark:
        cmd.append('--benchmark')
    record={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'command':cmd,'timeout_seconds':30,'node_cap_per_level':CAP,
            'target_precision':TARGET,'benchmark':benchmark,
            'source_sha256':sha(Path(__file__)),'status':'launching'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e)
        record.update(pid=proc.pid,status='running')
        job.write_text(json.dumps(record,indent=2)+'\n')
        emit(record)
        try:
            proc.wait(timeout=30)
            record['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:
            proc.kill();proc.wait()
            record['status']='timeout; identified child reaped; incomplete'
        record.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    record['output_hashes']={p.name:sha(p) for p in (out,err,HERE/(prefix+'-result.json'),HERE/(prefix+'-certificates.jsonl')) if p.is_file()}
    job.write_text(json.dumps(record,indent=2)+'\n')
    emit(record)


if __name__=='__main__':
    main()
