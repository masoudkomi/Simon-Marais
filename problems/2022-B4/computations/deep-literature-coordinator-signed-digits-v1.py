#!/usr/bin/env python3
"""Exact finite checks for an unverified rational-base coding lead.

This is not a search for, or proof against, infinite equality avoidance.
All operations use Python integer arithmetic. No third-party dependencies.
"""
from collections import Counter
from fractions import Fraction
import json


def canonical(n):
    """Most-significant-first 11/10 representation, value digits/10."""
    digits = []
    while n:
        n, a = divmod(10 * n, 11)
        digits.append(a)
    return list(reversed(digits))


def value(word):
    v = Fraction(0)
    for d in word:
        v = (11 * v + d) / 10
    return v


def normalize(word):
    carry, out = 0, []
    for d in reversed(word):
        carry, a = divmod(10 * carry + d, 11)
        out.append(a)
    return carry, list(reversed(out))


def main():
    counts, cases, negative = Counter(), 0, []
    for d in range(-13, 24):
        for r in range(60):
            c = 3 * ((r + d) // 30)
            assert c in (-3, 0, 3, 6)
            for t in range(10):
                s = 6 * t + r + c
                r_next = s % 60
                assert (r + c - r_next) % 6 == 0
                h = (r + c - r_next) // 6
                assert h == 10 * (s // 60) - t
                assert -10 <= h <= 10
                # Two actual quotient representatives per finite state,
                # with positive a,b above the official product boundary.
                for q in (t + 10, t + 30):
                    b, a = 60 * q + r, 60 * q + r + d
                    actual_b_next = b + 3 * (a // 30)
                    actual_a_next = a + 2 * (b // 20)
                    assert actual_b_next % 60 == r_next
                    q_next = actual_b_next // 60
                    assert 10 * q_next == 11 * q + h
                    word = canonical(q) + [h]
                    assert value(word) == q_next
                    carry, output = normalize(word)
                    assert carry == 0 and value(output) == q_next
                    assert output == [0] * (len(output) - len(canonical(q_next))) + canonical(q_next)
                    assert actual_a_next - actual_b_next == d + 2 * (r // 20) - c
                cases += 1
                counts[h] += 1
                if h < 0 and len(negative) < 4:
                    negative.append({'d': d, 'r': r, 't': t, 'h': h})
    states, todo, transitions = {0}, [0], []
    while todo:
        z = todo.pop()
        for digit in range(-10, 11):
            z_next, a = divmod(10 * z + digit, 11)
            assert -10 <= z_next <= 0 and 0 <= a <= 10
            assert 10 * z + digit == 11 * z_next + a
            transitions.append([z, digit, a, z_next])
            if z_next not in states:
                states.add(z_next)
                todo.append(z_next)
    assert states == set(range(-10, 1))
    # Multi-step checks are exact finite examples, never an infinite claim.
    examples = []
    for a, b in ((599, 600), (601, 600), (25, 24), (1000001, 1000000)):
        initial, word, q0 = [a, b], canonical(b // 60), b // 60
        for step in range(40):
            d, q, r = a - b, b // 60, b % 60
            c = 3 * ((r + d) // 30)
            an, bn = a + 2 * (b // 20), b + 3 * (a // 30)
            h = (r + c - bn % 60) // 6
            word.append(h)
            assert 10 * (bn // 60) == 11 * q + h
            assert value(word) == bn // 60
            carry, output = normalize(word)
            assert carry == 0 and value(output) == bn // 60
            a, b = an, bn
        examples.append({'initial': initial, 'initial_quotient': q0,
                         'steps': 40, 'final': [a, b], 'final_quotient': b // 60})
    result = {'status': 'finite evidence for candidate coding; unverified mathematical lead',
              'controller_cases': cases, 'representatives_per_case': 2,
              'h_min': min(counts), 'h_max': max(counts),
              'h_counts': dict(sorted(counts.items())),
              'negative_examples': negative,
              'normalizer_states': sorted(states),
              'normalizer_transitions': sorted(transitions),
              'multi_step_examples': examples,
              'limitations': 'Right normalization of finite words is not a forward causal conjugacy, an automaticity theorem, or proof of universal equality.'}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
