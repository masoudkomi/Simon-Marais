#!/usr/bin/env python3
"""R13 whole OTHER R1 byte preservation only; not mathematical evidence."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-review-1-"
AUTHOR = "problems/2020-B4/notes/reasoning-arithmetic-return-r13-"
AUTHOR_MANIFEST = AUTHOR + "freeze-v1.json"
EXPECTED_MANIFEST = {"path": AUTHOR_MANIFEST, "bytes": 6630,
    "sha256": "eba097f9c6bffc2549fef51ef74b99962b16affa86a7dcaf9679bab95ad8adbe"}
NAMES = ("reasoning-Todd-return-r12", "reasoning-arithmetic-return-r9",
         "reasoning-arithmetic-return-r11")
FORBIDDEN = ("problems/2020-B4/reviews/reasoning-arithmetic-return-r13-review-2-",)
PAYLOADS = ("report-v1.md", "ledger-v1.md", "issues-v1.md",
    "source-checks-v1.md", "sources-v1.json", "worklog-v1.md", "freeze-v1.py",
    "baseline-v1.json", "metadata-v1.json", "input-validation-v1.json")

def now():
    return datetime.now(timezone.utc).isoformat()

def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not any(path.startswith(p) for p in FORBIDDEN), path
    return (ROOT / path).read_bytes()

def obj(path):
    return json.loads(raw(path))

def fp(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def check(record):
    wanted = {k: record[k] for k in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == wanted, record["path"]
    return wanted

def put(suffix, value):
    assert suffix in ("baseline-v1.json", "metadata-v1.json",
                      "input-validation-v1.json", "manifest-v1.json")
    with (ROOT / (PREFIX + suffix)).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

def inputs():
    records = [check(EXPECTED_MANIFEST)]
    author = obj(AUTHOR_MANIFEST)
    assert author["whole_obligations"] == 64
    assert len(author["artifacts"]) == 10
    for record in author["artifacts"]:
        assert record["path"].startswith(AUTHOR)
        records.append(check(record))
    bindings = []
    for name in NAMES:
        authority = "problems/2020-B4/reviews/" + name + "-acceptance.json"
        data = obj(authority)
        assert data["status"].startswith("proved, independently reviewed")
        accepted, candidate = data["accepted_copy"], data["candidate"]
        records += [fp(authority), fp(authority[:-5] + ".md"),
                    check(accepted), check(candidate)]
        assert raw(accepted["path"]).endswith(raw(candidate["path"]))
        bindings.append({"name": name, "accepted_body": accepted,
            "candidate_suffix": candidate,
            "historical_occurrences_NOT_replayed": data["record_occurrences_verified"],
            "historical_paths_NOT_replayed": data["unique_paths_verified"],
            "operative": name in NAMES[:2]})
    for name in NAMES:
        records.append(fp("problems/2020-B4/notes/" + name + "-failed-routes-v1.md"))
    records += [fp("AGENTS.md"), fp("problems/2020-B4/statement.md")]
    assert len(records) == len({r["path"] for r in records}) == 28
    return sorted(records, key=lambda r: r["path"]), bindings

def labels():
    content = raw(PREFIX + "ledger-v1.md").decode()
    assert [int(x) for x in re.findall(r"(?m)^(\d+)\. PASS", content)] == list(range(1, 65))
    source = obj(PREFIX + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert source["constructor_excluded"] is True
    assert source["root_NEW_construction_contribution"] is False
    assert source["no_corresponding_NEW_review_2_finding_file_hash_or_metadata_accessed"] is True
    assert all("L13" + letter in raw(PREFIX + "report-v1.md").decode() for letter in "ABCD")

def baseline():
    records, bindings = inputs()
    labels()
    put("baseline-v1.json", {"created_at_utc": now(),
        "purpose": "whole R13 OTHER R1 integrity only, not proof",
        "protected_paths": 28, "fingerprints": records,
        "current_accepted_bindings": bindings,
        "no_historical_recursive_replay_or_mutable_guard_replay": True,
        "corresponding_NEW_peer_prefix_never_opened_or_hashed": list(FORBIDDEN)})
    print(json.dumps({"baseline": fp(PREFIX + "baseline-v1.json"), "protected_paths": 28}))

def preserved():
    data = obj(PREFIX + "baseline-v1.json")
    records, bindings = inputs()
    assert records == data["fingerprints"]
    assert bindings == data["current_accepted_bindings"]
    labels()
    return data

def freeze():
    preserved()
    put("metadata-v1.json", {"created_at_utc": now(),
        "role": "OTHER initially blind ENTIRE whole review1",
        "reviewer": "/root", "constructor": "/root/review_2022_complexity_r2",
        "constructor_excluded": True, "root_NEW_construction_contribution": False,
        "whole_obligations_reconstructed": 64, "substantive_defects": 0,
        "required_mathematical_author_repairs": 0, "closed_scope_notes": 6,
        "no_corresponding_NEW_peer_material_accessed": True,
        "early_user_facing_preliminary_disposition_disclosed": True,
        "second_reviewer_explicit_nonexposure_confirmation_required": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "metadata_only_NOT_proof_or_coordinator_acceptance": True})
    put("input-validation-v1.json", {"verified_at_utc": now(),
        "ENTIRE_author_11_file_hashes_checked": True,
        "current_accepted_body_candidate_suffix_MD_JSON_bindings_checked": 3,
        "necessary_immutable_paths_unchanged": 28,
        "ALL64_ordered_ledger_labels_present": True,
        "no_NEW_peer_read_or_hash": True,
        "no_math_or_old_author_source_freezer_execution": True,
        "FULL_readback_and_SEPARATE_verify_required_before_handoff": True})
    artifacts = [fp(PREFIX + suffix) for suffix in PAYLOADS]
    put("manifest-v1.json", {"frozen_at_utc": now(),
        "whole_checkpoint": "ENTIRE L13A-D audit, ALL64 dispositions/issues/sources/log/code/ALLmetadata",
        "status": "initially blind OTHER whole review, not coordinator acceptance",
        "reviewer": "/root", "constructor_excluded": True,
        "root_NEW_construction_contribution": False,
        "whole_obligations": 64, "substantive_defects": 0,
        "required_mathematical_author_repairs": 0, "closed_scope_notes": 6,
        "no_corresponding_NEW_peer_material_accessed": True,
        "BOTH_entire_initials_required_before_detailed_report_release": True,
        "early_user_facing_preliminary_disposition_disclosed": True,
        "second_reviewer_explicit_nonexposure_confirmation_required": True,
        "protected_paths": 28, "artifacts": artifacts})
    print(json.dumps({"manifest": fp(PREFIX + "manifest-v1.json"), "files": 11,
                      "report": artifacts[0], "whole_obligations": 64}))

def verify():
    preserved()
    data = obj(PREFIX + "manifest-v1.json")
    assert data["whole_obligations"] == 64
    assert [r["path"] for r in data["artifacts"]] == [PREFIX+s for s in PAYLOADS]
    for record in data["artifacts"]:
        check(record)
    print(json.dumps({"separate_postverify": "pass", "files": 11,
        "whole_obligations": 64, "protected_paths": 28,
        "report": data["artifacts"][0], "manifest": fp(PREFIX + "manifest-v1.json"),
        "no_corresponding_NEW_peer_read_or_hash": True}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("baseline", "freeze", "verify"))
    mode = parser.parse_args().mode
    {"baseline": baseline, "freeze": freeze, "verify": verify}[mode]()
