#!/usr/bin/env python3
"""Raw finite-result comparison after the independent extension run."""
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parent
own = json.loads((base / "newton-review-2-extension-independent-result.json").read_text())
source = base.parent / "computations/coordinator-newton-degeneration-v1-result.json"
assert hashlib.sha256(source.read_bytes()).hexdigest() == "04e24446d48f7073e5a9775cc121babef33e66db3391ded2aaa22fb63d6e2864"
author = json.loads(source.read_text())
assert own["visited"] == author["binary_flags"] == 131072
assert own["histogram"] == author["before"]
after = dict(own["histogram"])
for j, group in own["groups"].items():
    after[j] = len(group["retained_masks"])
assert after == author["after_low_center_disjunction"]
assert author["J15_removed"] == len(own["groups"]["15"]["discarded_masks"]) == 392
assert author["J15_retained"] == len(own["groups"]["15"]["retained_masks"]) == 69

# Author labels bit k-2 by Hasse order k; R2 labels bit j-2 by
# derivative degree j=20-k. These are reversed 17-bit conventions.
expected_keep = set(own["groups"]["15"]["retained_masks"])
expected_drop = set(own["groups"]["15"]["discarded_masks"])
seen = set()
for record in author["masks_J15"]:
    mask_by_k = record["mask_hasse_orders_2_to_18"]
    assert 0 <= mask_by_k < 2 ** 17
    mask_by_j = sum(1 << (16 - i) for i in range(17) if mask_by_k & (1 << i))
    assert mask_by_j not in seen
    seen.add(mask_by_j)
    assert mask_by_j in expected_keep | expected_drop
    low = [k for k in range(2, 5) if mask_by_k & (1 << (k - 2))]
    assert record["low_center_orders"] == low
    assert record["retained"] == bool(low) == (mask_by_j in expected_keep)
assert seen == expected_keep | expected_drop
assert len(seen) == 461
result = dict(histograms_match=True, all_461_j15_masks_match=True, all_low_center_orders_match=True, all_retention_booleans_match=True, duplicate_masks=0, missing_masks=0, mask_conversion="17-bit reversal: author bit k-2 versus R2 bit (20-k)-2", removed=392, retained=69, combined_remaining=772, author_result_sha256=hashlib.sha256(source.read_bytes()).hexdigest())
(base / "newton-review-2-extension-comparison-result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
print(json.dumps(dict(phase="complete", **result), sort_keys=True), flush=True)
