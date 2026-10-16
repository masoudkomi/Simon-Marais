#!/usr/bin/env python3
"""Reproduce capped-run continuation and official-domain boundary evidence."""
import json
import platform
from pathlib import Path

from exact_search import iterate


root = Path(__file__).resolve().parent
initial = json.loads((root / "random-256.json").read_text())
pending = [r for r in initial["records"] if "status" in r]
continuations = []
for record in pending:
    a, b = record["a0"], record["b0"]
    status, n, x, y = iterate(a, b, 20000, 8192)
    continuations.append({"a0": a, "b0": b, "status": status,
                          "first_hit_or_cap_n": n, "a_end": x, "b_end": y})
boundaries = []
for a in range(1, 601):
    if 600 % a == 0:
        b = 600 // a
        status, n, x, y = iterate(a, b, 20000, 8192)
        boundaries.append({"a0": a, "b0": b, "status": status,
                           "first_hit_or_cap_n": n})
for a in (25, 30, 600, 10**100):
    status, n, _, _ = iterate(a, a, 20000, 8192)
    boundaries.append({"a0": a, "b0": a, "status": status,
                       "first_hit_or_cap_n": n})
print(json.dumps({"meaning": "finite exact evidence only",
                  "python": platform.python_version(), "step_cap": 20000,
                  "bit_cap": 8192, "continued_input": "random-256.json",
                  "continuations": continuations,
                  "product_600_and_n0_cases": boundaries}, indent=2, sort_keys=True))
