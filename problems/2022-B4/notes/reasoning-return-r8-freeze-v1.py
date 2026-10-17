"""R8 compact administrative freeze, not a mathematical computation.

Every existing input is read-only; only exclusive new R8 metadata is
written. No proof/certificate/constructor program is run or imported.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/notes/reasoning-return-r8-"
PREVIOUS = "problems/2019-B4/reviews/coordinator-separation-scale-r1-review-2-"


def record(path):
    absolute = (ROOT / path).resolve()
    assert absolute.is_relative_to(ROOT), path
    rel = str(absolute.relative_to(ROOT))
    if rel.startswith("problems/2022-B4/reviews/reasoning-return-r8-"):
        raise RuntimeError("No NEW R8 reviewer material in constructor freeze")
    data = absolute.read_bytes()
    return {"path": rel, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = record(expected["path"])
    assert actual["sha256"] == expected["sha256"], expected["path"]
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], expected["path"]
    return actual


def load(path):
    checked = record(path)
    return json.loads((ROOT / checked["path"]).read_text())


def declarations(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and isinstance(obj.get("sha256"), str)
                and re.fullmatch("[0-9a-f]{64}", obj["sha256"])):
            yield obj
        for child in obj.values():
            yield from declarations(child)
    elif isinstance(obj, list):
        for child in obj:
            yield from declarations(child)


def unique(rows):
    result = {}
    for row in rows:
        item = {k: row[k] for k in ["path", "bytes", "sha256"]}
        assert item["path"] not in result or result[item["path"]] == item
        result[item["path"]] = item
    return list(result.values())


def digest(rows):
    values = sorted(unique(rows), key=lambda r: r["path"])
    canonical = json.dumps(values, sort_keys=True, ensure_ascii=False,
                           separators=(",", ":")).encode()
    return {"unique_paths": len(values),
        "canonical_sorted_record_array_sha256": hashlib.sha256(canonical).hexdigest(),
        "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), sorted by path"}


def write_new(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(obj, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return record(path)


for suffix in ["sources-v1.json", "input-validation-v1.json", "freeze-v1.json"]:
    assert not (ROOT / (PREFIX + suffix)).exists()

# Exact accepted mathematical inputs and current scope authorities.
direct = [record(path) for path in ["AGENTS.md",
    "problems/2022-B4/statement.md",
    "problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
    "problems/2022-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
    "problems/2022-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
    "problems/2022-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2022-B4/reviews/reasoning-return-r7-acceptance.md",
    "problems/2022-B4/notes/reasoning-return-r6-source-audit-v1.md",
    "problems/2022-B4/notes/reasoning-return-r7-source-audit-v1.md"]]
authority = []
declared = []
for number in [5, 6, 7]:
    path = f"problems/2022-B4/reviews/reasoning-return-r{number}-acceptance.json"
    metadata = record(path)
    obj = load(path)
    rows = [verify(r) for r in declarations(obj)]
    declared.extend(rows)
    authority.append({"metadata": metadata,
        "declared_fingerprint_occurrences_verified": len(rows),
        "deduplicated_summary": digest(rows)})
    accepted = verify(obj["accepted_copy"])
    raw = verify(obj["candidate"])
    assert (ROOT / accepted["path"]).read_bytes().endswith((ROOT / raw["path"]).read_bytes())

# Reproduce complete OWN preservation through immutable parent metadata.
# Do not re-copy unrelated historical inventories or read their mathematics.
parent_manifest_record = verify({"path": PREVIOUS + "manifest-v1.json", "bytes": 4632,
    "sha256": "98718a43fdd13ab3f5d52881659895906ccfabcc6faa77f4b84456eba7066d38"})
parent = load(parent_manifest_record["path"])
parent_artifacts = [verify(r) for r in parent["artifacts"]]
parent_validation_record = next(r for r in parent_artifacts
    if r["path"] == PREVIOUS + "input-validation-v1.json")
parent_validation = load(parent_validation_record["path"])
old_2020_manifest_record = verify(parent_validation["immutable_previous_manifest"])
old_2020_validation_record = verify(parent_validation["immutable_previous_validation"])
old_2020 = load(old_2020_manifest_record["path"])
old_R9_manifest_record = verify(parent_validation["immutable_R9_manifest"])
old_R9_validation_record = verify(parent_validation["immutable_R9_validation"])
old_R9 = load(old_R9_manifest_record["path"])
old_2025_manifest_record = verify(parent_validation["immutable_2025_manifest"])
old_2025_validation_record = verify(parent_validation["immutable_2025_validation"])
old_2025 = load(old_2025_manifest_record["path"])
ic_manifest_record = verify(parent_validation["immutable_IC_manifest"])
ic_validation_record = verify(parent_validation["immutable_IC_validation"])
ic = load(ic_manifest_record["path"])
ic_validation = load(ic_validation_record["path"])
older394 = unique([verify(r) for r in
    ic_validation["earlier_unique_records_preserved"]
    + ic["artifacts"] + [ic_manifest_record]
    + old_2025["artifacts"] + [old_2025_manifest_record]
    + old_R9["artifacts"] + [old_R9_manifest_record]
    + old_2020["artifacts"] + [old_2020_manifest_record]])
assert len(older394) == 394
assert digest(older394)["canonical_sorted_record_array_sha256"] == parent_validation[
    "earlier_own_summary"]["canonical_sorted_record_array_sha256"]
older_own = unique(older394 + parent_artifacts + [parent_manifest_record])
assert len(older_own) == 406

ids = re.findall(r"^\|R8-(\d\d)\|",
    (ROOT / (PREFIX + "obligations-v1.md")).read_text(), re.MULTILINE)
assert ids == [f"{i:02}" for i in range(1, 33)]
main_text = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
assert all(label in main_text for label in ["Candidate proof - unverified",
    "R8A", "R8B", "R8C", "R8D", "UNPROVED"])

now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 18:59:49UTC", "total_used_percent": 57,
    "window_minutes": 10080, "reset_unix": 1792745187,
    "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
    "review_integration_reserve": True}
parent_binding = {
    "immutable_parent_manifest": parent_manifest_record,
    "immutable_parent_validation": parent_validation_record,
    "exact_2020_reproduction_manifest": old_2020_manifest_record,
    "exact_2020_reproduction_validation": old_2020_validation_record,
    "exact_R9_reproduction_manifest": old_R9_manifest_record,
    "exact_R9_reproduction_validation": old_R9_validation_record,
    "exact_2025_reproduction_manifest": old_2025_manifest_record,
    "exact_2025_reproduction_validation": old_2025_validation_record,
    "exact_IC_reproduction_manifest": ic_manifest_record,
    "exact_IC_reproduction_validation": ic_validation_record,
    "older_own_paths_reverified": len(older_own),
    "older_own_summary": digest(older_own),
    "full_historical_inventory_deliberately_not_copied": True,
    "reproduction": "Reconstruct immutable IC earlier_unique_records_preserved plus IC artifacts/manifest, old2025 artifacts/manifest, oldR9review artifacts/manifest, old2020R7review artifacts/manifest, then previousSSreview artifacts/manifest. Verify406 paths read-only and apply canonical sorted-record digest. Parent exact accepted/historical authority inventories stay bound by immutable metadata, not re-expanded here."}
sources = write_new("sources-v1.json", {
    "recorded_at_utc": now, "status": "candidate proof - unverified",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "direct_exact_inputs": direct, "exact_accepted_authority_bindings": authority,
    "complete_source_read_scope": PREFIX + "source-audit-v1.md",
    "primary_actual_read_records": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf", "scope": "actual page2 B4 positive/simultaneous/open(b) statement"},
        {"url": "https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf", "scope": "Lemma29 integer hypotheses; complete Proposition37/Corollary38 proof contexts pp21--22; not full30pages"},
        {"url": "https://arxiv.org/html/2510.11723v2", "scope": "modified-division/prefix definitions and Section3.3 Conjecture3.9, Proposition3.10 proof, Remark3.11, Question3.12, Proposition3.13 proof; conditional only"},
        {"url": "https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers", "scope": "original intro/proper-residue condition and complete Lemma3.1/Propositions3.1--3.2 proofs, chieflypp1--6; no scan import"},
        {"url": "https://arxiv.org/pdf/math/0209247", "scope": "definitions, Theorems1.2/1.4, displayed Section2 proof, Section3 branching context through3.6; standard real language only"}],
    "source_native_binary_hashes": None,
    "new_native_PDF_cache_or_completed_failed_access_claim": False,
    "new_external_ordinary_termination_theorem_imported": False,
    "root_broad_target_no_new_proof_inference": True,
    "old_authorship_and_review_roles_disclosed": True,
    "compact_immutable_preservation_binding": parent_binding,
    "no_math_program_CAS_scan_certificate_author_rerun": True,
    "direct_weekly_telemetry": telemetry})
validation = write_new("input-validation-v1.json", {
    "checked_at_utc": now, "administrative_only_not_mathematical_evidence": True,
    "unused_prefix_confirmed_before_first_write": True,
    "direct_exact_inputs_verified": direct,
    "accepted_authority_record_occurrences_verified": len(declared),
    "accepted_authority_deduplicated_summary": digest(declared),
    "all_three_accepted_math_suffixes_byte_identical": True,
    "compact_immutable_preservation_binding": parent_binding,
    "combined_deduplicated_summary": digest(direct + declared + older_own),
    "all32_whole_obligations": ids,
    "no_mathematical_program_scan_CAS_or_certificate": True,
    "old_shared_Git_cache_edit_spawn_contact_charge_bypass_or_live_native_job": False,
    "two_OTHER_fresh_whole_initially_blind_audits_required": True,
    "ordinary_infinite_existence_no_tenfold_termination_annual_or_novelty_claim": False,
    "source_metadata": sources,
    "direct_weekly_telemetry": telemetry})
suffixes = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "freeze-v1.py",
    "sources-v1.json", "input-validation-v1.json"]
artifacts = [record(PREFIX + suffix) for suffix in suffixes]
manifest = write_new("freeze-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE meaningful partial/failed-bridge checkpoint",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "claims": ["R8A exact canonical backward fork",
        "R8B least binary survivor birth and actualq2 counterexample to generic pullback",
        "R8C exact two-step ordinary predecessor versus AB phase distinction",
        "R8D literal real-beta scaling fails canonical prefix interface"],
    "UNPROVED": ["no aligned infinite ordinary birth", "no-tenfold theorem",
        "positive ordinary infinite AB existence or termination", "full-controller/annual equality"],
    "whole_obligations": 32,
    "two_OTHER_fresh_initially_blind_WHOLE_nonconstructor_audits_required": True,
    "root_broad_target_no_new_proof_contribution": True,
    "old_roles_disclosed_no_self_recertification": True,
    "no_new_exclusion_finite_feature_substitution_or_novelty_claim": True,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "compact_immutable_parent_manifest": parent_manifest_record,
    "earlier_own_paths_preserved": len(older_own),
    "accepted_authority_record_occurrences_verified": len(declared),
    "accepted_authority_deduplicated_paths_verified": len(unique(declared)),
    "direct_weekly_telemetry": telemetry,
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts})
print(json.dumps({"main": record(PREFIX + "candidate-v1.md"),
    "manifest": manifest, "artifacts": len(artifacts), "whole_obligations": 32,
    "older_own_paths_preserved": len(older_own),
    "accepted_authority_occurrences": len(declared)}, indent=2))
