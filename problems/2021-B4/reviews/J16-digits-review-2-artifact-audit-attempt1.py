#!/usr/bin/env python3
"""Post-freeze serialization/certificate adapter, using only R2's frozen math.
No constructor or peer module is imported. Every finite record is checked.
"""
import collections
import gzip
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
NOTES=HERE.parent/'notes'
COMP=HERE.parent/'computations'
BASE=HERE/'J16-digits-review-2'
spec=importlib.util.spec_from_file_location('r2_frozen_math',HERE/'J16-digits-review-2-independent.py')
R=importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def readj(path):
    return json.loads(path.read_text())

def tup(rows):
    return tuple(tuple(row) for row in rows)

MANIFESTS={
 'coordinator-J16-coupled-leading-candidate-v1-manifest.json':('da57838f8b632e9153f86742ed33096821627fbd3fdc2089f90fda6ea88d2878',12),
 'coordinator-J16-coupled-digit-candidate-v1-manifest.json':('b9e20e7634f94f2ad34055f5da2efd0460e5645d9c3d8933800bd4892321d2ad',46),
 'owner-J16-Hensel-v1-manifest.json':('2f5eec6a98e0ff8c264259a508868c3d0e5f5befa8de833a9434dfd7fc069f6a',53),
 'owner-J16-Hensel-v2-manifest.json':('8b9cd2bbcf1740cb119436d58eb4a9f60dbf7afe5e9d23f077e1bc7428d75db8',14)}

def integrity():
    result={}
    files={}
    for name,(expected,n) in MANIFESTS.items():
        path=NOTES/name
        assert sha(path)==expected,(name,'manifest hash')
        manifest=readj(path)
        assert len(manifest['artifacts'])==n
        for a in manifest['artifacts']:
            p=ROOT/a['path']
            assert p.stat().st_size==a['bytes'] and sha(p)==a['sha256'],a['path']
            if a['path'] in files:
                assert files[a['path']]==a
            files[a['path']]=a
        result[name]={'sha256':expected,'artifacts':n}
    freeze=readj(Path(str(BASE)+'-predata-freeze.json'))
    for a in freeze['files']:
        assert sha(ROOT/a['path'])==a['sha256'],('predata file changed',a['path'])
    return {'manifests':result,'unique_artifact_count':len(files),'files':files}

def chunks(meta, plainkey='plain_sha256'):
    h=hashlib.sha256();total=0
    for chunk in meta['chunks']:
        p=ROOT/chunk['path']
        assert sha(p)==chunk['sha256'] and p.stat().st_size==chunk['bytes']
        n=0
        with gzip.open(p,'rb') as f:
            for line in f:
                h.update(line);n+=1;total+=1
                yield json.loads(line)
        assert n==chunk['rows']
    if 'rows' in meta:
        assert total==meta['rows']
    if plainkey in meta:
        assert h.hexdigest()==meta[plainkey],('plain stream mismatch',plainkey)

