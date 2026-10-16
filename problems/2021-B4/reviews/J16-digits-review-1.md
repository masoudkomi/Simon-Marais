# Independent adversarial review R1: complete rational J16 L1--L4 packet

2026-10-16 UTC. **Initial blind review complete.** Recommendation:
accept L1--L4 as a partial rational-witness J16 exclusion, conditional
on the expressly accepted normalization, Newton/width-one, T1--T2 and
88-mask inputs. I found no unresolved substantive objection and request
no mathematical repair. This is one independent audit; promotion remains
the coordinator's decision after the second independent audit.

This does not establish the degree-20 case or classify B4(b). Its final
consequence removes the 88 J16 masks from the previously accepted
772-mask necessary cover, leaving 684 masks in other J classes.

## Reviewed scope, frozen inputs and independence

The initial assignment was the whole joint L1--L3 candidate, including
the earlier leading argument as unverified argument rather than an
accepted lemma. Before this initial report was frozen, the coordinator
extended it to the whole L1--L4 candidate and both author continuation
packets. Only 2021 B4(b) was investigated. No preliminary part (a), other
contest problem, or full annual classification was used as a substitute.

The exact candidate note hashes are:

| Packet | SHA-256 |
|---|---|
| Joint L1--L3 | `2fa8c3ad1ccea46350c7d8ae76d9463b332e2be636e48f48dbcbff7cad85c801` |
| Incorporated leading argument | `d8ad259a3084635d5f3b66e1aaf6fe611c6a118b47dfd16578d0e2958bde3fce` |
| Owner uniform-E/v1 continuation | `990661fa1cb7c173efa406437d6c9481edf80861a64609a73ec4f5b077c5b9dc` |
| Owner v2 final exclusion | `e4a9fcb1ee37c97b62ae389ce180b4644e751d4aee9e037f5a962fc6338d96e7` |

All 46 artifact records in the joint manifest, all 53 in owner v1 and
all 14 in owner v2 match their frozen sizes and SHA-256 hashes. The
older leading manifest's 12 entries also match. These are integrity
checks, supplemented by the complete mathematical and finite audit below.

I did not construct these candidates, read reviewer-2 material, receive
peer conclusions, import constructor helpers, edit candidate mathematics,
or communicate conclusions to a peer. I first read the frozen mathematical
notes and accepted input proof packets, then saved my own derivation and
full modular recursion/direct-division code before opening constructor
source, results or serialization. The first executable source snapshot
has hash `b53811a0f4a7c30c5492e662a9e496e3ba6263a36eb6c0138c7f6141fbd2ac8d`.

After extension, the arbitrary-precision evaluator and derivation were
likewise saved before opening any owner code, manifest or data. The
precomparison evaluator snapshot has hash
`1b9740ec4f47d90e30f4a3f6e299993617df1dd98cd90145390081aec971e5a8`.
One missing pair of parentheses in an assertion was corrected before its
first execution; no formula changed. The original text snapshot is
preserved. Later changes to the first verifier add serialization adapters,
statistics and a second linear-algebra check; its first source and both
benchmark source versions are preserved separately.

Requested settings were gpt-6.1-sol/max, inherited through the launch;
effective-setting readback is unavailable. No claim of verified effective
settings is made. The review uses Python 3.12.14 and its standard library.

## Reconstruction of L1 and the first finite cover

Accepted T2 supplies the complete rational root set {0,1,u,v}, with 0
double, 1 simple, u,v distinct nonzero rational roots of positive integral
19-adic valuation, and monic rational degree-15 Eisenstein quotient g.
Set B=(Z-1)g. Then v(b0)=1 and v(b1),v(b2)>=1. Direct expansion gives
c2=b0uv, c3=-b0(u+v)+b1uv, c4=b0-b1(u+v)+b2uv.
Thus v(c4)=1 and the proposed normalized root-sum identity follows.
This uses the exact rational quotient, not an unsupported rationality
assertion about a general Newton factor.

For r=v(u)<s=v(v), the c3 term -b0u has strictly smaller valuation than
the other terms. The small Newton edges have endpoints (2,1+r+s),
(3,1+r),(4,1), each with exactly its two endpoints on the supporting
line. The accepted width-one lemma applies at lower exponents 2 and 3,
both below 19. Neither small root can witness H2 or H3. Neither can 0,
since c2,c3 are nonzero. Both derivatives must therefore use 1. The
argument is symmetric under swapping u,v.

