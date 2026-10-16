# Complete 48-state fixed-factor certificate, v1

**Candidate proof - unverified.** Generated 2026-10-16. This is an exact
finite algebraic certificate supporting `zero-automaton-criterion-v1.md`.
A second implementation is not an independent adversarial agent review.

All integers encode F2 vectors. Bit k represents the monomial in row k
of the first table; XOR is vector addition. A listed basis has descending
pivot bits, and every pivot bit is zero in the other rows. The full
subspace consists of all XOR sums of subsets of that basis.

The denominator is K=1+z^2+(b+b^-1)z^3+b^2*z^4. Each operator column
is the encoded numerator C_(r,t)(monomial*K). Both parity residues are
in {0,1}, including for negative b exponents. The bit reading order
for state transitions is least significant first.

| Bit | z exponent | b exponent | L00 column | L01 column | L10 column | L11 column |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | -1 | 0 | 529 | 48 | 0 |
| 1 | 0 | 0 | 1058 | 0 | 0 | 48 |
| 2 | 0 | 1 | 0 | 1058 | 96 | 0 |
| 3 | 0 | 2 | 2116 | 0 | 0 | 96 |
| 4 | 1 | -1 | 768 | 0 | 0 | 529 |
| 5 | 1 | 0 | 0 | 768 | 1058 | 0 |
| 6 | 1 | 1 | 1536 | 0 | 0 | 1058 |
| 7 | 1 | 2 | 0 | 1536 | 2116 | 0 |
| 8 | 2 | -1 | 0 | 8464 | 768 | 0 |
| 9 | 2 | 0 | 16928 | 0 | 0 | 768 |
| 10 | 2 | 1 | 0 | 16928 | 1536 | 0 |
| 11 | 2 | 2 | 33856 | 0 | 0 | 1536 |
| 12 | 3 | -1 | 12288 | 0 | 0 | 8464 |
| 13 | 3 | 0 | 0 | 12288 | 16928 | 0 |
| 14 | 3 | 1 | 24576 | 0 | 0 | 16928 |
| 15 | 3 | 2 | 0 | 24576 | 33856 | 0 |

The initial state is state 0, span(1058)=span(1+z+b*z^2). To compute
the r successor, apply L_(r,0) and L_(r,1) to each listed basis row
and span the resulting vectors. A state accepts exactly when every
basis row has zero bottom four bits, i.e. no z^0 coefficient.

| State | Basis row masks | 0 successor | 1 successor | Accept? | Quotient class |
|---:|---|---:|---:|---|---|
| 0 | 1058 | 1 | 2 | no | S |
| 1 | 16672, 1058 | 3 | 4 | no | X |
| 2 | 530, 48 | 5 | 6 | no | A |
| 3 | 16672, 8480, 1058, 816 | 7 | 8 | no | X |
| 4 | 16386, 1280, 530, 48 | 9 | 10 | no | X |
| 5 | 17666, 768 | 11 | 12 | no | B |
| 6 | 1058, 529, 289 | 13 | 14 | no | X |
| 7 | 16672, 8480, 4384, 1058, 816 | 7 | 15 | no | X |
| 8 | 16386, 1041, 530, 273, 48 | 16 | 10 | no | X |
| 9 | 16656, 8480, 1042, 768 | 17 | 18 | no | X |
| 10 | 16385, 1057, 529, 289, 3 | 19 | 8 | no | X |
| 11 | 16928, 8464, 1810 | 20 | 10 | no | X |
| 12 | 16656, 1280, 768 | 21 | 22 | yes | C |
| 13 | 16672, 8193, 1058, 529 | 23 | 8 | no | X |
| 14 | 1041, 530, 273, 48 | 24 | 25 | no | X |
| 15 | 16386, 8193, 1041, 530, 273, 48 | 26 | 10 | no | X |
| 16 | 16433, 8193, 1042, 545, 289 | 27 | 18 | no | X |
| 17 | 16912, 8464, 4624, 1810, 48 | 20 | 28 | no | X |
| 18 | 16386, 1042, 530, 274, 51 | 29 | 18 | no | X |
| 19 | 16385, 8193, 1058, 529, 289 | 23 | 8 | no | X |
| 20 | 16656, 8480, 4368, 1042, 768 | 17 | 30 | no | X |
| 21 | 16912, 8464, 48 | 31 | 32 | yes | D |
| 22 | 16433, 1280, 768 | 33 | 34 | no | X |
| 23 | 16385, 8193, 4097, 1058, 529, 289 | 23 | 15 | no | X |
| 24 | 16433, 8193, 1331, 768 | 27 | 18 | no | X |
| 25 | 1057, 529, 289, 3 | 13 | 14 | no | X |
| 26 | 16433, 8193, 4145, 1042, 545, 289 | 27 | 30 | no | X |
| 27 | 16912, 8193, 4624, 1539, 273, 48 | 26 | 28 | no | X |
| 28 | 16385, 8193, 1057, 529, 289, 3 | 23 | 8 | no | X |
| 29 | 16912, 8193, 1539, 273, 48 | 26 | 10 | no | X |
| 30 | 16386, 8193, 1042, 530, 274, 51 | 27 | 18 | no | X |
| 31 | 8480, 4368, 768 | 35 | 36 | yes | E |
| 32 | 16672, 1058, 529 | 19 | 8 | no | X |
| 33 | 16912, 8193, 273, 48 | 37 | 38 | no | X |
| 34 | 16433, 1042, 530, 274 | 29 | 18 | no | X |
| 35 | 16928, 8464, 4624 | 39 | 13 | yes | Z |
| 36 | 17666, 8193, 768 | 40 | 12 | no | B |
| 37 | 8193, 4145, 545, 289 | 41 | 42 | no | X |
| 38 | 16385, 1058, 529, 289 | 19 | 8 | no | X |
| 39 | 16656, 8480, 4368, 768 | 43 | 24 | yes | Z |
| 40 | 16928, 8464, 4865, 1810 | 26 | 28 | no | X |
| 41 | 16928, 8193, 4624, 273 | 44 | 19 | no | X |
| 42 | 16656, 8193, 1042, 768 | 45 | 46 | no | X |
| 43 | 16912, 8464, 4624, 48 | 39 | 13 | yes | Z |
| 44 | 16433, 8193, 4145, 545, 289 | 47 | 16 | no | X |
| 45 | 16912, 8464, 4865, 1810, 48 | 26 | 28 | no | X |
| 46 | 16433, 1057, 545, 289 | 33 | 34 | no | X |
| 47 | 16912, 8193, 4624, 273, 48 | 44 | 19 | no | X |

Every row and both outgoing transitions were reconstructed by the
separate full-subspace implementation, which enumerates all vectors
rather than performing Gaussian elimination. Its largest full space
has 64 vectors, including zero. The 48 spaces are distinct and the
graph is transition-closed. The quotient table and its unrestricted
language argument appear in the candidate theorem note.

Input graph SHA256: `ee818f60e68da70ae2f0f7fa84a2c4dec740d10d03908359a271e354a1a0ce4e`.

Verification report SHA256: `49f10bc55de4482968867e5dc86ad78d74563a66f6ac7e8a595d9e074248f78a`.

Renderer source SHA256: `64a1eabc07d9ab4f54b9ce12817b048f9019495645512f675615cccbda9025c3`.
