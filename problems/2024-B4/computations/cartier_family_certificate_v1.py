#!/usr/bin/env python3
"""Exact symbolic certificate for the 2024 B4(b) fixed-factor candidate v1.

Only Python's standard library is used. A polynomial is a finite set of
(z exponent, b exponent) pairs; coefficients are in GF(2), and b exponents
may be negative. Thus b is an indeterminate, never a sampled field value.

The three Cartier numerator identities are bounded polynomial identities
that hold for every nonzero formal parameter. The separate series checks
at m=0,1,2 are finite evidence and are not the infinite-family proof.
"""

import hashlib
import json
import platform
from pathlib import Path


HERE = Path(__file__).resolve().parent
ONE = frozenset({(0, 0)})
ZERO = frozenset()


def add(*polynomials):
    result = set()
    for polynomial in polynomials:
        result.symmetric_difference_update(polynomial)
    return frozenset(result)


def mul(left, right):
    result = set()
    for i, a in left:
        for j, b in right:
            result.symmetric_difference_update({(i + j, a + b)})
    return frozenset(result)


def shift(polynomial, z=0, b=0):
    return frozenset((i + z, a + b) for i, a in polynomial)


def frobenius(polynomial, power):
    assert power > 0 and power & (power - 1) == 0
    return frozenset((i * power, a * power) for i, a in polynomial)


def power_by_repeated_multiplication(polynomial, exponent):
    result = ONE
    for _ in range(exponent):
        result = mul(result, polynomial)
    return result


def section(polynomial, residue):
    assert 0 <= residue < 16
    return frozenset(((i - residue) // 16, a)
                     for i, a in polynomial if i % 16 == residue)


def encode(polynomial):
    return [list(term) for term in sorted(polynomial)]


def coefficients_by_z(polynomial):
    return {str(i): sorted(a for j, a in polynomial if i == j)
            for i in range(4)}


def main():
    print("Candidate proof - unverified; exact symbolic GF(2)[b,b^-1,z] certificate.", flush=True)
    print("Python", platform.python_version(), "; standard library only; no native CAS.", flush=True)
    k = frozenset({(0, 0), (2, 0), (3, 1), (3, -1), (4, 2)})
    p0 = frozenset({(0, 0), (1, 0), (2, 1)})
    u = frozenset({(1, 0)})
    v = frozenset({(2, 0), (3, 1)})
    v16 = frozenset({(2, 0), (3, 16)})
    l = frozenset((0, a) for a in range(-7, 8, 2))
    m = frozenset((0, a) for a in (-6, -4, -2, 0, 2, 6, 8))
    j = add(m, frozenset({(0, 4), (0, -12)}))

    # Reconstruct K^15 two ways, with no factorization oracle.
    k15 = ONE
    for exponent in (1, 2, 4, 8):
        k15 = mul(k15, frobenius(k, exponent))
    assert k15 == power_by_repeated_multiplication(k, 15)
    assert frobenius(k, 16) == frozenset({
        (0, 0), (32, 0), (48, 16), (48, -16), (64, 32)})
    print("K^15 reconstructed by binary Frobenius product and 15 multiplications:",
          len(k15), "terms; z-degree", max(i for i, _ in k15), flush=True)

    cases = [
        ("C5(F)", p0, 5, add(mul(add(l, m), u), mul(add(l, j), v16))),
        ("C6(z/K)", u, 6, mul(l, add(u, v16))),
        ("C6((z^2+b*z^3)/K)", v, 6, add(mul(m, u), mul(j, v16))),
    ]
    identities = []
    for name, numerator, residue, expected in cases:
        product = mul(numerator, k15)
        actual = section(product, residue)
        assert max(i for i, _ in product) <= 63
        assert actual == expected, (name, sorted(add(actual, expected)))
        assert not any(i == 0 for i, _ in actual)
        assert max(i for i, _ in actual) <= 3
        entry = {
            "name": name,
            "residue_mod_16": residue,
            "input_numerator": encode(numerator),
            "output_numerator": encode(actual),
            "output_coefficients_b_exponents_by_z": coefficients_by_z(actual),
            "zero_difference": encode(add(actual, expected)),
        }
        identities.append(entry)
        print(name, ": exact identity PASS; output", len(actual), "terms; b-exponents by z:",
              entry["output_coefficients_b_exponents_by_z"], flush=True)

    # Independent recurrence for F=(1+z+b*z^2)/K, only up to j_2=1637.
    # Laurent polynomials in b are represented as sets of integer exponents.
    limit = (32 * 16**2 - 7) // 5
    coefficients = []
    for index in range(limit + 1):
        value = {0} if index in (0, 1) else ({1} if index == 2 else set())
        if index >= 2:
            value.symmetric_difference_update(coefficients[index - 2])
        if index >= 3:
            value.symmetric_difference_update(a + 1 for a in coefficients[index - 3])
            value.symmetric_difference_update(a - 1 for a in coefficients[index - 3])
        if index >= 4:
            value.symmetric_difference_update(a + 2 for a in coefficients[index - 4])
        coefficients.append(frozenset(value))
    finite_checks = []
    for iteration in range(3):
        index = (32 * 16**iteration - 7) // 5
        exponent = 2 * index + 3
        assert format(index, "x") == "6" * iteration + "5"
        assert not coefficients[index]
        check = {"m": iteration, "j_m": index, "hex_j_m": format(index, "x"),
                 "n_m": exponent, "coefficient_is_zero": True}
        finite_checks.append(check)
        print("Finite recurrence evidence:", check, flush=True)

    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    certificate = {
        "status": "candidate proof - unverified; no independent adversarial audits",
        "coefficient_ring": "GF(2)[b,b^-1] with formal indeterminate b",
        "term_encoding": "[z exponent, b exponent] has coefficient one; omitted terms are zero",
        "k": encode(k), "k15": encode(k15),
        "l_b_exponents": sorted(a for _, a in l),
        "m_b_exponents": sorted(a for _, a in m),
        "j_b_exponents": sorted(a for _, a in j),
        "identities": identities,
        "finite_series_evidence_only": finite_checks,
        "general_argument": "The versioned proof uses the exact identities and span induction for every m>=0; finite series checks are not its proof.",
        "script_sha256": source_hash,
    }
    destination = HERE / "cartier-family-certificate-v1.json"
    destination.write_text(json.dumps(certificate, indent=2) + "\n")
    print("Wrote", destination.name, flush=True)
    print("Script SHA256", source_hash, flush=True)
    print("All specified exact checks complete. No classification or irreducibility claim.", flush=True)


if __name__ == "__main__":
    main()
