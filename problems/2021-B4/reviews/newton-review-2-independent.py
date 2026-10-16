#!/usr/bin/env python3
"""R2 blind reconstruction. Does not read or import author programs/results.

Construct ordinary coefficients c_k directly from H_k(f)(w_k)=0.
Output paths belong exclusively to R2. Run through the bounded supervisor.
"""

import collections
import hashlib
import json
import math
from pathlib import Path
import sys
import time

D = 20
P = 19
BINOM = [[math.comb(n, k) for k in range(n + 1)] for n in range(D + 1)]
BASE = Path(__file__).resolve().parent
PREFIX = BASE / "newton-review-2"


def emit(**data):
    print(json.dumps(data, sort_keys=True), flush=True)


def trim(a):
    while a and a[-1] == 0:
        a.pop()
    return a


def add_scaled_shift(out, a, scale=1, shift=0):
    if not a or not scale:
        return
    need = len(a) + shift
    if len(out) < need:
        out.extend([0] * (need - len(out)))
    for i, value in enumerate(a):
        out[i + shift] += scale * value


def ordinary_family(center_mask, u_mask):
    """All lists are integer polynomial coefficients in U, ascending."""
    assert not (center_mask & u_mask)
    c = [[] for _ in range(D + 1)]
    c[D] = [1]
    c[D - 1] = [-D]
    for k in range(D - 2, 1, -1):
        bit = 1 << (D - k - 2)
        if not ((center_mask | u_mask) & bit):
            continue  # H_k(f)(0)=c_k, so c_k=0.
        use_u = bool(u_mask & bit)
        target = []
        for t in range(k + 1, D + 1):
            add_scaled_shift(target, c[t], -BINOM[t][k], t - k if use_u else 0)
        c[k] = trim(target)
        # The normalized a_j are integer polynomials, not merely rational.
        divisor = BINOM[D][k]
        assert all(value % divisor == 0 for value in c[k])
    at_one, at_u = [], []
    for k, coeff in enumerate(c):
        add_scaled_shift(at_one, coeff)
        add_scaled_shift(at_u, coeff, shift=k)
    return trim(at_one), trim(at_u)


def gcd_degree_mod(a, b, ell):
    a = trim([x % ell for x in a])
    b = trim([x % ell for x in b])
    while b:
        inverse = pow(b[-1], -1, ell)
        while len(a) >= len(b):
            factor = a[-1] * inverse % ell
            offset = len(a) - len(b)
            for i, value in enumerate(b):
                a[i + offset] = (a[i + offset] - factor * value) % ell
            trim(a)
        a, b = b, a
    return len(a) - 1


