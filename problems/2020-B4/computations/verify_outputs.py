#!/usr/bin/env python3
"""Consistency checks on saved finite evidence; not an independent proof review."""

from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import platform

from exact_search import generated_multipliers
from residual_orders import orbit_histogram


def main():
    directory = Path(__file__).parent
    checks = []
    small = json.loads((directory / "small-search.json").read_text())
    for row in small["results"]:
        witness = row["witness"]
        if witness is None:
            assert row["n"] == 7 and row["status"] == "exhausted_no_witness"
            continue
        v, n = row["v"], row["n"]
        lengths = [min(abs(a - b), v - abs(a - b)) for a, b in combinations(witness, 2)]
        assert len(witness) == len(set(witness)) == n
        assert len(lengths) == len(set(lengths)) == (v - 1) // 2
        assert set(lengths) == set(range(1, (v + 1) // 2))
        checks.append(f"n={n}: all undirected separations occur exactly once")
    examples = json.loads((directory / "orbit-examples.json").read_text())
    for row in examples["results"]:
        group, complete = generated_multipliers(row["q"])
        assert complete
        histogram = orbit_histogram(row["q"], group)
        explicit = dict(sorted(Counter(map(len, row["orbits"])).items()))
        assert histogram == explicit
        checks.append(f"q={row['q']}: arithmetic orbit histogram matches explicit orbits")
    filters = json.loads((directory / "filters-q5000.json").read_text())["results"]
    assert sum(filters["tallies"].values()) == filters["q_max"] - filters["q_min"] + 1
    assert filters["residual_non_prime_power_orders"] == [1944, 2304, 2435]
    checks.append("all 4999 orders in first pass accounted for exactly once")
    quotient = json.loads((directory / "quotient-counts.json").read_text())
    for row in quotient["results"]:
        q, v = row["q"], row["v"]
        for a, b, c in row["count_vectors"]:
            assert a + b + c == q + 1
            assert a * a + b * b + c * c == q + v // 3
            assert a * b + b * c + c * a == v // 3
        checks.append(f"q={q}: stored quotient vectors satisfy every quotient-by-3 equation")
    paths = sorted(directory.glob("*.py")) + sorted(directory.glob("*.json"))
    paths = [p for p in paths if p.name != "verification.json"]
    paths.append(directory.parent / "proofs/partial-v1.md")
    report = {
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "status": "all consistency checks passed; independent adversarial review still pending",
        "checks": checks,
        "sha256": {str(p.relative_to(directory.parent)): sha256(p.read_bytes()).hexdigest() for p in paths},
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    (directory / "verification.json").write_text(encoded)
    (directory / "verification.stdout").write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
