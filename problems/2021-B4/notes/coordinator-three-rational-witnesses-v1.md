# Degree20 cannot be covered by three rational recycled roots

2026-10-16 UTC. **Candidate proof - unverified.** Constructor: coordinator.
Two fresh independent adversarial audits, including complete reconstruction
of every finite certificate, are required. This is a partial necessary
condition, not a solution of degree20 or the full B4(b) classification.
No novelty is claimed.

## Statement

Let f be a degree20 polynomial in Q[x] satisfying the contest's rational
common-root condition for each derivative order1 through19. Suppose f is
not a power of a linear polynomial. Then no set of at most three rational
roots can supply all those common-root witnesses. Equivalently, a
nontrivial rational-witness counterexample in degree20 requires at least
four distinct rational recycled roots.                         (T1)

In the previously specified p=19 normalization, the following additional
consequences are proposed:

- If J=16, zero has multiplicity exactly2, and the complete rational root
  set is {0,1,u,v}, with u,v distinct and nonzero, not1. All four values
  are needed to cover the derivative conditions. The degree15 quotient
  after removing x^2(x-1)(x-u)(x-v) is Eisenstein at19.          (T2)
- If J=15, zero has multiplicity2 or3, rather than4. When its multiplicity
  is3, the rational root set again consists exactly of {0,1,u,v}, and the
  remaining degree14 quotient is Eisenstein at19.             (T3)

The unknown u,v are rational and have positive integral19-adic valuations.
No numerical height bound is placed on any witness.

## Explicit dependencies and attribution

Use the unchanged mathematics in the earlier separately reviewed packets:

1. `rational-witness-p-plus-one-v1.1.md`: normalization of a hypothetical
   nontrivial degree p+1 counterexample to monic f with double root0,
   simple center1, integral a_j and all other roots of positive valuation.
   It checks the rational affine map and the original CLO hypotheses.
2. `padic-rational-newton-obstructions-v1.md`: the long-edge and rational
   root-count restrictions, complete J=18/J=17 exclusions, and J=16
   center disjunction. Its independent audits check all29928 certificates.
3. `coordinator-newton-degeneration-v1.md`: the conditional good-prime
   small-cluster theorem, verified at19 for h<=5 using CLO's published
   degree5 bad-prime list; in particular the J=15 center disjunction.
   Both separate independent audits checked the theorem and all461 records.

These give exactly772 necessary center masks, among all131072 binary
choices, after excluding J=18,J=17 and applying J=16,J=15 disjunctions.
There are615 with J<=14,69 with J=15 and88 with J=16. The source mask list
is the already audited `reviews/newton-review-1-extension-result.json`,
SHA-256 `96f61ad6b173c1fd40bfc2dff3f87c44b616db87bd6db0a0ca77b1a019bee803`.
R2 independently obtained and compared the same complete list. Its use
here is an explicit accepted dependency, not another new proof review.

