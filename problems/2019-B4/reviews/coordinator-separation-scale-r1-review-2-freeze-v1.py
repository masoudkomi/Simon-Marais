"""SS R2 compact documentary freeze; does not run a mathematical program.

Every old input is read-only. Only exclusive new review-prefix outputs
are written. Both new SS peers and still-blind2020R7 peers are blocked.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/coordinator-separation-scale-r1-review-2-"
TARGET = "problems/2019-B4/notes/coordinator-separation-scale-r1-"
BLOCKED = "problems/2019-B4/reviews/coordinator-separation-scale-r1-"
PREVIOUS = "problems/2020-B4/reviews/reasoning-return-r7-review-2-"


def resolve_path(path):
    candidate = ROOT / path
    if not candidate.exists():
        candidate = ROOT / "problems/2019-B4" / path
    absolute = candidate.resolve()
    assert absolute.is_relative_to(ROOT), path
    rel = str(absolute.relative_to(ROOT))
    if rel.startswith(BLOCKED) and not rel.startswith(PREFIX):
        raise RuntimeError("Blind guard: no NEW SS peer reports or metadata")
    if (rel.startswith("problems/2020-B4/reviews/reasoning-return-r7-")
            and not rel.startswith(PREVIOUS)):
        raise RuntimeError("Blind guard: pending2020R7 root/peer initial")
    return rel


def fingerprint(path):
    rel = resolve_path(path)
    body = (ROOT / rel).read_bytes()
    return {"path": rel, "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], expected["path"]
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], expected["path"]
    return actual


def read_json(path):
    return json.loads((ROOT / resolve_path(path)).read_text())


def declarations(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and re.fullmatch("[0-9a-f]{64}", str(obj.get("sha256", "")))):
            yield obj
        for key, child in obj.items():
            if ("/" in key and isinstance(child, str)
                    and re.fullmatch("[0-9a-f]{64}", child)):
                yield {"path": key, "sha256": child}
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
        json.dump(obj, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return fingerprint(path)


for suffix in ["input-validation-v1.json", "manifest-v1.json"]:
    assert not (ROOT / (PREFIX + suffix)).exists()

main = verify({"path": TARGET + "candidate-v1.md", "bytes": 9068,
    "sha256": "d08d778d7bfe2e915b67d85833d4dfb312d78393f0e80aeecdc7859abae5070e"})
constructor_freeze = verify({"path": TARGET + "freeze-v1.json", "bytes": 3809,
    "sha256": "33abb0fd6e571f623f31c9d767be471b95cad1990f39d898700f3568acad732c"})
target = read_json(constructor_freeze["path"])
author_artifacts = [verify(r) for r in target["artifacts"]]
assert len(author_artifacts) == 14
sources = read_json(TARGET + "sources-v1.json")
validation = read_json(TARGET + "input-validation-v1.json")
declared = [verify(r) for obj in [target, sources, validation]
            for r in declarations(obj)]
authority = []
for descriptor in sources["immutable_authority_bindings"]:
    metadata = verify(descriptor["metadata"])
    rows = [verify(r) for r in declarations(read_json(metadata["path"]))]
    assert len(rows) == descriptor["declared_occurrences_verified"]
    declared.extend(rows)
    authority.append({"metadata": metadata,
        "declared_occurrences_verified": len(rows), "deduplicated_summary": digest(rows)})
assert sum(r["declared_occurrences_verified"] for r in authority) == 27
assert (ROOT / "problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md").read_bytes().endswith(
    (ROOT / "problems/2019-B4/notes/coordinator-moment-regular-tail-candidate-v1.md").read_bytes())

# Preserve the complete prior own chain compactly, without carrying
# forward an expanded inventory or re-reading unrelated mathematics.
previous_manifest_record = verify({"path": PREVIOUS + "manifest-v1.json", "bytes": 3221,
    "sha256": "9c9eb4231f2480e6b029551cb33bf14b80b0a9b3a10093edb1cc7644ae40d0df"})
previous = read_json(previous_manifest_record["path"])
previous_artifacts = [verify(r) for r in previous["artifacts"]]
previous_validation_record = next(r for r in previous_artifacts
    if r["path"] == PREVIOUS + "input-validation-v1.json")
previous_validation = read_json(previous_validation_record["path"])
old_R9_manifest_record = verify(previous_validation["reviewer_previous_manifest"])
old_R9_validation_record = verify(previous_validation["reviewer_previous_validation"])
old_R9 = read_json(old_R9_manifest_record["path"])
old_2025_manifest_record = verify(previous_validation["reviewer_prior_2025_manifest"])
old_2025_validation_record = verify(previous_validation["reviewer_prior_2025_validation"])
old_2025 = read_json(old_2025_manifest_record["path"])
ic_manifest_record = verify(previous_validation["reviewer_prior_IC_manifest"])
ic_validation_record = verify(previous_validation["reviewer_prior_IC_validation"])
ic = read_json(ic_manifest_record["path"])
ic_validation = read_json(ic_validation_record["path"])
old_388 = unique([verify(r) for r in
    ic_validation["earlier_unique_records_preserved"]
    + ic["artifacts"] + [ic_manifest_record]
    + old_2025["artifacts"] + [old_2025_manifest_record]
    + old_R9["artifacts"] + [old_R9_manifest_record]])
assert len(old_388) == 388
assert digest(old_388)["canonical_sorted_record_array_sha256"] == previous_validation[
    "earlier_own_summary"]["canonical_sorted_record_array_sha256"]
prior_own = unique(old_388 + previous_artifacts + [previous_manifest_record])
assert len(prior_own) == 394

additional_read_inputs = [fingerprint(p) for p in ["AGENTS.md",
    "problems/2019-B4/statement.md",
    "problems/2019-B4/proofs/candidate-v1.1.md",
    "problems/2019-B4/proofs/repair-v1.1.md"]]
author_ids = re.findall(r"^(\d+)\. ",
    (ROOT / (TARGET + "obligations-v1.md")).read_text(), re.MULTILINE)
review_pairs = re.findall(r"^\|SSR2-(\d\d) / SS-(\d\d)\|",
    (ROOT / (PREFIX + "issues-v1.md")).read_text(), re.MULTILINE)
assert author_ids == [str(i) for i in range(1, 14)]
assert review_pairs == [(f"{i:02}", f"{i:02}") for i in range(1, 14)]

job_record = fingerprint(PREFIX + "sign-job-v1.json")
sign_record = fingerprint(PREFIX + "sign-v1.json")
job = read_json(job_record["path"])
sign = read_json(sign_record["path"])
assert job["child_pid"] == 32567 and job["external_timeout_seconds"] == 10
assert job["reaped"] and job["exit_code"] == 0 and not job["timed_out"]
assert sign["new_sign"] == -1 and sign["old_sign"] == 1
assert sign["union_degree"] == 46 and sign["old_degree"] == 40
assert not sign["constructor_script_executed_or_imported"]
# These checks inspect saved finite-certificate metadata only. Do not
# recompute the mathematical values or rerun either certificate here.

now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 18:41:50UTC", "total_used_percent": 56,
    "window_minutes": 10080, "reset_unix": 1792745187,
    "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
    "review_integration_reserve": True}
integrity = write_new("input-validation-v1.json", {
    "checked_at_utc": now, "administrative_only_not_mathematical_evidence": True,
    "target": main, "constructor_freeze": constructor_freeze,
    "all14_author_artifacts_verified": author_artifacts,
    "declared_fingerprint_occurrences_verified": len(declared),
    "declared_deduplicated_summary": digest(declared),
    "exact_authority_bindings": authority,
    "legacy_path_meaning": "existing repository-relative path, otherwise exact2019 problem-relative path; bytes and SHA retained",
    "accepted_moment_suffix_byte_identical": True,
    "additional_actual_read_inputs": additional_read_inputs,
    "immutable_previous_manifest": previous_manifest_record,
    "immutable_previous_validation": previous_validation_record,
    "immutable_R9_manifest": old_R9_manifest_record,
    "immutable_R9_validation": old_R9_validation_record,
    "immutable_2025_manifest": old_2025_manifest_record,
    "immutable_2025_validation": old_2025_validation_record,
    "immutable_IC_manifest": ic_manifest_record,
    "immutable_IC_validation": ic_validation_record,
    "earlier_own_unique_records_preserved": len(prior_own),
    "earlier_own_summary": digest(prior_own),
    "combined_deduplicated_summary": digest(declared + prior_own + additional_read_inputs),
    "full_historical_inventory_deliberately_not_copied": True,
    "exact_reproduction": "Read recursive path/sha256 and legacy path->sha256 declarations in target/source/validation plus the three exact authority JSON records. Resolve legacy paths as stated. Reconstruct own394 from immutable IC earlier_unique_records_preserved plus IC artifacts/manifest, old2025 artifacts/manifest, oldR9review artifacts/manifest, previous2020R7review artifacts/manifest. Verify read-only, sort/deduplicate by path and apply stated canonical SHA.",
    "whole_author_obligation_IDs": author_ids,
    "independent_inference_IDs": [p[0] for p in review_pairs],
    "whole_SS1_SS2_SS3_reconstructed": True,
    "substantive_issues": 0, "required_author_repairs": 0,
    "optional_editorial_notes": 1,
    "NEW_SS_constructor_or_proof_contributor": False,
    "OLD_2019_authorship_review_roles_disclosed_no_self_recertification": True,
    "new_peer_SS_reports_ledgers_sources_metadata_findings_read_before_complete_initial_freeze": False,
    "mathematical_findings_withheld_until_both_whole_initial_freezes": True,
    "independent_fixed_sign_certificate": sign_record,
    "independent_sign_job": job_record,
    "independent_integer_method_source": fingerprint(PREFIX + "sign-v1.py"),
    "constructor_mathematical_program_or_old_certificate_rerun": False,
    "history_factor_automaton_count_prime_root_or_trial_scan_CAS": False,
    "new_native_PDF_cached_or_hash_fabricated": False,
    "old_shared_Git_cache_edit_spawn_contact_charge_bypass_or_live_native_job": False,
    "source_actual_read_scopes": PREFIX + "source-checks-v1.md",
    "last_direct_weekly_telemetry": telemetry})

artifact_suffixes = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "sign-v1.py", "sign-v1.json", "sign-start-v1.json", "sign-job-v1.json",
    "sign-stdout-v1.txt", "sign-stderr-v1.txt", "freeze-v1.py",
    "input-validation-v1.json"]
artifacts = [fingerprint(PREFIX + suffix) for suffix in artifact_suffixes]
manifest = write_new("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE2019SS R2; exact partial scope; root reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "target": main, "target_manifest": constructor_freeze,
    "author_artifact_count": 14, "whole_author_obligations": 13,
    "independent_inference_rows": 13,
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "optional_editorial_notes": 1,
    "NEW_SS_constructor_or_proof_contributor": False,
    "OLD_2019_roles_disclosed_no_self_recertification": True,
    "whole_minimum_width_first_count_union_and_fixed_sign_reconstructed": True,
    "independent_fixed_integer_sign_child_pid": 32567,
    "external_timeout_seconds": 10, "child_exited0_and_reaped": True,
    "constructor_program_or_old_certificate_rerun": False,
    "all_new_peer_SS_findings_unread_through_complete_initial_freeze": True,
    "withhold_findings_until_both_whole_initial_freezes": True,
    "no_exact_growth_entropy_gap_annual_or_novelty_claim": True,
    "declared_fingerprint_occurrences_verified": len(declared),
    "declared_deduplicated_paths_verified": len(unique(declared)),
    "earlier_own_paths_preserved": len(prior_own),
    "compact_provenance_without_repeated_historical_inventory": True,
    "last_direct_weekly_telemetry": telemetry,
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts})
print(json.dumps({"complete_initial_freeze": True, "manifest": manifest,
    "mathematical_findings_withheld_pending_other_whole_initial_freeze": True}, indent=2))
