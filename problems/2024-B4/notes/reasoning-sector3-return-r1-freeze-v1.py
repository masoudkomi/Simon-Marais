"""Create-new administrative freeze. NO mathematical computation or test.

Checks fingerprints/read-scope records and36 obligation labels only.
Never mutates an input, old artifact, cache, shared file or Git state.
Use a NEW version/prefix for any reproduction after the first freeze.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/notes/reasoning-sector3-return-r1-"
STAMP = datetime.datetime.now(datetime.timezone.utc).isoformat()


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def canonical_digest(rows):
    value = sorted(rows, key=lambda row: row["path"])
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def write_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    return record(path)


for suffix in ["sources-v1.json", "input-validation-v1.json", "freeze-v1.json"]:
    assert not (ROOT / (PREFIX + suffix)).exists(), suffix

baseline_path = PREFIX + "baseline-v1.json"
baseline = read_json(baseline_path)
assert baseline["unused_fresh_prefix_confirmed"] is True
assert baseline["old_R3_prefix_occupied_files"] == 16
assert baseline["record_occurrences"] == baseline["deduplicated_paths"] == 44
for row in baseline["direct_inputs_and_occupied_prefix_and_source_bytes"]:
    assert record(row["path"]) == row, row["path"]
assert canonical_digest(baseline["direct_inputs_and_occupied_prefix_and_source_bytes"]) == baseline["canonical_record_array_sha256"]

parent = baseline["immutable_parent_manifest"]
assert parent == record(parent["path"])
assert parent["sha256"] == "d0c587428aa42027a22e2ea954f79a4c51596883658d0917038fafdd08152242"
parent_body = read_json(parent["path"])
for row in parent_body["artifacts"]:
    assert record(row["path"]) == row
assert len(parent_body["artifacts"]) == 8

# These two additional source images were read after the first baseline.
# Their OLD declared fingerprints, not newly invented expected hashes, bind them.
source_parent = "problems/2024-B4/notes/deep-literature-r2-search-sources-v1.json"
source_body = read_json(source_parent)
declared_images = {row["path"]: row for row in source_body["derived_cache_files"]}
extra_images = [f".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-{page}.png"
                for page in ["12", "13"]]
for path in extra_images:
    current = record(path)
    old = declared_images[path]
    assert current["sha256"] == old["sha256"]
    assert current["bytes"] == old["bytes"]
extra_source_rows = [record(path) for path in extra_images]
official_path = ".cache/official/2024-paper_b.pdf"
extra_source_rows.append(record(official_path))

all_rows = baseline["direct_inputs_and_occupied_prefix_and_source_bytes"] + extra_source_rows
unique_rows = {row["path"]: row for row in all_rows}
assert len(all_rows) == len(unique_rows) == 47

main = PREFIX + "candidate-v1.md"
obligations = PREFIX + "obligations-v1.md"
labels = re.findall(r"^\| (\d\d) \|", (ROOT / obligations).read_text(), re.M)
assert labels == [f"{i:02d}" for i in range(1, 37)]
assert "Candidate proof - unverified" in (ROOT / main).read_text()
assert "S3A" in (ROOT / main).read_text() and "S3D" in (ROOT / main).read_text()

source_pdf = ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf"
assert record(source_pdf)["sha256"] == "d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24"
pages_read = [7, 12, 13, 14, 15, 18, 20, 21, 22, 23, 24, 25]
render_rows = [record(f".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-{page:02d}.png")
               for page in pages_read]
source_rows = [
    {
        "id": "S01",
        "title": "McGuire1995 original-author PhD thesis",
        "record_url": "https://thesis.caltech.edu/4053/",
        "url": "https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf",
        "doi": "10.7907/1CZ2-6S05",
        "existing_cache": record(source_pdf),
        "pdf_pages": 97,
        "visual_pages_read_this_task": pages_read,
        "printed_pages_read": "2,7--10,13,15--20",
        "theorem": "Theorem2.1prime, printed19--20/PDF24--25: WHOLE absolute irreducibility for every t>3,t=3mod4",
        "operative_proof_read": True,
        "other_exact_context": "PropA full proof, exact projective Bezout statement, quotient definition/singularity setup, printed2 journal attribution",
        "journal_pdf_read": False,
        "new_download": False,
        "read_only_source_images": render_rows,
        "role": "attributed published sector theorem and local method; full own reconstruction supplied",
    },
    {
        "id": "S02",
        "title": "Hernando--McGuire, Proof of a Conjecture on the Sequence of Exceptional Numbers",
        "url": "https://arxiv.org/pdf/0903.2016v4",
        "version": "arXiv0903.2016v4 header18Sep2009; published J.Algebra343(2011)78--92",
        "read_scope": "definitions/conjecture distinction; local setup and singularity tables; exact sections4/5 theorem premises and conclusions; section6 counterexample assertion",
        "whole_Theorem16_proof_newly_independently_audited": False,
        "role": "scope distinction only; not a substitute whole theorem",
        "access": "successful web PDF reading; no new local bytes saved",
        "downloaded_pdf_sha256": None,
        "hash_limit": "No byte hash invented for a web parser response",
    },
    {
        "id": "S03",
        "title": "Janwa--McGuire--Wilson1995 journal article",
        "url": "https://www.sciencedirect.com/science/article/pii/S0021869385713725",
        "doi": "10.1006/jabr.1995.1372",
        "bibliography": "J.Algebra178(2)(1995)665--676",
        "read_scope": "actual publisher metadata/abstract only; proof accessed through the original coauthor parallel thesis S01",
        "journal_full_proof_read": False,
        "sha256": None,
        "role": "attribution; NO theorem inferred from its abstract",
    },
    {
        "id": "S04",
        "title": "Janwa--Wilson1993 chapter",
        "doi": "10.1007/3-540-56686-4_43",
        "bibliography": "LNCS673(1993)180--194",
        "read_scope": "identified through actual primary references; original proof remains unread",
        "role": "context only; no factorization or APN premise imported",
        "sha256": None,
    },
    {
        "id": "S05",
        "title": "Delgado--Janwa, On the Conjecture on APN Functions",
        "url": "https://arxiv.org/pdf/1207.5528v1",
        "version": "v1,23Jul2012",
        "read_scope": "matching phi definitions, Lemma1 and selected surrounding applications; not every proof",
        "role": "selected-family coprimality context only; arbitrary-target isolation is proved in new main",
        "sha256": None,
        "hash_limit": "web PDF text access only in this task; no downloaded bytes asserted",
    },
    {
        "id": "S06",
        "title": "Official2024 PaperB, B4(b)",
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
        "existing_cache": record(official_path),
        "fresh_read_scope": "PDFpage2 actual B4(b) statement and coefficientwise/nonconstant definitions, text-extracted by pypdf",
        "role": "official domains and exact conclusion; preliminary statement not investigated or solved",
        "new_download": False,
    },
]
sources_record = write_new("sources-v1.json", {
    "recorded_at_utc": STAMP,
    "source_scope_status": "complete constructor read-scope checkpoint, not an independent audit",
    "source_records": source_rows,
    "actual_queries_retained": [
        '"McGuire_gm_1995.pdf" "irreducible"',
        '"Janwa" "McGuire" "Wilson" "1995" "full" "polynomials"',
        '"Double-Error-Correcting Cyclic Codes" pdf',
        'Janwa phi t "relatively prime" "3" "4"',
        'APN "coprime" "phi" "7" "11"',
        '"polynomials" "relatively prime" "t" "3 (mod 4)"',
        '"Janwa" "phi_7" coprime',
        '"APN" "relatively prime" "3" "mod"',
        '"Janwa" "relatively prime" "7"',
        '"Janwa" "relatively prime" "odd"',
        '"APN" "coprime" "3 (mod 4)"',
        '"φ" "relatively prime" "n ≡ 3"',
        '"phi" "Janwa" "coprime" "odd"',
    ],
    "query_log_limit": "Exact retained strings only; no invented precompaction event timestamps or unavailable native response hashes",
    "unsuccessful_normal_web_routes": [
        "https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf (web cache miss/internal error; existing cached scan later found)",
        "https://thesis.library.caltech.edu/4053/1/McGuire_gm_1995.pdf (web internal error)",
        "https://www.sciencedirect.com/science/article/pii/S0021869385713725 (direct full opening unavailable; publisher abstract indexed)",
    ],
    "all_old_cache_bytes_unchanged": True,
    "no_new_source_download_contact_payment_bypass_or_escalated_wait": True,
    "PDF_skill": "read-only visual inspection of pre-existing original-author page renders",
    "new_theorem_from_abstract": False,
    "no_exhaustive_priority_claim": True,
})

telemetry = {
    "at_utc": "2026-10-17 19:20:55 UTC",
    "total_used_percent": 58,
    "window_minutes": 10080,
    "reset_unix": 1792745187,
    "ordinary_usage_allowed": True,
    "total_ceiling_percent": 90,
    "review_integration_reserve": True,
}
validation_record = write_new("input-validation-v1.json", {
    "checked_at_utc": STAMP,
    "administrative_only_not_mathematical_evidence": True,
    "baseline": record(baseline_path),
    "all_44_baseline_record_occurrences_reverified": True,
    "baseline_deduplicated_paths": 44,
    "baseline_canonical_record_array_sha256": baseline["canonical_record_array_sha256"],
    "additional_source_records": extra_source_rows,
    "additional_thesis_images_matched_OLD_declared_fingerprints": True,
    "all_record_occurrences": len(all_rows),
    "all_deduplicated_paths": len(unique_rows),
    "canonical_sorted_record_array_sha256": canonical_digest(list(unique_rows.values())),
    "compact_immutable_parent_manifest": parent,
    "parent_8_artifact_hashes_reverified": True,
    "earlier_own_paths_bound_transitively_not_inventory_recopied": 415,
    "occupied_old_2024_R3_files_reverified": 16,
    "all36_obligations": labels,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "contributors_excluded_from_two_independent_audit_count": ["C", "root"],
    "old_shared_Git_cache_edit_spawn_contact_charge_bypass_or_live_native_job": False,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "sources_metadata": sources_record,
    "direct_weekly_telemetry": telemetry,
})

artifact_suffixes = [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "source-audit-v1.md", "worklog-v1.md", "baseline-v1.json",
    "freeze-v1.py", "sources-v1.json", "input-validation-v1.json",
]
artifacts = [record(PREFIX + suffix) for suffix in artifact_suffixes]
assert artifacts[-1] == validation_record

# Recheck preserved old bytes after all NEW administrative outputs.
for row in all_rows:
    assert record(row["path"]) == row

freeze_record = write_new("freeze-v1.json", {
    "frozen_at_utc": STAMP,
    "status": "candidate proof - unverified; COMPLETE source-led mathematical checkpoint",
    "constructor": "/root/review_2017_coarsening_r1",
    "contributors": ["C", "root"],
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "independently_verified_effective_settings": None,
    "claims": [
        "S3A attributed published WHOLE sector theorem with complete reconstruction",
        "S3B arbitrary-odd-target diagonal-germ alternative with exact quotient correction",
        "S3C every sector base isolated from EVERY other odd index, even over the algebraic closure",
        "S3D finite graded-sum divisibility consequence",
    ],
    "whole_obligations": 36,
    "two_OTHER_fresh_initially_blind_WHOLE_nonconstructor_audits_required": True,
    "published_source_attribution_and_original_journal_read_limit_retained": True,
    "no_source_infinity_defect_claim": True,
    "old_C7_C11_not_rerun_or_claimed_new": True,
    "no_full_annual_classification_new_qualifying_family_or_novelty_claim": True,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "compact_immutable_parent_manifest": parent,
    "earlier_own_paths_preserved_by_compact_reference": 415,
    "all_47_current_source_input_and_occupied_prefix_records_reverified": True,
    "source_input_record_occurrences": len(all_rows),
    "source_input_deduplicated_paths": len(unique_rows),
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "direct_weekly_telemetry": telemetry,
    "artifacts": artifacts,
})
print(json.dumps({
    "COMPLETE": True, "freeze": freeze_record, "main": artifacts[0],
    "artifacts": len(artifacts), "obligations": len(labels),
    "input_occurrences": len(all_rows), "input_unique_paths": len(unique_rows),
    "all_earlier_bound_bytes_preserved": True,
    "mathematical_program": False,
}, ensure_ascii=False))
