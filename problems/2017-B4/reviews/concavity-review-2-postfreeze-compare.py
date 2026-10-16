#!/usr/bin/env python3
"""Post-blind-freeze comparison; never executes or rewrites constructor files."""

from datetime import datetime, timezone
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PREFIX = HERE / "concavity-review-2-postfreeze-comparison"
REPO = HERE.parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def now():
    return datetime.now(timezone.utc).isoformat()


def worker():
    freeze_path = HERE / "concavity-review-2-blind-initial-freeze-v1.json"
    assert sha(freeze_path) == "aa69df336924f90c3ccfa139e6d487105083939df7be0be90c7fd53ec9e184a2"
    freeze = json.loads(freeze_path.read_text())
    for record in freeze["owned_artifacts"]:
        assert sha(REPO / record["path"]) == record["sha256"], record["path"]
    print("blind frozen artifacts unchanged", flush=True)

    constructor = REPO / "problems/2017-B4/computations/deep-literature-r2-concavity-certificate.json"
    assert sha(constructor) == "8b5222a9240d6d6dd8126ccaaff8a2585523f1914e8e4b2932b6ae07fa14714f"
    c = json.loads(constructor.read_text())
    own = json.loads((HERE / "concavity-review-2-independent-certificate.json").read_text())

    spec = importlib.util.spec_from_file_location("reviewer_own_frozen_check", HERE / "concavity-review-2-independent-check.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.N = 80
    checks = {}
    logs80 = {}
    aliases = {"lnA": "ln107648over43687"}
    for name, data in c["log_intervals"].items():
        argument = Q(*data["argument"])
        actual = mod.log_bounds(argument)
        saved = (Q(*data["lower"]), Q(*data["upper"]))
        checks[name + "_80_exact_recomputed_match"] = actual == saved
        o = own["logs"][aliases.get(name, name)]
        unpack = lambda d: Q(int(d["numerator"]), int(d["denominator"]))
        lo96, hi96 = unpack(o["lower"]), unpack(o["upper"])
        checks[name + "_96_interval_nested_inside_80"] = saved[0] <= lo96 <= hi96 <= saved[1]
        logs80[name] = actual
        print("compared", name, "exactly", flush=True)

    l2, h2 = logs80["ln2"]
    l1, h1 = logs80["ln32over7"]
    ls, hs = logs80["ln79over58"]
    la, ha = logs80["lnA"]
    phi80 = ((Q(21,100)*l1 + Q(29,50)*ls)/h2 + Q(29,50),
             (Q(21,100)*h1 + Q(29,50)*hs)/l2 + Q(29,50))
    d80 = ((la + Q(7,32) + Q(21,79))/h2 - 2,
           (ha + Q(7,32) + Q(21,79))/l2 - 2)
    checks["phi_80_derived_endpoints_match"] = phi80 == tuple(Q(*c["phi_at_21over100"][k]) for k in ("lower","upper"))
    checks["derivative_80_derived_endpoints_match"] = d80 == tuple(Q(*c["derivative_at_21over100"][k]) for k in ("lower","upper"))
    checks["quarter_80_derived_upper_matches"] = 1 + logs80["ln3over2"][1]/(2*l2) == Q(*c["phi_at_quarter_upper"])
    checks["constructor_phi_upper_below_target"] = phi80[1] < Q(64951,50000)
    checks["constructor_derivative_strictly_positive_small"] = 0 < d80[0] <= d80[1] < Q(1,5000)
    checks["constructor_quarter_upper_below_target"] = Q(*c["phi_at_quarter_upper"]) < Q(1293,1000)
    checks["objective_half_equals_limsup_target"] = Q(*c["objective_bound"])/2 == Q(*c["candidate_limsup_bound"]) == Q(324757,500000)
    assert all(checks.values()), [k for k,v in checks.items() if not v]
    output = PREFIX.with_name(PREFIX.name + "-result.json")
    payload = {"completed_utc":now(),"status":"all post-freeze comparisons passed",
               "blind_freeze_sha256":sha(freeze_path),
               "constructor_certificate_sha256":sha(constructor),
               "constructor_code_executed":False,
               "constructor_files_modified":False,
               "method":"Own frozen logarithm routine, N=80, and exact Fraction endpoint comparisons; original blind run used N=96",
               "checks":checks}
    output.write_text(json.dumps(payload,indent=2)+"\n")
    print("all",len(checks),"exact comparison assertions passed",flush=True)


def supervisor():
    command = [sys.executable,"-B","-u",str(Path(__file__).resolve()),"--child"]
    stdout = PREFIX.with_name(PREFIX.name + "-stdout.txt")
    stderr = PREFIX.with_name(PREFIX.name + "-stderr.txt")
    job_path = PREFIX.with_name(PREFIX.name + "-job.json")
    job = {"started_utc":now(),"command":command,"timeout_seconds":30,
           "timed_out":False,"script_sha256":sha(Path(__file__))}
    started = time.monotonic()
    with stdout.open("wb") as out, stderr.open("wb") as err:
        child = subprocess.Popen(command,stdout=out,stderr=err)
        job["child_pid"] = child.pid
        job_path.write_text(json.dumps(job,indent=2)+"\n")
        try:
            job["returncode"] = child.wait(timeout=30)
        except subprocess.TimeoutExpired:
            job["timed_out"] = True
            child.kill()
            job["returncode"] = child.wait(timeout=3)
        job["child_reaped"] = child.poll() is not None
    job["finished_utc"] = now()
    job["elapsed_seconds"] = time.monotonic() - started
    job_path.write_text(json.dumps(job,indent=2)+"\n")
    print(json.dumps(job,indent=2))
    print(stdout.read_text())
    if stderr.stat().st_size:
        print(stderr.read_text(),file=sys.stderr)
    assert not job["timed_out"] and job["returncode"] == 0 and job["child_reaped"]


if __name__ == "__main__":
    if sys.argv[1:] == ["--child"]:
        worker()
    else:
        assert len(sys.argv) == 1
        supervisor()
