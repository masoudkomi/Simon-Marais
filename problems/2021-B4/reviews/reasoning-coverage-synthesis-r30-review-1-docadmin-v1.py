"""NEW documentary-only R30 review administration; no mathematical verifier.

Run from the repository root with prepare, freeze or verify. Standard library
only. This reads exactly selected documentary guards and own output files;
it never imports/runs author or historical code, enumerates mathematics,
opens corresponding peer material, recursively expands a parent, or writes
an existing file. Freeze is allowed only AFTER final MODEL payload readbacks;
verify is a later separate read-only invocation AFTER MODEL manifest readback.
"""
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path.cwd()
PREFIX = "problems/2021-B4/reviews/reasoning-coverage-synthesis-r30-review-1-"
AUTHOR = "problems/2021-B4/notes/reasoning-coverage-synthesis-r30-"
SUFFIXES = ("initial-v1.md", "sources-v1.json", "docadmin-v1.py", "baseline-v1.json")
BASE = ROOT / (PREFIX + "baseline-v1.json")
MANIFEST = ROOT / (PREFIX + "manifest-v1.json")
EXPECTED_AUTHOR = {
    "path": AUTHOR + "freeze-v1.json", "bytes": 2394,
    "sha256": "39ce9a61b63f77c40e3d83d2e229cccf9a10f1e75d5eb35151ec2327fdc05b8a"
}
PARENT = {
    "path": "problems/2021-B4/reviews/coordinator-original-roots-r29-review-1-manifest-v1.json",
    "bytes": 2896,
    "sha256": "104d3eff9f932a4ebaeb04829c863b87904b3f1257cb21662f254e6c0d7ea4f5"
}

def stamp():
    return datetime.now(timezone.utc).isoformat()

def record(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}

def check(expected):
    actual = record(expected["path"])
    assert actual == expected, ("documentary fingerprint mismatch", expected, actual)

def load(path):
    return json.loads((ROOT / path).read_text())

def exclusive(path, value):
    with path.open("x", encoding="utf-8") as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write("\n")

def summary(rows):
    unique = {row["path"]: row for row in rows}
    canonical = [unique[path] for path in sorted(unique)]
    digest = hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"occurrences": len(rows), "unique_paths": len(unique), "canonical_deduplicated_sha256": digest}

mode = sys.argv[1]
if mode == "prepare":
    check(EXPECTED_AUTHOR)
    author = load(EXPECTED_AUTHOR["path"])
    assert author["ENTIRE_files"] == 5 and author["ALL_obligations"] == 12
    author_payloads = author["payloads"]
    for row in author_payloads:
        check(row)
    historical = load(AUTHOR + "baseline-v1.json")
    # The constructor's unrelated own parent is embedded metadata, not our guard.
    necessary = [r for r in historical["guards"] if r["path"] != historical["ONE_OWN_parent_note"]["path"]]
    assert len(necessary) == 35
    for row in necessary:
        check(row)
    check(PARENT)
    all_rows = [EXPECTED_AUTHOR, *author_payloads, *necessary, PARENT]
    assert len(all_rows) == len({r["path"] for r in all_rows}) == 41
    indexed = {r["path"]: r for r in necessary}
    authority_matches = 0
    for row in necessary:
        if row["path"].endswith("-acceptance.json"):
            copy = load(row["path"])["accepted_copy"]
            assert copy == indexed[copy["path"]]
            authority_matches += 1
    assert authority_matches == 11
    source = load(PREFIX + "sources-v1.json")
    assert source["whole_obligations"] == 12
    assert source["NEW_R30_peer_finding_file_actual_inventory_hash_metadata_commentary_access"] is False
    exclusive(BASE, {
        "prepared_UTC": stamp(), "guards": all_rows,
        "guard_summary": summary(all_rows),
        "current_accepted_copy_authorities_match": authority_matches,
        "ONE_compact_OWN_parent": PARENT,
        "guard_policy": "41 necessary unique paths only; no recursion, mutable maps or direct constructor-parent access",
        "documentary_only_not_mathematical_truth_or_read_scope": True,
        "NEW_corresponding_R30_peer_access": False,
        "prospective_R31_access": False
    })
    print(json.dumps({"prepared": str(BASE.relative_to(ROOT)), "guards": summary(all_rows), "accepted_copy_matches": authority_matches, "UTC": stamp()}))
elif mode == "freeze":
    baseline = load(PREFIX + "baseline-v1.json")
    assert baseline["guard_summary"]["unique_paths"] == 41
    report = (ROOT / (PREFIX + "initial-v1.md")).read_text()
    for index in range(1, 13):
        assert f"| R30-O{index:02d} | PASS:" in report
    exclusive(MANIFEST, {
        "frozen_UTC": stamp(),
        "status": "SEALED immutable initially blind OTHER WHOLE1; coordinator pending",
        "reviewer": "/root/review_2021_reasoning_j15_r2",
        "constructor": "C /root/review_2017_coarsening_r1",
        "constructor_excluded": True,
        "NEW_R30_construction_contribution": False,
        "ENTIRE_files": 5, "whole_obligations": 12,
        "payloads": [record(PREFIX + suffix) for suffix in SUFFIXES],
        "guard_summary": baseline["guard_summary"],
        "ONE_compact_OWN_parent": PARENT,
        "all12_independent_application_checks": "PASS",
        "unresolved_substantive_defects": 0,
        "required_author_repairs": 0,
        "closed_scope_notes": 8,
        "FULL_final_ALL4_payload_MODEL_readbacks_completed": True,
        "FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED": True,
        "NEW_R30_peer_finding_file_actual_inventory_hash_metadata_commentary_access": False,
        "prospective_R31_access": False,
        "mathematical_source_author_old_helper_or_certificate_replay": False,
        "NEW_documentary_only_code": True,
        "Git_shared_old_cache_configuration_mutation": False,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_backend_readback": None,
        "quota": {"earlier_preparation_usedPercent": 88, "transition_usedPercent": 89,
            "resetsAt": 1792874445, "TOTAL_ceiling": 90,
            "root_notified_at_89": True, "only_bounded_required_final_documentation": True,
            "reserve_included": True, "automatic_later_window": False}
    })
    print(json.dumps({"manifest": record(str(MANIFEST.relative_to(ROOT))), "UTC": stamp()}))
elif mode == "verify":
    manifest = load(PREFIX + "manifest-v1.json")
    assert manifest["ENTIRE_files"] == 5 and manifest["whole_obligations"] == 12
    for row in manifest["payloads"]:
        check(row)
    baseline = load(PREFIX + "baseline-v1.json")
    for row in baseline["guards"]:
        check(row)
    assert summary(baseline["guards"]) == manifest["guard_summary"]
    assert manifest["NEW_R30_peer_finding_file_actual_inventory_hash_metadata_commentary_access"] is False
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "UTC": stamp(),
        "payloads": 4, "protected_unique_paths": 41,
        "manifest": record(str(MANIFEST.relative_to(ROOT))),
        "mathematical_verification_or_old_replay": False}))
else:
    raise SystemExit("prepare | freeze | verify")
