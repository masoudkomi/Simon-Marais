#!/usr/bin/env python3
"""Administrative whole EC R2 freeze only. No mathematics is executed.

Reads fingerprints, JSON and obligation labels. Never runs constructor or
older scripts, scans tilings, or opens NEW EC peer findings. All writes
are exclusive creations below this reviewer's assigned unused prefix.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/reasoning-value-return-r4-review-2-"
TP = "problems/2017-B4/notes/reasoning-value-return-r4-"
TARGET = {"path": TP + "candidate-v1.md", "bytes": 42968,
          "sha256": "e2c497814ebd8c9ec8b767c30be6cd37ca8ea9d2d9e51f5496bbd91c91bc854a"}
TARGET_FREEZE = {"path": TP + "freeze-v1.json", "bytes": 3773,
                 "sha256": "99df2683197f1a6e6e0f5c5696859c8c57b8a601bff3bf07d1bd6bd1fa831dca"}
PARENT_MANIFEST = {
    "path": "problems/2025-B4/reviews/reasoning-return-r7-review-2-manifest-v1.json",
    "bytes": 3975,
    "sha256": "e7aa0fe112734e27ba562cd8465b0f81bc62b6c6975cfe9adbb0e37e808a9b91"}
PARENT_VALIDATION = {
    "path": "problems/2025-B4/reviews/reasoning-return-r7-review-2-input-validation-v1.json",
    "bytes": 14846,
    "sha256": "8006b0f7a89865bfcd29b33d1dabac3fadf911188d4b38f1d6a5a740ccc9e256"}
for suffix in ("sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "manifest-v1.json"):
    if (ROOT / (PREFIX + suffix)).exists():
        raise SystemExit("Refusing frozen output overwrite: " + PREFIX + suffix)
inventory = {}
occurrences = 0


def rec(path):
    absolute = (ROOT / path).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Outside workspace")
    rel = str(absolute.relative_to(ROOT))
    if (rel.startswith("problems/2017-B4/reviews/reasoning-value-return-r4-")
            and not rel.startswith(PREFIX)):
        raise SystemExit("Forbidden NEW EC peer record: " + rel)
    data = absolute.read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    global occurrences
    actual = rec(expected["path"])
    if actual["sha256"] != expected["sha256"]:
        raise SystemExit("Fingerprint mismatch: " + actual["path"])
    if expected.get("bytes") is not None and actual["bytes"] != expected["bytes"]:
        raise SystemExit("Byte-length mismatch: " + actual["path"])
    if actual["path"] in inventory and inventory[actual["path"]] != actual:
        raise SystemExit("Inconsistent duplicate fingerprint")
    inventory[actual["path"]] = actual
    occurrences += 1
    return actual


def load(row):
    return json.loads((ROOT / verify(row)["path"]).read_text())


def rows(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("path"), str) and re.fullmatch("[0-9a-f]{64}", str(obj.get("sha256", ""))):
            yield obj
        for key, value in obj.items():
            if key == "artifacts" and isinstance(value, dict):
                for path, sha in value.items():
                    if isinstance(path, str) and re.fullmatch("[0-9a-f]{64}", str(sha)):
                        yield {"path": path, "sha256": sha}
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)


def digest(records):
    unique = {r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")} for r in records}
    ordered = [unique[p] for p in sorted(unique)]
    data = json.dumps(ordered, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return {"unique_paths": len(ordered),
            "canonical_sorted_record_array_sha256": hashlib.sha256(data).hexdigest(),
            "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), records sorted by path"}


# Reconstruct the exact own preservation chain without copying its inventory.
parent = load(PARENT_MANIFEST)
parent_val = load(PARENT_VALIDATION)
r7bind = parent_val["compact_immutable_parent_binding"]
cs_manifest_row = r7bind["immutable_parent_manifest"]
cs_validation_row = r7bind["immutable_parent_validation"]
cs = load(cs_manifest_row)
cs_val = load(cs_validation_row)
pb = cs_val["compact_immutable_parent_binding"]
old_manifest_row = pb["immutable_full_inventory_manifest_for_reproduction"]
old_validation_row = pb["immutable_full_inventory_validation_for_reproduction"]
old = load(old_manifest_row)
old_val = load(old_validation_row)
older_own = {}
for row in old_val["older_own_records"] + old["records"] + [old_manifest_row]:
    actual = verify(row)
    older_own[actual["path"]] = actual
for manifest_row in (pb["immutable_R9_manifest_for_reproduction"], pb["immutable_previous_manifest"]):
    doc = load(manifest_row)
    for row in doc["artifacts"] + [manifest_row]:
        actual = verify(row)
        older_own[actual["path"]] = actual
verify(pb["immutable_R9_validation_for_reproduction"])
verify(pb["immutable_previous_validation"])
if digest(list(older_own.values())) != pb["older_own_preserved_summary"]:
    raise SystemExit("341-path preservation digest mismatch")
for row in cs["artifacts"] + [cs_manifest_row]:
    actual = verify(row)
    older_own[actual["path"]] = actual
if digest(list(older_own.values())) != r7bind["older_own_preserved_summary"]:
    raise SystemExit("349-path preservation digest mismatch")
for row in parent["artifacts"] + [PARENT_MANIFEST]:
    actual = verify(row)
    older_own[actual["path"]] = actual
if len(older_own) != 357:
    raise SystemExit("Unexpected older-own count")

verify(TARGET)
constructor = load(TARGET_FREEZE)
constructor_records = [verify(row) for row in constructor["artifacts"]]
if len(constructor_records) != 10:
    raise SystemExit("Incomplete constructor packet")
source = json.loads((ROOT / (TP + "sources-v1.json")).read_text())
constructor_val = json.loads((ROOT / (TP + "input-validation-v1.json")).read_text())
direct = []
for key in ("official_and_protocol_fingerprints", "complete_accepted_bodies_read",
            "complete_core_acceptance_MD_scopes_read", "old_source_context_read"):
    for row in source[key]:
        direct.append(verify(row))
if len(source["complete_accepted_bodies_read"]) != 14:
    raise SystemExit("Unexpected accepted-body count")
authority_summaries = []
for row in source["accepted_authority_JSON_fingerprints"]:
    authority = verify(row)
    doc = json.loads((ROOT / authority["path"]).read_text())
    declared = [verify(r) for r in rows(doc)]
    authority_summaries.append({
        "immutable_authority": authority,
        "necessary_declared_fingerprint_occurrences_reverified": len(declared),
        "necessary_declared_deduplicated_summary": digest(declared),
        "transitive_historical_inventories_not_replayed": True})
if len(authority_summaries) != 14:
    raise SystemExit("Unexpected authority count")
constructor_parent = [verify(constructor_val[key]) for key in
                      ("previous_COMPLETE_own_manifest_bound", "immutable_parent_inventory_bound_not_copied")]

obligations = (ROOT / (TP + "obligations-v1.md")).read_text()
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
for number in range(1, 65):
    label = "|EC-O%02d|" % number
    if obligations.count(label) != 1 or ledger.count(label) != 1:
        raise SystemExit("Missing/duplicate whole obligation: " + label)
prose_names = ["initial.md", "issues-v1.md", "source-checks-v1.md"]
prose = [rec(PREFIX + name) for name in prose_names]
now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 18:56:21 UTC", "total_used_percent": 56,
             "window_minutes": 10080, "reset_unix": 1792745187,
             "spend_control_reached": False, "rate_limit_reached_type": None,
             "total_ceiling_percent": 90, "review_integration_reserve": True}
binding = {"immutable_parent_manifest": PARENT_MANIFEST,
           "immutable_parent_validation": PARENT_VALIDATION,
           "older_own_preserved_summary": digest(list(older_own.values())),
           "historical_inventory_not_copied": True,
           "reproduction": "Follow exact2025R7 parent validation to exact CS validation; reconstruct341 paths from its full older2022 inventory plus R9/2020R7 manifests; append CS8, then2025R7 eight artifacts/manifest paths, giving357. All are reverified without copying that growing inventory."}
primary_reads = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf",
     "scope": "Actual p2 B4 official whole domain/normalization only"},
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf",
     "scope": "Actual p12 B4 comments/count convention and attributed dictionary context, no numerical replay"},
    {"url": "https://arxiv.org/pdf/1609.02879",
     "version": "v2", "scope": "Complete Theorem1,2.1, relevant2.2 and Section4 constructive logical elimination; not whole Section3 or independent full complexity reconstruction",
     "import": "Published finite rational/real-algebraic polynomial QE, computable signs and dummy free variable"},
    {"url": "https://arxiv.org/pdf/1811.01702", "version": "v2",
     "scope": "Introduction beta definitions/Theorem1.1/Fourier-method attribution, Lemmas2.5--2.6 and complete planar2.4.1; not full general-dimensional/parabolic proofs",
     "import": "Classical methodology attribution only; EC1 special estimate reconstructed directly"},
    {"url": "https://annals.math.princeton.edu/2010/171-3/p12",
     "scope": "Publisher abstract/model context only", "import": "None; no SFT/strong-irreducibility theorem applied"}]
for primary in primary_reads:
    primary.update(read_date_utc="2026-10-17", new_native_binary_hash=None,
                   native_download_or_cache_write=False)


def new(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    with path.open("x") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


new("sources-v1.json", {
    "frozen_at_utc": now, "reviewer": "/root/review_2022_complexity_r2",
    "role": "fresh initially blind NONCONSTRUCTOR WHOLE R2, complete EC1--EC4/all64 obligations",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "target": TARGET, "constructor_freeze": TARGET_FREEZE,
    "complete_constructor_artifacts": constructor_records,
    "exact_direct_inputs_and_context": direct,
    "all14_accepted_bodies_freshly_read_completely": source["complete_accepted_bodies_read"],
    "five_core_acceptance_MD_freshly_read_completely": source["complete_core_acceptance_MD_scopes_read"],
    "old_context_rows_metadata_bound_not_claimed_fresh_complete_math_reads": source["old_source_context_read"],
    "primary_actual_reads": primary_reads,
    "old_allD_G_authorship_with_root_strategy_and_local_V_OP_HC_review_roles_disclosed": True,
    "new_EC_construction_contribution": False,
    "old_own_accepted_premises_not_independently_self_recertified": True,
    "new_EC_peer_findings_unread_before_entire_freeze": True,
    "root_pending_initial_findings_withheld_completion_identity_only": True,
    "compact_immutable_parent_binding": binding,
    "no_math_code_CAS_scan_QE_catalogue_or_count_execution_author_rerun": True,
    "no_old_shared_Git_cache_write_spawn_charge_contact_or_bypass": True,
    "direct_weekly_telemetry": telemetry})
new("input-validation-v1.json", {
    "frozen_at_utc": now, "administrative_only_not_mathematical_evidence": True,
    "constructor_artifacts_verified": constructor_records,
    "exact_direct_records": direct,
    "accepted_authority_compact_summaries": authority_summaries,
    "constructor_old_parent_metadata_bound_only": constructor_parent,
    "constructor_old_occurrences_recorded_not_replayed": constructor_val["verified_fingerprint_occurrences"],
    "constructor_old_deduplicated_paths_recorded_not_replayed": constructor_val["deduplicated_verified_paths"],
    "compact_immutable_parent_binding": binding,
    "older_own_unique_paths_preserved": len(older_own),
    "current_fingerprint_occurrences_reverified": occurrences,
    "current_verified_records_deduplicated_summary_only": digest(list(inventory.values())),
    "whole64_obligation_rows_covered_once": True, "prose_records": prose,
    "all_new_EC_peer_findings_unread_before_entire_freeze": True,
    "root_pending_initial_completion_identity_only": True,
    "no_math_code_CAS_scan_author_rerun_old_shared_Git_cache_edit": True,
    "direct_weekly_telemetry": telemetry})
new("freeze-output-v1.json", {
    "frozen_at_utc": now, "whole_initial_complete": True,
    "all64_author_obligations_covered": True, "substantive_issues": 0, "required_repairs": 0,
    "new_EC_peer_findings_unread_before_entire_freeze": True,
    "older_own_unique_paths_preserved": len(older_own),
    "record_occurrences_reverified": occurrences, "unique_paths_reverified": len(inventory),
    "no_math_code_CAS_scan_author_rerun_or_theoretical_algorithm_execution": True,
    "root_pending_initial_completion_identity_only": True,
    "coordinator_promotion_performed": False, "direct_weekly_telemetry": telemetry})
artifacts = [rec(PREFIX + name) for name in prose_names +
             ["freeze-v1.py", "sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json"]]
new("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; recommendation only, no promotion",
    "reviewer": "/root/review_2022_complexity_r2", "constructor": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "target": TARGET, "constructor_freeze": TARGET_FREEZE,
    "whole_claims": ["EC1 finite affine extraction", "EC2 effective local catalogue/finite strict block",
                     "EC3 total finite-M exact-GE recovery", "EC4 actual one-sided lower certificates"],
    "whole_author_obligations": 64, "substantive_issues": 0, "required_repairs": 0,
    "new_EC_peer_findings_unread_before_entire_freeze": True,
    "old_G_authorship_and_other_review_roles_disclosed_no_self_recertification": True,
    "no_new_EC_construction_contribution": True,
    "root_pending_initial_findings_withheld_completion_identity_only": True,
    "no_upper_R_two_sided_rate_value_annual_or_novelty_claim": True,
    "no_math_code_CAS_scan_algorithm_execution_author_rerun_old_shared_Git_cache_edit": True,
    "compact_parent_manifest": PARENT_MANIFEST, "compact_parent_validation": PARENT_VALIDATION,
    "historical_inventory_not_copied": True,
    "older_own_unique_paths_preserved": len(older_own),
    "record_occurrences_reverified": occurrences, "unique_paths_reverified": len(inventory),
    "direct_weekly_telemetry": telemetry,
    "command": "python3 " + PREFIX + "freeze-v1.py", "artifacts": artifacts})
print(json.dumps({"manifest": rec(PREFIX + "manifest-v1.json"), "artifacts": len(artifacts),
                  "whole_obligations": 64, "record_occurrences": occurrences,
                  "unique_paths": len(inventory), "older_own_paths": len(older_own)}, indent=2))
