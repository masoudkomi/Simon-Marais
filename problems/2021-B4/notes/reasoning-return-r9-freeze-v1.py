#!/usr/bin/env python3
"""R9 administrative freeze only. No mathematics, CAS, scan or source rerun.

Reproduce from the workspace root:
    python3 problems/2021-B4/notes/reasoning-return-r9-freeze-v1.py

This script refuses existing generated outputs. Frozen outputs must never
be overwritten to replay it. All inputs are named immutable parent records;
old files are read only for exact byte/hash preservation, not reinterpreted.
"""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r9-"
OUTPUT_NAMES = ["sources-v1.json", "input-validation-v1.json",
                "freeze-output-v1.json", "freeze-v1.json"]
for name in OUTPUT_NAMES:
    if (ROOT / (PREFIX + name)).exists():
        raise SystemExit("Refusing to overwrite frozen output: " + PREFIX + name)

PREVIOUS_MANIFEST = {
    "path": "problems/2022-B4/reviews/reasoning-return-r7-review-2-manifest-v1.json",
    "bytes": 3421,
    "sha256": "c36de81e3d4dcccf125fe959ae1b544527c305d2d68ecf93b293440ed117597d",
}
PREVIOUS_VALIDATION = {
    "path": "problems/2022-B4/reviews/reasoning-return-r7-review-2-input-validation-v1.json",
    "bytes": 355375,
    "sha256": "b59801e5ad40536355d3ed7c0aeeaceac5f28de785757e439b24251dd52c132b",
}
EXACT_ACCEPTED = [
    {"path": "AGENTS.md", "bytes": 4707,
     "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"},
    {"path": "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
     "bytes": 19921,
     "sha256": "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"},
    {"path": "problems/2021-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
     "bytes": 20531,
     "sha256": "4932a051d4a296b8a73d51c9a1cf07b7de52b6bd710b4fbeb113ee2f8c4fa1ea"},
    {"path": "problems/2021-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
     "bytes": 20411,
     "sha256": "f15db94cc97ccf370298fad58364810cb0ff7d0a3493d52b588cf3da2119da96"},
    {"path": "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
     "bytes": 23675,
     "sha256": "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d"},
]
R8_FREEZE = {
    "path": "problems/2021-B4/notes/reasoning-return-r8-freeze-v1.json",
    "bytes": 3602,
    "sha256": "9d366b0c0eee1a56dae269a2aeb197627516d00f2d87d17a4d6c93304b1919b8",
}
DIRECT_CONTEXT = [
    "problems/2021-B4/statement.md",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.md",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.json",
    "problems/2021-B4/notes/reasoning-return-r8-candidate-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-obligations-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-failed-routes-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-source-audit-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-worklog-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-sources-v1.json",
    "problems/2021-B4/notes/reasoning-return-r8-input-validation-v1.json",
]

inventory = {}
occurrences = 0

