"""Administrative identity freeze only. No EC algorithm/math/count is run."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/reasoning-value-return-r4-"
seen = {}
occurrences = 0

def allowed(path):
    assert isinstance(path, str) and not Path(path).is_absolute(), path
    assert ".." not in Path(path).parts, path
    assert "coordinator-component-saturation-r1" not in path, "Queued CS remains unopened"
    assert not path.startswith("problems/2017-B4/reviews/reasoning-value-return-r4-"), "No new EC peer file"
    return ROOT / path

def fingerprint(path):
    data = allowed(path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def check(rec):
    global occurrences
    actual = fingerprint(rec["path"])
    assert actual["sha256"] == rec["sha256"], rec["path"]
    if rec.get("bytes") is not None:
        assert actual["bytes"] == rec["bytes"], rec["path"]
    if actual["path"] in seen:
        assert seen[actual["path"]] == actual, actual["path"]
    seen[actual["path"]] = actual
    occurrences += 1
    return actual

def read_json(path):
    return json.loads(allowed(path).read_text())

def write_new(path, obj):
    assert path.startswith(PREFIX), path
    with allowed(path).open("x") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")

def declared_records(obj):
    out = []
    if isinstance(obj, dict):
        if isinstance(obj.get("path"), str) and isinstance(obj.get("sha256"), str):
            out.append(obj)
        for key, value in obj.items():
            if key == "artifacts" and isinstance(value, dict):
                for path, digest in value.items():
                    if isinstance(path, str) and isinstance(digest, str) and re.fullmatch("[0-9a-f]{64}", digest):
                        out.append({"path": path, "sha256": digest})
            out.extend(declared_records(value))
    elif isinstance(obj, list):
        for value in obj:
            out.extend(declared_records(value))
    return out

source_path = PREFIX + "sources-v1.json"
source_fp = fingerprint(source_path)
sources = read_json(source_path)
for key in ["official_and_protocol_fingerprints", "complete_accepted_bodies_read", "complete_core_acceptance_MD_scopes_read", "old_source_context_read"]:
    for rec in sources[key]:
        check(rec)
assert len(sources["complete_accepted_bodies_read"]) == 14

authorities = []
for rec in sources["accepted_authority_JSON_fingerprints"]:
    authority_fp = check(rec)
    doc = read_json(rec["path"])
    records = declared_records(doc)
    for old in records:
        check(old)
    authorities.append({"authority": authority_fp, "declared_fingerprint_occurrences_checked": len(records)})
assert len(authorities) == 14

parent_manifest = check({
    "path": "problems/2022-B4/reviews/reasoning-return-r7-review-1-manifest-v1.json",
    "bytes": 3334,
    "sha256": "d55d873a3b1afc6730b07d53591efe2007fb55f8ba96c2ebb3fe81cb0a26192b",
})
parent_input = check({
    "path": "problems/2022-B4/reviews/reasoning-return-r7-review-1-input-validation-v1.json",
    "bytes": 208204,
    "sha256": "71e86424ce281319a76d4ce2f5152932c715c2b9455285914511ab128ffbf23e",
})
parent_doc = read_json(parent_manifest["path"])
for rec in parent_doc["artifacts"]:
    check(rec)
parent_data = read_json(parent_input["path"])
assert len(parent_data["older_own_packets"]) == 61
old_artifact_occurrences = len(parent_doc["artifacts"])
for packet in parent_data["older_own_packets"]:
    check(packet["manifest"])
    for rec in packet["checks"]:
        check(rec)
    old_artifact_occurrences += len(packet["checks"])
addenda = [check(parent_data[key]) for key in [
    "GK_separate_telemetry_addendum_preserved",
    "IC_separate_hash_only_authority_addendum_preserved",
]]
older_own_packet_count = 62

obligations = allowed(PREFIX + "obligations-v1.md").read_text()
ids = sorted(set(re.findall(r"EC-O\d{2}", obligations)))
assert ids == [f"EC-O{i:02d}" for i in range(1, 65)]
for suffix in ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md", "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md"]:
    assert fingerprint(PREFIX + suffix)["bytes"] > 2000
main_text = allowed(PREFIX + "candidate-v1.md").read_text()
assert "Candidate proof - unverified" in main_text
for label in ["EC1", "EC2", "EC3", "EC4"]:
    assert label in main_text

deduplicated = [seen[path] for path in sorted(seen)]
dedup_digest = hashlib.sha256(json.dumps(deduplicated, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
now = datetime.now(timezone.utc).isoformat()
validation = {
    "checked_at_utc": now,
    "administrative_identity_only_not_mathematical_evidence": True,
    "source_packet_bound": source_fp,
    "complete_accepted_bodies_and_context_fingerprints_checked": True,
    "accepted_authorities": authorities,
    "previous_COMPLETE_own_manifest_bound": parent_manifest,
    "immutable_parent_inventory_bound_not_copied": parent_input,
    "older_own_packets_preserved": older_own_packet_count,
    "older_own_artifact_descriptor_occurrences_checked": old_artifact_occurrences,
    "separate_older_addenda_preserved": addenda,
    "all_necessary_direct_declared_rows_including_SHA_only_checked": True,
    "transitive_old_metadata_bound_by_hash_unrelated_math_not_reread": True,
    "verified_fingerprint_occurrences": occurrences,
    "deduplicated_verified_paths": len(deduplicated),
    "deduplicated_fingerprint_digest_sha256": dedup_digest,
    "digest_reproduction": "Sort actual verified {path,bytes,sha256} records by path; JSON sort_keys=True separators=(',',':'); SHA256 UTF8. Exact source/authority/parent references and this administrative script reproduce the set.",
    "compact_preservation_requested_by_coordinator": True,
    "whole_obligation_count": 64,
    "whole_obligation_IDs": ids,
    "old_roles_disclosed_no_independent_self_recertification": True,
    "root_new_EC_proof_inference_or_constant_contribution": False,
    "two_OTHER_fresh_initially_blind_WHOLE_audits_required": True,
    "candidate_unverified_no_promotion": True,
    "EC_theoretical_algorithms_executed_or_mathematical_program_CAS_scan_rerun": False,
    "two_sided_upper_R_absolute_rate_value_annual_or_novelty_resolved": False,
    "queued_2024_CS_packet_or_new_peer_findings_read": False,
    "Git_shared_old_bytes_cache_edit_spawning_charge_contact_or_bypass": False,
    "only_assigned_new_prefix_written": True,
    "latest_authoritative_weekly_usage": sources["latest_authoritative_weekly_usage"],
}
write_new(PREFIX + "input-validation-v1.json", validation)
output = {
    "completed_at_utc": now,
    "status": "COMPLETE constructor freeze; candidate proof - unverified",
    "claims": ["EC1", "EC2", "EC3", "EC4"],
    "whole_obligations": 64,
    "complete_accepted_bodies": 14,
    "accepted_authorities_bound": 14,
    "verified_fingerprint_occurrences": occurrences,
    "deduplicated_verified_paths": len(deduplicated),
    "deduplicated_fingerprint_digest_sha256": dedup_digest,
    "older_own_packets_preserved": older_own_packet_count,
    "older_addenda_preserved": 2,
    "mathematical_code_CAS_scan_or_algorithm_execution": False,
    "queued_CS_or_peer_findings_opened": False,
    "two_OTHER_fresh_whole_audits_then_coordinator_reconciliation_required": True,
}
write_new(PREFIX + "freeze-output-v1.json", output)
artifacts = [fingerprint(PREFIX + suffix) for suffix in [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md",
    "sources-v1.json", "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json",
]]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE constructor checkpoint",
    "constructor": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "verified_effective_settings": None,
    "claims": ["EC1 finite affine estimate", "EC2 finite local recovery catalogue", "EC3 effective finite-M GE recovery", "EC4 one-sided finite certificates and left semicomputability"],
    "whole_obligations": 64,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_WHOLE_audits": True,
    "root_broad_assignment_only_no_new_EC_proof_inference_or_constant": True,
    "old_authorship_and_review_roles_disclosed": True,
    "accepted_old_premises_not_independently_self_recertified": True,
    "upper_R_two_sided_rate_numerical_value_annual_or_novelty_claim": False,
    "mathematical_code_CAS_scan_count_rerun_or_theoretical_algorithm_execution": False,
    "all_sixty_two_older_own_packets_and_two_addenda_preserved": True,
    "compact_parent_binding_and_deduplicated_integrity_summary": True,
    "verified_fingerprint_occurrences": occurrences,
    "deduplicated_verified_paths": len(deduplicated),
    "queued_2024_CS_packet_or_new_peer_findings_read": False,
    "Git_shared_old_bytes_cache_edit_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": sources["latest_authoritative_weekly_usage"],
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
write_new(PREFIX + "freeze-v1.json", manifest)
print(json.dumps({**output, "main": artifacts[0], "manifest": fingerprint(PREFIX + "freeze-v1.json")}, indent=2))
