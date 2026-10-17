"""IC R2 administrative provenance freeze. No mathematical computation."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/reasoning-components-r1-review-2-"
TARGET = "problems/2024-B4/notes/reasoning-components-r1-"
PREVIOUS = "problems/2019-B4/reviews/auxiliary-presentation-r1-review-2-"


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(record):
    actual = fingerprint(record["path"])
    assert actual["sha256"] == record["sha256"], record["path"]
    if "bytes" in record:
        assert actual["bytes"] == record["bytes"], record["path"]
    return actual


def declarations(value):
    if isinstance(value, dict):
        if ("path" in value and isinstance(value.get("sha256"), str)
                and len(value["sha256"]) == 64):
            yield value
        for child in value.values():
            yield from declarations(child)
    elif isinstance(value, list):
        for child in value:
            yield from declarations(child)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def write_new(suffix, value):
    with (ROOT / (PREFIX + suffix)).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return fingerprint(PREFIX + suffix)


assert not (ROOT / (PREFIX + "input-validation-v1.json")).exists()
assert not (ROOT / (PREFIX + "manifest-v1.json")).exists()
target_main = verify({"path": TARGET + "candidate-v1.md", "bytes": 24588,
    "sha256": "21a23e6dedf5531b23c004e78cc4bf54253e356fa29676d97a9ae6e23d5bee48"})
target_freeze = verify({"path": TARGET + "freeze-v1.json", "bytes": 3689,
    "sha256": "1c2ac7f2322f7e83d62cfbb563c312eca75aa536448e875f849c9b2195ffd5e9"})
target_addendum = verify({"path": TARGET + "authority-hash-only-addendum-v1.json",
    "bytes": 3673,
    "sha256": "3aac70a9a54b40f00087007562de109d9325419190e65aecbea9bae76c9b7133"})
target_manifest = read_json(target_freeze["path"])
target_records = [verify(record) for record in target_manifest["artifacts"]]
assert len(target_records) == 9
source = read_json(TARGET + "sources-v1.json")
author_validation = read_json(TARGET + "input-validation-v1.json")
addendum = read_json(target_addendum["path"])

declared = []
hash_only = []
for obj in [target_manifest, source, author_validation, addendum]:
    for record in declarations(obj):
        actual = verify(record)
        declared.append(actual)
        if "bytes" not in record:
            hash_only.append(actual)

authority_details = []
for path in source["accepted_authority_paths"]:
    authority = read_json(path)
    full_or_hash_only = []
    for record in declarations(authority):
        actual = verify(record)
        declared.append(actual)
        full_or_hash_only.append(actual)
        if "bytes" not in record:
            hash_only.append(actual)
    legacy = []
    for relative, value in authority.get("artifacts", {}).items():
        if isinstance(value, str) and len(value) == 64:
            path_record = {"path": "problems/2024-B4/" + relative,
                           "sha256": value}
            actual = verify(path_record)
            declared.append(actual)
            legacy.append(actual)
    authority_details.append({"authority": fingerprint(path),
        "declared_records_verified": full_or_hash_only,
        "legacy_path_hash_map_verified": legacy})
assert len(authority_details) == 12
assert len(hash_only) == 2
declared_unique = {}
for record in declared:
    if record["path"] in declared_unique:
        assert record == declared_unique[record["path"]]
    declared_unique[record["path"]] = record

previous_manifest_record = verify({"path": PREVIOUS + "manifest-v1.json",
    "bytes": 3194,
    "sha256": "9050e6b9373c873012f8aeb668b9c9a89306273aaaefcff4ed923440021e5d50"})
previous_manifest = read_json(previous_manifest_record["path"])
previous_validation_path = PREVIOUS + "input-validation-v1.json"
verify(next(record for record in previous_manifest["artifacts"]
            if record["path"] == previous_validation_path))
previous_validation = read_json(previous_validation_path)
prior = {}
for record in (previous_validation["earlier_unique_records_preserved"]
               + previous_manifest["artifacts"] + [previous_manifest_record]):
    actual = verify(record)
    if actual["path"] in prior:
        assert prior[actual["path"]] == actual
    prior[actual["path"]] = actual
assert len(prior) == 367

author_ids = re.findall(r"^\| IC-(\d\d) \|",
    (ROOT / (TARGET + "obligations-v1.md")).read_text(), re.MULTILINE)
review_ids = re.findall(r"^\|ICR2-(\d\d)\|",
    (ROOT / (PREFIX + "issues-v1.md")).read_text(), re.MULTILINE)
assert author_ids == [f"{i:02}" for i in range(1, 49)]
assert review_ids == author_ids
now = datetime.now(timezone.utc).isoformat()
primary = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
     "read": "Complete actual B4 domain and(b), coefficientwise congruence and nonconstant-mod2 definition; no preliminary construction research"},
    {"url": "https://arxiv.org/pdf/1612.05997v1",
     "read": "Printed6 quotient/affine definitions and COMPLETE printed7 Section3 eq5 J statement; old local extraction and pre-existing whole-page image actually inspected",
     "limit": "Original1993 proof not read/reconstructed; published J imported through primary coauthor statement. Adjacent odd-k/extension/APN and later parity/transversality statements not imported"},
    {"url": "https://arxiv.org/pdf/1207.5528v1",
     "read": "Kasami factorization and complete Lemma1(b) with short written proof on printed5",
     "limit": "Already published pure-base distinct-q subcase attributed, no novelty or full paper audit"},
]
validation = write_new("input-validation-v1.json", {
    "validated_at_utc": now, "administrative_metadata_only_not_mathematical_proof": True,
    "complete_target_nine_artifacts_freeze_and_separate_addendum": target_records + [target_freeze, target_addendum],
    "declared_author_fingerprint_occurrences_verified": len(declared),
    "declared_author_unique_paths_verified": [declared_unique[path] for path in sorted(declared_unique)],
    "twelve_accepted_authority_declarations_and_legacy_maps_verified": authority_details,
    "two_legacy_hash_only_divisor_declarations_explicitly_verified": hash_only,
    "author_sixty_older_packets_metadata_checked_not_fresh_proof_reread": len(author_validation["older_own_packets"]),
    "earlier_unique_records_preserved": [prior[path] for path in sorted(prior)],
    "earlier_unique_record_count": len(prior),
    "all_author_obligation_IDs": author_ids, "all_independent_inference_IDs": review_ids,
    "whole_accepted_KC_GK_bodies_scopes_read": True,
    "OLD_CP_NV_whole_bodies_and_all_other_eight_authority_MD_scopes_read": True,
    "all_twelve_older_mathematical_bodies_freshly_reread_or_recertified": False,
    "reviewer_NEW_IC_constructor_or_contributor": False,
    "OLD_CP_authorship_and_older_2024_review_roles_disclosed": True,
    "new_IC_peer_root_report_manifest_ledger_or_findings_read_before_complete_initial_freeze": False,
    "blind_guard_prefix": "problems/2024-B4/reviews/reasoning-components-r1-review-1-",
    "primary_reads_and_exact_limits": primary,
    "published_J_original_proof_read_or_abs_irreducibility_reproved": False,
    "J_coauthor_statement_and_existing_image_actually_seen": True,
    "source_free_IC1_separate_from_J_applications": True,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "new_native_download_cache_mutation_live_text_binary_identity_or_third_party_redistribution": False,
    "old_shared_Git_edit_spawning_contact_charge_bypass_or_pending_native_job": False,
})
artifacts = [fingerprint(PREFIX + suffix) for suffix in [
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md", "freeze-v1.py"]] + [validation]
manifest = write_new("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE IC R2; no substantive scoped defect or required repair; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": target_main, "target_manifest": target_freeze,
    "separate_administrative_addendum": target_addendum,
    "whole_author_obligations": 48, "independent_inference_rows": 48,
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "reviewer_NEW_IC_constructor_or_contributor": False,
    "OLD_CP_authorship_and_older_review_roles_disclosed_not_self_recertification": True,
    "complete_IC1_IC2_IC3_IC4_and_every_boundary_reconstructed": True,
    "exact_cofactor_unit_contact_not_lower_bound_and_individual_to_whole_order_checked": True,
    "ordinary_F2_orbits_mixed_q_every_index_and_q16_proper_gaps_retained": True,
    "published_J_coauthor_statement_verified_original1993_proof_unread": True,
    "no_annual_new_qualifying_family_or_novelty_claim": True,
    "new_IC_peer_root_findings_read_before_complete_initial_freeze": False,
    "declared_author_fingerprint_occurrences_verified": len(declared),
    "declared_author_unique_paths_verified": len(declared_unique),
    "explicit_hash_only_declarations_verified": len(hash_only),
    "author_older_packet_metadata_count": len(author_validation["older_own_packets"]),
    "earlier_frozen_context_records_verified_unchanged": len(prior),
    "mathematical_program_CAS_scan_source_certificate_or_author_rerun": False,
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 17:53:46UTC",
        "total_used_percent": 52, "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "review_integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
})
print(json.dumps({"manifest": manifest, "main": artifacts[0],
    "whole_author_obligations": 48, "independent_inference_rows": 48,
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "target_artifacts_plus_freeze_addendum": len(target_records) + 2,
    "declared_author_fingerprint_occurrences_verified": len(declared),
    "declared_author_unique_paths_verified": len(declared_unique),
    "explicit_hash_only_declarations_verified": len(hash_only),
    "earlier_unique_records_preserved": len(prior)}, indent=2))
