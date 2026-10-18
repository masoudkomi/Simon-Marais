#!/usr/bin/env python3
"""NEW R19 affected-review administration only. No mathematical evaluation.

Allowed modes: prepare (new metadata once), check, freeze (after payload
model readback), verify (read-only, after complete manifest model readback).
No author/source/old script is imported or executed. Exact paths only.
"""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2021-B4/reviews/reasoning-center-return-r19-review-2-v1.1-"
AUTH = "problems/2021-B4/notes/reasoning-center-return-r19-"
OLD_B = "problems/2021-B4/reviews/reasoning-center-return-r19-review-2-"
OLD_ROOT = "problems/2021-B4/reviews/reasoning-center-return-r19-review-1-"
PARENT = "problems/2019-B4/notes/reasoning-cut-transfer-r6-freeze-v1.json"
EXPECTED = {
    AUTH + "candidate-v1.1.md": (23302, "fd5a5399414c60c20797b63dfa9f55b8f66ac679fdd5458488c3250e3605a56a"),
    AUTH + "freeze-v1.1.json": (4753, "1b86a88b22a1cf755836900d314e26b7ac109f83e3031b03254a78a3d36f49fd"),
    AUTH + "candidate-v1.md": (17591, "589eddbf5f305b3380ee2c499d774aff8bb1b4499aa46c15c3dbffcf1bd56462"),
    AUTH + "freeze-v1.json": (3893, "dfe7b6b4f372b44a2806fc96ce41613bfc2fb7e8f5469fc2d10552aa83b835d3"),
    OLD_B + "manifest-v1.json": (5195, "2cdc76363c43865d1ca20347670ba0878e6c90cf0ad4b2acb2af04b26212754e"),
    OLD_ROOT + "manifest-v1.json": (2677, "4dbb9d1f2c775c2198fb990bd23a40ed5400f9d054042c796fe84a4c9eb0653d"),
    PARENT: (5022, "4b8e9a485850e2410f045ad4d83e13184d2d6ce60a327b153cd47313f483b4cc"),
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    "problems/2021-B4/statement.md": (1745, "5cd9750a2458191370590120fb4ae7d547740784eb1de38ee9e2e7890a2fabed"),
}
BODY_NAMES = ["reasoning-center-return-r18", "reasoning-center-return-r17", "reasoning-return-r8", "reasoning-return-r5"]
BODY_HASHES = [
    (26067,"f26de3a17895354408e514d6a0b0066715a1c0f0234d494fd53485ea3feb8284"),
    (23107,"8c8daa274ea6dcf95e25249e215b09646c3473c4ccd6320302a364b0af5b7797"),
    (19921,"33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"),
    (23675,"f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d"),
]
FAILURE_PATHS = [
    "problems/2021-B4/notes/reasoning-center-return-r18-failures-v1.md",
    "problems/2021-B4/notes/reasoning-center-return-r18-sources-v1.md",
    "problems/2021-B4/notes/reasoning-center-return-r17-failures-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-failed-routes-v1.md",
]
PAYLOAD_SUFFIXES = ["report.md", "ledger.md", "issues.md", "sources.md", "sources.json", "worklog.md", "metadata.py", "baseline.json", "input-validation.json"]
MODE = sys.argv[1] if len(sys.argv) == 2 else ""

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def allowed(path):
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
    # Never inspect corresponding NEW affected peer content/hash/metadata.
    if path.startswith(OLD_ROOT):
        assert "v1.1" not in path, "NEW root affected peer path prohibited"
    assert not path.startswith("problems/2021-B4/reviews/reasoning-center-return-r19-review-3-")
    assert "/.git/" not in path and not path.startswith(".cache/")
    return ROOT / path

def raw(path):
    return allowed(path).read_bytes()

def obj(path):
    return json.loads(raw(path))

def fp(path):
    data = raw(path)
    return {"path":path, "bytes":len(data), "sha256":hashlib.sha256(data).hexdigest()}

def match(rec):
    got = fp(rec["path"])
    assert got == {k:rec[k] for k in ("path","bytes","sha256")}, rec["path"]
    return got