With equal valuations nu, integral rescaling reduces to
T^4-(U+V)T^3+UVT^2. Its H3 values at 0,U,V are
-(U+V),3U-V,3V-U. Its H2 values at U,V are
U(3U-2V),V(3V-2U), while H2(0)=UV is nonzero. This proves every
sole-center ratio. H3's possible zero witness is retained, and equal
leading residues are never discarded by an inequality test.

I independently enumerated all 2^17 binary masks using normalized
derivative recursion, the divided center-root congruence, J16 and the
accepted H2/H3 disjunction. The resulting 88 masks equal the accepted
raw list. For every mask I computed exact a_j(0,0) and q0. All q0
are nonzero: 84 have valuation one, four valuation two. Hence no higher
minimum valuation is omitted. Linear coefficients follow from the exact
recursion; noncenter positions are active precisely when a_(j-1)^0 is
a unit modulo 19. The canonical-center rule justifies the sole-center
contrapositive for an actual counterexample. Extra formal families can
only enlarge this necessary cover.

The independent leading traversal checks 11886 label/nu combinations
before constant prerequisites and 11559 afterward, testing the complete
19-by-19 residue grid at every eligible branch. It reconstructs all 88
result rows, all saved first examples and equations, all 768 branch-index
records, and their complete order. The 18 leading exclusions and all 70
retained masks match. There are 756 passing projected branches at nu=1
and 12 at nu=2. Restoring every inactive ternary label gives exactly
840396 unique full keys, with no unused-label pruning at this stage.

Neither zero leading residues nor equal residues were removed in
both-center cases. In fact no such pair survives the leading equations;
that is an output of the complete grid check. Missing u or v labels
are still present in 14248 full assignments, including 20 missing both.

## Uniform integral equations, L3 and arbitrary subsequent digits

For a fixed complete assignment the triangular derivative equations
force integer polynomials a_j(u,v) without division. With q=19^nu,
u=qX,v=qY, divide f/Z^2 by the monic quadratic Z^2-(u+v)Z+uv.
An actual distinct-root pair makes both remainders R0,R1 zero. This
division is defined even at coincident finite residues; no u-v denominator
is introduced.

The independently reconstructed vector is

    E=(Ptilde/q, R0/(19*q*10), R1/(19*q)).

The checked q divisibility of q0,a17^0,a18^0 makes its low terms
integral over Z_(19). All other middle coefficients have an explicit
factor 19, and quadratic-remainder homogeneity supplies enough q powers.
The two exceptional top coefficients occur at parameter degrees at least
17 in R0 and 16 in R1, also more than sufficient. The denominator 10
is a 19-adic unit. The precise derivation is preserved in the two
independent derivation files.

Modulo 19 every degree-at-least-two term has a factor 19. The Jacobian
is therefore the stated constant matrix: sum beta*A in the first row,
A18,B18 in the second, and beta17*A17+C4,beta17*B17+C4 in the third.
Inactive labels do not affect that matrix, though their higher terms
are restored and used in every scalar evaluation.

At an input satisfying E=0 modulo 19^k, Taylor expansion gives the
entire next fiber M*d=-E/19^k modulo 19. The discarded change terms
have valuation at least 2k>=k+1. This holds for rank zero, one or two,
and requires no unique lift or nonsingularity. My solver uses Cramer's
rule or a free coordinate, checked separately against RREF. All solutions,
including all 19 rank-one children, are retained.

My scalar route differs from the constructor shortcuts: it computes
every term's actual modular coefficient in the full normalized recurrence,
builds all ordinary coefficients of f/Z^2, includes c19=-20,c20=1,
and performs full monic long division. At precision k the coefficient
modulus is 19^(nu+k+1) and the remainder modulus 19^(nu+k+2). Checked
exact division by q or 19q then determines E modulo 19^(k+1); the
remaining factor 10 is inverted at that modulus. This precision argument
avoids any silent integer-floor division or loss of a carry.

For L3 specifically, this independently includes the nu=1 correction
-t*c4 to R0 and (s^2-t)*c5 to R1, while their stated nu=2 disappearance
is justified by valuation. Every one of the 840396 prior records matches
the independently computed constants, rank and consistency. There are
no missing or duplicate keys. All 15 gzip chunks, their row counts and
both hashes match:

- Row stream: `b0ab2fd44f64015b0ae1caa954c3dad76be44c02833cec62d79c2df6c1f3dacb`.
- Scalar binding stream: `dfe2ca43528f5e55c68a642f61838343b0a09bc6690afe153643c04ff574e49f`.

The 125346 consistent parents comprise 112222 rank-two and 13124
rank-one cases. The twelve additional exclusions and full 58-mask list
match exactly. These facts establish the finite L3 substage; the later
uniform-E audit independently reevaluates this stage and does not take
the old L3 scalar formulas as an axiom.

## Full tree and L4 consequence

T1 validly prunes a full assignment with an unused u or v label:
H1 is already witnessed by 0 and H19 by 1, so three rational roots
would cover every derivative. This is unrelated to root closeness or
to whether the unused formal variable is still required to be a root.
The first lifting level evaluates every assignment before applying this
pruning, preserving the complete old-stream comparison.

I independently generated the expected initial full-key set, checked
every input exactly once, generated its complete unpruned digit fiber,
and compared every next node stream to that independently generated set.
All coefficient residues, moduli, E residues, matrices, ranks, RREF rows,
pruning decisions and complete digit lists match at every level.

| Input precision | Inputs independently checked | Next precision | Complete next layer |
|---:|---:|---:|---:|
| 1 | 840396 | 2 | 361194 |
| 2 | 361194 | 3 | 2026 |
| 3 | 2026 | 4 | 90 |
| 4 | 90 | 5 | 14 |
| 5 | 14 | 6 | 0 |

At the first level, T1 prunes 14248 assignments, of which 384 had
consistent rank-two systems. The remaining children are exactly
111838+19*13124=361194. At precision two all 249356 rank-one inputs
are inconsistent; 109812 rank-two inputs fail and 2026 pass. At the
next level 1936 fail and 90 pass. Swap closure is checked for every
saved v1 output layer.

All 90 precision-four states are independently rebuilt with untruncated
integer recurrence and exact integer monic division. Every integer a_j,
ordinary F coefficient, remainder, exact Fraction, matrix and minor
matches the author post-check. Every matrix has rank two. Since it is
constant through the family, at most one child arises at any later
precision, proving the structural bound of 90 per future layer.

All 104 final systems are also rebuilt exactly. I compare every exact
integer coefficient and Fraction, and brute-force all 361 digit pairs
for each of these systems. The signed-minor left-kernel vectors are
nonzero, annihilate both columns, and their dot products with the
constant vectors match all saved obstructions. At precision four there
are 76 nonzero obstructions and 14 zero obstructions; at precision five
all 14 are nonzero. Their exact chain is 90 -> 14 -> 0.

Every exact rational counterexample would give a path through each
finite layer because its roots make E exactly zero. The empty
precision-six layer therefore contradicts its existence in J16. No
infinite lifting, convergence argument, height bound, finite root
separation, unproved general p-adic three-root theorem, or all-roots-
rational assumption is used.

## Reproducibility, budget and limits

All commands, source hashes, child PIDs, external timeouts, exit codes,
stdout checkpoints and output hashes are saved under the assigned R1
prefix. The principal full L3 run used child 51599, finished in 49.436
supervisor seconds under 300 seconds, and was reaped. The complete
general-tree run used child 52973, finished in 53.541 supervisor seconds
under 300 seconds, and was reaped. Its exact worker time was 53.426
seconds. Both followed bounded 8192-case benchmarks under 30 seconds.
No timeout, cap increase, CAS, dependency install, global kill, billed
API, paper redistribution, shared-source edit, commit or push occurred.

The complete tree audit independently checks 1203720 input records,
plus all node streams, all 90 exact post-check states and all 12 author
self-test cases. It also verifies that both owner benchmarks are exact
prefixes of the complete verified traversal. Benchmarks remain incomplete
and contribute no exclusions. The initial R1 benchmark's provisional
per-mask fields likewise carry no exclusion inference.

Authoritative account-wide weekly telemetry was available throughout:
12% total used with reset 1792745187 at the latest checks, below the
90% total-used threshold with review/integration reserve intact.

The issue log records every main adversarial challenge and its resolution.
The final R1 manifest freezes this report, code, derivations, exact results,
commands, outputs, version snapshots and issue log before any peer
conclusions are read. There are no unresolved substantive issues. The
coordinator must still apply the required independent-review gate; this
report alone does not promote the candidate.
