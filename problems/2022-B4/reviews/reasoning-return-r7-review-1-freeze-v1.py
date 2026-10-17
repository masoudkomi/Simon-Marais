"""Administrative SHA/JSON freeze only; no mathematical computation or rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/reviews/reasoning-return-r7-review-1-"
TARGET_PREFIX = "problems/2022-B4/notes/reasoning-return-r7-"
NEW_PEER_PREFIX = "problems/2022-B4/reviews/reasoning-return-r7-"

def admissible(path):
    assert isinstance(path, str) and not Path(path).is_absolute(), path
    assert ".." not in Path(path).parts, path
    assert not (path.startswith(NEW_PEER_PREFIX) and not path.startswith(PREFIX)), "Refuse new peer R7 file: " + path
    return ROOT / path

def fp(path):
    data = admissible(path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def check(rec):
    actual = fp(rec["path"])
    assert actual["sha256"] == rec["sha256"], actual["path"]
    if "bytes" in rec:
        assert actual["bytes"] == rec["bytes"], actual["path"]
    actual["matches"] = True
    return actual

def read_json(path):
    return json.loads(admissible(path).read_text())

def write_new(path, obj):
    out = admissible(path)
    assert path.startswith(PREFIX), path
    with out.open("x") as f:
        json.dump(obj, f, indent=2)
        f.write("\n")

def records(obj):
    out = []
    if isinstance(obj, dict):
        if isinstance(obj.get("path"), str) and isinstance(obj.get("sha256"), str):
            out.append(obj)
        for key, value in obj.items():
            if key == "artifacts" and isinstance(value, dict):
                for path, value_hash in value.items():
                    if isinstance(path, str) and isinstance(value_hash, str) and re.fullmatch("[0-9a-f]{64}", value_hash):
                        out.append({"path": path, "sha256": value_hash})
            out.extend(records(value))
    elif isinstance(obj, list):
        for value in obj:
            out.extend(records(value))
    return out

manifest_path = TARGET_PREFIX + "freeze-v1.json"
target_manifest = check({"path": manifest_path, "bytes": 3683, "sha256": "f1894610350eb829c7be4c93329cc9054420ac111f5f28c3d0c709099529df69"})
target_doc = read_json(manifest_path)
assert len(target_doc["artifacts"]) == 10
target_checks = [check(rec) for rec in target_doc["artifacts"]]
assert target_checks[0]["path"] == TARGET_PREFIX + "candidate-v1.md"
assert target_checks[0]["bytes"] == 20450
assert target_checks[0]["sha256"] == "874e30f4fef000510edc0e67541161a735d5e11654e430ff283f4610047abd1e"
target_input = read_json(TARGET_PREFIX + "input-validation-v1.json")
constructor_old_checks = [check(rec) for rec in target_input["earlier_unique_records_preserved"]]
assert len(constructor_old_checks) == 350
accepted_context = [check(rec) for rec in target_input["accepted_context_fingerprints"]]
assert len(accepted_context) == 7

authority_paths = [
    "problems/2022-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2022-B4/reviews/reasoning-return-r6-acceptance.json",
]
authority_checks = []
for path in authority_paths:
    doc = read_json(path)
    authority_checks.append({"authority": fp(path), "declared_records_checked": [check(rec) for rec in records(doc)]})
authority_md_scopes = [fp(path) for path in [
    "problems/2022-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2022-B4/reviews/reasoning-return-r6-acceptance.md",
]]

old_ic_manifest_path = "problems/2024-B4/notes/reasoning-components-r1-freeze-v1.json"
old_ic_manifest_fp = check({"path": old_ic_manifest_path, "bytes": 3689, "sha256": "1c2ac7f2322f7e83d62cfbb563c312eca75aa536448e875f849c9b2195ffd5e9"})
old_ic_manifest = read_json(old_ic_manifest_path)
old_ic_checks = [check(rec) for rec in old_ic_manifest["artifacts"]]
old_ic_input = read_json("problems/2024-B4/notes/reasoning-components-r1-input-validation-v1.json")
older_packets = []
for packet in old_ic_input["older_own_packets"]:
    older_packets.append({"manifest": check(packet["manifest"]), "checks": [check(rec) for rec in packet["checks"]]})
assert len(older_packets) == 60
older_packets.append({"manifest": old_ic_manifest_fp, "checks": old_ic_checks})
assert len(older_packets) == 61
gk_addendum = check({"path": "problems/2024-B4/reviews/generalized-Kasami-review-1-telemetry-addendum-v1.json", "bytes": 938, "sha256": "1a4998c93bcc7183680053c105c8fed6181b30205eb0dbfa2ede61a1c2e88632"})
ic_addendum = check({"path": "problems/2024-B4/notes/reasoning-components-r1-authority-hash-only-addendum-v1.json", "bytes": 3673, "sha256": "3aac70a9a54b40f00087007562de109d9325419190e65aecbea9bae76c9b7133"})

ledger = admissible(PREFIX + "issues-v1.md").read_text()
review_ids = sorted(set(re.findall(r"R1-\d{2}", ledger)))
assert review_ids == [f"R1-{i:02d}" for i in range(1, 53)]
constructor_ids = sorted(set(re.findall(r"R7-O\d{2}", ledger)))
assert constructor_ids == [f"R7-O{i:02d}" for i in range(1, 47)]
assert constructor_ids == sorted(set(re.findall(r"R7-O\d{2}", admissible(TARGET_PREFIX + "obligations-v1.md").read_text())))
for suffix in ["initial-v1.md", "issues-v1.md", "source-checks-v1.md"]:
    assert fp(PREFIX + suffix)["bytes"] > 2000

now = datetime.now(timezone.utc).isoformat()
validation = {
    "checked_at_utc": now,
    "metadata_only_not_mathematical_evidence": True,
    "constructor_manifest": target_manifest,
    "complete_ten_artifact_packet": target_checks,
    "constructor_earlier_350_declared_records_preserved": constructor_old_checks,
    "accepted_context_fingerprints_checked": accepted_context,
    "complete_accepted_authority_JSON_declared_records_checked": authority_checks,
    "complete_accepted_MD_scopes_bound": authority_md_scopes,
    "older_own_packets": older_packets,
    "all_sixty_one_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "IC_separate_hash_only_authority_addendum_preserved": ic_addendum,
    "all_forty_six_constructor_obligations_individually_matched": True,
    "whole_review_inference_check_count": 52,
    "review_IDs": review_ids,
    "constructor_obligation_IDs": constructor_ids,
    "complete_initial_blind_to_all_new_peer_R7_records_and_findings": True,
    "old_roles_disclosed": True,
    "new_R7_construction_contribution": False,
    "old_F5_R6_acceptance_not_independent_self_recertification": True,
    "both_ordinary_converses_and_COMPLETE_full_ordinary_fibers_reconstructed": True,
    "substantive_issues": 0,
    "nonblocking_old_explanatory_scope_note": "R7R1-N1; new tenfold at10C qualifies the old F5 warning, preserving formal old results and all old bytes.",
    "mathematical_program_CAS_scan_sampler_or_constructor_rerun": False,
    "Git_shared_old_byte_cache_edit_spawning_charge_contact_or_bypass": False,
    "only_current_assigned_unused_review_prefix_written": True,
    "promotion_no_tenfold_bridge_ordinary_infinite_termination_annual_or_novelty_claim": False,
    "latest_authoritative_weekly_usage": read_json(PREFIX + "sources-v1.json")["latest_authoritative_weekly_usage"],
}
write_new(PREFIX + "input-validation-v1.json", validation)
output = {
    "completed_at_utc": now,
    "status": "COMPLETE initially blind WHOLE R1 frozen; recommendation only",
    "constructor_artifacts_checked": 10,
    "constructor_earlier_declared_records_checked": 350,
    "accepted_authority_record_occurrences_checked": sum(len(a["declared_records_checked"]) for a in authority_checks),
    "older_own_packets_preserved": 61,
    "separate_older_addenda_preserved": 2,
    "whole_review_inference_checks": 52,
    "constructor_obligations_matched": 46,
    "substantive_issues": 0,
    "nonblocking_integration_notes": 1,
    "mathematical_computation_or_author_rerun": False,
    "new_peer_R7_records_or_findings_opened": False,
    "coordinator_reconciliation_of_two_complete_fresh_whole_reports_still_required": True,
}
write_new(PREFIX + "freeze-output-v1.json", output)
artifacts = [fp(PREFIX + suffix) for suffix in [
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json",
    "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json",
]]
review_manifest = {
    "frozen_at_utc": now,
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "status": "COMPLETE initially blind WHOLE nonconstructor R1; scoped recommendation, no promotion",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "verified_effective_settings": None,
    "target_main": target_checks[0],
    "target_manifest": target_manifest,
    "whole_review_inference_checks": 52,
    "constructor_obligations_matched": 46,
    "new_R7_construction_contribution": False,
    "older_authorship_review_roles_disclosed": True,
    "substantive_issues": 0,
    "nonblocking_integration_notes": ["R7R1-N1 old F5 explanatory tenfold qualification at DIFFERENT value10C"],
    "new_peer_R7_records_or_findings_read_before_complete_initial_freeze": False,
    "all_sixty_one_older_own_packets_and_two_addenda_preserved": True,
    "ordinary_infinite_existence_no_tenfold_bridge_termination_annual_or_novelty_claim": False,
    "mathematical_code_CAS_scan_or_author_rerun": False,
    "Git_shared_old_byte_cache_edits_spawning_charge_contact_or_bypass": False,
    "latest_authoritative_weekly_usage": validation["latest_authoritative_weekly_usage"],
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
write_new(PREFIX + "manifest-v1.json", review_manifest)
print(json.dumps({**output, "manifest": fp(PREFIX + "manifest-v1.json"), "artifacts": artifacts}, indent=2))
