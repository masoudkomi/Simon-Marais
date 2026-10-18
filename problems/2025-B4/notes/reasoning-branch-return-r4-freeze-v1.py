#!/usr/bin/env python3
"""NEW branch-R4 metadata only. No mathematical test, search or calculation."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/notes/reasoning-branch-return-r4-"
PARENT = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-2-manifest-v1.json"
PARENT_EXPECTED = {
    "path": PARENT, "bytes": 6457,
    "sha256": "b40ab0e94c87ceddb649b63695e07181b4d7a2b9f0cfae5ac1ffaa6ba9db5ca4",
}
FORBIDDEN_READ_PREFIXES = (
    "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-",
    "problems/2020-B4/reviews/reasoning-Todd-return-r12-",
    "problems/2025-B4/reviews/reasoning-branch-return-r4-",
)
AUTHORITY_NAMES = (
    "reasoning-Runge-return-r3", "reasoning-Runge-return-r2",
    "reasoning-return-r6", "reasoning-return-r9", "reasoning-return-r9-runge",
)
OLD_READ_NOTES = (
    "problems/2025-B4/notes/reasoning-Runge-return-r3-failed-routes-v1.md",
    "problems/2025-B4/notes/reasoning-Runge-return-r2-failed-routes-v1.md",
    "problems/2025-B4/notes/reasoning-return-r9-failed-routes-v1.1.md",
    "problems/2025-B4/notes/reasoning-return-r9-runge-failures-worklog-v1.md",
    "problems/2025-B4/notes/reasoning-return-r6-source-audit-v1.md",
    "problems/2025-B4/notes/reasoning-Runge-return-r3-sources-v1.md",
)
PAYLOAD_SUFFIXES = (
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
    "input-validation-v1.json",
)
BASELINE = PREFIX + "baseline-v1.json"
VALIDATION = PREFIX + "input-validation-v1.json"
FREEZE = PREFIX + "freeze-v1.json"


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not any(path.startswith(x) for x in FORBIDDEN_READ_PREFIXES), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fingerprint(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check_record(record):
    assert fingerprint(record["path"]) == record, record["path"]


def canonical_sha(value):
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


def write_exclusive(path, value):
    assert path.startswith(PREFIX)
    assert path in {BASELINE, VALIDATION, FREEZE}
    with (ROOT / path).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def accepted_bindings():
    result = []
    declared = {r["path"]: r for r in obj(PREFIX + "sources-v1.json")[
        "complete_current_accepted_bodies_and_MD_JSON_read"]}
    for name in AUTHORITY_NAMES:
        authority = "problems/2025-B4/reviews/" + name + "-acceptance.json"
        authority_md = authority[:-5] + ".md"
        data = obj(authority)
        assert data["status"].startswith("proved, independently reviewed")
        body, candidate = data["accepted_copy"], data["candidate"]
        check_record(body)
        check_record(candidate)
        assert body["path"] in declared
        assert {k: declared[body["path"]][k] for k in ("path", "bytes", "sha256")} == body
        assert raw(body["path"]).endswith(raw(candidate["path"])), body["path"]
        result.append({
            "authority_json": authority, "authority_md": authority_md,
            "accepted_body": body["path"], "exact_candidate_suffix": candidate["path"],
            "historical_occurrences_bound_not_recopied_or_replayed": data["record_occurrences_verified"],
            "historical_paths_bound_not_recopied_or_replayed": data["unique_paths_verified"],
            "operative": name in AUTHORITY_NAMES[:3],
        })
    return result


def parent_and_paths():
    check_record(PARENT_EXPECTED)
    data = obj(PARENT)
    assert data["older_plus_new_own_paths_bound_transitively"] == 687
    assert len(data["artifacts"]) == 9
    for record in data["artifacts"]:
        assert record["path"].startswith("problems/2024-B4/reviews/cofactor-Frobenius-r5-review-2-")
        check_record(record)
    return data, [PARENT] + [r["path"] for r in data["artifacts"]]


def make_baseline():
    assert not (ROOT / BASELINE).exists()
    assert fingerprint("AGENTS.md") == {
        "path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff",
    }
    bindings = accepted_bindings()
    _, paths = parent_and_paths()
    paths += ["AGENTS.md", "problems/2025-B4/statement.md"] + list(OLD_READ_NOTES)
    for binding in bindings:
        paths += [binding[k] for k in (
            "authority_json", "authority_md", "accepted_body", "exact_candidate_suffix")]
    assert len(paths) == len(set(paths)) == 38
    records = [fingerprint(path) for path in sorted(paths)]
    value = {
        "created_at_utc": now(),
        "purpose": "NEW metadata-only necessary preservation baseline, not a mathematical certificate",
        "snapshot_stage": "after complete hand derivation and initial source reads, before whole immutable freeze",
        "protected_fingerprint_occurrences": len(records),
        "protected_unique_paths": len(records),
        "canonical_protected_summary_sha256": canonical_sha(records),
        "protected_fingerprints": records,
        "accepted_bindings": bindings,
        "immediate_own_parent": PARENT_EXPECTED,
        "older_own_paths_bound_transitively": 687,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "mutable_landscape_context_snapshots_not_immutable_premises": [
            fingerprint("problems/2025-B4/research.md"),
            fingerprint("problems/2025-B4/references.md"),
        ],
        "forbidden_peer_prefixes_never_read_or_hashed_by_this_code": list(FORBIDDEN_READ_PREFIXES),
        "no_math_program_scan_CAS_source_author_or_certificate_rerun": True,
    }
    write_exclusive(BASELINE, value)
    print(json.dumps({"baseline": fingerprint(BASELINE), "protected_paths": len(records)}))


def check_baseline():
    data = obj(BASELINE)
    records = data["protected_fingerprints"]
    assert len(records) == len({r["path"] for r in records}) == 38
    assert canonical_sha(records) == data["canonical_protected_summary_sha256"]
    for record in records:
        check_record(record)
    parent_and_paths()
    assert accepted_bindings() == data["accepted_bindings"]
    return data


def whole_document_labels():
    for suffix in ("obligations-v1.md", "constructor-checks-v1.md"):
        content = raw(PREFIX + suffix).decode()
        labels = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", content)]
        assert labels == list(range(1, 65)), suffix
    main = raw(PREFIX + "candidate-v1.md").decode()
    assert "Candidate proof - unverified" in main
    assert all("**BD" + str(i) + ":" in main for i in range(1, 5))
    source = obj(PREFIX + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert source["TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required"] is True
    assert source["requested_settings"] == {
        "model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}
    assert source["independently_verified_effective_settings"] is None
    telemetry = source["authoritative_weekly_telemetry"]
    assert telemetry["reset_unix"] == 1792874445
    assert telemetry["used_percent_TOTAL"] < telemetry["ceiling_TOTAL_percent"] == 90
    assert telemetry["automatic_later_reset_spending"] is False
    return source


def make_freeze():
    assert not (ROOT / FREEZE).exists()
    assert not (ROOT / VALIDATION).exists()
    baseline = check_baseline()
    source = whole_document_labels()
    for suffix in PAYLOAD_SUFFIXES:
        if suffix != "input-validation-v1.json":
            assert raw(PREFIX + suffix)
    validation = {
        "verified_at_utc": now(),
        "metadata_ONLY_not_proof_or_mathematical_test": True,
        "necessary_protected_paths_unchanged": 38,
        "exact_accepted_bodies_and_candidate_suffixes_checked": 5,
        "historical_inventories_recursively_replayed": False,
        "immediate_own_parent_plus_nine_payloads_unchanged": True,
        "whole_obligations_labels_ordered_1_to_64": True,
        "constructor_dispositions_labels_ordered_1_to_64": True,
        "whole_candidate_BD1_to_BD4_present_UNVERIFIED": True,
        "old_peer_proof_sources_or_mathematical_executables_run": False,
        "entire_generated_metadata_full_readback_and_separate_verify_required_before_handoff": True,
    }
    write_exclusive(VALIDATION, validation)
    artifacts = [fingerprint(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    assert len(artifacts) == 10
    freeze = {
        "frozen_at_utc": now(),
        "status": "candidate proof - unverified",
        "whole_checkpoint": "ENTIRE BD1-BD4 proofs, ALL64 obligations/dispositions, failures/sources/log/code/ALLmetadata",
        "constructor": "/root/review_2022_complexity_r2",
        "constructor_excluded_from_TWO_OTHER_whole_audits": True,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "root_or_other_worker_NEW_proof_inference_contribution": False,
        "older_roles_disclosed_not_fresh_self_recertification": source["older_roles_disclosed"],
        "requested_settings": source["requested_settings"],
        "independently_verified_effective_settings": None,
        "whole_obligations": 64,
        "pure_X_subfamily_claimed_new_discovery": False,
        "unrestricted_prime_bound_all_residual_cofactors_or_annual_answer": False,
        "no_NEW_R5_review1_ToddR12_or_future_branchR4_peer_material_accessed": True,
        "no_math_program_CAS_scan_test_source_author_or_certificate_rerun": True,
        "no_old_shared_Git_cache_edit_spawn_download_charge_contact_or_bypass": True,
        "accepted_operative_binding_authorities": [
            r for r in baseline["accepted_bindings"] if r["operative"]],
        "accepted_context_binding_authorities": [
            r for r in baseline["accepted_bindings"] if not r["operative"]],
        "compact_necessary_baseline": fingerprint(BASELINE),
        "protected_fingerprint_occurrences": 38,
        "protected_unique_paths": 38,
        "canonical_protected_summary_sha256": baseline["canonical_protected_summary_sha256"],
        "immediate_own_parent": PARENT_EXPECTED,
        "older_own_paths_bound_transitively": 687,
        "new_constructor_files_including_freeze": 11,
        "older_plus_new_own_paths_bound_transitively": 698,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "artifacts": artifacts,
    }
    write_exclusive(FREEZE, freeze)
    print(json.dumps({"freeze": fingerprint(FREEZE), "main": artifacts[0], "files": 11}))


def verify():
    baseline = check_baseline()
    whole_document_labels()
    data = obj(FREEZE)
    assert data["status"] == "candidate proof - unverified"
    assert data["whole_obligations"] == 64
    assert data["older_plus_new_own_paths_bound_transitively"] == 698
    assert data["compact_necessary_baseline"] == fingerprint(BASELINE)
    assert data["canonical_protected_summary_sha256"] == baseline["canonical_protected_summary_sha256"]
    assert [r["path"] for r in data["artifacts"]] == [PREFIX + s for s in PAYLOAD_SUFFIXES]
    for record in data["artifacts"]:
        check_record(record)
    print(json.dumps({
        "separate_postfreeze_metadata_verification": "pass",
        "freeze": fingerprint(FREEZE), "main": data["artifacts"][0],
        "new_files": 11, "necessary_protected_paths_unchanged": 38,
        "own_parent_plus_new_paths_bound_transitively": 698,
        "mathematical_certificate_or_independent_review": False,
        "no_peer_material_read_or_hashed": True,
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("baseline", "freeze", "verify"))
    mode = parser.parse_args().mode
    {"baseline": make_baseline, "freeze": make_freeze, "verify": verify}[mode]()
