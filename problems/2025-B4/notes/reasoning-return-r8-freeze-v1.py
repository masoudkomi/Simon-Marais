#!/usr/bin/env python3
"""Administrative R8 constructor freeze only; no mathematical algorithm.

No primes, ratios, phase matrices, tilings, counts, CAS, source certificates
or older scripts are evaluated. Only files/JSON/fingerprints/obligation IDs.
All outputs are exclusive NEW creations below the assigned R8 notes prefix.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/notes/reasoning-return-r8-"
PARENT_MANIFEST = {
    "path": "problems/2017-B4/reviews/reasoning-value-return-r4-review-2-manifest-v1.json",
    "bytes": 4083,
    "sha256": "572f3cb6a412c56c499047974aa7b360358198bfd1cefb32128f295b0da83476"}
PARENT_VALIDATION = {
    "path": "problems/2017-B4/reviews/reasoning-value-return-r4-review-2-input-validation-v1.json",
    "bytes": 19919,
    "sha256": "f6001c230523eb97e2ad319e83d478e34c8ed8b2991fe0f909d9e09a0f4e9130"}
DIRECT = [
    {"path": "AGENTS.md", "bytes": 4707,
     "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"},
    {"path": "problems/2025-B4/statement.md", "bytes": 2024,
     "sha256": "af0075dd635e8e4d31bb3ae9148d1731a7fbb57c06cf104763332e1496673f59"},
    {"path": "problems/2025-B4/proofs/reviewed-original-weight-universal-v1.1.md", "bytes": 22590,
     "sha256": "bb4d3f1b378f8062ba5d1f6e8ee0a197f0f09f01e4f97b7abe8195a9627cd2c4"},
    {"path": "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md", "bytes": 28748,
     "sha256": "4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a"},
    {"path": "problems/2025-B4/proofs/reviewed-reasoning-return-r7-v1.1.md", "bytes": 26875,
     "sha256": "f3bdf6dd49210954e619daec5ef50ef7bc288777230127c0c9d086f46af3634d"},
    {"path": "problems/2025-B4/proofs/reviewed-reciprocal-kernel-v1.1.md", "bytes": 12969,
     "sha256": "41d1882ce1efa59f24b5d76636125edeb037e712add8ee93632c2aa3d8030e60"},
    {"path": "problems/2025-B4/notes/reasoning-return-r7-candidate-v1.md", "bytes": 24429,
     "sha256": "ee144e23b5a40e828f3e4f74790f5ec1394b4a9462609a8102f8b3a16465c8e0"},
    {"path": "problems/2025-B4/notes/reasoning-return-r7-freeze-v1.json", "bytes": 3864,
     "sha256": "0f3dc3419bc3f7a031a38f5d5d9448187cad39fe62588e4d5f43967e9c644174"},
    {"path": "problems/2025-B4/notes/reasoning-return-r7-sources-v1.json", "bytes": 5653,
     "sha256": "c1c89cd63f746412ed39b5644a653e583c614914c99f5d0cf8aaf1a5d7862126"},
    {"path": "problems/2025-B4/notes/reasoning-return-r7-failed-routes-v1.md", "bytes": 4762,
     "sha256": "d515d88d23d2b40343677b22595a38b9462eceb90c7f2a0e1acbc16919257555"},
    {"path": "problems/2025-B4/reviews/original-weight-universal-acceptance.md", "bytes": 3261,
     "sha256": "52b9cc1fedf397eeb764189144805cd330178fa9eb6c805eabf7e43de405c936"},
    {"path": "problems/2025-B4/reviews/original-weight-universal-acceptance.json", "bytes": 2537,
     "sha256": "73c04300bef8cfd0db3903c862af47dbdab5f859dc1a85d2cbb0c5a96fa6fa49"},
    {"path": "problems/2025-B4/reviews/original-weight-universal-acceptance-integrity.json", "bytes": 1966,
     "sha256": "a11556552df0ca9d9822eaf325790e217b39bff171e6a4ecce8e997a8229d19b"},
    {"path": "problems/2025-B4/reviews/reasoning-return-r6-acceptance.md", "bytes": 3261,
     "sha256": "9eec12d169ef7c33efeeb1254dff467990b41822707db0086a4b14016544cf20"},
    {"path": "problems/2025-B4/reviews/reasoning-return-r6-acceptance.json", "bytes": 2483,
     "sha256": "9d32b3f32be2bf758dc2bbe0182c11a6597a96139d0bd3b24680ba7041d56135"},
    {"path": "problems/2025-B4/reviews/reasoning-return-r6-acceptance-integrity.json", "bytes": 1918,
     "sha256": "16b3a89c3f990a81da68e428f7685631816b0ef106ec0dc8b7c5ea9aed9ad077"},
    {"path": "problems/2025-B4/reviews/reasoning-return-r7-acceptance.md", "bytes": 2544,
     "sha256": "19946bfbb0df58428c7c14d32cf7a5fd036615479b1adfb6177c5e38c5980bb8"},
    {"path": "problems/2025-B4/reviews/reasoning-return-r7-acceptance.json", "bytes": 2604,
     "sha256": "0f9d4d01ba72b582768d89c142d1c8004417f0ab9e89b0a1213f78add921cac2"},
    {"path": "problems/2025-B4/reviews/reasoning-return-r7-acceptance-integrity.json", "bytes": 2172,
     "sha256": "51a024505f5e7f594bf3fc7c25d752069a56161913be504c1978b50e672a46f8"},
]
for suffix in ("sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "freeze-v1.json"):
    if (ROOT / (PREFIX + suffix)).exists():
        raise SystemExit("Refusing frozen output overwrite: " + PREFIX + suffix)
inventory = {}
occurrences = 0


def rec(path):
    absolute = (ROOT / path).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Outside workspace")
    rel = str(absolute.relative_to(ROOT))
    if rel.startswith("problems/2025-B4/reviews/reasoning-return-r8-"):
        raise SystemExit("No NEW R8 peer findings: " + rel)
    data = absolute.read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    global occurrences
    actual = rec(expected["path"])
    if actual["sha256"] != expected["sha256"]:
        raise SystemExit("Immutable SHA mismatch: " + actual["path"])
    if expected.get("bytes") is not None and actual["bytes"] != expected["bytes"]:
        raise SystemExit("Immutable length mismatch: " + actual["path"])
    if actual["path"] in inventory and inventory[actual["path"]] != actual:
        raise SystemExit("Conflicting immutable rows")
    inventory[actual["path"]] = actual
    occurrences += 1
    return actual


def load(row):
    return json.loads((ROOT / verify(row)["path"]).read_text())


def rows(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("path"), str) and re.fullmatch("[0-9a-f]{64}", str(obj.get("sha256", ""))):
            yield obj
        for key, value in obj.items():
            if key == "artifacts" and isinstance(value, dict):
                for path, sha in value.items():
                    if isinstance(path, str) and re.fullmatch("[0-9a-f]{64}", str(sha)):
                        yield {"path": path, "sha256": sha}
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)


def digest(records):
    unique = {r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")} for r in records}
    ordered = [unique[p] for p in sorted(unique)]
    data = json.dumps(ordered, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return {"unique_paths": len(ordered),
            "canonical_sorted_record_array_sha256": hashlib.sha256(data).hexdigest(),
            "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), records sorted by path"}


# Compact immutable preservation of own old packets, exact reproduction chain.
parent = load(PARENT_MANIFEST)
parent_val = load(PARENT_VALIDATION)
r4bind = parent_val["compact_immutable_parent_binding"]
r7_manifest_row = r4bind["immutable_parent_manifest"]
r7_validation_row = r4bind["immutable_parent_validation"]
r7 = load(r7_manifest_row)
r7val = load(r7_validation_row)
r7bind = r7val["compact_immutable_parent_binding"]
cs_manifest_row = r7bind["immutable_parent_manifest"]
cs_validation_row = r7bind["immutable_parent_validation"]
cs = load(cs_manifest_row)
csval = load(cs_validation_row)
pb = csval["compact_immutable_parent_binding"]
old_manifest_row = pb["immutable_full_inventory_manifest_for_reproduction"]
old_validation_row = pb["immutable_full_inventory_validation_for_reproduction"]
old = load(old_manifest_row)
oldval = load(old_validation_row)
older_own = {}
for row in oldval["older_own_records"] + old["records"] + [old_manifest_row]:
    actual = verify(row)
    older_own[actual["path"]] = actual
for manifest_row in (pb["immutable_R9_manifest_for_reproduction"], pb["immutable_previous_manifest"]):
    doc = load(manifest_row)
    for row in doc["artifacts"] + [manifest_row]:
        actual = verify(row)
        older_own[actual["path"]] = actual
verify(pb["immutable_R9_validation_for_reproduction"])
verify(pb["immutable_previous_validation"])
if digest(list(older_own.values())) != pb["older_own_preserved_summary"]:
    raise SystemExit("341-path preservation mismatch")
for row in cs["artifacts"] + [cs_manifest_row]:
    actual = verify(row)
    older_own[actual["path"]] = actual
if digest(list(older_own.values())) != r7bind["older_own_preserved_summary"]:
    raise SystemExit("349-path preservation mismatch")
for row in r7["artifacts"] + [r7_manifest_row]:
    actual = verify(row)
    older_own[actual["path"]] = actual
if digest(list(older_own.values())) != r4bind["older_own_preserved_summary"]:
    raise SystemExit("357-path preservation mismatch")
for row in parent["artifacts"] + [PARENT_MANIFEST]:
    actual = verify(row)
    older_own[actual["path"]] = actual
if len(older_own) != 365:
    raise SystemExit("Unexpected365-path preservation count")

direct = [verify(row) for row in DIRECT]
authorities = []
for name in ("original-weight-universal", "reasoning-return-r6", "reasoning-return-r7"):
    base = "problems/2025-B4/reviews/" + name + "-acceptance"
    md = verify(rec(base + ".md"))
    authority = verify(rec(base + ".json"))
    obj = json.loads((ROOT / authority["path"]).read_text())
    declared = [verify(row) for row in rows(obj)]
    integrity = verify(rec(base + "-integrity.json"))
    authorities.append({"acceptance_markdown": md, "immutable_authority": authority,
        "immutable_integrity_summary": integrity,
        "necessary_declared_fingerprint_occurrences_reverified": len(declared),
        "necessary_declared_deduplicated_summary": digest(declared),
        "prior_full_inventory_occurrences_recorded_not_replayed": obj.get("record_occurrences_verified"),
        "prior_full_inventory_paths_recorded_not_replayed": obj.get("unique_paths_verified")})
r7_constructor = json.loads((ROOT / "problems/2025-B4/notes/reasoning-return-r7-freeze-v1.json").read_text())
r7_records = [verify(row) for row in r7_constructor["artifacts"]]
if not (ROOT / "problems/2025-B4/proofs/reviewed-reasoning-return-r7-v1.1.md").read_bytes().endswith(
        (ROOT / "problems/2025-B4/notes/reasoning-return-r7-candidate-v1.md").read_bytes()):
    raise SystemExit("Accepted R7 exact suffix changed")

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
for number in range(1, 49):
    if obligations.count("|R8-%02d|" % number) != 1:
        raise SystemExit("Missing/duplicate whole obligation")
main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
for claim in ("R8A", "R8B", "R8C", "R8D"):
    if claim not in main:
        raise SystemExit("Missing claim")
if "Candidate proof - unverified" not in main:
    raise SystemExit("Missing unverified status")
prose_names = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
               "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md"]
prose = [rec(PREFIX + name) for name in prose_names]
for record in prose:
    if record["bytes"] < 2500:
        raise SystemExit("Incomplete prose companion")
now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 19:25:31 UTC", "total_used_percent": 59,
             "window_minutes": 10080, "reset_unix": 1792745187,
             "spend_control_reached": False, "rate_limit_reached_type": None,
             "total_ceiling_percent": 90, "review_integration_reserve": True}
binding = {"immutable_parent_manifest": PARENT_MANIFEST,
           "immutable_parent_validation": PARENT_VALIDATION,
           "older_own_preserved_summary": digest(list(older_own.values())),
           "historical_inventory_not_copied": True,
           "reproduction": "Follow exact2017R4 R2 validation to2025R7 R2, then CS validation; reconstruct341 paths from its full older2022 inventory and R9/2020R7 manifests; append CS8,2025R7 eight,2017R4 eight, yielding365. Every old own path reverified; inventory not copied."}
primary_reads = [
    {"title": "Official2025 Paper B p2 B4(b)",
     "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf",
     "actual_fresh_scope": "All-integer open(b) domain and indexing only; no preliminary proof"},
    {"title": "Mihailescu, Class Number Conditions for the Diagonal Case of the Equation of Nagell and Ljunggren",
     "doi": "10.1007/978-3-211-74280-8_15",
     "url": "https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren",
     "version": "Author text Version2.0 September17,2007; published2008",
     "actual_fresh_scope": "Jacobi2.2 definitions/ideal/normalization, selected binomial majorant, COMPLETE4.2 and4.3, Theorem3 statement",
     "role": "Attributed classical matched-prime ideal input through accepted R6 and existing phase/two-list/norm methodology; no full external theorem or rank repair import"},
    {"title": "Bartolome--Mihailescu, On the equation X^n-1=BZ^n", "version": "1412.5798v2",
     "url": "https://arxiv.org/pdf/1412.5798v2",
     "actual_fresh_scope": "Moment/selection2.6--2.7, reciprocal2.8--2.10 statements/relevant proofs, COMPLETE Appendices5.1/5.1.1/5.2",
     "role": "Existing moment/selection/bouquet methodology; no prescribed-target/whole binary-Thue theorem import"},
    {"title": "Liu--Mihailescu, An alternative proof of the Catalan conjecture(2025)",
     "doi": "10.31926/but.mif.2025.5.67.1.12",
     "url": "https://webbut.unitbv.ro/index.php/Series_III/article/download/8768/6170/17457",
     "actual_fresh_scope": "Introduction/q>p/Prop1 statement, actualSection3 pair-module/quotient proof, subsequent applications and finalRemark2; not fresh all12 pages",
     "role": "Context only; q=p/q<p expressly deferred; no character/counting/Diophantine import or source refutation"}]
for row in primary_reads:
    row.update(read_date_utc="2026-10-17", new_native_binary_hash=None,
               native_download_or_cache_write=False)


def new(suffix, obj):
    with (ROOT / (PREFIX + suffix)).open("x") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


new("sources-v1.json", {"frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE new constructor checkpoint",
    "constructor": "/root/review_2022_complexity_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "exact_direct_inputs_and_context": direct,
    "complete_fresh_accepted_bodies": ["UW", "R6", "R7"],
    "complete_fresh_context_body_not_a_new_infinity_chart_premise": "RK",
    "complete_fresh_acceptance_MD": ["original-weight-universal", "reasoning-return-r6", "reasoning-return-r7"],
    "accepted_authority_compact_summaries": authorities,
    "accepted_R7_exact_eight_artifact_packet_verified_not_all_claimed_fresh_math_reads": r7_records,
    "accepted_R7_candidate_suffix_byte_identical": True,
    "primary_actual_reads": primary_reads,
    "old_UW_authorship_root_exploratory_contribution_and_R6_R7_review_roles_disclosed": True,
    "old_own_accepted_premise_not_independently_self_recertified": True,
    "root_new_R8_proof_inference_or_constant_contribution": False,
    "new_R8_requires_two_OTHER_initially_blind_WHOLE_audits": True,
    "new_R8_peer_findings_read": False,
    "compact_immutable_parent_binding": binding,
    "mathematical_code_CAS_prime_phase_count_scan_certificate_or_author_rerun": False,
    "Git_shared_old_bytes_cache_write_spawn_charge_contact_or_bypass": False,
    "official_annual_classification_new_exclusion_practical_height_improvement_or_novelty": False,
    "direct_weekly_telemetry": telemetry})
new("input-validation-v1.json", {"frozen_at_utc": now,
    "administrative_only_not_mathematical_evidence": True,
    "exact_direct_records": direct, "accepted_authority_compact_summaries": authorities,
    "accepted_R7_eight_original_artifact_records": r7_records,
    "compact_immutable_parent_binding": binding,
    "older_own_unique_paths_preserved": len(older_own),
    "current_fingerprint_occurrences_reverified": occurrences,
    "current_verified_records_deduplicated_summary_only": digest(list(inventory.values())),
    "all48_author_obligations_once": True, "new_prose_records": prose,
    "no_theoretical_proof_algorithm_execution_or_math_code_CAS_scan_rerun": True,
    "no_old_shared_Git_cache_edit": True, "new_peer_R8_findings_read": False,
    "candidate_unverified_two_OTHER_whole_audits_required": True,
    "direct_weekly_telemetry": telemetry})
new("freeze-output-v1.json", {"frozen_at_utc": now,
    "status": "COMPLETE constructor freeze; candidate proof - unverified",
    "claims": ["R8A quantitative original-weight orbits", "R8B actual bounded real cancellation",
               "R8C nonzero formal leading-order certificate", "R8D BOTH arithmetic branches"],
    "whole_obligations": 48, "older_own_unique_paths_preserved": len(older_own),
    "verified_fingerprint_occurrences": occurrences, "deduplicated_verified_paths": len(inventory),
    "mathematical_code_CAS_scan_QE_count_or_author_rerun": False,
    "new_annual_exclusion_useful_unconditional_height_improvement_or_novelty_claim": False,
    "two_OTHER_fresh_WHOLE_audits_and_coordinator_reconciliation_required": True})
artifacts = [rec(PREFIX + name) for name in prose_names +
             ["sources-v1.json", "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]]
new("freeze-v1.json", {"frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE constructor checkpoint",
    "constructor": "/root/review_2022_complexity_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "claims": ["R8A quantitative actual original-weight orbit lower bound",
               "R8B actual phase-uniform real homogeneous cancellation and integral bounds",
               "R8C nonzero canonical formal series with finite leading-order/size witness",
               "R8D signed nonzero/zero arithmetic branch bounds, no useful new unconditional improvement"],
    "whole_obligations": 48,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_WHOLE_audits": True,
    "root_new_R8_proof_inference_or_constant_contribution": False,
    "old_UW_authorship_and_other_roles_disclosed_no_independent_self_recertification": True,
    "only_assigned_unused_R8_prefix_written": True,
    "mathematical_code_CAS_prime_phase_scan_certificate_or_author_rerun": False,
    "new_R8_peer_findings_read": False,
    "new_annual_classification_exclusion_practical_height_improvement_or_novelty": False,
    "all_old_bytes_preserved_compact_parent_binding": True,
    "compact_parent_manifest": PARENT_MANIFEST, "compact_parent_validation": PARENT_VALIDATION,
    "older_own_unique_paths_preserved": len(older_own),
    "record_occurrences_reverified": occurrences, "unique_paths_reverified": len(inventory),
    "Git_shared_old_bytes_cache_write_spawn_charge_contact_or_bypass": False,
    "direct_weekly_telemetry": telemetry,
    "command": "python3 " + PREFIX + "freeze-v1.py", "artifacts": artifacts})
print(json.dumps({"main": rec(PREFIX + "candidate-v1.md"),
                  "manifest": rec(PREFIX + "freeze-v1.json"), "artifacts": len(artifacts),
                  "whole_obligations": 48, "verified_occurrences": occurrences,
                  "unique_paths": len(inventory), "older_own_paths": len(older_own)}, indent=2))
