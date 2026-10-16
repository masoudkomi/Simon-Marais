#!/usr/bin/env python3
"""Exact finite certificate for the candidate 2019 B4(b) upper bound.

The integer inequalities, not the floating-point eigenvalue, certify the matrix
bound. Mathematical justification of its applicability is in ../proof.md.
"""
import json

FORBIDDEN = ["RRLL", "RRLRRLRLLRLL"]
WEIGHTS = [1000000000000, 837605905420, 539189558215, 451628358102,
           829914937903, 525056590887, 425657533878, 782190797941,
           912301838575, 838845340670, 541467151750, 455813677432]
Q_NUMERATOR, Q_DENOMINATOR = 183761, 100000


def context(history, first_bit=0):
    left = right = ""
    for i, move in enumerate(history):
        bit = str(first_bit ^ (i % 2))
        if move == "L":
            left = bit + left
        else:
            right += bit
    return left, right


def main():
    replacements = [("RRLL", "LLRR"),
                    ("RRLRRLRLLRLL", "LLRLLRLRRLRR")]
    for larger, smaller in replacements:
        assert len(larger) == len(smaller) and smaller < larger
        for first_bit in (0, 1):
            assert context(larger, first_bit) == context(smaller, first_bit)
    states = sorted({f[:i] for f in FORBIDDEN for i in range(len(f))},
                    key=lambda s: (len(s), s))
    index = {s: i for i, s in enumerate(states)}
    matrix = [[0] * len(states) for _ in states]
    transitions = []
    for i, state in enumerate(states):
        row = {}
        for letter in "LR":
            word = state + letter
            if any(word.endswith(f) for f in FORBIDDEN):
                row[letter] = None
                continue
            target = max((s for s in states if word.endswith(s)), key=len)
            matrix[i][index[target]] += 1
            row[letter] = target
        transitions.append(row)
    assert len(WEIGHTS) == len(states)
    slacks = []
    for row, weight in zip(matrix, WEIGHTS):
        av = sum(entry * v for entry, v in zip(row, WEIGHTS))
        slack = Q_NUMERATOR * weight - Q_DENOMINATOR * av
        assert weight > 0 and slack > 0
        slacks.append(slack)
    v = [1.0] * len(states)
    for _ in range(300):
        u = [sum(entry * x for entry, x in zip(row, v)) for row in matrix]
        ratios = [a / b for a, b in zip(u, v)]
        v = [x / max(u) for x in u]
    print(json.dumps({"status": "candidate proof - unverified; exact finite certificate",
                      "forbidden": FORBIDDEN,
                      "equal_context_12_move_relation": {
                          h: context(h) for h in replacements[1]},
                      "states": states, "transitions": transitions,
                      "matrix": matrix, "positive_integer_weights": WEIGHTS,
                      "q_numerator": Q_NUMERATOR, "q_denominator": Q_DENOMINATOR,
                      "strict_integer_slacks": slacks,
                      "numerical_eigenvalue_evidence_only": [min(ratios), max(ratios)]},
                     indent=2))


if __name__ == "__main__":
    main()