def binary_filter():
    """Use ordinary Hasse coefficients modulo p^2, no a_j recurrence."""
    modulus = P * P
    c = [0] * (D + 1)
    c[D], c[D - 1] = 1, -D
    passes = {}
    visited = 0

    def descend(k, mask):
        nonlocal visited
        if k == 1:
            visited += 1
            if sum(c) % modulus == 0:
                smallest = next(i for i in range(2, D - 1) if c[i] % modulus)
                passes[mask] = D - smallest
            if visited % 32768 == 0:
                emit(phase="binary_checkpoint", visited=visited, passes=len(passes))
            return
        c[k] = 0
        descend(k - 1, mask)
        c[k] = -sum(BINOM[t][k] * c[t] for t in range(k + 1, D + 1)) % modulus
        assert c[k] % P == 0
        descend(k - 1, mask | (1 << (D - k - 2)))
        c[k] = 0

    descend(D - 2, 0)
    assert visited == 2 ** (D - 3)
    assert len(passes) == len(set(passes))
    histogram = collections.Counter(passes.values())
    bit_h2 = 1 << (18 - 2)
    bit_h3 = 1 << (17 - 2)
    j17 = sorted(mask for mask, j in passes.items() if j == 17 and mask & bit_h2)
    j16 = sorted(mask for mask, j in passes.items() if j == 16 and mask & (bit_h2 | bit_h3))
    survivors = sorted(mask for mask, j in passes.items() if j < 16 or (j == 16 and mask & (bit_h2 | bit_h3)))
    assert all(mask & bit_h3 for mask in j17)
    result = dict(
        visited=visited,
        passes=len(passes),
        histogram=dict(sorted(histogram.items())),
        j17_retained_masks=j17,
        j17_discarded_masks=sorted(mask for mask, j in passes.items() if j == 17 and not mask & bit_h2),
        j16_retained_masks=j16,
        j16_discarded_masks=sorted(mask for mask, j in passes.items() if j == 16 and not mask & (bit_h2 | bit_h3)),
        remaining_masks=survivors,
    )
    Path(str(PREFIX) + "-patterns.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    emit(phase="binary_complete", visited=visited, passes=len(passes), histogram=dict(sorted(histogram.items())), j17_retained=len(j17), j16_retained=len(j16), remaining=len(survivors))
    return result


def initial_form_check():
    # Dividing the initial form by its nonzero C normalizes C=1.
    # This visits every normalized A!=0, B, alpha!=0 over F_19.
    hits = []
    visited = 0
    for a in range(1, P):
        for b in range(P):
            for alpha in range(1, P):
                visited += 1
                if (a + b * alpha + alpha * alpha) % P:
                    continue
                if (a + 3 * b * alpha + 6 * alpha * alpha) % P:
                    continue
                beta = (-b - alpha) % P
                assert b != 0
                assert alpha == -2 * b * pow(5, -1, P) % P
                assert beta == -3 * b * pow(5, -1, P) % P
                assert beta and alpha != beta
                assert (a + b * beta + beta * beta) % P == 0
                assert (b + 4 * alpha) % P == -3 * b * pow(5, -1, P) % P != 0
                assert (b + 4 * beta) % P == -7 * b * pow(5, -1, P) % P != 0
                hits.append(dict(A=a, B=b, C=1, alpha=alpha, beta=beta))
    assert len(hits) == P - 1
    result = dict(visited=visited, compatible_normalized_initial_forms=hits)
    Path(str(PREFIX) + "-initial-forms.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    emit(phase="initial_forms_complete", visited=visited, compatible=len(hits))
    return result


def compatibility_check(patterns):
    full_mask = (1 << 17) - 1
    count = 0
    certificates = collections.Counter()
    aggregate = hashlib.sha256()
    output = Path(str(PREFIX) + "-independent-cases.jsonl")
    with output.open("w") as stream:
        for center in patterns["j17_retained_masks"]:
            complement = full_mask ^ center
            sub = complement
            refinements = []
            while True:
                refinements.append(sub)
                if sub == 0:
                    break
                sub = (sub - 1) & complement
            assert len(refinements) == 2 ** complement.bit_count()
            for u_mask in sorted(refinements):
                f_one, f_u = ordinary_family(center, u_mask)
                payload = json.dumps({"P": f_one, "Q": f_u}, sort_keys=True, separators=(",", ":")).encode()
                aggregate.update(payload + b"\n")
                record = dict(center_mask=center, u_mask=u_mask, degrees=[len(f_one) - 1, len(f_u) - 1], ordinary_polynomial_sha256=hashlib.sha256(payload).hexdigest())
                if len(f_one) == 1 and f_one[0] != 0:
                    record["constant_P"] = f_one[0]
                    certificates["constant"] += 1
                else:
                    for ell in [101, 103, 107, 109]:
                        if not f_one or not f_u or f_one[-1] % ell == 0 or f_u[-1] % ell == 0:
                            continue
                        if gcd_degree_mod(f_one, f_u, ell) == 0:
                            record["ell"] = ell
                            record["leading_residues"] = [f_one[-1] % ell, f_u[-1] % ell]
                            record["gcd_degree"] = 0
                            certificates[str(ell)] += 1
                            break
                    else:
                        raise ArithmeticError(f"Unresolved family {center}, {u_mask}")
                stream.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
                count += 1
                if count % 1024 == 0:
                    stream.flush()
                    emit(phase="family_checkpoint", checked=count, certificates=dict(certificates))
    result = dict(checked=count, certificates=dict(certificates), ordinary_polynomial_stream_sha256=aggregate.hexdigest(), records_path=str(output), records_sha256=hashlib.sha256(output.read_bytes()).hexdigest())
    emit(phase="family_complete", **result)
    return result


def main():
    start = time.monotonic()
    emit(phase="start", python=sys.version, method="ordinary Hasse coefficients; complete mod p^2 binary tree; integer polynomial construction; Euclidean remainders over finite fields", author_code_or_results_read=False)
    patterns = binary_filter()
    forms = initial_form_check()
    families = compatibility_check(patterns)
    result = dict(binary_patterns=patterns["passes"], histogram=patterns["histogram"], j17_retained=len(patterns["j17_retained_masks"]), j16_retained=len(patterns["j16_retained_masks"]), remaining=len(patterns["remaining_masks"]), normalized_initial_form_cases=forms["visited"], compatible_initial_forms=len(forms["compatible_normalized_initial_forms"]), families=families, elapsed_seconds=time.monotonic() - start)
    Path(str(PREFIX) + "-independent-summary.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    emit(phase="complete", **result)


if __name__ == "__main__":
    main()
