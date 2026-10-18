#!/usr/bin/env python3
"""NEW metadata-only preservation tool. No mathematical evaluation or replay."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2019-B4/notes/reasoning-cut-transfer-r5-"
PARENT = "problems/2025-B4/notes/reasoning-diagonal-return-r5-freeze-v1.json"
PARENT_EXPECTED = {
    "path": PARENT,
    "bytes": 8179,
    "sha256": "b81f17c54ed4df58c1d2ee32a8123c6d0e46aa9f8d05d9df23e5aa06d1c6b6c2",
}
AGENTS_SHA = "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"
PAYLOAD_NAMES = [
    "candidate-v1.md", "obligations-v1.md", "issues-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
    "input-validation-v1.json",
]
AUTH_NAMES = [
    "reasoning-cut-transfer-r4",
    "reasoning-critical-return-r2",
    "reasoning-return-r7",
    "reasoning-cut-number-r3",
    "reasoning-growth-return-r1",
]


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def read(path):
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts
    assert path != ".git" and ".git" not in p.parts
    return (ROOT / p).read_bytes()


def obj(path):
    return json.loads(read(path))


def fp(path):
    data = read(path)
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def match(record):
    assert fp(record["path"]) == record, ("fingerprint mismatch", record["path"])


def canonical(records):
    data = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def write_new(path, data):
    assert path.startswith(BASE)
    target = ROOT / path
    with target.open("x", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def labels():
    text = read(BASE + "obligations-v1.md").decode()
    found = re.findall(r"^\| BT-(\d{2}) \|", text, re.MULTILINE)
    assert found == [f"{i:02d}" for i in range(1, 57)], found
    return 56


def bindings_and_paths():
    paths = ["AGENTS.md", "problems/2019-B4/statement.md",
             "problems/2019-B4/references.md"]
    bindings = []
    for name in AUTH_NAMES:
        authority = "problems/2019-B4/reviews/" + name + "-acceptance.json"
        prose = authority[:-5] + ".md"
        a = obj(authority)
        assert a["status"].startswith("proved, independently reviewed")
        assert a["unresolved_substantive_issues"] == 0
        assert a["repair_required"] is False
        match(a["candidate"])
        match(a["accepted_copy"])
        submitted = read(a["candidate"]["path"])
        accepted = read(a["accepted_copy"]["path"])
        assert accepted.endswith(submitted), name
        operative = a["accepted_copy"]
        if name == "reasoning-cut-transfer-r4":
            erratum_json = ("problems/2019-B4/reviews/"
                            "reasoning-cut-transfer-r4-presentation-erratum-v1.json")
            erratum_md = erratum_json[:-5] + ".md"
            e = obj(erratum_json)
            for key in ["old_accepted_copy", "operative_accepted_copy",
                        "unchanged_candidate_suffix", "historical_authority"]:
                match(e[key])
            assert e["old_accepted_copy"] == a["accepted_copy"]
            assert e["unchanged_candidate_suffix"] == a["candidate"]
            new_data = read(e["operative_accepted_copy"]["path"])
            assert accepted.count(b"t0=010") == 1
            assert accepted.replace(b"t0=010", b"t0=10", 1) == new_data
            assert new_data.endswith(submitted)
            operative = e["operative_accepted_copy"]
            paths += [erratum_json, erratum_md, operative["path"]]
        paths += [authority, prose, a["candidate"]["path"],
                  a["accepted_copy"]["path"]]
        bindings.append({
            "authority": fp(authority),
            "accepted_operative_body": operative,
            "unchanged_candidate_suffix": a["candidate"],
            "historical_record_occurrences_bound_not_replayed":
                a["record_occurrences_verified"],
            "historical_unique_paths_bound_not_replayed":
                a["unique_paths_verified"],
        })
    paths += [
        "problems/2019-B4/notes/secondpass-canonical-renewal.md",
        "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
        "problems/2019-B4/reviews/secondpass-acceptance.md",
        "problems/2019-B4/notes/reasoning-cut-transfer-r4-failed-routes-v1.md",
        "problems/2019-B4/notes/reasoning-critical-return-r2-failed-routes-v1.md",
        "problems/2019-B4/notes/coordinator-unmarked-greedy-failure-v1.md",
    ]
    match(PARENT_EXPECTED)
    parent = obj(PARENT)
    assert parent["older_plus_new_own_paths_bound_transitively"] == 760
    assert parent["ENTIRE_files_including_freeze"] == 11
    paths.append(PARENT)
    for record in parent["payloads"]:
        match(record)
        paths.append(record["path"])
    for path in paths:
        assert "problems/2024-B4/reviews/" not in path
        assert not ("/reviews/" in path and "-review-" in Path(path).name)
    assert fp("AGENTS.md")["sha256"] == AGENTS_SHA
    unique = sorted(set(paths))
    records = [fp(path) for path in unique]
    return bindings, paths, records


def prepare():
    assert labels() == 56
    bindings, paths, records = bindings_and_paths()
    baseline = {
        "created_at_utc": utc(),
        "purpose": "compact necessary read-only guards, not mathematical proof",
        "current_guard_occurrences": len(paths),
        "current_guard_unique_paths": len(records),
        "canonical_guard_summary_sha256": canonical(records),
        "records": records,
        "accepted_operative_bindings": bindings,
        "immediate_own_parent": PARENT_EXPECTED,
        "older_own_paths_bound_transitively": 760,
        "no_historical_inventory_recopy_or_recursive_replay": True,
    }
    write_new(BASE + "baseline-v1.json", baseline)
    validation = {
        "validated_at_utc": utc(),
        "status": "PASS necessary fingerprints and current accepted-body suffixes; NOT proof",
        "whole_obligation_labels": 56,
        "accepted_bindings": 5,
        "current_CT_presentation_erratum_checked": True,
        "current_guard_occurrences": len(paths),
        "current_guard_unique_paths": len(records),
        "canonical_guard_summary_sha256": canonical(records),
        "mathematical_program_CAS_scan_test_optimizer_or_replay": False,
        "NEW_peer_review_content_or_metadata_access": False,
    }
    write_new(BASE + "input-validation-v1.json", validation)
    print(json.dumps({"mode": "prepare", "UTC": utc(),
                      "whole_obligations": 56,
                      "guard_occurrences": len(paths), "guard_unique_paths": len(records),
                      "canonical_guard_summary_sha256": canonical(records)}))


def check_baseline():
    baseline = obj(BASE + "baseline-v1.json")
    for record in baseline["records"]:
        match(record)
    assert canonical(baseline["records"]) == baseline["canonical_guard_summary_sha256"]
    bindings, paths, records = bindings_and_paths()
    assert records == baseline["records"]
    assert bindings == baseline["accepted_operative_bindings"]
    assert len(paths) == baseline["current_guard_occurrences"]
    assert labels() == 56
    validation = obj(BASE + "input-validation-v1.json")
    assert validation["canonical_guard_summary_sha256"] == canonical(records)
    return baseline


def freeze():
    baseline = check_baseline()
    payloads = [fp(BASE + suffix) for suffix in PAYLOAD_NAMES]
    source = obj(BASE + "sources-v1.json")
    manifest = {
        "frozen_at_utc": utc(),
        "status": "candidate proof - unverified",
        "claims": ["BT1", "BT2", "BT3", "BT4"],
        "whole_obligations": 56,
        "constructor": "/root/review_2022_complexity_r2",
        "constructor_excluded": True,
        "root_supplied_NEW_mathematical_inference": False,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "ENTIRE_final_payload_code_ALLmetadata_model_readback_required": True,
        "separate_postfreeze_read_only_verify_required": True,
        "only_2019_B4b": True,
        "actual_independent_uniform_input_law_kept_distinct_from_uniform_outputs": True,
        "actual_criticality_regime_value_or_annual_claim": False,
        "unconditional_upper_bound_on_residual_U_proved": False,
        "requested_settings": source["requested_settings"],
        "independent_effective_setting_readback": None,
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "main": payloads[0],
        "compact_necessary_baseline": fp(BASE + "baseline-v1.json"),
        "current_guard_occurrences": baseline["current_guard_occurrences"],
        "current_guard_unique_paths": baseline["current_guard_unique_paths"],
        "canonical_guard_summary_sha256": baseline["canonical_guard_summary_sha256"],
        "accepted_operative_bindings": baseline["accepted_operative_bindings"],
        "immediate_own_parent": PARENT_EXPECTED,
        "older_own_paths_bound_transitively": 760,
        "ENTIRE_files_including_freeze": 11,
        "older_plus_new_own_paths_bound_transitively": 771,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "no_mathematical_program_CAS_scan_test_optimizer_author_source_or_old_freezer_replay": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_upload_bypass": True,
        "no_NEW_active_peer_review_content_or_metadata_used": True,
        "payloads": payloads,
    }
    path = BASE + "freeze-v1.json"
    write_new(path, manifest)
    print(json.dumps({"mode": "freeze", "UTC": utc(), "freeze": fp(path),
                      "main": payloads[0], "ENTIRE_files": 11,
                      "whole_obligations": 56}))


def verify():
    baseline = check_baseline()
    path = BASE + "freeze-v1.json"
    manifest = obj(path)
    assert manifest["status"] == "candidate proof - unverified"
    assert manifest["whole_obligations"] == 56
    assert manifest["ENTIRE_files_including_freeze"] == 11
    for record in manifest["payloads"]:
        match(record)
    match(manifest["compact_necessary_baseline"])
    assert manifest["canonical_guard_summary_sha256"] == canonical(baseline["records"])
    assert manifest["accepted_operative_bindings"] == baseline["accepted_operative_bindings"]
    assert manifest["main"] == manifest["payloads"][0]
    assert len(manifest["payloads"]) == 10
    print(json.dumps({"mode": "verify", "verified_at_utc": utc(),
                      "status": "PASS SEPARATE read-only metadata verification; NOT proof",
                      "ENTIRE_files": 11, "whole_obligations": 56,
                      "guard_unique_paths": len(baseline["records"]),
                      "own_paths_bound_transitively": 771,
                      "freeze": fp(path), "main": manifest["main"]}))


if __name__ == "__main__":
    assert len(sys.argv) == 2
    mode = sys.argv[1]
    assert mode in {"prepare", "freeze", "verify"}
    {"prepare": prepare, "freeze": freeze, "verify": verify}[mode]()
