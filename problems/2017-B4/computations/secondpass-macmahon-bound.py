#!/usr/bin/env python3
"""Exact finite evidence for candidate M1, not a proof for unrestricted sizes.

Checks M(a,b,c)^2*16^(ab+bc+ca) <= 27^(ab+bc+ca) with integer arithmetic
for 1 <= a <= b <= c <= 24, using the hyperfactorial MacMahon product.
Also prints numerical unequal-proportion coefficients for orientation only.
One dedicated child; PID, arguments, 20s timeout and incremental output saved.
Standard library only. No native CAS, random choices or network calls.
"""
import argparse
from datetime import datetime, timezone
from itertools import combinations_with_replacement
import json
from math import factorial, log, log2
from pathlib import Path
import platform
import subprocess
import sys
from time import monotonic

BASE = Path(__file__).resolve().parent


def worker(cap):
    print(f"Python {platform.python_version()}; standard library; exact integer checks", flush=True)
    print("Finite evidence for candidate proof - unverified; no unrestricted computational claim", flush=True)
    hyper = [1] * (3 * cap + 1)
    for n in range(1, len(hyper)):
        hyper[n] = hyper[n - 1] * factorial(n - 1)
    checked = 0
    best = (-1, None)
    for a, b, c in combinations_with_replacement(range(1, cap + 1), 3):
        numerator = hyper[a] * hyper[b] * hyper[c] * hyper[a + b + c]
        denominator = hyper[a + b] * hyper[b + c] * hyper[c + a]
        count, remainder = divmod(numerator, denominator)
        assert remainder == 0
        s = a*b + b*c + c*a
        left = (count * count) << (4 * s)
        right = pow(27, s)
        assert left < right, (a, b, c, count)
        coefficient = log2(count) / (2 * s)
        if coefficient > best[0]:
            best = (coefficient, (a, b, c))
        checked += 1
        if a == b == c:
            print(f"balanced m={a} M={count} exact_integer_inequality=True "
                  f"log2_M/(2S)={coefficient:.15f}", flush=True)
    print(f"COMPLETE integer triples={checked}; cap={cap}; all_strict=True; "
          f"largest_numerical_coefficient={best[0]:.15f}; at={best[1]}", flush=True)
    c0 = 3*log2(3)/4 - 1
    print(f"candidate sharp coefficient c0={c0:.15f}", flush=True)
    for p in ((1/3, 1/3, 1/3), (1/2, 1/4, 1/4), (3/5, 1/5, 1/5),
              (4/5, 1/10, 1/10), (9/20, 9/20, 1/10)):
        integral = sum(x*x*log(x) - (1-x)**2*log(1-x) for x in p) / 2
        coefficient = integral / ((1 - sum(x*x for x in p)) * log(2))
        print(f"proportions={p} amplified_coefficient={coefficient:.15f} [numerical]", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--cap", type=int, default=24)
    parser.add_argument("--timeout", type=float, default=20)
    args = parser.parse_args()
    if args.worker:
        worker(args.cap)
        return
    output_path = BASE / "secondpass-macmahon-bound-output.txt"
    job_path = BASE / "secondpass-macmahon-bound-job.json"
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", "--cap", str(args.cap)]
    start = monotonic()
    with output_path.open("w") as output:
        child = subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT)
        job = {"started_utc": datetime.now(timezone.utc).isoformat(), "pid": child.pid,
               "command": command, "timeout_seconds": args.timeout,
               "stdout": str(output_path), "status": "running"}
        job_path.write_text(json.dumps(job, indent=2) + "\n")
        print(f"child_pid={child.pid}; job={job_path}; stdout={output_path}", flush=True)
        try:
            code = child.wait(timeout=args.timeout)
            job["status"] = "complete" if code == 0 else "failed"
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                code = child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                code = child.wait(timeout=2)
            job["status"] = "timeout_incomplete"
        job["returncode"] = code
        job["elapsed_seconds"] = monotonic() - start
        job["finished_utc"] = datetime.now(timezone.utc).isoformat()
        job_path.write_text(json.dumps(job, indent=2) + "\n")
    print(json.dumps(job, sort_keys=True), flush=True)
    if job["status"] != "complete":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
