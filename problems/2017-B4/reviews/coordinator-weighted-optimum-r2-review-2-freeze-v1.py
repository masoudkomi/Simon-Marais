#!/usr/bin/env python3
"""Independent WO R2 administrative hashes/labels only; no math program."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-review-2-"
PEER = "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-review-1-"
AUTHOR = "problems/2017-B4/notes/coordinator-weighted-optimum-r2-"
TARGET = AUTHOR + "freeze-v1.json"
TARGET_SHA = "e8c60dd823a4e88c0b7d9cd5eb820f13c2791ca69b00317195c806faf51e30ec"
MAIN_SHA = "ca09c36677badac6649775d2ade78a4f5af90fcbdafd0648a6bf8541e835e533"
PARENT = "problems/2019-B4/notes/reasoning-cut-transfer-r4-freeze-v1.json"
PARENT_SHA = "49123da7a3382b51694438f936965a24ce359f5fe4d0d3ea9549e20a037002c9"
WC = "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-acceptance.json"
ROOTS = [TARGET, AUTHOR + "baseline-v1.json", WC, PARENT]
PLAIN = ["AGENTS.md", "problems/2017-B4/statement.md", WC[:-5] + ".md",
         "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-source-audit-v1.md",
         "problems/2017-B4/notes/coordinator-weighted-cutpath-r1-sources-v1.json"]
STATIC = [PRE + s for s in ["initial-v1.md", "ledger-v1.md", "issues-v1.md",
                           "sources-v1.md", "worklog-v1.md", "freeze-v1.py"]]
BASE, META = PRE + "baseline-v1.json", PRE + "metadata-v1.json"
VALID, MANIFEST = PRE + "input-validation-v1.json", PRE + "manifest-v1.json"


def utc():
    return datetime.now(timezone.utc).isoformat()


def raw(p):
    assert not p.startswith(PEER), "NEVER read corresponding NEW peer"
    f = ROOT / p
    assert f.resolve().is_relative_to(ROOT)
    return f.read_bytes()


def obj(p):
    return json.loads(raw(p))


def fp(p):
    b = raw(p)
    return {"path": p, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def write(p, value):
    assert p.startswith(PRE)
    with (ROOT / p).open("x") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def declared(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", value["sha256"])):
            yield {k: value[k] for k in ("path", "bytes", "sha256")}
        for k, v in value.items():
            if k != "mutable_living_context_snapshots_not_immutable_premises":
                yield from declared(v)
    elif isinstance(value, list):
        for v in value:
            yield from declared(v)


def bind():
    t, parent = fp(TARGET), fp(PARENT)
    assert t["bytes"] == 2906 and t["sha256"] == TARGET_SHA
    assert fp(AUTHOR + "candidate-v1.md")["sha256"] == MAIN_SHA
    assert parent["bytes"] == 2732 and parent["sha256"] == PARENT_SHA
    rows = [fp(p) for p in ROOTS + PLAIN]
    count = 0
    for p in ROOTS:
        for r in declared(obj(p)):
            assert fp(r["path"]) == r, ("preservation mismatch", p, r["path"])
            rows.append(r)
            count += 1
    target = obj(TARGET)
    assert target["whole_obligations"] == 48 and len(target["artifacts"]) == 10
    wc = obj(WC)
    assert wc["status"] == "proved, independently reviewed scoped partial result"
    assert not wc["repair_required"] and not wc["unresolved_substantive_issues"]
    assert raw(wc["accepted_copy"]["path"]).endswith(raw(wc["candidate"]["path"]))
    dedup = {}
    for r in rows:
        previous = dedup.setdefault(r["path"], r)
        assert previous == r, ("conflicting row", r["path"])
    return {
        "entrypoint_bindings": [fp(p) for p in ROOTS],
        "standalone_bindings": [fp(p) for p in PLAIN],
        "constructor_entire_files": 11,
        "necessary_direct_declarations_verified": count,
        "necessary_fingerprint_occurrences": len(rows),
        "deduplicated_necessary_paths": len(dedup),
        "WC_current_authority_and_literal_suffix_exact": True,
        "author_living_context_snapshots_not_immutable_guards": True,
        "no_recursive_expansion_of_historical_inventories": True,
        "no_corresponding_NEW_B_WO_file_hash_metadata_access": True,
    }


def labels():
    actual = re.findall(r"^\| (WO-\d{2}) \|", raw(PRE + "ledger-v1.md").decode(), re.M)
    author = re.findall(r"^\|(WO-\d{2})\|", raw(AUTHOR + "obligations-v1.md").decode(), re.M)
    expected = [f"WO-{i:02d}" for i in range(1, 49)]
    assert actual == author == expected
    for p in STATIC:
        assert raw(p)
    return actual


def prepare():
    b = bind()
    write(BASE, {
        "captured_utc": utc(), "administrative_only": True,
        "immediate_own_parent": fp(PARENT), "target_freeze": fp(TARGET),
        "bound_inputs": b,
        "compact_provenance_policy": (
            "Verify necessary direct declared fingerprints; bind immutable metadata roots "
            "by whole-file bytes/SHA instead of recopying nested historical inventory."
        ),
    })
    print(json.dumps({"operation": "prepare", "baseline": fp(BASE),
                      "preserved_paths": b["deduplicated_necessary_paths"]}))


def check_inputs():
    b = obj(BASE)
    actual = bind()
    assert b["bound_inputs"] == actual
    assert b["immediate_own_parent"] == fp(PARENT) and b["target_freeze"] == fp(TARGET)
    return actual


def freeze():
    for p in [META, VALID, MANIFEST]:
        assert not (ROOT / p).exists(), "preserve immutable review"
    b = check_inputs()
    all_labels = labels()
    stamp = utc()
    write(VALID, {
        "verified_utc": stamp, "administrative_only": True,
        "all_48_author_and_independent_ledger_labels_once_in_order": all_labels,
        "constructor_all11_and_necessary_old_inputs_preserved": True,
        "necessary_occurrences": b["necessary_fingerprint_occurrences"],
        "necessary_paths": b["deduplicated_necessary_paths"],
        "accepted_WC_literal_suffix_exact": True,
        "mathematical_code_scan_CAS_optimizer_author_or_old_certificate_run": False,
        "no_NEW_corresponding_peer_access": True,
    })
    write(META, {
        "frozen_utc": stamp, "status": "ENTIRE initially blind OTHER WHOLE WO R2 frozen; not promotion",
        "reviewer": "/root/review_2017_coarsening_r1", "constructor": "/root",
        "reviewer_not_NEW_constructor_or_contributor": True,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
        "effective_readback": "unavailable", "whole_obligations": 48,
        "PASS": 48, "open_substantive_issues": 0, "required_repairs": 0,
        "advisory_changes": 0, "closed_interpretation_notes": 3,
        "entire_review_files_including_manifest": 10,
        "author_entire_files_read": 11, "immediate_own_parent": fp(PARENT),
        "old_roles": "C OLD WC whole R1 reviewer and unrelated earlier2017 inputs; not fresh self-certification",
        "operative_accepted_input": WC,
        "full_primary_source_read_limits_recorded": True,
        "no_new_peer_finding_file_hash_metadata_read_before_ENTIRE_freeze": True,
        "identity_only_handoff_until_explicit_BOTH_entire_confirmation": True,
        "no_math_executable_optimizer_scan_CAS_or_certificate_rerun": True,
        "no_old_shared_cache_or_Git_mutation": True,
        "actual_LC_cost_density_exact_value_or_annual_certified": False,
        "account_total_used_percent_at_transition": 31,
        "authorized_reset_unix": 1792874445, "total_ceiling_percent": 90,
        "integration_reserve_no_automatic_later_window": True,
        "FULL_readback_then_SEPARATE_readonly_postverify_required": True,
    })
    write(MANIFEST, {
        "frozen_utc": stamp, "status": "ENTIRE initially blind OTHER WHOLE WO R2 initial; not promotion",
        "whole_obligations": 48, "review_files_including_manifest": 10,
        "target_main": fp(AUTHOR + "candidate-v1.md"), "target_freeze": fp(TARGET),
        "immediate_own_parent": fp(PARENT),
        "ENTIRE_report_ALL48_issues_sources_log_code_ALLmetadata_frozen": True,
        "no_NEW_corresponding_peer_material_accessed": True,
        "identity_only_until_BOTH_entire_confirmation": True,
        "artifacts": [fp(p) for p in STATIC + [BASE, META, VALID]],
    })
    print(json.dumps({"operation": "freeze", "manifest": fp(MANIFEST),
                      "initial": fp(PRE + "initial-v1.md"),
                      "entire_review_files": 10, "whole_obligations": 48}))


def verify():
    b = check_inputs()
    all_labels = labels()
    m = obj(MANIFEST)
    assert len(m["artifacts"]) == 9 and m["whole_obligations"] == len(all_labels) == 48
    for r in m["artifacts"]:
        assert fp(r["path"]) == r
    expected = set(STATIC + [BASE, META, VALID, MANIFEST])
    found = {str(p.relative_to(ROOT)) for p in (ROOT / "problems/2017-B4/reviews").glob(
        "coordinator-weighted-optimum-r2-review-2-*") if p.is_file()}
    assert found == expected
    print(json.dumps({"operation": "SEPARATE readonly postverify", "verified_utc": utc(),
                      "result": "PASS", "manifest": fp(MANIFEST),
                      "entire_files": len(expected), "all_obligations": len(all_labels),
                      "preserved_paths": b["deduplicated_necessary_paths"],
                      "preserved_occurrences": b["necessary_fingerprint_occurrences"]}))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("operation", choices=["prepare", "freeze", "verify"])
    {"prepare": prepare, "freeze": freeze, "verify": verify}[p.parse_args().operation]()