The primary normalization and characteristic-p inputs are attributed to
Castryck--Laterveer--Ounaies, [arXiv:1208.5404](https://arxiv.org/abs/1208.5404).
The two-recycled-root obstruction is credited to Draisma--Knopper via
Draisma--de Jong's Newsletter80, Proposition6. Massri's
[arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6), Theorem7.10, claims
the stronger absence of three-recycled-root degree20 polynomials without
the present rational restriction. That earlier preprint claim was
located but its computational proof has not been independently audited
here. This note does not rely on it, validate it, or claim a novel stronger
result. It supplies a separate exact rational-witness certificate.

## Why the finite families cover every possible three-witness case

Assume a counterexample has a covering set of size at most3. A covering
set of size1 forces a pure power; size2 is excluded by the cited input.
Choose its rational first-derivative witness and translate it to0. Scale
by the distinct rational center to make that center1. The normalizing
affine change is rational. Since1 is simple, it differs from0, and the
covering set becomes {0,1,u} for some rational u distinct from0,1.

Write d=20, a0=1,a1=-1, and

    f(x)=x^20-20*x^19+sum_(j=2)^18 binom(20,j)*a_j*x^(20-j),
    D_j(x)=sum_(k=0)^j binom(j,k)*a_k*x^(j-k).

For every j=2,...,18 choose the center1 whenever it is an available
common root. Otherwise choose0 or u. Since all noncenter rational roots
have positive integral19-adic valuation, reduction gives a_j=0 modulo19
on every noncenter choice. A center choice gives

    a_j = -sum_(k<j) binom(j,k)*a_k modulo19.

The divided equation f(1)/19=0 gives the final necessary congruence.
Thus every actual counterexample supplies a canonical mask in the complete
necessary enumeration. The previously reviewed exclusions/disjunctions
place that mask among the772. Noncenter masks do not require the center
to fail; this keeps a superset and cannot lose an actual counterexample.

For each mask, independently assign every noncenter position0 or an
indeterminate U. Set a0(U)=1,a1(U)=-1 and recursively over Z[U] solve

    a_j(U)=-sum_(k<j) binom(j,k)*a_k(U)*w_j^(j-k),
    w_j=1 at a center bit, otherwise0 or U.

There is no division in this recursion. The selected derivative equations
are exact polynomial identities, and the specialized actual coefficients
are forced by induction. The constant and linear coefficients remain0;
the first derivative condition at0 and the last at1 are already imposed.
An actual value u must in addition satisfy

    P(U)=f_U(1)=0,        Q(U)=f_U(U)=0.

Distinct assignments to0/U at different positions are allowed, and
repetition of witnesses is allowed. Every actual canonical mask and all
its possible0/U refinements are covered, with no height bound or
assumption that the remaining polynomial roots are rational.

The exact number of refinements is

    sum_(772 masks M) 2^(17-popcount(M)) = 1493024.

The mask list has no duplicates and each refinement is identified by its
pair (center_mask,U_mask), with disjoint bit sets. The recursive traversal
visits each such pair exactly once. These combinatorial facts are review
targets in addition to matching the total count.

## Exact finite incompatibility certificates

`computations/coordinator-three-witness-v2.py` constructs each pair P,Q
over the integers. It explicitly reuses the frozen author's elementary
polynomial helpers from `padic-rational-j17-compatibility.py`; its job
records that source hash. This is construction, not independent review.

For each pair the certificate is either a nonzero constant P or a prime
ell at which both integer degrees are retained and the reduced P,Q are
coprime. In the latter case the integer Sylvester resultant reduces to a
nonzero finite-field resultant. Therefore it is a nonzero integer, and
P,Q have no common root over Qbar. This avoids the invalid step of
reducing a rational u whose denominator might be divisible by ell.

The full initial run completed1493024 families and left exactly one case
unresolved by its five-prime list. Its unchanged raw totals are:

| Certificate | Cases |
|---|---:|
| Nonzero constant P |772|
| Prime101 |1416728|
| Prime103 |71108|
| Prime107 |4109|
| Prime109 |297|
| Prime127 |9|
| Unresolved by initial list |1|

The retained unresolved polynomial pair has key(6436,24785). The separate
targeted resolver, without changing that initial output, obtains
coprimality modulo131 with degrees(16,20) retained and leading residues
(8,102). Thus the proposed complete certificate resolves every family.
The new resolver is not an independent audit. Both initial incompleteness
and its additional exact certificate remain explicit artifacts.

The entire integer polynomial stream has SHA-256
`aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad`.
The uncompressed compact certificate stream has SHA-256
`4befc080569dbe0d4d978efaef502e51f644163d15ef9bd22ae7112cf1840387`.
It is stored in25 deterministic gzip chunks,9431158 bytes total. Rows
are either [mask,U_mask,0,Pconstant] or
[mask,U_mask,prime,degP,degQ,leadP,leadQ]; the single unresolved row has
sentinel-1 and is resolved by the separate JSON. All chunk hashes/counts
are in the result and candidate manifest. The compact representation
does not replace the independently regenerable exact polynomials.

This finite exhaustion, together with the coverage proof, would establish
T1 after two independent complete audits. A constructor's successful run
alone is not the project's reviewed-proof gate.

## Root-count consequences T2 and T3

The previously reviewed long-edge bound gives, for h=20-J,

    number of distinct rational roots <= h-m+2.

T1 requires at least4 rational roots, hence m<=h-2. For J=16, h=4 and
m>=2, so m=2. Exactly four distinct rational roots are then possible,
and all four are required:0, the simple center1 and two distinct nonzero
small roots u,v. All remaining15 root slots are the fractional long-edge
cluster, of valuation1/15.

Monic division by x^2(x-1)(x-u)(x-v) preserves Z_(19) coefficients,
since each removed root is19-integral. The quotient has degree15 and
every root has valuation1/15. Its coefficient of degree15-r, r>=1,
has positive valuation at least r/15, and rationality makes this an
integer valuation at least1. Its constant term, the product of all15
roots up to sign, has valuation exactly1. It is Eisenstein at19 and
therefore irreducible over Q_19 and over Q. This proves the proposed T2
conditional on T1; no irreducibility of an arbitrary Newton factor over
Q is inferred without these exact quotient-degree and rationality facts.

For J=15, h=5, the same inequality gives m<=3. If m=3, precisely two
small nonzero slots remain besides0 and1 and they must both be rational
to supply four witnesses. Removing x^3(x-1)(x-u)(x-v) leaves degree14
with every root of valuation1/14. The identical monic-integrality and
constant-valuation argument makes it Eisenstein. When m=2 the extra
small slot need not be rational, and no such quotient conclusion is
claimed. This proves the proposed scope of T3.

## Reproduction and current limits

From the repository root:

    .venv/bin/python -u problems/2021-B4/computations/coordinator-three-witness-v2.py
    .venv/bin/python -u problems/2021-B4/computations/coordinator-three-witness-v2-resolve.py

The complete main childPID31072 finished in163.005seconds under an
explicit300second timeout, with incremental8192-family checkpoints.
The separate resolver childPID32702 finished in0.074seconds under20seconds.
Both exited0 and were reaped; neither needed termination. Python3.12.14
and the standard library suffice. No native CAS, installed dependency,
paid API or third-party full paper is included in the certificates.

Preliminary J=16 and J=15 construction runs are preserved separately as
v1 artifacts,54240 and54400 families respectively. They are subsumed by
the complete v2 traversal and do not count as independent reviews.

The next substantive task is the four-witness case, particularly the
two-variable exact compatibility problem at J=16. The necessary772 masks
are unchanged by T1: it constrains witness multiplicity, not the number
of binary center masks. No full degree is solved and no unsupported
inference about all complex recycled roots is made.
