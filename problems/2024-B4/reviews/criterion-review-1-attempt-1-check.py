#!/usr/bin/env python3
"""Blind independent audit of the frozen v1 fixed-factor criterion.

No author implementation is imported or executed. Polynomials are finite
sets of exponent tuples, addition is symmetric difference, and subspaces
are complete sets of their polynomial vectors. The default entry point
runs this file's child under a dedicated wall-clock timeout.
"""

from __future__ import annotations

import collections
import datetime
import hashlib
import itertools
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
YEAR = HERE.parent
ROOT = YEAR.parent.parent
PREFIX = HERE / "criterion-review-1"
LIMIT = 45
COEFFICIENT_LIMIT = 65535
FROZEN_CRITERION = "59e3bb1f9aba8162ea5b79f0ccec5f56b6f2cb0cc7917cfe81f4aff196ff6ab4"
FROZEN_MANIFEST = "41fef0ca55da72d8efc8fb04f3b0180f77fc43edf28b276a87f7bd033b6687f2"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def log(message):
    print(message, flush=True)


def add(*polynomials):
    out = frozenset()
    for polynomial in polynomials:
        out = out ^ polynomial
    return out


def mul(a, b):
    out = set()
    for first in a:
        for second in b:
            term = tuple(x + y for x, y in zip(first, second))
            if term in out:
                out.remove(term)
            else:
                out.add(term)
    return frozenset(out)


def power(a, exponent, variables):
    out = frozenset({(0,) * variables})
    while exponent:
        if exponent & 1:
            out = mul(out, a)
        a = mul(a, a)
        exponent >>= 1
    return out


