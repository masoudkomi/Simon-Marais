"""New R29 reviewer: one fixed proof certificate; documentary modes are separate.

No author/old executable is imported or executed. Mathematics uses sparse
bivariate Fraction polynomials and factorial-scaled coefficients, followed by
direct modular power sums. This differs from the author's integer-pair/Horner
certificate. No prime, height, depth, or generic root search occurs.
"""
import datetime as dt
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/coordinator-original-roots-r29-review-2-"
AUTHOR = "problems/2021-B4/notes/coordinator-original-roots-r29-"
PARENT = "problems/2021-B4/reviews/coordinator-global-return-r28-review-2-manifest-v1.json"


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def read_json(path):
    return json.loads((ROOT / path).read_text())


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def write_new(path, data):
    with (ROOT / path).open("x") as handle:
        handle.write(json.dumps(data, indent=2) + "\n")


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def add(poly, other, scale=F(1)):
    result = dict(poly)
    for key, value in other.items():
        result[key] = result.get(key, F(0)) + scale * value
    return clean(result)


def shift_h(poly, exponent):
    return {(h + exponent, b): value for (h, b), value in poly.items()}


def univariate(poly, b_degree):
    result = {h: value for (h, b), value in poly.items() if b == b_degree}
    assert all(value.denominator == 1 for value in result.values())
    return {h: int(value) for h, value in result.items()}


