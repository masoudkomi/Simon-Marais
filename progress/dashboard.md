# Research dashboard

Initial scope: nine official B4 open portions, 2017-2025. **2026 deferred by the user**, not counted as a verified problem. The 2017 problem and general 2018 enumeration are in scope; for 2019-2025, **part (b) only**. Preliminary part (a) and the already known 2018 m=5 case are excluded as research targets. See sources/open-scope-audit.md.

| Year | Owner | Status | Strongest established starting point | Main obstruction | Next approach | Review status |
|---|---|---|---|---|---|---|
| 2017 | checkpoint complete; slot reassigned to 2020 | Initial pass complete; no full solution located | Attributed 2024/2025 bounds 0.2721 < liminf <= limsup < 0.6496; exact finite counts cross-checked | Exact rate(s), even existence remains open in inspected 2025 source | Boundary-preserving patch dynamic program against exact benchmarks | No new candidate |
| 2018 | author checkpoint complete; review_2018_r1 active | General formula found in pre-competition literature; reproduction under audit | Explicit finite binomial sum, Hering-Howard Prop. 3.2 (2014) | Verify full proof and resolve historical open-label discrepancy | Two fresh blind adversarial reviews | Candidate v1.0 unverified; first review active |
| 2019 | initial checkpoint complete; slot reassigned to 2021 | Partial candidates saved, part (b) only | Candidate growth-limit existence and exact rational upper certificate below 1.83761; exact enumeration through length 25 | Determine the exact growth constant; independent proof audits pending | Fresh reconstruction/counterexample reviews, then canonical-context relations | Partial candidate v1 unverified |
| 2020 | owner_2020 | Initial pass running, part (b) only | Newer cyclic prime-power-conjecture restrictions located; n=2 boundary isolated | General cyclic planar difference-set classification | Verify literature, exact equivalence and bounded searches | No candidate |
| 2021 | owner_2021 | Initial pass running, part (b) only | Claimed full proofs located; withdrawal and verification status being audited | Rational Casas-Alvero degree classification; conflicting literature claims | Verify primary proof status and domain distinctions; exact structural checks | No accepted candidate |
| 2022 | unassigned | Inventory verified; present-day status unchecked | Official part (a) gives a bounded difference strip | Whether every admissible orbit reaches equality | Exact residue dynamics, invariants and exhaustive bounded checks | No candidate |
| 2023 | unassigned | Inventory verified; present-day status unchecked | Official positive-r case is a=b | Negative-r, opposite-parity exponents >1 | Quadratic conjugates, binomial identities and exact algebraic checks | No candidate |
| 2024 | unassigned | Inventory verified; present-day status unchecked | Official notes give reducible families and irreducible cases | Full factorization classification over F2 | Verify APN-related literature and exact polynomial factorization | No candidate |
| 2025 | unassigned | Inventory verified; present-day status unchecked | Official part (a) is solved | General Nagell-Ljunggren classification | Verify literature; audit integer domains and exponent indexing | No candidate |

## Coordination

One coordinator plus at most three active owners/reviewers. Workers own isolated year directories. Reviews may replace checkpointed owners. Requested mathematical-worker settings: GPT-6.1 Sol, Max reasoning. The launch interface accepts explicit settings but does not expose independent effective-setting readback; do not describe this as independently verified.

## Integration log

- Repository verified as the newly created, empty `masoudkomi/Simon-Marais` repository, including its browser clone URL and successful remote reference query. Workspace initially had no remote, commits, or unrelated files.
- Created research branch `codex/smmc-b4-research`. No default-branch merge or force push is authorized.
- Verified official source inventory using two bounded setup helpers. They did not solve problems. Initial source notes distinguish as-issued openness from present-day literature status.
