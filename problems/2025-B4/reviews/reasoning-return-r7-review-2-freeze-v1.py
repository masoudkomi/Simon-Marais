#!/usr/bin/env python3
"""Administrative WHOLE R7 R2 freeze. No mathematical computation.

This reads exact fingerprints, JSON and obligation labels only. It never
executes a constructor/older script or opens a NEW peer R7 finding.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-return-r7-review-2-"
TP = "problems/2025-B4/notes/reasoning-return-r7-"
TARGET = {"path": TP + "candidate-v1.md", "bytes": 24429,
          "sha256": "ee144e23b5a40e828f3e4f74790f5ec1394b4a9462609a8102f8b3a16465c8e0"}
TARGET_FREEZE = {"path": TP + "freeze-v1.json", "bytes": 3864,
                 "sha256": "0f3dc3419bc3f7a031a38f5d5d9448187cad39fe62588e4d5f43967e9c644174"}
PARENT_MANIFEST = {
    "path": "problems/2024-B4/reviews/coordinator-component-saturation-r1-review-2-manifest-v1.json",
    "bytes": 4039, "sha256": "287e5e85ecf37f74b7213c5bb4570889b4e613726c3248cffbfa8290260b05e2"}
PARENT_VALIDATION = {
    "path": "problems/2024-B4/reviews/coordinator-component-saturation-r1-review-2-input-validation-v1.json",
    "bytes": 11799, "sha256": "bd2dbaf3b35fdad2496f9c085c46f12e5de4de4adba5361e09b090d536177ec5"}
for suffix in ("sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json", "manifest-v1.json"):
    if (ROOT / (PREFIX + suffix)).exists():
        raise SystemExit("Refusing frozen output overwrite: " + PREFIX + suffix)
inventory = {}
occurrences = 0

def rec(path):
    absolute = (ROOT / path).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Outside workspace input")
    rel = str(absolute.relative_to(ROOT))
    if ((rel.startswith("problems/2025-B4/reviews/reasoning-return-r7-")
         and not rel.startswith(PREFIX))
            or rel.startswith("problems/2017-B4/notes/reasoning-value-return-r4-")
            or rel.startswith("problems/2017-B4/reviews/reasoning-value-return-r4-")):
        raise SystemExit("Forbidden NEW peer or queued packet: " + rel)
    b = absolute.read_bytes()
    return {"path": rel, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def verify(expected):
    global occurrences
    actual = rec(expected["path"])
    if actual["sha256"] != expected["sha256"] or ("bytes" in expected and actual["bytes"] != expected["bytes"]):
        raise SystemExit("Immutable fingerprint mismatch: " + actual["path"])
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
        for value in obj.values():
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)

def digest(records):
    unique = {r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")} for r in records}
    canonical = [unique[p] for p in sorted(unique)]
    b = json.dumps(canonical, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return {"unique_paths": len(canonical), "canonical_sorted_record_array_sha256": hashlib.sha256(b).hexdigest(),
            "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), records sorted by path"}

parent = load(PARENT_MANIFEST)
parent_val = load(PARENT_VALIDATION)
pb = parent_val["compact_immutable_parent_binding"]
old_manifest_row = pb["immutable_full_inventory_manifest_for_reproduction"]
old_validation_row = pb["immutable_full_inventory_validation_for_reproduction"]
old = load(old_manifest_row)
old_val = load(old_validation_row)
older_own = {}
for row in old_val["older_own_records"] + old["records"] + [old_manifest_row]:
    r = verify(row); older_own[r["path"]] = r
for manifest_row in (pb["immutable_R9_manifest_for_reproduction"], pb["immutable_previous_manifest"]):
    manifest = load(manifest_row)
    for row in manifest["artifacts"] + [manifest_row]:
        r = verify(row); older_own[r["path"]] = r
verify(pb["immutable_R9_validation_for_reproduction"])
verify(pb["immutable_previous_validation"])
if digest(list(older_own.values())) != pb["older_own_preserved_summary"]:
    raise SystemExit("Parent341-path preservation summary mismatch")
for row in parent["artifacts"] + [PARENT_MANIFEST]:
    r = verify(row); older_own[r["path"]] = r
if len(older_own) != 349:
    raise SystemExit("Unexpected older-own count")

verify(TARGET)
constructor = load(TARGET_FREEZE)
constructor_records = [verify(r) for r in constructor["artifacts"]]
source = json.loads((ROOT / (TP + "sources-v1.json")).read_text())
constructor_val = json.loads((ROOT / (TP + "input-validation-v1.json")).read_text())
direct = [verify(r) for r in source["accepted_input_records"]]
direct.append(verify(source["official"]["local_statement"]))
direct.append(verify(rec("AGENTS.md")))
r6_manifest_row = source["accepted_R6_frozen_parent"]
r6 = load(r6_manifest_row)
r6_records = [verify(r) for r in r6["artifacts"]]
r6_main_row = verify(source["accepted_R6_byte_identical_original_candidate"])
r6_accepted = next(r for r in direct if r["path"].endswith("reviewed-reasoning-return-r6-v1.1.md"))
if not (ROOT / r6_accepted["path"]).read_bytes().endswith((ROOT / r6_main_row["path"]).read_bytes()):
    raise SystemExit("Accepted R6 suffix changed")
for primary in source["primary_sources"]:
    if "cached_binary" in primary:
        direct.append(verify(primary["cached_binary"]))

# Bind constructor's old chain rather than duplicating or claiming a new
# unrelated mathematical reread. Direct necessary declared identities match.
constructor_parent_records = [verify(constructor_val[k]) for k in
                              ("immutable_parent_manifest", "immutable_parent_validation")]
authority_summaries = []
for name in ("reasoning-return-r6", "original-weight-universal", "reciprocal-kernel",
             "Fueter-selection-return", "original-weight-selection"):
    base = "problems/2025-B4/reviews/" + name + "-acceptance"
    md = verify(rec(base + ".md")); direct.append(md)
    js = verify(rec(base + ".json")); obj = json.loads((ROOT / js["path"]).read_text())
    declared = [verify(r) for r in rows(obj)]
    integrity_row = verify(rec(base + "-integrity.json"))
    authority_summaries.append({"acceptance_markdown": md, "immutable_acceptance": js,
        "immutable_integrity_summary": integrity_row,
        "necessary_declared_fingerprint_occurrences_reverified": len(declared),
        "necessary_declared_deduplicated_summary": digest(declared),
        "coordinator_prior_full_inventory_occurrences_recorded_not_replayed": obj.get("record_occurrences_verified"),
        "coordinator_prior_full_inventory_unique_paths_recorded_not_replayed": obj.get("unique_paths_verified")})

obligations = (ROOT / (TP + "obligations-v1.md")).read_text()
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
for number in range(1, 57):
    if obligations.count("| R7-%02d |" % number) != 1 or ledger.count("|R7-%02d|" % number) != 1:
        raise SystemExit("Missing/duplicate full obligation row")
prose_names = ["initial.md", "issues-v1.md", "source-checks-v1.md"]
prose = [rec(PREFIX + n) for n in prose_names]
now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 18:46:21 UTC", "total_used_percent": 56,
             "window_minutes": 10080, "reset_unix": 1792745187,
             "ordinary_usage_allowed": True, "total_ceiling_percent": 90,
             "review_integration_reserve": True}
binding = {"immutable_parent_manifest": PARENT_MANIFEST,
           "immutable_parent_validation": PARENT_VALIDATION,
           "exact_reproduction_chain_bound_in_parent_validation": True,
           "older_own_preserved_summary": digest(list(older_own.values())),
           "historical_inventory_not_copied": True,
           "reproduction": "Use exact CS parent validation compact_immutable_parent_binding to reconstruct341 paths from full older2022 validation/manifest plus R9 and2020R7 artifacts/manifests; append exact CS artifacts/manifest. This script re-verifies349 own paths without copying the inventory."}
primary_reads = [
    {"url": source["official"]["url"], "scope": "Actual official B4(b), signed integer domain, no preliminary proof"},
    {"url": source["primary_sources"][0]["url"],
     "scope": "Fresh actual2.2 equations10--13, Stickelberger definitions/generation context, selected2.5/2.5.1/4.2 canonical/phase passages, COMPLETE Theorem3 statement; old full4.3 read retained as context, no new full external proof certification",
     "import": "Attributed matched-prime Jacobi ideal formula, ordinary cyclotomic background; no full Diophantine/class-number theorem"},
    {"url": "https://arxiv.org/pdf/1412.5798v2",
     "scope": "Fresh Jacobi/series normalization, Lemma2.7, relevant2.8--2.10, beginning5.2 selection; earlier complete relevant appendices retained as old context",
     "strict_N_less_than_p_minus_1_not_extended_by_source_import": True},
    {"url": source["primary_sources"][2]["url"],
     "scope": "ALL12 primary PDF pages including Proposition1, quotient/module action, applications and final remark",
     "hypotheses": "q>p; q=p and q<p explicitly deferred; NOT a diagonal input or theorem refutation"}]
for row in primary_reads:
    row.update(read_date_utc="2026-10-17", new_native_pdf_hash=None, new_pdf_or_cache_write=False)

def new(suffix, obj):
    with (ROOT / (PREFIX + suffix)).open("x") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2); f.write("\n")

new("sources-v1.json", {"frozen_at_utc": now, "reviewer": "/root/review_2022_complexity_r2",
    "role": "fresh initially blind NONCONSTRUCTOR WHOLE R2, all56 obligations",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "target": TARGET, "constructor_freeze": TARGET_FREEZE,
    "complete_constructor_artifacts": constructor_records,
    "exact_accepted_inputs_and_context": direct,
    "accepted_R6_exact_eight_artifact_packet": r6_records,
    "accepted_R6_suffix_byte_identical": True,
    "actual_local_read_scope": "Complete constructor8 plus freeze; COMPLETE accepted R6/UW/RK/FS/OW and their5 acceptance Markdown scopes; partial header/fullCF1; MS/PG other old metadata not claimed full freshly reread",
    "primary_actual_reads": primary_reads,
    "old_UW_authorship_R6_MS_related_review_roles_disclosed": True,
    "new_R7_construction_contribution": False,
    "old_own_accepted_inputs_not_independently_self_recertified": True,
    "new_peer_R7_findings_and_queued2017R4_unread_before_entire_freeze": True,
    "compact_immutable_binding": binding,
    "no_mathematical_program_CAS_scan_author_rerun_certificate_or_new_binary_download": True,
    "direct_weekly_telemetry": telemetry})
new("input-validation-v1.json", {"frozen_at_utc": now,
    "administrative_only_not_mathematical_evidence": True,
    "constructor_artifacts_verified": constructor_records,
    "exact_direct_records": direct,
    "accepted_authority_compact_summaries": authority_summaries,
    "constructor_old_parent_metadata_bound_only": constructor_parent_records,
    "constructor_old_recorded_occurrences_not_replayed": constructor_val["parent_declared_fingerprint_occurrences_verified"],
    "constructor_old_recorded_deduplicated_paths_not_replayed": constructor_val["parent_declared_deduplicated_paths_verified"],
    "compact_immutable_parent_binding": binding,
    "older_own_unique_paths_preserved": len(older_own),
    "current_fingerprint_occurrences_reverified": occurrences,
    "current_verified_records_deduplicated_summary_only": digest(list(inventory.values())),
    "whole56_obligation_rows_covered_once": True,
    "prose_records": prose,
    "all_new_peer_findings_unread_before_entire_freeze": True,
    "no_mathematical_code_scan_CAS_author_rerun_or_old_shared_Git_cache_edit": True,
    "direct_weekly_telemetry": telemetry})
new("freeze-output-v1.json", {"frozen_at_utc": now, "whole_initial_complete": True,
    "all56_author_obligations_covered": True, "substantive_issues": 0,
    "required_repairs": 0, "new_peer_findings_unread_before_entire_freeze": True,
    "older_own_unique_paths_preserved": len(older_own),
    "record_occurrences_reverified": occurrences, "unique_paths_reverified": len(inventory),
    "no_math_code_CAS_scan_author_rerun_or_certificate": True,
    "coordinator_promotion_performed": False, "direct_weekly_telemetry": telemetry})
artifacts = [rec(PREFIX + name) for name in prose_names +
             ["freeze-v1.py", "sources-v1.json", "input-validation-v1.json", "freeze-output-v1.json"]]
new("manifest-v1.json", {"frozen_at_utc": now,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; recommendation only, no promotion",
    "reviewer": "/root/review_2022_complexity_r2", "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "target": TARGET, "constructor_freeze": TARGET_FREEZE,
    "whole_claims": ["R7A actual odd-lattice normalization", "R7B divided moment/projection/product",
                     "R7C residual quotient/kernel boundary", "R7D conditional original-weight purity bound",
                     "R7E ACTUAL higher-weight Jacobi row-collapse"],
    "whole_author_obligations": 56, "substantive_issues": 0, "required_repairs": 0,
    "new_peer_findings_unread_before_entire_freeze": True,
    "old_UW_authorship_R6_MS_related_roles_disclosed_no_self_review": True,
    "no_new_R7_construction_contribution": True,
    "no_original_weight_counterexample_Diophantine_exclusion_annual_or_novelty_claim": True,
    "no_math_code_CAS_scan_author_rerun_certificate_or_old_shared_Git_cache_edit": True,
    "compact_parent_manifest": PARENT_MANIFEST, "compact_parent_validation": PARENT_VALIDATION,
    "historical_inventory_not_copied": True,
    "older_own_unique_paths_preserved": len(older_own),
    "record_occurrences_reverified": occurrences, "unique_paths_reverified": len(inventory),
    "direct_weekly_telemetry": telemetry,
    "command": "python3 " + PREFIX + "freeze-v1.py", "artifacts": artifacts})
print(json.dumps({"manifest": rec(PREFIX + "manifest-v1.json"), "artifacts": len(artifacts),
    "whole_obligations": 56, "substantive_issues": 0,
    "record_occurrences": occurrences, "unique_paths": len(inventory),
    "older_own_paths": len(older_own)}, indent=2))
