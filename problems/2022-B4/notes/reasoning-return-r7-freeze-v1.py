"""Administrative R7 source/identity freeze. NO mathematical computation.

Run from repository root with the bundled Python. Refuses overwrites.
Only writes the assigned reasoning-return-r7-* prefix.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/notes/reasoning-return-r7-"
PREVIOUS = "problems/2021-B4/reviews/reasoning-return-r8-review-2-"


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(record):
    actual = fingerprint(record["path"])
    assert actual == {key: record[key] for key in actual}, record["path"]
    return actual


def write_new(suffix, value):
    path = ROOT / (PREFIX + suffix)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
    return fingerprint(PREFIX + suffix)


generated = ["sources-v1.json", "input-validation-v1.json",
             "freeze-output-v1.json", "freeze-v1.json"]
assert all(not (ROOT / (PREFIX + suffix)).exists() for suffix in generated)

previous_manifest_record = verify({
    "path": PREVIOUS + "manifest-v1.json", "bytes": 3085,
    "sha256": "f26c4f6f0ef83a1cb472001dcaa6344a2f3ff190bac0824cc00809f5c2406c4c",
})
previous_manifest = json.loads((ROOT / previous_manifest_record["path"]).read_text())
previous_validation_record = next(
    record for record in previous_manifest["artifacts"]
    if record["path"] == PREVIOUS + "input-validation-v1.json")
verify(previous_validation_record)
previous_validation = json.loads((ROOT / previous_validation_record["path"]).read_text())
prior = {}
for record in (previous_validation["earlier_unique_records_preserved"]
               + previous_manifest["artifacts"] + [previous_manifest_record]):
    actual = verify(record)
    if actual["path"] in prior:
        assert prior[actual["path"]] == actual
    prior[actual["path"]] = actual
assert len(prior) == 350

accepted = [fingerprint(path) for path in [
    "AGENTS.md", "problems/2022-B4/statement.md",
    "problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
    "problems/2022-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
    "problems/2022-B4/proofs/reviewed-return-r3-v1.1.md",
    "problems/2022-B4/proofs/reviewed-rational-base-shadow-return-v1.1.md",
    "problems/2022-B4/references.md",
]]
assert accepted[2]["sha256"] == "1a2544cb8ced3bba9cc6efed1870c242c652b3e6029f39881028d4637d7c6da6"
obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
ids = re.findall(r"^\|R7-O(\d\d)\|", obligations, re.MULTILINE)
assert ids == [f"{i:02}" for i in range(1, 47)]

now = datetime.now(timezone.utc).isoformat()
settings = {"requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
            "verified_effective_settings": None}
telemetry = {"at_utc": "2026-10-17 about16:25--16:26UTC direct tool",
             "total_used_percent": 51, "window_minutes": 10080,
             "reset_unix": 1792745187, "total_ceiling_percent": 90,
             "review_integration_reserve": True}
primary = [
    {"name": "Official2022 Paper B, B4(b)",
     "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf",
     "read": "Complete B4 actual domain and(b), simultaneous updates and product600; no preliminary proof research",
     "role": "Official problem only"},
    {"name": "Dubickas2009, Acta Arithmetica137,233--239",
     "url": "https://www.impan.pl/shop/publication/transaction/download/product/82938",
     "doi": "10.4064/aa137-3-4",
     "read": "Intro, Theorems1/3 statements and written Theorem1 proof throughp237; concluding context only",
     "limit": "SINGLE closed circular interval and1<q<p<q². Not applicable to disconnected J; no Sturmian extension imported",
     "role": "Failed-bridge scope check, not a premise of R7A--D"},
    {"name": "Kari--Kopra2017, RAIRO51(4),191--204",
     "url": "https://www.numdam.org/item/10.1051/ita/2017014.pdf",
     "alternative_version": "https://arxiv.org/pdf/1710.05737",
     "doi": "10.1051/ita/2017014",
     "read": "Intro encoding definitions, complete published Theorem4.9/Cor4.11 written proofs pp199--200, Theorem5.9 statement/proof and conclusions",
     "limit": "Existential small supporting unions and other forbidden unions do not identify J or the even/odd phase restriction; complete CA/ergodicity proof audit not claimed",
     "role": "Attribution of measure-only obstruction, not R7A--D proof premise"},
    {"name": "Akiyama--Frougny--Sakarovitch author rational-base PDF",
     "url": "https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf",
     "read": "Finite-word convention and complete Proposition37/Corollary38 proofs pp21--22",
     "limit": "Integer bound parameter and p>=2q-1 respected; no no-tenfold theorem at11/10, no complete thirty-page fresh audit",
     "role": "Published representation method attribution; direct accepted F5 supplies specialized finite language"},
    {"name": "Primary recent rational-base v2, arXiv2510.11723",
     "url": "https://arxiv.org/html/2510.11723v2",
     "read": "Section3.3 definitions, Conjecture3.9, Prop3.10 proof, Remark3.11, Question3.12 and Prop3.13 proof",
     "limit": "Normality/two-expansion conjectures and proper-residue termination remain conjectural/conditional here",
     "role": "Open-bridge status check, no arithmetic exclusion imported"},
    {"name": "Dubickas--Mossinghoff2009, Lower bounds for Z-numbers, author upload",
     "url": "https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers",
     "read": "Intro proper-residue question, complete Lemma3.1/Propositions3.1--3.2 statements and written proofs, adjacent binary-series/countability context",
     "limit": "Proved singleton case does not cover two residues0/9; conditional direction not a proved hypothesis",
     "role": "Classical residue/countability context, not R7 termination"},
]
failures = [
    {"url": "https://www.mscand.dk/article/download/15004/12999/34505",
     "result": "Web tool InternalError; no completed retrieval, cache identity, binary hash or theorem read claimed"},
    {"doi": "10.1002/mana.200510651",
     "result": "Publisher abstract/discovery only; full paper not retrieved; no theorem imported"},
]
sources_record = write_new("sources-v1.json", {
    "recorded_at_utc": now, "status": "candidate proof - unverified",
    **settings, "primary_actual_reads": primary, "discovery_or_access_limits": failures,
    "complete_accepted_F5_R6_bodies_and_scopes_read": True,
    "other_R3_R4_relevant_sections_only_freshly_consulted": True,
    "local_context_fingerprints_not_independent_theorem_recertification": accepted,
    "new_native_PDF_download_or_live_text_binary_hash_claim": False,
    "third_party_redistribution_licence_or_priority_claim": False,
})
validation_record = write_new("input-validation-v1.json", {
    "validated_at_utc": now, "administrative_identity_only": True,
    "earlier_unique_records_preserved": [prior[path] for path in sorted(prior)],
    "earlier_unique_record_count": len(prior),
    "accepted_context_fingerprints": accepted,
    "complete_F5_R6_scopes_read_but_old_authored_input_not_freshly_independently_reviewed": True,
    "whole_obligation_IDs": ids, "whole_obligation_count": len(ids),
    "new_math_program_CAS_scan_certificate_or_author_rerun": False,
    "ordinary_infinite_start_termination_no_tenfold_or_annual_solution_claim": False,
    "no_tenfold_sufficient_only_through_distinct_value_10C": True,
    "F5_formal_results_not_refuted_old_explanatory_scope_flagged_for_coordinator": True,
    "old_frozen_shared_Git_or_cache_mutation": False,
    "native_job_pending_approval_charge_contact_access_bypass_or_spawning": False,
    "queued_2019_AF_candidate_or_new_peer_findings_read_before_R7_freeze": False,
    "two_OTHER_fresh_initially_blind_WHOLE_audits_required": True,
})

artifacts = [fingerprint(PREFIX + suffix) for suffix in [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md",
    "freeze-v1.py"]] + [sources_record, validation_record]
output = {
    "status": "COMPLETE R7 constructor checkpoint frozen; candidate proof - unverified",
    "frozen_at_utc": now, "main": artifacts[0],
    "freeze_path": PREFIX + "freeze-v1.json", "artifact_count_excluding_freeze": 10,
    "whole_obligations": len(ids), "earlier_unique_records_preserved": len(prior),
    "mathematical_program_or_source_certificate_rerun": False,
    "requires_two_OTHER_fresh_initially_blind_WHOLE_audits": True,
}
output_record = write_new("freeze-output-v1.json", output)
artifacts.append(output_record)
write_new("freeze-v1.json", {
    "frozen_at_utc": now, "status": "candidate proof - unverified; COMPLETE constructor packet",
    "constructor": "/root/review_2017_coarsening_r1", **settings,
    "claims": ["R7A exact phased real iff with actual ordinary converse",
               "R7B exact scaled restricted ceiling bijection",
               "R7C conditional full10/ordinary9 fibers at10C",
               "R7D discrete feasible growth set and exact predecessor scope"],
    "UNPROVED": ["Existence or emptiness of the all-time phased set",
                 "No-tenfold theorem", "Future-to-past bridge(B)",
                 "Ordinary infinite avoiding path or unrestricted termination"],
    "official_scope": "2022 B4(b) only; restricted A/B family, no annual or all-controller closure",
    "no_other_worker_new_R7_proof_contribution_used": True,
    "OLD_R4_authorship_and_older_review_roles_disclosed": True,
    "F5_old_explanatory_no_tenfold_scope_flagged_not_edited": True,
    "two_OTHER_fresh_initially_blind_WHOLE_audits_then_coordinator_reconciliation_required": True,
    "whole_obligations": len(ids), "preserved_earlier_unique_records": len(prior),
    "last_direct_weekly_telemetry": telemetry,
    "mathematical_computation_or_source_theorem_rerun": False,
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
})
print(json.dumps(output, indent=2, ensure_ascii=False))