def record(path):
    rel = str(path)
    absolute = (ROOT / rel).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Input outside authorized workspace: " + rel)
    rel = str(absolute.relative_to(ROOT))
    if rel.startswith("problems/2021-B4/reviews/reasoning-return-r9-"):
        raise SystemExit("No new R9 peer finding may be opened during construction")
    payload = absolute.read_bytes()
    return {"path": rel, "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest()}

def verify(row):
    global occurrences
    actual = record(row["path"])
    expected = {k: row[k] for k in ("path", "bytes", "sha256")}
    expected["path"] = actual["path"]
    if actual != expected:
        raise SystemExit("Preservation mismatch: " + str(row["path"]))
    occurrences += 1
    previous = inventory.get(actual["path"])
    if previous is not None and previous != actual:
        raise SystemExit("Conflicting historical fingerprints: " + actual["path"])
    inventory[actual["path"]] = actual
    return actual

def walk_records(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and isinstance(obj.get("bytes"), int)
                and isinstance(obj.get("sha256"), str)
                and len(obj["sha256"]) == 64):
            yield obj
        for value in obj.values():
            yield from walk_records(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk_records(value)

def load_recorded(row):
    checked = verify(row)
    return json.loads((ROOT / checked["path"]).read_text())

def digest_rows(rows):
    # A reproducible administrative inventory fingerprint, not a math certificate.
    unique = {r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")}
              for r in rows}
    canonical = [unique[p] for p in sorted(unique)]
    body = json.dumps(canonical, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode()
    return {"unique_paths": len(canonical),
            "canonical_sorted_record_array_sha256": hashlib.sha256(body).hexdigest(),
            "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), records sorted by path"}

old_manifest = load_recorded(PREVIOUS_MANIFEST)
old_validation = load_recorded(PREVIOUS_VALIDATION)
parent_inputs = old_validation["deduplicated_all_verified_input_records"]
for row in parent_inputs:
    verify(row)

older_own = {}
for row in (old_validation["older_own_records"]
            + old_manifest["records"] + [PREVIOUS_MANIFEST]):
    checked = verify(row)
    older_own[checked["path"]] = checked

for row in EXACT_ACCEPTED:
    verify(row)
r8_freeze = load_recorded(R8_FREEZE)
for row in r8_freeze["artifacts"]:
    verify(row)

direct_records = EXACT_ACCEPTED + [R8_FREEZE]
for path in DIRECT_CONTEXT:
    current = record(path)
    verify(current)
    direct_records.append(current)

declared_sources = [
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.json",
    "problems/2021-B4/notes/reasoning-return-r8-freeze-v1.json",
    "problems/2021-B4/notes/reasoning-return-r8-sources-v1.json",
    "problems/2021-B4/notes/reasoning-return-r8-input-validation-v1.json",
]
declared_summaries = []
for path in declared_sources:
    source_row = verify(record(path))
    rows = list(walk_records(json.loads((ROOT / path).read_text())))
    for row in rows:
        verify(row)
    declared_summaries.append({"immutable_metadata_source": source_row,
                               "declared_fingerprint_occurrences_reverified": len(rows),
                               "deduplicated_declared_inventory": digest_rows(rows)})

prose_names = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
               "source-audit-v1.md", "constructor-checks-v1.md", "worklog-v1.md"]
prose_records = [record(PREFIX + name) for name in prose_names]
body = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
if not all(label in body for label in ("Candidate proof - unverified", "R9A", "R9B", "R9C", "R9D")):
    raise SystemExit("Missing candidate/claim labels")
obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
for number in range(1, 47):
    if obligations.count("|R9-%02d|" % number) != 1:
        raise SystemExit("Missing/duplicate whole obligation label")

now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 18:03:46 UTC",
             "total_used_percent": 53, "window_minutes": 10080,
             "reset_unix": 1792745187, "ordinary_usage_allowed": True,
             "total_ceiling_percent": 90, "integration_reserve": True}
parent_binding = {
    "immutable_previous_manifest": PREVIOUS_MANIFEST,
    "immutable_previous_validation": PREVIOUS_VALIDATION,
    "parent_original_fingerprint_occurrences_recorded": old_manifest["source_document_fingerprint_occurrences_verified"],
    "parent_deduplicated_inputs_reverified": digest_rows(parent_inputs),
    "older_own_records_reverified_including_previous_whole_packet": digest_rows(list(older_own.values())),
    "full_inventory_deliberately_not_copied": True,
    "reproduction": "Use the exact parent validation's deduplicated_all_verified_input_records and older_own_records, plus the exact parent manifest records and manifest itself; this script re-verifies them read-only.",
}

sources = {
    "created_at_utc": now, "status": "candidate proof - unverified",
    "constructor": "/root/review_2022_complexity_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "official_scope": "2021 B4(b) only; actual rational coefficients and rational derivative common values; no preliminary proof",
    "direct_mathematical_and_authority_inputs": direct_records,
    "direct_read_limits": "Complete accepted R5,R6,R7,R8 bodies/headers and R8 acceptance/source/obligation/failure/log records; unrelated preserved mathematical content is not claimed freshly read",
    "new_attributed_theorem_import": {
        "authors": "K. Atkinson and A. Sharma",
        "title": "A partial characterization of poised Hermite-Birkhoff interpolation problems",
        "citation": "SIAM J. Numer. Anal. 6(2)(1969),230-235, Theorem2",
        "url": "https://homepage.math.uiowa.edu/~atkinson/papers/HB_interp.pdf",
        "actual_read_scope": "All six source pages as web-extracted text, definitions, Theorem2 and complete published proof",
        "published_proof_attributed_import_not_new_external_formalization": True,
        "conjectured_converse_used": False,
        "all_polynomial_roots_real_hypothesis_used": False,
        "native_bytes_sha256": None,
        "native_pdf_not_downloaded_or_written": True,
    },
    "primary_context_reads": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
         "scope": "page2 B4 actual hypothesis and(b), no preliminary proof", "native_bytes_sha256": None},
        {"url": "https://arxiv.org/pdf/1208.5404",
         "authors": "Castryck-Laterveer-Ounaies",
         "scope": "normalized equation7; Section3.4 equations9-10/Lemma17; complete Proposition19/unramified qualification; Proposition15 context",
         "all_root_rational_unramified_theorem_applied_to_only_rational_witnesses": False,
         "entire_external_paper_claimed_reconstructed": False, "native_bytes_sha256": None},
        {"url": "https://arxiv.org/pdf/1806.09561", "author": "Cesar Massri",
         "scope": "v6 abstract/intro, Section3 identities through Proposition3.5, Definition5.3 valuation ring, Section7 displayed lemmas/theorems/proofs through7.10",
         "three_recycled_theorem_extended_to_four": False, "finite_computation_rerun_or_independently_certified": False,
         "valuation_ring_R_not_confused_with_reals": True, "native_bytes_sha256": None},
        {"url": "https://arxiv.org/html/2608.14726v1", "author": "Mohammad F. Marashdeh",
         "scope": "introductory support/scenario definitions and TheoremsB/C/D statements, actual multi-root limit",
         "new_four_value_exclusion_import": False, "entire_external_proof_claimed_reconstructed": False,
         "native_bytes_sha256": None},
    ],
    "root_broad_target_only_no_new_R9_proof_inference": True,
    "constructor_old_single_center_return_R5_R6_R7_review_roles_disclosed": True,
    "two_OTHER_fresh_whole_nonconstructor_audits_required": True,
    "new_result_claims": ["R9A every selection has at least four odd positive real-interior runs",
                          "R9B at least four whole gcd supports forced into real interior pair",
                          "R9C exact actual cubic collision depth and weighted lower bound",
                          "R9D stated collision-depth nonunit-essential-center criterion"],
    "no_full_branch_degree20_annual_Q19_or_Q_lift_novelty_claim": True,
    "mathematical_executable_CAS_scan_certificate_or_author_rerun": False,
    "compact_immutable_preservation_binding": parent_binding,
    "direct_weekly_telemetry": telemetry,
}

