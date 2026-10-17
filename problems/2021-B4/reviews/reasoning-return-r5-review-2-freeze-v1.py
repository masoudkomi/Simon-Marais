"""Exclusive administrative R5 review freeze; no mathematics or author reruns."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-return-r5-review-2-"


def row(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(item):
    actual = row(item["path"])
    assert actual == {k: item[k] for k in ("path", "bytes", "sha256")}, (item, actual)
    return actual


def read_json(path):
    return json.loads((ROOT / path).read_text())


def embedded(value):
    out = []
    if isinstance(value, dict):
        if {"path", "bytes", "sha256"} <= value.keys():
            out.append(check(value))
        for child in value.values():
            out.extend(embedded(child))
    elif isinstance(value, list):
        for child in value:
            out.extend(embedded(child))
    return out


def create(path, obj):
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


constructor_prefix = "problems/2021-B4/notes/reasoning-return-r5-"
author_manifest_path = constructor_prefix + "freeze-v1.json"
assert row(author_manifest_path)["sha256"] == "1626fa3981c78eb04f7fe41fc5a725b2500de0cf1647e7324941c6a5f3671533"
author_manifest = read_json(author_manifest_path)
author_records = [check(r) for r in author_manifest["artifacts"]]
assert len(author_records) == 8
assert author_records[0]["bytes"] == 20083
assert author_records[0]["sha256"] == "0d546265a3f9b1f83c05fce46e5a97acb6cad5d8841518d891ffed91717166f6"
sources = read_json(constructor_prefix + "sources-v1.json")
validation = read_json(constructor_prefix + "input-validation-v1.json")
source_records = embedded(sources)
validation_records = embedded(validation)
assert len(source_records) == 50
assert len(validation_records) == 252
assert len(sources["complete_accepted_bodies_and_registers_read"]) == 12
assert len(sources["all_seven_exact_accepted_return_mathematical_texts_read"]) == 7
pn_raw = sources["PN_raw_body"]
pn_accepted = "problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md"
assert (ROOT / pn_accepted).read_bytes().endswith((ROOT / pn_raw["path"]).read_bytes())
for i in range(1, 31):
    assert f"| R5-{i:02d} |" in (ROOT / (constructor_prefix + "obligations-v1.md")).read_text()
ledger = (ROOT / (PREFIX + "issues.md")).read_text()
for i in range(1, 55):
    assert f"| R5-R2-{i:02d} |" in ledger
direct_paths = [
    "AGENTS.md", "problems/2021-B4/statement.md", "problems/2021-B4/references.md",
    author_manifest_path,
    *[r["path"] for r in author_records if not r["path"].endswith("input-validation-v1.json")],
    *[r["path"] for r in sources["complete_accepted_bodies_and_registers_read"]],
    *[r["path"] for r in sources["all_seven_exact_accepted_return_mathematical_texts_read"]],
    "problems/2021-B4/notes/padic-rational-newton-obstructions-v1.md",
    "problems/2021-B4/notes/coordinator-newton-degeneration-v1.md",
    "problems/2021-B4/notes/coordinator-three-rational-witnesses-v1.md",
    "problems/2021-B4/reviews/return-r3-acceptance.md",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance.md",
]
direct_records = [row(p) for p in dict.fromkeys(direct_paths)]
prior_prefix = "problems/2025-B4/reviews/diagonal-moment-review-1-"
prior_inputs = read_json(prior_prefix + "input-checks-v1.json")
prior_manifest_path = prior_prefix + "manifest-v1.json"
prior_manifest = read_json(prior_manifest_path)
older = [check(r) for r in prior_inputs["older_own_records"]]
older.extend(check(r) for r in prior_manifest["records"])
older.append(row(prior_manifest_path))
by_path = {r["path"]: r for r in older}
assert len(older) == len(by_path) == 177
older = sorted(by_path.values(), key=lambda r: r["path"])
all_inputs = [row(author_manifest_path), *author_records, *source_records,
              *validation_records, *direct_records]
now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17T11:47:34+00:00", "source": "direct account-wide Codex usage tool",
             "total_used_percent": 35, "window_duration_minutes": 10080,
             "resets_at_unix": 1792745187, "ordinary_usage_allowed": True,
             "total_used_cutoff_percent": 90, "integration_reserve": True}
actual_source_scopes = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
     "scope": "Page2 B4, (b) only, actual PDF text reopened; no fresh viewer/cached binary identity claimed."},
    {"url": "https://arxiv.org/pdf/1208.5404",
     "scope": "Cached exact PDF pages13–15, Section3.4 equations9–10/root discussion/full Lemma17 and Section3.5 selector/divided-center context; Proposition19 hypothesis boundary. Not entire paper.",
     "cache": sources["primary_sources"][1]["existing_cache"]},
    {"url": "https://arxiv.org/html/1710.11033v2",
     "scope": "Exact definition n>maxI, Proposition2.1 and complete concatenation proof, Theorem2.2 polynomial extension. No maximal-descent theorem.",
     "binary_hash": None},
    {"url": "https://arxiv.org/html/2608.14726v1",
     "scope": "TheoremB and multi-root boundary, Definition4.2, Corollary4.3, Theorem4.4 determinant proof, Corollary4.6; attribution, not direct normalized-index theorem import.",
     "binary_hash": None},
    {"url": "https://www.mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf",
     "scope": "Newton setup, Lemma3.5/Theorem3.6 and complete short product proof; page16 explicit multiplicities. Q_p hypotheses checked; not complete course notes.",
     "binary_hash": None},
]
inputs = {
    "checked_at_utc": now, "metadata_only_not_mathematical_evidence": True,
    "reviewer": "review_2022_complexity_r2", "constructor": "review_2017_coarsening_r1",
    "root_triple_count_clarification_disclosed_not_independent_reviewer": True,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "initial_whole_R5_audit_blind_to_new_peer_findings": True,
    "prior_R3_and_single_center_review_roles_disclosed_no_R5_construction": True,
    "author_manifest": row(author_manifest_path), "author_eight_records": author_records,
    "constructor_source_fingerprint_occurrences_metadata_checks": source_records,
    "constructor_validation_fingerprint_occurrences_metadata_checks": validation_records,
    "direct_full_document_or_register_reads": direct_records,
    "all_seven_return_mathematical_bodies_reread": True,
    "PN_exact_complete_accepted_suffix_verified": True,
    "all30_obligations_covered_by54_inference_checks": True,
    "context_registers_not_entire_linked_certificate_reruns": [
        "coordinator-three-complex-witnesses-reviewed-v1.1.md",
        "coordinator-J16-exclusion-reviewed-v1.1.md", "ghosh-source-reviewed-register-v1.1.md"],
    "all_hashed_author_contexts_claimed_fresh_complete_reads": False,
    "actual_primary_read_scopes": actual_source_scopes,
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "older_own_paths_verified_unchanged": len(older), "older_own_records": older,
    "per_inference_checks": 54, "unresolved_substantive_issues": 0,
    "minimum_selected_noncenter_bound_not_all_root_bound": True,
    "symbolic_equal_degree_carrier_trace_case_checked": True,
    "RC2_PN4_exact_conjunction_and_five_unit_TA1_chain_checked": True,
    "mathematical_computation_scan_CAS_certificate_or_author_rerun": False,
    "old_candidate_shared_Git_or_other_review_edits": False,
    "only_new_assigned_prefix_written": True,
    "spawning_charge_contact_or_access_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "administrative_freeze_command": "python3 " + PREFIX + "freeze-v1.py",
    "all_verified": True,
}
create(PREFIX + "input-checks-v1.json", inputs)
outputs = [row(PREFIX + suffix) for suffix in
           ["initial.md", "issues.md", "source-checks.md", "freeze-v1.py", "input-checks-v1.json"]]
manifest = {
    "frozen_at_utc": now,
    "status": "Initially blind nonconstructor WHOLE R5A–R5E R2 frozen; no substantive objection found; root alone may accept after both whole audits.",
    "reviewer": "review_2022_complexity_r2", "constructor": "review_2017_coarsening_r1",
    "reviewer_constructed_R5": False, "earlier_review_roles_disclosed": True,
    "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "complete_candidate_log_sources30_obligations_and_direct_accepted_bodies_read": True,
    "all_seven_accepted_return_bodies_reread": True,
    "actual_primary_definitions_and_assigned_proof_passages_checked": True,
    "blind_to_new_peer_R5_findings_before_freeze": True,
    "claims_audited": ["R5A", "R5B", "R5C", "R5D", "R5E"],
    "per_inference_checks": 54, "unresolved_substantive_issues": 0,
    "author_repairs_requested": 0,
    "no_full_J15_mask_degree20_annual_solution_or_novelty_claim": True,
    "mathematical_computation_scan_CAS_enumeration_or_author_rerun": False,
    "old_candidate_shared_Git_or_other_review_edits": False,
    "author_manifest": row(author_manifest_path),
    "author_artifact_records_verified": len(author_records),
    "constructor_source_fingerprint_occurrences_verified": len(source_records),
    "constructor_validation_occurrences_verified": len(validation_records),
    "constructor_validation_unique_paths_verified": len({r["path"] for r in validation_records}),
    "input_record_occurrences_verified": len(all_inputs),
    "input_unique_paths_verified": len({r["path"] for r in all_inputs}),
    "earlier_own_paths_preserved_unchanged": len(older),
    "direct_weekly_telemetry": telemetry, "records": outputs,
}
create(PREFIX + "manifest-v1.json", manifest)
print(json.dumps({"manifest": row(PREFIX + "manifest-v1.json"), "records": outputs,
                  "source_occurrences": len(source_records), "validation_occurrences": len(validation_records),
                  "validation_paths": len({r["path"] for r in validation_records}),
                  "input_occurrences": len(all_inputs), "input_paths": len({r["path"] for r in all_inputs}),
                  "older_own_paths_preserved": len(older)}, indent=2))
