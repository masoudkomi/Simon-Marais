"""Administrative R11 byte/hash binding only. No mathematical calculation.

Run from the repository with:
    .venv/bin/python problems/2021-B4/notes/reasoning-return-r11-freeze-v1.py --freeze
or --verify for a read-only postfreeze check.
All writes use exclusive creation inside this NEW assigned prefix.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r11-"
NOW = lambda: datetime.now(timezone.utc).isoformat()


def record(path):
    p = Path(path)
    if not p.is_absolute():
        p = ROOT / p
    b = p.read_bytes()
    try:
        shown = str(p.relative_to(ROOT))
    except ValueError:
        shown = str(p)
    return {"path": shown, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def verify(row):
    got = record(row["path"])
    if got["sha256"] != row["sha256"]:
        raise RuntimeError("SHA mismatch: " + row["path"])
    if "bytes" in row and got["bytes"] != row["bytes"]:
        raise RuntimeError("size mismatch: " + row["path"])
    return got


def declarations(obj):
    if isinstance(obj, dict):
        if isinstance(obj.get("path"), str) and isinstance(obj.get("sha256"), str):
            if len(obj["sha256"]) == 64:
                yield obj
        for v in obj.values():
            yield from declarations(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from declarations(v)


def write_new(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    if not str(path.relative_to(ROOT)).startswith(PREFIX):
        raise RuntimeError("write outside assigned prefix")
    with path.open("x", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return record(path)


EXPECTED = [
    ("AGENTS.md", 4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    ("problems/2021-B4/proofs/reviewed-reasoning-return-r10-v1.1.md", 27060, "99eaab93c008085e8ea8d4c961f26c53d66f4ac8a288500ca1efeb31bc87e55b"),
    ("problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md", 19921, "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"),
    ("problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md", 23675, "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d"),
    ("problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md", 8176, "56274936ab198f01cb38b1701fdec7907860eb654fd2bc79c3b2d0e03054a271"),
    ("problems/2021-B4/proofs/reviewed-return-r3-v1.1.md", 5304, "9cda0a35c42e7a3098418ec052180f4868ca995feee47b503971b8fc2cb6d4b4"),
    ("problems/2021-B4/notes/reasoning-return-r3-transfer-candidate-v1.md", 9020, "0bcc9898ff010abf489f7b4c58d4a5011e91df99ab680bd0094d76054b3e3961"),
    ("problems/2021-B4/notes/reasoning-return-r10-candidate-v1.md", 23674, "30c6046d83792ffff937f6052f7b00c18288754b3dc8e73345ca4a112015d09f"),
    ("problems/2021-B4/notes/reasoning-return-r10-failed-routes-v1.md", 5189, "aabca8cbdca341bb98d6a2371d7cdb26ec87bac60ea68b23e44d8a9888efa5a5"),
    ("problems/2021-B4/notes/reasoning-return-r10-freeze-v1.json", 3884, "ff20fd17e080ce3fb5d3c0f4f3f7c1f58624741b0fadc1be4a0fee26fc73f2bd"),
    ("problems/2019-B4/reviews/coordinator-retained-core-gap-r1-review-1-manifest-v1.json", 3766, "f05ab8b1f3ce97acfcb020906b774655531402fbcf390f6b0eb748fbd7a4ae3d"),
    (".cache/literature/2021/cited-66c5af6a0f0239f5.pdf", None, "d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf"),
    (".cache/literature/deep-literature-r1/2021-draisma-dejong-erratum-2011.pdf", None, "9414998fc302643b7cf261e4adec1333034dc732e8a3a493a1a0ff7418d8f262"),
]

PARENTS = [
    "problems/2021-B4/notes/reasoning-return-r10-freeze-v1.json",
    "problems/2021-B4/notes/reasoning-return-r10-sources-v1.json",
    "problems/2021-B4/notes/reasoning-return-r10-input-validation-v1.json",
    "problems/2021-B4/reviews/reasoning-return-r10-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r10-acceptance-integrity.json",
    "problems/2021-B4/notes/reasoning-return-r8-freeze-v1.json",
    "problems/2021-B4/notes/reasoning-return-r8-sources-v1.json",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance-integrity.json",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance-integrity.json",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance.json",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance-integrity.json",
    "problems/2021-B4/reviews/return-r3-acceptance.json",
    "problems/2021-B4/reviews/return-r3-acceptance-integrity.json",
    "problems/2021-B4/notes/reasoning-return-r3-transfer-manifest-v1.json",
    "problems/2019-B4/reviews/coordinator-retained-core-gap-r1-review-1-manifest-v1.json",
]

PROSE_INPUTS = [
    "problems/2021-B4/statement.md",
    "problems/2021-B4/reviews/reasoning-return-r10-acceptance.md",
    "problems/2021-B4/reviews/reasoning-return-r8-acceptance.md",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance.md",
    "problems/2021-B4/reviews/return-r3-acceptance.md",
]

PUBLIC = [
    {"title": "Official2021 Paper B", "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf", "read_scope": "page2 B4 hypothesis and(b) target only; no preliminary proof", "role": "official domain"},
    {"title": "Castryck--Laterveer--Ounaies, Constraints on counterexamples ... degree12", "url": "https://arxiv.org/pdf/1208.5404", "read_scope": "Sections3.4--3.5 equations9--13/Lemma17, beta identity; complete Proposition19 and unramified remark, not whole23pages", "role": "attribution; stronger all-root-rational/unramified hypotheses NOT applied"},
    {"title": "Draisma--de Jong August2011 erratum", "url": "https://math-unibe.ch/jdraisma/publications/erratumcasasalvero.pdf", "read_scope": "complete original one page,20 extracted lines", "role": "prime5 correction retained"},
    {"title": "Atkinson--Sharma1969, A partial characterization of poised Hermite-Birkhoff interpolation problems", "url": "https://homepage.math.uiowa.edu/~atkinson/papers/HB_interp.pdf", "read_scope": "complete six pages230--235 extracted text, definitions/Theorem2/full proof and unused converse conjecture", "role": "failed-route context only; no new theorem import"},
    {"title": "Yakubovich, Polynomial problems of the Casas-Alvero type", "url": "https://files.ele-math.com/articles/jca-04-07.pdf", "read_scope": "Corollaries1--3 printed105; Lemma6 statement/proof printed112; not full24pages", "role": "all-roots-real hypothesis prevents shortcut"},
    {"title": "Massri, The Casas-Alvero conjecture for three recycled roots in degree20", "url": "https://arxiv.org/pdf/1806.09561", "read_scope": "servedv6/August2023, introduction/Section1 opening/Section5 through Theorem5.7 and Remark5.8; not Section7 proof or whole paper", "role": "context only; finiteness not emptiness or a four-value theorem"},
    {"title": "Armengol Gasull, A Primer on Resultants and Their Applications (2026)", "url": "https://link.springer.com/article/10.1007/s44425-026-00047-6", "read_scope": "subsection3.4, reference19 and author metadata only", "role": "status sentence not imported; worked proposition concerns4,5"},
]


def input_validation():
    all_rows = []
    direct = []
    for path, size, sha in EXPECTED:
        row = {"path": path, "sha256": sha}
        if size is not None:
            row["bytes"] = size
        got = verify(row)
        direct.append(got)
        all_rows.append(got)
    for path in PROSE_INPUTS:
        got = record(path)
        direct.append(got)
        all_rows.append(got)
    bindings = []
    for path in PARENTS:
        parent = record(path)
        rows = list(declarations(json.loads((ROOT / path).read_text())))
        checked = [verify(row) for row in rows]
        bindings.append({"metadata": parent,
                         "declared_fingerprint_occurrences_verified": len(checked)})
        all_rows.extend(checked)
        all_rows.append(parent)
    dedup = {}
    for row in all_rows:
        if row["path"] in dedup and dedup[row["path"]] != row:
            raise RuntimeError("incompatible frozen declarations: " + row["path"])
        dedup[row["path"]] = row
    canonical = [dedup[p] for p in sorted(dedup)]
    digest = hashlib.sha256(json.dumps(canonical, separators=(",", ":"), sort_keys=True).encode()).hexdigest()
    return {"verified_at_utc": NOW(), "administrative_only": True,
            "all_necessary_selected_parent_declarations_verified": True,
            "direct_inputs": direct, "immutable_parent_bindings": bindings,
            "fingerprint_occurrences_verified": len(all_rows),
            "unique_paths_verified": len(canonical),
            "canonical_deduplicated_summary_sha256": digest,
            "historical_rows_bound_in_exact_parents_not_duplicated": True,
            "parent_reference_scope": "ALL declarations within each selected immutable parent, not a recursive reread of every unrelated historical inventory",
            "old_mathematics_fresh_read_scope": "complete accepted R10/R5/R8/PN/register/TA1 and stated acceptance prose; old own RC metadata guarded only",
            "new_math_code_CAS_scan_author_rerun_or_certificate_replay": False}


def freeze():
    manifest_path = ROOT / (PREFIX + "freeze-v1.json")
    if manifest_path.exists():
        raise RuntimeError("already frozen; use --verify")
    validation = input_validation()
    input_row = write_new("input-validation-v1.json", validation)
    public = [{**s, "fresh_native_file_sha256": None} for s in PUBLIC]
    source_row = write_new("sources-v1.json", {
        "recorded_at_utc": NOW(), "status": "candidate proof - unverified",
        "claims": ["R11A two complete field incompatibilities", "R11B ACTUAL m7 first-break exclusion", "R11C four-unit essential-even-center consequence"],
        "public_primary_sources": public,
        "accepted_body_paths_complete_read": [r["path"] for r in validation["direct_inputs"] if "/proofs/" in r["path"]] + ["problems/2021-B4/notes/reasoning-return-r3-transfer-candidate-v1.md"],
        "compact_immutable_parent_record": input_row,
        "browser_source_not_asserted_identical_to_old_native_cache": True,
        "new_external_theorem_import": False,
        "older_constructor_roles": ["TA1/return-r3", "R6/R7/R8/R10"],
        "older_reviewer_roles": ["J15", "PN", "R5"],
        "root_generic_assignment_only_no_new_R11_mathematical_inference": True,
        "two_OTHER_fresh_initially_blind_WHOLE_audits_required": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "independently_verified_effective_settings": None,
        "new_mathematical_executable_CAS_scan_or_author_rerun": False,
        "new_download_cache_write_render_native_wait_contact_charge_bypass": False,
    })
    out = {
        "finished_at_utc": NOW(), "kind": "administrative byte/hash validation ONLY",
        "command": ".venv/bin/python " + PREFIX + "freeze-v1.py --freeze",
        "exit_code": 0, "mathematical_inferences_executed": 0,
        "fingerprint_occurrences_verified": validation["fingerprint_occurrences_verified"],
        "unique_paths_verified": validation["unique_paths_verified"],
        "canonical_deduplicated_summary_sha256": validation["canonical_deduplicated_summary_sha256"],
        "all_old_selected_declarations_unchanged": True,
        "no_writes_outside_NEW_assigned_prefix": True,
    }
    out_row = write_new("freeze-output-v1.json", out)
    suffixes = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
                "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md",
                "freeze-v1.py"]
    payload = [record(PREFIX + s) for s in suffixes] + [source_row, input_row, out_row]
    manifest = {
        "frozen_at_utc": NOW(), "status": "candidate proof - unverified; COMPLETE constructor checkpoint",
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "claims": ["R11A", "R11B", "R11C"], "whole_obligations": 56,
        "two_OTHER_fresh_initially_blind_WHOLE_nonconstructor_audits_required": True,
        "root_supplied_NO_new_R11_mathematical_inference": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "independently_verified_effective_settings": None,
        "proposed_actual_m7_exclusion_not_annual_degree20_or_novelty": True,
        "ordinary_endpoint_geometry_or_max_valuation_assumed": False,
        "new_mathematical_code_CAS_scan_author_rerun_or_old_certificate_replay": False,
        "old_shared_cache_Git_writes_spawn_charge_contact_bypass": False,
        "authoritative_weekly_snapshot": {"at_utc": "2026-10-17 20:33:57 UTC", "total_used_percent": 64, "window_minutes": 10080, "reset_unix": 1792745187, "ordinary_usage_allowed": True, "total_ceiling_percent": 90, "integration_reserve": True, "automatic_new_window_spending": False},
        "compact_input_summary": {k: validation[k] for k in ["fingerprint_occurrences_verified", "unique_paths_verified", "canonical_deduplicated_summary_sha256"]},
        "administrative_command": out["command"], "artifacts": payload,
    }
    got = write_new("freeze-v1.json", manifest)
    for row in payload:
        verify(row)
    print(json.dumps({"manifest": got, "main": payload[0], "artifacts": len(payload),
                      "whole_obligations": 56, "compact_input_summary": manifest["compact_input_summary"]}, indent=2))


def postverify():
    manifest = json.loads((ROOT / (PREFIX + "freeze-v1.json")).read_text())
    for row in manifest["artifacts"]:
        verify(row)
    saved = json.loads((ROOT / (PREFIX + "input-validation-v1.json")).read_text())
    for row in saved["direct_inputs"]:
        verify(row)
    count = 0
    for parent in saved["immutable_parent_bindings"]:
        verify(parent["metadata"])
        body = json.loads((ROOT / parent["metadata"]["path"]).read_text())
        rows = list(declarations(body))
        for row in rows:
            verify(row)
        if len(rows) != parent["declared_fingerprint_occurrences_verified"]:
            raise RuntimeError("parent count mismatch")
        count += len(rows)
    print(json.dumps({"verified": True, "manifest": record(PREFIX + "freeze-v1.json"),
                      "artifacts": len(manifest["artifacts"]),
                      "selected_parent_declarations_reverified": count,
                      "writes": 0}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--freeze", action="store_true")
    mode.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    freeze() if args.freeze else postverify()