def write_new(name, obj):
    with (ROOT / (PREFIX + name)).open("x") as output:
        json.dump(obj, output, ensure_ascii=False, indent=2)
        output.write("\n")

write_new("sources-v1.json", sources)
validation = {
    "checked_at_utc": now, "constructor": "/root/review_2022_complexity_r2",
    "metadata_only_not_mathematical_evidence": True,
    "status": "candidate proof - unverified; complete construction checkpoint, no promotion",
    "requested_settings": sources["requested_settings"],
    "independently_verified_effective_settings": None,
    "unused_prefix_confirmed_before_first_write": True,
    "direct_exact_input_records": direct_records,
    "declared_parent_metadata_reverification_summaries": declared_summaries,
    "compact_immutable_preservation_binding": parent_binding,
    "all_reverified_records_deduplicated_summary_only": digest_rows(list(inventory.values())),
    "fingerprint_occurrences_reverified_this_freeze": occurrences,
    "older_own_unique_paths_preserved": len(older_own),
    "whole_obligations": 46,
    "constructor_prose_records": prose_records,
    "mathematical_program_CAS_scan_native_job_or_constructor_rerun": False,
    "Git_shared_old_file_cache_edit_spawning_charge_contact_bypass": False,
    "two_OTHER_whole_independent_audits_still_required": True,
    "direct_weekly_telemetry": telemetry,
}
write_new("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "status": "complete meaningful candidate construction checkpoint - unverified",
    "candidate": record(PREFIX + "candidate-v1.md"),
    "all46_obligation_labels_present": True,
    "fingerprint_occurrences_reverified": occurrences,
    "unique_paths_reverified": len(inventory),
    "older_own_unique_paths_preserved": len(older_own),
    "historical_inventory_bound_not_copied": True,
    "validation": record(PREFIX + "input-validation-v1.json"),
    "two_OTHER_whole_audits_required_before_promotion": True,
    "mathematical_computation": False,
}
write_new("freeze-output-v1.json", output)
artifact_names = prose_names + ["sources-v1.json", "freeze-v1.py",
                               "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; complete meaningful construction checkpoint",
    "constructor": "/root/review_2022_complexity_r2",
    "requested_settings": sources["requested_settings"],
    "independently_verified_effective_settings": None,
    "claims": sources["new_result_claims"],
    "whole_obligations": 46,
    "new_external_theorem": "Atkinson-Sharma1969 Theorem2, sufficient conservative/Pólya criterion only",
    "all_root_real_hypothesis_or_converse_conjecture_imported": False,
    "actual_rational_double_branch_and_complete_accepted_R8_retained": True,
    "root_broad_assignment_no_new_proof_inference": True,
    "two_OTHER_fresh_initially_blind_whole_nonconstructor_audits_required": True,
    "no_full_branch_degree20_annual_rational_lift_or_novelty_claim": True,
    "no_math_code_CAS_scan_old_certificate_author_rerun": True,
    "no_Git_shared_old_cache_edit_spawn_charge_contact_bypass": True,
    "old_unique_paths_preserved": len(older_own),
    "fingerprint_occurrences_reverified": occurrences,
    "unique_paths_reverified": len(inventory),
    "compact_parent_manifest": PREVIOUS_MANIFEST,
    "compact_parent_validation": PREVIOUS_VALIDATION,
    "historical_inventory_not_copied": True,
    "direct_weekly_telemetry": telemetry,
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "artifacts": [record(PREFIX + name) for name in artifact_names],
}
write_new("freeze-v1.json", manifest)
print(json.dumps({"manifest": record(PREFIX + "freeze-v1.json"), **output},
                 ensure_ascii=False, indent=2))
