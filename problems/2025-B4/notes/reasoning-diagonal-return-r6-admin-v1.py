#!/usr/bin/env python3
"""DR6 administrative preservation ONLY. No mathematics or old program replay."""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = Path("problems/2025-B4/notes")
PREFIX = "reasoning-diagonal-return-r6-"
PARENT = "problems/2024-B4/reviews/reasoning-cofactor-return-r7-review-2-"
PARENT_EXPECTED = (3604, "23a509ad6334c743929bc13552b43d21d9ea9dd37b2e68c177b8b4d796c319ef")
AUTHORITIES = [
    ("reasoning-diagonal-return-r5-acceptance", "reviewed-reasoning-diagonal-return-r5-v1.1.md", 22518, "4b76934a72989d31a5d836ffd5ff9519e1b84b4a917072a5a65e04494a167499"),
    ("reasoning-branch-return-r4-acceptance", "reviewed-reasoning-branch-return-r4-v1.1.md", 25278, "c5bbac8c0671adc8a3b06b750a46b6b2df732b9d896506870f4c374f0f07843c"),
    ("reasoning-Runge-return-r3-acceptance", "reviewed-reasoning-Runge-return-r3-v1.1.md", 28696, "d27502c014cfd83d56923cea1740daf6d159bee19e15b4b17d18749e16a0ba98"),
    ("reasoning-Runge-return-r2-acceptance", "reviewed-reasoning-Runge-return-r2-v1.1.md", 27717, "33222ffbc2a756fe5f7a9641c248654b0d5626e8283d3d054624b69496c658a3"),
    ("reasoning-return-r6-acceptance", "reviewed-reasoning-return-r6-v1.1.md", 28748, "4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a"),
]
CONTEXTS = [
    "AGENTS.md", "problems/2025-B4/statement.md",
    "problems/2025-B4/notes/reasoning-diagonal-return-r5-failed-routes-v1.md",
    "problems/2025-B4/notes/reasoning-diagonal-return-r5-sources-v1.md",
    "problems/2025-B4/notes/reasoning-branch-return-r4-failed-routes-v1.md",
    "problems/2025-B4/notes/reasoning-Runge-return-r3-failed-routes-v1.md",
    "problems/2025-B4/notes/reasoning-Runge-return-r2-failed-routes-v1.md",
    "problems/2025-B4/notes/coordinator-higher-trace-frontier-r6-v1.md",
    "problems/2025-B4/notes/coordinator-higher-trace-frontier-r6-v1.json",
]
CONTAINERS = [PARENT + "manifest-v1.json", PARENT + "baseline-v1.json"]
CONTAINERS += ["problems/2025-B4/reviews/" + stem + ".json" for stem, _, _, _ in AUTHORITIES]


def now():
    return datetime.now(timezone.utc).isoformat()


def own(suffix):
    return str(BASE / (PREFIX + suffix))


