#!/usr/bin/env python3
"""Validate frozen artifacts against independent reconstruction and raw bytes."""
import collections
import gzip
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "problems/2021-B4"
REV = BASE / "reviews"
spec = importlib.util.spec_from_file_location("independent_r1", REV / "J16-digits-review-1-verifier.py")
r1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r1)


def read(p):
    return json.loads(Path(p).read_text())


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    joint = BASE / "notes/coordinator-J16-coupled-digit-candidate-v1-manifest.json"
    assert sha(joint) == "b9e20e7634f94f2ad34055f5da2efd0460e5645d9c3d8933800bd4892321d2ad"
    m = read(joint)
    artifacts = []
    for a in m["artifacts"]:
        p = ROOT / a["path"]
        h, n = sha(p), p.stat().st_size
        assert h == a["sha256"] and n == a["bytes"], ("artifact-hash-or-size", str(p))
        artifacts.append({"path":a["path"], "bytes":n, "sha256":h, "matched":True})
    assert len(artifacts) == 46
    old = read(BASE / "notes/coordinator-J16-coupled-leading-candidate-v1-manifest.json")
    for a in old["artifacts"]:
        p = ROOT / a["path"]
        assert sha(p) == a["sha256"] and p.stat().st_size == a["bytes"]

    data, branches, tests, bounds, before = r1.leading_cover()
    accepted = read(REV / "newton-review-1-extension-result.json")["retained_masks"]["16"]
    assert accepted == list(data), "accepted-88-mask-list"
    leading = read(BASE / "computations/coordinator-J16-coupled-leading-v1-result.json")
    index = read(BASE / "computations/coordinator-J16-leading-branch-index-v1-result.json")
    assert tests == leading["projected_label_and_nu_tests"] == index["projected_label_and_nu_tests"]
    grouped = collections.defaultdict(list)
    for branch in branches:
        grouped[branch[0]].append(branch)
    assert leading["retained_masks"] == index["retained_masks"] == sorted(grouped)
    assert leading["excluded_masks"] == index["excluded_masks"] == sorted(set(data)-set(grouped))
    assert leading["rows"] == index["rows"]
    assert len(leading["rows"]) == len(data) == 88
    hist = collections.Counter()
    for row in leading["rows"]:
        mask = row["center_mask"]
        dd = data[mask]
        aa = dd["a0"]
        assert row["H2_center"] == r1.center(mask,18)
        assert row["H3_center"] == r1.center(mask,17)
        assert row["minimum_valuation_upper_bound"] == dd["bound"]
        assert row["active_positions"] == dd["active"]
        count = (3**len(dd["active"])) * sum(aa[17] % (19**nu) == 0 and aa[18] % (19**nu) == 0
                                                   for nu in range(1,dd["bound"]+1))
        assert row["projected_label_and_nu_tests"] == count
        counts = dict(collections.Counter("nu"+str(b[3]) for b in grouped[mask]))
        assert row["passing_leading_points"] == counts
        assert row["excluded_by_this_necessary_projection"] == (not bool(grouped[mask]))
        hist[str((r1.center(mask,18),r1.center(mask,17)))+" excluded="+str(not bool(grouped[mask]))] += 1
        for valkey, example in row["first_examples"].items():
            nu = int(valkey[2:])
            b = next(b for b in grouped[mask] if b[3] == nu)
            mm, uu, vv, nn, x, y = b
            labels = [1 if uu & (1 << (j-2)) else 2 if vv & (1 << (j-2)) else 0 for j in dd["active"]]
            assert example["active_labels"] == labels
            assert example["residue_U_V"] == [x,y]
            ax,ay,rows = r1.linear_rows(mask,uu,vv,aa)
            q = 19**nu
            c4 = r1.BETA[16]*aa[16] % 19
            eqs = [[dd["q0"]//q, sum(r1.BETA[j]*ax[j] for j in range(2,19)), sum(r1.BETA[j]*ay[j] for j in range(2,19))],
                   [aa[18]//q,ax[18],ay[18]],
                   [r1.BETA[17]*(aa[17]//q),r1.BETA[17]*ax[17]+c4,r1.BETA[17]*ay[17]+c4]]
            assert example["equations"] == eqs
    assert dict(hist) == leading["histogram"] == index["histogram"]
    independent_index = []
    for mask,umask,vmask,nu,x,y in branches:
        dd=data[mask]
        labels=[1 if umask & (1 << (j-2)) else 2 if vmask & (1 << (j-2)) else 0 for j in dd["active"]]
        independent_index.append({"center_mask":mask,"nu":nu,"active_positions":dd["active"],
                                  "active_labels":labels,"U":x,"V":y,"inactive_positions":dd["inactive"],
                                  "full_label_expansions":3**len(dd["inactive"])})
    assert independent_index == index["leading_branches"]
    assert sum(b["full_label_expansions"] for b in independent_index) == index["expanded_label_residue_branches"] == 840396

    chunks=[]
    prefix_lines=[]
    stream=hashlib.sha256()
    counts=collections.Counter()
    per_mask=collections.defaultdict(lambda:[0,0])
    for path in sorted((BASE / "computations").glob("coordinator-J16-second-digit-v1-certificates-0*.jsonl.gz")):
        n=0
        with gzip.open(path,"rb") as f:
            for line in f:
                stream.update(line)
                n+=1
                row=json.loads(line)
                if len(prefix_lines)<8192:
                    prefix_lines.append(line)
                counts[(row[9],bool(row[10]))]+=1
                per_mask[row[0]][0]+=1
                per_mask[row[0]][1]+=row[10]
        chunks.append({"path":str(path.relative_to(ROOT)),"rows":n,"bytes":path.stat().st_size,"sha256":sha(path)})
    assert len(chunks)==15
    assert [c["rows"] for c in chunks]==[60000]*14+[396]
    result=read(BASE / "computations/coordinator-J16-second-digit-v1-result.json")
    assert result["chunks"]==chunks
    assert stream.hexdigest()==result["certificate_stream_sha256"]
    assert result["visited"]==sum(c["rows"] for c in chunks)==840396
    assert result["passing"]==sum(v[1] for v in per_mask.values())==125346
    assert result["per_mask_tested_passing"]=={str(k):v for k,v in per_mask.items()}
    assert result["rank_histogram"]=={str(k[0])+" consistent="+str(k[1]):v for k,v in counts.items()}
    assert result["candidate_remaining_J16_masks"]==sorted(k for k,v in per_mask.items() if v[1])
    assert result["old_leading_exclusions"]==leading["excluded_masks"]
    assert result["source_sha256"]==sha(BASE / "computations/coordinator-J16-leading-branch-index-v1-result.json")
    benchmark=BASE / "computations/coordinator-J16-second-digit-v1-benchmark-certificates-001.jsonl.gz"
    with gzip.open(benchmark,"rb") as f:
        benchmark_raw=f.read()
    assert benchmark_raw==b"".join(prefix_lines)
    br=read(BASE / "computations/coordinator-J16-second-digit-v1-benchmark-result.json")
    assert br["visited"]==8192 and br["limit"]==8192
    assert br["certificate_stream_sha256"]==hashlib.sha256(benchmark_raw).hexdigest()
    assert br["candidate_remaining_J16_masks"] is None
    output={"status":"all-artifacts-and-leading-data-checked", "joint_manifest_sha256":sha(joint),
            "joint_artifact_count":len(artifacts),"joint_artifacts":artifacts,
            "leading_manifest_artifact_count":len(old["artifacts"]),
            "accepted_mask_list_matched":True,"leading_rows_checked":88,
            "leading_projected_checks":tests,"leading_preprerequisite_checks":before,
            "leading_branches_checked":len(branches),"expansions_checked":840396,
            "all_chunk_rows_checked":sum(c["rows"] for c in chunks),"chunks":chunks,
            "certificate_stream_sha256":stream.hexdigest(),
            "benchmark_equal_to_first_8192_full_rows":True,
            "result_counts_and_mask_lists_match_all_rows":True}
    (REV / "J16-digits-review-1-artifact-check.json").write_text(json.dumps(output,indent=2,sort_keys=True)+"\n")
    print(json.dumps({k:v for k,v in output.items() if k not in ("joint_artifacts","chunks")}),flush=True)


if __name__=="__main__":main()
