#!/usr/bin/env python3
"""Administrative-only R10 R2 freeze. No mathematics, scans or author rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-return-r10-review-2-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    actual = record(row["path"])
    if actual != expected:
        raise RuntimeError(("Fingerprint changed", expected, actual))
    return actual


def read_json(path):
    return json.loads((ROOT / path).read_text())


def write_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as handle:
        json.dump(value, handle, indent=2)
        handle.write("\n")
    return record(path)


def summary(rows):
    unique = {}
    for row in rows:
        old = unique.setdefault(row["path"], row)
        if old != row:
            raise RuntimeError(("Conflicting same-path rows", old, row))
    canonical = json.dumps([unique[key] for key in sorted(unique)],
                           sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "canonical_deduplicated_summary_sha256":
            hashlib.sha256(canonical).hexdigest(),
            "encoding": "UTF8 sorted unique path/bytes/sha256 JSON, sorted keys, compact separators"}


def main():
    for suffix in ("sources-v1.json", "input-validation-v1.json",
                   "freeze-output-v1.json", "manifest-v1.json"):
        if (ROOT / (PREFIX + suffix)).exists():
            raise RuntimeError("Refuse to overwrite any frozen or existing output")

    baseline_row = record(PREFIX + "baseline-v1.json")
    if baseline_row["bytes"] != 19717 or baseline_row["sha256"] != \
            "82859828b8b71ec5c83051e17874e29783273a65474de8942a16bf1b9badf536":
        raise RuntimeError("Unexpected baseline")
    baseline = read_json(baseline_row["path"])
    packet = [verify(row) for row in baseline["constructor_packet_records"]]
    direct = [verify(row) for row in baseline["necessary_direct_mathematical_scope_and_protocol_bindings"]]
    anchors = [verify(row) for row in baseline["constructor_previously_declared_anchors"]]
    parents = [{"metadata": verify(row["metadata"]),
                "declared_historical_fingerprint_occurrences":
                row["declared_historical_fingerprint_occurrences"]}
               for row in baseline["immutable_constructor_parent_metadata"]]
    source = read_json("problems/2021-B4/notes/reasoning-return-r10-sources-v1.json")
    accepted = [verify(row) for row in source["accepted_bodies"]]
    old_rows = [verify(row) for row in baseline["own_parent_new_records"]]
    old_manifest = verify(baseline["compact_own_parent_manifest"])
    old_validation = verify(baseline["compact_own_parent_validation"])
    all_old = packet + direct + anchors + [row["metadata"] for row in parents] + \
        accepted + old_rows + [old_validation]
    old_summary = summary(all_old)
    assert len(packet) == 11 and len(direct) == 14 and len(anchors) == 7
    assert len(parents) == 27 and len(accepted) == 5 and len(old_rows) == 15
    assert old_summary["occurrences"] == baseline["necessary_current_fingerprint_occurrences"] == 80
    assert old_summary["unique_paths"] == baseline["necessary_current_unique_paths"] == 67
    assert old_summary["canonical_deduplicated_summary_sha256"] == \
        baseline["current_canonical_deduplicated_summary_sha256"]
    assert baseline["older_own_paths_bound_transitively"] == 400
    constructor_validation = read_json("problems/2021-B4/notes/reasoning-return-r10-input-validation-v1.json")
    declared_summary = baseline["constructor_reported_historical_fingerprint_summary_bound_not_replayed"]
    assert declared_summary == {
        "occurrences": constructor_validation["declared_fingerprint_occurrences_verified"],
        "unique_paths": constructor_validation["unique_paths_fingerprinted"],
        "canonical_sha256": constructor_validation["canonical_deduplicated_summary_sha256"]}

    report_path = PREFIX + "initial-v1.md"
    ledger_path = PREFIX + "issues-v1.md"
    source_check_path = PREFIX + "source-checks-v1.md"
    report = (ROOT / report_path).read_text()
    ledger = (ROOT / ledger_path).read_text()
    rows = re.findall(r"^\|(R10-\d{2})\|(PASS)\|(.+)\|$", ledger, re.MULTILINE)
    assert [row[0] for row in rows] == ["R10-%02d" % index for index in range(1, 53)]
    assert all(len(row[2]) > 50 for row in rows)
    assert all(claim in report for claim in ("R10A", "R10B", "R10C"))
    assert "availability,+the" not in report
    prose = [record(path) for path in (report_path, ledger_path, source_check_path)]

    source_json = {
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 source record; no promotion",
        "reviewer": "/root/review_2022_complexity_r2",
        "new_R10_constructed_or_contributed_by_reviewer": False,
        "older_R9_constructor_role_disclosed_not_fresh_self_recertification": True,
        "older_J15_single_center_and_return_review_roles_disclosed": True,
        "requested_settings": baseline["requested_settings"],
        "independently_verified_effective_settings": None,
        "constructor_main": verify(baseline["constructor_main"]),
        "constructor_freeze": verify(baseline["constructor_freeze"]),
        "all_ten_constructor_artifacts_plus_freeze_actually_read": True,
        "constructor_freezer_read_as_text_only_not_executed": True,
        "complete_accepted_bodies_freshly_read": accepted,
        "all_five_acceptance_md_and_json_scopes_read": True,
        "R9_source_audit_and_failed_routes_freshly_read_complete": True,
        "truncated_combined_reads_completed_in_bounded_followups": True,
        "primary_public_sources": [
            {"title": "Official SMMC2021 Paper B",
             "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
             "actual_scope": "page2 B4 full hypothesis and(b), checked against complete local statement; no preliminary proof",
             "fresh_native_PDF_sha256": None},
            {"title": "Atkinson-Sharma1969, A partial characterization of poised Hermite-Birkhoff interpolation problems",
             "url": "https://homepage.math.uiowa.edu/~atkinson/papers/HB_interp.pdf",
             "actual_scope": "all226 extracted lines/all six pages230-235, incidence definitions, Theorem2 and full proof, distinct unused converse",
             "use": "published sufficient criterion via exact accepted R9 adaptation; no all-roots-real premise",
             "fresh_native_PDF_sha256": None},
            {"title": "Castryck-Laterveer-Ounaies, Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree12",
             "url": "https://arxiv.org/pdf/1208.5404",
             "actual_scope": "Section3.4 normalization through Lemma17, returned lines898-1013; complete Proposition19 and following unramified remark, lines1163-1307; nearby3.5 context, not full23pages/degree certificate",
             "use": "normalization attribution and stronger ALL-root hypothesis boundary",
             "fresh_native_PDF_sha256": None}
        ],
        "new_R10_peer_report_ledger_source_integrity_manifest_contents_or_findings_read": False,
        "only_peer_path_names_in_inventory_no_contents": True,
        "no_new_full_R6_R7_or_unlisted_external_paper_read_claim": True,
        "no_mathematical_executable_CAS_scan_author_or_certificate_rerun": True,
        "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
        "necessary_current_old_fingerprint_summary_reverified": old_summary,
        "constructor_historical_summary_immutable_bound_not_newly_replayed": declared_summary,
        "older_own_paths_bound_transitively": 400,
        "compact_own_parent_manifest": old_manifest,
        "compact_own_parent_validation": old_validation,
        "historical_inventory_not_recopied_or_claimed_freshly_reread": True,
        "direct_weekly_telemetry": baseline["direct_weekly_telemetry"]}
    source_row = write_new("sources-v1.json", source_json)
    freezer = record(PREFIX + "freeze-v1.py")
    current_rows = prose + [baseline_row, source_row, freezer]
    validation = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "administrative_only_not_mathematical_evidence": True,
        "baseline": baseline_row,
        "all_necessary_baseline_fingerprints_unchanged": True,
        "all_ten_constructor_artifacts_plus_freeze_verified": True,
        "constructor_packet_records": packet,
        "direct_input_and_anchor_occurrences": len(direct) + len(anchors),
        "immutable_constructor_metadata_parents_count": len(parents),
        "all_five_accepted_body_fingerprints_verified": True,
        "necessary_current_old_fingerprint_summary_reverified": old_summary,
        "constructor_historical_summary_immutable_bound_not_newly_replayed": declared_summary,
        "compact_own_parent_manifest": old_manifest,
        "compact_own_parent_validation": old_validation,
        "older_own_paths_bound_transitively": 400,
        "historical_inventory_not_recopied": True,
        "new_review_records": current_rows,
        "all_current_input_and_review_fingerprint_summary": summary(all_old + current_rows),
        "all52_obligation_rows_once_and_complete": True,
        "whole_claims": ["R10A", "R10B", "R10C"],
        "substantive_issues_remaining": 0,
        "required_repairs": False,
        "new_peer_R10_files_or_findings_read": False,
        "mathematical_code_CAS_scan_author_or_certificate_rerun": False,
        "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
        "source_record": source_row,
        "direct_weekly_telemetry": baseline["direct_weekly_telemetry"]}
    validation_row = write_new("input-validation-v1.json", validation)
    output_row = write_new("freeze-output-v1.json", {
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; no promotion",
        "all52_obligations_reconstructed": True,
        "substantive_issues_remaining": 0,
        "required_repair": False,
        "peer_blindness_through_entire_initial_freeze": True,
        "necessary_old_fingerprint_occurrences_reverified": 80,
        "necessary_old_unique_paths": 67,
        "older_own_paths_bound_transitively": 400,
        "new_review_and_input_summary": validation["all_current_input_and_review_fingerprint_summary"],
        "no_mathematical_program_or_author_rerun": True,
        "report_ledger_sources": prose,
        "input_validation": validation_row})
    artifacts = prose + [baseline_row, freezer, source_row, validation_row, output_row]
    manifest = {
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; no promotion",
        "reviewer": "/root/review_2022_complexity_r2",
        "new_candidate_constructed_or_contributed_by_reviewer": False,
        "older_accepted_R9_authorship_disclosed_no_fresh_self_recertification": True,
        "older_review_roles_disclosed": True,
        "requested_settings": baseline["requested_settings"],
        "independently_verified_effective_settings": None,
        "constructor_main": verify(baseline["constructor_main"]),
        "constructor_freeze": verify(baseline["constructor_freeze"]),
        "whole_claims": ["R10A", "R10B", "R10C"],
        "all52_author_obligations_reconstructed": True,
        "substantive_issues_remaining": 0,
        "required_repair": False,
        "full_initial_report_ledger_source_before_peer_comparison": True,
        "new_peer_R10_report_ledger_source_integrity_manifest_contents_or_findings_read": False,
        "all_six_quartic_cases_and_integer_coefficients_reconstructed_by_hand": True,
        "no_rational_lift_full_first_break_degree20_annual_or_novelty_claim": True,
        "no_mathematical_executable_CAS_scan_author_or_old_certificate_rerun": True,
        "compact_own_parent_manifest": old_manifest,
        "compact_own_parent_validation": old_validation,
        "older_own_paths_bound_transitively": 400,
        "historical_inventory_not_copied_or_claimed_freshly_reread": True,
        "necessary_old_fingerprint_occurrences_reverified": 80,
        "necessary_old_unique_paths": 67,
        "all_current_input_and_review_fingerprint_summary": validation["all_current_input_and_review_fingerprint_summary"],
        "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
        "direct_weekly_telemetry": baseline["direct_weekly_telemetry"],
        "command": "python3 " + PREFIX + "freeze-v1.py",
        "artifacts": artifacts}
    manifest_row = write_new("manifest-v1.json", manifest)
    for row in all_old + artifacts + [manifest_row]:
        verify(row)
    print(json.dumps({"manifest": manifest_row, "report": prose[0],
                      "ledger": prose[1], "source_checks": prose[2],
                      "validation": validation_row,
                      "all52_obligations": True, "substantive_issues": 0,
                      "required_repair": False,
                      "artifacts_plus_manifest": len(artifacts) + 1,
                      "preservation_verified": True}, indent=2))


if __name__ == "__main__":
    main()
