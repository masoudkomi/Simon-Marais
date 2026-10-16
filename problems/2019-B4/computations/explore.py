#!/usr/bin/env python3
"""Reproduce bounded first-pass observations, not unrestricted proofs."""
from itertools import product
import json


def context(history):
    left = right = ""
    for i, letter in enumerate(history):
        bit = str(i % 2)
        if letter == "L":
            left = bit + left
        else:
            right += bit
    return left, right


def left_greedy(word):
    steps = [word]
    while len(word) > 1:
        expected = str(len(word) % 2)
        if word[0] == expected:
            word = word[1:]
        elif word[-1] == expected:
            word = word[:-1]
        else:
            return False, steps
        steps.append(word)
    return word == "1", steps


seen, collisions = {}, []
for choices in product("LR", repeat=12):
    h = "".join(choices)
    if "RRLL" in h:
        continue
    pair = context(h)
    if pair in seen:
        collisions.append({"smaller": seen[pair], "larger": h,
                           "left": pair[0], "right": pair[1]})
    else:
        seen[pair] = h

words = {"1"}
greedy_counterexample = None
for n in range(1, 6):
    if n == 5:
        greedy_counterexample = next(w for w in sorted(words)
                                     if not left_greedy(w)[0])
        break
    bit = str(1 - n % 2)
    words = {bit + w for w in words} | {w + bit for w in words}

print(json.dumps({"status": "bounded computational evidence only",
                  "first_extra_collision_search_moves": 12,
                  "RRLL_avoiding_context_collisions": collisions,
                  "left_greedy_counterexample_in_B5": greedy_counterexample,
                  "failed_greedy_trace": left_greedy(greedy_counterexample),
                  "successful_deletion_trace": ["11001", "1100", "110", "10", "1"],
                  "balanced_count_counterexample": "1001",
                  "plain_concatenation_counterexample": ["10", "01", "1001"]},
                 indent=2))
