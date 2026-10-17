"""2020 R7 R2 compact administrative integrity freeze; no mathematical code.

Only new review-prefix outputs are written, exclusively. No author rerun.
An explicit guard rejects every new R7 peer-review path, even metadata.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-return-r7-review-2-"
TARGET = "problems/2020-B4/notes/reasoning-return-r7-"
BLOCKED = "problems/2020-B4/reviews/reasoning-return-r7-"
PREVIOUS = "problems/2021-B4/reviews/reasoning-return-r9-review-2-"


def fingerprint(path):
    absolute = (ROOT / path).resolve()
    assert absolute.is_relative_to(ROOT), path
    path = str(absolute.relative_to(ROOT))
    if path.startswith(BLOCKED) and not path.startswith(PREFIX):
        raise RuntimeError("Blind guard: no NEW R7 root/peer report or metadata")
    body = absolute.read_bytes()
    return {"path": path, "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], expected["path"]
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], expected["path"]
    return actual


def read_json(path):
    fingerprint(path)  # Same blind guard, including metadata-only reads.
    return json.loads((ROOT / path).read_text())


def declarations(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and isinstance(obj.get("sha256"), str)
                and len(obj["sha256"]) == 64):
            yield obj
        for child in obj.values():
            yield from declarations(child)
    elif isinstance(obj, list):
        for child in obj:
            yield from declarations(child)


def unique(rows):
    result = {}
    for row in rows:
        item = {k: row[k] for k in ["path", "bytes", "sha256"]}
        assert item["path"] not in result or result[item["path"]] == item
        result[item["path"]] = item
    return list(result.values())


def digest(rows):
    values = sorted(unique(rows), key=lambda r: r["path"])
    canonical = json.dumps(values, sort_keys=True, ensure_ascii=False,
                           separators=(",", ":")).encode()
    return {"unique_paths": len(values),
        "canonical_sorted_record_array_sha256": hashlib.sha256(canonical).hexdigest(),
        "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), sorted by path"}


def write_new(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")
    return fingerprint(path)


for suffix in ["input-validation-v1.json", "manifest-v1.json"]:
    assert not (ROOT / (PREFIX + suffix)).exists()

main = verify({"path": TARGET + "candidate-v1.md", "bytes": 21471,
    "sha256": "4a0866b149aab5beb0dd0b7e76bf6abaf90355085178ea8ea18b2b539e5abe7b"})
constructor_freeze = verify({"path": TARGET + "freeze-v1.json", "bytes": 4168,
    "sha256": "b83040ef82ae1b4ef8393b4d1c8799fd095ed4d81a52a7ebb03aff8087fb649a"})
target = read_json(constructor_freeze["path"])
target_artifacts = [verify(r) for r in target["artifacts"]]
assert len(target_artifacts) == 10
sources = read_json(TARGET + "sources-v1.json")
validation = read_json(TARGET + "input-validation-v1.json")
declared = [verify(r) for obj in [target, sources, validation]
            for r in declarations(obj)]

# Reproduce the constructor's compact OLD-OWN inventory, not unrelated
# historical mathematical inventories. Every referenced parent is bound.
binding = validation["compact_immutable_preservation_binding"]
author_parent_manifest_record = verify(binding["immutable_parent_manifest"])
author_parent_validation_record = verify(binding["immutable_parent_validation"])
author_parent = read_json(author_parent_manifest_record["path"])
author_parent_validation = read_json(author_parent_validation_record["path"])
author_reproduction_manifest_record = verify(binding["exact_parent_reproduction_manifest"])
author_reproduction_validation_record = verify(binding["exact_parent_reproduction_validation"])
author_reproduction_manifest = read_json(author_reproduction_manifest_record["path"])
author_reproduction_validation = read_json(author_reproduction_validation_record["path"])
author_old = unique([verify(r) for r in
    author_reproduction_validation["older_own_records"]
    + author_reproduction_manifest["records"]
    + [author_reproduction_manifest_record]
    + author_parent["artifacts"] + [author_parent_manifest_record]])
assert len(author_old) == 330
assert digest(author_old)["canonical_sorted_record_array_sha256"] == binding[
    "older_own_records_reverified_including_parent_packet"]["canonical_sorted_record_array_sha256"]

authority = []
for descriptor in validation["declared_authority_metadata_reverification_summaries"]:
    metadata = verify(descriptor["immutable_metadata_source"])
    rows = [verify(r) for r in declarations(read_json(metadata["path"]))]
    assert len(rows) == descriptor["declared_fingerprint_occurrences_reverified"]
    assert digest(rows)["canonical_sorted_record_array_sha256"] == descriptor[
        "deduplicated_declared_inventory"]["canonical_sorted_record_array_sha256"]
    declared.extend(rows)
    authority.append({"metadata": metadata,
        "declared_occurrences_verified": len(rows), "deduplicated_summary": digest(rows)})

# Compact preservation of the reviewer's OWN complete prior chain.
# Do not copy the growing historical inventory to this output.
previous_manifest_record = verify({"path": PREVIOUS + "manifest-v1.json", "bytes": 3166,
    "sha256": "2e99bcf560a5c45a1f0da6d12bb4c06ef9402ea8be8748b5253166ecb89c7fbb"})
previous = read_json(previous_manifest_record["path"])
previous_artifacts = [verify(r) for r in previous["artifacts"]]
previous_validation_record = next(r for r in previous_artifacts
    if r["path"] == PREVIOUS + "input-validation-v1.json")
previous_validation = read_json(previous_validation_record["path"])
prior_2025_manifest_record = verify(previous_validation["reviewer_previous_manifest"])
prior_2025_validation_record = verify(previous_validation["reviewer_previous_validation"])
prior_2025 = read_json(prior_2025_manifest_record["path"])
ic_manifest_record = verify(previous_validation["reviewer_previous_parent_manifest"])
ic_validation_record = verify(previous_validation["reviewer_previous_parent_validation"])
ic = read_json(ic_manifest_record["path"])
ic_validation = read_json(ic_validation_record["path"])
prior_own = unique([verify(r) for r in
    ic_validation["earlier_unique_records_preserved"]
    + ic["artifacts"] + [ic_manifest_record]
    + prior_2025["artifacts"] + [prior_2025_manifest_record]
    + previous_artifacts + [previous_manifest_record]])
assert len(prior_own) == 388

author_ids = re.findall(r"^\|R7-(\d\d)\|",
    (ROOT / (TARGET + "obligations-v1.md")).read_text(), re.MULTILINE)
review_pairs = re.findall(r"^\|R7R2-(\d\d) / R7-(\d\d)\|",
    (ROOT / (PREFIX + "issues-v1.md")).read_text(), re.MULTILINE)
assert author_ids == [f"{i:02}" for i in range(1, 57)]
assert review_pairs == [(i, i) for i in author_ids]

now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 18:41:50UTC",
    "total_used_percent": 56, "window_minutes": 10080,
    "reset_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_ceiling_percent": 90, "review_integration_reserve": True}
all_verified = unique(declared + author_old + prior_own)
integrity = write_new("input-validation-v1.json", {
    "checked_at_utc": now,
    "administrative_metadata_only_not_mathematical_evidence": True,
    "candidate": main, "constructor_freeze": constructor_freeze,
    "all_ten_constructor_artifacts_verified": target_artifacts,
    "declared_fingerprint_occurrences_verified": len(declared),
    "declared_deduplicated_summary": digest(declared),
    "exact_authority_metadata": authority,
    "author_immutable_parent_manifest": author_parent_manifest_record,
    "author_immutable_parent_validation": author_parent_validation_record,
    "author_exact_reproduction_manifest": author_reproduction_manifest_record,
    "author_exact_reproduction_validation": author_reproduction_validation_record,
    "author_older_own_paths_reverified": len(author_old),
    "author_older_own_summary": digest(author_old),
    "author_unrelated_historical_summary_immutable_binding_only": binding[
        "parent_recorded_all_input_summary_not_copied"],
    "reviewer_previous_manifest": previous_manifest_record,
    "reviewer_previous_validation": previous_validation_record,
    "reviewer_prior_2025_manifest": prior_2025_manifest_record,
    "reviewer_prior_2025_validation": prior_2025_validation_record,
    "reviewer_prior_IC_manifest": ic_manifest_record,
    "reviewer_prior_IC_validation": ic_validation_record,
    "earlier_own_unique_records_preserved": len(prior_own),
    "earlier_own_summary": digest(prior_own),
    "combined_deduplicated_summary": digest(all_verified),
    "full_historical_inventory_deliberately_not_copied": True,
    "exact_reproduction": "Use recursive path/sha256 declarations in target/source/validation plus each named authority metadata. Reconstruct author330 from immutable reproduction validation older_own_records, reproduction manifest records/manifest and author parent artifacts/manifest. Reconstruct reviewer388 from immutable IC validation earlier_unique_records_preserved, IC artifacts/manifest, prior2025 artifacts/manifest, previousR9review artifacts/manifest. Verify all bytes/hashes read-only, deduplicate and sort by path before the stated canonical digest.",
    "whole_author_obligation_IDs": author_ids,
    "independent_inference_IDs": [p[0] for p in review_pairs],
    "complete_new_R7A_R7B_R7C_R7D_R7E_reconstructed": True,
    "OLD_repaired_R3_and_R6_authorship_R4_R5_review_roles_disclosed": True,
    "NEW_R7_constructor_or_proof_contributor": False,
    "substantive_issues_found": 0, "required_author_repairs": 0,
    "root_peer_R7_reports_ledgers_sources_metadata_or_findings_read_before_complete_initial_freeze": False,
    "all_mathematical_findings_withheld_until_root_entire_R1_freeze": True,
    "blind_guard_prefix": BLOCKED,
    "full_accepted_initial_R4_R5_R6_bodies_and_three_acceptance_MD_scopes_read": True,
    "R3_fresh_read_limit": "header/first100lines plus inherited prior authorship; not a new full reread claim",
    "primary_read_scope_record": PREFIX + "source-checks-v1.md",
    "native_PDF_hash_fabricated_or_new_full_paper_cached": False,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "old_shared_Git_cache_edit_spawn_contact_charge_bypass_or_live_native_job": False,
    "last_direct_weekly_telemetry": telemetry})

artifacts = [fingerprint(PREFIX + suffix) for suffix in ["initial-v1.md",
    "issues-v1.md", "source-checks-v1.md", "freeze-v1.py",
    "input-validation-v1.json"]]
manifest = write_new("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2020R7 R2; exact partial scope; root reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "target": main, "target_manifest": constructor_freeze,
    "constructor_artifact_count": 10, "whole_author_obligations": 56,
    "independent_inference_rows": 56,
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "NEW_R7_constructor_or_proof_contributor": False,
    "OLD_repaired_R3_R6_authorship_and_R4_R5_review_roles_disclosed": True,
    "complete_R7A_to_R7E_including_prime_lift_unit_gap_and_actual_proper_quotients": True,
    "all_new_root_peer_R7_findings_unread_through_complete_initial_freeze": True,
    "withhold_all_mathematical_findings_until_root_complete_R1_freeze": True,
    "no_annual_classification_new_forbidden_order_cutoff_or_novelty_claim": True,
    "declared_fingerprint_occurrences_verified": len(declared),
    "declared_deduplicated_paths_verified": len(unique(declared)),
    "author_older_own_paths_preserved": len(author_old),
    "reviewer_earlier_own_paths_preserved": len(prior_own),
    "compact_provenance_without_repeated_historical_inventory": True,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "last_direct_weekly_telemetry": telemetry,
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts})
# Print only the identity/completion needed for the first parent notice.
# Mathematical conclusions remain in the complete frozen packet.
print(json.dumps({"complete_initial_freeze": True, "manifest": manifest,
                  "mathematical_findings_withheld_pending_root_R1_freeze": True}, indent=2))