def put(path, data):
    assert path.startswith(PRE), path
    target = allowed(path)
    assert not target.exists(), "Never overwrite frozen/existing file: " + path
    if not isinstance(data,str):
        data = json.dumps(data,indent=2,ensure_ascii=False) + "\n"
    target.write_text(data,encoding="utf-8")

def labels(text):
    return re.findall(r"^\|(R19-(?:\d{2}|FC\d{2}))\|",text,re.M)

def necessary():
    rows=[]
    for path,(n,h) in EXPECTED.items():
        rows.append(match({"path":path,"bytes":n,"sha256":h}))
    author = obj(AUTH+"freeze-v1.1.json")
    assert author["whole_obligations"] == 76 and author["ENTIRE_files"] == 16
    for rec in author["payloads"]:
        assert rec["path"].startswith(AUTH)
        rows.append(match(rec))
    parents=[]
    for path in [AUTH+"freeze-v1.json", OLD_B+"manifest-v1.json", OLD_ROOT+"manifest-v1.json", PARENT]:
        parent=obj(path)
        records=parent["payloads"]
        for rec in records:
            rows.append(match(rec))
        parents.append({"parent":fp(path),"immediate_payload_rows_verified":len(records),
                        "older_occurrences_bound_NOT_replayed":parent.get("necessary_guard_occurrences",parent.get("protected_current_occurrences")),
                        "older_unique_paths_bound_NOT_replayed":parent.get("necessary_guard_unique_paths",parent.get("protected_current_unique_paths")),
                        "nested_historical_inventory_opened_or_replayed":False})
    accepted=[]
    for name,(n,h) in zip(BODY_NAMES,BODY_HASHES):
        path="problems/2021-B4/proofs/reviewed-"+name+"-v1.1.md"
        body=match({"path":path,"bytes":n,"sha256":h})
        rows.append(body)
        md="problems/2021-B4/reviews/"+name+"-acceptance.md"
        js="problems/2021-B4/reviews/"+name+"-acceptance.json"
        rows.extend([fp(md),fp(js)])
        authority=obj(js)
        original=match(authority["candidate"])
        rows.append(original)
        assert raw(path).endswith(raw(original["path"])), path
        assert authority["unresolved_substantive_issues"] == 0
        accepted.append({"body":body,"authority_md":fp(md),"authority_json":fp(js),
                         "candidate_suffix":original,"byte_identical_suffix":True,
                         "historical_authority_occurrences_NOT_replayed":authority["record_occurrences_verified"],
                         "historical_authority_paths_NOT_replayed":authority["unique_paths_verified"]})
    for path in FAILURE_PATHS:
        rows.append(fp(path))
    for ext in ["md","json"]:
        path="problems/2021-B4/reviews/reasoning-center-return-r19-coordinator-reconciliation-v1."+ext
        rows.append(fp(path))
    unique={}
    for rec in rows:
        prev=unique.setdefault(rec["path"],rec)
        assert prev == rec
    ordered=[unique[p] for p in sorted(unique)]
    canonical=hashlib.sha256(json.dumps(ordered,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    old=raw(AUTH+"candidate-v1.md").decode()
    new=raw(AUTH+"candidate-v1.1.md").decode()
    expected_diff="".join(difflib.unified_diff(old.splitlines(keepends=True),new.splitlines(keepends=True),
        fromfile="reasoning-center-return-r19-candidate-v1.md",tofile="reasoning-center-return-r19-candidate-v1.1.md"))
    assert expected_diff.encode() == raw(AUTH+"diff-v1-to-v1.1.patch")
    assert old[old.index("## 1."):old.index("## 6.")] == new[new.index("## 1."):new.index("## 6.")]
    expected_labels=["R19-"+str(i).zfill(2) for i in range(1,65)]+["R19-FC"+str(i).zfill(2) for i in range(1,13)]
    assert labels(raw(AUTH+"obligations-v1.1.md").decode()) == expected_labels
    assert labels(raw(PRE+"ledger.md").decode()) == expected_labels
    assert labels(raw(AUTH+"obligations-v1.md").decode()) == expected_labels[:64]
    return {"necessary_occurrences":len(rows),"necessary_unique_paths":len(ordered),
        "canonical_deduplicated_sha256":canonical,"necessary_records":ordered,
        "compact_parent_bindings":parents,"accepted_operative_inputs":accepted,
        "author_entire_files":16,"old_author_entire_files":13,"original_peer_entire_files":21,
        "all76_author_labels_and_separate_reviewer_labels":True,"exact_unified_diff_reproduced":True,
        "original_sections1_to5_byte_identical":True,"nested_historical_inventory_replay":False,
        "all_fingerprint_checks_are_administration_not_mathematical_proof":True}

def summary(data):
    return {k:data[k] for k in ["necessary_occurrences","necessary_unique_paths","canonical_deduplicated_sha256",
        "author_entire_files","old_author_entire_files","original_peer_entire_files",
        "all76_author_labels_and_separate_reviewer_labels","exact_unified_diff_reproduced","original_sections1_to5_byte_identical"]}

def disclosure():
    return {"NEW_corresponding_root_affected_filenames_appeared_in_inventory":True,
        "NEW_corresponding_root_affected_contents_findings_hashes_or_metadata_file_contents_opened_read_hashed":False,
        "peer_conclusion_exposed":False,"promptly_disclosed_to_root":True,
        "literal_zero_filename_exposure_claimed":False,"root_assigned_additional_C_ENTIRE_affected_audit":True,
        "NEW_corresponding_C_affected_content_or_findings_accessed":False}

if MODE == "prepare":
    data=necessary()
    put(PRE+"baseline.json",{"created_at_utc":now(),"status":"entire affected review; necessary compact integrity only",
        "author_main":fp(AUTH+"candidate-v1.1.md"),"author_freeze":fp(AUTH+"freeze-v1.1.json"),
        "immediate_own_parent":fp(PARENT),"older_own_paths_bound_transitively_NOT_freshly_rehashed":824,
        "filename_inventory_disclosure":disclosure(),**data})
    sources={"date_utc":"2026-10-18","reviewer":"/root/review_2022_complexity_r2",
        "requested":{"model":"gpt-6.1-sol","reasoning":"max","inherited":True},"independent_effective_readback":None,
        "ENTIRE_author16_FULL_model_read":True,"ALL76_hand_reconstructions":True,
        "original_issue_and_counterexample_contribution_disclosed":True,
        "older_roles":"R9 constructor, older R5/R6/R7/R11-R16/R18 reviewer; not independent self-recertification",
        "filename_inventory_disclosure":disclosure(),
        "complete_accepted_bodies_and_each_current_MD_JSON_fresh_read":data["accepted_operative_inputs"],
        "primary_reads":[
          {"url":"https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
           "scope":"B4 setup/(b),page2 extracted67-81; no preliminary proof","binary_sha256":None},
          {"url":"https://arxiv.org/pdf/1806.09561v6",
           "scope":"definition253-257, ENTIRE operative Prop7.7 proof/Remark7.8,1034-1067; returned three-value theorem/computational description1083-1103 context only",
           "unread_or_NOT_imported":"fullpaper, independent source computation certification/replay,priority audit", "binary_sha256":None},
          {"url":"https://arxiv.org/pdf/1208.5404",
           "scope":"normalized derivative/integrality717-841; Section3.4/3.5/Lemmas17-18,898-1147; ENTIRE Prop19 proof/unramified remark1163-1307; returned Prop16 context",
           "unread":"whole23pages,journalversion,sourceprograms,2011p5correctionproof","binary_sha256":None}],
        "new_binary_download_or_cache_write":False,"new_visual_PDF_read_claimed":False,
        "local_lifting_quadratic_root_field_and_all_translations_reconstructed_self_contained":True,
        "actual_frameII_III_exclusion_annual_height_lift_or_priority_claim":False,
        "mathematical_program_CAS_scan_test_or_author_source_old_replay":False,
        "NEW_metadata_only_code":True,"source_hashes_are_not_mathematical_proof":True}
    put(PRE+"sources.json",sources)
    put(PRE+"input-validation.json",{"checked_at_utc":now(),"result":"PASS",**summary(data),
        "author_payload_hashes_match":True,"old_original_author13_and_peer21_preserved":True,
        "accepted_suffixes_verified":4,"immediate_own_parent_entire11_verified":True,
        "older_own_paths_bound_transitively":824,"filename_inventory_disclosure":disclosure(),
        "mathematical_assertions_evaluated_by_code":False})
    print(json.dumps({"mode":"prepare","result":"PASS",**summary(data)},indent=2))
elif MODE in ("check","freeze","verify"):
    data=necessary()
    baseline=obj(PRE+"baseline.json")
    assert data["necessary_records"] == baseline["necessary_records"]
    validation=obj(PRE+"input-validation.json")
    assert summary(data) == {k:validation[k] for k in summary(data)}
    for suffix in PAYLOAD_SUFFIXES:
        assert allowed(PRE+suffix).is_file(),suffix
    if MODE == "freeze":
        put(PRE+"manifest.json",{"frozen_at_utc":now(),
            "status":"ENTIRE affected OTHER WHOLE2 audit; initial findings EMBARGOED; not promotion",
            "reviewer":"/root/review_2022_complexity_r2","A_constructor_excluded":True,
            "original_objection_coordinate_counterexample_contribution_disclosed":True,
            "requested":{"model":"gpt-6.1-sol","reasoning":"max","inherited":True},
            "independent_effective_readback":None,"whole_obligations":76,"original64_plus_repair12":True,
            "author_ENTIRE_files_FULLread":16,"separate_hand_dispositions":76,
            "original_R19R2_01_resolved_in_audited_replacement_subject_other_review_and_reconciliation":True,
            "additional_substantive_math_defect_or_required_author_repair_found":False,
            "filename_inventory_disclosure":disclosure(),
            "no_NEW_peer_affected_contents_or_findings_or_hashes_or_metadata_file_contents_accessed":True,
            "ENTIRE_review_files_including_manifest":10,"immediate_own_parent":fp(PARENT),
            "older_own_paths_bound_transitively":824,"older_plus_new_own_paths_bound_transitively":834,
            "necessary_guard_summary":summary(data),
            "FULL_final_ALL9_payload_model_readback_including_code_and_generated_metadata_attested":True,
            "FULL_manifest_model_readback_then_SEPARATE_readonly_verification_required_before_handoff":True,
            "explicit_required_BOTH_confirmation_NOT_yet_received":True,
            "identity_only_completion_until_explicit_required_confirmation":True,
            "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass":True,
            "no_mathematical_program_CAS_scan_test_or_author_source_old_replay":True,
            "authoritative_weekly_telemetry":{"observed_at_utc":"2026-10-18 14:30:20 UTC",
                "method":"own same-awaited clock/get_usage_limits","TOTAL_used_percent":43,
                "window_minutes":10080,"resetsAt":1792874445,"ordinary_usage_allowed":True,
                "legacy_by_limit_agree":True,"account_label":"029a8928...1334ac3a",
                "human_authorized_current_window_only":True,"TOTAL_ceiling_percent":90,
                "integration_reserve":True,"automatic_later_window_spending":False},
            "payloads":[fp(PRE+s) for s in PAYLOAD_SUFFIXES]})
    if MODE == "verify":
        manifest=obj(PRE+"manifest.json")
        for rec in manifest["payloads"]:
            match(rec)
        assert len(manifest["payloads"]) == 9 and manifest["whole_obligations"] == 76
        print(json.dumps({"mode":"SEPARATE read-only verification","at_utc":now(),"result":"PASS",
            "ENTIRE_files":10,"whole_obligations":76,"manifest":fp(PRE+"manifest.json"),
            "report":fp(PRE+"report.md"),**summary(data)},indent=2))
    else:
        print(json.dumps({"mode":MODE,"at_utc":now(),"result":"PASS",**summary(data)},indent=2))
else:
    raise SystemExit("Use prepare, check, freeze or verify; NEW administration only")
