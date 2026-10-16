#!/usr/bin/env python3
"""Final frozen-data comparisons for R1's independent complex extension audit."""
from datetime import datetime,timezone
import hashlib
import json
import math
from pathlib import Path

root=Path(__file__).resolve().parents[3]
prefix=Path(__file__).with_name("three-complex-review-1")
comps=root/"problems/2021-B4/computations"
own=json.loads(Path(str(prefix)+"-full-result.json").read_text())
author=json.loads((comps/"coordinator-three-complex-witnesses-v1-result.json").read_text())
assert own["families"]==author["refinements"]==4731928
assert own["polynomial_stream_sha256"]==author["polynomial_stream_sha256"]=="49da0560f41fdf3fce8a1ed7e63e877b5d51533de93142d74be7129d3db04da2"
assert own["uncompressed_certificate_stream_sha256"]==author["uncompressed_certificate_stream_sha256"]=="e4dee952d410bf709b8c90dd61002ee88c4179a5fe7a8ca0678fe3644a25ffb1"
assert own["chunks"]==author["chunks"]
assert own["compressed_bytes"]==28442028
assert len(own["chunks"])==79
assert [c["rows"] for c in own["chunks"]]==[60000]*78+[51928]
expected={"0":5908,"101":4495784,"103":218175,"107":11555,"109":477,"127":26,"131":3}
assert own["certificate_histogram"]==expected
assert author["resolution_histogram"]=={"constant_nonzero":5908,**{k:v for k,v in expected.items() if k not in ("0","131")}}
assert author["unresolved"]==3 and author["resolved"]==4731925
for p in (101,103,107,109,127,131):
    assert all(p%d for d in range(2,math.isqrt(p)+1))

own_cases={(s["mask"],s["U_mask"]):s for s in own["sentinels"]}
assert set(own_cases)=={(117075,9220),(117075,1548),(117075,9356)}
unresolved=[json.loads(line) for line in (comps/"coordinator-three-complex-witnesses-v1-unresolved.jsonl").read_text().splitlines()]
assert len(unresolved)==3
for case in unresolved:
    key=(case["center_mask"],case["u_mask"])
    assert (case["P"],case["Q"])==(own_cases[key]["P"],own_cases[key]["Q"])
resolver=json.loads((comps/"coordinator-three-complex-witnesses-v1-resolve-result.json").read_text())
assert resolver["resolved"]==3 and resolver["unresolved"]==0 and len(resolver["cases"])==3
for case in resolver["cases"]:
    s=own_cases[(case["center_mask"],case["u_mask"])]
    assert case["prime"]==s["prime"]==131 and case["gcd_degree"]==0
    assert case["degrees"]==s["degrees"] and case["leading_residues"]==s["leading_residues"]
assert own_cases[(117075,9220)]["degrees"]==[15,20]
assert own_cases[(117075,1548)]["degrees"]==[12,20]
assert own_cases[(117075,9356)]["degrees"]==[15,20]
assert own_cases[(117075,9220)]["leading_residues"]==[83,3]
assert own_cases[(117075,1548)]["leading_residues"]==[44,79]
assert own_cases[(117075,9356)]["leading_residues"]==[97,124]

old_own_result=json.loads((prefix.parent/"three-witness-review-1-full-result.json").read_text())
old_author_result=json.loads((comps/"coordinator-three-witness-v2-result.json").read_text())
assert old_own_result["families"]==1493024
assert old_own_result["polynomial_stream_sha256"]==old_author_result["polynomial_stream_sha256"]=="aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad"
assert old_own_result["uncompressed_certificate_stream_sha256"]==old_author_result["uncompressed_certificate_stream_sha256"]=="4befc080569dbe0d4d978efaef502e51f644163d15ef9bd22ae7112cf1840387"
assert old_own_result["chunks"]==old_author_result["chunks"]
old_resolver=json.loads((comps/"coordinator-three-witness-v2-resolve-result.json").read_text())
assert old_resolver["resolved"]==1 and old_resolver["unresolved"]==0
old_case=old_resolver["cases"][0]
assert (old_case["center_mask"],old_case["u_mask"],old_case["prime"],old_case["gcd_degree"],old_case["degrees"],old_case["leading_residues"])==(6436,24785,131,0,[16,20],[8,102])
assert old_own_result["sentinel"][0]["mask"]==6436 and old_own_result["sentinel"][0]["U_mask"]==24785
union={k:expected[k]+old_own_result["certificate_histogram"][k] for k in expected}
assert sum(union.values())==6224952

