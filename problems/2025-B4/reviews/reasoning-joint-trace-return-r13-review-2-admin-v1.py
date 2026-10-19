"""NEW JT13 review documentary SHA/JSON helper only: never mathematical code.
No author/source/old helper execution, network, peer inventory, or old mutation.
prepare captures the finite necessary guard SET; freeze binds four new payloads
only AFTER their final MODEL readbacks; verify is a separate read-only pass.
"""
import datetime
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
BASE = "problems/2025-B4/reviews/reasoning-joint-trace-return-r13-review-2-"
AUTHOR = "problems/2025-B4/notes/reasoning-joint-trace-return-r13-freeze-v1.json"
PARENT = "problems/2022-B4/reviews/reasoning-physical-return-r13-review-1-manifest-v1.json"
EXPECTED = """AGENTS.md|4707|28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff
problems/2025-B4/statement.md|2024|af0075dd635e8e4d31bb3ae9148d1731a7fbb57c06cf104763332e1496673f59
problems/2025-B4/proofs/reviewed-reasoning-exception-return-r12-v1.1.md|32008|4954539d16386f5aa80ee58afd1897b02148ef0d045feb05d196663298285fcb
problems/2025-B4/reviews/reasoning-exception-return-r12-acceptance.md|6569|80d2bf548bd1bae4f0aa6ce00ff76260152d9e1a1fd74d0a9545003cb399e26c
problems/2025-B4/reviews/reasoning-exception-return-r12-acceptance.json|3445|aa80d2fb646d1359fdc9f52a28dab82a2bdabc05bddf223c1a56708f56309ed2
problems/2025-B4/proofs/reviewed-reasoning-compatible-return-r10-v1.1.md|26605|dbbce8dcc26f1251e30c3ab939dd013062fe96bf98652fd06a2bb53bff527448
problems/2025-B4/reviews/reasoning-compatible-return-r10-acceptance.md|6568|d755581c3a022e6c5e6517f24a38b4ca550df7e8ee35cf6a06c59a01b9928051
problems/2025-B4/reviews/reasoning-compatible-return-r10-acceptance.json|4090|3038ec356defebb77464a4b34a5534a7121d9e00fd65e208d7434c582facf565
problems/2025-B4/proofs/reviewed-reasoning-global-return-r11-v1.1.md|32026|6a72f0d8348fc39f6343a3381975f8fbc02bc001036bc88acbd32a93a51f1196
problems/2025-B4/reviews/reasoning-global-return-r11-acceptance.md|6200|a0b01f127da4c9538d560d8ee9e6ffeeeb2bd9954bad98a9d17c0dfe1050434f
problems/2025-B4/reviews/reasoning-global-return-r11-acceptance.json|3480|70872a5fc214d3b390ebf69837e75b07bb06cadbf1bf6a8dbe9f34b2ce1ef008"""

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def row(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def expect(record):
    actual = row(record["path"])
    assert actual == record, (record["path"], actual, record)
    return actual

def read(path):
    return json.loads((ROOT / path).read_text())

def write_new(path, value):
    with (ROOT / path).open("x") as handle:
        handle.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

def digest(records):
    return hashlib.sha256(json.dumps(sorted(records, key=lambda r:r["path"]), sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def prepare():
    author_row = expect({"path":AUTHOR,"bytes":2115,"sha256":"c797b85ac45ac25e2c8155a62c2d768f721538650d97c925dcd1210502a22075"})
    author = read(AUTHOR)
    assert author["ALL_obligations"] == 32 and author["ENTIRE_files"] == 5
    records = [author_row] + [expect(r) for r in author["payloads"]]
    for literal in EXPECTED.splitlines():
        path, size, sha = literal.split("|")
        records.append(expect({"path":path,"bytes":int(size),"sha256":sha}))
    parent = expect({"path":PARENT,"bytes":2632,"sha256":"781950158696b464031a0c40dd96b3ea7eb2bd560a4599b3fa5f263c83be5cc0"})
    records.append(parent)
    assert len(records) == 17 and len({r["path"] for r in records}) == 17
    baseline = {"captured_UTC":now(),"necessary_immutable_records":records,
      "guard_occurrences":17,"guard_unique_paths":17,"canonical_deduplicated_sha256":digest(records),
      "ONE_compact_OWN_parent":parent,"recursive_parent_inventory_expansion":False,
      "living_maps_are_guards":False,"author_or_old_code_executed":False,
      "NEW_JT13_peer_finding_file_actual_inventory_hash_metadata_commentary_access":False,
      "mathematical_truth_checked_by_code":False}
    write_new(BASE + "baseline-v1.json", baseline)
    print(json.dumps({"prepared_UTC":baseline["captured_UTC"],"guards":17,"guard_digest":digest(records)}))

def freeze():
    baseline = read(BASE + "baseline-v1.json")
    main = (ROOT / (BASE + "initial-v1.md")).read_text()
    labels = [line.split("|")[1] for line in main.splitlines() if line.startswith("|JT13-")]
    assert labels == ["JT13-" + str(i).zfill(2) for i in range(1,33)]
    paths = [BASE + suffix for suffix in ("initial-v1.md","sources-v1.json","admin-v1.py","baseline-v1.json")]
    manifest = {"frozen_UTC":now(),"status":"SEALED immutable initially blind independent OTHER WHOLE2; coordinator pending",
      "reviewer":"/root/review_2021_reasoning_j15_r2","constructor":"B /root/review_2022_complexity_r2",
      "constructor_excluded":True,"NEW_JT13_construction_contribution":False,
      "whole_obligations":32,"ENTIRE_files":5,"payloads":[row(path) for path in paths],
      "guard_summary":{"occurrences":17,"unique_paths":17,"canonical_deduplicated_sha256":baseline["canonical_deduplicated_sha256"]},
      "ONE_compact_OWN_parent":baseline["ONE_compact_OWN_parent"],
      "whole_hand_reconstruction":True,"unresolved_substantive_defects":0,"required_author_repairs":0,"closed_scope_notes":12,
      "FULL_final_ALL4_payload_MODEL_readbacks_completed":True,
      "FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED":True,
      "NEW_JT13_peer_finding_file_actual_inventory_hash_metadata_commentary_access":False,
      "findings_require_explicit_BOTH_release":True,"mathematical_truth_checked_by_code":False,
      "author_source_old_helper_certificate_freezer_executed":False,
      "Git_shared_old_cache_configuration_mutation":False,
      "requested":{"model":"gpt-6.1-sol","reasoning":"max","inherited":True},
      "independent_effective_backend_readback":None,
      "quota":{"start_usedPercent":85,"latest_usedPercent":86,"latest_observed_UTC":"2026-10-19 03:56:44 UTC","windowDurationMins":10080,"resetsAt":1792874445,"ordinaryUsageAllowed":True,"TOTAL_ceiling":90,"reserve":True,"automatic_later_window":False}}
    write_new(BASE + "manifest-v1.json", manifest)
    print(json.dumps({"frozen_UTC":manifest["frozen_UTC"],"manifest":row(BASE + "manifest-v1.json")}))

def verify():
    manifest = read(BASE + "manifest-v1.json")
    for record in manifest["payloads"]:
        expect(record)
    baseline = read(BASE + "baseline-v1.json")
    records = baseline["necessary_immutable_records"]
    assert len(records) == len({r["path"] for r in records}) == 17
    assert digest(records) == baseline["canonical_deduplicated_sha256"] == manifest["guard_summary"]["canonical_deduplicated_sha256"]
    for record in records:
        expect(record)
    assert manifest["whole_obligations"] == 32 and manifest["ENTIRE_files"] == 5
    print(json.dumps({"SEPARATE_readonly_verified_UTC":now(),"PASS":True,"payloads":4,"necessary_immutable_paths":17,"manifest":row(BASE + "manifest-v1.json"),"mathematical_truth_checked_by_code":False}))

if __name__ == "__main__":
    {"prepare":prepare,"freeze":freeze,"verify":verify}[sys.argv[1]]()
