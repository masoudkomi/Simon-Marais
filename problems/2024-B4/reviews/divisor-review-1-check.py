"""Independent exact certificate reconstruction, not an index scan.

Polynomial arithmetic uses exponent-pair supports. Constructor code and
operator columns are neither imported nor read. Static certificate data
are proof inputs and are checked against the actual numerator/denominator.
"""
from pathlib import Path
import json
import hashlib

BASE = Path(__file__).with_name("divisor-review-1")
CERT = Path(str(BASE) + "-certificate-input.json")
OUT = Path(str(BASE) + "-check-output.json")
data = json.loads(CERT.read_text())
K = frozenset({(0, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2)})
N0 = frozenset({(0, 0), (1, 0), (2, 1)})
assert frozenset(map(tuple, data["denominator"])) == K
assert frozenset(map(tuple, data["numerator"])) == N0


def decode(number):
    assert isinstance(number, int) and 0 <= number < (1 << 12)
    return frozenset((i, h) for i in range(4) for h in range(3)
                     if number & (1 << (3 * i + h)))


def encode(poly):
    assert all(0 <= i <= 3 and 0 <= h <= 2 for i, h in poly)
    return sum(1 << (3 * i + h) for i, h in poly)


def multiply(left, right):
    answer = set()
    for a, b in left:
        for c, d in right:
            exponent = (a + c, b + d)
            if exponent in answer:
                answer.remove(exponent)
            else:
                answer.add(exponent)
    return frozenset(answer)


def section(poly, r, t):
    product = multiply(poly, K)
    answer = frozenset(((i - r) // 2, (h - t) // 2)
                       for i, h in product if i % 2 == r and h % 2 == t)
    encode(answer)  # Independently check closure in the claimed 12 monomials.
    return answer


def span(polys):
    vectors = {frozenset()}
    for poly in polys:
        vectors |= {old ^ poly for old in vectors}
    return frozenset(vectors)


columns = []
for r in range(2):
    for t in range(2):
        for i in range(4):
            for h in range(3):
                image = section(frozenset({(i, h)}), r, t)
                columns.append({"r": r, "t": t, "input": [i, h],
                                "output_support": sorted(image),
                                "output_encoded": encode(image)})
assert len(columns) == 48
print(json.dumps({"checkpoint": "all_operator_columns", "count": 48}), flush=True)

bases = [[decode(n) for n in row] for row in data["state_bases"]]
spaces = [span(basis) for basis in bases]
assert len(spaces) == 15 and len(set(spaces)) == 15
assert spaces[data["initial_state"]] == span([N0])
state_records = []
for index, (basis, vectors) in enumerate(zip(bases, spaces)):
    assert len(vectors) == 2 ** len(basis), ("dependent basis", index)
    accepts = all(not any(i == 0 for i, h in poly) for poly in vectors)
    assert accepts == (index in data["accepting_states"]), index
    state_records.append({"state": index, "dimension": len(basis),
                          "vectors": sorted(map(encode, vectors)),
                          "accept": accepts})
    print(json.dumps({"checkpoint": "full_subspace", "state": index,
                      "dimension": len(basis), "vector_count": len(vectors),
                      "accept": accepts}), flush=True)

edge_records = []
for index, vectors in enumerate(spaces):
    for r in range(2):
        images = [section(poly, r, t) for poly in vectors for t in range(2)]
        generated = span(images)
        target = data["transitions"][index][r]
        assert generated == spaces[target], (index, r, target)
        # Cross-check that images of a basis generate the same entire space.
        basis_generated = span(section(poly, r, t)
                               for poly in bases[index] for t in range(2))
        assert basis_generated == generated
        edge_records.append({"source": index, "digit": r, "target": target,
                             "entire_image_space": sorted(map(encode, generated)),
                             "equality_verified": True})
assert len(edge_records) == 30
print(json.dumps({"checkpoint": "all_transition_equalities", "count": 30}), flush=True)

classes = data["classes"]
assert sum(map(len, classes.values())) == 15
membership = {}
for name, members in classes.items():
    for index in members:
        assert index not in membership
        membership[index] = name
assert set(membership) == set(range(15))
quotient = []
for name, members in classes.items():
    outputs = {state_records[index]["accept"] for index in members}
    assert len(outputs) == 1
    result = outputs.pop()
    assert result == (name in data["accepting_classes"])
    targets = []
    for r in range(2):
        names = {membership[data["transitions"][index][r]] for index in members}
        assert names == {data["class_transitions"][name][r]}
        targets.append(names.pop())
    quotient.append({"class": name, "members": members,
                     "transitions": targets, "accept": result})

reachable = {data["initial_state"]: ""}
while True:
    extra = {}
    for source, word in list(reachable.items()):
        for r, target in enumerate(data["transitions"][source]):
            if target not in reachable and target not in extra:
                extra[target] = word + str(r)
    if not extra:
        break
    reachable.update(extra)
assert set(reachable) == set(range(15))
print(json.dumps({"checkpoint": "quotient_and_reachability", "classes": 5,
                  "reachable_states": 15}), flush=True)

result = {"status": "all exact finite-certificate checks passed",
          "method": "independent exponent-support polynomial arithmetic; complete subspaces",
          "input_sha256": hashlib.sha256(CERT.read_bytes()).hexdigest(),
          "denominator": sorted(K), "numerator": sorted(N0),
          "encoding": "bit 3*i+h is z^i*b^h, i0..3,h0..2",
          "operator_columns": columns, "states": state_records,
          "transitions": edge_records, "quotient": quotient,
          "reachability_witnesses_LSB_first": reachable,
          "no_index_scan_or_CAS": True}
with OUT.open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({"checkpoint": "completed", "states": 15, "columns": 48,
                  "transitions": 30, "all_full_spaces_verified": True}), flush=True)
