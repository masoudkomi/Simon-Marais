"""NEW AR19 documentary administration only; no mathematical computation.

Run from repository root. Modes baseline/freeze write ONLY this unused
R19 prefix. Verify is read-only. No old helper is imported or replayed.
Full model readbacks are human/model acts, not certified by this code.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import re

PREFIX = "problems/2020-B4/notes/reasoning-realization-return-r19-"
MAIN = PREFIX + "candidate-v1.md"
SOURCES = PREFIX + "sources-v1.json"
ADMIN = PREFIX + "admin-v1.py"
BASELINE = PREFIX + "baseline-v1.json"
FREEZE = PREFIX + "freeze-v1.json"
PARENT = "problems/2017-B4/reviews/reasoning-lower-return-r14-review-2-manifest-v1.json"
PAYLOADS = [MAIN, SOURCES, ADMIN, BASELINE]

PINNED = {
    "AGENTS.md": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff",
    PARENT: "f77fddb99a26733be4c81df8cdf89cbbe1550e296f29f2ef80e82e2e15d53889",
    "problems/2020-B4/proofs/reviewed-reasoning-actual-return-r18-v1.1.md": "f38609238baaa9909dfd7655220794a89bf7e00a5f128253d56167507f2d48cf",
    "problems/2020-B4/proofs/reviewed-reasoning-return-r8-v1.1.md": "9003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb",
    "problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r9-v1.1.md": "ab2ee4e7a2dcfa464780c6144f996d683f08b7f04da63d2a77ee2fdd4ec922b8",
    "problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r14-v1.2.md": "0b9f21290c5ecc7833645db76d74ef6def1bbb010bd205b2bc1d3514a6ef7c3f",
    "problems/2020-B4/proofs/reviewed-reasoning-class-return-sq15-v1.1.md": "7367a7ee4dd98bed7c42acb1974e5cdf30a1d274702335aa0fc8d056b9880bdc",
    "problems/2020-B4/proofs/reviewed-reasoning-class-return-sq17-v1.1.md": "abac8882b345910aa9a91fa04c20ab8e0842d2d56de4f26ae73727570014be59",
}


def now():
    return datetime.now(timezone.utc).isoformat()


def record(path):
    data = Path(path).read_bytes()
    result = {"path": path, "bytes": len(data),
              "sha256": hashlib.sha256(data).hexdigest()}
    if path in PINNED:
        assert result["sha256"] == PINNED[path], ("pinned mismatch", path)
    return result


def check_record(expected):
    actual = record(expected["path"])
    assert actual == expected, ("documentary mismatch", expected["path"])


def load(path):
    return json.loads(Path(path).read_text())


def canonical(records):
    unique = {}
    for item in records:
        path = item["path"]
        if path in unique:
            assert unique[path] == item
        unique[path] = item
    ordered = [unique[p] for p in sorted(unique)]
    encoded = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(records), "unique_paths": len(ordered),
            "canonical_deduplicated_sha256": hashlib.sha256(encoded).hexdigest()}


def literal_checks():
    text = Path(MAIN).read_text()
    labels = re.findall(r"^\|AR19-(\d\d)\|", text, re.M)
    assert labels == [f"{i:02}" for i in range(1, 49)], labels
    notes = re.findall(r"^\* R19-N(\d):", text, re.M)
    assert notes == [str(i) for i in range(1, 9)], notes
    assert "Candidate proof - unverified" in text
    assert "TWO OTHER" in text
    assert "even" in text.lower() and "odd" in text.lower()
    load(SOURCES)
    return {"literal_whole_obligations": len(labels), "literal_author_notes": len(notes),
            "mathematical_truth_checked_by_code": False}


def parent_check():
    parent = load(PARENT)
    parent_record = record(PARENT)
    for item in parent["payload_records"]:
        check_record(item)
    assert parent["older_plus_NEW5_own_paths_bound_transitively"] == 1015
    return {"manifest": parent_record,
            "immediate_parent_payload_records_verified": len(parent["payload_records"]),
            "older_own_paths_bound_transitively": 1015,
            "historical_inventory_expanded_or_replayed": False}


def gather():
    sources = load(SOURCES)
    paths = ["AGENTS.md", "problems/2020-B4/statement.md", PARENT]
    authority_summaries = []
    for item in sources["accepted_inputs"]:
        paths += [item["body"], item["authority_md"], item["authority_json"]]
        authority = load(item["authority_json"])
        assert authority["status"] == "proved, independently reviewed scoped partial result"
        assert authority["accepted_copy"]["path"] == item["body"]
        check_record(authority["accepted_copy"])
        authority_summaries.append({
            "authority": record(item["authority_json"]),
            "reported_historical_occurrences": authority["record_occurrences_verified"],
            "reported_historical_unique_paths": authority["unique_paths_verified"],
            "expanded_historical_inventory_rehashed_this_rotation": False,
            "necessary_accepted_body_fingerprint_freshly_verified": True})
    guards = [record(p) for p in paths]
    return {"generated_utc": now(), "kind": "compact documentary input baseline",
            "direct_guard_records": guards, "direct_guard_summary": canonical(guards),
            "immutable_authority_parent_summaries": authority_summaries,
            "own_immediate_parent": parent_check(),
            "mutable_research_map_is_not_an_immutable_guard": True,
            "literal_checks": literal_checks(),
            "mathematical_program_or_old_helper_replay": False}


def write_new(path, obj):
    assert path.startswith(PREFIX), path
    with Path(path).open("x") as stream:
        stream.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def verify_baseline():
    baseline = load(BASELINE)
    for item in baseline["direct_guard_records"]:
        check_record(item)
    assert canonical(baseline["direct_guard_records"]) == baseline["direct_guard_summary"]
    assert parent_check() == baseline["own_immediate_parent"]
    assert literal_checks() == baseline["literal_checks"]
    for item in baseline["immutable_authority_parent_summaries"]:
        check_record(item["authority"])
    return baseline


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["baseline", "freeze", "verify"])
    parser.add_argument("--ack-final-model-readback", action="store_true")
    args = parser.parse_args()
    if args.mode == "baseline":
        baseline = gather()
        write_new(BASELINE, baseline)
        print(json.dumps({"baseline": record(BASELINE),
                          "direct_guards": baseline["direct_guard_summary"],
                          "literal_checks": baseline["literal_checks"]}, indent=2))
        return
    baseline = verify_baseline()
    if args.mode == "freeze":
        assert args.ack_final_model_readback, "Model must FIRST read ALL final payload contents"
        manifest = {
            "frozen_utc": now(), "status": "candidate proof - unverified",
            "role": "B sole NEW AR19 constructor; excluded from TWO OTHER whole audits",
            "ENTIRE_files": 5, "whole_obligations": 48,
            "payload_records": [record(p) for p in PAYLOADS],
            "direct_guard_summary": baseline["direct_guard_summary"],
            "own_immediate_parent": baseline["own_immediate_parent"]["manifest"],
            "older_own_paths_bound_transitively": 1015,
            "older_plus_NEW5_own_paths_bound_transitively": 1020,
            "literal_checks": baseline["literal_checks"],
            "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
            "independent_effective_readback": None,
            "FULL_final_MODEL_ALL4_payload_readback_declared_completed": True,
            "FULL_manifest_MODEL_readback_then_SEPARATE_verify_required": True,
            "NEW_corresponding_CR11_peer_review_access": False,
            "mathematical_program_CAS_scan_test_optimizer_old_replay": False,
            "Git_shared_old_cache_mutation_spawn_charge_contact_bypass": False,
            "annual_priority_or_new_taut_order_claim": False,
            "weekly": {"source": "fresh direct account-wide, legacy/by-limit agree",
                       "at_utc": "2026-10-18 23:41:19 UTC", "TOTAL_used_percent": 71,
                       "resetsAt": 1792874445, "windowDurationMins": 10080,
                       "ordinaryUsageAllowed": True, "account_label": "...ac3a",
                       "TOTAL_ceiling": 90, "integration_reserve": True,
                       "automatic_later_window_spending": False}}
        write_new(FREEZE, manifest)
        print(json.dumps({"freeze": record(FREEZE), "frozen_utc": manifest["frozen_utc"],
                          "payload_records": manifest["payload_records"]}, indent=2))
        return
    manifest = load(FREEZE)
    assert manifest["ENTIRE_files"] == len(PAYLOADS) + 1 == 5
    assert manifest["whole_obligations"] == 48
    assert manifest["literal_checks"] == literal_checks()
    assert manifest["direct_guard_summary"] == baseline["direct_guard_summary"]
    assert [r["path"] for r in manifest["payload_records"]] == PAYLOADS
    for item in manifest["payload_records"]:
        check_record(item)
    print(json.dumps({"SEPARATE_readonly_verify_utc": now(), "result": "PASS",
                      "ENTIRE_files": 5, "whole_obligations": 48,
                      "freeze": record(FREEZE), "payloads_verified": len(PAYLOADS),
                      "direct_old_guards_verified": len(baseline["direct_guard_records"]),
                      "immediate_own_parent_payloads_verified": 4,
                      "mathematical_truth_certified": False}, indent=2))


if __name__ == "__main__":
    main()
