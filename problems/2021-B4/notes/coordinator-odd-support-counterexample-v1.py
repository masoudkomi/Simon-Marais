"""Exact counterexample/intuition probe of one stated 64-support obstruction."""
from itertools import product
from math import comb
from pathlib import Path
import json
import os

prime = 19
optional = (3, 5, 7, 9, 11, 13)
rows = []
print(json.dumps({"checkpoint": "start", "pid": os.getpid(),
                  "supports": 64, "scope": "one necessary residue branch only"}),
      flush=True)
for mask in product((0, 1), repeat=6):
    support = (1,) + tuple(j for bit, j in zip(mask, optional) if bit) + (15,)
    b = [1] + [0] * 15
    for j in range(1, 16):
        if j in support:
            b[j] = -sum(comb(j, k) * b[k] for k in range(j))
    f17 = sum(comb(17, j) * b[j] for j in range(16))
    f20 = sum(comb(20, j) * b[j] for j in range(16))
    fminus2 = sum((-1)**j * (j+1) * b[j] for j in range(16))
    derivative_mod19 = (b[1] - sum(b[j] * pow(j*(j-1), -1, prime)
                                  for j in range(3, 16, 2))) % prime
    assert sum(b[j] * comb(1, j) for j in range(2)) == 0
    assert f20 % prime == 0
    assert f17 % prime == fminus2 % prime
    assert (f20//prime) % prime == derivative_mod19
    valid_support = all(b[j] % prime for j in support)
    rows.append({"mask": list(mask), "support": list(support),
                 "b_integer": b, "all_selected_coefficients_nonzero_mod19": valid_support,
                 "F17_integer": str(f17), "F20_integer": str(f20),
                 "F17_mod19": f17 % prime, "F20_mod361": f20 % (prime**2),
                 "F20_div19_mod19": (f20//prime) % prime,
                 "Fprime1_mod19": derivative_mod19,
                 "both_endpoint_congruences": f17 % prime == 0 and f20 % (prime**2) == 0})
    if len(rows) % 8 == 0:
        print(json.dumps({"checkpoint": "supports inspected", "completed": len(rows)}),
              flush=True)
joint = [r for r in rows if r["both_endpoint_congruences"]]
first = [r for r in rows if r["F17_mod19"] == 0]
result = {"purpose": "counterexample/intuition probe; no unrestricted proof or promotion",
          "scope": "odd supports containing1 and15 only;64 possibilities",
          "prime": prime, "optional_indices": list(optional), "rows": rows,
          "first_endpoint_zero_supports": [r["support"] for r in first],
          "joint_endpoint_supports": [r["support"] for r in joint],
          "joint_endpoint_valid_supports": [r["support"] for r in joint
                                            if r["all_selected_coefficients_nonzero_mod19"]],
          "full_degree20_or_rational_lift_claimed": False,
          "external_dependency_or_CAS": False}
out = Path(__file__).with_suffix(".json")
with out.open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({"checkpoint": "completed", "rows": len(rows),
                  "first_endpoint_zero_supports": result["first_endpoint_zero_supports"],
                  "joint_endpoint_supports": result["joint_endpoint_supports"],
                  "joint_endpoint_valid_supports": result["joint_endpoint_valid_supports"]}),
      flush=True)
