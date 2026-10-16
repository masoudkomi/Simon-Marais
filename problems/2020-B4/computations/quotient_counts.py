#!/usr/bin/env python3
"""Enumerate exact quotient-by-3 occupancy constraints, not difference sets."""

from datetime import datetime, timezone
from pathlib import Path
import json
import platform


def vectors(q):
    assert q % 3 == 1
    v, k = q * q + q + 1, q + 1
    results = []
    for a in range(k + 1):
        for b in range(k - a + 1):
            c = k - a - b
            if a * a + b * b + c * c == q + v // 3:
                assert a * b + b * c + c * a == v // 3
                assert (a - c) ** 2 - (a - c) * (b - c) + (b - c) ** 2 == q
                results.append([a, b, c])
    return {"q": q, "n": q + 1, "v": v, "count_vectors": results}


def main():
    report = {
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "dependencies": "Python standard library only",
        "warning": "These are occupancy vectors, not witnesses for tautness.",
        "results": [vectors(q) for q in [10, 28, 52, 55, 91, 100]],
    }
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    prefix = Path(__file__).parent / "quotient-counts"
    prefix.with_suffix(".json").write_text(encoded)
    prefix.with_suffix(".stdout").write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
