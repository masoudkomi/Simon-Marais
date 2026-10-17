#!/usr/bin/env python3
"""R7 administrative freeze only: bytes, SHA256, JSON and label counts.

Run from the workspace root. This is not a mathematical program or a
source/certificate rerun. It refuses existing generated outputs and never
writes outside this new owner prefix. Compact parent references preserve
the old inventory without copying it again.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r7-"
GENERATED = ["sources-v1.json", "input-validation-v1.json",
             "freeze-output-v1.json", "freeze-v1.json"]
for name in GENERATED:
    if (ROOT / (PREFIX + name)).exists():
        raise SystemExit("Refusing to overwrite frozen output: " + PREFIX + name)

PARENT_MANIFEST = {
    "path": "problems/2021-B4/notes/reasoning-return-r9-freeze-v1.json",
    "bytes": 4203,
    "sha256": "736bf5eb2c18eb8727c705e747583ca6ac3276d91b4d8829ed9c28277d3d2333",
}
PARENT_VALIDATION = {
    "path": "problems/2021-B4/notes/reasoning-return-r9-input-validation-v1.json",
    "bytes": 9744,
    "sha256": "c2f6d7a623091efb5104ceb71805a1c9fc603e58fbafbc0d0c029382c0d2a741",
}
EXACT_MATH_INPUTS = [
    {"path": "AGENTS.md", "bytes": 4707,
     "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"},
    {"path": "problems/2020-B4/statement.md", "bytes": 2006,
     "sha256": "91c9e7e86eef7bc6a68770f6ee730d18618443304ac3aace5541b42170ac64cc"},
    {"path": "problems/2020-B4/proofs/reviewed-partial-v1.1.md", "bytes": 2207,
     "sha256": "3fcdd2d50c4545b2e466b8a24f5a958fb69f2b0f10cccf19fa4b628ed02a690f"},
    {"path": "problems/2020-B4/proofs/partial-v1.md", "bytes": 8703,
     "sha256": "f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525"},
    {"path": "problems/2020-B4/proofs/reviewed-return-r3-v1.2.md", "bytes": 20446,
     "sha256": "18fc1871219740c528527eb1cfb68c2c1571eba0243e4866b5a8630092a91317"},
    {"path": "problems/2020-B4/proofs/reviewed-reasoning-return-r4-v1.2.md", "bytes": 26219,
     "sha256": "6e1c29498cb3c61f84da80785a2697dc0511718c745098c3624e8a1eb7207493"},
    {"path": "problems/2020-B4/proofs/reviewed-reasoning-return-r5-v1.1.md", "bytes": 26986,
     "sha256": "a466aab8f96fe418497a8ce3dc60afc4bb9554868a08759bdd0492aa0ce7ce2a"},
    {"path": "problems/2020-B4/proofs/reviewed-reasoning-return-r6-v1.1.md", "bytes": 22211,
     "sha256": "472d1bb2676c7139512fe1c0f77793d430a10c06170c9aa811febdf0bec0fd13"},
]
AUTHORITY_PATHS = [
    "problems/2020-B4/reviews/reasoning-return-r4-acceptance.md",
    "problems/2020-B4/reviews/reasoning-return-r4-acceptance.json",
    "problems/2020-B4/reviews/reasoning-return-r4-acceptance-integrity.json",
    "problems/2020-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2020-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2020-B4/reviews/reasoning-return-r5-acceptance-integrity.json",
    "problems/2020-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2020-B4/reviews/reasoning-return-r6-acceptance.json",
    "problems/2020-B4/reviews/reasoning-return-r6-acceptance-integrity.json",
    "problems/2020-B4/notes/reasoning-return-r6-freeze-v1.json",
    "problems/2020-B4/notes/reasoning-return-r6-sources-v1.json",
]
inventory = {}
occurrences = 0

def record(path):
    absolute = (ROOT / path).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Outside workspace input: " + str(path))
    rel = str(absolute.relative_to(ROOT))
    if (rel.startswith("problems/2020-B4/reviews/reasoning-return-r7-")
            or rel.startswith("problems/2024-B4/notes/coordinator-component-saturation-")
            or rel.startswith("problems/2024-B4/reviews/coordinator-component-saturation-")
            or rel.startswith("problems/2025-B4/notes/reasoning-return-r7-")
            or rel.startswith("problems/2025-B4/reviews/reasoning-return-r7-")):
        raise SystemExit("Forbidden new/queued peer or construction input: " + rel)
    body = absolute.read_bytes()
    return {"path": rel, "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest()}

def verify(expected):
    global occurrences
    actual = record(expected["path"])
    normalized = {k: expected[k] for k in ("path", "bytes", "sha256")}
    normalized["path"] = actual["path"]
    if actual != normalized:
        raise SystemExit("Immutable input mismatch: " + str(expected["path"]))
    prior = inventory.get(actual["path"])
    if prior is not None and prior != actual:
        raise SystemExit("Conflicting declared fingerprint: " + actual["path"])
    inventory[actual["path"]] = actual
    occurrences += 1
    return actual

def load_recorded(expected):
    checked = verify(expected)
    return json.loads((ROOT / checked["path"]).read_text())

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

def digest_rows(rows):
    by_path = {r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")}
               for r in rows}
    canonical = [by_path[p] for p in sorted(by_path)]
    encoded = json.dumps(canonical, ensure_ascii=False, sort_keys=True,
                         separators=(",", ":")).encode()
    return {"unique_paths": len(canonical),
            "canonical_sorted_record_array_sha256": hashlib.sha256(encoded).hexdigest(),
            "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), records sorted by path"}

parent = load_recorded(PARENT_MANIFEST)
parent_validation = load_recorded(PARENT_VALIDATION)
binding = parent_validation["compact_immutable_preservation_binding"]
older_manifest_record = binding["immutable_previous_manifest"]
older_validation_record = binding["immutable_previous_validation"]
older_manifest = load_recorded(older_manifest_record)
older_validation = load_recorded(older_validation_record)

# Reconstruct and verify only the old OWN inventory. Unrelated old
# mathematical inventories stay bound by exact immutable metadata hashes.
older_own = {}
for row in (older_validation["older_own_records"]
            + older_manifest["records"] + [older_manifest_record]):
    current = verify(row)
    older_own[current["path"]] = current
if digest_rows(list(older_own.values())) != binding["older_own_records_reverified_including_previous_whole_packet"]:
    raise SystemExit("Parent older-own digest mismatch")
for row in parent["artifacts"] + [PARENT_MANIFEST]:
    current = verify(row)
    older_own[current["path"]] = current
if len(older_own) != 330:
    raise SystemExit("Unexpected older-own path count")

direct_records = [verify(row) for row in EXACT_MATH_INPUTS]
authority_records = []
declared_summaries = []
for path in AUTHORITY_PATHS:
    source_record = verify(record(path))
    direct_records.append(source_record)
    authority_records.append(source_record)
    if path.endswith(".json"):
        obj = json.loads((ROOT / path).read_text())
        declared = list(walk_records(obj))
        for row in declared:
            verify(row)
        declared_summaries.append({
            "immutable_metadata_source": source_record,
            "declared_fingerprint_occurrences_reverified": len(declared),
            "deduplicated_declared_inventory": digest_rows(declared),
        })

prose_names = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
               "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md"]
prose_records = [record(PREFIX + name) for name in prose_names]
main_text = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
if not all(label in main_text for label in
           ("Candidate proof - unverified", "R7A", "R7B", "R7C", "R7D", "R7E")):
    raise SystemExit("Missing complete-candidate claim/status labels")
obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
for number in range(1, 57):
    if obligations.count("|R7-%02d|" % number) != 1:
        raise SystemExit("Missing/duplicate whole obligation label")

now = datetime.now(timezone.utc).isoformat()
telemetry = {
    "at_utc": "2026-10-17 18:28:34 UTC",
    "total_used_percent": 54, "window_minutes": 10080,
    "reset_unix": 1792745187, "ordinary_usage_allowed": True,
    "total_ceiling_percent": 90, "review_integration_reserve": True,
}
parent_binding = {
    "immutable_parent_manifest": PARENT_MANIFEST,
    "immutable_parent_validation": PARENT_VALIDATION,
    "exact_parent_reproduction_manifest": older_manifest_record,
    "exact_parent_reproduction_validation": older_validation_record,
    "parent_recorded_all_input_summary_not_copied": parent_validation["all_reverified_records_deduplicated_summary_only"],
    "parent_recorded_input_occurrences_not_claimed_all_freshly_reverified": parent_validation["fingerprint_occurrences_reverified_this_freeze"],
    "older_own_records_reverified_including_parent_packet": digest_rows(list(older_own.values())),
    "full_historical_inventory_deliberately_not_copied": True,
    "reproduction": "Load exact parent validation's compact_immutable_preservation_binding; reconstruct old own rows from its exact previous validation older_own_records plus previous manifest records and manifest; append exact parent artifacts and manifest. This script re-verifies all330 own paths read-only. Unrelated old inventories remain bound by their immutable metadata hashes.",
}
primary_reads = [
    {"id": "official", "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf",
     "scope": "B4 actual statement on page2; open(b), no preliminary proof"},
    {"id": "Turyn1965", "url": "https://msp.org/pjm/1965/15-1/pjm-v15-n1-p32-p.pdf",
     "scope": "Applicable original printed pp319--327, cyclotomic facts1--4, character/group-ring formulas, multiplier normalization and beginning self-conjugacy discussion",
     "attributed_inputs": "cyclotomic integer basis and unramified Frobenius; Fourier methods classical; R7 exact reconstruction written in full",
     "entire_external_proof_chain_newly_reconstructed": False},
    {"id": "MilneANT", "url": "https://jmilne.org/math/CourseNotes/ANT.pdf",
     "scope": "v3.08 printed pp68--69, ideal norm definition and COMPLETE Proposition4.1(a),(c) statements/proofs",
     "hypotheses": "rings of integers are Dedekind; F/E finite separable degree5 in R7D; extension ideal and principal compatibility"},
    {"id": "ConradIdeals", "url": "https://kconrad.math.uconn.edu/blurbs/gradnumthy/idealfactor.pdf",
     "scope": "Ring-of-integers Dedekind conclusion/Theorem6.9 statement; Definition7.1, COMPLETE Theorem7.2 proof; applicable Theorems7.4--7.5 statements/proofs, PDF pp13--15",
     "foundational_Dedekind_full_proof_chain_newly_reconstructed": False},
    {"id": "Cohen1989", "url": "https://www.researchgate.net/publication/220077727_Generators_in_cyclic_difference_sets",
     "doi": "10.1016/0097-3165(89)90047-2",
     "scope": "Original pp227--231 principally: actual difference-set definition, Theorem1, TWO literal exceptions, translation caveat, early proof and v273 special discussion",
     "complete_sieve_reconstructed": False, "formal_multiset_or_bad_tuple_used_as_actual_D": False},
    {"id": "HuangSchmidt", "url": "https://personal.ntu.edu.sg/bernhard/Publications/pub/Singer.pdf",
     "scope": "Original introduction and Section2 basics/attributed Hall input, beginning classical normalizer statement, roughly printed pp1--4",
     "use": "attributed known Singer existence q5/q16 only; no preliminary construction, universal classicality or uniqueness import"},
    {"id": "Gordon2020", "url": "https://arxiv.org/pdf/2007.07292",
     "scope": "Eight-page text available; applicable Section2 Lemma2/Theorems3--5 statements/proofs plus introductory/table context",
     "unrestricted_realization_or_scan_import": False},
]
for entry in primary_reads:
    entry["retrieved_read_utc_date"] = "2026-10-17"
    entry["native_bytes_sha256"] = None
    entry["native_pdf_downloaded_or_new_cache_written"] = False
limited_leads = [
    {"url": "https://www.sciencedirect.com/science/article/pii/S0022314X98922752",
     "scope": "Schmidt1998 publisher abstract/title only; author class.pdf, exp.pdf, survey2.pdf extraction garbled; no theorem imported"},
    {"url": "https://doi.org/10.1090/S0025-5718-1965-0171368-6",
     "scope": "Hayashi1965 search lead; direct PDF/DOI access failed internally; no order-ten classification or computation imported"},
    {"url": "https://arxiv.org/pdf/math/0304502",
     "scope": "Baumert-Gordon literature context only; no theorem/cutoff imported or source computation replayed"},
]
sources = {
    "created_at_utc": now, "status": "candidate proof - unverified",
    "constructor": "/root/review_2022_complexity_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "official_scope": "2020 B4(b) only; q>=2 new arguments, accepted n2 boundary; no preliminary construction",
    "direct_exact_mathematical_and_authority_inputs": direct_records,
    "actual_local_read_scope": "Full accepted initial header/linked body, repairedR4/R5/R6 bodies and three acceptance Markdown scopes; R6 source record; R3 inherited not claimed wholly freshly reconstructed; JSON/historical inputs may be metadata-only",
    "primary_source_actual_read_records": primary_reads,
    "limited_or_failed_source_leads_not_premises": limited_leads,
    "complete_source_audit": PREFIX + "source-audit-v1.md",
    "compact_immutable_preservation_binding": parent_binding,
    "old_R4_R5_authorship_and_R6_whole_review_roles_disclosed": True,
    "root_broad_target_no_new_R7_proof_inference": True,
    "two_OTHER_fresh_initially_blind_whole_nonconstructor_audits_required": True,
    "all_new_math_is_written_hand_proof_not_numerical_scan": True,
    "no_unrestricted_taut_classification_new_cutoff_or_novelty_claim": True,
    "no_Git_shared_old_cache_edit_spawning_charge_contact_bypass": True,
    "direct_weekly_telemetry": telemetry,
}

def write_new(name, obj):
    target = ROOT / (PREFIX + name)
    if target.exists():
        raise SystemExit("Refusing overwrite: " + str(target))
    target.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

write_new("sources-v1.json", sources)
validation = {
    "checked_at_utc": now, "administrative_only_not_mathematical_evidence": True,
    "status": "candidate proof - unverified; complete meaningful construction checkpoint",
    "unused_prefix_confirmed_before_first_write": True,
    "direct_exact_input_records": direct_records,
    "declared_authority_metadata_reverification_summaries": declared_summaries,
    "compact_immutable_preservation_binding": parent_binding,
    "all_currently_reverified_records_deduplicated_summary_only": digest_rows(list(inventory.values())),
    "fingerprint_occurrences_reverified_this_freeze": occurrences,
    "older_own_unique_paths_preserved": len(older_own),
    "whole_obligations": 56,
    "constructor_prose_records": prose_records,
    "source_native_hashes_not_fabricated_from_web_text": True,
    "no_mathematical_program_CAS_scan_author_rerun_or_certificate": True,
    "no_Git_shared_old_cache_edit_spawning_charge_contact_bypass": True,
    "two_OTHER_whole_independent_audits_still_required": True,
    "direct_weekly_telemetry": telemetry,
}
write_new("input-validation-v1.json", validation)
output = {
    "checked_at_utc": now, "result": "all declared current inputs and330 older own paths match",
    "fingerprint_occurrences_reverified": occurrences,
    "unique_paths_reverified": len(inventory),
    "older_own_unique_paths_preserved": len(older_own),
    "all56_whole_obligation_labels_present_once": True,
    "all_R7A_R7B_R7C_R7D_R7E_status_labels_present": True,
    "historical_inventory_compact_binding_not_copied": True,
    "mathematical_program_or_scan_run": False,
    "no_pending_native_mathematical_job": True,
    "two_OTHER_fresh_whole_audits_required": True,
    "direct_weekly_telemetry": telemetry,
}
write_new("freeze-output-v1.json", output)
artifact_names = prose_names + ["sources-v1.json", "freeze-v1.py",
                                "input-validation-v1.json", "freeze-output-v1.json"]
artifacts = [record(PREFIX + name) for name in artifact_names]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE R7A--R7E construction checkpoint",
    "constructor": "/root/review_2022_complexity_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "claims": [
        "R7A all-divisor integral-phase iff with binary recovery and common T frame",
        "R7B prime-modulus single relative-norm element iff and exact fixed-field/multiplier criterion",
        "R7C separate exact ideal balance, principality and unit-norm obligations",
        "R7D explicit balanced nonprincipal ideal in nonsaturated q5 multiplier fixed field",
        "R7E q16 primitive trace obstruction even with jointly ACTUAL proper quotient images",
    ],
    "whole_obligations": 56,
    "two_OTHER_fresh_initially_blind_whole_nonconstructor_audits_required": True,
    "root_broad_target_only_no_new_R7_proof_inference": True,
    "old_roles_disclosed_no_independent_self_review": True,
    "no_unrestricted_taut_classification_new_cutoff_or_novelty_claim": True,
    "no_mathematical_program_CAS_scan_author_rerun_or_certificate": True,
    "no_Git_shared_old_cache_edit_spawning_charge_contact_bypass": True,
    "compact_parent_manifest": PARENT_MANIFEST,
    "compact_parent_validation": PARENT_VALIDATION,
    "historical_inventory_not_copied": True,
    "older_own_unique_paths_preserved": len(older_own),
    "fingerprint_occurrences_reverified": occurrences,
    "unique_paths_reverified": len(inventory),
    "direct_weekly_telemetry": telemetry,
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
write_new("freeze-v1.json", manifest)
print(json.dumps({"main": record(PREFIX + "candidate-v1.md"),
                  "manifest": record(PREFIX + "freeze-v1.json"),
                  "artifacts": len(artifacts), "whole_obligations": 56,
                  "occurrences_reverified": occurrences,
                  "unique_paths_reverified": len(inventory),
                  "older_own_unique_preserved": len(older_own)}, indent=2))
