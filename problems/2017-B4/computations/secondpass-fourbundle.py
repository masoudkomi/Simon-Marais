#!/usr/bin/env python3
"""Bounded exact counts for square patches of the periodic four-bundle grid.

Lines: x=i, y=j, y-x=k, y+x=l, all integer constants. The patch is
[1/10,L+1/10] x [1/5,L+1/5]. Boundaries avoid every grid crossing and corner
tangency. Fourfold grid vertices occur at the L^2 integer points; simple
twofold diagonal intersections are also preserved. Extract the FULL labelled
boundary pairing by exact Fraction arithmetic, then use the independently
implemented cut counter. No scalar crossing-count substitution is used.

One child, 45 seconds, 50000 memo states. Incremental completed L-values
survive a timeout. Results are computational evidence pending independent
audit, not an unrestricted B4 bound. Standard library only.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import importlib.util
import json
from math import ceil, floor, log2
from pathlib import Path
import platform
import subprocess
import sys
from time import monotonic

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent


def boundary_word(side):
    xmin, ymin = Fraction(1, 10), Fraction(1, 5)
    xmax, ymax = xmin + side, ymin + side
    families = ((1, 0, xmin, xmax, "vertical"),
                (0, 1, ymin, ymax, "horizontal"),
                (-1, 1, ymin-xmax, ymax-xmin, "rising"),
                (1, 1, xmin+ymin, xmax+ymax, "falling"))
    events = []
    lines = []
    for aa, bb, low, high, family in families:
        for cc in range(ceil(low), floor(high) + 1):
            points = []
            if aa:
                for y, edge in ((ymin, 0), (ymax, 2)):
                    x = (cc - bb*y) / aa
                    if xmin < x < xmax:
                        points.append((edge, x if edge == 0 else -x))
            if bb:
                for x, edge in ((xmax, 1), (xmin, 3)):
                    y = (cc - aa*x) / bb
                    if ymin < y < ymax:
                        points.append((edge, y if edge == 1 else -y))
            if not points:
                continue
            assert len(points) == 2
            label = len(lines)
            lines.append((aa, bb, cc, family))
            events.extend((edge, coordinate, label) for edge, coordinate in points)
    events.sort()
    assert len({(a, b) for a, b, _ in events}) == len(events)
    return tuple(label for _, _, label in events), lines


def worker(max_side):
    spec = importlib.util.spec_from_file_location("patch_counter", BASE / "secondpass-patchcount.py")
    counter = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(counter)
    counter.STATE_CAP = 50000
    print(f"Python {platform.python_version()}; standard library; Fraction geometry", flush=True)
    print("Exact finite patch evidence; no current global-bound improvement asserted", flush=True)
    for side in range(1, max_side + 1):
        word, lines = boundary_word(side)
        print(f"START L={side} area={side*side} strands={len(lines)} "
              f"word={word} lines={lines}", flush=True)
        start = monotonic()
        count = counter.count_patch(counter.canonical(word))
        # Independent tiny disks about the L^2 fourfold points give 8 choices each.
        assert count >= (1 << (3 * side * side))
        print(f"DONE L={side} F={count} log2_F_per_area={log2(count)/(side*side):.15f} "
              f"memo_states={counter.count_patch.cache_info().currsize} "
              f"elapsed_seconds={monotonic()-start:.6f}", flush=True)
    print("COMPLETE", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--max-side", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=45)
    args = parser.parse_args()
    if args.worker:
        worker(args.max_side)
        return
    output_path = BASE / "secondpass-fourbundle-output.txt"
    job_path = BASE / "secondpass-fourbundle-job.json"
    command = [sys.executable, str(Path(__file__).resolve()), "--worker",
               "--max-side", str(args.max_side)]
    start = monotonic()
    with output_path.open("w") as output:
        child = subprocess.Popen(command, stdout=output, stderr=subprocess.STDOUT)
        job = {"started_utc": datetime.now(timezone.utc).isoformat(), "pid": child.pid,
               "command": command, "timeout_seconds": args.timeout, "state_cap": 50000,
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
