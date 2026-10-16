#!/usr/bin/env python3
"""Independent extension filter: incremental Pascal values in F_19.

Does not read/import the coordinator program or finite result. Reuses no
old author program. Its result is saved before the comparison is run.
"""
import collections
import json
import math
from pathlib import Path
import time

P = 19
D = 20
BASE = Path(__file__).resolve().parent
CHOOSE = [[math.comb(n, k) for k in range(n + 1)] for n in range(D)]
WEIGHTS = {j: math.comb(D, j) // P % P for j in range(2, D - 1)}
visited = 0
passes = {}
start = time.monotonic()


def emit(**row):
    print(json.dumps(row, sort_keys=True), flush=True)


def descend(j, values, residue, mask, largest_unit):
    global visited
    if j == D - 1:
        visited += 1
        if residue == 0:
            passes[mask] = largest_unit
        if visited % 32768 == 0:
            emit(phase="checkpoint", visited=visited, passing=len(passes))
        return
    # values[t] is D_t(1) before a_j and all later coefficients are set.
    # The noncenter residue equation is a_j=0.
    descend(j + 1, values, residue, mask, largest_unit)
    a_j = -values[j] % P
    next_values = values.copy()
    for t in range(j + 1, D - 1):
        next_values[t] = (next_values[t] + CHOOSE[t][j] * a_j) % P
    descend(j + 1, next_values, (residue + WEIGHTS[j] * a_j) % P,
            mask | (1 << (j - 2)), j if a_j else largest_unit)


emit(phase="start", degree=D, prime=P, method="incremental Pascal evaluations over F_19, independent of ordinary-coefficient coordinator implementation", coordinator_code_or_results_read=False)
descend(2, [(1 - j) % P for j in range(D)], P - 1, 0, 0)
assert visited == 2 ** 17
histogram = collections.Counter(passes.values())
assert len(passes) == 6680


def low_flags(h):
    return sum(1 << (D - k - 2) for k in range(2, h))


groups = {}
for j in (15, 16, 17, 18):
    h = D - j
    retained = sorted(mask for mask, value in passes.items() if value == j and mask & low_flags(h))
    discarded = sorted(mask for mask, value in passes.items() if value == j and not mask & low_flags(h))
    groups[str(j)] = dict(h=h, low_derivative_orders=list(range(2, h)), flag_mask=low_flags(h), retained_masks=retained, discarded_masks=discarded)

old_remaining = sorted(mask for mask, j in passes.items() if j < 16 or (j == 16 and mask & low_flags(4)))
new_remaining = sorted(mask for mask, j in passes.items() if j < 15 or (j in (15, 16) and mask & low_flags(D - j)))
assert len(old_remaining) == 1164
assert len(new_remaining) == 772
assert set(new_remaining).issubset(old_remaining)
removed = sorted(set(old_remaining) - set(new_remaining))
assert removed == groups["15"]["discarded_masks"]
assert len(removed) == 392

result = dict(visited=visited, total_necessary_patterns=len(passes), histogram=dict(sorted(histogram.items())), groups=groups, old_remaining_masks=old_remaining, remaining_after_j17_exclusion_and_new_filter=new_remaining, newly_removed_masks=removed, elapsed_seconds=time.monotonic() - start)
(BASE / "newton-review-2-extension-independent-result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
emit(phase="complete", visited=visited, passes=len(passes), histogram=result["histogram"], counts={j: {"h": row["h"], "retained": len(row["retained_masks"]), "discarded": len(row["discarded_masks"])} for j, row in groups.items()}, old_remaining=len(old_remaining), new_remaining=len(new_remaining), newly_removed=len(removed), elapsed_seconds=result["elapsed_seconds"])
