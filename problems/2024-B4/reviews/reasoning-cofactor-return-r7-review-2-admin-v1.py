#!/usr/bin/env python3
"""NEW R7 review2 byte/JSON/label preservation ONLY; no mathematical executable."""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = Path("problems/2024-B4/reviews")
PREFIX = "reasoning-cofactor-return-r7-review-2-"
AUTHOR = "problems/2024-B4/notes/reasoning-cofactor-return-r7-"
PARENT = "problems/2019-B4/reviews/reasoning-cut-transfer-r5-review-2-"
EXPECTED = {
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    AUTHOR + "candidate-v1.md": (17331, "f8afed9064dcc6445c3e6bb05102ecb1c1420c3da0ad6bdf9ef7db4f28c4b05e"),
    AUTHOR + "freeze-v1.json": (3129, "18d2a87ffb4f0f7ca2140659a0883f697974620ba507453fdfda01b8cff49cd1"),
    PARENT + "manifest-v1.json": (3646, "d7cf91221d3fab1ae0caf576bed97c1d06f70ccb47b5bd16a77c115d340e9e99"),
    "problems/2024-B4/proofs/reviewed-structural-v1.1.md": (17079, "082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f"),
    "problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md": (20658, "fb988a13187b5765619532ad14077ae2f32a948e04704252e3d8981e10d65d98"),
}
AUTHORITY_STEMS = [
    "structural-acceptance",
    "reasoning-cofactor-return-r6-acceptance",
    "cofactor-dominant-r4-acceptance",
    "cofactor-Frobenius-r5-acceptance",
    "coordinator-three-bit-sector-r2-acceptance",
]
CONTAINERS = [
    AUTHOR + "freeze-v1.json",
    AUTHOR + "baseline-v1.json",
    AUTHOR + "input-validation-v1.json",
    AUTHOR + "metadata-v1.json",
    AUTHOR + "sources-v1.json",
    PARENT + "manifest-v1.json",
    PARENT + "baseline-v1.json",
]
CONTAINERS += ["problems/2024-B4/reviews/" + s + ".json" for s in AUTHORITY_STEMS]


def now():
    return datetime.now(timezone.utc).isoformat()


def own(suffix):
    return str(BASE / (PREFIX + suffix))


def rec(path):
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts, path
    assert "reasoning-cofactor-return-r7-review-1-" not in str(path), "NEW peer prohibited"
    data = (ROOT / p).read_bytes()
    return {"path": str(p), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def load(path):
    return json.loads((ROOT / path).read_text())


def records(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
                and isinstance(value.get("bytes"), int)
                and re.fullmatch(r"[0-9a-f]{64}", str(value.get("sha256", "")))):
            yield {k: value[k] for k in ("path", "bytes", "sha256")}
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)


def validate(row):
    actual = rec(row["path"])
    assert actual == row, {"declared": row, "actual": actual}
    return actual


def write(suffix, value):
    path = ROOT / own(suffix)
    with path.open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def protection_summary():
    rows = []
    for path, (size, digest) in EXPECTED.items():
        actual = rec(path)
        assert (actual["bytes"], actual["sha256"]) == (size, digest), actual
        rows.append(actual)
    for path in CONTAINERS:
        rows.append(rec(path))
        rows.extend(records(load(path)))
    direct = ["problems/2024-B4/statement.md"]
    direct += ["problems/2024-B4/reviews/" + s + ext
               for s in AUTHORITY_STEMS for ext in (".md", ".json")]
    rows += [rec(path) for path in direct]
    author_manifest = load(AUTHOR + "freeze-v1.json")
    assert len(author_manifest["artifacts"]) == 12
    assert author_manifest["whole_obligations"] == 64
    expected_author_paths = {r["path"] for r in author_manifest["artifacts"]}
    actual_author_paths = {str(p.relative_to(ROOT)) for p in (ROOT / "problems/2024-B4/notes").glob("reasoning-cofactor-return-r7-*") if p.is_file()}
    assert actual_author_paths == expected_author_paths | {AUTHOR + "freeze-v1.json"}
    unique = {}
    for row in rows:
        checked = validate(row)
        old = unique.get(checked["path"])
        assert old is None or old == checked
        unique[checked["path"]] = checked
    canonical = sorted(unique.values(), key=lambda row: row["path"])
    digest = hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {
        "protected_occurrences": len(rows),
        "protected_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest,
        "compact_container_bindings": [rec(path) for path in CONTAINERS],
        "direct_input_bindings": [rec(path) for path in EXPECTED] + [rec(path) for path in direct],
        "author_files_including_freeze": 13,
    }


def check_ledger():
    value = (ROOT / own("ledger-v1.md")).read_text()
    ids = re.findall(r"^\| (R7-\d{2}) \| PASS \|", value, flags=re.M)
    assert ids == [f"R7-{j:02d}" for j in range(1, 65)], ids
    return 64


