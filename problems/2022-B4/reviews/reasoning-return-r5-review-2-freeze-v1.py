"""Administrative hashes/JSON only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/reviews/reasoning-return-r5-review-2-"
AUTHOR = "problems/2022-B4/notes/reasoning-return-r5-"


def record(path):
    location = (ROOT / path).resolve()
    assert location.is_relative_to(ROOT), "Only repository/cache records are checked"
    data = location.read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def checked(expected):
    actual = record(expected["path"])
    for key in ("bytes", "sha256"):
        if key in expected:
            assert actual[key] == expected[key], (expected, actual)
    return actual


def unique_checked(records):
    output = {}
    for expected in records:
        clean = {key: expected[key] for key in ("path", "bytes", "sha256")}
        if clean["path"] in output:
            assert output[clean["path"]] == clean
        else:
            output[clean["path"]] = checked(clean)
    return list(output.values())


def all_records(value):
    rows = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
            and isinstance(value.get("bytes"), int)
            and isinstance(value.get("sha256"), str)
            and re.fullmatch("[0-9a-f]{64}", value["sha256"])):
            rows.append({key: value[key] for key in ("path", "bytes", "sha256")})
        for child in value.values():
            rows.extend(all_records(child))
    elif isinstance(value, list):
        for child in value:
            rows.extend(all_records(child))
    return rows


for suffix in ("input-validation-v1.json", "manifest-v1.json"):
    assert not (ROOT / (PREFIX + suffix)).exists(), "Never overwrite a frozen output"

target_path = AUTHOR + "candidate-v1.md"
checked({"path": target_path, "bytes": 26928,
         "sha256": "f08f3e579f9ddeec52746060ab81aec6055f1ecfce24fa2031608eadb7743bef"})
target_manifest_path = AUTHOR + "freeze-v1.json"
checked({"path": target_manifest_path,
         "sha256": "29a0ba60beda79572326525a2ab5fe20b23f0aff1c4129fc9645a86b83ff4601"})
target_manifest = read_json(target_manifest_path)
assert len(target_manifest["artifacts"]) == 8
assert target_manifest["whole_independent_audit_obligations"] == 42
assert target_manifest["requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits"]
target_records = unique_checked(target_manifest["artifacts"] + [record(target_manifest_path)])
source = read_json(AUTHOR + "sources-v1.json")
declared_sources = unique_checked(
    source["complete_accepted_proof_bodies_read"]
    + [source["unverified_contributing_note_fully_reconstructed_not_accepted_premise"]]
    + [{"path": item["cache_path"], "bytes": item["bytes"], "sha256": item["sha256"]}
       for item in source["primary_sources"] if "cache_path" in item])
author_input_validation = read_json(AUTHOR + "input-validation-v1.json")
author_record_occurrences = all_records(author_input_validation)
author_unique_records = unique_checked(author_record_occurrences)
scope_records = [record(path) for path in (
    "AGENTS.md", "problems/2022-B4/statement.md",
    "problems/2022-B4/reviews/rational-base-shadow-return-acceptance.md",
    "problems/2022-B4/reviews/return-r3-acceptance.md",
    "problems/2022-B4/reviews/arithmetic-complexity-acceptance.md")]
author_rows = (ROOT / (AUTHOR + "obligations-v1.md")).read_text()
review_rows = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert re.findall(r"^\| (R5O\d{2}) \|", author_rows, re.M) == [f"R5O{i:02d}" for i in range(1, 43)]
assert re.findall(r"^\| (R5O\d{2}) \|", review_rows, re.M) == [f"R5O{i:02d}" for i in range(1, 43)]

prior_path = "problems/2025-B4/reviews/original-weight-selection-review-1-manifest-v1.json"
checked({"path": prior_path, "bytes": 3087,
         "sha256": "e0113c0047bab748521bb3bf9423d5a86243000b47ac90d391117b374740ae15"})
prior = read_json(prior_path)
prior_validation = read_json("problems/2025-B4/reviews/original-weight-selection-review-1-input-validation-v1.json")
earlier = unique_checked(prior_validation["earlier_unique_records_preserved"]
                         + prior["artifacts"] + [record(prior_path)])
assert len(earlier) == 280

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now, "administrative_integrity_only": True,
    "all_eight_author_artifacts_plus_freeze": target_records,
    "declared_accepted_bodies_contributing_note_and_caches": declared_sources,
    "author_validation_record_occurrences_checked": len(author_record_occurrences),
    "author_validation_unique_records_checked": author_unique_records,
    "current_protocol_official_and_scope_records": scope_records,
    "all_42_author_and_review_ledger_rows_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "new_R5_nonconstructor": True,
    "old_R4_E1_E2_V1_V4_authorship_disclosed": True,
    "not_independent_self_reaudit_of_old_R4": True,
    "new_R5_peer_findings_read_before_initial_freeze": False,
    "root_carry_note_rederived_not_accepted_as_premise": True,
    "mathematical_program_CAS_scan_table_certificate_or_author_rerun": False,
    "shared_Git_spawning_contact_charge_bypass": False,
    "primary_web_reads": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf",
         "scope": "Exact B4 page2, part(b), no preliminary proof"},
        {"url": "https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf",
         "scope": "Modified division/finite uniqueness and definitions, printedpp7-8; order/evaluation definitions; full Section5.1 Proposition37 and Corollary38 statements/proofs"},
        {"url": "https://arxiv.org/html/2510.11723v2",
         "scope": "Global indexed representation and complete relevant Section3.3 including Conj3.9/Prop3.10/Remark3.11/Question3.12/Prop3.13 and proofs"},
        {"url": "https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers",
         "scope": "Original Section1 proper-set question; Lemma3.1 and Proposition3.1/3.2 statements/proof passages, no external termination theorem import"}],
    "new_native_source_download_or_fictitious_web_binary_hash": False,
}
(ROOT / (PREFIX + "input-validation-v1.json")).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind whole R2; F5A-F5E reconstruct in their exact partial/conditional scopes, no substantive issue found; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "new_R5_constructor": False,
    "old_R4_constructor_disclosed_not_independently_reaudited": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path), "target_manifest": record(target_manifest_path),
    "whole_author_obligations_audited": 42,
    "open_substantive_issues": 0,
    "strict_tail_q_bound_complete_fiber_shape_and_ordinary_iff_reconstructed": True,
    "arbitrary_global_expansion_common_index_and_entire_seed_recovered": True,
    "exact_nine_and_eight_seed_plateau_remain_conditional_on_positive_ordinary_AB_lift": True,
    "real_interval_and_two_prime_Z10_cylinders_distinguished": True,
    "source_singleton_and_conjectural_hypotheses_not_promoted": True,
    "no_ninefold_termination_infinite_ordinary_lift_full_annual_or_novelty_claim": False,
    "new_R5_peer_findings_read_before_initial_freeze": False,
    "mathematical_program_CAS_scan_table_certificate_or_author_rerun": False,
    "all_author_validation_unique_paths_checked": len(author_unique_records),
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 13:11:25 UTC", "total_used_percent": 40,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "author_validation_occurrences_checked": len(author_record_occurrences),
                  "author_validation_unique_paths_checked": len(author_unique_records),
                  "old_own_paths_unchanged": len(earlier),
                  "whole_obligations": 42, "open_substantive_issues": 0}, indent=2))

