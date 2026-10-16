#!/usr/bin/env python3
"""Finite quotient graph for B4(b), explicitly not an orbit-lift proof."""
import collections
import hashlib
import json
import sys


def successors(d, r):
    # b=60*q+r, a=b+d; e=q mod 10. Floors may use r+d<0,
    # but all such residue states have sufficiently large positive lifts.
    c = 3 * ((r + d) // 30)
    dn = d + 2 * (r // 20) - c
    return [(dn, (6 * e + r + c) % 60) for e in range(10)]


def components(graph):
    sys.setrecursionlimit(20000)
    clock = 0
    index, low, stack, active, output = {}, {}, [], set(), []

    def visit(v):
        nonlocal clock
        index[v] = low[v] = clock
        clock += 1
        stack.append(v)
        active.add(v)
        for w in graph[v]:
            if w not in index:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in active:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                active.remove(w)
                comp.append(w)
                if w == v:
                    break
            output.append(comp)

    for v in graph:
        if v not in index:
            visit(v)
    return output


def main():
    states = [(d, r) for d in range(-13, 24) for r in range(60)]
    state_set = set(states)
    all_graph = {v: successors(*v) for v in states}
    outside = [(v, w) for v in states for w in all_graph[v] if w not in state_set]
    safe = {v for v in states if v[0] != 0}
    graph = {v: [w for w in all_graph[v] if w in safe] for v in sorted(safe)}
    comps = components(graph)
    cyclic = [c for c in comps if len(c) > 1 or c[0] in graph[c[0]]]
    # Repeatedly delete vertices with no remaining successor. The remaining
    # states have arbitrarily long abstract walks avoiding d=0.
    survivors = set(safe)
    pruning = []
    while True:
        dead = {v for v in survivors if not any(w in survivors for w in graph[v])}
        if not dead:
            break
        pruning.append(len(dead))
        survivors -= dead
    edges = [(v, e, w) for v in states for e, w in enumerate(all_graph[v])]
    digest = hashlib.sha256(repr(edges).encode()).hexdigest()
    # Breadth-first distances are finite graph evidence, not an integer-orbit proof.
    reverse = {v: [] for v in states}
    for v in states:
        for w in all_graph[v]:
            reverse[w].append(v)
    distances = {v: 0 for v in states if v[0] == 0}
    queue = collections.deque(distances)
    while queue:
        v = queue.popleft()
        for u in reverse[v]:
            if u not in distances:
                distances[u] = distances[v] + 1
                queue.append(u)
    # Check the analytic sign-based policy from proof.md, without using it to
    # promote the candidate partial theorem.
    policy_maximum = 0
    for v0 in states:
        v = v0
        n = 0
        while v[0] != 0:
            dn = successors(*v)[0][0]
            if dn == 0:
                n += 1
                break
            target = range(30, 36) if dn > 0 else range(20, 26)
            choices = [w for w in successors(*v) if w[1] in target]
            assert len(choices) == 1
            v = choices[0]
            n += 1
            assert n <= 24
        policy_maximum = max(policy_maximum, n)
    # Verify the explicit finite-delay formula on a modest grid, with exact ints.
    delay_checks = 0
    for length in range(1, 41):
        for t in (1, 2, 7):
            for r in range(20):
                b = 60 * 10**length * t + r
                a = b + 1
                for n in range(length + 1):
                    common = 60 * 11**n * 10**(length - n) * t
                    assert (a, b) == (common + r + 1, common + r)
                    assert a != b and a * b >= 600
                    if n < length:
                        a, b = a + 2 * (b // 20), b + 3 * (a // 30)
                delay_checks += 1
    print(json.dumps({
        "meaning": "finite exact graph calculation; infinite integer lift unresolved",
        "state": "(d=a-b, r=b mod60)", "d_interval": [-13, 23],
        "number_states": len(states), "number_edges_with_controls": len(edges),
        "transitions_leaving_interval": outside,
        "avoiding_vertices": len(safe), "avoiding_edges": sum(map(len, graph.values())),
        "scc_size_histogram": dict(sorted(collections.Counter(map(len, comps)).items())),
        "number_cyclic_sccs": len(cyclic),
        "largest_cyclic_scc_size": max(map(len, cyclic), default=0),
        "pruning_round_sizes": pruning,
        "arbitrarily_long_abstract_avoidance_vertices": len(survivors),
        "self_loop_example": {"state": [1, 0], "control_e": 0,
                              "successor": successors(1, 0)[0]},
        "ordered_edge_sha256": digest,
        "states_with_abstract_hitting_path": len(distances),
        "shortest_abstract_hitting_path_maximum": max(distances.values()),
        "abstract_hitting_distance_histogram": dict(sorted(collections.Counter(distances.values()).items())),
        "analytic_policy_verified_states": len(states),
        "analytic_policy_observed_maximum": policy_maximum,
        "finite_delay_formula_checks": delay_checks,
        "caution": "Graph cycles do not establish an infinite positive integer orbit."
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