def prepare():
    check_ledger()
    summary = protection_summary()
    write("baseline-v1.json", {
        "created_at_utc": now(), "role": "OTHER initially blind ENTIRE WHOLE R7 review2",
        **summary,
        "compact_recipe": "Validate every path/bytes/SHA row recursively declared in the bound immediate author JSON, immediate own parent manifest/baseline and five current authority JSON containers; bind containers rather than recopy historical inventory. No further unbound-history traversal.",
        "mathematical_reading_is_separately_limited_in_source_MD_JSON": True,
        "no_corresponding_NEW_root_R7_finding_file_hash_metadata_or_user_commentary_access": True,
    })
    write("input-validation-v1.json", {
        "validated_at_utc": now(), "status": "PASS, administrative only",
        "baseline": rec(own("baseline-v1.json")),
        "protected_occurrences": summary["protected_occurrences"],
        "protected_unique_paths": summary["protected_unique_paths"],
        "canonical_deduplicated_sha256": summary["canonical_deduplicated_sha256"],
        "all13_author_artifacts_and64_review_rows": True,
        "no_mathematical_computation_or_old_program_rerun": True,
    })
    write("metadata-v1.json", {
        "created_at_utc": now(), "role": "OTHER initially blind ENTIRE WHOLE review2",
        "reviewer": "/root/review_2021_reasoning_j15_r2",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "root_generic_assignment_no_NEW_inference": True,
        "whole_author_files": 13, "whole_obligations": 64,
        "substantive_defects": 0, "required_repairs": 0, "closed_notes": 9,
        "recommendation_only_not_promotion": True,
        "old_T1_C7_C11_CP_GK_S3_NF_R4_R5_R6_roles_disclosed": True,
        "old_accepted_input_not_fresh_independent_self_recertification": True,
        "no_corresponding_NEW_root_R7_finding_file_hash_metadata_or_user_commentary_access": True,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
        "verified_effective_setting_readback": "unavailable",
        "authoritative_usage_observed_at_utc": "2026-10-18T13:52:58Z",
        "total_used_percent": 40, "weekly_window_minutes": 10080,
        "authorized_weekly_reset": 1792874445, "ordinaryUsageAllowed": True,
        "total_ceiling_percent": 90, "integration_reserve_required": True,
        "no_automatic_later_week_authority": True,
        "FULL_final_ALLfiles_model_readback_then_SEPARATEverify_required_before_handoff": True,
        "findings_embargoed_until_explicit_BOTH_ENTIRE_confirmation": True,
        "mathematical_program_CAS_scan_author_source_or_old_replay": False,
        "Git_shared_old_cache_changes": False,
    })
    print(json.dumps({"prepared_at_utc": now(), "whole_obligations": 64,
                      "protected_occurrences": summary["protected_occurrences"],
                      "protected_unique_paths": summary["protected_unique_paths"]}, indent=2))


def freeze():
    check_ledger()
    summary = protection_summary()
    baseline = load(own("baseline-v1.json"))
    for key in ("protected_occurrences", "protected_unique_paths", "canonical_deduplicated_sha256"):
        assert summary[key] == baseline[key]
    files = sorted(p for p in (ROOT / BASE).glob(PREFIX + "*") if p.is_file())
    assert len(files) == 10, [str(p) for p in files]
    for path in files:
        if path.suffix == ".json":
            json.loads(path.read_text())
    write("manifest-v1.json", {
        "frozen_at_utc": now(), "role": "OTHER initially blind ENTIRE WHOLE R7 review2",
        "whole_obligations": 64, "payload_files": 10, "ENTIRE_files": 11,
        "substantive_defects": 0, "required_repairs": 0, "closed_notes": 9,
        "recommendation_only_not_promotion": True,
        "author_ENTIRE_freeze": rec(AUTHOR + "freeze-v1.json"),
        "immediate_own_parent": rec(PARENT + "manifest-v1.json"),
        "compact_baseline": rec(own("baseline-v1.json")),
        "protected_occurrences": summary["protected_occurrences"],
        "protected_unique_paths": summary["protected_unique_paths"],
        "canonical_deduplicated_sha256": summary["canonical_deduplicated_sha256"],
        "FULL_final_ALLfiles_model_readback_then_SEPARATEverify_required_before_handoff": True,
        "no_corresponding_NEW_root_R7_finding_file_hash_metadata_or_user_commentary_access": True,
        "identity_only_until_explicit_BOTH_ENTIRE_confirmation": True,
        "mathematical_program_CAS_scan_author_source_or_old_replay": False,
        "payloads": [rec(p.relative_to(ROOT)) for p in files],
    })
    print(json.dumps({"freeze": rec(own("manifest-v1.json")),
                      "initial": rec(own("initial-v1.md")), "ENTIRE_files": 11,
                      "whole_obligations": 64}, indent=2))


def verify():
    manifest = load(own("manifest-v1.json"))
    assert len(manifest["payloads"]) == 10
    for row in manifest["payloads"]:
        validate(row)
        if row["path"].endswith(".json"):
            load(row["path"])
    files = {str(p.relative_to(ROOT)) for p in (ROOT / BASE).glob(PREFIX + "*") if p.is_file()}
    assert files == {r["path"] for r in manifest["payloads"]} | {own("manifest-v1.json")}
    check_ledger()
    summary = protection_summary()
    for key in ("protected_occurrences", "protected_unique_paths", "canonical_deduplicated_sha256"):
        assert manifest[key] == summary[key] == load(own("baseline-v1.json"))[key]
    print(json.dumps({"separate_read_only_verify_at_utc": now(), "status": "PASS",
                      "ENTIRE_files": 11, "whole_obligations": 64,
                      "protected_occurrences": summary["protected_occurrences"],
                      "protected_unique_paths": summary["protected_unique_paths"],
                      "manifest": rec(own("manifest-v1.json")),
                      "initial": rec(own("initial-v1.md")),
                      "no_NEW_corresponding_peer_access": True,
                      "no_mathematics_run": True}, indent=2))


if __name__ == "__main__":
    modes = {"prepare": prepare, "freeze": freeze, "verify": verify}
    assert len(sys.argv) == 2 and sys.argv[1] in modes
    modes[sys.argv[1]]()
