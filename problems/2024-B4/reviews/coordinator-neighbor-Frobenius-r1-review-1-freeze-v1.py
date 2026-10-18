"""Administrative byte binding ONLY. No mathematical calculation or replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-review-1-"
T = "problems/2024-B4/notes/coordinator-neighbor-Frobenius-r1-"
PEER = "problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-review-2-"
PRIOR = "problems/2017-B4/reviews/reasoning-value-return-r6-review-1-manifest-v1.json"


def safe(path):
    assert isinstance(path, str) and not path.startswith(PEER), path
    f = (ROOT / path).resolve()
    assert f.is_relative_to(ROOT), path
    assert not str(f.relative_to(ROOT)).startswith(PEER), path
    return f


def fp(path):
    b = safe(path).read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def verify(row):
    actual = fp(row["path"])
    assert actual == {k: row[k] for k in ("path", "bytes", "sha256")}, row["path"]
    return actual


def load(path):
    return json.loads(safe(path).read_text())


def write(suffix, obj):
    path = P + suffix
    with safe(path).open("x") as stream:
        json.dump(obj, stream, indent=2)
        stream.write("\n")
    return fp(path)


assert not safe(P + "manifest-v1.json").exists()
assert fp(T + "candidate-v1.md") == {
    "path": T + "candidate-v1.md", "bytes": 13799,
    "sha256": "775501d763a46b8411a6509c7da06d3a7fc3dacb3b27141881b80de2ea37f9d4"}
assert fp(T + "freeze-v1.json") == {
    "path": T + "freeze-v1.json", "bytes": 2492,
    "sha256": "f97a4dc9eb21dea3e4e4e94d42ba7f3bdf09ddf3555e2defcab19c4ec5812671"}
constructor = load(T + "freeze-v1.json")
assert len(constructor["artifacts"]) == 6
target_rows = [verify(row) for row in constructor["artifacts"]]
target_rows.append(fp(T + "freeze-v1.json"))
declared = load(T + "inputs-v1.json")
assert len(declared["direct_context_records"]) == 14
context_rows = [verify(row) for row in declared["direct_context_records"]]
embedded_rows = [verify(row["existing_native_record"])
                 for row in declared["public_primary_sources"]
                 if "existing_native_record" in row]
assert len(embedded_rows) == 1

assert fp(PRIOR) == {
    "path": PRIOR, "bytes": 4335,
    "sha256": "01b4b4e1f3215ee9f846e8681986060d68ecd7e561689fa60baa9c59cc08aa15"}
prior = load(PRIOR)
assert len(prior["artifacts"]) == 7
prior_rows = [fp(PRIOR)] + [verify(row) for row in prior["artifacts"]]
rows = target_rows + context_rows + embedded_rows + prior_rows
unique = {}
for row in rows:
    if row["path"] in unique:
        assert unique[row["path"]] == row
    unique[row["path"]] = row
dedup = [unique[path] for path in sorted(unique)]
digest = hashlib.sha256(json.dumps(dedup, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()

prose = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md", "worklog-v1.md"]
for suffix in prose:
    assert safe(P + suffix).stat().st_size > 2000
ledger = safe(P + "issues-v1.md").read_text()
ids = re.findall(r"^\|NF-(\d\d)\|", ledger, re.M)
assert ids == [str(i).zfill(2) for i in range(1, 37)]
assert ledger.count("|Closed: valid|") == 36

budget = {
    "explicit_human_authorization_for_new_reported_window": True,
    "tool": "mcp__codex_app__get_usage_limits",
    "at_utc": "2026-10-18 00:20:10 UTC",
    "total_weekly_used_percent": 2,
    "window_minutes": 10080,
    "reset_unix": 1792874445,
    "ordinary_usage_allowed": True,
    "legacy_and_by_limit_fields_agree": True,
    "ceiling_total_percent": 90,
    "integration_reserve_retained": True,
    "automatic_further_reset_authorized": False,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning": "max",
    "independently_verified_effective_settings": None}

input_row = write("input-validation-v1.json", {
    "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
    "administrative_only_no_mathematical_calculation": True,
    "target_manifest_and_payloads": target_rows,
    "constructor_direct_context_records": context_rows,
    "repeated_embedded_native_source_records": embedded_rows,
    "immutable_immediate_own_parent_manifest_and_payloads": prior_rows,
    "parent_historical_current_input_summary_bound_not_recopied_or_rewalked":
        prior["current_input_summary"],
    "occurrences_verified": len(rows),
    "unique_paths_verified": len(unique),
    "deduplicated_summary_sha256": digest,
    "encoding": "UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators",
    "all_necessary_current_declared_fingerprints_verified": True,
    "all_NEW_peer_NF_reports_findings_sources_metadata_unread_and_unhashed": True,
    "only_own_assigned_NEW_prefix_written": True,
    "old_accepted_bodies_context_not_mathematical_premises": True,
    "whole_author_obligations": 36,
    "individual_ledger_dispositions": 36,
    "substantive_defects": 0, "required_repairs": 0, "open_issues": 0,
    "weekly_budget_and_settings": budget,
    "public_source_read_scopes": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
         "scope": "page2 B4 hypothesis and actual(b), freshly read; no preliminary research",
         "fresh_native_hash": None},
        {"url": "https://arxiv.org/pdf/0903.2016v4",
         "scope": "fresh Section3 setup/local data and Section3.2 Bezout/Cor8; Section4 and Theorem15/16 actual conditional/component boundaries; not whole19pages",
         "fresh_native_hash": None},
        {"url": "https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf",
         "scope": "existing images29,30,31 printed24--26 COMPLETE Theorem8 proof; native PDF bound not entire97pages read"},
        {"url": "https://eprint.iacr.org/2005/096",
         "scope": "constructor's abstract/metadata/403 failure disclosed, not freshly retrieved or imported"},
        {"url": "https://arxiv.org/pdf/2602.01583",
         "scope": "constructor's partial lead unimported; not freshly read or applied"}]
})

output_row = write("freeze-output-v1.json", {
    "administrative_only": True,
    "current_input_occurrences_verified": len(rows),
    "current_unique_paths_verified": len(unique),
    "deduplicated_summary_sha256": digest,
    "entire_whole_initial_complete": True,
    "all_author_obligations": 36, "individual_ledger_dispositions": 36,
    "substantive_defects": 0, "required_repairs": 0, "open_issues": 0,
    "peer_NEW_NF_material_unread_through_entire_initial": True,
    "mathematical_programs_CAS_scans_author_reruns": 0,
    "own_prior_parent_preserved": True,
    "not_a_promotion": True})

artifacts = [fp(P + suffix) for suffix in prose + ["freeze-v1.py"]]
artifacts += [input_row, output_row]
manifest_row = write("manifest-v1.json", {
    "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "ENTIRE initially blind nonconstructor WHOLE R1 complete; coordinator reconciliation pending",
    "reviewer": "/root/review_2021_reasoning_j15_r2",
    "target": target_rows[0],
    "constructor_freeze": target_rows[-1],
    "claims": ["NF1 neighbor-Frobenius whole absolute irreducibility",
               "NF2 entire projective shared-point elimination",
               "NF3 ell7 four-bit corollary for 3 not dividing a"],
    "all_author_obligations": 36, "individual_ledger_dispositions": 36,
    "substantive_defects": 0, "required_repairs": 0, "open_issues": 0,
    "recommendation": "Accept exact scoped NF1--NF3 after second OTHER whole audit and coordinator reconciliation; no annual/four-bit classification/novelty claim",
    "root_sole_NEW_constructor_excluded": True,
    "reviewer_old_T1_T4_C7_C11_authorship_and_CP_GK_S3_jet_review_roles_disclosed": True,
    "reviewer_no_NEW_NF_construction_contribution": True,
    "old_accepted_bodies_context_not_newly_self_recertified_or_used_as_premises": True,
    "ENTIRE_initial_blind_to_all_NEW_B_NF_reports_findings_ledgers_sources_metadata": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "current_input_summary": {"occurrences": len(rows), "unique_paths": len(unique),
        "deduplicated_summary_sha256": digest,
        "encoding": "UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators"},
    "immutable_own_prior_parent": fp(PRIOR),
    "weekly_budget_and_settings": budget,
    "administrative_command": "python3 " + P + "freeze-v1.py",
    "no_mathcode_CAS_scan_author_rerun_shared_Git_cache_old_edit_spawn_contact_charge_bypass": True,
    "not_a_promotion": True,
    "artifacts": artifacts})

for row in rows + artifacts + [manifest_row]:
    verify(row)
print(json.dumps({"manifest": manifest_row, "report": artifacts[0],
                  "ledger": artifacts[1], "whole_rows": 36,
                  "payloads": len(artifacts), "records_including_manifest": len(artifacts) + 1,
                  "current_input_occurrences": len(rows),
                  "current_unique_paths": len(unique),
                  "summary_sha256": digest,
                  "postfreeze_all_current_and_own_records_verified": True,
                  "substantive_defects": 0, "required_repairs": 0,
                  "open_issues": 0}, indent=2))
