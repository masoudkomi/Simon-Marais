#!/usr/bin/env python3
"""Bounded structural probes for 2019 B4(b); finite evidence only."""
from __future__ import annotations

import argparse
import itertools
import json
import os
import time


def context(history: str, phase: int = 0) -> tuple[str, str]:
    tapes = ["", ""]
    for i, c in enumerate(history):
        tapes[c == "R"] += str((i + phase) % 2)
    return tuple(tapes)


def product_context(word: str) -> tuple[str, str]:
    generators = {"A": ("01", ""), "B": ("0", "1"),
                  "C": ("1", "0"), "D": ("", "01")}
    return tuple("".join(generators[c][i] for c in word) for i in (0, 1))


def canonical_probe(max_moves: int, state_cap: int) -> dict:
    assert 2 ** max_moves <= state_cap
    nonminimal: set[str] = set()
    minimal_forbidden: list[dict] = []
    rows = []
    for t in range(max_moves + 1):
        first: dict[tuple[str, str], str] = {}
        new_forbidden = []
        for choices in itertools.product("LR", repeat=t):
            h = "".join(choices)
            pair = context(h)
            if pair in first:
                nonminimal.add(h)
                # A shorter bad factor is detected by deleting at one end.
                if h[1:] not in nonminimal and h[:-1] not in nonminimal:
                    row = {"larger": h, "smaller": first[pair], "tapes": pair}
                    new_forbidden.append(row)
                    minimal_forbidden.append(row)
            else:
                first[pair] = h
        row = {"moves": t, "histories": 2 ** t, "contexts": len(first),
               "new_minimal_forbidden": len(new_forbidden)}
        rows.append(row)
        print(json.dumps({"checkpoint": row, "pid": os.getpid()}), flush=True)
    relation_checks = []
    for a, b in (("AD", "DA"), ("BCB", "ABD"), ("CBC", "DCA"),
                 ("ACBBCD", "DBCCBA")):
        relation_checks.append({"left": a, "right": b,
                                "left_tapes": product_context(a),
                                "right_tapes": product_context(b),
                                "equal": product_context(a) == product_context(b)})
    return {"status": "finite computational evidence only", "rows": rows,
            "relations": relation_checks, "minimal_forbidden": minimal_forbidden}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-moves", type=int, default=14)
    parser.add_argument("--state-cap", type=int, default=20000)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    start = time.monotonic()
    data = canonical_probe(args.max_moves, args.state_cap)
    data["parameters"] = vars(args)
    data["elapsed_seconds"] = time.monotonic() - start
    with open(args.output, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(json.dumps({"finished": True, "seconds": data["elapsed_seconds"],
                      "output": args.output}), flush=True)


if __name__ == "__main__":
    main()
