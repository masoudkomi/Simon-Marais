#!/usr/bin/env python3
"""NEW SQ14 metadata only: no mathematical computation or historical replay."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2020-B4/notes/reasoning-arithmetic-return-r14-"
FORBIDDEN = (
    "problems/2019-B4/reviews/reasoning-cut-transfer-r5-",
    "problems/2017-B4/notes/coordinator-path-moment-r9-",
)
PARENT = {
    "path": "problems/2017-B4/reviews/reasoning-path-mass-return-r8-review-2-manifest-v1.json",
    "bytes": 7544,
    "sha256": "d0323fba2a97322c0caab828da532afb98903dbc656811ff5d9784a4e02ddffd",
}
AUTHORITIES = [
    "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-acceptance.json",
    "problems/2020-B4/reviews/reasoning-Todd-return-r12-acceptance.json",
    "problems/2020-B4/reviews/reasoning-arithmetic-return-r9-acceptance.json",
]
EXPECTED_BODIES = {
    "problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r13-v1.1.md":
        (26335, "4af07d91ba8381672ebdacdd804fe345e9d2921397a5bafe34367735578f062d"),
    "problems/2020-B4/proofs/reviewed-reasoning-Todd-return-r12-v1.1.md":
        (35569, "f1663778cf78c18b3cb30a4702d7fbff95be29ab73c5f8e4f74d344362c8fba6"),
    "problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r9-v1.1.md":
        (24622, "ab2ee4e7a2dcfa464780c6144f996d683f08b7f04da63d2a77ee2fdd4ec922b8"),
}
PAYLOADS = [
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "issues-v1.md", "failed-routes-v1.md", "sources-v1.md",
    "sources-v1.json", "worklog-v1.md", "freeze-v1.py",
    "baseline-v1.json", "input-validation-v1.json",
]


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def read(path):
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts and ".git" not in p.parts
    assert not any(path.startswith(prefix) for prefix in FORBIDDEN)
    return (ROOT / p).read_bytes()


def obj(path):
    return json.loads(read(path))


def fp(path):
    data = read(path)
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def match(rec):
    actual = fp(rec["path"])
    for key in ("bytes", "sha256"):
        assert actual[key] == rec[key], (rec["path"], key)
    return actual


def canonical(records):
    return hashlib.sha256(json.dumps(records, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def write_new(path, data):
    assert path.startswith(BASE)
    with (ROOT / path).open("x", encoding="utf-8") as out:
        json.dump(data, out, indent=2, ensure_ascii=False)
        out.write("\n")


def labels():
    expected = [f"{i:02d}" for i in range(1, 65)]
    for suffix in ("obligations-v1.md", "constructor-checks-v1.md"):
        found = re.findall(r"^\| SQ14-(\d{2}) \|",
                           read(BASE + suffix).decode(), re.MULTILINE)
        assert found == expected, suffix
    source = obj(BASE + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert source["constructor_excluded"] is True
    assert source["OTHER_entire_whole_audits_required"] == 2
    assert source["claims"] == ["SQ14A", "SQ14B", "SQ14C", "SQ14D", "SQ14E"]
    for claim in source["claims"]:
        assert claim in read(BASE + "candidate-v1.md").decode()
    return 64


def inputs():
    match(PARENT)
    parent = obj(PARENT["path"])
    assert parent["ENTIRE_review_files_including_manifest"] == 10
    assert parent["older_plus_new_own_paths_bound_transitively"] == 781
    assert len(parent["payloads"]) == 9
    paths = ["AGENTS.md", "problems/2020-B4/statement.md", PARENT["path"]]
    for record in parent["payloads"]:
        match(record)
        paths.append(record["path"])
    bindings = []
    for path in AUTHORITIES:
        authority = obj(path)
        assert authority["status"].startswith("proved, independently reviewed")
        assert authority["unresolved_substantive_issues"] == 0
        assert authority["repair_required"] is False
        match(authority["candidate"])
        match(authority["accepted_copy"])
        accepted = authority["accepted_copy"]
        assert accepted["path"] in EXPECTED_BODIES
        size, sha = EXPECTED_BODIES[accepted["path"]]
        assert (accepted["bytes"], accepted["sha256"]) == (size, sha)
        assert read(accepted["path"]).endswith(read(authority["candidate"]["path"]))
        paths += [path, path[:-5] + ".md", accepted["path"],
                  authority["candidate"]["path"]]
        bindings.append({
            "authority": fp(path), "accepted_body": accepted,
            "unchanged_candidate_suffix": authority["candidate"],
            "old_metadata_occurrences_bound_not_reexpanded":
                authority["record_occurrences_verified"],
            "old_metadata_unique_paths_bound_not_reexpanded":
                authority["unique_paths_verified"],
        })
    paths += [
        "problems/2020-B4/notes/reasoning-arithmetic-return-r13-sources-v1.md",
        "problems/2020-B4/notes/reasoning-arithmetic-return-r13-failed-routes-v1.md",
        "problems/2020-B4/notes/reasoning-Todd-return-r12-sources-v1.md",
        "problems/2020-B4/notes/reasoning-Todd-return-r12-failed-routes-v1.md",
        "problems/2020-B4/notes/reasoning-arithmetic-return-r9-sources-v1.md",
        "problems/2020-B4/notes/reasoning-arithmetic-return-r9-failed-routes-v1.md",
    ]
    records = [fp(path) for path in sorted(set(paths))]
    assert fp("AGENTS.md")["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"
    assert labels() == 64
    return records, bindings, len(paths)


def prepare():
    records, bindings, occurrences = inputs()
    baseline = {
        "created_at_utc": utc(),
        "status": "necessary compact readonly preservation; NOT mathematical proof",
        "guard_records": records,
        "guard_occurrences": occurrences,
        "guard_unique_paths": len(records),
        "guard_canonical_sha256": canonical(records),
        "accepted_bindings": bindings,
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 781,
        "no_old_historical_inventory_expansion_or_recursive_replay": True,
        "no_NEW_BT_peer_or_PM9_draft_access": True,
        "mutable_research_references_context_only_not_frozen_premises": True,
    }
    write_new(BASE + "baseline-v1.json", baseline)
    validation = {
        "validated_at_utc": utc(),
        "status": "PASS necessary fingerprints/accepted suffixes/ALL64 labels; NOT proof",
        "whole_obligations": 64,
        "constructor_checks": 64,
        "guard_occurrences": occurrences, "guard_unique_paths": len(records),
        "guard_canonical_sha256": canonical(records),
        "old_own_paths_bound_transitively": 781,
        "mathematical_code_CAS_scan_test_or_old_replay": False,
        "NEW_BT_peer_or_PM9_draft_access": False,
    }
    write_new(BASE + "input-validation-v1.json", validation)
    print(json.dumps({"mode": "prepare", "at_utc": utc(), "whole_obligations": 64,
                      "guard_occurrences": occurrences, "guard_unique_paths": len(records),
                      "guard_canonical_sha256": canonical(records)}))


def check():
    baseline = obj(BASE + "baseline-v1.json")
    for record in baseline["guard_records"]:
        match(record)
    records, bindings, occurrences = inputs()
    assert records == baseline["guard_records"]
    assert bindings == baseline["accepted_bindings"]
    assert occurrences == baseline["guard_occurrences"]
    assert canonical(records) == baseline["guard_canonical_sha256"]
    validation = obj(BASE + "input-validation-v1.json")
    assert validation["whole_obligations"] == 64
    assert validation["constructor_checks"] == 64
    assert validation["guard_canonical_sha256"] == baseline["guard_canonical_sha256"]
    return baseline


def freeze():
    baseline = check()
    source = obj(BASE + "sources-v1.json")
    payloads = [fp(BASE + suffix) for suffix in PAYLOADS]
    manifest = {
        "frozen_at_utc": utc(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
        "root_NEW_proof_inference": False,
        "claims": source["claims"], "whole_obligations": 64,
        "constructor_hand_checks": 64,
        "OTHER_initially_blind_ENTIRE_WHOLE_audits_required": 2,
        "independently_reviewed_or_coordinator_promoted": False,
        "requested_settings": source["requested_settings"],
        "independent_effective_readback": None,
        "main": payloads[0],
        "ENTIRE_files_including_freeze": 12,
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 781,
        "older_plus_new_own_paths_bound_transitively": 793,
        "guard_occurrences": baseline["guard_occurrences"],
        "guard_unique_paths": baseline["guard_unique_paths"],
        "guard_canonical_sha256": baseline["guard_canonical_sha256"],
        "accepted_bindings": baseline["accepted_bindings"],
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "FULL_final_model_readback_ALLpayloads_code_generatedmetadata_required": True,
        "FULL_freeze_readback_then_SEPARATE_readonly_verify_required": True,
        "no_mathematical_program_CAS_scan_test_source_author_old_replay": True,
        "no_NEW_BT_peer_or_PM9_draft_access": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass": True,
        "payloads": payloads,
    }
    path = BASE + "freeze-v1.json"
    write_new(path, manifest)
    print(json.dumps({"mode": "freeze", "at_utc": utc(), "ENTIRE_files": 12,
                      "whole_obligations": 64, "main": payloads[0], "freeze": fp(path)}))


def verify():
    baseline = check()
    path = BASE + "freeze-v1.json"
    manifest = obj(path)
    assert manifest["status"] == "candidate proof - unverified"
    assert manifest["whole_obligations"] == 64
    assert manifest["ENTIRE_files_including_freeze"] == 12
    assert len(manifest["payloads"]) == 11
    for record in manifest["payloads"]:
        match(record)
    assert manifest["guard_canonical_sha256"] == baseline["guard_canonical_sha256"]
    print(json.dumps({
        "mode": "verify", "verified_at_utc": utc(),
        "status": "PASS SEPARATE read-only metadata verification; NOT mathematical proof",
        "ENTIRE_files": 12, "whole_obligations": 64,
        "guard_occurrences": baseline["guard_occurrences"],
        "guard_unique_paths": baseline["guard_unique_paths"],
        "own_paths_bound_transitively": 793,
        "main": manifest["main"], "freeze": fp(path),
    }))


if __name__ == "__main__":
    assert len(sys.argv) == 2
    mode = sys.argv[1]
    assert mode in {"prepare", "freeze", "verify"}
    {"prepare": prepare, "freeze": freeze, "verify": verify}[mode]()

