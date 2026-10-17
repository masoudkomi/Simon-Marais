"""Administrative integrity only; no mathematical computation or candidate edits."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/necessary-valuation-review-1-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(item):
    actual = record(item["path"])
    assert actual == {k: item[k] for k in ("path", "bytes", "sha256")}, (item, actual)
    return actual


def read_json(path):
    return json.loads((ROOT / path).read_text())


def embedded(value):
    found = []
    if isinstance(value, dict):
        if {"path", "bytes", "sha256"} <= value.keys():
            found.append(verify(value))
        for child in value.values():
            found.extend(embedded(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(embedded(child))
    return found


def write_new(path, value):
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


author_path = "problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-manifest-v1.json"
author = read_json(author_path)
assert record(author_path)["sha256"] == "005a5ea65ac2b7da94ec085c3b6d93ac7938f2102cd5b1af79f569012b6e2ac8"
author_records = [verify(item) for item in author["records"]]
assert len(author_records) == 4
assert author_records[0]["sha256"] == "5b772b77f821c3e3b2f7b04a22c0f9d3609f85942e9cd3d3a0d13104cbc118a4"
source_path = "problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-sources-v1.json"
source_records = embedded(read_json(source_path))
assert len(source_records) == 3
acceptance_path = "problems/2024-B4/reviews/composition-Kasami-acceptance.json"
acceptance_records = embedded(read_json(acceptance_path))
assert len(acceptance_records) == 9
direct_paths = [
    "AGENTS.md", "problems/2024-B4/statement.md", author_path,
    *[r["path"] for r in author_records], *[r["path"] for r in source_records],
]
direct_records = [record(p) for p in dict.fromkeys(direct_paths)]
prior_prefix = "problems/2022-B4/reviews/reasoning-return-r4-review-2-"
prior_inputs = read_json(prior_prefix + "input-checks-v1.json")
prior_manifest_path = prior_prefix + "manifest-v1.json"
prior_manifest = read_json(prior_manifest_path)
older = [verify(r) for r in prior_inputs["older_own_records"]]
older.extend(verify(r) for r in prior_manifest["records"])
older.append(record(prior_manifest_path))
older_by_path = {r["path"]: r for r in older}
assert len(older) == len(older_by_path) == 165
older = sorted(older_by_path.values(), key=lambda r: r["path"])
all_inputs = [record(author_path), *author_records, *source_records,
              *acceptance_records, *direct_records]
now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17T11:20:47+00:00", "source": "direct account-wide Codex usage tool",
             "total_used_percent": 33, "window_duration_minutes": 10080,
             "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
             "total_used_cutoff_percent": 90, "integration_reserve": True}
inputs = {
    "checked_at_utc": now, "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2", "constructor": "coordinator root",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "initial_whole_NV_audit_blind_to_new_peer_findings": True,
    "prior_2024_structural_divisor_GK_reviews_disclosed_no_NV_construction": True,
    "author_manifest": record(author_path), "author_four_records": author_records,
    "source_three_fingerprints": source_records,
    "CP_acceptance_nine_hash_entries_metadata_only": acceptance_records,
    "complete_direct_read_body_and_scope_records": direct_records,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "older_own_paths_verified_unchanged": len(older), "older_own_records": older,
    "actual_primary_scope": "Official 2024 Paper B page 2 B4(b), reopened PDF text 2026-10-17; no fresh visual claim. No new external theorem imported.",
    "CP_body_scope": "Complete accepted composition-Kasami body and acceptance MD/JSON; CP1 whole multiplicity-sensitive composition equivalence used; CP2/CP3 read context only.",
    "constructor_shared_script_read_only_not_executed": True,
    "per_inference_checks": 23, "unresolved_substantive_issues": 0,
    "mathematical_computation_scan_CAS_certificate_or_author_rerun": False,
    "old_candidate_shared_Git_or_other_review_edits": False,
    "only_new_assigned_prefix_written": True,
    "spawning_charge_contact_or_access_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "administrative_freeze_command": "python3 " + PREFIX + "freeze-v1.py",
    "all_verified": True,
}
write_new(PREFIX + "input-checks-v1.json", inputs)
outputs = [record(PREFIX + suffix) for suffix in
           ["initial.md", "issues.md", "source-checks.md", "freeze-v1.py", "input-checks-v1.json"]]
manifest = {
    "frozen_at_utc": now,
    "status": "Initially blind nonconstructor WHOLE NV R1 frozen; no substantive objection found; root alone may accept after both independent audits.",
    "reviewer": "review_2022_complexity_r2", "constructor": "coordinator root",
    "reviewer_constructed_NV": False, "earlier_2024_reviews_disclosed": True,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "complete_candidate_11_obligations_sources_and_CP_body_read": True,
    "blind_to_new_peer_NV_findings_before_freeze": True,
    "per_inference_checks": 23, "unresolved_substantive_issues": 0,
    "author_repairs_requested": 0, "whole_divisor_necessary_valuation_only": True,
    "q2_exclusion_essential": True, "n_equals_d_and_q4_checked": True,
    "no_full_progression_reducibility_or_novelty_claim": True,
    "mathematical_computation_scan_CAS_enumeration_or_author_rerun": False,
    "old_candidate_shared_Git_or_other_review_edits": False,
    "author_manifest": record(author_path),
    "author_artifact_records_verified": len(author_records),
    "source_fingerprint_entries_verified": len(source_records),
    "CP_acceptance_hash_entries_verified": len(acceptance_records),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "earlier_own_paths_preserved_unchanged": len(older),
    "direct_weekly_telemetry": telemetry, "records": outputs,
}
write_new(PREFIX + "manifest-v1.json", manifest)
print(json.dumps({"manifest": record(PREFIX + "manifest-v1.json"), "records": outputs,
                  "input_occurrences": len(all_inputs), "input_paths": len({r["path"] for r in all_inputs}),
                  "older_own_paths_preserved": len(older)}, indent=2))
