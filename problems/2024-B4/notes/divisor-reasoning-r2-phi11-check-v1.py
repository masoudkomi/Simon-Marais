"""Verify the finite symbolic phi11 certificate. No coefficient scan or CAS."""

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "divisor-reasoning-r2-phi11-certificate-v1.json"
OUT = HERE / "divisor-reasoning-r2-phi11-check-output-v1.json"
certificate = json.loads(CERT.read_text())
monomials = [(i, h) for i in range(4) for h in range(3)]
index = {term: k for k, term in enumerate(monomials)}
denominator = set(map(tuple, certificate["denominator"]))


def support(vector):
    return {term for k, term in enumerate(monomials) if vector & (1 << k)}


def encode(terms):
    result = 0
    for term in terms:
        if term not in index:
            raise AssertionError(f"Operator left the declared vector space: {term}")
        result ^= 1 << index[term]
    return result


def multiply(left, right):
    result = set()
    for i, h in left:
        for j, k in right:
            term = (i + j, h + k)
            if term in result:
                result.remove(term)
            else:
                result.add(term)
    return result


def section(vector, r, t):
    product = multiply(support(vector), denominator)
    selected = {
        ((i - r) // 2, (h - t) // 2)
        for i, h in product if i % 2 == r and h % 2 == t
    }
    return encode(selected)


def span(generators):
    vectors = {0}
    for generator in generators:
        vectors |= {vector ^ generator for vector in tuple(vectors)}
    return frozenset(vectors)


states = [span(basis) for basis in certificate["state_bases"]]
assert len(states) == 15 and len(set(states)) == 15
assert states[certificate["initial_state"]] == span([encode(set(map(tuple, certificate["numerator"])))])
columns = {
    f"{r}{t}": [section(1 << k, r, t) for k in range(12)]
    for r in (0, 1) for t in (0, 1)
}
print("All 48 operator columns rebuilt from polynomial supports", flush=True)

for state_id, state in enumerate(states):
    for r in (0, 1):
        images = [section(vector, r, t) for vector in state for t in (0, 1)]
        wanted = states[certificate["transitions"][state_id][r]]
        assert span(images) == wanted, (state_id, r)
accepting = [i for i, state in enumerate(states) if all(vector & 7 == 0 for vector in state)]
assert accepting == certificate["accepting_states"]
print("All 30 transitions and all constant-coefficient outputs verified", flush=True)

class_of = {}
for name, members in certificate["classes"].items():
    for member in members:
        assert member not in class_of
        class_of[member] = name
assert set(class_of) == set(range(15))
for state_id in range(15):
    name = class_of[state_id]
    assert (state_id in accepting) == (name in certificate["accepting_classes"])
    for r in (0, 1):
        assert class_of[certificate["transitions"][state_id][r]] == certificate["class_transitions"][name][r]

# A direct equality of finite state machines, not a bounded word sample.
language_machine = {
    "S": ("A", "X"),
    "A": ("B", "X"),
    "B": ("X", "Z"),
    "Z": ("Z", "X"),
    "X": ("X", "X"),
}
assert {name: tuple(edges) for name, edges in certificate["class_transitions"].items()} == language_machine
assert certificate["accepting_classes"] == ["Z"]
assert class_of[certificate["initial_state"]] == "S"
print("The quotient machine is exactly S--0-->A--0-->B--1-->Z, with only zero suffixes", flush=True)

output = {
    "certificate_sha256": hashlib.sha256(CERT.read_bytes()).hexdigest(),
    "operator_columns": columns,
    "states": len(states),
    "transitions_checked": 30,
    "state_dimensions": [(len(state).bit_length() - 1) for state in states],
    "complete_vector_sets": [sorted(state) for state in states],
    "accepting_states": accepting,
    "closed_graph_verified": True,
    "quotient_language_verified": "0010* least-significant-bit first; canonical index 4 only",
    "index_scan_performed": False,
    "enumeration_search_or_CAS": False,
    "role": "Exact finite certificate for the general Cartier invariant, not a claim from numerical tests",
}
with OUT.open("x", encoding="utf-8") as stream:
    json.dump(output, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "passed", "states": 15, "edges": 30, "index_scan": False}), flush=True)
