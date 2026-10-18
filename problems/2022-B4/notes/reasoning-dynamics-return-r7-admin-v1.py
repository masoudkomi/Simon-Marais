#!/usr/bin/env python3
"""D7 administrative bytes/labels/JSON only. No mathematical executable."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2022-B4/notes/reasoning-dynamics-return-r7-"
PARENT = "problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-2-manifest-v1.json"
PARENT_EXPECT = (3068, "d91bb80ed5b7ee9b55e1bf308ac8cac3eff3750897cd4a06291a3d4f9d23c535")
ACCEPTED = [
    ("reasoning-dynamics-return-r6", 25006, "a9f9e12a3c814a4c1098778acaec1bfd13eb631be0837b5550d767715d19b0c8"),
    ("reasoning-fiber-return-r5", 27422, "ab4158f60b3412ace615be689cd61d9384f753319c312e776831392f97a37ef8"),
    ("reasoning-complexity-return-r9-v3", 49080, "18e681d69b29d3495fea0cc2a29dbcb8a9c34db60644b981b3f653d666bef4ad"),
]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith("/") and ".." not in Path(path).parts
    return (ROOT / path).read_bytes()


def fp(path):
    value = raw(path)
    return {"path": path, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def obj(path):
    return json.loads(raw(path))


def check(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(row["path"]) == expected, row["path"]
    return expected


def pinned(path, expected):
    value = fp(path)
    assert (value["bytes"], value["sha256"]) == expected, path
    return value


def put(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "freeze-v1.json")
    with (ROOT / (PRE + suffix)).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def inputs():
    guards = [pinned("AGENTS.md", (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff")), fp("problems/2022-B4/statement.md")]
    bindings = []
    for name, size, digest in ACCEPTED:
        apath = f"problems/2022-B4/reviews/{name}-acceptance.json"
        authority = obj(apath)
        body = check(authority["accepted_copy"])
        assert (body["bytes"], body["sha256"]) == (size, digest)
        candidate = check(authority["candidate"])
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        amd = fp(f"problems/2022-B4/reviews/{name}-acceptance.md")
        ajson = fp(apath)
        guards.extend([body, amd, ajson])
        bindings.append({"accepted_body": body, "authority_md": amd, "authority_json": ajson, "unchanged_candidate_suffix": candidate})
    for name, failure in (("reasoning-dynamics-return-r6", "failures-v1.md"), ("reasoning-fiber-return-r5", "failed-routes-v1.md")):
        for suffix in (failure, "sources-v1.md", "sources-v1.json"):
            guards.append(fp(f"problems/2022-B4/notes/{name}-{suffix}"))
    guards.append(fp("problems/2022-B4/proofs/reviewed-partials-v1.md"))
    assert len(guards) == 18
    parent = pinned(PARENT, PARENT_EXPECT)
    pmeta = obj(PARENT)
    parent_rows = [check(row) for row in pmeta["artifacts"]] + [parent]
    assert len(parent_rows) == 11
    return guards, bindings, parent_rows


def labels():
    expected = [f"{j:02d}" for j in range(1, 49)]
    obligations = re.findall(r"(?m)^\| D7-(\d{2}) \|", raw(PRE + "obligations-v1.md").decode())
    checks = re.findall(r"(?m)^\| D7-(\d{2}) \| CHECKED:", raw(PRE + "constructor-checks-v1.md").decode())
    assert obligations == checks == expected
    issues = re.findall(r"(?m)^\| D7-C(\d) \| CLOSED \|", raw(PRE + "issues-v1.md").decode())
    assert issues == list("12345678")
    source = obj(PRE + "sources-v1.json")
    assert source["whole_obligations"] == 48 and source["constructor_excluded_from_TWO_OTHER_whole_audits"]
    assert not source["queued_NEW_DR6_author_or_peer_accessed"]
    assert not source["ordinary_infinite_avoider_or_universal_hitting_proved"]


def freeze():
    guards, bindings, parent_rows = inputs()
    labels()
    all_rows = guards + parent_rows
    unique = {row["path"]: row for row in all_rows}
    put("baseline-v1.json", {
        "created_at_utc": now(),
        "status": "Compact immutable preservation, not mathematical proof",
        "necessary_old_guard_records": guards,
        "accepted_bindings": bindings,
        "immediate_own_parent_records": parent_rows,
        "fingerprint_occurrences": len(all_rows),
        "unique_paths": len(unique),
        "own_parent_old_guard_occurrences_bound_not_reexpanded": 53,
        "own_parent_old_guard_unique_paths_bound_not_reexpanded": 53,
        "no_recursive_historical_inventory_recopy_or_old_replay": True,
        "queued_NEW_DR6_author_or_peer_accessed": False,
    })
    put("input-validation-v1.json", {
        "validated_at_utc": now(),
        "status": "PASS administrative only",
        "guard18_and_own_parent11_preserved": True,
        "accepted_current_body_candidate_suffixes_unchanged": True,
        "ALL48_obligation_and_hand_check_labels": True,
        "closed_constructor_scope_checks": 8,
        "baseline": fp(PRE + "baseline-v1.json"),
        "mathematical_program_or_old_freezer_executed": False,
    })
    put("metadata-v1.json", {
        "created_at_utc": now(),
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded": True,
        "root_new_inference": False,
        "claims": ["D7A", "D7B", "D7C", "D7D"],
        "whole_obligations": 48,
        "all_files_including_freeze": 13,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "old_CF_SR_constructor_roles_not_self_recertification": True,
        "CF6_existence_used": False,
        "actual_ordinary_universal_hitting_or_infinite_avoider_claim": False,
        "ancestry_event_bound_not_last_clock_bound": True,
        "full_positive_domain_not_strip_orphan_identification": True,
        "queued_NEW_DR6_author_or_peer_accessed": False,
        "FULL_final_ALL13_model_readback_then_SEPARATE_verify_required_after_freeze": True,
        "requested_model": "gpt-6.1-sol",
        "requested_reasoning": "max",
        "effective_readback": None,
        "authorized_weekly_reset": 1792874445,
        "latest_root_context_TOTAL_percent": 40,
        "TOTAL_ceiling_percent": 90,
        "integration_reserve": True,
        "no_auto_later_window": True,
        "mathematical_program_scan_CAS_test_source_author_old_replay": False,
        "Git_shared_old_cache_change_spawn_charge_contact_bypass": False,
    })
    paths = sorted((ROOT / Path(PRE).parent).glob(Path(PRE).name + "*"))
    assert len(paths) == 12, [str(path) for path in paths]
    for path in paths:
        if path.suffix == ".json":
            json.loads(path.read_text())
    put("freeze-v1.json", {
        "frozen_at_utc": now(),
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded": True,
        "root_new_inference": False,
        "whole_obligations": 48,
        "claims": ["D7A", "D7B", "D7C", "D7D"],
        "all_files_including_freeze": 13,
        "immediate_own_parent": fp(PARENT),
        "main": fp(PRE + "candidate-v1.md"),
        "TWO_OTHER_whole_initials_and_coordinator_reconciliation_required": True,
        "FULL_final_ALL13_model_readback_then_SEPARATE_readonly_verify_required": True,
        "payloads": [fp(str(path.relative_to(ROOT))) for path in paths],
    })
    print(json.dumps({"main": fp(PRE + "candidate-v1.md"), "freeze": fp(PRE + "freeze-v1.json"), "ENTIRE_files": 13, "whole_obligations": 48}, indent=2))


def verify():
    inputs()
    labels()
    baseline = obj(PRE + "baseline-v1.json")
    for key in ("necessary_old_guard_records", "immediate_own_parent_records"):
        for row in baseline[key]:
            check(row)
    for binding in baseline["accepted_bindings"]:
        for row in binding.values():
            check(row)
    manifest = obj(PRE + "freeze-v1.json")
    assert len(manifest["payloads"]) == 12
    for row in manifest["payloads"]:
        check(row)
        if row["path"].endswith(".json"):
            obj(row["path"])
    print(json.dumps({"separate_readonly_verify_at_utc": now(), "status": "PASS", "ALL13_and_necessary_inputs_unchanged": True, "ALL48_labels": True, "main": fp(PRE + "candidate-v1.md"), "freeze": fp(PRE + "freeze-v1.json"), "mathematics_executed": False}, indent=2))


if __name__ == "__main__":
    if sys.argv[1:] == ["verify"]:
        verify()
    elif not sys.argv[1:]:
        freeze()
    else:
        raise SystemExit("usage: admin-v1.py [verify]")
