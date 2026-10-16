#!/usr/bin/env python3
"""Compare frozen author certificates only after R2 blind reconstruction.

Uses only R2 mathematical construction/finite-field arithmetic. Author source
was inspected for JSON hash serialization after the independent run completed;
no author program is imported or executed.
"""
import collections
import hashlib
import json
from pathlib import Path
import runpy
import time

base = Path(__file__).resolve().parent
own = runpy.run_path(str(base / "newton-review-2-independent.py"))
emit = own["emit"]
family = own["ordinary_family"]
gcd_degree_mod = own["gcd_degree_mod"]
author = base.parent / "computations"
start = time.monotonic()
patterns = json.loads((base / "newton-review-2-patterns.json").read_text())
own_records = [json.loads(line) for line in (base / "newton-review-2-independent-cases.jsonl").read_text().splitlines()]
by_key = {(r["center_mask"], r["u_mask"]): r for r in own_records}
assert len(by_key) == len(own_records) == 29928

author_patterns = next(json.loads(line) for line in (author / "padic-rational-newton-patterns.jsonl").read_text().splitlines() if json.loads(line).get("event") == "complete")
assert patterns["histogram"] == author_patterns["f1_mod_p_squared_survivors_by_J"]
assert patterns["j17_retained_masks"] == sorted(author_patterns["J17_remaining_center_masks"])
assert patterns["j17_discarded_masks"] == sorted(author_patterns["J17_discarded_center_masks"])
author_j16 = next(json.loads(line) for line in (author / "padic-rational-j16-obstruction.jsonl").read_text().splitlines() if json.loads(line).get("event") == "complete")
assert patterns["j16_retained_masks"] == sorted(author_j16["remaining_center_masks"])
assert patterns["j16_discarded_masks"] == sorted(author_j16["excluded_center_masks"])
emit(phase="pattern_comparison_complete", histogram_matches=True, all_j17_and_j16_mask_sets_match=True, masks_remaining=len(patterns["remaining_masks"]))

source = author / "padic-rational-j17-certificates.jsonl"
assert hashlib.sha256(source.read_bytes()).hexdigest() == "9676e4885d670a23ea1fb1b0a151ec1f9a8cece8532a1dd43277450b3a7a7fc3"
aggregate = hashlib.sha256()
seen = set()
hist = collections.Counter()
checks = 0
for line in source.read_text().splitlines():
    record = json.loads(line)
    key = record["center_mask"], record["u_mask"]
    assert key in by_key and key not in seen
    seen.add(key)
    r2 = by_key[key]
    f_one, f_u = family(*key)
    raw = json.dumps([*key, f_one, f_u], separators=(",", ":")).encode()
    aggregate.update(raw + b"\n")
    assert hashlib.sha256(raw).hexdigest() == record["polynomials_sha256"]
    own_raw = json.dumps({"P": f_one, "Q": f_u}, sort_keys=True, separators=(",", ":")).encode()
    assert hashlib.sha256(own_raw).hexdigest() == r2["ordinary_polynomial_sha256"]
    assert record["degrees"] == r2["degrees"] == [len(f_one) - 1, len(f_u) - 1]
    if record["status"] == "constant_nonzero":
        assert len(f_one) == 1 and f_one[0] != 0
        assert record["constant"] == r2["constant_P"] == f_one[0]
        hist["constant"] += 1
    else:
        assert record["status"] == "coprime_mod_prime"
        ell = record["prime"]
        assert ell == r2["ell"]
        assert ell in (101, 103, 107, 109)
        assert all(ell % n for n in range(2, int(ell ** 0.5) + 1))
        leading = [f_one[-1] % ell, f_u[-1] % ell]
        assert all(leading)  # both integer degrees are retained
        assert record["leading_residues"] == r2["leading_residues"] == leading
        assert record["gcd_degree"] == r2["gcd_degree"] == gcd_degree_mod(f_one, f_u, ell) == 0
        hist[str(ell)] += 1
    checks += 1
    if checks % 1024 == 0:
        emit(phase="certificate_comparison_checkpoint", checked=checks)
assert seen == set(by_key)
assert aggregate.hexdigest() == "47a5b912863c67f22fed42daaf92b72949a06164966037ac97e4ad8afd22395b"
summary = dict(checked=checks, exact_family_coverage=True, duplicate_records=0, missing_records=0, spurious_records=0, every_polynomial_hash_matches=True, every_recorded_degree_preserved=True, every_recorded_gcd_recomputed=True, certificate_histogram=dict(hist), author_polynomial_stream_sha256=aggregate.hexdigest(), author_certificate_sha256=hashlib.sha256(source.read_bytes()).hexdigest(), elapsed_seconds=time.monotonic() - start)
(base / "newton-review-2-comparison-summary.json").write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n")
emit(phase="complete", **summary)
