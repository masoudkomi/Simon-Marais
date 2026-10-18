#!/usr/bin/env python3
"""CT administrative integrity only. No mathematics, enumeration or tests."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2019-B4/notes/reasoning-cut-transfer-r4-"
PARENT = "problems/2025-B4/reviews/reasoning-branch-return-r4-review-2-manifest-v1.json"
PARENT_SHA = "64add39dfc128c58113342c1a8005ad3218f3e62572fe923ae67219f498be640"
AUTH = [
    "problems/2019-B4/reviews/reasoning-return-r7-acceptance.json",
    "problems/2019-B4/reviews/reasoning-critical-return-r2-acceptance.json",
    "problems/2019-B4/reviews/reasoning-cut-number-r3-acceptance.json",
]
PLAIN = [
    "AGENTS.md", "problems/2019-B4/statement.md",
    "problems/2019-B4/research.md", "problems/2019-B4/references.md",
] + [p[:-5] + ".md" for p in AUTH]
STATIC = [PRE + s for s in [
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "worklog-v1.md", "freeze-v1.py",
]]
BASE = PRE + "baseline-v1.json"
META = PRE + "metadata-v1.json"
VALID = PRE + "input-validation-v1.json"
FREEZE = PRE + "freeze-v1.json"


def utc():
    return datetime.now(timezone.utc).isoformat()


def data(path):
    p = ROOT / path
    if not p.resolve().is_relative_to(ROOT):
        raise ValueError("outside workspace path: " + path)
    return p.read_bytes()


def fp(path):
    b = data(path)
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def read_json(path):
    return json.loads(data(path))


def write_json(path, obj):
    if not path.startswith(PRE):
        raise ValueError("write outside assigned prefix")
    p = ROOT / path
    if p.exists():
        raise FileExistsError("preserve existing file: " + path)
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def rows(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and isinstance(obj.get("bytes"), int)
                and isinstance(obj.get("sha256"), str)
                and re.fullmatch(r"[0-9a-f]{64}", obj["sha256"])):
            yield {k: obj[k] for k in ("path", "bytes", "sha256")}
        for v in obj.values():
            yield from rows(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from rows(v)


def bind_inputs():
    parent = fp(PARENT)
    assert parent["bytes"] == 2966 and parent["sha256"] == PARENT_SHA
    roots = [fp(p) for p in [PARENT] + AUTH]
    all_rows = list(roots) + [fp(p) for p in PLAIN]
    direct_occurrences = 0
    suffixes = []
    for p in [PARENT] + AUTH:
        for row in rows(read_json(p)):
            assert fp(row["path"]) == row, ("declared fingerprint mismatch", p, row)
            all_rows.append(row)
            direct_occurrences += 1
    for p in AUTH:
        a = read_json(p)
        candidate, accepted = a["candidate"], a["accepted_copy"]
        assert data(accepted["path"]).endswith(data(candidate["path"])), p
        suffixes.append({"authority": p, "candidate": candidate,
                         "accepted_copy": accepted, "literal_suffix_pass": True})
    dedup = {}
    for row in all_rows:
        old = dedup.setdefault(row["path"], row)
        assert old == row, ("conflicting declarations", row["path"])
    return {
        "root_bindings": roots,
        "standalone_inputs": [fp(p) for p in PLAIN],
        "direct_declared_fingerprint_occurrences": direct_occurrences,
        "all_necessary_occurrences_with_root_and_standalone": len(all_rows),
        "deduplicated_necessary_paths": len(dedup),
        "literal_accepted_suffixes": suffixes,
    }


def obligations():
    s = data(PRE + "obligations-v1.md").decode()
    labels = re.findall(r"^\| (CT-\d{2}) \|", s, re.M)
    expected = [f"CT-{i:02d}" for i in range(1, 65)]
    assert labels == expected, ("whole obligation label coverage", labels)
    for title in ("CT1", "CT2", "CT3", "CT4"):
        assert title in data(PRE + "candidate-v1.md").decode()
    for p in STATIC:
        assert len(data(p)) > 0
    return labels


def prepare():
    bound = bind_inputs()
    obj = {
        "created_utc": utc(),
        "purpose": "compact own-parent-bound provenance; administrative integrity only",
        "immediate_own_parent": fp(PARENT),
        "preservation_policy": (
            "Verify direct declared fingerprints at the immutable parent and exact "
            "operative acceptance roots. Bind nested historical metadata by its own "
            "whole-file bytes/SHA; do not expand or duplicate growing historical inventories."
        ),
        "bound_inputs": bound,
        "no_old_shared_cache_Git_mutations": True,
        "no_corresponding_NEW_2017_WO_peer_file_hash_metadata_accessed": True,
    }
    write_json(BASE, obj)
    print(json.dumps({"operation": "prepare", "baseline": fp(BASE),
                      "necessary_paths": bound["deduplicated_necessary_paths"]}))


def check_baseline():
    b = read_json(BASE)
    actual = bind_inputs()
    assert b["bound_inputs"] == actual, "input preservation failed"
    assert b["immediate_own_parent"] == fp(PARENT)
    return actual


def freeze():
    for p in [META, VALID, FREEZE]:
        assert not (ROOT / p).exists(), "immutable checkpoint already exists"
    inputs = check_baseline()
    labels = obligations()
    time = utc()
    write_json(VALID, {
        "checked_utc": time, "administrative_only": True,
        "input_preservation": "PASS", "whole_obligation_labels": labels,
        "necessary_paths": inputs["deduplicated_necessary_paths"],
        "necessary_occurrences": inputs["all_necessary_occurrences_with_root_and_standalone"],
        "direct_declared_occurrences": inputs["direct_declared_fingerprint_occurrences"],
        "literal_accepted_suffixes": inputs["literal_accepted_suffixes"],
        "mathematical_test_scan_CAS_or_certificate_run": False,
        "TWO_OTHER_whole_audits_pending": True,
    })
    write_json(META, {
        "frozen_utc": time, "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
        "effective_setting_readback": "unavailable",
        "official_scope": "2019 B4(b) only",
        "whole_obligations": 64, "entire_packet_file_count": 11,
        "immediate_own_parent": fp(PARENT),
        "compact_baseline": fp(BASE),
        "proof_claims": ["CT1", "CT2", "CT3", "CT4"],
        "old_roles": "CR/CN and other older reviewer roles; not new CT self-certification",
        "root_new_proof_contribution": False,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "selected_renewal_regime_exact_lambda_or_annual_claim": False,
        "mathematical_executable_scan_CAS_or_certificate_run": False,
        "source_reads": {
            "official_PDF_B4b_checked": True,
            "accepted_R7_CR_CN_complete_bodies_current_authorities": True,
            "primary_multivalued_map_Lemma_1_5_entire_proof": True,
            "SAW_model_theorem_imported": False,
            "original_Kesten_full_body_read": False,
            "remote_sources_downloaded_or_local_hash_claimed": False,
        },
        "no_old_shared_cache_or_Git_mutations": True,
        "no_new_corresponding_queued_WO_peer_material_accessed": True,
        "no_pending_operation_approval_or_owned_job": True,
        "last_parent_authoritative_total_weekly_percent": 30,
        "own_transition_authoritative_total_weekly_percent": 31,
        "own_transition_readback_utc": "2026-10-18T11:50:11+00:00",
        "authorized_reset_unix": 1792874445, "total_ceiling_percent": 90,
        "reserve_required": True, "automatic_later_window_authorized": False,
        "full_readback_and_separate_verify_required_after_freeze": True,
    })
    artifacts = [fp(p) for p in STATIC + [BASE, META, VALID]]
    write_json(FREEZE, {
        "frozen_utc": time, "status": "ENTIRE CT constructor packet frozen; candidate-unverified",
        "whole_obligations": 64, "entire_file_count": 11,
        "main": fp(PRE + "candidate-v1.md"),
        "immediate_own_parent": fp(PARENT),
        "TWO_OTHER_whole_audits_pending": True,
        "root_new_mathematical_inference_supplied": False,
        "artifacts": artifacts,
    })
    print(json.dumps({"operation": "freeze", "freeze": fp(FREEZE),
                      "main": fp(PRE + "candidate-v1.md"),
                      "entire_files": 11, "whole_obligations": 64}))


def verify():
    inputs = check_baseline()
    labels = obligations()
    f = read_json(FREEZE)
    assert f["whole_obligations"] == len(labels) == 64
    assert len(f["artifacts"]) == 10
    for row in f["artifacts"]:
        assert fp(row["path"]) == row, ("new checkpoint changed", row["path"])
    expected = set(STATIC + [BASE, META, VALID, FREEZE])
    found = {str(p.relative_to(ROOT)) for p in (ROOT / "problems/2019-B4/notes").glob(
        "reasoning-cut-transfer-r4-*") if p.is_file()}
    assert found == expected, ("unexpected or incomplete assigned packet", found ^ expected)
    print(json.dumps({"operation": "SEPARATE readonly postverify", "checked_utc": utc(),
                      "result": "PASS", "freeze": fp(FREEZE),
                      "entire_files": len(expected), "all_obligations": len(labels),
                      "preserved_necessary_paths": inputs["deduplicated_necessary_paths"],
                      "preserved_occurrences": inputs["all_necessary_occurrences_with_root_and_standalone"]}))


if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("operation", choices=["prepare", "freeze", "verify"])
    op = a.parse_args().operation
    {"prepare": prepare, "freeze": freeze, "verify": verify}[op]()
