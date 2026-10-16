#!/usr/bin/env python3
"""Small explicit arithmetic certificates for a blind source audit.

These are evidence for the displayed finite calculations, not a search for
solutions or proof of an unrestricted Diophantine assertion. No CAS/imports
from another owner's code, no network, no spawned children, no mutable inputs.
"""

import json
from pathlib import Path


def order(a, modulus):
    for exponent in range(1, modulus):
        if pow(a, exponent, modulus) == 1:
            return exponent
    raise ValueError((a, modulus))


def fueter_coefficients(p, n):
    return [((n + 1) * c) // p - (n * c) // p for c in range(1, p)]


def fermat_map(coefficients, p):
    return sum(a * pow(c, -1, p) for c, a in enumerate(coefficients, 1)) % p


def galois_coefficients(coefficients, d, p):
    # sigma_d * sigma_c^-1 = sigma_(c/d)^-1.
    out = [0] * (p - 1)
    for c, a in enumerate(coefficients, 1):
        out[(c * pow(d, -1, p)) % p - 1] = a
    return out


psi51 = fueter_coefficients(5, 1)
psi52 = fueter_coefficients(5, 2)
assert psi51 == [0, 0, 1, 1]
assert psi52 == [0, 1, 0, 1]
assert [a + b for a, b in zip(psi51, galois_coefficients(psi52, 2, 5))] == [1] * 4
allowed_p5 = [
    [a, b, 2 - b, 2 - a]
    for a in range(3)
    for b in range(3)
    if fermat_map([a, b, 2 - b, 2 - a], 5) == 0
]
assert allowed_p5 == [[1, 1, 1, 1]]

psi72 = fueter_coefficients(7, 2)
assert psi72 == [0, 0, 1, 0, 1, 1]
assert fermat_map(psi72, 7) == 0
assert sum(psi72) == 3  # odd augmentation; lambda^psi has conjugate ratio -1

decomposition_examples = []
for p, q, r in [(5, 3, 2), (11, 3, 2)]:
    generated = []
    for exponent in range(1, (p - 1) * (q - 1) + 1):
        pair = (pow(r, exponent, p), pow(r, exponent, q))
        generated.append(pair)
        if pair == (1, 1):
            break
    intersection_with_h = [pair for pair in generated if pair[0] == 1]
    projection_to_h = sorted({pair[1] for pair in generated})
    assert intersection_with_h == [(1, 1)]
    assert projection_to_h != [1]
    decomposition_examples.append({
        "p": p, "q": q, "r": r,
        "order_r_mod_p": order(r, p),
        "order_r_mod_q": order(r, q),
        "generated_decomposition_subgroup": generated,
        "intersection_with_H_prime": intersection_with_h,
        "projection_to_H_prime": projection_to_h,
        "r_splits_in_C_prime": r % q == 1,
    })

assert pow(2, 5, 11) == 10
assert pow(2, 5, 3) == 2

# Gaussian illustration, represented by exact integer pairs.
b1 = complex(1, 2)
b = b1 * b1
chi = complex(-4, 2)
assert b == complex(-3, 4)
assert b - 5 == 2 * chi
assert 2j * b1 == chi
# All these magnitudes are small exact integral values; avoid floating norms.
norm_b = (-3) ** 2 + 4 ** 2
norm_chi = (-4) ** 2 + 2 ** 2
assert norm_b == 25 and norm_chi == 20
assert norm_chi % norm_b != 0

result = {
    "status": "finite arithmetic evidence; no unrestricted theorem inferred",
    "source_version": "arXiv:2509.18275v1",
    "p5": {
        "psi_1_inverse_basis": psi51,
        "psi_2_inverse_basis": psi52,
        "phi_values": [fermat_map(psi51, 5), fermat_map(psi52, 5)],
        "positive_relative_weight2_phi_zero_necessary_vectors": allowed_p5,
    },
    "p7": {
        "psi_2_inverse_basis": psi72,
        "phi": fermat_map(psi72, 7),
        "augmentation": sum(psi72),
        "sign_deduction": "conjugate ratio -1 and norm7 imply (lambda^psi_2)^2=-7",
    },
    "decomposition_examples": decomposition_examples,
    "local_norm_compatibility_p11_q3_r2": {
        "frobenius_power_for_conjugation": 5,
        "2_to_5_mod11": pow(2, 5, 11),
        "2_to_5_mod3": pow(2, 5, 3),
        "interpretation": "primitive cube root b in F_(2^10) has bar(b)=b^(-1), so b*bar(b)=1",
        "global_solution_claimed": False,
    },
    "gaussian_divisibility_illustration": {
        "b1_equals_b2": [1, 2], "b": [-3, 4],
        "D": 2, "z_to_k": 5, "chi": [-4, 2],
        "norm_b": norm_b, "norm_chi": norm_chi,
        "equation_2_solution_claimed": False,
    },
}

output = Path(__file__).with_name("strongfc-review-2-certificates-v1.json")
output.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": "completed", "output": str(output), "assertions": "passed"}))
