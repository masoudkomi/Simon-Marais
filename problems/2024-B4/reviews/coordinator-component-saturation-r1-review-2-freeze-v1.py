#!/usr/bin/env python3
"""Immutable CS whole R2 metadata freeze, not mathematical computation.

No constructor script, mathematical source certificate or old freezer is
executed. Historical inventories are reverified/bound compactly. New peer
CS and queued2025R7 findings are forbidden until this whole initial freeze.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/coordinator-component-saturation-r1-review-2-"
TARGET = {
    "path": "problems/2024-B4/notes/coordinator-component-saturation-r1-candidate-v1.md",
    "bytes": 13194,
    "sha256": "61f8c60491880e941149649c2c4180abef91671496d56c5869f8543a915aba46",
}
TARGET_FREEZE = {
    "path": "problems/2024-B4/notes/coordinator-component-saturation-r1-freeze-v1.json",
    "bytes": 3452,
    "sha256": "13dff01ab6757aa2214d4be9667c96f8381446f7b41c0b06b3458babfe80f0fb",
}
PREVIOUS_MANIFEST = {
    "path": "problems/2020-B4/notes/reasoning-return-r7-freeze-v1.json",
    "bytes": 4168,
    "sha256": "b83040ef82ae1b4ef8393b4d1c8799fd095ed4d81a52a7ebb03aff8087fb649a",
}
PREVIOUS_VALIDATION = {
    "path": "problems/2020-B4/notes/reasoning-return-r7-input-validation-v1.json",
    "bytes": 13368,
    "sha256": "7c116489b6bfbb77f7014104ce49b0b5940823d70a1706fa034a7794dbe92ca3",
}
for name in ("sources-v1.json", "input-validation-v1.json",
             "freeze-output-v1.json", "manifest-v1.json"):
    if (ROOT / (PREFIX + name)).exists():
        raise SystemExit("Refusing frozen-output overwrite: " + PREFIX + name)
inventory = {}
occurrences = 0

def rec(path):
    absolute = (ROOT / path).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Outside workspace: " + str(path))
    rel = str(absolute.relative_to(ROOT))
    if ((rel.startswith("problems/2024-B4/reviews/coordinator-component-saturation-r1-review-")
         and not rel.startswith(PREFIX))
            or rel.startswith("problems/2025-B4/reviews/reasoning-return-r7-")
            or rel.startswith("problems/2025-B4/notes/reasoning-return-r7-")):
        raise SystemExit("Forbidden unfrozen peer/queued input: " + rel)
    b = absolute.read_bytes()
    return {"path": rel, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def verify(expected):
    global occurrences
    actual = rec(expected["path"])
    if actual["sha256"] != expected["sha256"]:
        raise SystemExit("SHA mismatch: " + actual["path"])
    if "bytes" in expected and actual["bytes"] != expected["bytes"]:
        raise SystemExit("Length mismatch: " + actual["path"])
    if actual["path"] in inventory and inventory[actual["path"]] != actual:
        raise SystemExit("Conflicting old record: " + actual["path"])
    inventory[actual["path"]] = actual
    occurrences += 1
    return actual

def load(expected):
    current = verify(expected)
    return json.loads((ROOT / current["path"]).read_text())

def rows(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and re.fullmatch("[0-9a-f]{64}", str(obj.get("sha256", "")))):
            yield obj
        for key, value in obj.items():
            if ("/" in key and isinstance(value, str)
                    and re.fullmatch("[0-9a-f]{64}", value)):
                yield {"path": key, "sha256": value}
            yield from rows(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from rows(value)

def digest(records):
    unique = {r["path"]: {k: r[k] for k in ("path", "bytes", "sha256")}
              for r in records}
    canonical = [unique[p] for p in sorted(unique)]
    b = json.dumps(canonical, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")).encode()
    return {"unique_paths": len(canonical),
            "canonical_sorted_record_array_sha256": hashlib.sha256(b).hexdigest(),
            "canonical_encoding": "UTF8 JSON ensure_ascii=false sort_keys=true separators=(comma,colon), records sorted by path"}

# Reconstruct old own inventory through the two compact immutable links.
previous = load(PREVIOUS_MANIFEST)
previous_val = load(PREVIOUS_VALIDATION)
pb = previous_val["compact_immutable_preservation_binding"]
r9_manifest_record = pb["immutable_parent_manifest"]
r9_validation_record = pb["immutable_parent_validation"]
r9 = load(r9_manifest_record)
r9_val = load(r9_validation_record)
r9b = r9_val["compact_immutable_preservation_binding"]
old_manifest_record = r9b["immutable_previous_manifest"]
old_validation_record = r9b["immutable_previous_validation"]
old = load(old_manifest_record)
old_val = load(old_validation_record)
older_own = {}
for expected in old_val["older_own_records"] + old["records"] + [old_manifest_record]:
    current = verify(expected)
    older_own[current["path"]] = current
if digest(list(older_own.values())) != r9b["older_own_records_reverified_including_previous_whole_packet"]:
    raise SystemExit("Old319-path parent digest mismatch")
for expected in r9["artifacts"] + [r9_manifest_record]:
    current = verify(expected)
    older_own[current["path"]] = current
if digest(list(older_own.values())) != pb["older_own_records_reverified_including_parent_packet"]:
    raise SystemExit("Old330-path parent digest mismatch")
for expected in previous["artifacts"] + [PREVIOUS_MANIFEST]:
    current = verify(expected)
    older_own[current["path"]] = current
if len(older_own) != 341:
    raise SystemExit("Unexpected older-own preservation count")

verify(TARGET)
target_manifest = load(TARGET_FREEZE)
constructor_records = [verify(r) for r in target_manifest["artifacts"]]
target_prefix = "problems/2024-B4/notes/coordinator-component-saturation-r1-"
cs_source = json.loads((ROOT / (target_prefix + "sources-v1.json")).read_text())
cs_validation = json.loads((ROOT / (target_prefix + "input-validation-v1.json")).read_text())
direct_records = [verify(r) for r in cs_source["direct_input_identities"]]

metadata_summaries = []
declared_occurrences = 0
declared_unique = {}
for wrapper in cs_validation["immutable_metadata"]:
    source_record = verify(wrapper["metadata"])
    declared = list(rows(json.loads((ROOT / source_record["path"]).read_text())))
    if len(declared) != wrapper["declared_record_occurrences_verified"]:
        raise SystemExit("Changed declared metadata count: " + source_record["path"])
    for expected in declared:
        current = verify(expected)
        declared_unique[current["path"]] = current
    declared_occurrences += len(declared)
    metadata_summaries.append({
        "immutable_metadata_source": source_record,
        "declared_fingerprint_occurrences_reverified": len(declared),
        "deduplicated_declared_summary": digest([rec(r["path"]) for r in declared]),
    })
if declared_occurrences != 666 or len(declared_unique) != 576:
    raise SystemExit("Constructor declared inventory count mismatch")

acceptance_markdown = []
for path in ("problems/2024-B4/reviews/Kasami-whole-criterion-acceptance.md",
             "problems/2024-B4/reviews/generalized-Kasami-acceptance.md",
             "problems/2024-B4/reviews/reasoning-components-r1-acceptance.md"):
    current = verify(rec(path))
    acceptance_markdown.append(current)
    direct_records.append(current)

obligations = (ROOT / (target_prefix + "obligations-v1.md")).read_text()
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
for i in range(1, 31):
    if obligations.count("|CS-%02d|" % i) != 1 or ledger.count("|CS-%02d|" % i) != 1:
        raise SystemExit("Missing/duplicate whole obligation coverage")
prose_names = ["initial.md", "issues-v1.md", "source-checks-v1.md"]
prose_records = [rec(PREFIX + name) for name in prose_names]
now = datetime.now(timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-17 18:35:09 UTC",
             "total_used_percent": 55, "window_minutes": 10080,
             "reset_unix": 1792745187, "ordinary_usage_allowed": True,
             "total_ceiling_percent": 90, "review_integration_reserve": True}
parent_binding = {
    "immutable_previous_manifest": PREVIOUS_MANIFEST,
    "immutable_previous_validation": PREVIOUS_VALIDATION,
    "immutable_R9_manifest_for_reproduction": r9_manifest_record,
    "immutable_R9_validation_for_reproduction": r9_validation_record,
    "immutable_full_inventory_manifest_for_reproduction": old_manifest_record,
    "immutable_full_inventory_validation_for_reproduction": old_validation_record,
    "older_own_preserved_summary": digest(list(older_own.values())),
    "historical_inventory_not_copied": True,
    "reproduction": "Reconstruct319 old own rows from exact full-inventory validation older_own_records plus its manifest records and manifest; append exact R9 artifacts/manifest, then exact2020R7 artifacts/manifest. This script re-verifies341 paths and checks both parent digests without copying their inventories.",
}
primary_reads = [
    {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
     "scope": "Actual page2 B4(b), odd positive n and coefficientwise integer target; no preliminary proof"},
    {"url": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Another_elementary_proof_of_Luroth%27s_theorem-06.2004.pdf",
     "scope": "Bensimhoun2004 COMPLETE two-page authored theorem/proof and degree/tower conclusion",
     "hypotheses": "arbitrary field, no characteristic0/tameness/separability condition"},
    {"url": "https://arxiv.org/pdf/1907.01066v1",
     "scope": "Mesnager--Qu Section5.4 Definition44, parameter paragraph, odd-k exceptionality and Proposition45 statement/attribution, PDF pp21--22",
     "finite_field_exceptionality_or_two_to_one_theorem_used": False},
    {"url": "https://arxiv.org/pdf/1612.05997v1",
     "scope": "Delgado--Janwa equations2--4 definitions and Section3 COMPLETE equation5 Janwa--Wilson statement, printed7",
     "role": "optional labelled interpretation only; original1993 proof unread; no later transversality/APN claims used"},
]
for entry in primary_reads:
    entry["read_date_utc"] = "2026-10-17"
    entry["native_bytes_sha256"] = None
    entry["new_pdf_download_or_cache_write"] = False
source_obj = {
    "frozen_at_utc": now,
    "review": "fresh initially blind NONCONSTRUCTOR WHOLE R2, all30 author obligations",
    "reviewer": "/root/review_2022_complexity_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "target": TARGET, "constructor_freeze": TARGET_FREEZE,
    "complete_constructor_artifacts": constructor_records,
    "exact_direct_accepted_inputs_and_context": direct_records,
    "actual_accepted_read_scope": "COMPLETE accepted KC/GK/IC mathematical bodies and acceptance Markdown; inherited CP1 through KC not claimed newly independently reconstructed; old roles disclosed",
    "primary_source_actual_reads": primary_reads,
    "actual_image_read": {"path": ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-40.png",
                          "scope": "printed35 q4 explicit factors; mixed X^3Y term, no computer certificate rerun"},
    "source_limits": "Original JW1993 proof/Ferard full theorem unread; no full28page MCM audit or remaining thesis pages newly read; source checks explicit",
    "new_CS_construction_contribution": False,
    "older_CP_GK_NV_NJ_HR_related_review_context_disclosed": True,
    "root_constructor_excluded_from_independent_count": True,
    "new_peer_CS_or_queued_2025R7_findings_read_before_freeze": False,
    "compact_immutable_parent_binding": parent_binding,
    "direct_weekly_telemetry": telemetry,
}
def new(name, obj):
    target = ROOT / (PREFIX + name)
    with target.open("x") as stream:
        json.dump(obj, stream, ensure_ascii=False, indent=2)
        stream.write("\n")

new("sources-v1.json", source_obj)
validation = {
    "frozen_at_utc": now, "administrative_only_not_mathematical_evidence": True,
    "all_exact_records_verified": True,
    "constructor_artifacts_verified": constructor_records,
    "direct_input_records": direct_records,
    "declared_constructor_metadata_summaries": metadata_summaries,
    "constructor_declared_record_occurrences_reverified": declared_occurrences,
    "constructor_declared_unique_paths_reverified": len(declared_unique),
    "all_current_fingerprint_occurrences_reverified": occurrences,
    "all_current_verified_records_deduplicated_summary_only": digest(list(inventory.values())),
    "compact_immutable_parent_binding": parent_binding,
    "older_own_unique_paths_preserved": len(older_own),
    "report_and_ledger_records": prose_records,
    "all30_whole_obligations_covered_once": True,
    "no_mathematical_program_CAS_scan_author_rerun_or_certificate": True,
    "no_Git_shared_old_cache_edit_spawn_charge_contact_bypass": True,
    "new_peer_findings_unread_before_entire_freeze": True,
    "direct_weekly_telemetry": telemetry,
}
new("input-validation-v1.json", validation)
output = {
    "frozen_at_utc": now,
    "whole_initial_complete": True,
    "all30_author_obligations_covered": True,
    "substantive_issues": 0, "required_repairs": 0,
    "optional_nonblocking_notes": ["N1 separable/squarefree wording; actual gcd check supplied"],
    "new_peer_findings_unread_before_entire_freeze": True,
    "older_own_unique_paths_preserved": len(older_own),
    "record_occurrences_reverified": occurrences,
    "unique_paths_reverified": len(inventory),
    "mathematical_program_run": False,
    "coordinator_promotion_performed": False,
    "direct_weekly_telemetry": telemetry,
}
new("freeze-output-v1.json", output)
names = prose_names + ["freeze-v1.py", "sources-v1.json",
                       "input-validation-v1.json", "freeze-output-v1.json"]
artifacts = [rec(PREFIX + name) for name in names]
manifest = {
    "frozen_at_utc": now,
    "status": "COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial freeze; recommendation only, no promotion",
    "reviewer": "/root/review_2022_complexity_r2",
    "constructor": "coordinator root, excluded from independent reviewer count",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "target": TARGET, "constructor_freeze": TARGET_FREEZE,
    "whole_claims": ["CS1 every-k component saturation", "CS2 exact gcd/label occurrence via accepted KC/GK"],
    "whole_author_obligations": 30,
    "substantive_issues": 0, "required_repairs": 0,
    "optional_nonblocking_notes": ["N1"],
    "new_peer_findings_unread_before_entire_freeze": True,
    "no_new_CS_construction_contribution": True,
    "older_review_roles_and_source_limits_disclosed": True,
    "no_full_annual_general_factor_classification_or_novelty_claim": True,
    "no_mathematical_program_CAS_scan_author_rerun_or_certificate": True,
    "no_Git_shared_old_cache_edit_spawn_charge_contact_bypass": True,
    "compact_parent_manifest": PREVIOUS_MANIFEST,
    "compact_parent_validation": PREVIOUS_VALIDATION,
    "historical_inventory_not_copied": True,
    "older_own_unique_paths_preserved": len(older_own),
    "record_occurrences_reverified": occurrences,
    "unique_paths_reverified": len(inventory),
    "direct_weekly_telemetry": telemetry,
    "command": "python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
new("manifest-v1.json", manifest)
print(json.dumps({"manifest": rec(PREFIX + "manifest-v1.json"),
                  "artifacts": len(artifacts),
                  "whole_obligations": 30,
                  "substantive_issues": 0,
                  "record_occurrences": occurrences,
                  "unique_paths": len(inventory),
                  "older_own_paths": len(older_own)}, indent=2))
