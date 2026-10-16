#!/usr/bin/env python3
"""Reviewer-written exact certificate; no constructor module or outputs are read.

Invoke without arguments.  A dedicated subprocess is externally capped at 30 s,
and its PID, parameters, checkpoint stream, status and reaping are preserved.
The --child mode performs only rational arithmetic in the standard library.
"""

from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
PREFIX = HERE / "concavity-review-2-independent"
N = 96


def stamp():
    return datetime.now(timezone.utc).isoformat()


def serial(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def log_bounds(r):
    # Integrate 2/(1-z*z) on [0,z], after r=(1+z)/(1-z).
    # After N terms, each omitted denominator is at least 2*N+1.
    z = (r - 1) / (r + 1)
    assert 0 < z < 1
    power = z
    partial = Q(0)
    for j in range(N):
        partial += power / (2*j + 1)
        power *= z*z
    lower = 2*partial
    upper = lower + 2*power / ((2*N + 1)*(1-z*z))
    assert lower > 0 and upper > lower
    return lower, upper


def main_child():
    print("independent exact check starts", stamp(), "N=", N, flush=True)
    logs = {}
    for name, argument in [
        ("ln2", Q(2)),
        ("ln32over7", Q(32, 7)),
        ("ln79over58", Q(79, 58)),
        ("ln107648over43687", Q(107648, 43687)),
        ("ln3over2", Q(3, 2)),
    ]:
        logs[name] = log_bounds(argument)
        print("completed", name, "argument", argument, flush=True)

    L2, U2 = logs["ln2"]
    def quotient(interval):
        # All log numerators and the relevant sums below are positive.
        return interval[0]/U2, interval[1]/L2

    A = quotient(logs["ln32over7"])
    B = quotient(logs["ln79over58"])
    phi = (Q(21, 100)*A[0] + Q(29, 50)*B[0] + Q(29, 50),
           Q(21, 100)*A[1] + Q(29, 50)*B[1] + Q(29, 50))
    rational_derivative_term = Q(7, 32) + Q(21, 79)
    dlog = logs["ln107648over43687"]
    dphi = ((dlog[0] + rational_derivative_term)/U2 - 2,
            (dlog[1] + rational_derivative_term)/L2 - 2)
    C = quotient(logs["ln3over2"])
    f0 = (1 + C[0]/2, 1 + C[1]/2)

    checks = {
        "phi_at_21over100_lt_64951over50000": phi[1] < Q(64951, 50000),
        "dphi_at_21over100_gt_zero": dphi[0] > 0,
        "dphi_at_21over100_lt_1over5000": dphi[1] < Q(1, 5000),
        "f0_lt_1293over1000": f0[1] < Q(1293, 1000),
        "ln2_gt_1over3": L2 > Q(1, 3),
    }
    # For u in [0,1/4], tangent slope is positive; max offset is 1/25.
    tangent_upper = phi[1] + dphi[1]/25
    objective_upper = max(tangent_upper, f0[1])
    target = Q(324757, 250000)
    # Supply an additional simple uniform ceiling below the candidate's target.
    simple_ceiling = Q(1299027, 1000000)
    checks["uniform_objective_upper_lt_candidate_target"] = objective_upper < target
    checks["uniform_objective_upper_lt_1299027over1000000"] = objective_upper < simple_ceiling
    checks["simple_ceiling_half_lt_324757over500000"] = simple_ceiling/2 < Q(324757, 500000)
    for name, passed in checks.items():
        print("assert", name, passed, flush=True)
        assert passed, name

    payload = {
        "created_utc": stamp(),
        "status": "all exact rational assertions passed; verification evidence",
        "method": "independent atanh integral series with N=96, positive geometric tail",
        "N": N,
        "constructor_code_or_data_read": False,
        "logs": {name: {"lower": serial(lo), "upper": serial(hi)}
                 for name, (lo, hi) in logs.items()},
        "derived_intervals": {
            "phi": {"lower": serial(phi[0]), "upper": serial(phi[1])},
            "dphi": {"lower": serial(dphi[0]), "upper": serial(dphi[1])},
            "F0": {"lower": serial(f0[0]), "upper": serial(f0[1])},
        },
        "tangent_upper": serial(tangent_upper),
        "uniform_objective_upper": serial(objective_upper),
        "candidate_target": serial(target),
        "simple_uniform_ceiling": serial(simple_ceiling),
        "exact_slack_to_candidate_target": serial(target-objective_upper),
        "checks": checks,
        "diagnostic_floats_not_proof": {
            "phi_lower": float(phi[0]), "phi_upper": float(phi[1]),
            "dphi_lower": float(dphi[0]), "dphi_upper": float(dphi[1]),
            "F0_upper": float(f0[1]),
            "uniform_objective_upper": float(objective_upper),
            "limsup_ceiling_half": float(simple_ceiling/2),
        },
    }
    output = PREFIX.with_name(PREFIX.name + "-certificate.json")
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print("certificate written", output.name, flush=True)


def main_supervisor():
    cmd = [sys.executable, "-B", "-u", str(Path(__file__).resolve()), "--child"]
    stdout = PREFIX.with_name(PREFIX.name + "-stdout.txt")
    stderr = PREFIX.with_name(PREFIX.name + "-stderr.txt")
    job_path = PREFIX.with_name(PREFIX.name + "-job.json")
    before = time.monotonic()
    job = {"started_utc": stamp(), "command": cmd, "cwd": str(Path.cwd()),
           "timeout_seconds": 30, "N": N, "timed_out": False,
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "stdout_path": str(stdout), "stderr_path": str(stderr)}
    with stdout.open("wb") as out, stderr.open("wb") as err:
        child = subprocess.Popen(cmd, stdout=out, stderr=err)
        job["child_pid"] = child.pid
        job_path.write_text(json.dumps(job, indent=2) + "\n")
        try:
            job["returncode"] = child.wait(timeout=30)
        except subprocess.TimeoutExpired:
            job["timed_out"] = True
            child.terminate()
            try:
                job["returncode"] = child.wait(timeout=3)
            except subprocess.TimeoutExpired:
                child.kill()
                job["returncode"] = child.wait(timeout=3)
        job["child_reaped"] = child.poll() is not None
    job["finished_utc"] = stamp()
    job["elapsed_seconds"] = time.monotonic() - before
    job_path.write_text(json.dumps(job, indent=2) + "\n")
    print(json.dumps(job, indent=2))
    print(stdout.read_text())
    if stderr.stat().st_size:
        print(stderr.read_text(), file=sys.stderr)
    assert not job["timed_out"] and job["returncode"] == 0 and job["child_reaped"]


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--child":
        main_child()
    else:
        assert len(sys.argv) == 1
        main_supervisor()
