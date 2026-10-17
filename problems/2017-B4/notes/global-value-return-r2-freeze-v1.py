"""Administrative freeze only. No mathematical computation or theorem test."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path("/Users/uqmkamga/Documents/ChatGPT/Website")
BASE = Path("problems/2017-B4/notes")
PREFIX = "global-value-return-r2"
OUTPUT_MANIFEST = BASE / (PREFIX + "-manifest-v1.json")
assert not (ROOT / OUTPUT_MANIFEST).exists(), "Frozen manifest already exists; no overwrite."
NOW = datetime.now(timezone.utc).isoformat()

def record(path):
    path = str(path)
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}

def check(expected):
    actual = record(expected["path"])
    assert actual == {k: expected[k] for k in ("path", "bytes", "sha256")}, (
        "Record changed", expected, actual)
    return actual

def write_json(path, value):
    (ROOT / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")

previous_manifest_record = {
    "path": "problems/2024-B4/reviews/P2-critical-jet-review-2-manifest-v1.json",
    "bytes": 2970,
    "sha256": "73a3e6ff8c1a1944cb9caa06442415c837668d9d008d06e1c4fc65e872fdd4ce"}
previous_validation_record = {
    "path": "problems/2024-B4/reviews/P2-critical-jet-review-2-input-validation-v1.json",
    "bytes": 59431,
    "sha256": "9988155549a58bcd108deb9bfb0550eb005b1ae06f8d6823a54213146d0152f0"}
check(previous_manifest_record)
check(previous_validation_record)
previous_manifest = json.loads((ROOT / previous_manifest_record["path"]).read_text())
previous_validation = json.loads((ROOT / previous_validation_record["path"]).read_text())
previous_records = previous_validation["earlier_unique_records_preserved"]
assert len(previous_records) == 286
previous_records += previous_manifest["artifacts"] + [previous_manifest_record]
unique_previous = {}
for item in previous_records:
    item = {k: item[k] for k in ("path", "bytes", "sha256")}
    if item["path"] in unique_previous:
        assert unique_previous[item["path"]] == item, "Inconsistent prior identity"
    unique_previous[item["path"]] = item
prior_checks = [check(item) for item in unique_previous.values()]
assert len(prior_checks) == 292

old_source_path = "problems/2017-B4/notes/global-value-return-r1-sources-v1.json"
old_sources = json.loads((ROOT / old_source_path).read_text())
logical_paths = [
    "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md",
    "problems/2017-B4/proofs/reviewed-allD-global-v1.1.md",
    "problems/2017-B4/proofs/reviewed-concavity-v1.1.md"]
old_inputs = {item["path"]: item for item in
              old_sources["direct_full_logical_or_protocol_context_reads"]}
logical = [check(old_inputs[path]) for path in logical_paths]
accepted_v_path = "problems/2017-B4/proofs/reviewed-global-value-return-v1.1.md"
accepted_v = record(accepted_v_path)
old_v_body = (ROOT / "problems/2017-B4/notes/global-value-return-r1-candidate-v1.md").read_bytes()
assert (ROOT / accepted_v_path).read_bytes().endswith(old_v_body)
logical.append(accepted_v)
transitive = [
    check(item) for item in
    old_sources["global_ten_accepted_transitive_interfaces_checked_against_frozen_source_hashes"]]
assert len(transitive) == 10
context = [
    record("AGENTS.md"),
    record("problems/2017-B4/statement.md"),
    record("problems/2017-B4/notes/global-value-return-r1-manifest-v1.json"),
    record(old_source_path)]
cache = [check(item) for item in old_sources["existing_cache_fingerprints"]]
unconfirmed_cache = ".cache/literature/2017/global-value-return-r2-felsner-valtr-2011.pdf"
assert not (ROOT / unconfirmed_cache).exists(), (
    "A later file appeared; inspect provenance and revise the new source record before freezing.")

obligation_path = BASE / (PREFIX + "-obligations-v1.md")
obligation_text = (ROOT / obligation_path).read_text()
for index in range(1, 49):
    assert ("| OP-%02d |" % index) in obligation_text
main_path = BASE / (PREFIX + "-candidate-v1.md")
main_text = (ROOT / main_path).read_text()
for marker in ("**Candidate proof - unverified.**", "**OP1", "**OP2", "**OP3",
               "## 1.", "## 2.", "## 3.", "## 4.", "## 5.", "## 6.", "## 7."):
    assert marker in main_text, ("Missing complete main section", marker)

sources_path = BASE / (PREFIX + "-sources-v1.json")
sources = {
    "recorded_at_utc": NOW,
    "status": "candidate proof - unverified; source scopes are not independent review",
    "direct_accepted_logical_input_records": logical,
    "exact_input_scopes": [
        "DC: invariant projection/section, canonical gaps/full port decorations, kth matching and event-poset reconstruction",
        "G: each fixed D full balanced ALL-integer limit and official scalar limit, no effective side-length rate",
        "V: accepted old internal-class/full per-rank ordered port lists; earlier E/R remain hypotheses",
        "U: separately accepted L<324757/500000 only, old certificate not rerun"],
    "transitive_ten_accepted_global_interface_identities": transitive,
    "transitive_read_limit": (
        "Previous complete accepted bodies/source maps and own whole global audit retained; "
        "this return does not independently re-audit the constructor's own older inputs."),
    "protocol_official_and_prior_frozen_context": context,
    "existing_cache_records_revalidated": cache,
    "primary_web_reads": [
        {
            "url": "https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf",
            "title": "Felsner and Valtr, Coding and Counting Arrangements of Pseudolines (2011)",
            "read_scope": "Complete introduction and Section2 through printed p7 in primary web viewer",
            "role": "Bounded marked/wiring/local-sequence and cutpath coding context only; no OP theorem import",
            "binary_local_hash": None},
        {
            "url": "https://arxiv.org/pdf/2502.20909v2",
            "title": "Dallant, Improved Bound on the Number of Pseudoline Arrangements via the Zone Theorem, v2",
            "read_scope": "Reopened primary viewer; introduction/conventions also actually read in prior return",
            "role": "Dated context; new OP1-OP3 direct, accepted U imported separately",
            "binary_hash": cache[-1]["sha256"]}
    ],
    "source_retrieval_failure": {
        "url": "https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf",
        "attempted_output": unconfirmed_cache,
        "sandbox_result": "curl6; could not resolve host",
        "escalated_retry_result": "No output/PID/session; tool/approval wait interrupted; tool aborted after2508.2s",
        "parent_estimated_wait_utc": "last completed13:29UTC to roughly14:11UTC",
        "local_file_exists_at_freeze": False,
        "process_inspection_result": "/bin/ps denied by sandbox; no process absence or reap claimed",
        "retried_after_interruption": False,
        "missing_hash_invented": False},
    "coordinator_integer_grid_SFT_lead": {
        "received": True, "used_as_theorem_or_strategy_premise": False,
        "exact_encoding_mixing_or_boundary_entropy_interface_established": False},
    "new_mathematical_program_CAS_enumeration_or_numerical_certificate": False,
    "full_external_paper_redistribution_charge_contact_or_bypass": False,
    "novelty_numeric_value_actual_computability_or_effective_UR_claim": False}
write_json(sources_path, sources)

validation_path = BASE / (PREFIX + "-input-validation-v1.json")
validation = {
    "validated_at_utc": NOW,
    "administrative_integrity_only": True,
    "direct_accepted_input_records": logical,
    "ten_transitive_input_records": transitive,
    "context_records": context,
    "existing_cache_records": cache,
    "accepted_V_exact_old_frozen_suffix_verified": True,
    "all48_obligation_rows_and_main_sections_present": True,
    "unconfirmed_Felsner_Valtr_download_still_absent": True,
    "earlier_unique_records_preserved": sorted(prior_checks, key=lambda x: x["path"]),
    "earlier_unique_record_count": len(prior_checks),
    "mathematical_program_or_theorem_validation_claim": False}
write_json(validation_path, validation)

artifact_names = [
    PREFIX + "-candidate-v1.md",
    PREFIX + "-obligations-v1.md",
    PREFIX + "-constructor-checks-v1.md",
    PREFIX + "-source-checks-v1.md",
    PREFIX + "-worklog-v1.md",
    PREFIX + "-freeze-v1.py",
    PREFIX + "-sources-v1.json",
    PREFIX + "-input-validation-v1.json"]
artifacts = [record(BASE / name) for name in artifact_names]
manifest = {
    "frozen_at_utc": NOW,
    "status": "candidate proof - unverified; complete OP1-OP3 plus auxiliary obstruction checkpoint",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "new_mathematical_claims": [
        "OP1: actual contact forces equal crossed-other-track sets and equal partner gap index",
        "OP2: invariant one-sided port code; Q-dependent common-prefix weights, uniform weighted and closed finite bounds",
        "OP3: fixed-D direction error f_D+L/D, f_D=(1-1/(2D))h2(1/(2D-1))",
        "Auxiliary: even brickwall classes obstruct uniform quadratic improvement of the OLD per-class degree/Jensen bound"],
    "author_obligations": 48,
    "independent_whole_audits_required": 2,
    "independent_whole_audits_completed_for_this_packet": 0,
    "old_V_local_background_authorship_disclosed": True,
    "new_numerical_value_full_annual_novelty_or_actual_computability_claim": False,
    "effective_E_R_or_fixedD_rate_established": False,
    "coordinator_new_SFT_lead_used": False,
    "mathematical_program_CAS_scan_or_certificate_rerun": False,
    "earlier_frozen_and_context_records_verified_unchanged": len(prior_checks),
    "source_download_stall_recorded_honestly": True,
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 14:11:16 UTC",
        "total_used_percent": 43,
        "window_minutes": 10080,
        "reset_unix": 1792745187,
        "total_ceiling_percent": 90,
        "reserve_for_review_integration": True},
    "administrative_command": (
        "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 "
        "problems/2017-B4/notes/global-value-return-r2-freeze-v1.py"),
    "artifacts": artifacts}
write_json(OUTPUT_MANIFEST, manifest)
print(json.dumps({
    "manifest": record(OUTPUT_MANIFEST),
    "candidate": artifacts[0],
    "artifacts": len(artifacts),
    "obligations": 48,
    "earlier_records_preserved": len(prior_checks),
    "status": manifest["status"]}, indent=2))

