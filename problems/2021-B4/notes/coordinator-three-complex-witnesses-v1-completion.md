# Complement certificate completion for proposed C20

2026-10-16 UTC. **Candidate proof - unverified.** Construction only;
two independent full extension audits are still required. See the complete
[coverage proof](coordinator-three-complex-witnesses-v1.md).

The additional 5,908 center masks give 4,731,928 families. The 900-second
supervised run completed in 600.386 seconds, child PID 37199, exit 0,
reaped, with 8,192-family checkpoints. It created 79 deterministic gzip
chunks, 78 of 60,000 rows and one of 51,928 rows, 28,442,028 bytes total.
The original 772-mask packet contributes 1,493,024 families, so the
disjoint union covers all 6,224,952 refinements of the 6,680 masks.

| Original complementary certificate | Families |
|---|---:|
| Nonzero constant P | 5908 |
| 101 | 4495784 |
| 103 | 218175 |
| 107 | 11555 |
| 109 | 477 |
| 127 | 26 |
| Initial unresolved sentinel | 3 |

The three initial misses are retained unchanged in the raw stream and
unresolved-pair file. A separate resolver completed in 0.076 seconds,
child PID 43351, under a 20-second timeout, exit 0, reaped. All resolve
at 131 with retained degrees:

| (center_mask,U_mask) | degrees P,Q | leading residues at131 |
|---|---|---|
| (117075,9220) | (15,20) | (83,3) |
| (117075,1548) | (12,20) | (44,79) |
| (117075,9356) | (15,20) | (97,124) |

Thus no complementary family is left unresolved by the combined
constructor records. This is not independent acceptance of the mathematics.
The old 772-mask stream's separate (6436,24785) miss at 131 is also
preserved and required for the complete union.

Complement integer-polynomial stream SHA-256:
`49da0560f41fdf3fce8a1ed7e63e877b5d51533de93142d74be7129d3db04da2`.
Complement uncompressed compact-certificate stream SHA-256:
`e4dee952d410bf709b8c90dd61002ee88c4179a5fe7a8ca0678fe3644a25ffb1`.
The result records every compressed chunk's bytes, rows and hash. The
freeze manifest binds those artifacts, the symbolic proof, exact mask
index, construction provenance, all initial failures and both resolvers.

Main and resolver code explicitly reuse the earlier frozen constructor's
helpers; exact replacements and source hashes are recorded. Reuse supplies
no independent-review credit. Python 3.12.14 and its standard library
suffice; no native CAS, paid API, purchase or full third-party paper is
part of the tracked output. No timeout or global process kill occurred.

Reproduce from the repository root, preserving the frozen originals:

    .venv/bin/python problems/2021-B4/computations/coordinator-three-complex-masks-v1.py
    .venv/bin/python -u problems/2021-B4/computations/coordinator-three-complex-witnesses-v1.py
    .venv/bin/python -u problems/2021-B4/computations/coordinator-three-complex-witnesses-v1-resolve.py

Use a copied checkout for reproduction if exact frozen run metadata must
remain unchanged. Numeric elapsed times in a fresh run will differ.
Independent reviewers must derive the ramified normalization and prime-field
coverage, independently enumerate masks/refinements and check all new
exact polynomial pairs/certificates. The finite old algebraic compatibility
facts may be an explicit accepted dependency; sampling does not suffice.
Novelty is unestablished and no full degree-20 classification is proposed.