def child():
    started = time.monotonic()
    result = {
        "independent_reviewer": "criterion-review-1",
        "started_utc": stamp(),
        "python": platform.python_version(),
        "pid": os.getpid(),
        "dependencies": "Python standard library only",
        "scope": "2024 B4(b), exact whole-phi_13 divisibility criterion only",
        "construction_code_read_imported_or_executed": False,
        "other_reviews_read": False,
    }
    candidate = YEAR / "notes/zero-automaton-criterion-v1.md"
    manifest_path = YEAR / "notes/zero-automaton-v1-manifest.json"
    assert digest(candidate) == FROZEN_CRITERION
    assert digest(manifest_path) == FROZEN_MANIFEST
    manifest = json.loads(manifest_path.read_text())
    frozen_hashes = {}
    for relative, expected in manifest["files_sha256"].items():
        observed = digest(YEAR / relative)
        assert observed == expected, relative
        frozen_hashes[relative] = observed
    result["frozen_input_hashes"] = frozen_hashes
    result["manifest_sha256"] = digest(manifest_path)
    result["official_paper_cached_sha256"] = digest(ROOT / ".cache/official/2024-paper_b.pdf")
    log("PASS: criterion, manifest, and every listed artifact retain their frozen hashes")

    # Exact ordinary polynomial identities in F2[x,y,z].
    one = frozenset({(0, 0, 0)})
    zero = frozenset()
    x = frozenset({(1, 0, 0)})
    y = frozenset({(0, 1, 0)})
    z = frozenset({(0, 0, 1)})
    w = add(x, y, z)
    Q = add(power(x, 2, 3), power(y, 2, 3), power(z, 2, 3), mul(x, y), mul(y, z), mul(z, x))
    R = mul(mul(add(x, y), add(y, z)), add(z, x))
    D = mul(mul(mul(x, y), z), w)
    elementary = [one]
    for a in (x, y, z, w):
        next_coefficients = [zero] * (len(elementary) + 1)
        for i, value in enumerate(elementary):
            next_coefficients[i] = add(next_coefficients[i], value)
            next_coefficients[i + 1] = add(next_coefficients[i + 1], mul(value, a))
        elementary = next_coefficients
    assert elementary == [one, zero, Q, R, D]
    leading = [max(Q), max(power(R, 2, 3)), max(D)]
    assert leading == [(2, 0, 0), (4, 2, 0), (2, 1, 1)]
    determinant = (
        leading[0][0] * (leading[1][1] * leading[2][2] - leading[2][1] * leading[1][2])
        - leading[1][0] * (leading[0][1] * leading[2][2] - leading[2][1] * leading[0][2])
        + leading[2][0] * (leading[0][1] * leading[1][2] - leading[1][1] * leading[0][2])
    )
    assert determinant == 4
    squared_root_relations = []
    for a in (x, y, z):
        quartic = add(power(a, 4, 3), mul(Q, power(a, 2, 3)), mul(R, a), D)
        monic_eighth = add(power(a, 8, 3), mul(power(Q, 2, 3), power(a, 4, 3)), mul(power(R, 2, 3), power(a, 2, 3)), power(D, 2, 3))
        assert not quartic and not monic_eighth
        squared_root_relations.append(True)
    A_image = add(power(Q, 5, 3), mul(Q, power(D, 2, 3)), mul(power(R, 2, 3), D))
    f13 = add(*(power(a, 13, 3) for a in (x, y, z, w)))
    assert mul(R, A_image) == f13
    # The formal recurrence, using exponent coordinates (q,u,d).
    q = x
    u = y
    d = z
    formal = []
    for j in range(21):
        value = one if j == 0 else q if j == 1 else d if j == 2 else zero
        if j >= 2:
            value = add(value, mul(power(q, 2, 3), formal[j - 2]))
        if j >= 3:
            value = add(value, mul(u, formal[j - 3]))
        if j >= 4:
            value = add(value, mul(power(d, 2, 3), formal[j - 4]))
        assert all(2 * a + 6 * b + 4 * c == 2 * j for a, b, c in value)
        formal.append(value)
    assert formal[5] == frozenset({(5, 0, 0), (1, 0, 2), (0, 1, 1)})
    result["finite_algebra"] = {
        "elementary_symmetric_identity": True,
        "P5": sorted(formal[5]),
        "leading_monomials": leading,
        "integer_exponent_determinant": determinant,
        "three_quartic_and_squared_monic_identities": squared_root_relations,
        "R_times_A_image_equals_f13": True,
        "A_image_term_count": len(A_image),
        "recurrence_weight_checked_through_j": 20,
    }
    log("PASS: elementary symmetric identity, P5, phi13 identity, leading monomials and three monic relations")

    # Independent Laurent-support implementation. All vectors are represented
    # as support sets, and every subspace stores every vector, including zero.
    basis = tuple((i, h) for i in range(4) for h in range(-1, 3))
    positions = {term: i for i, term in enumerate(basis)}
    K = frozenset({(0, 0), (2, 0), (3, -1), (3, 1), (4, 2)})
    P = frozenset({(0, 0), (1, 0), (2, 1)})

    def encode(polynomial):
        assert polynomial <= positions.keys()
        return sum(1 << positions[term] for term in polynomial)

    def decode(mask):
        assert 0 <= mask < (1 << 16)
        return frozenset(term for i, term in enumerate(basis) if (mask >> i) & 1)

    def section(polynomial, r, t):
        return frozenset(((i - r) // 2, (h - t) // 2) for i, h in polynomial if i % 2 == r and h % 2 == t)

    def L(polynomial, r, t):
        product = mul(polynomial, K)
        assert all(0 <= i <= 7 and -2 <= h <= 4 for i, h in product)
        answer = section(product, r, t)
        assert all(0 <= i <= 3 and -1 <= h <= 2 for i, h in answer)
        return answer

    def span(generators):
        space = {frozenset()}
        for generator in generators:
            if generator not in space:
                space.update(vector ^ generator for vector in tuple(space))
        return frozenset(space)

    def advance(space, r):
        return span(L(vector, r, t) for vector in space for t in (0, 1))

    columns = {str(r) + str(t): [encode(L(frozenset({term}), r, t)) for term in basis] for r in (0, 1) for t in (0, 1)}
    start = span((P,))
    states = [start]
    indices = {start: 0}
    transitions = []
    for space in states:
        row = []
        for r in (0, 1):
            target = advance(space, r)
            if target not in indices:
                assert len(states) < 1000
                indices[target] = len(states)
                states.append(target)
            row.append(indices[target])
        transitions.append(row)
    accepting = [all(all(i != 0 for i, h in vector) for vector in space) for space in states]
    assert len(states) == len(transitions) == 48
    assert len(set(states)) == 48
    assert sum(accepting) == 6
    raw = json.loads((YEAR / "computations/zero-automaton-v1-graph.json").read_text())
    assert raw["monomial_bit_order"] == [list(term) for term in basis]
    assert raw["operators_columns"] == columns
    raw_spaces = [span(decode(mask) for mask in row) for row in raw["states_rref"]]
    assert len(raw_spaces) == len(set(raw_spaces)) == 48
    correspondence = [indices[space] for space in raw_spaces]
    assert set(correspondence) == set(range(48))
    assert raw_spaces[raw["initial_state"]] == start
    for s in range(48):
        assert accepting[correspondence[s]] == raw["accepting"][s]
        for r in (0, 1):
            assert transitions[correspondence[s]][r] == correspondence[raw["transitions"][s][r]]
        rows = raw["states_rref"][s]
        pivots = [row.bit_length() - 1 for row in rows]
        assert pivots == sorted(pivots, reverse=True)
        for row_number, pivot in enumerate(pivots):
            assert all(((row >> pivot) & 1) == (i == row_number) for i, row in enumerate(rows))
        assert len(raw_spaces[s]) == (1 << len(rows))
    # Check the rendered certificate itself, rather than only its JSON input.
    certificate_rows = {}
    rendered_columns = {}
    for line in (YEAR / "notes/zero-automaton-certificate-v1.md").read_text().splitlines():
        if not line.startswith("|"):
            continue
        parts = [cell.strip() for cell in line.strip("|").split("|")]
        if not parts[0].isdigit():
            continue
        if len(parts) == 7:
            bit, i, h, *values = map(int, parts)
            assert basis[bit] == (i, h)
            rendered_columns[bit] = values
        elif len(parts) == 6:
            s = int(parts[0])
            certificate_rows[s] = parts
            assert [int(mask.strip()) for mask in parts[1].split(",")] == raw["states_rref"][s]
            assert list(map(int, parts[2:4])) == raw["transitions"][s]
            assert (parts[4] == "yes") == raw["accepting"][s]
    assert set(certificate_rows) == set(range(48))
    assert set(rendered_columns) == set(range(16))
    for bit in range(16):
        assert rendered_columns[bit] == [columns[key][bit] for key in ("00", "01", "10", "11")]
    log("PASS: all 64 columns, all 48 complete subspaces, all 96 transitions, all outputs and both rendered tables")

    # Minimize the independently reconstructed machine, then compare the
    # proposed quotient and all its members. No minimization code is imported.
    blocks = [frozenset(i for i, flag in enumerate(accepting) if flag == output) for output in (False, True)]
    refinements = 0
    while True:
        owner = {s: block_number for block_number, block in enumerate(blocks) for s in block}
        signatures = {}
        for s in range(48):
            signature = (accepting[s], *(owner[t] for t in transitions[s]))
            signatures.setdefault(signature, set()).add(s)
        replacement = [frozenset(group) for group in signatures.values()]
        if set(replacement) == set(blocks):
            break
        blocks = replacement
        refinements += 1
    assert len(blocks) == 8
    claims = {}
    for line in candidate.read_text().splitlines():
        if not line.startswith("|"):
            continue
        parts = [cell.strip() for cell in line.strip("|").split("|")]
        if len(parts) == 5 and parts[0] in {"X", "S", "A", "B", "Z", "C", "D", "E"}:
            name, next0, next1, flag, members = parts
            claims[name] = (next0, next1, flag == "yes", frozenset(map(int, members.split(","))))
    assert len(claims) == 8
    assert set().union(*(data[3] for data in claims.values())) == set(range(48))
    assert sum(len(data[3]) for data in claims.values()) == 48
    state_names = {s: name for name, data in claims.items() for s in data[3]}
    for name, (next0, next1, flag, members) in claims.items():
        for s in members:
            assert certificate_rows[s][5] == name
            assert raw["accepting"][s] == flag
            assert [state_names[t] for t in raw["transitions"][s]] == [next0, next1]
    assert {frozenset(correspondence[s] for s in data[3]) for data in claims.values()} == set(blocks)

    # Epsilon NFA built directly from regex 101(0011)*0*. The loop uses
    # 3-0->4-0->5-1->6-1->3; epsilon 3->7 starts the terminal zero loop.
    edges = {(0, 1): {1}, (1, 0): {2}, (2, 1): {3}, (3, 0): {4}, (4, 0): {5}, (5, 1): {6}, (6, 1): {3}, (7, 0): {7}}

    def closure(group):
        return frozenset(set(group) | ({7} if 3 in group else set()))

    def regex_step(group, bit):
        return closure(set().union(*(edges.get((s, bit), set()) for s in group)))

    initial_pair = (0, closure({0}))
    products = {initial_pair}
    queue = collections.deque([initial_pair])
    regex_states = set()
    while queue:
        s, regex_state = queue.popleft()
        regex_states.add(regex_state)
        assert accepting[s] == (7 in regex_state)
        for r in (0, 1):
            pair = (transitions[s][r], regex_step(regex_state, r))
            if pair not in products:
                products.add(pair)
                queue.append(pair)
    assert len(products) == 48 and len(regex_states) == 8
    result["automaton"] = {
        "operators_columns": columns,
        "complete_vector_states": [sorted(encode(vector) for vector in state) for state in states],
        "transitions": transitions,
        "accepting": accepting,
        "state_count": len(states),
        "maximum_full_subspace_size": max(map(len, states)),
        "dimension_counts": dict(sorted(collections.Counter(len(state).bit_length() - 1 for state in states).items())),
        "raw_to_independent_state_correspondence": correspondence,
        "minimal_partition": sorted([sorted(block) for block in blocks]),
        "refinement_count": refinements,
        "claimed_quotient_and_rendered_tables_match": True,
        "regex": "101(0011)*0*",
        "all_word_equivalence_product_states": len(products),
        "regex_determinized_state_count": len(regex_states),
        "closed_finite_language_product_checked": True,
    }
    log("PASS: eight quotient classes and all-word equivalence to regex by a closed product-automaton check")

    # Finite evidence only: a separate recurrence, using a bounded integer
    # Laurent coefficient representation. Exponent h is bit h+offset; the
    # bound h>=-j prevents any low-bit truncation for j<=COEFFICIENT_LIMIT.
    offset = COEFFICIENT_LIMIT + 8
    recent = []
    zero_indices = []

    def machine_accepts(j):
        s = 0
        while j:
            s = transitions[s][j & 1]
            j >>= 1
        return accepting[s]

    for j in range(COEFFICIENT_LIMIT + 1):
        value = (1 << offset) if j in (0, 1) else (1 << (offset + 1)) if j == 2 else 0
        if j >= 2:
            value ^= recent[-2]
        if j >= 3:
            value ^= (recent[-3] << 1) ^ (recent[-3] >> 1)
        if j >= 4:
            value ^= recent[-4] << 2
        assert not (value & 255)
        assert (value == 0) == machine_accepts(j), j
        if value == 0:
            zero_indices.append(j)
        recent.append(value)
        recent = recent[-4:]
        if j and j % 16384 == 0:
            log(f"CHECKPOINT: direct Laurent recurrence matched through j={j}")
    expected = []
    next_j = 5
    while next_j <= COEFFICIENT_LIMIT:
        expected.append(next_j)
        next_j = 16 * next_j + 21
    assert zero_indices == expected
    result["finite_coefficient_evidence_only"] = {
        "j_interval_inclusive": [0, COEFFICIENT_LIMIT],
        "zero_indices": zero_indices,
        "corresponding_n": [2 * j + 3 for j in zero_indices],
        "all_match_automaton": True,
        "not_a_proof_by_extrapolation": True,
    }
    result["elapsed_seconds"] = time.monotonic() - started
    result["finished_utc"] = stamp()
    result["status"] = "PASS: independent exact finite checks; general arguments audited in report"
    write_json(str(PREFIX) + "-result.json", result)
    log(json.dumps({"status": result["status"], "elapsed_seconds": result["elapsed_seconds"], "zero_indices": zero_indices}, sort_keys=True))


def harness():
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "--child"]
    output_path = Path(str(PREFIX) + "-output.txt")
    error_path = Path(str(PREFIX) + "-stderr.txt")
    job_path = Path(str(PREFIX) + "-job.json")
    job = {"command": command, "cwd": str(ROOT), "timeout_seconds": LIMIT, "coefficient_limit": COEFFICIENT_LIMIT, "started_utc": stamp(), "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "verified_effective_settings": None, "cleanup_scope": "Only this explicitly identified dedicated child PID"}
    started = time.monotonic()
    with output_path.open("w") as out, error_path.open("w") as err:
        process = subprocess.Popen(command, cwd=ROOT, stdout=out, stderr=err)
        job["child_pid"] = process.pid
        job["status"] = "running"
        write_json(job_path, job)
        log(f"Dedicated review child PID={process.pid}; explicit timeout={LIMIT}s")
        try:
            returncode = process.wait(timeout=LIMIT)
            job["status"] = "completed" if returncode == 0 else "failed"
        except subprocess.TimeoutExpired:
            job["status"] = "timed_out"
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=3)
            returncode = process.returncode
    job.update(returncode=returncode, finished_utc=stamp(), elapsed_seconds=time.monotonic() - started, child_reaped=process.poll() is not None)
    job["sha256"] = {path.name: digest(path) for path in (Path(__file__).resolve(), output_path, error_path)}
    result_path = Path(str(PREFIX) + "-result.json")
    if result_path.exists():
        job["sha256"][result_path.name] = digest(result_path)
    write_json(job_path, job)
    log(output_path.read_text())
    if error_path.stat().st_size:
        log(error_path.read_text())
    log(json.dumps({"job_status": job["status"], "elapsed_seconds": job["elapsed_seconds"], "child_reaped": job["child_reaped"]}, sort_keys=True))
    raise SystemExit(0 if job["status"] == "completed" else 1)


if __name__ == "__main__":
    if sys.argv[1:] == ["--child"]:
        child()
    elif not sys.argv[1:]:
        harness()
    else:
        raise SystemExit("usage: criterion-review-1-check.py [--child]")
