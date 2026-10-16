#!/usr/bin/env python3
"""Freeze/check the author-repair packet without rerunning mathematics.

Checks original/revised fingerprints, exact unified diffs, unchanged M1/M3
math sections, Markdown display delimiters and source-file whitespace. A
unified diff's mandatory blank-context prefix is not trailing source space.
Standard library only; no child process, network request, or CAS operation.
"""
from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "problems/2017-B4"
NOTES = BASE / "notes"
CHECKPOINT = NOTES / "author-repair-checkpoint-v1.1.json"
assert not CHECKPOINT.exists(), "checkpoint already frozen; do not overwrite it"
manifest = json.loads((NOTES / "author-repair-manifest-v1.1.json").read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()

for path, expected in manifest["preserved_input_sha256"].items():
    assert sha(ROOT / path) == expected, (path, "frozen input changed")

diffs_checked = []
for rec in manifest["candidates"]:
    old, new, diff = (ROOT / rec[k] for k in ("old_path", "revised_path", "exact_diff_path"))
    assert sha(old) == rec["old_sha256"]
    assert sha(new) == rec["revised_sha256"]
    assert sha(diff) == rec["exact_diff_sha256"]
    expected_diff = "".join(difflib.unified_diff(
        old.read_text().splitlines(keepends=True), new.read_text().splitlines(keepends=True),
        fromfile=rec["old_path"], tofile=rec["revised_path"], n=4))
    assert diff.read_text() == expected_diff
    text = new.read_text()
    assert text.splitlines().count(r"\[") == text.splitlines().count(r"\]")
    assert r"\\[" not in text
    assert "**candidate proof - unverified**" in text
    diffs_checked.append(rec["claim_prefix"])

old_mac = (NOTES / "secondpass-macmahon-candidate-v1.md").read_text()
new_mac = (NOTES / "author-repair-macmahon-candidate-v1.1.md").read_text()
for left, right in (("## Candidate M1:", "## Candidate M2:"),
                    ("## Candidate M3:", "## Independent-review obligations")):
    assert old_mac.split(left, 1)[1].split(right, 1)[0] == new_mac.split(left, 1)[1].split(right, 1)[0]

files = sorted(list(NOTES.glob("author-repair-*"))
               + list((BASE / "computations").glob("author-repair-*")))
for path in files:
    if path.is_file() and path.suffix != ".diff":
        assert all(line.rstrip() == line for line in path.read_text().splitlines()), path

record = {
    "recorded_utc": datetime.now(timezone.utc).isoformat(),
    "status": "candidate proof - unverified; frozen for both targeted re-audits; no promotion",
    "author": "/root/owner_2017; original second-pass constructor",
    "preserved_input_fingerprints_verified": len(manifest["preserved_input_sha256"]),
    "exact_diffs_verified": diffs_checked,
    "M1_M3_math_sections_byte_identical": True,
    "display_delimiters_and_no_double_escape_verified": True,
    "source_trailing_whitespace": [],
    "verification_note": "An initial blanket whitespace check flagged the mandatory space on unified-diff blank context lines; no candidate defect or changed frozen bytes. Final check excludes .diff formatting prefixes and verifies each diff exactly.",
    "unchanged_Q_3_3": 4419734746,
    "new_enumeration_or_CAS_runs": 0,
    "larger_computational_caps": False,
    "targeted_independent_reaudits_completed": 0,
    "files": [{"path": str(p.relative_to(ROOT)), "sha256": sha(p), "bytes": p.stat().st_size}
              for p in files if p.is_file()],
}
with CHECKPOINT.open("x") as out:
    out.write(json.dumps(record, indent=2) + "\n")
print("preserved input hashes:", record["preserved_input_fingerprints_verified"], "unchanged")
print("exact diffs and display delimiters:", ", ".join(diffs_checked))
print("M1/M3 mathematics: byte-identical; no new mathematical computations")
print("checkpoint:", str(CHECKPOINT.relative_to(ROOT)), sha(CHECKPOINT))
for rec in manifest["candidates"]:
    print(rec["claim_prefix"], rec["revised_sha256"])