derived=json.loads(Path(str(prefix)+"-independent-masks.json").read_text())
author_masks=json.loads((comps/"coordinator-three-complex-masks-v1-result.json").read_text())
assert derived["all_masks"]==author_masks["center_masks"]
assert derived["old_masks"]==author_masks["previously_certified_center_masks"]
assert derived["additional_masks"]==author_masks["additional_center_masks"]
assert {str(k):v for k,v in derived["J_histogram_diagnostic_only"].items()}==author_masks["J_histogram"]
assert author_masks["all_refinements"]==6224952 and author_masks["additional_refinements"]==4731928

provenance=json.loads((comps/"coordinator-three-complex-witnesses-v1-construction-provenance.json").read_text())
reconstructed=(root/provenance["source"]).read_text()
for old,new in provenance["exact_replacements"]:
    assert old in reconstructed
    reconstructed=reconstructed.replace(old,new)
assert reconstructed==(root/provenance["new_source"]).read_text()
old_resolver_source=(comps/"coordinator-three-witness-v2-resolve.py").read_text()
assert old_resolver_source.replace("coordinator-three-witness-v2","coordinator-three-complex-witnesses-v1")== (comps/"coordinator-three-complex-witnesses-v1-resolve.py").read_text()

manifest_path=root/"problems/2021-B4/notes/coordinator-three-complex-witnesses-v1-manifest.json"
assert hashlib.sha256(manifest_path.read_bytes()).hexdigest()=="d9210626ef24fe18ccde57706399d6c30a5fedb81d71a972da5e562a1c582ec8"
frozen=json.loads(manifest_path.read_text())
assert len(frozen["artifacts"])==154
for artifact in frozen["artifacts"]:
    path=root/artifact["path"]
    assert path.stat().st_size==artifact["bytes"]
    assert hashlib.sha256(path.read_bytes()).hexdigest()==artifact["sha256"]
old_manifest_path=prefix.parent/"three-witness-review-1-manifest.json"
assert hashlib.sha256(old_manifest_path.read_bytes()).hexdigest()=="f7f9d077585f699081c5fe337af925d2997f7453ce8e9e8a32f05039913695ca"
for artifact in json.loads(old_manifest_path.read_text())["artifacts"]:
    path=root/artifact["path"]
    assert path.stat().st_size==artifact["bytes"]
    assert hashlib.sha256(path.read_bytes()).hexdigest()==artifact["sha256"]

sources=[(".cache/literature/2021/cited-66c5af6a0f0239f5.pdf","https://arxiv.org/abs/1208.5404",[13]),
         (".cache/literature/2021/massri-1806.09561v6.pdf","https://arxiv.org/abs/1806.09561v6",[13,14])]
result={"verified_at_utc":datetime.now(timezone.utc).isoformat(),
        "all154_frozen_candidate_artifacts_match_before_and_after":True,
        "all_19_old_own_review_artifacts_and_manifest_unchanged":True,
        "all_masks_and_disjoint_union_independently_verified":True,
        "all4731928_complementary_families_regenerated_and_certified":True,
        "all79_new_chunk_hashes_bytes_and_counts_match":True,
        "both_new_complete_stream_hashes_match":True,
        "all_three_new_sentinels_and_exact_integer_polynomials_match":True,
        "new_mod131_resolver_fully_matches_independent_regeneration":True,
        "old_separate_mod131_certificate_still_explicit_required_dependency":True,
        "old25_chunks_are_accepted_finite_data_hash_verified_not_freshly_recomputed":True,
        "constructor_copy_and_resolver_copy_provenance_verified_exactly":True,
        "union_certificate_histogram":union,
        "ramification_check":{"pi_squared":19,"v_pi":"1/2","D2_equation":"a2=2*pi-pi^2",
                              "v_a2":"1/2","v_ordinary_c18":"3/2",
                              "meaning":"local derivative example only, not a CA counterexample"},
        "primary_sources":[{"path":path,"url":url,"pdf_pages_one_based":pages,
                            "sha256":hashlib.sha256((root/path).read_bytes()).hexdigest()} for path,url,pages in sources],
        "telemetry_entry_and_midrun":{"total_weekly_used_percent":11,"window_minutes":10080,
                                     "reset_unix_seconds":1792745187,"stop_at_total_percent":90},
        "requested_model":"gpt-6.1-sol","requested_reasoning_effort":"max","verified_effective_settings":None}
Path(str(prefix)+"-postcheck-result.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({k:v for k,v in result.items() if isinstance(v,bool)}))
