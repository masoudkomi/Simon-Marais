"""Freeze a new mathematical construction; byte hashing only, no math search."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/notes/reasoning-return-r3-"


def fingerprint(path):
    payload = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest()}


def check(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def create_json(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")
    return path


now = datetime.now(timezone.utc).isoformat()
expected_inputs = [
    ("AGENTS.md", "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    ("problems/2019-B4/statement.md", "53d4201dca8bc4a77d995e3df14f95dd146e2df0c82d3b6447ad35a348e89de9"),
    ("problems/2019-B4/proof.md", "58f140f1fe9c64aa77d04a9c80a76f13411264d09d5f9e908f8e0997dc6985e2"),
    ("problems/2019-B4/proofs/reviewed-secondpass-v1.1.md", "5fbaa388fe2ff795034094823c088fa5402da60eb9eca83f78165df0c8ad2cd7"),
    ("problems/2019-B4/notes/secondpass-canonical-renewal.md", "886266000a34023b033099889a3bb23bc6b3e642194ded12ce53b3aaa1642763"),
    ("problems/2019-B4/notes/secondpass-rigidity-obstructions.md", "58112ed40ba7146c8b5885669602d44770bdd525540c4221eaf17b101eb1c109"),
    ("problems/2019-B4/notes/secondpass-staircases-and-pumping.md", "5e2539982e32d116076c2c17ad8e85d865792a14630db04634c7372ae345cd52"),
    ("problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md", "58462ad7e44a7d3477d086a663cdb127128c5adcae65d6a904f1fdaa7e862cbf"),
    ("problems/2019-B4/notes/thirdpass-bounded-separation-v1.md", "3364e8c6cf23ba3ecb250f13a5873732c108b6904a68126f52f5d7234eb916d4"),
    ("problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md", "b9d934da65eedf4514ef7883e29dda98ee846982e89c8e3ee677f2c96bff2ee8"),
    ("problems/2019-B4/notes/thirdpass-literature.md", "90ed53bc773b79d2fc0790b5972757f73ca03026c3c42b7ecf733acd1a622b83"),
    ("problems/2019-B4/notes/thirdpass-literature-sources.json", "b131a9bef91787088f5fc2daef120b93c3a68c7221031904dc19ad9dbacda4e8"),
    ("problems/2019-B4/reviews/acceptance.md", "9a4c893182bf84dec4b00a86268f9b1d24f39ba1f54c11fe08695777eb20d7b8"),
    ("problems/2019-B4/reviews/secondpass-acceptance.md", "a167e1f52bff2503c6ac571ea047efe7621425f2379868a0a6db31eccd22aefa"),
    ("problems/2019-B4/reviews/thirdpass-acceptance.md", "3aa35ed0db260b45394676681426fa5c504e7414d9bbad143ac1eed65ffb105f"),
    ("problems/2019-B4/reviews/moment-tail-acceptance.md", "d3647718f04eb1a67dce90b5ffb103cdefc4400dc86d64103e828a199b6e064e"),
    (".cache/official/2019-paper_b.pdf", "5d7dbea3566e5b34bd84fa517ba2c5bf0258459db3a980988008490169be46bb"),
]
input_checks = [check({"path": path, "sha256": sha}) for path, sha in expected_inputs]
context_checks = [fingerprint("problems/2019-B4/" + path) for path in [
    "research.md", "references.md", "notes/coordinator-two-tape-directions.md",
]]
raw_source_checks = []
for row in read_json("problems/2019-B4/notes/thirdpass-literature-sources.json")["full_papers"]:
    raw_source_checks.append(check({"path": row["cache_path"],
                                    "bytes": row["bytes"], "sha256": row["sha256"]}))
assert len(raw_source_checks) == 6

prior_path = "problems/2024-B4/reviews/reasoning-return-r3-review-2-manifest-v1.json"
prior_fp = check({"path": prior_path, "bytes": 2862,
                  "sha256": "3c6339e2715e1a6c5fa53f314ab280c6406177858e09864e10869b8262b6a6e4"})
prior_checks = [check(row) for row in read_json(prior_path)["records"]]
prior_validation = read_json("problems/2024-B4/reviews/reasoning-return-r3-review-2-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 33
older.append({"manifest": prior_fp, "checks": prior_checks})

obligations = read_json(PREFIX + "obligations-v1.json")
assert len(obligations["obligations"]) == 20
assert obligations["claims"] == ["NR1", "NR2", "NR3", "NR4"]

sources_path = create_json("sources-v1.json", {
    "created_at_utc": now,
    "status": "candidate proof - unverified",
    "accepted_and_protocol_input_fingerprints": input_checks,
    "additional_context_fingerprints": context_checks,
    "public_cached_source_fingerprints": raw_source_checks,
    "raw_hash_implies_full_paper_read": False,
    "fresh_primary_reads": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
         "scope": "p2 B4(b) full official domain; no preliminary proof",
         "role": "authoritative target"},
        {"url": "https://cs.nyu.edu/~mohri/pub/edit.pdf",
         "scope": "section4.3 Definition9 and Lemmas1–2 bounded delay and residual finiteness",
         "role": "method/hypothesis boundary, no imported exact-recognizer theorem"},
        {"url": "https://eiche.theoinf.tu-ilmenau.de/kuske/Publications/HusKZ14.pdf",
         "scope": "section3 definition, Theorem4.1 normal-form context, section8 product embedding statement",
         "role": "different transformation equivalence; not identified with B4 context equality"},
    ],
    "new_mathematical_theorem_from_external_paper_imported": False,
    "standard_finite_methods": ["DFA pumping on fixed pair boundaries",
                                "regular closure and right-language minimization",
                                "finite Perron–Frobenius existence with irreducibility",
                                "written strict comparison for reducible edge deletion"],
    "complete_deep_primary_report_read": True,
    "novelty_or_search_absence_proof_claim": False,
    "native_network_download_contact_charge_or_bypass": False,
})
validation_path = create_json("input-validation-v1.json", {
    "validated_at_utc": now,
    "protocol_accepted_source_inputs": input_checks,
    "context_records": context_checks,
    "six_raw_source_checks": raw_source_checks,
    "older_own_packets": older,
    "all_thirty_four_older_own_packets_unchanged": True,
    "active_2017_global_or_future_2024_generalization_read": False,
    "mathematical_program_CAS_or_enumeration": False,
    "old_math_certificates_rerun": False,
    "only_assigned_new_prefix_written": True,
    "standard_Perron_comparison_hypotheses_written_in_full": True,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; complete NR1–NR4 checkpoint",
    "fixed_input_records_checked": len(input_checks),
    "additional_context_records": len(context_checks),
    "raw_source_records_checked": 6,
    "older_own_packets_checked": 34,
    "fresh_audit_obligations": 20,
    "all_fingerprints_match": True,
    "two_fresh_other_whole_reviews_still_required": True,
    "mathematical_computation_or_CAS": False,
    "exact_lambda_or_new_numerical_bound_claim": False,
    "candidate_or_shared_old_file_mutation": False,
    "git_operations_or_spawning": False,
})
records = [PREFIX + name for name in [
    "candidate-v1.md", "researchlog-v1.md", "source-audit-v1.md",
    "obligations-v1.json", "freeze-v1.py",
]] + [sources_path, validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified",
    "constructor": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "scope": "2019 B4(b) exact obstruction-language structure, not evaluated growth",
    "claims": ["NR1 unrestricted alternating-block prefix budget",
               "NR2 nonregular exact minimal/canonical and synchronous-equality languages",
               "NR3 strict growth gap for every regular subset of actual minimal obstructions",
               "NR4 explicit cap reset and every finite cap above lambda"],
    "two_fresh_other_initially_blind_whole_audits_required": True,
    "constructor_can_count_as_independent_reviewer": False,
    "fresh_review_obligation_rows": 20,
    "records": [fingerprint(path) for path in records],
    "older_own_packets_preserved": 34,
    "mathematical_program_enumeration_or_CAS": False,
    "larger_cap_or_numerical_tightening": False,
    "exact_growth_or_series_nonalgebraicity_or_novelty_claim": False,
    "different_regular_cross_section_or_original_B_language_nonregularity_claim": False,
    "active_2017_global_or_future_2024_generalization_read": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "weekly_total_used_percent": 31,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2019-B4/notes/reasoning-return-r3-freeze-v1.py",
})
print(json.dumps({"frozen_at_utc": now,
                  "candidate": fingerprint(PREFIX + "candidate-v1.md"),
                  "manifest": fingerprint(manifest_path),
                  "record_count": len(records),
                  "older_own_packets_preserved": 34,
                  "all_input_fingerprints_match": True}, indent=2))
