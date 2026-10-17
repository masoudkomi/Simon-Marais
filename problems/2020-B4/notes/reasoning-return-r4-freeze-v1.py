"""Freeze new 2020 r4 prose and metadata only. No mathematical computation.

Run from the repository root:
python3 problems/2020-B4/notes/reasoning-return-r4-freeze-v1.py

Existing outputs are refused. All prior inputs and own frozen records are
read and hashed; no old file, shared register, Git state or cache is changed.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r4-"
SOURCE_PATH = PREFIX + "sources-v1.json"
INPUT_PATH = PREFIX + "input-validation-v1.json"
FREEZE_PATH = PREFIX + "freeze-v1.json"
NOW = datetime.now(timezone.utc).isoformat()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {
        "path": path,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def verify(record):
    actual = fingerprint(record["path"])
    assert actual["sha256"] == record["sha256"], (record, actual)
    if "bytes" in record:
        assert actual["bytes"] == record["bytes"], (record, actual)
    return actual


def write_new(path, value):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


for output_path in (SOURCE_PATH, INPUT_PATH, FREEZE_PATH):
    assert not (ROOT / output_path).exists(), output_path

telemetry = {
    "at_utc": "2026-10-17T12:09:00+00:00",
    "source": "direct account-wide Codex usage tool, paired with UTC clock read",
    "total_used_percent": 36,
    "window_duration_minutes": 10080,
    "resets_at_unix": 1792745187,
    "ordinary_usage_allowed": True,
    "total_used_cutoff_percent": 90,
    "integration_reserve": True,
}

direct_full_reads = [
    "AGENTS.md",
    "problems/2020-B4/statement.md",
    "problems/2020-B4/references.md",
    "problems/2020-B4/issues.md",
    "problems/2020-B4/proofs/partial-v1.md",
    "problems/2020-B4/proofs/reviewed-partial-v1.1.md",
    "problems/2020-B4/proofs/reviewed-return-r3-v1.2.md",
    "problems/2020-B4/reviews/acceptance.md",
    "problems/2020-B4/reviews/acceptance.json",
    "problems/2020-B4/reviews/return-r3-acceptance.md",
    "problems/2020-B4/reviews/return-r3-acceptance.json",
    "problems/2020-B4/notes/reasoning-return-r3-repair-v1.1.md",
    "problems/2020-B4/notes/reasoning-return-r3-sources-v1.1.json",
    "problems/2020-B4/notes/deep-literature-r1-report-v1.md",
    "problems/2020-B4/notes/deep-literature-r1-sources-v1.json",
    "problems/2020-B4/notes/reviewed-source-clarifications-v1.md",
    "problems/2020-B4/reviews/initial-review-2-sources.json",
]
direct_records = [fingerprint(path) for path in direct_full_reads]
verify({"path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
verify({"path": "problems/2020-B4/proofs/partial-v1.md",
        "sha256": "f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525"})
verify({"path": "problems/2020-B4/proofs/reviewed-return-r3-v1.2.md",
        "bytes": 20446,
        "sha256": "18fc1871219740c528527eb1cfb68c2c1571eba0243e4866b5a8630092a91317"})

# Compare the exact full repaired suffix, not only the new status register.
repaired_path = "problems/2020-B4/notes/reasoning-return-r3-candidate-v1.1.md"
repaired_data = (ROOT / repaired_path).read_bytes()
accepted_data = (ROOT / "problems/2020-B4/proofs/reviewed-return-r3-v1.2.md").read_bytes()
assert accepted_data.endswith(repaired_data)
assert len(repaired_data) == 19010
assert hashlib.sha256(repaired_data).hexdigest() == (
    "f6f9947b8140f9d4bafc01ec24bf68dcd7634df5ccba655f4e6cdab334bef467"
)

initial_acceptance = read_json("problems/2020-B4/reviews/acceptance.json")
initial_records = [
    verify({"path": "problems/2020-B4/" + name, "sha256": digest})
    for name, digest in initial_acceptance["artifacts"].items()
]
return_acceptance = read_json("problems/2020-B4/reviews/return-r3-acceptance.json")
return_records = [
    verify(record)
    for record in [return_acceptance["candidate"], return_acceptance["accepted_copy"]]
    + return_acceptance["whole_initial_manifests"]
    + return_acceptance["targeted_manifests"]
]
integrity_path = "problems/2020-B4/reviews/return-r3-acceptance-integrity.json"
integrity = read_json(integrity_path)
assert integrity["all_verified"] is True
integrity_records = [verify(record) for record in integrity["records"]]
assert len(integrity_records) == 761
repair_freeze_path = "problems/2020-B4/notes/reasoning-return-r3-freeze-v1.1.json"
repair_artifacts = [verify(record) for record in read_json(repair_freeze_path)["artifacts"]]
assert len(repair_artifacts) == 8

# The earlier own packet already carries the complete older preservation chain.
prior_manifest_path = "problems/2021-B4/reviews/reasoning-return-r5-review-2-manifest-v1.json"
prior_input_path = "problems/2021-B4/reviews/reasoning-return-r5-review-2-input-checks-v1.json"
prior_manifest = read_json(prior_manifest_path)
verify({"path": prior_manifest_path, "bytes": 3070,
        "sha256": "74c87c1766199f824719ac5b6b82c61a87feb9f6aeeb6ca6c41ea7c77adb284c"})
prior_inputs = read_json(prior_input_path)
older_records = [verify(record) for record in prior_inputs["older_own_records"]]
assert len(older_records) == 177
older_records += [verify(record) for record in prior_manifest["records"]]
older_records += [fingerprint(prior_manifest_path)]
older_by_path = {}
for record in older_records:
    if record["path"] in older_by_path:
        assert record == older_by_path[record["path"]]
    older_by_path[record["path"]] = record
older_records = [older_by_path[path] for path in sorted(older_by_path)]
assert len(older_records) == 183

# Related existing native files are fingerprinted, with no new download claim.
cache_paths = [
    ".cache/official/2020-paper_b.pdf",
    ".cache/literature/2020/initial-review-2/gordon1994.pdf",
    ".cache/literature/2020/initial-review-2/gordon-small-lambda-v1.pdf",
]
cache_records = [fingerprint(path) for path in cache_paths]
for path in cache_paths:
    assert (ROOT / path).read_bytes().startswith(b"%PDF")
verify({"path": cache_paths[2], "bytes": 128808,
        "sha256": "fd92867ab367f70e15a19118e711f84f601dfa835d9c5ab33fb706d3eedf2850"})

sources = {
    "recorded_at_utc": NOW,
    "status": "candidate proof - unverified; constructor source audit",
    "constructor": "review_2022_complexity_r2",
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "scope": "2020 B4(b) only; q=n-1>=2 in all new structural claims",
    "full_external_proofs_all_reconstructed": False,
    "new_native_downloads": False,
    "existing_related_native_cache_fingerprints": cache_records,
    "actual_primary_read_scopes": [
        {
            "key": "official",
            "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf",
            "locator": "page2 B4; (b) only under investigation",
            "read_scope": "Exact official domain and geometric problem read directly; no preliminary proof reproduced",
            "existing_cache_related": cache_paths[0],
            "fresh_web_native_bytes_returned": False,
        },
        {
            "key": "cohen1989",
            "title": "Generators in Cyclic Difference Sets",
            "author": "Stephen D. Cohen",
            "doi": "10.1016/0097-3165(89)90047-2",
            "url": "https://www.researchgate.net/publication/220077727_Generators_in_cyclic_difference_sets",
            "version": "Original JCTA51(1989),227-236; author-uploaded full text",
            "locator": "Definition and Theorem1 printedp227; q4 exception discussion printedp230",
            "read_scope": "Actual original definition, theorem and exception/translation caveat directly read; not entire sieve proof reconstructed",
            "use": "Attributed existence of a unit member of actual D, q!=4; R4C and R4D",
            "hypotheses_checked": ["cyclic actual difference set", "1<k<v-1", "q!=4 excludes both (21,5,1) exceptions", "applied to chosen normalized translate"],
            "new_native_pdf_sha256": None,
            "download_link_status": "Web tool cache miss; no native returned bytes, no download or cleanup claim",
            "full_paper_redistributed": False,
        },
        {
            "key": "gordon1994",
            "url": "https://www.combinatorics.org/ojs/index.php/eljc/article/download/v1i1r6/pdf/",
            "locator": "Section2 printedpp2-3, numerical multiplier definition and Theorems2-4,9",
            "read_scope": "Actual primary theorem statements read directly; no fresh audit of original Hall/Ho proofs",
            "use": "Accepted divisor-multiplier context and classical bound attribution; R4B proves its own bound",
            "existing_cache_related": cache_paths[1],
            "new_native_download": False,
        },
        {
            "key": "gordon2020v1",
            "url": "https://arxiv.org/pdf/2007.07292v1",
            "title": "On difference sets with small lambda",
            "locator": "Theorem4 and complete Theorem5 proof printedpp3-4; Theorem6 collision statement",
            "read_scope": "Actual primary statements and Cohen-based degree proof read; journal theorem numbering differs",
            "use": "Classical context; no contracted-multiplier or collision theorem used as unproved replacement for R4A/B",
            "existing_cache_related": cache_paths[2],
            "new_native_download": False,
        },
        {
            "key": "baumert-gordon2003",
            "url": "https://arxiv.org/pdf/math/0304502",
            "locator": "Section5 Theorem5.1 printedp7",
            "read_scope": "Actual primary theorem statement and context read; original Evans-Mann/Lander proofs not imported",
            "use": "Attribution and exact distinction from the present cyclic planar noncollision reconstruction",
            "new_native_pdf_sha256": None,
        },
        {
            "key": "xia2023v7",
            "url": "https://arxiv.org/pdf/1707.05486v7",
            "title": "New necessary conditions for the existence of finite non-Desarguesian flag-transitive projective planes",
            "locator": "Introductionpp1-3, Proposition1.2, Theorem1.3 domain, cyclotomic definition and prior-work discussion",
            "read_scope": "Actual active v7 primary text; no full Gauss-sum proof or polynomial system theorem imported",
            "use": "Context and hypothesis caution only; index L versus subgroup order m kept distinct",
            "new_native_pdf_sha256": None,
            "withdrawn_v5_used": False,
            "substantive_theorem_import": False,
        },
    ],
    "not_directly_read_not_imported": [
        "Original full Cohen character-sum/sieve proof beyond the assigned statement and exception passages",
        "Original full Hall/Ho/Evans-Mann/Lander proofs",
        "Thas-Zagier2008 full proof and Xia2018 full cyclotomic proof",
        "Xia2023 full non-Desarguesian flag-transitive theorems",
    ],
    "new_R4E_symbolic_moment_proof": "Complete elementary argument in candidate, not an external theorem import or a finite computation",
    "existing_BBB_raw_hash_limitation_preserved": True,
    "direct_full_local_document_or_register_reads": direct_records,
    "no_mathematical_scans_CAS_author_reruns_contacts_charges_bypass": True,
    "direct_weekly_telemetry": telemetry,
}

metadata_extra = [fingerprint(path) for path in (
    integrity_path, repair_freeze_path, prior_manifest_path, prior_input_path,
)]
all_input_records = (
    direct_records + initial_records + return_records + integrity_records
    + repair_artifacts + older_records + cache_records + metadata_extra
)
source_checks = {
    "checked_at_utc": NOW,
    "metadata_only_not_mathematical_evidence": True,
    "scope": "2020 r4 new construction with exact accepted inputs; not independent review",
    "direct_full_document_or_register_reads": direct_records,
    "initial_acceptance_fingerprint_records_verified": initial_records,
    "repaired_return_acceptance_records_verified": return_records,
    "repaired_return_acceptance_integrity_occurrences_verified": integrity_records,
    "repaired_author_eight_records_verified": repair_artifacts,
    "accepted_repaired_body_exact_byte_suffix_verified": True,
    "old_false_v1_both_initials_and_exact_counterexample_preserved": True,
    "older_own_records": older_records,
    "older_own_unique_paths_verified_unchanged": len(older_records),
    "related_existing_source_cache_records": cache_records,
    "metadata_registers": metadata_extra,
    "record_occurrences_verified": len(all_input_records),
    "unique_paths_verified": len({r["path"] for r in all_input_records}),
    "all36_author_obligations_checked_analytically_pending_two_whole_audits": True,
    "Cohen_full_proof_is_attributed_import_not_fresh_reconstruction": True,
    "classical_overlap_and_failed_novelty_route_explicit": True,
    "actual_integer_lift_from_all_prime_field_moments_written": True,
    "full_unrestricted_classification_or_numerical_answer_or_novelty": False,
    "mathematical_program_scan_CAS_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_or_cache_writes": False,
    "spawning_contacts_charges_or_access_bypass": False,
    "only_new_assigned_prefix_written": True,
    "administrative_freeze_command": "python3 problems/2020-B4/notes/reasoning-return-r4-freeze-v1.py",
    "direct_weekly_telemetry": telemetry,
    "all_verified": True,
}

write_new(SOURCE_PATH, sources)
write_new(INPUT_PATH, source_checks)
artifacts = [fingerprint(PREFIX + suffix) for suffix in (
    "candidate-v1.md", "obligations-v1.md", "source-checks-v1.md",
    "worklog-v1.md", "freeze-v1.py", "sources-v1.json",
    "input-validation-v1.json",
)]
freeze = {
    "frozen_at_utc": NOW,
    "status": "candidate proof - unverified; complete scoped conceptual construction checkpoint",
    "constructor": "review_2022_complexity_r2",
    "root_contributed_to_this_new_R4_construction": False,
    "requested_model": "gpt-6.1-sol",
    "requested_reasoning_effort": "max",
    "verified_effective_setting_readback": None,
    "scope": "2020 B4(b); R4A-R4E partial structural claims, q>=2 with exact q4 exclusions",
    "claims": ["R4A", "R4B", "R4C", "R4D", "R4E"],
    "author_obligations": 36,
    "requires_two_fresh_initially_blind_nonconstructor_whole_audits": True,
    "independent_audits_already_obtained_for_new_packet": 0,
    "coordinator_promotion": False,
    "Cohen_generator_theorem_attributed_import": True,
    "new_external_full_proofs_all_reconstructed": False,
    "whole_mathematical_argument_and_exact_scope_written": True,
    "complete_moment_system_solved_for_unbounded_parameters": False,
    "nonsaturated_multiplier_branch_resolved": False,
    "full_annual_classification_numerical_answer_or_novelty_claim": False,
    "mathematical_program_scan_CAS_certificate_or_author_rerun": False,
    "old_shared_Git_cache_writes_spawning_contacts_charges_bypass": False,
    "input_record_occurrences_verified": len(all_input_records),
    "input_unique_paths_verified": len({r["path"] for r in all_input_records}),
    "older_own_frozen_paths_preserved": len(older_records),
    "accepted2020R3_integrity_occurrences_rechecked": len(integrity_records),
    "direct_weekly_telemetry": telemetry,
    "artifacts": artifacts,
}
write_new(FREEZE_PATH, freeze)
print(json.dumps({
    "freeze": fingerprint(FREEZE_PATH),
    "artifacts": artifacts,
    "input_record_occurrences_verified": len(all_input_records),
    "input_unique_paths_verified": len({r["path"] for r in all_input_records}),
    "older_own_frozen_paths_preserved": len(older_records),
    "all_verified": True,
}, indent=2, ensure_ascii=False))
