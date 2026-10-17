"""R9 R2 compact integrity freeze only. No mathematical program or author rerun."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-return-r9-review-2-"
TARGET = "problems/2021-B4/notes/reasoning-return-r9-"
PREVIOUS = "problems/2025-B4/notes/reasoning-return-r7-"
BLOCKED = "problems/2021-B4/reviews/reasoning-return-r9-"


def fingerprint(path):
    if path.startswith(BLOCKED) and not path.startswith(PREFIX):
        raise RuntimeError("Blind guard: do not open new R9 peer metadata/findings")
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], expected["path"]
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], expected["path"]
    return actual


def read_json(path):
    fingerprint(path)  # Applies the same explicit blind guard.
    return json.loads((ROOT / path).read_text())


def declarations(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
                and isinstance(value.get("sha256"), str)
                and len(value["sha256"]) == 64):
            yield value
        for child in value.values():
            yield from declarations(child)
    elif isinstance(value, list):
        for child in value:
            yield from declarations(child)


def unique(records):
    result = {}
    for item in records:
        if item["path"] in result:
            assert result[item["path"]] == item, item["path"]
        result[item["path"]] = item
    return list(result.values())


def inventory_summary(records):
    values = sorted(unique(records), key=lambda r: r["path"])
    canonical = json.dumps(values, sort_keys=True, ensure_ascii=False,
                           separators=(",", ":")).encode()
    return {"unique_paths": len(values),
        "canonical_sorted_record_array_sha256": hashlib.sha256(canonical).hexdigest(),
        "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), sorted by path"}


def write_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return fingerprint(path)


for name in ["input-validation-v1.json", "manifest-v1.json"]:
    assert not (ROOT / (PREFIX + name)).exists()

main = verify({"path": TARGET + "candidate-v1.md", "bytes": 18824,
    "sha256": "b0f973b26d0eafdf293c41f73ce193d76b761b1229d016ceadc18e0c13f4b503"})
target_freeze = verify({"path": TARGET + "freeze-v1.json", "bytes": 4203,
    "sha256": "736bf5eb2c18eb8727c705e747583ca6ac3276d91b4d8829ed9c28277d3d2333"})
target = read_json(target_freeze["path"])
target_artifacts = [verify(r) for r in target["artifacts"]]
assert len(target_artifacts) == 10
sources = read_json(TARGET + "sources-v1.json")
validation = read_json(TARGET + "input-validation-v1.json")
declared = [verify(r) for obj in [target, sources, validation]
            for r in declarations(obj)]

# Reproduce the constructor's compact immutable-parent validation read-only.
binding = sources["compact_immutable_preservation_binding"]
author_parent_manifest = verify(binding["immutable_previous_manifest"])
author_parent_validation = verify(binding["immutable_previous_validation"])
author_parent = read_json(author_parent_validation["path"])
author_parent_records = [verify(r) for r in
    author_parent["deduplicated_all_verified_input_records"]]
assert inventory_summary(author_parent_records)["canonical_sorted_record_array_sha256"] == binding["parent_deduplicated_inputs_reverified"]["canonical_sorted_record_array_sha256"]
assert len(unique(author_parent_records)) == 1403

# Direct R8 scope authority and its frozen declarations, never new R9 peers.
authority_paths = [
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.json",
    "problems/2021-B4/notes/reasoning-return-r8-freeze-v1.json",
    "problems/2021-B4/notes/reasoning-return-r8-sources-v1.json",
    "problems/2021-B4/notes/reasoning-return-r8-input-validation-v1.json"]
authority = []
for path in authority_paths:
    obj = read_json(path)
    rows = [verify(r) for r in declarations(obj)]
    declared.extend(rows)
    authority.append({"metadata": fingerprint(path),
        "declared_occurrences_verified": len(rows),
        "deduplicated_summary": inventory_summary(rows)})

# Compactly preserve this reviewer's complete prior own chain via R7 parent.
previous_manifest = verify({"path": PREVIOUS + "freeze-v1.json", "bytes": 3864,
    "sha256": "0f3dc3419bc3f7a031a38f5d5d9448187cad39fe62588e4d5f43967e9c644174"})
previous = read_json(previous_manifest["path"])
previous_artifacts = [verify(r) for r in previous["artifacts"]]
previous_validation_record = next(r for r in previous_artifacts
    if r["path"] == PREVIOUS + "input-validation-v1.json")
previous_validation = read_json(previous_validation_record["path"])
ic_manifest_record = verify(previous_validation["immutable_parent_manifest"])
ic_validation_record = verify(previous_validation["immutable_parent_validation"])
ic = read_json(ic_manifest_record["path"])
ic_validation = read_json(ic_validation_record["path"])
prior_own = unique([verify(r) for r in ic_validation["earlier_unique_records_preserved"]]
    + [verify(r) for r in ic["artifacts"]] + [ic_manifest_record]
    + previous_artifacts + [previous_manifest])
assert len(prior_own) == 382

author_ids = re.findall(r"^\|R9-(\d\d)\|",
    (ROOT / (TARGET + "obligations-v1.md")).read_text(), re.MULTILINE)
review_pairs = re.findall(r"^\|R9R2-(\d\d) / R9-(\d\d)\|",
    (ROOT / (PREFIX + "issues-v1.md")).read_text(), re.MULTILINE)
assert author_ids == [f"{i:02}" for i in range(1, 47)]
assert review_pairs == [(i, i) for i in author_ids]
assert (ROOT / "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md").read_bytes().endswith(
    (ROOT / "problems/2021-B4/notes/reasoning-return-r8-candidate-v1.md").read_bytes())

now = datetime.now(timezone.utc).isoformat()
all_declared = unique(declared + author_parent_records + prior_own)
integrity = write_new("input-validation-v1.json", {
    "checked_at_utc": now,
    "administrative_metadata_only_not_mathematical_evidence": True,
    "candidate": main, "constructor_freeze": target_freeze,
    "all_ten_constructor_artifacts_verified": target_artifacts,
    "declared_fingerprint_occurrences_verified": len(declared),
    "declared_deduplicated_summary": inventory_summary(declared),
    "direct_authority_metadata": authority,
    "author_compact_parent_manifest": author_parent_manifest,
    "author_compact_parent_validation": author_parent_validation,
    "author_parent_reverified_summary": inventory_summary(author_parent_records),
    "reviewer_previous_manifest": previous_manifest,
    "reviewer_previous_validation": previous_validation_record,
    "reviewer_previous_parent_manifest": ic_manifest_record,
    "reviewer_previous_parent_validation": ic_validation_record,
    "earlier_own_unique_records_preserved": len(prior_own),
    "earlier_own_summary": inventory_summary(prior_own),
    "combined_deduplicated_summary": inventory_summary(all_declared),
    "full_historical_inventory_deliberately_not_copied": True,
    "exact_reproduction": "Use the immutable author parent deduplicated_all_verified_input_records; recursive path/sha256 declarations in target/source/validation and named R8 metadata; reconstruct reviewer prior chain from immutable IC earlier_unique_records_preserved plus its artifacts/manifest and previous R7 artifacts/manifest. The script verifies every byte/hash read-only; sort/deduplicate records as stated before hashing.",
    "complete_accepted_R5_R6_R7_R8_bodies_and_R8_scope_read": True,
    "accepted_R8_frozen_suffix_byte_identical": True,
    "OLD_R5_authorship_and_older_review_roles_disclosed": True,
    "NEW_R9_constructor_or_contributor": False,
    "all_author_obligation_IDs": author_ids,
    "all_independent_inference_IDs": [p[0] for p in review_pairs],
    "substantive_issues_found": 0, "required_author_repairs": 0,
    "root_peer_R9_report_ledger_source_manifest_or_findings_read_before_complete_initial_freeze": False,
    "root_completion_identity_notice_received_but_file_unopened": True,
    "blind_guard_prefix": BLOCKED,
    "sole_new_primary_theorem": {"url": "https://homepage.math.uiowa.edu/~atkinson/papers/HB_interp.pdf",
        "scope": "Atkinson-Sharma1969 Theorem2, sufficient only, all6pages definitions/proof read as extracted text",
        "native_pdf_downloaded_or_binary_hash_invented": False,
        "converse_or_all_roots_real_hypothesis_imported": False},
    "other_primary_contexts": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf", "scope": "actual page2 B4 hypothesis and(b)"},
        {"url": "https://arxiv.org/pdf/1208.5404", "scope": "displayed3.4/Lemma17; complete Proposition19 proof and unramified qualification"},
        {"url": "https://arxiv.org/pdf/1806.09561", "scope": "v6 metadata, Definition5.3, Theorem7.10 and full displayed computation proof; no rerun"},
        {"url": "https://arxiv.org/html/2608.14726v1", "scope": "intro/support/scenario and TheoremsB/C/D statements only"}],
    "math_code_CAS_scan_table_certificate_or_constructor_rerun": False,
    "old_shared_Git_cache_edit_spawn_contact_charge_bypass_or_live_native_job": False})

artifacts = [fingerprint(PREFIX + s) for s in ["initial-v1.md",
    "issues-v1.md", "source-checks-v1.md", "freeze-v1.py",
    "input-validation-v1.json"]]
manifest = write_new("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R9 R2; exact partial scope; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": main, "target_manifest": target_freeze,
    "constructor_artifact_count": 10, "whole_author_obligations": 46,
    "independent_inference_rows": 46,
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "NEW_R9_constructor_or_contributor": False,
    "OLD_R5_authorship_and_older_review_roles_disclosed_not_self_recertification": True,
    "whole_R9A_R9B_R9C_R9D_every_cubic_T4_zero_and_two_frames_reconstructed": True,
    "actual_primary_Hermite_Birkhoff_hypotheses_complete_sufficient_theorem_checked": True,
    "no_branch_degree20_annual_lift_or_novelty_claim": True,
    "new_root_peer_R9_findings_read_before_complete_initial_freeze": False,
    "declared_fingerprint_occurrences_verified": len(declared),
    "declared_deduplicated_paths_verified": len(unique(declared)),
    "author_parent_deduplicated_paths_verified": len(unique(author_parent_records)),
    "earlier_own_records_preserved": len(prior_own),
    "compact_provenance_without_repeated_historical_inventory": True,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 18:30:01UTC",
        "total_used_percent": 55, "window_minutes": 10080,
        "reset_unix": 1792745187, "total_ceiling_percent": 90,
        "review_integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts})
print(json.dumps({"report": artifacts[0], "manifest": manifest,
    "whole_rows": 46, "substantive_issues": 0, "required_repairs": 0,
    "declared_occurrences": len(declared),
    "declared_unique_paths": len(unique(declared)),
    "old_own_records": len(prior_own)}, indent=2))
