"""Administrative-only Runge R2 freeze. No mathematical computation or rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-return-r9-runge-review-2-"
TARGET = "problems/2025-B4/notes/reasoning-return-r9-runge-"
rows = []


def data(path):
    assert not Path(path).name.startswith("reasoning-return-r9-runge-review-1-")
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
    return (ROOT / path).read_bytes()


def fingerprint(path):
    value = data(path)
    return {"path": path, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def bind(path, origin, expected=None):
    actual = fingerprint(path)
    if expected is not None:
        assert actual == {k: expected[k] for k in ("path", "bytes", "sha256")}, (origin, path)
    rows.append({"origin": origin, **actual})
    return actual


def expected(path, size, sha):
    return {"path": path, "bytes": size, "sha256": sha}


def exclusive(suffix, value):
    path = ROOT / (PREFIX + suffix)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return fingerprint(PREFIX + suffix)


constructor_path = TARGET + "freeze-v1.json"
bind(constructor_path, "exact assigned constructor freeze", expected(
    constructor_path, 2364,
    "cb5073bbce53c07b12e5b253af51f278ebd6475c0600d700bef6a9064a7ec32b"))
constructor = json.loads(data(constructor_path))
assert constructor["whole_obligations"] == 34 and len(constructor["artifacts"]) == 8
for item in constructor["artifacts"]:
    bind(item["path"], "constructor frozen payload", item)
assert fingerprint(TARGET + "candidate-v1.md") == expected(
    TARGET + "candidate-v1.md", 16773,
    "8bcd69dfa97441b23fd456268e655312aea55a0f7a64a5237f0117f6a192b90a")

baseline = json.loads(data(TARGET + "baseline-v1.json"))
assert len(baseline["records"]) == 13
for item in baseline["records"]:
    bind(item["path"], "constructor compact parent/current authority declaration", item)

bind("AGENTS.md", "current protocol", expected(
    "AGENTS.md", 4707,
    "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"))
bind("problems/2025-B4/statement.md", "current official-domain normalization read")
for number in ("6", "8"):
    proof = "problems/2025-B4/proofs/reviewed-reasoning-return-r" + number + "-v1.1.md"
    acceptance = "problems/2025-B4/reviews/reasoning-return-r" + number + "-acceptance"
    bind(proof, "complete accepted body read")
    bind(acceptance + ".md", "complete old acceptance scope read")
    bind(acceptance + ".json", "old authority compact metadata")
    authority = json.loads(data(acceptance + ".json"))
    for key in ("candidate", "accepted_copy"):
        bind(authority[key]["path"], "old authority current " + key + " declaration", authority[key])

parent_path = "problems/2021-B4/notes/reasoning-return-r12-freeze-v1.json"
bind(parent_path, "immediate own immutable constructor parent, NOT premise", expected(
    parent_path, 4087,
    "3ed49540ef24d6b947add1abc2db155f6c3bda82c8e2a40c7615547aa3351f02"))
parent = json.loads(data(parent_path))
assert len(parent["artifacts"]) == 10
for item in parent["artifacts"]:
    bind(item["path"], "direct own immutable parent payload, NOT premise", item)

ledger = data(PREFIX + "issues-v1.md").decode()
ids = re.findall(r"^\| (\d\d) \|", ledger, flags=re.MULTILINE)
assert ids == [f"{n:02d}" for n in range(1, 35)], ids
assert len(re.findall(r"\| Closed \|$", ledger, flags=re.MULTILINE)) == 34
assert "0 substantive defects" in ledger and "0 open issues" in ledger

unique = {}
for item in rows:
    record = {k: item[k] for k in ("path", "bytes", "sha256")}
    if record["path"] in unique:
        assert unique[record["path"]] == record
    unique[record["path"]] = record
deduplicated = [unique[path] for path in sorted(unique)]
digest = hashlib.sha256(json.dumps(deduplicated, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
summary = {
    "occurrences": len(rows), "unique_paths": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "encoding": "UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators",
    "old_parent_inventories_bound_not_recopied": True,
}

payloads = [PREFIX + suffix for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md", "worklog-v1.md", "freeze-v1.py")]
assert all((ROOT / path).is_file() for path in payloads)
for suffix in ("input-validation-v1.json", "freeze-output-v1.json", "manifest-v1.json"):
    assert not (ROOT / (PREFIX + suffix)).exists(), suffix

exclusive("input-validation-v1.json", {
    "status": "all current necessary declarations verified; compact immutable parents bound",
    "reviewer": "/root/review_2021_reasoning_j15_r2", "summary": summary,
    "occurrence_records": rows, "deduplicated_records": deduplicated,
    "constructor_parent_historical_own_paths_bound": constructor["historical_own_paths_bound"],
    "own_parent_input_summary_bound": parent["compact_input_summary"],
    "new_root_Runge_R1_files_metadata_or_findings_read_or_hashed": False,
    "old_unverified_R9_and_own_R12_are_preservation_NOT_mathematical_premises": True,
    "browser_primary_sources_have_URL_read_scopes_not_invented_native_hashes": True,
})
payloads.append(PREFIX + "input-validation-v1.json")
for item in deduplicated:
    assert fingerprint(item["path"]) == item
output = {
    "status": "COMPLETE initially blind ENTIRE WHOLE Runge R2 initial frozen",
    "whole_obligations": 34, "closed": 34, "substantive_issues": 0, "required_author_repairs": 0,
    "compact_input_summary": summary,
    "all_current_input_hashes_rechecked": True,
    "mathematical_code_CAS_scan_author_rerun_old_certificate_replay": False,
    "old_shared_cache_Git_writes_or_spawn": False,
}
exclusive("freeze-output-v1.json", output)
payloads.append(PREFIX + "freeze-output-v1.json")
manifest = {
    "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": output["status"], "reviewer": "/root/review_2021_reasoning_j15_r2",
    "constructor": constructor["constructor"],
    "target": fingerprint(TARGET + "candidate-v1.md"),
    "constructor_freeze": fingerprint(constructor_path),
    "scope": "ENTIRE RG1/RG2/RG3, all 34 obligations, exact sources and operative accepted interfaces",
    "closed_obligations": 34, "substantive_issues": 0, "required_author_repairs": 0,
    "candidate_promotion": False,
    "recommendation": "scoped acceptance after OTHER whole audit and coordinator full reconciliation",
    "new_root_Runge_R1_files_metadata_findings_read_or_hashed_before_ENTIRE_freeze": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "mathematical_code_CAS_scan_author_rerun_old_certificate_replay": False,
    "old_shared_cache_Git_writes_spawn_contact_charge_bypass": False,
    "authoritative_weekly_snapshot": {
        "tool": "mcp__codex_app__get_usage_limits", "at_utc": "2026-10-18 00:52:35 UTC",
        "total_weekly_used_percent": 5, "window_minutes": 10080,
        "reset_unix": 1792874445, "ordinary_usage_allowed": True,
        "legacy_and_by_limit_agree": True, "new_window_explicitly_user_authorized": True,
        "ceiling_total_percent": 90, "integration_reserve_retained": True,
        "automatic_further_reset_authorized": False,
    },
    "compact_input_summary": summary,
    "administrative_command": "python3 " + PREFIX + "freeze-v1.py",
    "artifacts": [fingerprint(path) for path in payloads],
}
assert len(manifest["artifacts"]) == 7
manifest_record = exclusive("manifest-v1.json", manifest)
print(json.dumps({"manifest": manifest_record, **output}, indent=2))
