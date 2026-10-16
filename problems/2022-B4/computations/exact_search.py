#!/usr/bin/env python3
"""Exact finite evidence for SMMC 2022 B4(b); no unrestricted proof.

Only Python's standard library is used. Equality at n=0 is included, and
both next coordinates are computed from the old coordinates.
"""
import argparse
import collections
import hashlib
import json
import platform
import random
import time


def iterate(a, b, step_cap, bit_cap):
    for n in range(step_cap + 1):
        if a == b:
            return "hit", n, a, b
        if max(a.bit_length(), b.bit_length()) > bit_cap:
            return "bit_cap", n, a, b
        if n == step_cap:
            return "step_cap", n, a, b
        a, b = a + 2 * (b // 20), b + 3 * (a // 30)
    raise AssertionError("unreachable")


def inputs(args):
    if args.mode == "box":
        for a in range(1, args.bound + 1):
            for b in range(1, args.bound + 1):
                if a * b >= 600:
                    yield a, b
    elif args.mode == "strip":
        for b in range(1, args.bound + 1):
            for d in range(-13, 24):
                a = b + d
                if a > 0 and a * b >= 600:
                    yield a, b
    elif args.mode == "random":
        rng = random.Random(args.seed)
        for _ in range(args.samples):
            a = rng.getrandbits(args.input_bits) + 1
            b = rng.getrandbits(args.input_bits) + 1
            if a * b < 600:
                raise ValueError("random input too small")
            yield a, b
    elif args.mode == "random-strip":
        rng = random.Random(args.seed)
        for _ in range(args.samples):
            b = rng.getrandbits(args.input_bits) + 1000
            yield b + rng.randrange(-13, 24), b
    else:
        raise ValueError(args.mode)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("mode", choices=["box", "strip", "random", "random-strip"])
    p.add_argument("--bound", type=int, default=500)
    p.add_argument("--samples", type=int, default=10000)
    p.add_argument("--input-bits", type=int, default=256)
    p.add_argument("--seed", type=int, default=20221015)
    p.add_argument("--step-cap", type=int, default=5000)
    p.add_argument("--bit-cap", type=int, default=4096)
    p.add_argument("--seconds", type=float, default=90)
    args = p.parse_args()
    start = time.monotonic()
    counts = collections.Counter()
    histogram = collections.Counter()
    records = []
    maximum = -1
    digest = hashlib.sha256()
    completed = True
    for a, b in inputs(args):
        if time.monotonic() - start > args.seconds:
            completed = False
            break
        status, n, x, y = iterate(a, b, args.step_cap, args.bit_cap)
        counts[status] += 1
        digest.update(f"{a},{b},{status},{n},{x},{y}\n".encode())
        if status == "hit":
            histogram[n] += 1
            if n > maximum:
                maximum = n
                records.append({"a0": a, "b0": b, "first_hit_n": n})
        else:
            records.append({"a0": a, "b0": b, "status": status, "n": n,
                            "a_end": x, "b_end": y})
    out = {"meaning": "finite exact computation, evidence only",
           "python": platform.python_version(), "parameters": vars(args),
           "completed_input_enumeration": completed, "counts": dict(counts),
           "maximum_first_hit": maximum, "records": records,
           "histogram": dict(sorted(histogram.items())),
           "ordered_result_sha256": digest.hexdigest(),
           "elapsed_seconds": time.monotonic() - start}
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
