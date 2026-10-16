#!/usr/bin/env python3
"""Preserve exact earlier review source versions and freeze the blind report."""
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
REV=Path(__file__).resolve().parent
BASE=REV.parent
ROOT=BASE.parents[1]
PFX="J16-digits-review-1"


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())


def snapshot(name,text,expected):
    raw=text.encode()
    assert hashlib.sha256(raw).hexdigest()==expected,("snapshot-reconstruction",name,hashlib.sha256(raw).hexdigest())
    target=REV/name
    if target.exists():assert target.read_bytes()==raw
    else:target.write_bytes(raw)
    return {"path":str(target.relative_to(ROOT)),"sha256":expected}


def main():
    snapshots=[]
    code=(REV/(PFX+"-verifier.py")).read_text()
    code=code.replace("    before_prerequisites = 0\n","")
    code=code.replace("                before_prerequisites += 1\n                q = P**nu\n                if aa[17] % q or aa[18] % q:\n                    continue\n                checks += 1\n",
                      "                checks += 1\n                q = P**nu\n                if aa[17] % q or aa[18] % q:\n                    continue\n")
    code=code.replace("return data, branches, checks, dict(bounds), before_prerequisites","return data, branches, checks, dict(bounds)")
    start=code.index("def affine_cramer(")
    end=code.index("def main():",start)
    code=code[:start]+code[end:]
    code=code.replace("data, branches, checks, bounds, before_prerequisites = leading_cover()","data, branches, checks, bounds = leading_cover()")
    code=code.replace("                  leading_checks_before_constant_prerequisites=before_prerequisites,\n","")
    code=code.replace("    constructor_coeff_hash = hashlib.sha256()\n    per_mask = collections.defaultdict(lambda: [0,0])\n    boundary = collections.Counter()\n","")
    code=code.replace('        assert (rank, consistent) == affine_cramer(jrows, constants), ("affine-method-disagreement", key)\n',"")
    start=code.index("        constructor_coeff_hash.update(")
    end=code.index("        n += 1\n",start)
    code=code[:start]+"        totals[(nu, rank, consistent)] += 1\n        if consistent:\n            passed[mask] += 1\n"+code[end:]
    code=code.replace("                  constructor_scalar_stream_sha256=constructor_coeff_hash.hexdigest(),\n                  per_mask_tested_passing=dict(per_mask),\n                  boundary_case_counts=dict(boundary),\n","")
    snapshots.append(snapshot(PFX+"-verifier-initial-v0.py",code,"b53811a0f4a7c30c5492e662a9e496e3ba6263a36eb6c0138c7f6141fbd2ac8d"))
    code=(REV/(PFX+"-tree-independent.py")).read_text()
    code=code.replace("assert bool(points)==(not any(r[0]==r[1]==0 and r[2] for r in reduced))",
                      "assert bool(points)==not any(r[0]==r[1]==0 and r[2] for r in reduced)")
    snapshots.append(snapshot(PFX+"-tree-precomparison-v0.txt",code,"1b9740ec4f47d90e30f4a3f6e299993617df1dd98cd90145390081aec971e5a8"))
    code=(REV/(PFX+"-tree-audit.py")).read_text()
    code=code.replace("        # JSON map keys are strings; keep all 70 masks including zero rows.\n",
       '        saved_masks={str(m):masks[m] for m in v1["levels"][0]["per_mask_visited_passing_generated"]}\n'
       "        # JSON map keys are strings; keep all 70 masks including zero rows.\n")
    snapshots.append(snapshot(PFX+"-tree-audit-benchmark-v0.py",code,"82c5a554f618a388ad1839163c0583f00e2bff0ab2905c99c88f9082e33dc016"))

    artifact_count=0
    for name,expected in [
       ("coordinator-J16-coupled-digit-candidate-v1-manifest.json","b9e20e7634f94f2ad34055f5da2efd0460e5645d9c3d8933800bd4892321d2ad"),
       ("owner-J16-Hensel-v1-manifest.json","2f5eec6a98e0ff8c264259a508868c3d0e5f5befa8de833a9434dfd7fc069f6a"),
       ("owner-J16-Hensel-v2-manifest.json","8b9cd2bbcf1740cb119436d58eb4a9f60dbf7afe5e9d23f077e1bc7428d75db8")]:
        mm=BASE/"notes"/name
        assert sha(mm)==expected
        for row in read(mm)["artifacts"]:
            path=ROOT/row["path"]
            assert sha(path)==row["sha256"] and path.stat().st_size==row["bytes"]
            artifact_count+=1
    assert artifact_count==113
    provenance=read(BASE/"computations/coordinator-J16-leading-branch-index-v1-provenance.json")
    source=(ROOT/provenance["source"]).read_text()
    for old,new in provenance["exact_replacements"]:
        assert source.count(old)==1
        source=source.replace(old,new)
    assert source==(ROOT/provenance["new_source"]).read_text()

    old=read(BASE/"computations/coordinator-J16-second-digit-v1-result.json")
    ours=read(REV/(PFX+"-result.json"))
    assert ours["status"]=="complete" and ours["records_checked"]==840396 and ours["missing_keys"]==0
    assert ours["row_stream_sha256"]==old["certificate_stream_sha256"]
    assert ours["constructor_scalar_stream_sha256"]==old["scalar_coefficient_stream_sha256"]
    assert ours["per_mask_tested_passing"]==old["per_mask_tested_passing"]
    assert ours["next_retained"]==old["candidate_remaining_J16_masks"]
    tree=read(REV/(PFX+"-tree-result.json"))
    assert tree["tree"]==[840396,361194,2026,90,14,0]
    assert tree["records_checked"]==1203720
    assert tree["final_nodes"]==0 and tree["final_precision"]==6
    assert tree["all_104_exact_systems_checked"] and tree["all_90_postcheck_exact_states_verified"]
    owner2=read(BASE/"computations/owner-J16-Hensel-v2-result.json")
    assert len(owner2["levels"])==2
    assert tree["tree_source_sha256"]==sha(REV/(PFX+"-tree-independent.py"))

    # Exact independent q0 values and active/inactive partitions are archived.
    spec=importlib.util.spec_from_file_location("r1final",REV/(PFX+"-verifier.py"))
    r1=importlib.util.module_from_spec(spec);spec.loader.exec_module(r1)
    constants=[]
    for mask in ours["independent_mask_list"]:
        aa=r1.constant_coefficients(mask)
        q0=-1+sum(r1.BETA[j]*aa[j] for j in range(2,19))
        constants.append({"mask":mask,"a0":aa,"q0":q0,"valuation_q0":r1.valuation(q0),
                          "active":[j for j in range(2,19) if not r1.center(mask,j) and aa[j-1]%19],
                          "inactive":[j for j in range(2,19) if not r1.center(mask,j) and not aa[j-1]%19]})
    jobs=[]
    byhash={s["sha256"]:ROOT/s["path"] for s in snapshots}
    for path in sorted(REV.glob(PFX+"*-job.json")):
        job=read(path)
        assert job["status"]=="finished" and job["exit_code"]==0 and not job["timed_out"] and job["reaped"]
        assert job["timeout_seconds"]<=300
        for name,h in job["source_sha256"].items():
            source=ROOT/name
            assert sha(source)==h or (h in byhash and sha(byhash[h])==h)
        stem=str(path)[:-len("-job.json")]
        assert sha(stem+"-stdout.txt")==job["stdout_sha256"]
        assert sha(stem+"-stderr.txt")==job["stderr_sha256"]
        jobs.append({"path":str(path.relative_to(ROOT)),"child_pid":job["child_pid"],
                     "seconds":job["seconds"],"timeout_seconds":job["timeout_seconds"],"reaped":True})
    assert len(jobs)==5
    checks={"status":"all final crosschecks passed; initial blind audit complete",
            "artifact_records_rechecked":artifact_count,"exact_provenance_replacements_verified":True,
            "source_version_snapshots":snapshots,"jobs":jobs,
            "all_L3_result_hashes_and_mask_counts_match":True,"all_L4_layers_complete":True,
            "independent_exact_mask_constants":constants,
            "peer_conclusions_read":False,"substantive_open_issues":0,
            "promotion_performed":False,"telemetry":read(REV/(PFX+"-telemetry.json"))}
    (REV/(PFX+"-final-check.json")).write_text(json.dumps(checks,indent=2,sort_keys=True)+"\n")
    path=REV/(PFX+"-manifest.json")
    entries=[]
    for p in sorted(REV.glob(PFX+"*")):
        if p.is_file() and p!=path:
            entries.append({"path":str(p.relative_to(ROOT)),"bytes":p.stat().st_size,"sha256":sha(p)})
    manifest={"status":"frozen initial blind R1 report; recommend accept L1-L4; no promotion",
              "frozen_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "claims_audited":["L1","L2","L3","L4"],"peer_conclusions_read":False,
              "requested_settings":{"model":"gpt-6.1-sol","reasoning":"max"},
              "effective_setting_readback":"unavailable","artifacts":entries,
              "artifact_count":len(entries),"substantive_open_issues":0}
    path.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"manifest":str(path.relative_to(ROOT)),"sha256":sha(path),
                      "artifact_count":len(entries),"review_sha256":sha(REV/(PFX+".md")),
                      "issue_log_sha256":sha(REV/(PFX+"-issues.md")),
                      "tree_result_sha256":sha(REV/(PFX+"-tree-result.json")),
                      "status":manifest["status"]}),flush=True)


if __name__=="__main__":main()
