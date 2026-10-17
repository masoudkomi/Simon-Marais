#!/usr/bin/env python3
"""Create-new whole-review integrity freeze; administrative metadata only.

No mathematical algorithm, polynomial, exponent scan, certificate, CAS or
old author script is executed. Inputs and all old/cache/shared/Git bytes
are read-only. Refuses new sector3 peer paths and existing output files.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/reasoning-sector3-return-r1-review-1-"
CTOR = "problems/2024-B4/notes/reasoning-sector3-return-r1-"
BASELINE = {"path": PREFIX + "baseline-v1.json", "bytes": 6602,
    "sha256": "1146ff0f7421921db81b7b31e1955f7166fe7658d9b44f2ce0af915ff1c28988"}
STAMP = datetime.now(timezone.utc).isoformat()
TELEMETRY = {"at_utc": "2026-10-17 19:35:33 UTC",
    "total_used_percent": 59, "window_minutes": 10080,
    "reset_unix": 1792745187, "ordinary_usage_allowed": True,
    "spend_control_reached": False, "rate_limit_reached_type": None,
    "total_ceiling_percent": 90, "review_integration_reserve": True}
inventory = {}
occurrences = 0


def record(path):
    absolute = (ROOT / path).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Outside assigned workspace: " + path)
    path = str(absolute.relative_to(ROOT))
    if path.startswith("problems/2024-B4/reviews/reasoning-sector3-return-r1-") and not path.startswith(PREFIX):
        raise SystemExit("New peer sector3 files forbidden: " + path)
    data = absolute.read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    global occurrences
    actual = record(expected["path"])
    if actual["sha256"] != expected["sha256"]:
        raise SystemExit("Immutable SHA changed: " + actual["path"])
    if expected.get("bytes") is not None and actual["bytes"] != expected["bytes"]:
        raise SystemExit("Immutable length changed: " + actual["path"])
    if actual["path"] in inventory and actual != inventory[actual["path"]]:
        raise SystemExit("Conflicting immutable records")
    inventory[actual["path"]] = actual
    occurrences += 1
    return actual


def load(row):
    return json.loads((ROOT / verify(row)["path"]).read_text())


def summary(rows):
    ordered = sorted({r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")}
                      for r in rows}.values(), key=lambda r: r["path"])
    data = json.dumps(ordered, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode()
    return {"unique_paths": len(ordered),
        "canonical_sorted_record_array_sha256": hashlib.sha256(data).hexdigest()}


def declared_rows(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("path"), str) and re.fullmatch("[0-9a-f]{64}", str(obj.get("sha256", ""))):
            yield obj
        for value in obj.values():
            yield from declared_rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from declared_rows(value)


def write_new(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return record(path)


for suffix in ("sources-v1.json", "input-validation-v1.json",
               "freeze-output-v1.json", "manifest-v1.json"):
    if (ROOT / (PREFIX + suffix)).exists():
        raise SystemExit("Refusing frozen output overwrite: " + suffix)

baseline = load(BASELINE)
assert baseline["assigned_prefix_unused_before_first_write"] is True
packet = [verify(row) for row in baseline["constructor_packet_records"]]
assert len(packet) == 10
assert packet[0]["sha256"] == "e8ca03cd139df7dcbe7508ad4c701e66d220a177c58ea01f8fac23a1788edd6a"
assert packet[-1]["sha256"] == "2a3cf9ce9d04b92f42a03e0847a478c6b3402e4eadf7067cb2addf4f97055be2"
constructor = json.loads((ROOT / packet[-1]["path"]).read_text())
assert len(constructor["artifacts"]) == 9
for row in constructor["artifacts"]:
    verify(row)

cb = load(baseline["constructor_inventory_reproduction"][0])
cv = load(baseline["constructor_inventory_reproduction"][1])
current_declared = [verify(row) for row in cb["direct_inputs_and_occupied_prefix_and_source_bytes"]
                    + cv["additional_source_records"]]
assert len(current_declared) == 47
assert summary(current_declared) == baseline["constructor_declarations_compact_summary"]
assert summary(current_declared)["canonical_sorted_record_array_sha256"] == cv["canonical_sorted_record_array_sha256"]
cp = load(cb["immutable_parent_manifest"])
parent_ctor_records = [verify(row) for row in cp["artifacts"]]
assert len(parent_ctor_records) == 8

own_parent = load(baseline["compact_immutable_own_parent"])
own_validation = load(baseline["compact_immutable_own_parent_validation"])
own_direct = [verify(row) for row in own_parent["artifacts"]]
own_direct.append(verify(baseline["compact_immutable_own_parent"]))
assert len(own_direct) == 11
assert summary(own_direct) == baseline["own_parent_direct_records_summary"]
assert own_validation["older_own_unique_paths_preserved"] == 365
binding = own_validation["compact_immutable_parent_binding"]
assert binding["older_own_preserved_summary"] == baseline["earlier_365_paths_bound_by_exact_parent_validation"]
verify(binding["immutable_parent_manifest"])
verify(binding["immutable_parent_validation"])
assert baseline["older_own_paths_bound_transitively"] == 376

authority_summaries = []
for row in baseline["old_accepted_scope_authorities"]:
    verify(row)
    if row["path"].endswith("-acceptance.json"):
        obj = json.loads((ROOT / row["path"]).read_text())
        declared = [verify(r) for r in declared_rows(obj)]
        authority_summaries.append({"immutable_authority": row,
            "necessary_declared_fingerprint_occurrences_reverified": len(declared),
            "necessary_declared_deduplicated_summary": summary(declared),
            "prior_full_inventory_occurrences_recorded_not_replayed": obj.get("record_occurrences_verified", obj.get("manifest_records_verified")),
            "prior_full_inventory_paths_recorded_not_replayed": obj.get("unique_paths_verified")})

# Existing read-only original-author source pages; no renderer or download.
pages = [7, 11, 12, 13, 14, 15, 18, 20, 21, 22, 23, 24, 25]
source_declaration = next(r for r in current_declared
    if r["path"] == "problems/2024-B4/notes/deep-literature-r2-search-sources-v1.json")
old_source = load(source_declaration)
old_images = {row["path"]: row for row in old_source["derived_cache_files"]}
image_records = []
for page in pages:
    path = ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-%02d.png" % page
    image_records.append(verify(old_images[path]))
thesis = verify(next(r for r in current_declared
    if r["path"].endswith("2024-mcguire-thesis-1995.pdf")))
official = verify(next(r for r in current_declared
    if r["path"] == ".cache/official/2024-paper_b.pdf"))

main = (ROOT / (PREFIX + "initial-v1.md")).read_text()
issues = (ROOT / (PREFIX + "issues-v1.md")).read_text()
ids = re.findall(r"^\| S3R1-(\d\d) \|", issues, flags=re.M)
assert ids == ["%02d" % i for i in range(1, 37)]
assert "Whole initial audit complete" in main
assert "Unresolved substantive issues: 0" in issues
prose = [record(PREFIX + s) for s in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md")]

sources = write_new("sources-v1.json", {
    "recorded_at_utc": STAMP,
    "reviewer": "/root/review_2022_complexity_r2",
    "fresh_initially_blind_NONCONSTRUCTOR_WHOLE": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "source_records": [
        {"id": "S01", "title": "McGuire1995 original-author thesis",
         "url": "https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf",
         "doi": "10.7907/1CZ2-6S05", "existing_cache": thesis,
         "pdf_pages_total": 97, "complete_visual_pages_read": pages,
         "printed_pages_read": "2,6--10,13,15--20",
         "existing_read_only_images": image_records,
         "complete_operative_Theorem2_1prime_statement_and_proof_read": True,
         "complete_PropositionA_and_proof_read": True,
         "exact_ambient_field_multiplicity_Bezout_definitions_read": True,
         "journal_attribution_page7_read": True,
         "journal_PDF_or_successful_publisher_abstract_read_this_audit": False,
         "new_download_or_render": False,
         "web_open_limit": "Normal PDF opening inaccessible; existing original-author scan read without alteration"},
        {"id": "S02", "title": "Hernando--McGuire0903.2016v4",
         "url": "https://arxiv.org/pdf/0903.2016v4",
         "read_scope": "matching definitions; component/whole distinction; i1 attribution; exact Theorem15/16 statements and nearby proof context; section6 reported counterexample; references",
         "role": "scope context only, not imported general whole theorem",
         "complete_global_proof_newly_audited_or_reported_factorization_rerun": False,
         "new_local_pdf_bytes_or_hash": None},
        {"id": "S03", "title": "Delgado--Janwa1207.5528v1",
         "url": "https://arxiv.org/pdf/1207.5528v1",
         "read_scope": "matching definitions; full Lemma1 statement/proof passage PDF4--5; diagonal discussion PDF9--10",
         "role": "selected-family context only; no arbitrary-target inference imported",
         "whole_paper_newly_audited": False, "new_local_pdf_bytes_or_hash": None},
        {"id": "S04", "title": "JMW1995 journal article",
         "doi": "10.1006/jabr.1995.1372",
         "url": "https://www.sciencedirect.com/science/article/pii/S0021869385713725",
         "bibliography": "J.Algebra178(2)(1995)665--676",
         "publisher_open_success_this_audit": False,
         "journal_full_proof_read": False,
         "operative_proof_source": "Original coauthor thesis S01, not publisher abstract",
         "Janwa_Wilson1993_original_proof_imported": False},
        {"id": "S05", "title": "Official2024 PaperB B4(b)",
         "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
         "existing_cache": official,
         "fresh_scope": "PDFpage2 B4(b), odd positive domain and coefficientwise/nonconstant definitions",
         "preliminary_part_a_proof_investigated_or_reproduced": False,
         "new_download": False}
    ],
    "old_accepted_scope_authorities": baseline["old_accepted_scope_authorities"],
    "old_accepted_body_read_limits_are_in_full_source_checks": True,
    "new_sector3_peer_findings_or_files_read": False,
    "PDF_skill_applied_read_only": True,
    "mathematical_program_CAS_scan_author_script_or_old_certificate_run": False,
    "cache_shared_old_Git_edit_spawn_contact_charge_or_bypass": False,
})

validation = write_new("input-validation-v1.json", {
    "checked_at_utc": STAMP,
    "administrative_only_not_mathematical_evidence": True,
    "baseline": BASELINE,
    "exact_constructor_packet_records": packet,
    "constructor_all9_artifact_records_and_freeze_reverified": True,
    "constructor_47_declared_fingerprint_occurrences_reverified": len(current_declared),
    "constructor_declared_deduplicated_summary": summary(current_declared),
    "constructor_inventory_exact_reproduction_refs": baseline["constructor_inventory_reproduction"],
    "constructor_immutable_parent_8_artifact_records_reverified": True,
    "accepted_authority_compact_summaries": authority_summaries,
    "old_PDF11_additional_page_matches_original_declared_hash": image_records[1],
    "compact_immutable_parent_binding": {
        "immutable_parent_manifest": baseline["compact_immutable_own_parent"],
        "immutable_parent_validation": baseline["compact_immutable_own_parent_validation"],
        "parent_direct11_records_summary": summary(own_direct),
        "earlier365_summary_in_immutable_parent": binding["older_own_preserved_summary"],
        "older_own_paths_bound_transitively": 376,
        "all_historical_own_paths_rehashed_this_audit": False,
        "historical_inventory_not_copied": True,
        "reproduction": "Follow exact2025R8 manifest/validation to its2017R4 R2 parent and previous chain; append2025R8 ten artifacts plus manifest. Immutable parents bind365 earlier paths;11 newly direct old paths give376."},
    "necessary_current_fingerprint_occurrences_reverified": occurrences,
    "current_verified_records_deduplicated_summary": summary(list(inventory.values())),
    "all36_author_obligation_rows_once": ids,
    "whole_claims_audited": ["S3A", "S3B", "S3C", "S3D"],
    "additional_counterexample_scope_attacks": 4,
    "substantive_issues_remaining": 0,
    "required_mathematical_repairs": 0,
    "new_prose_records": prose,
    "sources": sources,
    "new_peer_sector3_findings_read": False,
    "old_roles_disclosed_not_fresh_self_recertification": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "direct_weekly_telemetry": TELEMETRY,
    "no_mathematical_code_CAS_scan_rerun_or_forbidden_edit": True,
})

output = write_new("freeze-output-v1.json", {
    "COMPLETE_initially_blind_NONCONSTRUCTOR_WHOLE": True,
    "all36_author_obligations": True,
    "substantive_issue_or_required_repair": False,
    "new_peer_sector3_files_or_findings_read": False,
    "constructor_main": packet[0], "constructor_freeze": packet[-1],
    "input_validation": validation,
    "current_fingerprint_occurrences": occurrences,
    "current_unique_paths": len(inventory),
    "older_own_paths_preserved_transitively": 376,
    "mathematical_code_or_old_script_run": False,
})
artifacts = [record(PREFIX + suffix) for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "baseline-v1.json", "freeze-v1.py", "sources-v1.json",
    "input-validation-v1.json", "freeze-output-v1.json")]
assert artifacts[-1] == output
assert artifacts[-2] == validation

# Final read-only preservation check after every new output.
for row in list(inventory.values()):
    if record(row["path"]) != row:
        raise SystemExit("Input changed during review freeze: " + row["path"])
manifest = write_new("manifest-v1.json", {
    "frozen_at_utc": STAMP,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R1 initial; no promotion",
    "reviewer": "/root/review_2022_complexity_r2",
    "constructor_and_root_contributors_excluded_from_independent_count": True,
    "new_candidate_constructed_or_contributed_by_this_reviewer": False,
    "older_review_context_roles_disclosed_not_fresh_self_recertification": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "exact_constructor_main": packet[0], "exact_constructor_freeze": packet[-1],
    "whole_claims": ["S3A", "S3B", "S3C", "S3D"],
    "all36_author_obligations_reconstructed": True,
    "substantive_issues_remaining": 0,
    "required_mathematical_repair": False,
    "entire_initial_before_peer_comparison": True,
    "new_sector3_peer_files_or_findings_read": False,
    "operative_thesis_Theorem2_1prime_PropositionA_proofs_and_projective_setup_read": True,
    "journal_PDF_read": False,
    "no_complete_annual_classification_new_qualifying_family_or_novelty_claim": True,
    "compact_own_parent_manifest": baseline["compact_immutable_own_parent"],
    "compact_own_parent_validation": baseline["compact_immutable_own_parent_validation"],
    "older_own_paths_bound_transitively": 376,
    "historical_inventory_not_copied_or_claimed_freshly_reread": True,
    "constructor_47_fingerprint_records_reverified": True,
    "current_fingerprint_occurrences_reverified": occurrences,
    "current_verified_unique_paths": len(inventory),
    "no_math_code_scan_CAS_author_rerun_cache_old_shared_Git_edit_spawn_contact_charge_or_bypass": True,
    "direct_weekly_telemetry": TELEMETRY,
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
})
print(json.dumps({"COMPLETE": True, "manifest": manifest,
    "report": artifacts[0], "ledger": artifacts[1], "sources": artifacts[2],
    "input_validation": validation, "artifact_count": len(artifacts),
    "current_fingerprint_occurrences": occurrences, "current_unique_paths": len(inventory),
    "substantive_issues_remaining": 0, "new_peer_findings_read": False}))
