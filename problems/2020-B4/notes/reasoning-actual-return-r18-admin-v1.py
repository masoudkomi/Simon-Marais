#!/usr/bin/env python3
"""NEW R18 documentary preservation only; no mathematical verification.

Never execute/import an old helper, inventorize a peer, compute an ideal,
evaluate a character, or test a mathematical case. Count literal labels,
parse the recorded JSON, and verify exact declared input bytes. Actual
FULL final MODEL payload readback must precede freeze; actual manifest
MODEL readback must precede a separate read-only verify call.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/notes/reasoning-actual-return-r18-"
MAIN = P + "candidate-v1.md"
SRC = P + "sources-v1.json"
BASE = P + "baseline-v1.json"
FREEZE = P + "freeze-v1.json"
PAYLOADS = [MAIN, SRC, P + "admin-v1.py", BASE]
PARENT = "problems/2025-B4/reviews/reasoning-compatible-return-r10-review-2-manifest-v1.json"
PARENT_FIXED = (3003, "bf0fefc985bc7c6d681338114f321f5d6c5a857cd6cd9d8ca751633f5b20ba32")
SPECS = [
    ("problems/2020-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
     29871, "9003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb",
     "problems/2020-B4/reviews/reasoning-return-r8-acceptance"),
    ("problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r14-v1.2.md",
     30567, "0b9f21290c5ecc7833645db76d74ef6def1bbb010bd205b2bc1d3514a6ef7c3f",
     "problems/2020-B4/reviews/reasoning-arithmetic-return-r14-repair-v1.1-acceptance"),
    ("problems/2020-B4/proofs/reviewed-reasoning-class-return-sq15-v1.1.md",
     31963, "7367a7ee4dd98bed7c42acb1974e5cdf30a1d274702335aa0fc8d056b9880bdc",
     "problems/2020-B4/reviews/reasoning-class-return-sq15-acceptance"),
    ("problems/2020-B4/proofs/reviewed-reasoning-class-return-sq16-v1.1.md",
     25788, "019a30f4d50eff19daf28cffa68bd2dc0ccd330eeff15d6d8a43234205fc6692",
     "problems/2020-B4/reviews/reasoning-class-return-sq16-acceptance"),
    ("problems/2020-B4/proofs/reviewed-reasoning-class-return-sq17-v1.1.md",
     24131, "abac8882b345910aa9a91fa04c20ab8e0842d2d56de4f26ae73727570014be59",
     "problems/2020-B4/reviews/reasoning-class-return-sq17-acceptance"),
]
LOCAL = ["AGENTS.md", "problems/2020-B4/statement.md",
         "problems/2020-B4/research.md", "problems/2020-B4/references.md"]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def safe(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert "reasoning-actual-return-r18-review-" not in path
    assert "coordinator-tensor-family-return-r13-" not in path
    assert "coordinator-tensor-return-r13-" not in path
    return ROOT / path


def record(path):
    data = safe(path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    assert record(rec["path"]) == rec, rec["path"]
    return rec


def read_json(path):
    return json.loads(safe(path).read_text())


def summary(records):
    raw = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(records),
            "unique_paths": len({r["path"] for r in records}),
            "canonical_sha256": hashlib.sha256(raw).hexdigest()}


def exclusive_json(path, value):
    assert path.startswith(P)
    with safe(path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def inputs():
    direct = [record(path) for path in LOCAL]
    declared = []
    for path, size, sha, authority in SPECS:
        assert record(path) == {"path": path, "bytes": size, "sha256": sha}
        direct += [record(path), record(authority + ".md"), record(authority + ".json")]
        authority_json = read_json(authority + ".json")
        assert authority_json["accepted_copy"] == record(path)
        candidate = checked(authority_json["candidate"])
        assert safe(path).read_bytes().endswith(safe(candidate["path"]).read_bytes())
        first_meta = authority_json["verification_metadata"][0]
        assert "freeze" in first_meta["path"]
        declared += [candidate, checked(first_meta)]
    size, sha = PARENT_FIXED
    assert record(PARENT) == {"path": PARENT, "bytes": size, "sha256": sha}
    parent = read_json(PARENT)
    assert parent["older_plus_NEW5_own_paths_bound_transitively"] == 995
    parent_records = [checked(r) for r in parent["payload_records"]] + [record(PARENT)]
    assert len(parent_records) == 5
    records = direct + declared + parent_records
    return direct, declared, parent_records, records


def labels():
    text = safe(MAIN).read_text()
    ids = re.findall(r"^\|(AR18-\d\d)\|", text, re.M)
    assert ids == [f"AR18-{i:02d}" for i in range(1, 65)]
    notes = re.findall(r"^\* R18-N(\d+):", text, re.M)
    assert notes == [str(i) for i in range(1, 9)]
    src = read_json(SRC)
    assert src["whole_author_obligations"] == 64
    assert src["NEW_claims"] == ["AR18A", "AR18B", "AR18C", "AR18D", "AR18E"]
    assert src["constructor_excluded"] is True
    assert src["OTHER_initially_blind_ENTIRE_WHOLE_audits_required"] == 2
    assert src["status"] == "candidate proof - unverified"
    for rec in src["fresh_current_inputs"]:
        checked({key: rec[key] for key in ("path", "bytes", "sha256")})
    return {"literal_whole_obligations": 64, "literal_author_scope_notes": 8,
            "claims": 5, "mathematical_truth_checked_by_code": False}


def prepare():
    direct, declared, parent_records, records = inputs()
    value = {
        "prepared_utc": now(), "scope": "NEW documentary preservation only",
        "direct_current_guard_records": direct,
        "direct_authority_candidate_and_freeze_records": declared,
        "own_immediate_parent": record(PARENT),
        "own_parent_ENTIRE5_summary": summary(parent_records),
        "older_own_paths_bound_transitively": 995,
        "older_plus_NEW5_own_paths_bound_transitively": 1000,
        "historical_inventory_recopied_or_old_code_executed": False,
        "all_guard_summary": summary(records), "literal_checks": labels(),
        "fresh_source_read_scopes": "complete main Section7 and sources JSON, never inferred from bytes",
        "no_NEW_peer_review_or_root_NEW_R13_tensor_material_access": True,
        "weekly": {"authority": "root direct telemetry received",
                   "at_utc": "2026-10-18 22:45:30 UTC", "TOTAL_used_percent": 67,
                   "resetsAt": 1792874445, "TOTAL_ceiling": 90,
                   "integration_reserve": True, "automatic_later_window_spending": False}}
    exclusive_json(BASE, value)
    print(json.dumps({"prepared": record(BASE), "guard_summary": summary(records),
                      "literal_checks": value["literal_checks"]}, indent=2))


def freeze(full_model_readback):
    assert full_model_readback, "Actual FULL final MODEL ALL4 payload readback must precede freeze"
    _, _, _, records = inputs()
    baseline = read_json(BASE)
    assert baseline["all_guard_summary"] == summary(records)
    for rec in baseline["direct_current_guard_records"] + baseline["direct_authority_candidate_and_freeze_records"]:
        checked(rec)
    value = {
        "frozen_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
        "root_NEW_mathematical_contribution": False,
        "OTHER_initially_blind_ENTIRE_WHOLE_audits_required": 2,
        "claims": ["AR18A", "AR18B", "AR18C", "AR18D", "AR18E"],
        "whole_obligations": 64, "ENTIRE_files": 5,
        "payload_records": [record(path) for path in PAYLOADS],
        "all_guard_summary": summary(records), "own_immediate_parent": record(PARENT),
        "older_own_paths_bound_transitively": 995,
        "older_plus_NEW5_own_paths_bound_transitively": 1000,
        "literal_checks": labels(),
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "effective_readback": None,
        "FULL_final_MODEL_ALL4_payload_readback_completed": True,
        "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
        "NEW_peer_review_or_root_NEW_R13_tensor_material_accessed": False,
        "mathematical_program_CAS_scan_test_source_author_old_replay": False,
        "Git_shared_old_cache_mutation_spawn_charge_contact_bypass": False,
        "full_annual_new_taut_order_mixed_exclusion_priority_or_promotion_claim": False,
        "weekly": baseline["weekly"]}
    exclusive_json(FREEZE, value)
    print(json.dumps({"frozen": record(FREEZE), "utc": value["frozen_utc"],
                      "ENTIRE_files": 5, "whole_obligations": 64}, indent=2))


def verify():
    value = read_json(FREEZE)
    assert value["ENTIRE_files"] == 5 and value["whole_obligations"] == 64
    assert [r["path"] for r in value["payload_records"]] == PAYLOADS
    for rec in value["payload_records"]:
        checked(rec)
    _, _, _, records = inputs()
    assert value["all_guard_summary"] == summary(records)
    assert value["literal_checks"] == labels()
    for rec in read_json(BASE)["direct_current_guard_records"] + read_json(BASE)["direct_authority_candidate_and_freeze_records"]:
        checked(rec)
    print(json.dumps({"verified_utc": now(), "status": "PASS",
                      "ENTIRE_files": 5, "whole_obligations": 64,
                      "guard_summary": summary(records), "main": record(MAIN),
                      "freeze": record(FREEZE), "read_only": True,
                      "mathematical_program": False}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    parser.add_argument("--full-model-readback", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.full_model_readback)
    else:
        verify()
