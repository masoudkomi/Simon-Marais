#!/usr/bin/env python3
"""Finite supplemental checks for the blind R2 audit, not unrestricted proofs.

Run with the installed research Python runtime. Each CAS child is bounded by
20 seconds. PID, parameters, output, errors and timeout state are checkpointed.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import time


def child(e, o):
    import sympy as s
    import flint

    D, P, N = s.symbols("D P N")
    F = [s.Integer(0), s.Integer(1)]
    for j in range(2, e + 1):
        F.append(s.expand(D * F[-1] + P * F[-2]))
    delta = e - o
    L = o * (e - 1)
    m = (e - 2) // 2
    expected_unit = D ** ((e - 1) * (o - 1) // 2)
    actual_unit = s.resultant(F[e], F[o], P)
    unit_ratio = s.cancel(actual_unit / expected_unit)
    assert unit_ratio in (-1, 1)
    A = F[e] - F[o]
    B = (D**2 + 4 * P) * F[o] ** 2 - 4 * N
    R = s.Poly(s.resultant(A, B, P), D, N)
    expected_constant = D ** (e * (o - 1)) * (
        (e // 2) * D**delta - 2 ** (delta - 1) * o
    )
    constant_ratio = s.cancel(R.as_expr().subs(N, 0) / expected_constant)
    assert constant_ratio in (-1, 1)
    weights = sorted({i + 2 * o * j for (i, j), c in R.terms()})
    assert max(weights) == L
    assert all((L - w) % delta == 0 for w in weights)
    assert all(c.is_Integer for _, c in R.terms())
    assert all(L - i >= 2 * o for (i, j), c in R.terms() if j >= 1)

    # The formal resultant has the original degree m even if specialization
    # drops A's degree. B has leading coefficient 4 and unchanged degree o.
    specializations = []
    for d0 in ([s.Rational(2, e)] if delta == 1 else []) + [s.Integer(0)]:
        a0 = s.Poly(A.subs(D, d0), P)
        b0 = s.Poly(B.subs(D, d0), P)
        dropped = m - a0.degree()
        actual_specialized = s.resultant(a0.as_expr(), b0.as_expr(), P)
        fixed_degree_specialized = R.as_expr().subs(D, d0)
        # Resultant conventions can introduce a sign when the degree changes.
        difference_plus = s.expand(
            fixed_degree_specialized - 4**dropped * actual_specialized
        )
        difference_minus = s.expand(
            fixed_degree_specialized + 4**dropped * actual_specialized
        )
        assert difference_plus == 0 or difference_minus == 0
        specializations.append(
            {"D": str(d0), "A_degree": a0.degree(), "degree_drop": dropped,
             "formal_vs_actual_resultant": "equal up to sign times 4^drop"}
        )
    print(json.dumps(
        {"e": e, "o": o, "sympy": s.__version__, "flint": flint.__version__,
         "unit_ratio": str(unit_ratio),
         "constant_ratio": str(constant_ratio), "L": L, "weights": weights,
         "R_terms": len(R.terms()), "specializations": specializations},
        sort_keys=True), flush=True)


def main():
    base = Path(__file__).resolve().parent
    proof = base.parent / "notes" / "candidate-resultant-v0.1.md"
    log_path = base / "review-2-evidence.txt"
    pairs = [(4, 3), (6, 5), (8, 3), (8, 5), (8, 7),
             (10, 3), (10, 7), (12, 5), (14, 9)]
    # Preserve prior failed runs as well as successful runs.
    with log_path.open("a", encoding="utf-8") as log:
        def record(obj):
            line = json.dumps(obj, sort_keys=True)
            print(line, flush=True)
            log.write(line + "\n")
            log.flush()

        record({"kind": "header", "evidence_only": True,
                "started_utc": datetime.now(timezone.utc).isoformat(),
                "candidate_sha256": hashlib.sha256(proof.read_bytes()).hexdigest(),
                "python": sys.version, "executable": sys.executable,
                "child_timeout_seconds": 20})
        for e, o in pairs:
            command = [sys.executable, str(Path(__file__).resolve()),
                       "--child", str(e), str(o)]
            start = time.monotonic()
            p = subprocess.Popen(command, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True)
            record({"kind": "child_start", "pid": p.pid,
                    "parameters": {"e": e, "o": o}, "command": command})
            timed_out = False
            try:
                out, err = p.communicate(timeout=20)
            except subprocess.TimeoutExpired:
                timed_out = True
                p.kill()  # Targeted cleanup of this child only.
                out, err = p.communicate()
            record({"kind": "child_complete", "pid": p.pid,
                    "parameters": {"e": e, "o": o}, "returncode": p.returncode,
                    "timed_out": timed_out,
                    "elapsed_seconds": round(time.monotonic() - start, 4),
                    "stdout": out.strip(), "stderr": err.strip()})

        # Exhaustive finite check of the derived necessary divisibility (17).
        checked = 0
        exceptions = []
        for o in range(3, 16, 2):
            for e in range(o + 1, 61, 2):
                if math.gcd(e, o) != 1:
                    continue
                delta = e - o
                for q in range(2, 11):
                    for p in range(1, q):
                        if math.gcd(p, q) != 1:
                            continue
                        checked += 1
                        H = (e // 2) * p**delta - 2 ** (delta - 1) * o * q**delta
                        if H % q ** (2 * o) == 0:
                            exceptions.append({"e": e, "o": o, "p": p, "q": q})
        record({"kind": "finite_divisibility_check", "checked": checked,
                "bounds": {"o_odd": [3, 15], "e_even": [4, 60], "q": [2, 10]},
                "exceptions": exceptions,
                "note": "Finite evidence only; not used as a proof of (C)."})


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--child", nargs=2, type=int)
    args = parser.parse_args()
    if args.child:
        child(*args.child)
    else:
        main()
