#!/usr/bin/env python3
"""Small exact certificates for source-audit queries, not a CA search.

The parent always runs the algebra worker as a subprocess with a 30 s timeout,
prints its PID and parameters, and kills only that child if the timeout fires.
"""
import argparse
import json
import os
import subprocess
import sys
import time


def report(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def worker():
    import sympy as sp

    report(event="checkpoint", pid=os.getpid(), task="exact small identities",
           python=sys.version.split()[0], sympy=sp.__version__)
    t, X = sp.symbols("t X")
    ambient = sp.expand((1 - t * X) * (1 + t * X) + X**2 * t**2 - 1)
    report(event="ambient_coefficient_identity", residual=str(ambient),
           coefficients_of_c=["1", "-t"], ideal="(t^2)", prime="(t)",
           scope="ambient local-ring certificate only")

    x, y, z = sp.symbols("x y z")
    f = [y**2, x*y, x**2, z]
    g = [sp.Integer(1), sp.Integer(2), sp.Integer(3), sp.Integer(1)]
    a, b, h = x**2 - 3*z, x*y - 2*z, y**2 - z
    # The three minors against column 4 generate every minor, since g_4=1.
    minors = [sp.expand(f[i]*g[j] - f[j]*g[i])
              for i in range(4) for j in range(i+1, 4)]
    certificate = (z+h)*a + (-4*z-b)*b + 3*z*h
    report(event="determinantal_nilpotent_model",
           f=[str(q) for q in f], g=[str(q) for q in g],
           minors=[str(q) for q in minors],
           z_squared_certificate_residual=str(sp.expand(certificate-z**2)),
           polynomial_unit_identity_residual=str(sp.expand(
               (1-z*X)*(1+z*X) + X**2*certificate - 1)),
           scope="local algebra model; not the specialized derivative construction")

    # Repeated differentiation is unnecessary: exact expansion certifies the
    # incidence equation and the explicit escaping family b=1/u.
    u = sp.symbols("u", nonzero=True)
    escape = sp.cancel(1*(1/u) - u*(1/u)**2)
    report(event="incidence_escape", map="b -> (b,b^2)",
           incidence="k2*b-k1*b^2=0", family="b=1/u, [k1:k2]=[u:1]",
           residual=str(escape), limit="([B0:B1],[k1:k2])=([0:1],[0:1])",
           scope="general closure/fiber inference only")
    report(event="complete", all_identity_residuals_zero=bool(
        ambient == 0 and sp.expand(certificate-z**2) == 0 and escape == 0))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    args = parser.parse_args()
    if args.worker:
        worker()
        return
    command = [sys.executable, os.path.abspath(__file__), "--worker"]
    started = time.monotonic()
    child = subprocess.Popen(command)
    report(event="child_started", pid=child.pid, command=command, timeout_seconds=30)
    try:
        exit_code = child.wait(timeout=30)
    except subprocess.TimeoutExpired:
        child.kill()
        exit_code = child.wait()
        report(event="timeout", pid=child.pid, exit_code=exit_code)
        raise SystemExit(124)
    report(event="child_finished", pid=child.pid, exit_code=exit_code,
           elapsed_seconds=round(time.monotonic()-started, 6))
    raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
