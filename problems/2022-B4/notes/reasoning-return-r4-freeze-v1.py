"""One-time E1-E2/V1-V4 freeze: byte verification, not mathematical tests."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/notes/reasoning-return-r4-"


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


sources = read(PREFIX + "sources-v1.json")
protocol = check({"path": "AGENTS.md", "bytes": 4707,
                  "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
statement = row("problems/2022-B4/statement.md")
accepted = [row(path) for path in sources["complete_accepted_bodies_read"]]
context = [row(path) for path in sources["additional_full_context_read"]]
raw_sources = [check({"path": src["cache_path"], "bytes": src["bytes"],
                      "sha256": src["sha256"]})
               for src in sources["primary_sources"] if "cache_path" in src]
assert len(accepted) == 4 and len(raw_sources) == 3

old_path = "problems/2017-B4/reviews/allD-uniform-strict-review-1-manifest-initial.json"
old_manifest = check({"path": old_path, "bytes": 3360,
                      "sha256": "9037242ee986643789c5e5ec966b19f2a59aa2dd881998727f8fcb444609262f"})
preserved = {old_path: old_manifest}
for expected in read(old_path)["artifacts"]:
    actual = check(expected)
    preserved[actual["path"]] = actual
for expected in read("problems/2017-B4/reviews/allD-uniform-strict-review-1-input-validation.json")["earlier_unique_records_preserved"]:
    actual = check(expected)
    if actual["path"] in preserved:
        assert preserved[actual["path"]] == actual
    preserved[actual["path"]] = actual
assert len(preserved) == 187, len(preserved)

validation = write("input-validation-v1.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "protocol": protocol,
    "official_statement": statement,
    "all_four_complete_accepted_bodies": accepted,
    "complete_deep_literature_and_acceptance_context": context,
    "all_three_cached_primary_raw_sources": raw_sources,
    "raw_cache_hash_does_not_claim_whole_source_read": True,
    "earlier_unique_records_preserved": sorted(preserved.values(), key=lambda r: r["path"]),
    "earlier_unique_count": len(preserved),
    "no_new_allD_global_candidate_or_peer_findings_read": True,
    "new_mathematical_program_CAS_scan_or_finite_certificate": False,
    "pypdf_four_page_read_was_not_a_mathematical_job": True,
    "only_assigned_r4_note_prefix_written": True,
})
artifacts = [row(PREFIX + suffix) for suffix in [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "sources-v1.json", "freeze-v1.py",
]] + [validation]
assert len(artifacts) == 8
manifest = write("freeze-v1.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "candidate proof - unverified; complete E1-E2/V1-V4 construction and explicit unresolved bridge, awaiting two other fresh whole audits",
    "constructor": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["E1 constant-translate admissible rational-base expansion lemma",
               "E2 positive ordinary AB lift implies at least nine base11/10 expansions",
               "V1 exact balanced-prime valuations and accelerated ordinary return",
               "V2 exact negative fixedpoint and first-two-B power100 shadow criteria",
               "V3 Phi two-prime isometry and arbitrary finite post-B continuation",
               "V4 ordinary target81 has inverse-limit but no nonnegative ordinary Phi1 preimage"],
    "fresh_whole_audit_obligations": 28,
    "artifacts": artifacts,
    "earlier_unique_frozen_own_records_preserved": len(preserved),
    "no_ninefold_bridge_is_an_unproved_hypothesis": True,
    "AFS_at_most_two_range_p_ge_2q_minus_1_satisfied_at_11_over_10": False,
    "ninth_expansion_is_claimed_a_ninth_ceiling_orbit": False,
    "digit10_kept_for_ninth_full_alphabet_path": True,
    "every_infinite_lift_or_exponent_claimed_ordinary": False,
    "finite_Phi_bijections_claimed_ordinary_surjectivity": False,
    "full_contest_termination_or_positive_infinite_counterexample_claim": False,
    "novelty_or_author_promotion_claim": False,
    "requires_two_other_initially_blind_whole_audits": True,
    "mathematical_program_CAS_enumeration_scan_or_certificate": False,
    "native_paper_download_or_full_third_party_tracked_copy": False,
    "git_shared_mutation_spawning_charges_contacts_or_bypass": False,
    "only_assigned_r4_prefix_written": True,
    "last_direct_weekly_telemetry": sources["latest_direct_weekly_telemetry"],
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "accepted_bodies": accepted,
                  "raw_sources": raw_sources,
                  "earlier_unique_frozen_own_records_preserved": len(preserved)}, indent=2))
