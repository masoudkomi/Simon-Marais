#!/usr/bin/env python3
"""NEW TR12 whole2 documentary byte/JSON/label binding only; no mathematics.
Never execute author/old/source code or inventory corresponding NEW peers.
ACTUAL full final MODEL readback is required before freeze, followed by
ACTUAL manifest MODEL readback and a SEPARATE read-only verification.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/coordinator-tensor-return-r12-review-2-"
A = "problems/2024-B4/notes/coordinator-tensor-return-r12-"
AFID = (1749, "d55148b98cfcf714fc80c88e92942d84181261185c212e7f4331a484025677a0")
AMID = (24907, "4d2195678cc6e029c0657edc21d98387282c2ccc6cbd8b27ff80c2a11f80c05a")
PARENT = "problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-2-manifest-v1.json"
PID = (3092, "c6965259aca4732d67905d0fd1dfc2172864f08aa2aea26bd9a6a24432a7dd52")
AUTH = "problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json"
PAYLOAD = ["initial-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(p):
    assert not p.startswith("problems/2024-B4/reviews/coordinator-tensor-return-r12-review-1-")
    assert not p.startswith("problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-1-")
    t = (ROOT / p).resolve()
    assert t.is_relative_to(ROOT)
    return t.read_bytes()


def obj(p):
    return json.loads(raw(p))


def rec(p):
    b = raw(p)
    return dict(path=p, bytes=len(b), sha256=hashlib.sha256(b).hexdigest())


def match(r):
    assert set(r) == {"path", "bytes", "sha256"}
    assert rec(r["path"]) == r, "Changed immutable document: " + r["path"]
    return r


def fixed(p, identity):
    return match(dict(path=p, bytes=identity[0], sha256=identity[1]))


def declared(x):
    out = []
    if isinstance(x, dict):
        if isinstance(x.get("path"), str) and isinstance(x.get("bytes"), int) and isinstance(x.get("sha256"), str):
            out.append({k: x[k] for k in ("path", "bytes", "sha256")})
        for v in x.values():
            out += declared(v)
    elif isinstance(x, list):
        for v in x:
            out += declared(v)
    return out


def summary(rows):
    u = {}
    for r in rows:
        assert u.setdefault(r["path"], r) == r
    b = json.dumps([u[p] for p in sorted(u)], sort_keys=True, separators=(",", ":")).encode()
    return dict(occurrences=len(rows), unique_paths=len(u), canonical_sha256=hashlib.sha256(b).hexdigest())


def inputs():
    af = fixed(A + "freeze-v1.json", AFID)
    f = obj(af["path"])
    assert f["ENTIRE_files"] == 5 and f["whole_obligations"] == 48
    author = [af] + [match(r) for r in f["payloads"]]
    fixed(A + "candidate-v1.md", AMID)
    assert len(author) == 5
    b = obj(A + "baseline-v1.json")
    direct = [match(r) for r in b["direct_inputs"]]
    match(b["immutable_authority_binding"])
    authority = obj(AUTH)
    old = [match(r) for r in declared(authority)]
    assert summary(old) == b["authority_declared_summary"]
    guard = direct + old
    assert summary(guard) == b["all_guard_summary"] == f["all_guard_summary"]
    abody = match(authority["accepted_copy"])
    assert (abody["bytes"], abody["sha256"]) == (27940, "ce9a3c9e00ce931716fe00d6ea0a605167ddf58a29779d459a62cbc9dd04d173")
    assert raw(abody["path"]).endswith(raw(authority["candidate"]["path"]))
    parent = fixed(PARENT, PID)
    po = obj(PARENT)
    assert po["older_plus_NEW5_own_paths_bound_transitively"] == 985
    own = [parent] + [match(r) for r in po["payload_records"]]
    assert len(own) == 5
    obj(A + "sources-v1.json")
    return author, guard, own


def labels():
    author = raw(A + "candidate-v1.md").decode()
    report = raw(P + "initial-v1.md").decode()
    expect = [f"TR12-O{i:02d}" for i in range(1, 49)]
    assert re.findall(r"^\| (TR12-O\d{2}) \|", author, re.M) == expect
    assert re.findall(r"^\|(TR12-O\d{2})\|PASS[^|]*\|", report, re.M) == expect
    assert re.findall(r"^\|(TR12R2-N\d+)\|CLOSED", report, re.M) == [f"TR12R2-N{i}" for i in range(1, 11)]
    s = obj(P + "sources-v1.json")
    assert s["whole_obligations"] == 48 and s["independent_effective_readback"] is None
    assert s["reviewer_NEW_proof_contribution"] is False
    assert s["corresponding_NEW_TR12_peer_finding_file_actualinventory_hash_metadata_commentary_accessed"] is False
    return dict(author_literal_obligations=48, review_literal_dispositions=48,
                closed_scope_notes=10, mathematical_truth_checked_by_code=False)


def put(suffix, value):
    with (ROOT / (P + suffix)).open("xb") as stream:
        stream.write((json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode())


def prepare():
    author, guard, own = inputs()
    checks = labels()
    put("baseline-v1.json", dict(prepared_utc=now(), author_ENTIRE5=author,
        author_compact_necessary_guard_summary=summary(guard), own_immediate_parent=own[0],
        own_parent_summary=summary(own), all_guard_summary=summary(author + guard + own),
        older_own_paths_bound_transitively=985, older_plus_NEW5_own_paths_bound_transitively=990,
        accepted_FR10_suffix_identical=True, literal_checks=checks,
        corresponding_NEW_peer_access=False, growing_historical_inventory_recopied=False))
    print(json.dumps(dict(action="NEW documentary prepare", PASS=True,
                         summary=summary(author + guard + own), literal_checks=checks)))


def check():
    author, guard, own = inputs()
    b = obj(P + "baseline-v1.json")
    assert author == b["author_ENTIRE5"]
    assert summary(guard) == b["author_compact_necessary_guard_summary"]
    assert own[0] == b["own_immediate_parent"] and summary(own) == b["own_parent_summary"]
    assert summary(author + guard + own) == b["all_guard_summary"]
    assert labels() == b["literal_checks"]
    return b


def freeze(readback):
    assert readback, "ACTUAL FULL final MODEL readback of ALL4 payloads must precede freeze"
    b = check()
    rows = [rec(P + s) for s in PAYLOAD]
    put("manifest-v1.json", dict(frozen_utc=now(), role="OTHER initially blind ENTIRE WHOLE2 TR12A-D",
        reviewer="/root/review_2022_complexity_r2", root_and_C_constructors_excluded=True,
        whole_obligations=48, ENTIRE_files=5, payload_records=rows,
        author_main=fixed(A + "candidate-v1.md", AMID), author_freeze=fixed(A + "freeze-v1.json", AFID),
        all_guard_summary=b["all_guard_summary"], own_immediate_parent=b["own_immediate_parent"],
        older_own_paths_bound_transitively=985, older_plus_NEW5_own_paths_bound_transitively=990,
        literal_checks=b["literal_checks"],
        requested=dict(model="gpt-6.1-sol", reasoning="max", inherited=True), effective_readback=None,
        FULL_final_MODEL_ALL4_payload_readback_completed=True,
        FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required=True,
        corresponding_NEW_peer_access=False, findings_EMBARGO_until_explicit_BOTH_ENTIRE=True,
        mathematical_program_CAS_scan_test_old_replay=False,
        old_shared_Git_cache_mutation=False, weekly=obj(P + "sources-v1.json")["weekly"]))
    print(json.dumps(dict(action="NEW documentary freeze", ENTIRE=5, whole_obligations=48,
                         report=rows[0], manifest=rec(P + "manifest-v1.json"))))


def verify():
    b = check()
    f = obj(P + "manifest-v1.json")
    assert [r["path"] for r in f["payload_records"]] == [P + s for s in PAYLOAD]
    for r in f["payload_records"]:
        match(r)
    assert f["all_guard_summary"] == b["all_guard_summary"]
    print(json.dumps(dict(action="SEPARATE readonly verify", verified_utc=now(), PASS=True,
        ENTIRE=5, whole_obligations=48, report=rec(P + "initial-v1.md"),
        manifest=rec(P + "manifest-v1.json"), all_guard_summary=b["all_guard_summary"],
        mathematical_truth_checked_by_code=False, write_performed=False)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare", "freeze", "verify"])
    parser.add_argument("--full-model-readback", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.full_model_readback)
    else:
        verify()
