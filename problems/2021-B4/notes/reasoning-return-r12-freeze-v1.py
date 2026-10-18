"""Administrative byte/JSON/obligation-syntax binding ONLY. No math calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/notes/reasoning-return-r12-"
R11 = "problems/2021-B4/notes/reasoning-return-r11-freeze-v1.json"
NF = "problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-review-1-manifest-v1.json"


def safe(path):
    assert isinstance(path, str)
    assert not path.startswith("problems/2021-B4/reviews/reasoning-return-r12-"), path
    assert not path.startswith("problems/2025-B4/reviews/reasoning-return-r9-runge-"), path
    f = (ROOT / path).resolve()
    assert f.is_relative_to(ROOT), path
    return f


def fp(path):
    b = safe(path).read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def verify(row):
    value = fp(row["path"])
    assert value == {k: row[k] for k in ("path", "bytes", "sha256")}, row["path"]
    return value


def load(path):
    return json.loads(safe(path).read_text())


def write(suffix, obj):
    path = P + suffix
    with safe(path).open("x") as stream:
        json.dump(obj, stream, indent=2)
        stream.write("\n")
    return fp(path)


assert not safe(P + "freeze-v1.json").exists()
prose = ["candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
         "failed-routes-v1.md", "source-audit-v1.md", "worklog-v1.md"]
for suffix in prose:
    assert safe(P + suffix).stat().st_size > 2000
ids = re.findall(r"^\|R12-(\d\d)\|",
                 safe(P + "obligations-v1.md").read_text(), re.M)
assert ids == [str(i).zfill(2) for i in range(1, 61)]

assert fp(R11) == {
    "path": R11, "bytes": 3477,
    "sha256": "c0b3a0650274e899fb97f84ec042e1edb9d5e6db0f603c7f22ee5bd691e12ca4"}
old_r11 = load(R11)
assert len(old_r11["artifacts"]) == 10
r11_rows = [fp(R11)] + [verify(row) for row in old_r11["artifacts"]]
old_inputs = load("problems/2021-B4/notes/reasoning-return-r11-input-validation-v1.json")

selected_paths = {
    "AGENTS.md",
    "problems/2021-B4/statement.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
    "problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md",
    "problems/2021-B4/proofs/reviewed-return-r3-v1.1.md",
    "problems/2021-B4/notes/reasoning-return-r3-transfer-candidate-v1.md",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.md",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance.md",
    "problems/2021-B4/reviews/return-r3-acceptance.md",
    ".cache/literature/2021/cited-66c5af6a0f0239f5.pdf",
    ".cache/literature/deep-literature-r1/2021-draisma-dejong-erratum-2011.pdf"}
direct = [verify(row) for row in old_inputs["direct_inputs"]
          if row["path"] in selected_paths]
assert {row["path"] for row in direct} == selected_paths

r11_accepted = {
    "path": "problems/2021-B4/proofs/reviewed-reasoning-return-r11-v1.1.md",
    "bytes": 20045,
    "sha256": "35dc50702ecd0965c8a4f35844bc47ea3c64c938dba3bd0ced9b7da484d8a9a6"}
direct.append(verify(r11_accepted))
direct.append(fp("problems/2021-B4/reviews/reasoning-return-r11-acceptance.md"))
acceptance_rows = []
acceptance_summaries = []
for name in ("reasoning-return-r11", "reasoning-return-r8",
             "reasoning-return-r5", "odd-support-exclusion", "return-r3"):
    path = "problems/2021-B4/reviews/" + name + "-acceptance.json"
    direct.append(fp(path))
    obj = load(path)
    if name == "return-r3":
        acceptance_rows += [verify(row) for row in obj["accepted_packets"]]
        acceptance_rows.append(verify(obj["proof_register"]))
        scope = "TA1 body/register read; other packet hashes only, not freshly reaudited"
    else:
        acceptance_rows += [verify(obj["candidate"]), verify(obj["accepted_copy"])]
        scope = "complete exact accepted body and scope read; no old peer review replay"
    acceptance_summaries.append({
        "path": path, "status": obj["status"], "read_scope": scope,
        "old_verified_occurrences_bound_not_replayed":
            obj.get("record_occurrences_verified", obj.get("verified_record_occurrences")),
        "old_verified_unique_paths_bound_not_replayed":
            obj.get("unique_paths_verified", obj.get("verified_unique_paths"))})

assert fp(NF) == {
    "path": NF, "bytes": 4594,
    "sha256": "08df7fdf30ef6c1a0b5d57b6e8cbca602d0a8af929287ade5a027dd209754ad7"}
old_nf = load(NF)
assert len(old_nf["artifacts"]) == 7
nf_rows = [fp(NF)] + [verify(row) for row in old_nf["artifacts"]]
rows = direct + r11_rows + nf_rows + acceptance_rows
unique = {}
for row in rows:
    if row["path"] in unique:
        assert unique[row["path"]] == row
    unique[row["path"]] = row
dedup = [unique[path] for path in sorted(unique)]
digest = hashlib.sha256(json.dumps(dedup, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()

sources = [
    {"title": "Official2021 Paper B",
     "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
     "fresh_read_scope": "page2 B4 full hypothesis and(b), no preliminary proof",
     "role": "official rational-witness domain", "fresh_native_hash": None},
    {"title": "Castryck--Laterveer--Ounaies, Constraints on counterexamples ... degree12",
     "url": "https://arxiv.org/pdf/1208.5404",
     "fresh_read_scope": "Sections3.4--3.5 eq9--13/Lemma17/normalized-center/beta derivation; Proposition19 statement/unramified remark; not whole23pages",
     "role": "method attribution; all-root-rational/unramified theorem not applied",
     "fresh_native_hash": None},
    {"title": "Draisma--de Jong2011 erratum",
     "url": "https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf",
     "fresh_read_scope": "complete one-page original correction,20 extracted lines",
     "role": "prime5 shortcut excluded", "fresh_native_hash": None}]

source_row = write("sources-v1.json", {
    "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "candidate proof - unverified",
    "public_primary_sources": sources,
    "fresh_complete_accepted_mathematical_bodies": [
        "problems/2021-B4/proofs/reviewed-reasoning-return-r11-v1.1.md",
        "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
        "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
        "problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md",
        "problems/2021-B4/proofs/reviewed-return-r3-v1.1.md",
        "problems/2021-B4/notes/reasoning-return-r3-transfer-candidate-v1.md"],
    "accepted_authority_records": acceptance_summaries,
    "old_native_source_bindings_browser_bytes_not_asserted_identical": [
        row for row in direct if row["path"].startswith(".cache/")],
    "immutable_R11_constructor_parent": fp(R11),
    "immutable_immediate_own_NF_review_parent": fp(NF),
    "no_new_external_theorem_import_for_field_lemma": True,
    "root_supplied_NO_new_R12_mathematical_inference": True,
    "older_TA1_R8_R11_authorship_and_J15_PN_R5_review_roles_disclosed": True,
    "two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
    "new_mathcode_CAS_scan_author_rerun_or_old_certificate_replay": False,
    "new_download_cache_edit_render_native_wait_contact_charge_bypass": False})

budget = {
    "human_explicitly_authorized_new_reported_window": True,
    "tool": "mcp__codex_app__get_usage_limits",
    "at_utc": "2026-10-18 00:40:13 UTC", "total_weekly_used_percent": 4,
    "window_minutes": 10080, "reset_unix": 1792874445,
    "ordinary_usage_allowed": True, "legacy_and_by_limit_agree": True,
    "ceiling_total_percent": 90, "integration_reserve_retained": True,
    "automatic_further_reset_authorized": False}

input_row = write("input-validation-v1.json", {
    "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
    "administrative_only_no_mathematical_calculation": True,
    "necessary_current_direct_inputs": direct,
    "accepted_authority_current_candidate_copy_and_register_declarations": acceptance_rows,
    "immutable_R11_constructor_manifest_and_payloads": r11_rows,
    "immutable_immediate_own_NF_review_manifest_and_payloads": nf_rows,
    "immutable_R11_historical_summary_bound_not_rewalked": old_r11["compact_input_summary"],
    "immutable_NF_historical_summary_bound_not_rewalked": old_nf["current_input_summary"],
    "fingerprint_occurrences_verified": len(rows),
    "unique_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "encoding": "UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators",
    "historical_inventories_bound_not_giant_recopied_or_mathematically_replayed": True,
    "whole_obligations": 60,
    "root_supplied_NO_new_R12_mathematical_inference": True,
    "no_future_RunGE_audit_or_NEW_R12_peer_files_read": True,
    "no_old_shared_cache_Git_writes_spawn_contact_charge_bypass": True,
    "new_mathcode_CAS_scan_author_rerun_or_old_certificate_replay": False,
    "weekly_budget": budget})

output_row = write("freeze-output-v1.json", {
    "administrative_only": True, "status": "candidate proof - unverified",
    "whole_obligations": 60, "current_fingerprint_occurrences": len(rows),
    "current_unique_paths": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "proposed_actual_m6_exclusion_complete": True,
    "mathematical_programs_CAS_scans_author_reruns": 0,
    "two_OTHER_whole_audits_still_required": True,
    "not_a_promotion_or_annual_solution": True})

artifacts = [fp(P + suffix) for suffix in prose + ["freeze-v1.py"]]
artifacts += [source_row, input_row, output_row]
manifest_row = write("freeze-v1.json", {
    "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "candidate proof - unverified; COMPLETE constructor checkpoint",
    "constructor": "/root/review_2021_reasoning_j15_r2",
    "claims": ["R12A exact six-even support-to-center nonvanishing obstruction",
               "R12B complete ACTUAL m6 first-break exclusion",
               "R12C three-unit essential-center/full-gcd corollary"],
    "whole_obligations": 60,
    "two_OTHER_fresh_initially_blind_ENTIRE_WHOLE_nonconstructor_audits_required": True,
    "constructor_excluded_from_independent_review": True,
    "root_supplied_NO_new_R12_mathematical_inference": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "no_full_repeated_branch_J15_degree20_annual_lift_or_novelty_claim": True,
    "no_extra_units_depth_height_sign_real_root_or_quotient_CA_assumptions": True,
    "new_mathematical_code_CAS_routine_scan_author_rerun_or_old_certificate_replay": False,
    "proof_critical_small_finite_field_certificates_entirely_hand_derived": True,
    "old_shared_cache_Git_writes_spawn_contact_charge_bypass": False,
    "authoritative_weekly_snapshot": budget,
    "compact_input_summary": {
        "occurrences": len(rows), "unique_paths": len(unique),
        "canonical_deduplicated_summary_sha256": digest,
        "encoding": "UTF8 JSON sorted unique path/bytes/sha256; sorted keys; compact separators",
        "old_parent_inventories_bound_not_recopied": True},
    "administrative_command": "python3 " + P + "freeze-v1.py",
    "artifacts": artifacts})

for row in rows + artifacts + [manifest_row]:
    verify(row)
print(json.dumps({
    "manifest": manifest_row, "candidate": artifacts[0],
    "whole_obligations": 60, "payloads": len(artifacts),
    "records_including_manifest": len(artifacts) + 1,
    "current_fingerprint_occurrences": len(rows),
    "current_unique_paths": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "postfreeze_current_and_own_records_verified": True,
    "status": "candidate proof - unverified; two OTHER whole audits pending"}, indent=2))