def multiply(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            result[i + j] = result.get(i + j, F(0)) + a * b
    return clean(result)


def divide_exact(numerator, denominator):
    remainder = {i: F(a) for i, a in numerator.items()}
    quotient = {}
    degree = max(denominator)
    while remainder and max(remainder) >= degree:
        shift = max(remainder) - degree
        value = remainder[max(remainder)] / denominator[degree]
        quotient[shift] = quotient.get(shift, F(0)) + value
        remainder = add(remainder, {i + shift: a for i, a in denominator.items()}, -value)
    return clean(quotient), remainder


def descending(poly):
    assert poly and all(F(a).denominator == 1 for a in poly.values())
    return [int(poly.get(i, 0)) for i in range(max(poly), -1, -1)]


def certificate_child():
    print("checkpoint: reconstructing factorial-scaled bivariate family", file=sys.stderr, flush=True)
    # Each key is (degree of h, degree of b). Enter mathematical low rows,
    # not a coefficient vector or an author-produced eliminant.
    low = {
        0: {(0, 0): 1}, 1: {(1, 0): -1}, 2: {}, 3: {(3, 0): 2},
        4: {}, 5: {}, 6: {(6, 0): -35},
        7: {(0, 0): -1, (1, 0): 7, (3, 0): -70, (6, 0): 245},
        8: {(0, 0): 7, (1, 0): -48, (3, 0): 448, (6, 0): -980, (0, 1): 1},
        9: {}, 10: {}, 19: {}, 20: {},
    }
    coefficients = {j: {key: F(a, math.factorial(j)) for key, a in poly.items()}
                    for j, poly in low.items()}
    for j, center_h in zip(range(11, 19), [True, True, True, False, True, False, True, False]):
        total = {}
        for i in range(j):
            term = shift_h(coefficients[i], j - i) if center_h else coefficients[i]
            total = add(total, term, -F(1, math.factorial(j - i)))
        coefficients[j] = total
    at_one, at_h = {}, {}
    for i in range(21):
        scale = F(math.factorial(20), math.factorial(20 - i))
        at_one = add(at_one, coefficients[i], scale)
        at_h = add(at_h, shift_h(coefficients[i], 20 - i), scale)
    assert all(b in (0, 1) for h, b in set(at_one) | set(at_h))
    q0, q1 = univariate(at_one, 0), univariate(at_one, 1)
    r0, r1 = univariate(at_h, 0), univariate(at_h, 1)
    n = add(multiply(r0, q1), multiply(r1, q0), -1)
    divisor = {3: F(125970), 2: F(-125970)}
    t, remainder = divide_exact(n, divisor)
    assert not remainder and max(n) == 29 and max(t) == 26
    assert clean(add(multiply(divisor, t), n, -1)) == {}
    t_desc = descending(t)
    residues = [a % 29 for a in t_desc]
    # Direct power sums, not the author's Horner evaluation.
    values = [sum(int(a) * pow(x, degree, 29) for degree, a in t.items()) % 29
              for x in range(29)]
    assert residues[0] == 24 and all(values)
    print("checkpoint: exact division and all 29 evaluations complete", file=sys.stderr, flush=True)
    computed = {
        "Q0_integer_coefficients_descending": descending(q0),
        "Q1_integer_coefficients_descending": descending(q1),
        "R0_integer_coefficients_descending": descending(r0),
        "R1_integer_coefficients_descending": descending(r1),
        "T_integer_coefficients_descending": t_desc,
        "T_coefficients_descending_mod29": residues,
        "T_values_at_0_through_28": values,
    }
    # Only now read the declared DATA for comparison. No author code is run.
    declared = read_json(AUTHOR + "sources-v1.json")["operative_standalone_certificate"]["complete_observed_stdout_semantic_JSON"]
    comparisons = {key: value == declared[key] for key, value in computed.items()}
    assert all(comparisons.values())
    print(json.dumps({
        "status": "PASS: fixed exact certificate only", "algorithm": "sparse bivariate factorial-scaled Fraction recurrence; exact long division; direct powers modulo 29",
        "degrees_Q0_Q1_R0_R1_N_T": [max(p) for p in (q0, q1, r0, r1, n, t)],
        "N_integer_coefficients_descending": descending(n),
        "identity": "N=125970*h^2*(h-1)*T", "division_remainder": {},
        "all_integer_coefficients": True, "leading_mod29": residues[0],
        "all29_nonzero": all(values), "declared_data_comparisons": comparisons,
        **computed,
    }, indent=2))


def certificate_wrapper():
    started = now()
    command = [sys.executable, str(Path(__file__).resolve()), "certificate-child"]
    child = subprocess.Popen(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(json.dumps({"child_PID": child.pid, "external_timeout_seconds": 15, "started_UTC": started}), flush=True)
    timed_out = False
    begin = time.monotonic()
    try:
        stdout, stderr = child.communicate(timeout=15)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.kill()
        stdout, stderr = child.communicate()
    output = {
        "started_UTC": started, "finished_UTC": now(), "command": command,
        "cwd": str(ROOT), "runs": 1, "fixed_field": 29,
        "external_timeout_seconds": 15, "child_PID": child.pid,
        "child_returncode": child.returncode, "child_reaped": child.poll() is not None,
        "timed_out": timed_out, "elapsed_seconds": time.monotonic() - begin,
        "dependencies": {"Python": sys.version, "libraries": "standard library only: fractions/math/json/subprocess/pathlib/datetime/hashlib/time"},
        "complete_stderr_checkpoints": stderr, "complete_stdout": stdout,
        "semantic_result": json.loads(stdout) if child.returncode == 0 else None,
        "author_or_old_executable_run": False,
    }
    write_new(PREFIX + "certificate-v1.json", output)
    assert child.returncode == 0 and not timed_out and output["child_reaped"]
    print(json.dumps({"PASS": True, "child_PID": child.pid, "reaped": True, "certificate_record": record(PREFIX + "certificate-v1.json")}, indent=2))


def prepare():
    author_freeze = record(AUTHOR + "freeze-v1.json")
    assert author_freeze["bytes"] == 2043
    assert author_freeze["sha256"] == "0fff6336528e3cb971f23e89626fb293a4d5658cdc38bbc4ef5e1d986b584233"
    frozen = read_json(AUTHOR + "freeze-v1.json")
    for declared in frozen["payloads"]:
        assert record(declared["path"]) == declared
    # Necessary accepted records once. Do not recurse into historical inventories.
    accepted = read_json(AUTHOR + "baseline-v1.json")["necessary_immutable_records"][:11]
    for declared in accepted:
        assert record(declared["path"]) == declared
    parent = record(PARENT)
    assert parent["bytes"] == 2349 and parent["sha256"] == "bb2f03228d01fb9290b0c6d4a2d3cb8cc3aa09674619c47f84edaeab170c1e53"
    guards = accepted + [author_freeze] + frozen["payloads"] + [parent]
    assert len(guards) == len({r["path"] for r in guards}) == 18
    write_new(PREFIX + "baseline-v1.json", {"captured_UTC": now(), "necessary_immutable_records": guards,
              "ONE_compact_OWN_parent": parent, "guard_occurrences": 18, "guard_unique_paths": 18,
              "recursive_inventory": False, "mutable_map_guards": False, "mathematics_certified_by_documentary_code": False})
    print(json.dumps({"prepared": True, "necessary_paths": 18, "baseline": record(PREFIX + "baseline-v1.json")}, indent=2))


def freeze():
    paths = [PREFIX + name for name in ["initial.md", "sources-v1.json", "checker-v1.py", "certificate-v1.json", "baseline-v1.json"]]
    initial = (ROOT / paths[0]).read_text()
    for i in range(1, 17):
        assert f"|R29R2-{i:02d}|" in initial
    for guard in read_json(PREFIX + "baseline-v1.json")["necessary_immutable_records"]:
        assert record(guard["path"]) == guard
    manifest = {
        "frozen_UTC": now(), "reviewer": "/root/review_2022_complexity_r2", "role": "OTHER initially blind WHOLE2",
        "ENTIRE_files": 6, "ALL_obligations": 16, "payloads": [record(p) for p in paths],
        "ONE_compact_OWN_parent": record(PARENT), "guard_occurrences": 18, "guard_unique_paths": 18,
        "FULL_final_ALL5_payload_MODEL_readbacks_completed": True,
        "FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED": True,
        "corresponding_NEW_peer_findings_files_inventory_hash_metadata_access": False,
        "findings_sealed_until_explicit_BOTH_release": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max"}, "independent_effective_backend_readback": None,
        "quota": {"start_usedPercent": 87, "usedPercent": 88, "observed_UTC": "2026-10-19 04:25:08 UTC", "resetsAt": 1792874445, "TOTAL_ceiling": 90, "checkpoint_at": 89, "reserve": True, "automatic_later_window": False},
    }
    write_new(PREFIX + "manifest-v1.json", manifest)
    print(json.dumps(record(PREFIX + "manifest-v1.json"), indent=2))


def verify():
    manifest = read_json(PREFIX + "manifest-v1.json")
    for declared in manifest["payloads"]:
        assert record(declared["path"]) == declared
    guards = read_json(PREFIX + "baseline-v1.json")["necessary_immutable_records"]
    for declared in guards:
        assert record(declared["path"]) == declared
    report = (ROOT / (PREFIX + "initial.md")).read_text()
    assert all(f"|R29R2-{i:02d}|" in report for i in range(1, 17))
    print(json.dumps({"verified_UTC": now(), "PASS": True, "ENTIRE_files": 6, "ALL_obligations": 16,
                      "necessary_paths": len(guards), "certificate_NOT_reexecuted": True,
                      "manifest": record(PREFIX + "manifest-v1.json")}, indent=2))


if __name__ == "__main__":
    {"certificate-child": certificate_child, "certificate": certificate_wrapper,
     "prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
