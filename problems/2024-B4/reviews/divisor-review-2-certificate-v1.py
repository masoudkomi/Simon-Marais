"""Independent fixed phi11 certificate audit; no graph or coefficient search.

The 15 bases and 30 proposed targets are data from the candidate table.
Maps are rebuilt by the six shifted monomials of the actual denominator.
Canonical Gaussian elimination supplies one check; complete finite vector
sets supply an additional equality check on every declared transition.
"""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "divisor-review-2-certificate-output-v1.json"
BASES = [
    [137], [1032, 73], [200, 17], [1025, 513, 129, 64],
    [1024, 137, 72, 25], [1025, 128, 64, 9], [128, 72, 24, 1],
    [1024, 512, 137, 72], [1024, 128, 64, 16, 8],
    [1024, 512, 128, 64, 8, 1], [1024, 128, 64, 16, 8, 1],
    [1025, 513, 129, 64, 9], [128, 64, 16, 8, 1],
    [1025, 129, 64, 17, 9], [1024, 512, 128, 64, 8],
]
TARGETS = [
    [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 10],
    [5, 12], [9, 13], [14, 5], [9, 10], [9, 10], [9, 10],
    [5, 12], [9, 10], [14, 5],
]
CLASSES = {
    "S": [0], "A": [1], "B": [3], "Z": [8, 14],
    "X": [2, 4, 5, 6, 7, 9, 10, 11, 12, 13],
}
QUOTIENT = {
    "S": ["A", "X"], "A": ["B", "X"], "B": ["X", "Z"],
    "Z": ["Z", "X"], "X": ["X", "X"],
}


def encode(i, h):
    assert 0 <= i <= 3 and 0 <= h <= 2, (i, h)
    return 1 << (3 * i + h)


def monomial_column(i, h, r, t):
    # z^i b^h times 1+z^2+z^3+bz^3+b^2z^3+b^2z^4.
    shifted = (
        (i, h), (i + 2, h), (i + 3, h),
        (i + 3, h + 1), (i + 3, h + 2), (i + 4, h + 2),
    )
    result = 0
    for j, k in shifted:
        if j % 2 == r and k % 2 == t:
            result ^= encode((j - r) // 2, (k - t) // 2)
    return result


def canonical_basis(generators):
    pivots = {}
    for generator in generators:
        value = generator
        assert 0 <= value < 4096
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    # Eliminate lower pivots from each higher row for unique RREF.
    for pivot in sorted(pivots):
        for other in sorted(pivots):
            if other > pivot and pivots[other] & (1 << pivot):
                pivots[other] ^= pivots[pivot]
    return tuple(pivots[p] for p in sorted(pivots, reverse=True))


def all_vectors(basis):
    values = [0]
    for row in basis:
        values += [x ^ row for x in values]
    assert len(values) == len(set(values)) == 2 ** len(basis)
    return tuple(sorted(values))


columns = {
    f"{r}{t}": [monomial_column(i, h, r, t)
               for i in range(4) for h in range(3)]
    for r in range(2) for t in range(2)
}
assert sum(map(len, columns.values())) == 48
print("checkpoint 1: all 48 columns rebuilt from the six actual K shifts", flush=True)


def apply_column_map(value, digit, parameter_parity):
    matrix = columns[f"{digit}{parameter_parity}"]
    result = 0
    while value:
        bit = value & -value
        result ^= matrix[bit.bit_length() - 1]
        value ^= bit
    return result


states = [canonical_basis(b) for b in BASES]
vectors = [all_vectors(b) for b in states]
assert len(set(states)) == len(set(vectors)) == 15
assert states[0] == canonical_basis([encode(0, 0) ^ encode(1, 0) ^ encode(2, 1)])
assert [len(b) for b in states] == [len(b) for b in BASES]
print("checkpoint 2: all 15 distinct full subspaces and initial numerator checked", flush=True)

edges = []
for source in range(15):
    for digit in range(2):
        images = [
            apply_column_map(row, digit, t)
            for row in states[source] for t in range(2)
        ]
        image_basis = canonical_basis(images)
        image_vectors = all_vectors(image_basis)
        target = TARGETS[source][digit]
        assert image_basis == states[target], (source, digit, target)
        assert image_vectors == vectors[target], (source, digit, target)
        # Also map every source vector, not only its basis.
        full_images = [
            apply_column_map(row, digit, t)
            for row in vectors[source] for t in range(2)
        ]
        assert canonical_basis(full_images) == image_basis
        edges.append({
            "source": source, "digit": digit, "target": target,
            "image_generators_from_basis": images,
            "image_rref": image_basis,
            "complete_image_vectors": image_vectors,
            "basis_and_full_vector_checks_agree": True,
        })
assert len(edges) == 30
print("checkpoint 3: all 30 transitions equal the full declared target subspaces", flush=True)

accepting = [
    state for state in range(15)
    if all(value & 7 == 0 for value in vectors[state])
]
assert accepting == [8, 14]
class_of = {}
for name, members in CLASSES.items():
    for state in members:
        assert state not in class_of
        class_of[state] = name
assert set(class_of) == set(range(15))
for state in range(15):
    name = class_of[state]
    assert (state in accepting) == (name == "Z")
    for digit in range(2):
        assert class_of[TARGETS[state][digit]] == QUOTIENT[name][digit]
assert class_of[0] == "S"
print("checkpoint 4: all outputs and quotient edges check; language is 0010*", flush=True)

# These comparisons do not construct any map or state; they check that the
# independently hard-coded candidate data and result agree with frozen inputs.
constructor_dir = HERE.parent / "notes"
certificate_path = constructor_dir / "divisor-reasoning-r2-phi11-certificate-v1.json"
constructor_output = constructor_dir / "divisor-reasoning-r2-phi11-check-output-v1.json"
certificate = json.loads(certificate_path.read_text())
assert certificate["state_bases"] == BASES
assert certificate["transitions"] == TARGETS
assert certificate["denominator"] == [[0, 0], [2, 0], [3, 0], [3, 1], [3, 2], [4, 2]]
assert certificate["numerator"] == [[0, 0], [1, 0], [2, 1]]
prior = json.loads(constructor_output.read_text())
assert prior["operator_columns"] == columns
assert prior["complete_vector_sets"] == [list(row) for row in vectors]
assert prior["accepting_states"] == accepting
print("checkpoint 5: independent columns/vector sets agree with frozen constructor output", flush=True)

result = {
    "status": "passed",
    "method": "six-shift monomial formulas; canonical Gaussian elimination and complete vector sets",
    "operator_columns": columns,
    "state_rref_bases": states,
    "state_dimensions": [len(b) for b in states],
    "complete_vector_sets": vectors,
    "edges": edges,
    "accepting_states": accepting,
    "classes": CLASSES, "quotient_transitions": QUOTIENT,
    "proved_word_language_after_checked_quotient": "0010* least significant bit first",
    "canonical_indices": [4],
    "all_columns": 48, "all_states": 15, "all_transitions": 30,
    "constructor_certificate_sha256": hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
    "constructor_output_sha256": hashlib.sha256(constructor_output.read_bytes()).hexdigest(),
    "larger_graph_search": False, "index_or_word_scan": False, "CAS": False,
}
with OUT.open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "passed", "columns": 48, "states": 15, "edges": 30}), flush=True)