def canonical(rows):
    # Generic FULL augmented row-space canonicalization, all 3 columns.
    a=[[z%19 for z in row] for row in rows]
    pivot=0
    for col in range(3):
        choices=[i for i in range(pivot,len(a)) if a[i][col]]
        if not choices:
            continue
        i=choices[0]
        a[i],a[pivot]=a[pivot],a[i]
        z=pow(a[pivot][col],-1,19)
        a[pivot]=[x*z%19 for x in a[pivot]]
        for i in range(len(a)):
            if i==pivot:
                continue
            z=a[i][col]
            a[i]=[(x-z*y)%19 for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==len(a):
            break
    return tuple(tuple(row) for row in a)

def check_rref(record,M,c):
    assert len(record)==3 and all(len(row)==3 for row in record)
    assert all(0<=x<19 for row in record for x in row)
    original=[list(row)+[-z%19] for row,z in zip(M,c)]
    assert canonical(record)==canonical(original)
    last=-1
    for i,row in enumerate(record):
        piv=next((j for j in range(2) if row[j]),None)
        if piv is not None:
            assert piv>last and row[piv]==1
            assert all(record[h][piv]==0 for h in range(3) if h!=i)
            last=piv

def expected_groups():
    path=Path(str(BASE)+'-full-certificates.jsonl.gz')
    with gzip.open(path,'rb') as f:
        rows=(json.loads(line) for line in f)
        for ident,group in itertools.groupby(rows,lambda row:(row[0],row[1][0])):
            expected={}
            for row in group:
                key=tuple(row[1])
                assert key not in expected
                expected[key]=hashlib.sha256(R.pack(row)).digest()
            yield ident,expected

def leading_check(independent):
    accepted=readj(HERE/'newton-review-1-extension-result.json')
    assert sha(HERE/'newton-review-1-extension-result.json')=='96f61ad6b173c1fd40bfc2dff3f87c44b616db87bd6db0a0ca77b1a019bee803'
    source_masks=sorted(itertools.chain.from_iterable(accepted['retained_masks'].values()))
    assert source_masks==independent['accepted_masks']
    assert sorted(accepted['retained_masks']['16'])==independent['j16_masks']
    a=readj(COMP/'coordinator-J16-coupled-leading-v1-result.json')
    b=readj(COMP/'coordinator-J16-leading-branch-index-v1-result.json')
    ours={tuple(key):tuple(inactive) for key,inactive in independent['branches']}
    assert len(ours)==len(independent['branches'])==768
    restored=0
    candidates={}
    for branch in b['leading_branches']:
        active=branch['active_positions'];labels=branch['active_labels']
        assert len(active)==len(labels) and all(label in (0,1,2) for label in labels)
        um=sum(1<<(j-2) for j,z in zip(active,labels) if z==1)
        vm=sum(1<<(j-2) for j,z in zip(active,labels) if z==2)
        key=(branch['center_mask'],um,vm,branch['nu'],branch['U'],branch['V'])
        assert key not in candidates
        candidates[key]=tuple(branch['inactive_positions'])
        check=independent['by_mask'][str(key[0])]
        assert active==check['active'] and branch['inactive_positions']==check['inactive']
        assert branch['full_label_expansions']==3**len(check['inactive'])
        restored+=branch['full_label_expansions']
    assert candidates==ours and restored==840396
    retained=independent['leading_masks']
    assert sorted(a['retained_masks'])==sorted(b['retained_masks'])==retained
    assert sorted(a['excluded_masks'])==sorted(b['excluded_masks'])==sorted(set(independent['j16_masks'])-set(retained))
    # R2 counts label/nu proposals before constant prerequisites; candidate
    # counts only AFTER them. Compare the latter definition explicitly.
    eligible=0
    for mask in independent['j16_masks']:
        st=independent['by_mask'][str(mask)]
        a0=R.constants(mask)
        count=sum(not(a0[17]%(19**nu) or a0[18]%(19**nu))
                  for nu in range(1,st['nu_bound']+1))*3**len(st['active'])
        eligible+=count
        row=next(row for row in a['rows'] if row['center_mask']==mask)
        assert row['projected_label_and_nu_tests']==count
        assert row['minimum_valuation_upper_bound']==st['nu_bound']
        assert row['active_positions']==st['active']
    assert eligible==a['projected_label_and_nu_tests']==b['projected_label_and_nu_tests']==11559
    return {'accepted_masks':772,'j16_masks':88,'leading_masks':len(retained),
            'leading_branches':len(ours),'full_keys':restored,
            'eligible_projection_tests':eligible,'proposal_tests_before_prerequisites':independent['projected_tests'],
            'nu_histogram':dict(collections.Counter(key[3] for key in ours)),
            'equal_leading_residues':sum(key[4]==key[5] for key in ours),
            'zero_leading_coordinate':sum(not(key[4] and key[5]) for key in ours)}

def audit_late(independent):
    ours={(row['precision'],tuple(row['key'])):row for row in independent['late_exact_states']}
    assert len(ours)==104
    post=readj(COMP/'owner-J16-Hensel-v1-postcheck-result.json')
    seen=set()
    for state in post['states']:
        key=tuple(state['key']);o=ours[(4,key)]
        assert key not in seen;seen.add(key)
        assert state['integer_a']==o['a'] and state['integer_R0_R1']==o['R']
        F=list(reversed([1,-20]+[R.C[20][j]*o['a'][j] for j in range(2,19)]))
        assert state['integer_F']==F and state['exact_E']==o['E']
        assert tup(state['jacobian_mod19'])==tup(o['M']) and state['rank']==o['rank']==2
        minors=[]
        for i,j in ((0,1),(0,2),(1,2)):
            d=(o['M'][i][0]*o['M'][j][1]-o['M'][i][1]*o['M'][j][0])%19
            minors.append([i,j,d])
        assert state['two_by_two_minors']==minors and any(z[2] for z in minors)
    assert len(seen)==90 and post['nodes']==90 and post['all_rank_two']
    assert {key for k,key in ours if k==4}==seen
    assert all((key[0],key[2],key[1],key[3],key[5],key[4]) in seen for key in seen)
    seen_late=set()
    v2=readj(COMP/'owner-J16-Hensel-v2-result.json')
    cert_path=ROOT/v2['certificate']['path']
    assert sha(cert_path)==v2['certificate']['sha256']==v2['certificate']['stream_sha256']
    previous_children=seen
    by_level=collections.defaultdict(set)
    children_by_level=collections.defaultdict(set)
    for line in cert_path.read_bytes().splitlines():
        row=json.loads(line);k=row['input_precision'];key=tuple(row['key']);ident=(k,key)
        assert ident not in seen_late;seen_late.add(ident)
        o=ours[ident]
        assert row['integer_a']==o['a'] and row['integer_R0_R1']==o['R'] and row['exact_E']==o['E']
        F=list(reversed([1,-20]+[R.C[20][j]*o['a'][j] for j in range(2,19)]))
        assert row['integer_F']==F
        assert tup(row['jacobian_mod19'])==tup(o['M']) and row['rank']==o['rank']==2
        assert row['affine_constants']==o['c'] and row['digits']==o['digits']
        assert row['E_modulus']==19**(k+1)
        Em=[num*pow(den,-1,row['E_modulus'])%row['E_modulus'] for num,den in o['E']]
        assert row['E_mod']==Em
        check_rref(row['rref'],tup(o['M']),o['c'])
        children=[list(key[:4]) + [key[4]+19**k*x,key[5]+19**k*y] for x,y in o['digits']]
        assert row['children']==children
        by_level[k].add(key)
        for child in children:
            assert tuple(child) not in children_by_level[k]
            children_by_level[k].add(tuple(child))
    assert seen_late==set(ours)
    assert by_level[4]==seen and by_level[5]==children_by_level[4] and not children_by_level[5]
    obs=readj(COMP/'owner-J16-Hensel-v2-obstructions-result.json')
    obseen=set();hist=collections.Counter()
    for row in obs['certificates']:
        ident=(row['input_precision'],tuple(row['key']));o=ours[ident]
        assert ident not in obseen;obseen.add(ident)
        assert row['matrix']==o['M'] and row['constants']==o['c']
        assert row['left_kernel']==o['lambda'] and row['obstruction_mod19']==o['obstruction']
        assert row['digits']==o['digits']
        expected=[list(o['key'][:4])+[o['key'][4]+19**o['precision']*x,o['key'][5]+19**o['precision']*y] for x,y in o['digits']]
        assert row['children']==expected
        hist[(o['precision'],bool(o['obstruction']))]+=1
    assert obseen==set(ours) and obs['chain']==[90,14,0] and obs['rows']==104
    return {'exact_integer_states':len(ours),'postcheck_states':len(seen),
            'all_rank_two':True,'obstructions':{str(k):v for k,v in hist.items()},
            'chain':[90,14,0]}

def main():
    benchmark='--benchmark' in sys.argv
    start=time.monotonic()
    before=integrity()
    independent=readj(Path(str(BASE)+'-full-result.json'))
    assert independent['complete']
    lead=leading_check(independent)
    print(json.dumps({'event':'integrity_leading','unique_artifacts':before['unique_artifact_count'],'leading':lead}),flush=True)
    result={'benchmark':benchmark,'integrity_before':before,'leading':lead,'levels':[]}
    old=readj(COMP/'coordinator-J16-second-digit-v1-result.json')
    v1=readj(COMP/'owner-J16-Hensel-v1-result.json')
    oldrows=iter(chunks(old,'certificate_stream_sha256'))
    exgroups=iter(expected_groups())
    old_coeff_hash=hashlib.sha256()
    matrices={};rrefspaces={}
    limit=8192 if benchmark else None
    total=0
    for level in v1['levels']:
        k=level['input_precision']
        nodeiter=iter(chunks(level['nodes']))
        count=generated=0
        candgroups=itertools.groupby(chunks(level['certificates']),lambda row:row[0][0])
        for mask,rows in candgroups:
            ident,expected=next(exgroups)
            assert ident==(k,mask),(ident,k,mask)
            for row in rows:
                key,amod,a,E,M,rank,rref,prune,digits=row
                key=tuple(key);M=tup(M)
                assert not(key[0]&key[1] or key[0]&key[2] or key[1]&key[2])
                assert key[1]|key[2] < 1<<17
                family=key[:3]
                if family not in matrices:
                    matrices[family]=R.linear(*family)
                assert M==matrices[family]
                e,aa=R.evaluate(key,k+1,True)
                assert amod==19**(key[3]+k+1) and a==aa and E==list(e)
                assert all(z%(19**k)==0 for z in e)
                c=tuple(z//(19**k) for z in e)
                rr,solve=R.solver(M)
                alldigits=solve(tuple(-z%19 for z in c))
                omit=not key[1] or not key[2]
                assert rank==rr and bool(prune)==bool(omit)
                assert prune==('accepted_T1_missing_label' if omit else None)
                assert sorted(map(tuple,digits))==([] if omit else alldigits)
                reduced=[k,list(key),list(c),rank,int(omit),alldigits]
                assert expected.pop(key)==hashlib.sha256(R.pack(reduced)).digest()
                # Repeated row spaces are cached by all mathematical data,
                # not just rank or a few representative systems.
                spacekey=(M,c,tup(rref))
                if spacekey not in rrefspaces:
                    check_rref(rref,M,c)
                    rrefspaces[spacekey]=True
                if k==1:
                    rootrow=next(oldrows)
                    assert rootrow==list(key)+list(c)+[rank,int(bool(alldigits))]
                    a_for_root=a[:];a_for_root[1]=-1
                    old_coeff_hash.update(R.pack([list(key),a_for_root]))
                for dx,dy in digits:
                    child=list(key[:4])+[key[4]+19**k*dx,key[5]+19**k*dy]
                    assert next(nodeiter)==child
                    generated+=1
                count+=1;total+=1
                if count%16384==0:
                    print(json.dumps({'event':'artifact_checkpoint','precision':k,'parents':count,'generated':generated,'seconds':time.monotonic()-start}),flush=True)
                if benchmark and total>=limit:
                    result.update({'complete':False,'verified_rows':total,'seconds':time.monotonic()-start})
                    R.save('artifact-benchmark-result',result)
                    print(json.dumps({'event':'benchmark_done','rows':total,'seconds':result['seconds']}),flush=True)
                    return
            assert not expected,(k,mask,'independent nodes omitted')
        assert next(nodeiter,None) is None
        assert count==level['input_visited']==independent['layers'][k-1]['parents']
        assert generated==level['generated_nodes']==independent['layers'][k-1]['children']
        result['levels'].append({'precision':k,'parents':count,'children':generated,'all_coefficient_vectors_and_fibers_matched':True})
        if k==1:
            assert next(oldrows,None) is None
            assert old_coeff_hash.hexdigest()==old['scalar_coefficient_stream_sha256']=='dfe2ca43528f5e55c68a642f61838343b0a09bc6690afe153643c04ff574e49f'
            assert old['certificate_stream_sha256']=='b0ab2fd44f64015b0ae1caa954c3dad76be44c02833cec62d79c2df6c1f3dacb'
    # Remaining independent groups correspond to the separately bounded v2.
    extra=[(ident,len(group)) for ident,group in exgroups]
    assert sum(n for _,n in extra)==104
    result['late']=audit_late(independent)
    after=integrity()
    assert before==after
    result.update({'complete':True,'verified_rows':total,'coefficient_stream_sha256':old_coeff_hash.hexdigest(),
                   'root_certificate_stream_sha256':old['certificate_stream_sha256'],
                   'all_immutable_artifacts_unchanged':True,'integrity_after':after,
                   'independent_source_sha256':sha(HERE/'J16-digits-review-2-independent.py'),
                   'all_affine_matrices_checked_by_361_pairs':len(R.VALIDATED),
                   'distinct_recorded_augmented_row_spaces_checked':len(rrefspaces),
                   'seconds':time.monotonic()-start})
    R.save('artifact-full-result',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('integrity_before','integrity_after')}),flush=True)

if __name__=='__main__':
    main()
