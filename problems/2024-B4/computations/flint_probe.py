#!/usr/bin/env python3
"""Bounded exact CAS factorization evidence, with independent multiply-back."""
import json
import subprocess
import sys
from pathlib import Path
import flint
import invariant_probe as sparse

HERE = Path(__file__).resolve().parent
C = flint.fmpz_mod_mpoly_ctx.get(("x", "y", "z"), 2, "lex")
x, y, z = C.gens()


def factor_back(p):
    c, factors = p.factor()
    rebuilt = C.constant(c)
    for factor, exponent in factors:
        rebuilt *= factor ** exponent
    assert rebuilt == p
    return c, factors


def one(n):
    sp = sparse.direct_phi(n)
    p = C.from_dict({u: 1 for u in sp})
    _, factors = factor_back(p)
    records = []
    for f, e in factors:
        terms = f.to_dict()
        total_degree = int(max(sum(u) for u in terms))
        records.append({"exponent":int(e), "degree":total_degree,
                        "terms":sorted(tuple(int(a) for a in u) for u in terms)})
    return {"n":n,"factors":records}


def save(results):
    (HERE/"flint-factor-certificates.json").write_text(json.dumps({
        "field":"GF(2)","python_flint":flint.__version__,
        "status":"bounded exact CAS factorization and multiply-back; irreducibility is CAS evidence only",
        "results":results},indent=2)+"\n")


def main():
    print("python-flint", flint.__version__)
    example = (x+y)*(x*x+y*z+1)
    print("API sanity:", factor_back(example), "; multiply-back exact")
    results = []
    # n205 is independently certified in n205-certificate.json; avoid repeating its expensive CAS factorization.
    # Every native factorization is isolated and has a 30 second wall-clock deadline.
    for n in (5, 7, 9, 13, 21, 25, 29, 41, 45, 57):
        try:
            child = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--one", str(n)],
                                   check=True, capture_output=True, text=True, timeout=30)
            record = json.loads(child.stdout)
            records = record["factors"]
            print("n",n,"CAS factor degrees/multiplicities",[(a["degree"],a["exponent"]) for a in records],
                  "multiply-back exact",flush=True)
        except subprocess.TimeoutExpired:
            record = {"n":n,"status":"timeout after 30 seconds; incomplete factorization"}
            print("n",n,"timeout after 30 seconds; incomplete",flush=True)
        results.append(record)
        save(results)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--one":
        print(json.dumps(one(int(sys.argv[2]))))
    else:
        main()
