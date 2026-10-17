"""R7 compact documentary freeze. No mathematical computation or old writes."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/notes/reasoning-return-r7-"
PARENT = "problems/2024-B4/reviews/reasoning-components-r1-review-2-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = record(expected["path"])
    assert actual["sha256"] == expected["sha256"], expected["path"]
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], expected["path"]
    return actual


def read_json(path):
    return json.loads((ROOT / path).read_text())


def declared(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
                and isinstance(value.get("sha256"), str)
                and len(value["sha256"]) == 64):
            yield value
        for child in value.values():
            yield from declared(child)
    elif isinstance(value, list):
        for child in value:
            yield from declared(child)


def digest(records):
    ordered = sorted(records, key=lambda r: r["path"])
    data = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def deduplicate(records):
    unique = {}
    for item in records:
        if item["path"] in unique:
            assert unique[item["path"]] == item, item["path"]
        unique[item["path"]] = item
    return list(unique.values())


def write_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return record(path)


for suffix in ["sources-v1.json", "input-validation-v1.json", "freeze-v1.json"]:
    assert not (ROOT / (PREFIX + suffix)).exists()

parent_manifest = verify({"path": PARENT + "manifest-v1.json", "bytes": 3599,
    "sha256": "4c82042830db3d3e45a602a96c4ae9680804c48f994c563e39c8aeff53d0f956"})
parent = read_json(parent_manifest["path"])
parent_validation = verify(next(r for r in parent["artifacts"]
    if r["path"] == PARENT + "input-validation-v1.json"))
assert parent_validation["sha256"] == "066ab3aeb52d9e278b4335ef7a4feee885e8c484bb7ac147ecc2578a992d9890"
old = read_json(parent_validation["path"])

# Verify the immutable parent's historical declarations but DO NOT COPY them.
parent_declared = [verify(r) for obj in [parent, old] for r in declared(obj)]
parent_unique = deduplicate(parent_declared)
old_chain = deduplicate([verify(r) for r in old["earlier_unique_records_preserved"]]
    + [verify(r) for r in parent["artifacts"]] + [parent_manifest])
assert len(old["earlier_unique_records_preserved"]) == 367
assert len(old_chain) == 373

r6_manifest = record("problems/2025-B4/notes/reasoning-return-r6-freeze-v1.json")
r6 = read_json(r6_manifest["path"])
r6_artifacts = [verify(r) for r in r6["artifacts"]]
r6_main = verify({"path": "problems/2025-B4/notes/reasoning-return-r6-candidate-v1.md",
    "bytes": 25588,
    "sha256": "bdf566f44dcabb5b7bbfb96778b1dd58b7375bf46fcd697c3579564e5e9da627"})
accepted_r6_path = "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md"
assert (ROOT / accepted_r6_path).read_bytes().endswith(
    (ROOT / r6_main["path"]).read_bytes())
r6_sources_path = "problems/2025-B4/notes/reasoning-return-r6-sources-v1.json"
r6_source = read_json(r6_sources_path)
accepted_old = [verify(r) for r in r6_source["accepted_context_records"]]
accepted_inputs = accepted_old + [record(accepted_r6_path)]
cache = verify(r6_source["primary_sources"][1]["cached_binary"])
statement = record("problems/2025-B4/statement.md")

now = datetime.now(timezone.utc).isoformat()
sources = write_new("sources-v1.json", {
    "recorded_at_utc": now,
    "status": "candidate proof - unverified; precise documentary source roles",
    "official": {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf",
        "open_part": "B4(b), all integers x,y,n,q, n,q>=2",
        "arithmetic_sector": "G_p(x)=y^p,p>=37 prime,|x|>=2,signed x retained",
        "local_statement": statement},
    "accepted_input_records": accepted_inputs,
    "accepted_R6_frozen_parent": r6_manifest,
    "accepted_R6_byte_identical_original_candidate": r6_main,
    "R6_all_eight_frozen_artifacts_verified": len(r6_artifacts),
    "primary_sources": [
        {"author": "Preda Mihailescu",
         "title": "Class Number Conditions for the Diagonal Case of the Equation of Nagell and Ljunggren",
         "year": 2008, "doi": "10.1007/978-3-211-74280-8_15",
         "url": "https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren",
         "internal_version": "2.0,2007-09-17",
         "actual_read": "Relevant2.2/2.3/2.5/2.5.1/4.2 and complete4.3 in current/preceding R6; Theorem3 statement rechecked current",
         "import": "Attributed classical matched-prime Jacobi ideal formula and standard cyclotomic background, as accepted R6",
         "attribution": "Phase additivity, idempotents and zero-signature norm mechanism are existing ideas",
         "not_imported": "Full Theorems3/4, class-number exclusion, all-conjugate target, generalized e1, or arbitrary-lift coefficientwise phase invariance",
         "binary_downloaded": False, "new_binary_sha256": None},
        {"authors": ["B. Bartolome", "P. Mihailescu"],
         "title": "On the equation X^n-1=BZ^n",
         "url": "https://arxiv.org/pdf/1412.5798v2",
         "actual_read": "Earlier complete relevant5-18 including appendices5.1/5.1.1/5.2 retained; targeted current series/bouquet and5.2 reads",
         "cached_binary": cache,
         "role": "Existing series/Vandermonde/bouquet context, no new arithmetic theorem import"},
        {"authors": ["Chang Liu", "Preda Mihailescu"],
         "title": "An alternative proof of the Catalan conjecture",
         "journal": "Bulletin Transilvania University Brasov,SeriesIII5(67),1(2025),161-172",
         "doi": "10.31926/but.mif.2025.5.67.1.12",
         "url": "https://webbut.unitbv.ro/index.php/Series_III/article/download/8768/6170/17457",
         "actual_read": "All12pages, actual Proposition1, pair-module quotient action, applications and final remark",
         "hypothesis_boundary": "q>p; q=p expressly deferred; NOT a diagonal input",
         "role": "Unimported lead; diagonal quotient-invariance obligation isolated, no arithmetic theorem refutation",
         "binary_downloaded": False, "new_binary_sha256": None}],
    "old_FS_R6_authorship_and_prior_review_roles_disclosed": True,
    "no_fresh_unrelated_mathematics_reread_for_administration": True,
    "mathematical_program_CAS_scan_table_certificate_or_author_rerun": False,
    "new_binary_download_cache_mutation_third_party_redistribution": False,
    "novelty_annual_or_published_theorem_refutation_claim": False})

ids = re.findall(r"^\| R7-(\d\d) \|",
    (ROOT / (PREFIX + "obligations-v1.md")).read_text(), re.MULTILINE)
assert ids == [f"{i:02}" for i in range(1, 57)]

validation = write_new("input-validation-v1.json", {
    "validated_at_utc": now,
    "administrative_metadata_only_not_mathematical_proof": True,
    "compact_preservation_instruction_applied": True,
    "immutable_parent_manifest": parent_manifest,
    "immutable_parent_validation": parent_validation,
    "parent_declared_fingerprint_occurrences_verified": len(parent_declared),
    "parent_declared_deduplicated_paths_verified": len(parent_unique),
    "parent_declared_deduplicated_digest_sha256": digest(parent_unique),
    "parent_original_historical_own_records": 367,
    "earlier_own_unique_chain_records_preserved": len(old_chain),
    "earlier_own_chain_digest_sha256": digest(old_chain),
    "historical_inventory_not_copied": True,
    "exact_reproduction": "Load immutable parent validation earlier_unique_records_preserved plus parent manifest artifacts and its manifest; verify and deduplicate by path. Parent declarations are recursively path/sha256 objects in the two immutable parent JSON records. Use sort-by-path JSON with sort_keys=True,separators=(comma,colon) before SHA256.",
    "direct_accepted_dependency_count": len(accepted_inputs),
    "direct_accepted_dependencies_in": sources,
    "accepted_R6_suffix_verified_byte_identical": True,
    "existing_source_binary_verified": cache,
    "all_obligation_IDs": ids,
    "full_R7A_through_R7E_proofs_present": True,
    "actual_higher_weight_example_original_weight_M1_and_solution_limits_explicit": True,
    "pure_model_realized_in_actual_original_weight_solution": False,
    "new_Diophantine_exclusion_or_unconditional_height_improvement": False,
    "mathematical_program_CAS_scan_test_certificate_or_author_rerun": False,
    "old_shared_Git_cache_edit_spawn_contact_charge_bypass_or_live_native_job": False})

artifacts = [record(PREFIX + suffix) for suffix in [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "sources-v1.json",
    "freeze-v1.py", "input-validation-v1.json"]]
manifest = write_new("freeze-v1.json", {
    "frozen_at_utc": now,
    "status": "COMPLETE candidate proof - unverified; TWO OTHER initially blind WHOLE audits required",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "whole_obligations": len(ids),
    "claims": ["R7A actual odd-lattice normalization and pM phase",
        "R7B divided direct moment and actual character-one product",
        "R7C residual quotient and exact kernel-stability boundary",
        "R7D pure full-orbit rank1 and CONDITIONAL original-weight4^p bound",
        "R7E actual HIGHER-weight Jacobi row-collapse countercheck"],
    "no_original_weight_counterexample_Diophantine_exclusion_annual_or_novelty_claim": True,
    "older_FS_R6_constructor_roles_disclosed": True,
    "primary_methods_attributed_and_new2025_q_gt_p_source_not_imported": True,
    "mathematical_program_CAS_scan_test_certificate_or_author_rerun": False,
    "compact_immutable_parent_preservation": {
        "manifest": parent_manifest, "validation": parent_validation,
        "declared_occurrences_verified": len(parent_declared),
        "declared_deduplicated_paths": len(parent_unique),
        "prior_own_unique_records_preserved": len(old_chain),
        "inventory_reproduction_in": validation},
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 18:20:41UTC",
        "total_used_percent": 54, "window_minutes": 10080,
        "reset_unix": 1792745187, "total_ceiling_percent": 90,
        "review_integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts})
print(json.dumps({"main": artifacts[0], "manifest": manifest,
    "obligations": len(ids), "artifacts": len(artifacts),
    "old_own_unique_preserved": len(old_chain),
    "parent_declared_occurrences_verified": len(parent_declared),
    "parent_declared_deduplicated_paths": len(parent_unique)}, indent=2))
