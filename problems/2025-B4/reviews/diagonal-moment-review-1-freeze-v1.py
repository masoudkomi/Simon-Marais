"""Administrative file integrity only. No algebra/CAS/scan or author rerun."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/diagonal-moment-review-1-"


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


author_path = "problems/2025-B4/notes/coordinator-diagonal-moment-manifest-v1.json"
assert record(author_path)["sha256"] == "5d0d897d3ff89828e26d16919357bf0d283866bb3bb97b7aa9f1277b3a3d3654"
author = read_json(author_path)
author_records = [verify(r) for r in author["records"]]
assert len(author_records) == 4
assert author_records[0]["sha256"] == "dae1907e2c3afe744ede7ffc89321d560ebbfab326afd78786f30dac960fcb2f"
source_path = "problems/2025-B4/notes/coordinator-diagonal-moment-sources-v1.json"
source_records = embedded(read_json(source_path))
assert len(source_records) == 6
obligation_path = "problems/2025-B4/notes/coordinator-diagonal-moment-obligations-v1.json"
assert len(read_json(obligation_path)["obligations"]) == 14
direct_paths = ["AGENTS.md", "problems/2025-B4/statement.md", author_path,
                *[r["path"] for r in author_records], *[r["path"] for r in source_records]]
direct_records = [record(p) for p in dict.fromkeys(direct_paths)]
prior_prefix = "problems/2024-B4/reviews/necessary-valuation-review-1-"
prior_inputs = read_json(prior_prefix + "input-checks-v1.json")
prior_manifest_path = prior_prefix + "manifest-v1.json"
prior_manifest = read_json(prior_manifest_path)
older = [verify(r) for r in prior_inputs["older_own_records"]]
older.extend(verify(r) for r in prior_manifest["records"])
older.append(record(prior_manifest_path))
older_by_path = {r["path"]: r for r in older}
assert len(older) == len(older_by_path) == 171
older = sorted(older_by_path.values(), key=lambda r: r["path"])
all_inputs = [record(author_path), *author_records, *source_records, *direct_records]
now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17T11:36:31+00:00", "source": "direct account-wide Codex usage tool",
             "total_used_percent": 34, "window_duration_minutes": 10080,
             "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
             "total_used_cutoff_percent": 90, "integration_reserve": True}
primary_scopes = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf",
     "scope": "Page 2 B4(b), official PDF text reopened 2026-10-17; no fresh visual-render claim."},
    {"url": "https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren",
     "edition": "Author-uploaded internal version2.0 2007-09-17; published2008",
     "scope": "Section2.1 convention; Section2.3 equations14–18 and complete Lemma3/proof; Section4.3 selections, complete Lemma14/proof, Fourier definition and relevant regular/singular/second-case passages. No whole Diophantine-proof acceptance.",
     "access": "Direct web text viewer, no binary download or invented binary hash."},
    {"url": "https://arxiv.org/pdf/1412.5798v2",
     "edition": "arXiv header2015-06-30; internal version1.13 2021-11-02",
     "scope": "Existing exact cached PDF pages1,5–7,9–10,15–16; definitions, relevant complete coefficient lemmas2.8–2.10/proofs, Appendix5.1–5.1.1 application. No full theorem import.",
     "cache": source_records[-1],
     "extraction": "Bundled dependency Python with pypdf; initial system-python pypdf import failed and was recorded, no installation."},
]
inputs = {
    "checked_at_utc": now, "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2", "constructor": "coordinator root",
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "initial_whole_MS_audit_blind_to_new_peer_findings": True,
    "earlier_PG_CF1_review_roles_disclosed_no_MS_construction": True,
    "NV_complete_freeze_preceded_MS_proof_read": True,
    "author_manifest": record(author_path), "author_four_records": author_records,
    "source_six_fingerprint_records": source_records,
    "complete_direct_read_body_and_scope_records": direct_records,
    "four_historical_moment_notes_and_appendix_read_entirely": True,
    "all14_obligations_read_and_covered": True,
    "actual_primary_read_scopes": primary_scopes,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "older_own_paths_verified_unchanged": len(older), "older_own_records": older,
    "per_inference_checks": 39, "unresolved_substantive_issues": 0,
    "fourier_vs_reciprocal_and_direct_vs_inverse_indices_checked": True,
    "reciprocal_array_not_misidentified_as_true_Galois_orbit": True,
    "p7_actual_stabilizer_counterexample_hand_reconstructed": True,
    "arbitrary_second_case_moment_or_full_external_proof_not_granted": True,
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
    "status": "Initially blind nonconstructor WHOLE MS1–MS5 R1 frozen; no substantive objection found; root alone may accept after both independent audits.",
    "reviewer": "review_2022_complexity_r2", "constructor": "coordinator root",
    "reviewer_constructed_MS": False, "earlier_PG_CF1_review_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "complete_consolidated_four_historical_notes_appendix_sources14_obligations_read": True,
    "actual_primary_definitions_and_assigned_passages_checked": True,
    "blind_to_new_peer_MS_findings_before_freeze": True,
    "claims_audited": ["MS1", "MS2", "MS3", "MS4", "MS5"],
    "per_inference_checks": 39, "unresolved_substantive_issues": 0,
    "author_repairs_requested": 0,
    "algebraic_lemmas_only_no_new_Diophantine_exclusion": True,
    "no_full_external_proof_appendix_repair_or_novelty_claim": True,
    "mathematical_computation_scan_CAS_enumeration_or_author_rerun": False,
    "old_candidate_shared_Git_or_other_review_edits": False,
    "author_manifest": record(author_path),
    "author_artifact_records_verified": len(author_records),
    "source_fingerprint_entries_verified": len(source_records),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "earlier_own_paths_preserved_unchanged": len(older),
    "direct_weekly_telemetry": telemetry, "records": outputs,
}
write_new(PREFIX + "manifest-v1.json", manifest)
print(json.dumps({"manifest": record(PREFIX + "manifest-v1.json"), "records": outputs,
                  "input_occurrences": len(all_inputs), "input_paths": len({r["path"] for r in all_inputs}),
                  "older_own_paths_preserved": len(older)}, indent=2))
