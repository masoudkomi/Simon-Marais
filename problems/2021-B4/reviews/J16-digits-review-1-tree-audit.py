#!/usr/bin/env python3
"""Constructor-format adapter; all mathematics comes from independent R1 code."""
import argparse
import collections
import gzip
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import sys
import time
sys.dont_write_bytecode=True
REV=Path(__file__).resolve().parent
BASE=REV.parent
ROOT=BASE.parents[1]
COMP=BASE/"computations"
spec=importlib.util.spec_from_file_location("r1tree",REV/"J16-digits-review-1-tree-independent.py")
tree=importlib.util.module_from_spec(spec)
spec.loader.exec_module(tree)
b=tree.base


def read(p):return json.loads(Path(p).read_text())
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def enc(o):return (json.dumps(o,separators=(",",":"))+"\n").encode()


def streams(info):
    digest=hashlib.sha256()
    total=0
    for chunk in info["chunks"]:
        p=ROOT/chunk["path"]
        assert sha(p)==chunk["sha256"] and p.stat().st_size==chunk["bytes"]
        n=0
        with gzip.open(p,"rb") as f:
            for line in f:
                n+=1;total+=1;digest.update(line)
                yield json.loads(line),line
        assert n==chunk["rows"]
    assert total==info["rows"] and digest.hexdigest()==info["plain_sha256"]


def manifests():
    out=[]
    for name,expected,count in [
      ("owner-J16-Hensel-v1-manifest.json","2f5eec6a98e0ff8c264259a508868c3d0e5f5befa8de833a9434dfd7fc069f6a",53),
      ("owner-J16-Hensel-v2-manifest.json","8b9cd2bbcf1740cb119436d58eb4a9f60dbf7afe5e9d23f077e1bc7428d75db8",14)]:
        path=BASE/"notes"/name
        assert sha(path)==expected
        mm=read(path)
        assert len(mm["artifacts"])==mm["artifact_count"]==count
        for a in mm["artifacts"]:
            p=ROOT/a["path"]
            assert sha(p)==a["sha256"] and p.stat().st_size==a["bytes"],("artifact",p)
        out.append({"path":str(path.relative_to(ROOT)),"sha256":expected,"all_matched":True,"artifacts":mm["artifacts"]})
    return out


def old_rows():
    for p in sorted(COMP.glob("coordinator-J16-second-digit-v1-certificates-0*.jsonl.gz")):
        with gzip.open(p,"rt") as f:
            for line in f:yield json.loads(line)