def rec(path):
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts
    data = (ROOT / p).read_bytes()
    return {"path": str(p), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def load(path):
    return json.loads((ROOT / path).read_text())


def records(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
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
    with (ROOT / own(suffix)).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def labels():
    for name in ("obligations-v1.md", "checks-v1.md"):
        ids = re.findall(r"^\| (DR6-\d{2}) \|", (ROOT / own(name)).read_text(), re.M)
        assert ids == [f"DR6-{i:02d}" for i in range(1, 49)], (name, ids)


def inputs():
    parent = rec(PARENT + "manifest-v1.json")
    assert (parent["bytes"], parent["sha256"]) == PARENT_EXPECTED
    rows = [rec(path) for path in CONTEXTS]
    direct = rows.copy()
    authority_checks = []
    for stem, name, size, digest in AUTHORITIES:
        body = rec("problems/2025-B4/proofs/" + name)
        assert (body["bytes"], body["sha256"]) == (size, digest), body
        js = "problems/2025-B4/reviews/" + stem + ".json"
        md = "problems/2025-B4/reviews/" + stem + ".md"
        declared = [r for r in records(load(js)) if r["path"] == body["path"]]
        assert declared and all(validate(r) == body for r in declared)
        direct += [body, rec(md), rec(js)]
        rows += [body, rec(md), rec(js)]
        authority_checks.append({"authority": js, "accepted_body": body, "matched_declared_occurrences": len(declared)})
    for path in CONTAINERS:
        rows.append(rec(path))
        rows.extend(records(load(path)))
    unique = {}
    for row in rows:
        checked = validate(row)
        assert checked["path"] not in unique or unique[checked["path"]] == checked
        unique[checked["path"]] = checked
    canonical = sorted(unique.values(), key=lambda row: row["path"])
    return {
        "direct_frozen_input_bindings": direct,
        "compact_immutable_parent_container_bindings": [rec(path) for path in CONTAINERS],
        "authority_body_matches": authority_checks,
        "protected_occurrences": len(rows), "protected_unique_paths": len(unique),
        "canonical_deduplicated_sha256": hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
        "recipe": "Validate every standard path/bytes/SHA record recursively inside the bound immediate container JSON; bind containers rather than recopy historical inventory. No further historical recursive traversal or old executable replay.",
    }


def prepare():
    labels()
    summary = inputs()
    observations = []
    for path in ("problems/2025-B4/research.md", "problems/2025-B4/references.md"):
        row = rec(path)
        observations.append({"path": path, "observed_at_utc": now(), "observed_bytes": row["bytes"], "observed_sha256": row["sha256"], "coordinator_owned_mutable_context_NOT_frozen_proof_input": True})
    write("baseline-v1.json", {"created_at_utc": now(), "status": "candidate proof - unverified", **summary,
          "coordinator_mutable_status_observations_not_frozen_expectations": observations,
          "only_old_non_elementary_consequence": "accepted RD3 in exact actual signed domain",
          "compact_parent_is_preservation_not_mathematical_premise": True})
    write("input-validation-v1.json", {"validated_at_utc": now(), "status": "PASS administrative only",
          "baseline": rec(own("baseline-v1.json")), "whole_obligations_and_checks": [48, 48],
          "accepted_authority_body_matches": 5,
          "protected_occurrences": summary["protected_occurrences"], "protected_unique_paths": summary["protected_unique_paths"],
          "canonical_deduplicated_sha256": summary["canonical_deduplicated_sha256"],
          "no_mathematical_program_source_author_or_old_replay": True})
    write("metadata-v1.json", {"created_at_utc": now(), "status": "candidate proof - unverified",
          "constructor": "/root/review_2021_reasoning_j15_r2", "constructor_excluded": True,
          "root_generic_target_only_no_NEW_proof_inference": True,
          "claims": ["DR6A", "DR6B", "DR6C", "DR6D"], "whole_obligations": 48,
          "TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required": True,
          "actual_signed_prime_diagonal_p_min": 37, "official_degree": "p-1",
          "only_old_non_elementary_import_RD3_exact_scope": True,
          "old_A_review_roles_not_independent_self_recertification": True,
          "root_higher_trace_note_UNVERIFIED_formal_context_only": True,
          "Chen_Mihailescu_distinct_prime_theorem_diagonal_import": False,
          "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "verified_effective_readback": "unavailable",
          "authoritative_usage_observed_at_utc": "2026-10-18T14:09:55Z", "total_used_percent": 41,
          "weekly_window_minutes": 10080, "authorized_weekly_reset": 1792874445,
          "ordinaryUsageAllowed": True, "total_ceiling_percent": 90, "integration_reserve_required": True,
          "automatic_later_window_spending": False,
          "mathematical_program_CAS_scan_numerical_log_source_author_old_replay": False,
          "native_child_PID_or_pending_permission": None,
          "Git_shared_old_or_cache_mutation": False,
          "annual_unbounded_prime_uniform_cofactor_or_priority_claim": False,
          "FULL_final_ALLfiles_readback_then_SEPARATEverify_required_before_handoff": True})
    print(json.dumps({"prepared_at_utc": now(), "whole_obligations": 48,
                      "protected_occurrences": summary["protected_occurrences"], "protected_unique_paths": summary["protected_unique_paths"]}, indent=2))


def freeze():
    labels()
    summary, baseline = inputs(), load(own("baseline-v1.json"))
    for key in ("protected_occurrences", "protected_unique_paths", "canonical_deduplicated_sha256"):
        assert summary[key] == baseline[key]
    files = sorted(p for p in (ROOT / BASE).glob(PREFIX + "*") if p.is_file())
    assert len(files) == 12, [str(p) for p in files]
    for p in files:
        if p.suffix == ".json":
            json.loads(p.read_text())
    write("freeze-v1.json", {"frozen_at_utc": now(), "status": "candidate proof - unverified",
          "constructor": "/root/review_2021_reasoning_j15_r2", "constructor_excluded": True,
          "claims": ["DR6A", "DR6B", "DR6C", "DR6D"], "whole_obligations": 48,
          "payload_files": 12, "ENTIRE_files": 13,
          "TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required": True,
          "immediate_own_parent": rec(PARENT + "manifest-v1.json"), "compact_baseline": rec(own("baseline-v1.json")),
          "protected_occurrences": summary["protected_occurrences"], "protected_unique_paths": summary["protected_unique_paths"],
          "canonical_deduplicated_sha256": summary["canonical_deduplicated_sha256"],
          "FULL_final_ALLfiles_model_readback_then_SEPARATE_readonly_verify_REQUIRED_before_handoff": True,
          "no_math_executable_scan_CAS_source_author_or_old_replay": True,
          "artifacts": [rec(p.relative_to(ROOT)) for p in files]})
    print(json.dumps({"freeze": rec(own("freeze-v1.json")), "main": rec(own("candidate-v1.md")),
                      "ENTIRE_files": 13, "whole_obligations": 48}, indent=2))


def verify():
    manifest = load(own("freeze-v1.json"))
    assert len(manifest["artifacts"]) == 12
    for row in manifest["artifacts"]:
        validate(row)
        if row["path"].endswith(".json"):
            load(row["path"])
    files = {str(p.relative_to(ROOT)) for p in (ROOT / BASE).glob(PREFIX + "*") if p.is_file()}
    assert files == {r["path"] for r in manifest["artifacts"]} | {own("freeze-v1.json")}
    labels()
    summary = inputs()
    for key in ("protected_occurrences", "protected_unique_paths", "canonical_deduplicated_sha256"):
        assert summary[key] == manifest[key] == load(own("baseline-v1.json"))[key]
    print(json.dumps({"separate_read_only_verify_at_utc": now(), "status": "PASS", "ENTIRE_files": 13,
                      "whole_obligations": 48, "protected_occurrences": summary["protected_occurrences"],
                      "protected_unique_paths": summary["protected_unique_paths"],
                      "freeze": rec(own("freeze-v1.json")), "main": rec(own("candidate-v1.md")),
                      "no_mathematical_computation_or_old_byte_change": True}, indent=2))


if __name__ == "__main__":
    modes = {"prepare": prepare, "freeze": freeze, "verify": verify}
    assert len(sys.argv) == 2 and sys.argv[1] in modes
    modes[sys.argv[1]]()
