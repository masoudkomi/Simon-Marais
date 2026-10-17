"""One-time administrative CP1--CP3 freeze; no mathematical program rerun."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/notes/reasoning-return-r3-"


def row(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def check(expected):
    actual = row(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def read(path):
    return json.loads((ROOT / path).read_text())


def write(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return row(path)


protocol = [check(expected) for expected in [
    {"path": "AGENTS.md", "bytes": 4707,
     "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"},
    {"path": "problems/2024-B4/statement.md", "bytes": 2470,
     "sha256": "60244f7752634772adb434efbdb41a63fb02029dc3be4238f3718c6e5ec84e5f"},
]]
accepted_and_context = [row(path) for path in [
    "problems/2024-B4/proofs/reviewed-structural-v1.1.md",
    "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
    "problems/2024-B4/proofs/fixed-factor-family-reviewed-v1.1.md",
    "problems/2024-B4/proofs/reviewed-divisor-criteria-v1.1.md",
    "problems/2024-B4/notes/deep-literature-r2-report-v1.md",
    "problems/2024-B4/notes/deep-literature-r2-kasami-orbit-lead-v1.md",
    "problems/2024-B4/notes/deep-literature-r2-search-sources-v1.json",
    "problems/2024-B4/notes/structural-reasoning-r2-sources-v1.json",
    "problems/2024-B4/research.md",
    "problems/2024-B4/references.md",
]]
check({"path": "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
       "bytes": 16607,
       "sha256": "362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226"})
raw_sources = [check(expected) for expected in [
    {"path": ".cache/official/2024-paper_b.pdf", "bytes": 151590,
     "sha256": "1401f21218ad4c387c4d537ed8fd7de119b376cba52957ef788c772dc5ab4ddc"},
    {"path": ".cache/literature/2024/cited-3e7f3cb84c20c6b1.pdf", "bytes": 198696,
     "sha256": "bc9389858756658a7a2769a74ebb40b4df05523ddfe24a4639cd7d79ef31df16"},
    {"path": ".cache/literature/deep-literature-r2/2024-delgado-janwa-1612.05997v1.pdf",
     "bytes": 191161,
     "sha256": "9704f18d5acbec194e89ab26eed3c0a39d944a3de0c73896e4a05269c18528d9"},
    {"path": ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf",
     "bytes": 2610589,
     "sha256": "d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24"},
]]

old_path = "problems/2017-B4/reviews/local-rank-mesh-review-1-manifest-initial.json"
old_manifest = check({"path": old_path, "bytes": 2929,
                      "sha256": "bb11c533e2fd9c28a28a5bf0ee84c3ed97d41be6006347b03cc3a604144d2201"})
preserved = {old_path: old_manifest}
for expected in read(old_path)["artifacts"]:
    actual = check(expected)
    preserved[actual["path"]] = actual
for expected in read("problems/2017-B4/reviews/local-rank-mesh-review-1-input-validation.json")["earlier_unique_records_preserved"]:
    actual = check(expected)
    if actual["path"] in preserved:
        assert preserved[actual["path"]] == actual
    preserved[actual["path"]] = actual
assert len(preserved) == 165, len(preserved)

job = read(PREFIX + "kasami-target-job-v1.json")
completion = read(PREFIX + "kasami-target-completion-v1.json")
assert job["child_pid"] == completion["child_pid"] == 95340
assert job["parent_pid"] == 95339 and job["timeout_seconds"] == 10
assert completion["return_code"] == 0 and not completion["timed_out"]
assert completion["child_reaped"] is True
for stream in ("stdout", "stderr"):
    assert row(PREFIX + "kasami-target-" + stream + "-v1.txt")["sha256"] == completion[stream + "_sha256"]

validation = write("input-validation-v1.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "protocol_and_official_statement": protocol,
    "accepted_and_context_records": accepted_and_context,
    "cached_public_source_raw_records": raw_sources,
    "raw_source_role": "Previously cached bytes preserved; actual reading scope is in source audit, not inferred from hashing",
    "earlier_unique_records_preserved": sorted(preserved.values(), key=lambda r: r["path"]),
    "earlier_unique_count": len(preserved),
    "exact_target_q8_job_and_stream_hashes_verified": True,
    "mathematical_child_rerun": False,
    "peer_CP_review_read": False,
    "author_is_not_independent_reviewer": True,
})
artifacts = [row(PREFIX + suffix) for suffix in [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "sources-v1.json",
    "kasami-target-check-v1.py", "kasami-target-run-v1.py",
    "kasami-target-job-v1.json", "kasami-target-completion-v1.json",
    "kasami-target-stdout-v1.txt", "kasami-target-stderr-v1.txt",
    "kasami-target-certificate-v1.json", "freeze-v1.py",
]] + [validation]
assert len(artifacts) == 15
manifest = write("freeze-v1.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "candidate proof - unverified; complete CP1--CP3 construction awaiting two other fresh whole audits",
    "constructor": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "whole_claims": ["CP1 all whole fixed divisors iff F2 univariate composition",
                     "CP2 unrestricted q=2^k composition identity including k1/k2 endpoints",
                     "CP3 genuine k>=3 family, v2=k, outside accepted whole-phi13 progression"],
    "fresh_audit_obligations": 16,
    "artifacts": artifacts,
    "earlier_unique_frozen_records_preserved": len(preserved),
    "accepted_phi13_criterion_used_only_for_progression_comparison": True,
    "APN_absolute_component_or_monodromy_theorem_import": False,
    "finite_q8_certificate_is_proof_premise": False,
    "math_child": {"pid": 95340, "harness_pid": 95339,
                   "external_timeout_seconds": 10, "return_code": 0,
                   "reaped": True, "scope": "single q8,d57,N3641 univariate symbolic corroboration"},
    "q2_endpoint_genuine_factor_claim": False,
    "q4_old205_context_attributed_and_not_rerun": True,
    "all_m_general_q_family_AS_S4_or_full_classification_claim": False,
    "novelty_claim": False,
    "author_promotion_or_independent_review_claim": False,
    "only_assigned_prefix_written": True,
    "git_shared_mutation_spawning_contacts_charges_or_bypass": False,
    "weekly_total_used_percent": 29,
    "telemetry_at_utc": "2026-10-17 07:27:04 UTC",
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "earlier_unique_frozen_records_preserved": len(preserved)}, indent=2))
