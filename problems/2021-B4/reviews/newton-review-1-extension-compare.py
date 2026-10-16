"""Compare raw author records only after independent enumeration completed."""
import json
import pathlib

base = pathlib.Path(__file__).resolve().parents[1]
author = json.loads((base / "computations/coordinator-newton-degeneration-v1-result.json").read_text())
review = json.loads((base / "reviews/newton-review-1-extension-result.json").read_text())
assert author["before"] == review["histogram"]
expected_after = {j: len(review["retained_masks"][j]) if int(j) >= 15 else count
                  for j, count in review["histogram"].items()}
assert author["after_low_center_disjunction"] == expected_after
expected, retained = set(review["initial_masks"]["15"]), set(review["retained_masks"]["15"])
seen = set()
for record in author["masks_J15"]:
    # Author bit k-2 is H_k; review bit j-2 is D_j=H_(20-j).
    raw = record["mask_hasse_orders_2_to_18"]
    assert 0 <= raw < 2**17
    converted = sum(1 << (16 - bit) for bit in range(17) if raw & (1 << bit))
    assert converted not in seen and converted in expected
    seen.add(converted)
    low_orders = [k for k in (2, 3, 4) if converted & (1 << (18 - k))]
    assert record["low_center_orders"] == low_orders
    assert record["retained"] is (converted in retained)
assert seen == expected and len(seen) == 461
assert author["J15_retained"] == len(retained) == 69
assert author["J15_removed"] == len(expected - retained) == 392
print(json.dumps({
    "all_461_j15_raw_records_checked": True,
    "encoding_conversion": "17-bit reversal: author H_k bit k-2, review D_j bit j-2",
    "all_low_center_order_lists_match": True,
    "all_retention_flags_match": True,
    "all_counts_histograms_match": True,
    "j15_retained": len(retained),
    "j15_removed": len(expected - retained),
    "other_reviewer_inputs_read": False,
}, sort_keys=True))
