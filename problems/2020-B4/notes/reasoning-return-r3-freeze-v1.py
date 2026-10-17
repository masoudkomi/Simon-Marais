"""Administrative immutable-byte checks and new freeze; no mathematics."""
from pathlib import Path
import hashlib
import json
import datetime

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r3-"


def row(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def check(expected):
    actual = row(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def write(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as out:
        json.dump(obj, out, ensure_ascii=False, indent=2)
        out.write("\n")
    return row(path)


inputs = [row(p) for p in [
    "AGENTS.md", "problems/2020-B4/statement.md", "problems/2020-B4/references.md",
    "problems/2020-B4/research.md", "problems/2020-B4/proofs/reviewed-partial-v1.1.md",
    "problems/2020-B4/notes/reviewed-source-clarifications-v1.md",
    "problems/2020-B4/reviews/acceptance.md", "problems/2020-B4/reviews/acceptance.json",
    "problems/2020-B4/notes/deep-literature-r1-report-v1.md",
    "problems/2020-B4/notes/deep-literature-r1-sources-v1.json",
    "problems/2020-B4/notes/deep-literature-r1-manifest-v1.json",
]]
check({"path": "AGENTS.md", "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
check({"path": "problems/2020-B4/proofs/partial-v1.md", "sha256": "f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525"})
accepted = json.loads((ROOT / "problems/2020-B4/reviews/acceptance.json").read_text())
accepted_preserved = [check({"path": "problems/2020-B4/"+p, "sha256": s})
                      for p, s in accepted["artifacts"].items()]
deep = json.loads((ROOT / "problems/2020-B4/notes/deep-literature-r1-manifest-v1.json").read_text())
deep_preserved = [check(r) for r in deep["artifacts"]]

old_manifest = check({"path": "problems/2017-B4/notes/rank-mesh-reasoning-r1-freeze-v1.json",
                      "sha256": "7173ee9db5d7990af60ca0731a301d9017691e42f9c741efce1e81a7d90de747"})
old = json.loads((ROOT / old_manifest["path"]).read_text())
own_preserved = {old_manifest["path"]: old_manifest}
for expected in old["artifacts"]:
    actual = check(expected)
    own_preserved[actual["path"]] = actual
validation = json.loads((ROOT / "problems/2017-B4/notes/rank-mesh-reasoning-r1-input-validation-v1.json").read_text())
for expected in validation["all_prior_frozen_rows_preserved"]:
    actual = check(expected)
    own_preserved[actual["path"]] = actual

suffixes = ["candidate-v1.md", "source-checks-v1.md", "obligations-v1.md",
            "worklog-v1.md", "sources-v1.json", "freeze-v1.py"]
for suffix in suffixes[:4]:
    assert "Candidate proof - unverified" in (ROOT / (PREFIX+suffix)).read_text() or "candidate proof - unverified" in (ROOT / (PREFIX+suffix)).read_text()
sources = json.loads((ROOT / (PREFIX+"sources-v1.json")).read_text())
assert sources["primary_source"]["sha256"] is None
assert not sources["mathematical_computation_enumeration_or_CAS"]

validation_row = write("input-validation-v1.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "current_read_inputs": inputs,
    "accepted_2020_artifacts_preserved": accepted_preserved,
    "deep_literature_artifacts_preserved": deep_preserved,
    "earlier_own_frozen_unique_records_preserved": sorted(own_preserved.values(), key=lambda r: r["path"]),
    "earlier_own_unique_count": len(own_preserved),
    "source_bytes_hash_unresolved": True,
    "no_mathematical_computation_or_CAS": True
})
artifacts = [row(PREFIX+s) for s in suffixes] + [validation_row]
manifest = write("freeze-v1.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "candidate proof - unverified; classical reconstructions and restricted corollary, requiring two fresh whole audits",
    "constructor": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "scope": "2020 B4(b) only",
    "claims": ["F1 common fixed-subgroup closure", "F1a cofactor/7p obstruction", "F2 involution fiber proof", "F2a 2-part coherence", "F3 original BBB relative trace", "F3a exact remaining lift", "B1 positive-definite relaxation barrier"],
    "artifacts": artifacts,
    "accepted_2020_and_deep_literature_bytes_unchanged": True,
    "earlier_own_frozen_unique_records_preserved": len(own_preserved),
    "original_BBB_applicable_text_directly_read": True,
    "original_BBB_pdf_sha256": None,
    "original_Mann_proof_imported": False,
    "source_integrity_limitation": "Byte-hash request stalled and was interrupted; no PID/output; no verified OS cleanup claimed",
    "mathematical_computation_enumeration_or_CAS": False,
    "preliminary_a_reproduced": False,
    "no_q2304_or_old_norm_filter_rerun": True,
    "novelty_or_new_published_cutoff_claimed": False,
    "prime_power_conjecture_assumed": False,
    "full_classification_proved": False,
    "requires_two_fresh_independent_nonconstructor_whole_reviews": True,
    "no_git_shared_status_spawning_contacts_charges_or_bypass": True,
    "only_assigned_return_prefix_written": True,
    "latest_authoritative_weekly_total_used_percent": 26,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "earlier_own_unique_records_preserved": len(own_preserved)}, indent=2))
