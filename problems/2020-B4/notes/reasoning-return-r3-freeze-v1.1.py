"""Administrative byte checks and versioned freeze; no mathematical computation."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json

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


def read(path):
    return json.loads((ROOT / path).read_text())


def write(suffix, data):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as out:
        json.dump(data, out, ensure_ascii=False, indent=2)
        out.write("\n")
    return row(path)


preserved = {}


def retain(expected):
    actual = check(expected)
    previous = preserved.get(actual["path"])
    assert previous is None or previous == actual
    preserved[actual["path"]] = actual
    return actual


pn_path = "problems/2021-B4/reviews/odd-support-exclusion-review-2-manifest-initial.json"
retain({"path": pn_path, "sha256": "63408a4584f966cd1e0db5f456bad44fa16a05e6dac5a039fc954012fe0df58b"})
pn = read(pn_path)
for expected in pn["artifacts"]:
    retain(expected)
pn_validation = read("problems/2021-B4/reviews/odd-support-exclusion-review-2-input-validation.json")
for expected in pn_validation["earlier_unique_records_preserved"]:
    retain(expected)
assert len(preserved) == 132

initials = []
for number, key, sha in [
    (1, "files", "cf3dcc0cfe57356ec3b61f8898403a8c2a6d6f6661f579e43080bdf313c1d7d1"),
    (2, "records", "bbda561c3d8379666e92308ae851de4f46c042548f4d4e3bf6bcdc0ba01b07b6"),
]:
    path = f"problems/2020-B4/reviews/reasoning-return-r3-review-{number}-manifest-v1.json"
    initials.append(retain({"path": path, "sha256": sha}))
    for expected in read(path)[key]:
        retain(expected)
assert len(preserved) == 144

old_path = PREFIX + "freeze-v1.json"
retain({"path": old_path, "sha256": "413351e9d6d6b9e8c463ba6b3ad230f2d4440c5042711df882f879a7b82a02ed"})
for expected in read(old_path)["artifacts"]:
    retain(expected)
original_validation = read(PREFIX + "input-validation-v1.json")
accepted_dependencies = [check(expected) for expected in original_validation["accepted_2020_artifacts_preserved"]]
deep_dependencies = [check(expected) for expected in original_validation["deep_literature_artifacts_preserved"]]
check({"path": "AGENTS.md", "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})

old_main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
new_main = (ROOT / (PREFIX + "candidate-v1.1.md")).read_text()
builder_path = ROOT / (PREFIX + "build-v1.1.py")
builder = builder_path.read_text()
# Run only the read-and-replace prefix, before either exclusive-write call.
namespace = {"__file__": str(builder_path)}
exec(compile(builder.split("\nout_path=", 1)[0], str(builder_path), "exec"), namespace)
assert namespace["new"] == new_main
expected_diff = "".join(difflib.unified_diff(
    old_main.splitlines(True), new_main.splitlines(True),
    fromfile="reasoning-return-r3-candidate-v1.md",
    tofile="reasoning-return-r3-candidate-v1.1.md"))
assert (ROOT / (PREFIX + "diff-v1.1.patch")).read_text() == expected_diff

sources = read(PREFIX + "sources-v1.1.json")
assert sources["repair_id"] == "2020R2-01"
assert sources["source_claims_unchanged"]["raw_pdf_sha256"] is None
assert not sources["mathematical_program_enumeration_or_CAS"]
assert not sources["author_promotion"]
for suffix in ["candidate-v1.1.md", "repair-v1.1.md", "worklog-v1.1.md"]:
    assert "Candidate proof - unverified" in (ROOT / (PREFIX + suffix)).read_text()

validation = write("input-validation-v1.1.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "original_candidate": row(PREFIX + "candidate-v1.md"),
    "original_freeze": row(old_path),
    "both_complete_initials_manifests": initials,
    "all_earlier_unique_frozen_records_preserved": sorted(preserved.values(), key=lambda r: r["path"]),
    "earlier_unique_count": len(preserved),
    "accepted_2020_dependencies_preserved": accepted_dependencies,
    "deep_literature_dependencies_preserved": deep_dependencies,
    "full_replacement_matches_builder_and_exact_diff": True,
    "source_raw_byte_hash_still_unresolved": True,
    "mathematical_program_or_CAS": False,
})
suffixes = ["candidate-v1.1.md", "repair-v1.1.md", "worklog-v1.1.md",
            "sources-v1.1.json", "diff-v1.1.patch", "build-v1.1.py", "freeze-v1.1.py"]
artifacts = [row(PREFIX + suffix) for suffix in suffixes] + [validation]
manifest = write("freeze-v1.1.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "candidate proof - unverified; full author versioned repair of 2020R2-01",
    "constructor": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "scope": "2020 B4(b) only; no full classification or preliminary construction",
    "repair": "F4 uses H_t=G^<t>, h_t,f_t,m_t; recursive restricted-action hypotheses reset",
    "actual_q4_counterexample_preserved_by_hand": True,
    "all_F1_F1a_F2_F2a_F3_F3a_B1_downstream_uses_checked": True,
    "artifacts": artifacts,
    "original_and_both_initial_reviews_and_prior_frozen_bytes_preserved": len(preserved),
    "both_original_auditors_affected_reaudits_required": True,
    "author_promotion": False,
    "new_theorem_extension_novelty_or_new_published_cutoff_claim": False,
    "no_new_source_import_or_native_retrieval": True,
    "original_BBB_raw_pdf_sha256": None,
    "mathematical_program_enumeration_or_CAS": False,
    "only_assigned_return_prefix_written": True,
    "git_shared_edits_spawning_contacts_charges_or_bypass": False,
    "weekly_total_used_percent": 27,
    "telemetry_at_utc": "2026-10-17 06:44:58 UTC",
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "earlier_unique_frozen_records_preserved": len(preserved)}, indent=2))