def check_self_test(data,mat):
    packet=read(COMP/"owner-J16-Hensel-v1-self-test.json")
    assert packet["case_count"]==len(packet["cases"])==12
    for row in packet["cases"]:
        key=tuple(row["key"])
        exact=tree.exact(key,1)
        matrix=mat(key)
        assert row["integer_a"]==exact["a"]
        assert row["integer_F"]==exact["F"]
        assert row["integer_R0_R1"]==[exact["R0"],exact["R1"]]
        assert row["exact_E"]==[[e.numerator,e.denominator] for e in exact["E_fraction"]]
        assert row["jacobian"]==matrix
        for saved in row["modular"]:
            k=saved["k"]
            aa,mod,ee=tree.evaluate(key,k)
            exact=tree.exact(key,k)
            assert [a%mod for a in aa]==[a%mod for a in exact["a"]]
            assert saved=={"k":k,"E_mod":ee,"a_modulus":mod}
            assert ee==exact["E"]
            pk=19**k
            for col in (0,1):
                shifted=list(key);shifted[4+col]+=pk
                new=tree.evaluate(shifted,k)[2]
                assert [((x-y)%(19*pk))//pk for x,y in zip(new,ee)]==[r[col] for r in matrix]
        lift=tree.lift(key,1,matrix)
        brute=[[x,y] for x in range(19) for y in range(19)
               if all((r[0]*x+r[1]*y+c)%19==0 for r,c in zip(matrix,lift["constants"]))]
        assert sorted(row["digit_solutions"])==lift["digits"]==brute
        assert row["rank"]==lift["rank"] and row["rref"]==lift["rref"]
    assert sha(COMP/"owner-J16-Hensel-v1-benchmark-self-test.json")==sha(COMP/"owner-J16-Hensel-v1-self-test.json")
    return 12


def exact_fields(row,key,k,matrix):
    ex=tree.exact(key,k)
    assert row["integer_a"]==ex["a"]
    assert row["integer_F"]==ex["F"]
    assert row["integer_R0_R1"]==[ex["R0"],ex["R1"]]
    assert row["exact_E"]==[[z.numerator,z.denominator] for z in ex["E_fraction"]]
    assert row["jacobian_mod19"]==matrix
    assert row["rank"]==2
    return ex


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--limit",type=int,default=0)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    start=time.monotonic()
    def emit(o):print(json.dumps(o,sort_keys=True),flush=True)
    manifest_checks=manifests()
    data,branches,tests,bounds,before=b.leading_cover()
    active_masks={m:sum(1<<(j-2) for j in d["active"]) for m,d in data.items()}
    matrices={}
    def matrix(key):
        m,um,vm=key[:3]
        ck=m,um&active_masks[m],vm&active_masks[m]
        if ck not in matrices:
            matrices[ck]=b.linear_rows(m,um,vm,data[m]["a0"])[2]
        return matrices[ck]
    expected=set(b.expanded_keys(data,branches))
    assert len(expected)==840396
    selftests=check_self_test(data,matrix)
    result={"status":"incomplete", "constructor_imports":False,"initial_expected":len(expected),
            "manifest_checks":manifest_checks,"selftest_exact_cases_checked":selftests,
            "initial_independent_tree_source_sha256": "1b9740ec4f47d90e30f4a3f6e299993617df1dd98cd90145390081aec971e5a8",
            "tree_source_sha256":sha(REV/"J16-digits-review-1-tree-independent.py"),"levels":[]}
    v1=read(COMP/"owner-J16-Hensel-v1-result.json")
    previous=old_rows()
    assert len(v1["levels"])==3
    benchmark_prefix_hash=hashlib.sha256()
    benchmark_children=set()
    benchmark_tally=collections.Counter()
    benchmark_masks=collections.defaultdict(lambda:[0,0,0])
    for k,level in enumerate(v1["levels"],1):
        assert k==level["input_precision"]
        assert len(expected)<=1000000
        input_n=len(expected)
        assert level["input_expected_nodes"]==input_n
        next_layer=set()
        tally=collections.Counter()
        masks=collections.defaultdict(lambda:[0,0,0])
        visited=generated=0
        for row,raw in streams(level["certificates"]):
            key=tuple(row[0])
            assert key in expected,("missing-or-duplicate-node",k,key)
            expected.remove(key)
            calc=tree.lift(key,k,matrix(key))
            aa=[x%calc["modulus"] for x in calc["a"]]
            assert row[1]==calc["modulus"] and row[2]==aa,("coefficients",k,key)
            assert row[3]==calc["E"] and row[4]==calc["matrix"],("E-or-matrix",k,key)
            assert row[5]==calc["rank"] and row[6]==calc["rref"],("rank-or-rref",k,key)
            assert row[7]==("accepted_T1_missing_label" if calc["pruned"] else None)
            expected_digits=[] if calc["pruned"] else calc["digits"]
            assert sorted(row[8])==expected_digits,("digits",k,key)
            if k==1:
                old=next(previous)
                assert old==list(key)+calc["constants"]+[calc["rank"],int(bool(calc["digits"]))]
            tally[f'rank{calc["rank"]}_consistent{bool(calc["digits"])}']+=1
            if calc["pruned"]:tally["pruned_by_accepted_T1_missing_label"]+=1
            masks[key[0]][0]+=1
            masks[key[0]][1]+=bool(expected_digits)
            masks[key[0]][2]+=len(calc["children"])
            for child in calc["children"]:
                assert child not in next_layer,("duplicate-child",k,child)
                next_layer.add(child)
            generated+=len(calc["children"])
            visited+=1
            assert generated<=1000000
            if k==1 and visited<=8192:
                benchmark_prefix_hash.update(raw)
                benchmark_children.update(calc["children"])
                benchmark_tally[f'rank{calc["rank"]}_consistent{bool(calc["digits"])}']+=1
                if calc["pruned"]:benchmark_tally["pruned_by_accepted_T1_missing_label"]+=1
                benchmark_masks[key[0]][0]+=1
                benchmark_masks[key[0]][1]+=bool(expected_digits)
                benchmark_masks[key[0]][2]+=len(calc["children"])
            if visited%8192==0:
                emit({"phase":"tree-checkpoint","precision":k,"checked":visited,
                      "generated":generated,"seconds":round(time.monotonic()-start,3)})
            if args.limit and k==1 and visited>=args.limit:
                result.update(benchmark_visited=visited,benchmark_generated=generated,
                              seconds=round(time.monotonic()-start,3),status="incomplete benchmark; no exclusion")
                Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
                emit({"phase":"benchmark-finished","checked":visited,"generated":generated,
                      "seconds":result["seconds"]})
                return
        assert not expected,("unprocessed-layer",k,len(expected))
        assert visited==level["input_visited"]==input_n
        assert generated==level["generated_nodes"]==len(next_layer)
        assert level["complete_input_traversal"] and level["stopped"] is None
        assert dict(tally)==level["tally"]
        # JSON map keys are strings; keep all 70 masks including zero rows.
        for m in level["per_mask_visited_passing_generated"]:
            assert level["per_mask_visited_passing_generated"][m]==masks[int(m)]
        left=next_layer.copy()
        node_n=0
        for node,raw in streams(level["nodes"]):
            node=tuple(node)
            assert node in left,("node-stream-extra-or-duplicate",k,node)
            left.remove(node);node_n+=1
        assert not left and node_n==generated
        assert all((m,vm,um,nu,y,x) in next_layer for m,um,vm,nu,x,y in next_layer)
        summary={"input_precision":k,"input_nodes":visited,"output_nodes":generated,
                 "output_masks":len({n[0] for n in next_layer}),"tally":dict(tally),
                 "certificate_plain_sha256":level["certificates"]["plain_sha256"],
                 "node_plain_sha256":level["nodes"]["plain_sha256"],
                 "complete_coverage":True,"all_coefficient_residual_matrix_digits_matched":True,
                 "swap_closure":True}
        result["levels"].append(summary)
        emit({"phase":"tree-layer-complete",**summary,"seconds":round(time.monotonic()-start,3)})
        expected=next_layer
    assert next(previous,None) is None
    assert len(expected)==90
    result["precision4_keys"]=sorted(map(list,expected))
    assert all(b.affine_cramer(matrix(key),[0,0,0])[0]==2 for key in expected)
    result["constant_rank2_future_bound"]=90
    post=read(COMP/"owner-J16-Hensel-v1-postcheck-result.json")
    assert post["nodes"]==90 and post["precision"]==4 and post["all_rank_two"]
    assert {tuple(s["key"]) for s in post["states"]}==expected
    for row in post["states"]:
        key=tuple(row["key"])
        mm=matrix(key)
        ex=exact_fields(row,key,4,mm)
        assert all(e.numerator%(19**4)==0 for e in ex["E_fraction"])
        minors=[[i,j,(mm[i][0]*mm[j][1]-mm[i][1]*mm[j][0])%19]
                for i in range(3) for j in range(i+1,3)]
        assert row["two_by_two_minors"]==minors and any(r[2] for r in minors)
    result["all_90_postcheck_exact_states_verified"]=True

    v2=read(COMP/"owner-J16-Hensel-v2-result.json")
    rows=[json.loads(line) for line in (COMP/"owner-J16-Hensel-v2-certificates.jsonl").read_text().splitlines()]
    assert len(rows)==104
    obs=read(COMP/"owner-J16-Hensel-v2-obstructions-result.json")
    obmap={(r["input_precision"],tuple(r["key"])):r for r in obs["certificates"]}
    assert len(obmap)==104
    all_obstructions=[]
    v2summary=[]
    for k,level in zip((4,5),v2["levels"]):
        layer=[r for r in rows if r["input_precision"]==k]
        assert len(layer)==len(expected)==level["input_nodes"]
        next_layer=set()
        tally=collections.Counter()
        for row in layer:
            key=tuple(row["key"])
            assert key in expected
            expected.remove(key)
            mm=matrix(key)
            calc=tree.lift(key,k,mm)
            ex=exact_fields(row,key,k,mm)
            assert ex["E"]==calc["E"]==row["E_mod"]
            assert row["E_modulus"]==19**(k+1)
            assert row["affine_constants"]==calc["constants"]
            assert row["rref"]==calc["rref"] and row["digits"]==calc["digits"]
            brute=[[x,y] for x in range(19) for y in range(19)
                   if all((r[0]*x+r[1]*y+c)%19==0 for r,c in zip(mm,calc["constants"]))]
            assert brute==calc["digits"]
            assert sorted(map(tuple,row["children"]))==sorted(calc["children"])
            for child in calc["children"]:
                assert child not in next_layer
                next_layer.add(child)
            lam,ob=tree.obstruction(mm,calc["constants"])
            o=obmap[(k,key)]
            assert o=={"key":list(key),"input_precision":k,"matrix":mm,
                       "constants":calc["constants"],"left_kernel":lam,"obstruction_mod19":ob,
                       "digits":calc["digits"],"children":[list(c) for c in calc["children"]]}
            assert bool(calc["children"])==(ob==0)
            all_obstructions.append(o)
            tally["consistent" if calc["children"] else "inconsistent"]+=1
        assert not expected
        assert len(next_layer)==level["output_nodes"]<=90
        assert {tuple(n) for n in level["output_states"]}==next_layer
        assert dict(tally)==level["histogram"]
        v2summary.append({"input_precision":k,"input_nodes":len(layer),"output_nodes":len(next_layer),
                          "histogram":dict(tally),"all_exact_values_and_obstructions_verified":True})
        expected=next_layer
    assert not expected and v2["last_complete_precision"]==6
    assert v2["last_output_nodes"]==0 and v2["target_precision"]==8
    assert v2["candidate_masks_at_last_complete_precision"]==[]
    assert obs["chain"]==[90,14,0] and obs["rows"]==104
    result["v2_levels"]=v2summary
    result["obstructions"]=all_obstructions
    result["all_104_exact_systems_checked"]=True

    # Benchmark files must encode the independently verified full-prefix data.
    bm=read(COMP/"owner-J16-Hensel-v1-benchmark-result.json")
    bl=bm["levels"][0]
    assert len(bm["levels"])==1 and bl["input_visited"]==8192
    assert bl["generated_nodes"]==len(benchmark_children)==2666
    assert bl["tally"]==dict(benchmark_tally)
    benchmark_records=list(streams(bl["certificates"]))
    assert hashlib.sha256(b"".join(raw for row,raw in benchmark_records)).hexdigest()==benchmark_prefix_hash.hexdigest()
    assert {tuple(n) for n,raw in streams(bl["nodes"])}==benchmark_children
    assert not bl["complete_input_traversal"]
    for m in bl["per_mask_visited_passing_generated"]:
        assert bl["per_mask_visited_passing_generated"][m]==benchmark_masks[int(m)]
    rawv2=(COMP/"owner-J16-Hensel-v2-certificates.jsonl").read_bytes().splitlines(keepends=True)
    assert (COMP/"owner-J16-Hensel-v2-benchmark-certificates.jsonl").read_bytes()==b"".join(rawv2[:90])
    bv2=read(COMP/"owner-J16-Hensel-v2-benchmark-result.json")
    assert len(bv2["levels"])==1 and bv2["levels"][0]==v2["levels"][0]
    result.update(status="complete independent L1-L4 finite reconstruction; no promotion",
                  tree=[840396,361194,2026,90,14,0],
                  records_checked=840396+361194+2026+104,
                  v1_benchmark_entire_prefix_verified=True,v2_benchmark_entire_prefix_verified=True,
                  final_precision=6,final_nodes=0,combined_necessary_mask_count=772-88,
                  seconds=round(time.monotonic()-start,3),python=sys.version)
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    emit({k:v for k,v in result.items() if k not in ("manifest_checks","precision4_keys","obstructions")})


if __name__=="__main__":main()
