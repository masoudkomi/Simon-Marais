# Fixed phi7/phi11 divisor criteria: whole initial blind audit 2

2026-10-17 UTC. Independent nonconstructor review of the complete
divisor-reasoning-r2 candidate, source/provenance packet and its finite
phi11 certificate. No peer divisor report, issue ledger or conclusion
was read before this full report, ledger, source checks and independent
certificate records were jointly frozen.

## Verdict and scope

I found no substantive mathematical defect. I reconstructed the invariant
generating series, the injective/integral/normal bridge, both prime
localization arguments, the unrestricted C7 witness, the conjunctive
Frobenius-section invariant, the complete C11 certificate and language,
the absolute-gcd consequence and the graded-sum/zero cases.

The independent finite checker passed all 48 operator columns, all 15
complete subspaces, all 30 transition equalities, every output, and the
five-class quotient. It used only the fixed certificate, without a graph
search or coefficient-index scan. Its explicit five-second child timeout,
PID, checkpoints and successful reap are preserved separately.

The resulting mathematical conclusions are exactly
\[
\phi_7\mid\phi_n\iff n=7,\qquad
\phi_{11}\mid\phi_n\iff n=11
\]
for odd \(n\geq3\), together with the stated gcd and finite odd-sum
corollaries. Neither criterion classifies all possible factors or gives
a new reducible exponent. The published irreducibility and general
automatic-zero-set results are attributed premises/context, not claimed
new theorems. Promotion remains the coordinator's decision after both
independent audits.

The reviewed candidate is 16935 bytes, SHA-256
48d2ca76b3492584b38d8798650e078c7c9771fea97bae8db4d7cd51b21e2fc4.
The assigned constructor manifest is SHA-256
76143ab6f93a41f0fe5c3db8088e184f41c0159c8d61b089e0bdb66c3477b971.
All mathematical records named by that manifest are integrity-checked
in the companion review manifest.

The official domain is coefficientwise factorization over \(\mathbb F_2\)
for positive odd \(n\), with both remaining factors nonconstant modulo
two. Polynomial functions on the eight binary points are not the
domain. This audit addresses only part (b); it does not investigate or
reproduce the preliminary infinite-family construction.

## 1. General fixed-factor recurrence and its published hypotheses

For nonconstant \(\mathbb F_2\)-irreducible \(G\) not dividing \(R\),
the ideal \((G)\) is prime in the polynomial UFD
\(T=\mathbb F_2[x,y,z]\). Hence \(T/(G)\) is a domain and its fraction
field \(K\) is explicitly finitely generated over \(\mathbb F_2\).
The four images \(a_i\) of \(x,y,z,x+y+z\) lie in \(K\).

Each sequence \(a_i^n\) is annihilated by the shift polynomial \(U+a_i\).
The product of the four commuting operators therefore annihilates
\(v(n)=\sum_i a_i^n\), giving a monic recurrence of order at most four.
This remains true for repeated roots and for \(a_i=0\). In the latter
case the definition \(0^0=1\) gives the sequence \(1,0,0,\ldots\),
which is annihilated by the shift \(U\). Its initial value is not silently
discarded.

For \(n\geq3\), \(f_n=R\phi_n\). Since \(R\) has nonzero image in
the domain \(T/(G)\),
\[
G\mid\phi_n
\iff G\mid f_n
\iff v(n)=0\text{ in }K.
\]
Passing to the fraction field loses no nonzero element of \(T/(G)\).

Derksen's Theorems 1.10 and 4.14 have the needed hypotheses: positive
characteristic recurrence, with effective determination over an explicitly
finitely generated field for the effective statement. They do not require
this recurrence to be simple, basic or nondegenerate at input. The source
handles such reductions internally. The initial values here are explicit
polynomial images, so the recurrence is an effective input.

Thus the general fixed-\(G\) zero-set deduction is valid and attributed.
Restricting to odd indices at least three preserves automaticity by an
elementary regular/finite restriction. It does not find or bound the
unbounded collection of possible \(G\)'s. Adamczewski--Bell is additional
published zero-coefficient context, not a needed premise of C7 or C11.
In particular no claim is made that the infinitely many possible
\(\mathbb F_2(b)\)-valued coefficients themselves form a finite-valued
automatic sequence.

## 2. Invariant series and actual-to-formal divisibility

The accepted whole-phi13 packet and its coordinator acceptance were read.
Only its generating identity, section framework and ring bridge are used;
its older small-divisor probes and index scans are not accepted dependencies.
I also reconstruct the tools needed here.

For the four entries \(x,y,z,x+y+z\), the elementary symmetric functions
are \(0,Q,R,D\). Therefore
\[
E(t)=1+Qt^2+Rt^3+Dt^4.
\]
The formal power-sum identity gives the numerator series
\(Rt^3/E(t)\). Taking the even part of \(1/E=E/E^2\), then putting
\(s=t^2\), gives the odd-quotient series used in the candidate.
All denominators are units at the origin. This is the required invariant
identity for part (b), not a construction of a preliminary family.

In independent variables \(S=\mathbb F_2[q,u,d]\), coefficient comparison
gives
\[
P_j=q^2P_{j-2}+uP_{j-3}+d^2P_{j-4}
       +{\bf1}_{j=0}+q{\bf1}_{j=1}+d{\bf1}_{j=2},
\]
with negative subscripts zero. Consequently
\[
P_0=1,\ P_1=q,\ P_2=q^2+d,\ P_3=q^3+u,\quad
P_4=q^4+q^2d+qu+d^2.
\]
Substitution \((q,u,d)=(Q,R^2,D)\) gives
\(\phi_{2j+3}\).

For injectivity, the lexicographic leading exponents of \(Q,R^2,D\)
are \((2,0,0),(4,2,0),(2,1,1)\). An image of
\(q^\alpha u^\beta d^\gamma\) has leading exponent
\[
(2\alpha+4\beta+2\gamma,\ 2\beta+\gamma,\ \gamma).
\]
It determines \(\gamma,\beta,\alpha\) uniquely. The integer determinant
4 is about exponent vectors, not a determinant reduced modulo two.
In a finite nonzero sum the greatest such leading monomial cannot
cancel, proving the embedding \(S\hookrightarrow T\).

Each of \(x,y,z\) satisfies its quartic root equation with coefficients
\(Q,R,D\). Squaring gives the monic equation
\[
X^8+Q^2X^4+R^2X^2+D^2=0
\]
with coefficients in the image of \(S\). Thus
\(T=S[x,y,z]\) is integral over \(S\). For example, the monomials
with exponents below eight in each variable span a finite \(S\)-module.
The polynomial ring \(S\) is integrally closed in its fraction field.

If nonzero \(A,B\in S\) satisfy \(\iota(A)\mid\iota(B)\), the actual
quotient in \(T\) is the same element \(B/A\) of \(\operatorname{Frac}(S)\).
It is integral over \(S\), so it lies in \(S\). This proves the whole
element divisibility equivalence. The zero-\(B\) case is separately
trivial. No statement about every individual factor descending to \(S\)
is being inferred. No specialization at \(q=0\) or \(d=0\) was used in
this bridge.

## 3. Both formal divisors are prime and localization is saturated

For \(A_2=d+q^2=P_2\), the quotient is a polynomial ring in \(q,u\);
in particular \(A_2\) is prime and does not divide \(q\).
After inverting \(q\), set \(d=q^2\), \(u=q^3b\), and \(s=z/q\).
The normalized series is
\[
F_7=\frac{1+z+z^2}{1+z^2+bz^3+z^4}
\]
in a polynomial indeterminate \(b\), with free invertible \(q\).
Its \(z^j\) coefficient is the image of \(q^{-j}P_j\).

For \(A_4=qu+q^4+q^2d+d^2=P_4\), regard it as a polynomial in \(u\).
The coefficients \(q\) and \(q^4+q^2d+d^2\) have gcd one:
the second reduces to \(d^2\neq0\) modulo the prime \(q\).
It is primitive, and its degree one over \(\mathbb F_2(q,d)\)
proves irreducibility by Gauss's lemma. In the UFD \(S\) it is
prime and does not divide \(q\).

After inverting \(q\), eliminating \(u\) and putting \(d=q^2b\)
gives exactly
\[
u=q^3(1+b+b^2),\qquad
F_{11}=\frac{1+z+bz^2}
 {1+z^2+(1+b+b^2)z^3+b^2z^4}.
\]
The quotient in each case is precisely
\(\mathbb F_2[q,q^{-1},b]\); the displayed substitutions have an
explicit inverse. The parameter \(b\) is not a finite-field value
or a noninjective curve specialization.

If localization makes \(P_j\) zero modulo either prime \(A\),
clearing a power of \(q\) gives \(A\mid q^eP_j\). Since
\(A\nmid q\), primality gives \(A\mid P_j\) already in \(S\).
Conversely divisibility remains true after localization. Thus both
coefficient-zero equivalences (6) and (8) are exact.
Points with \(q=0\) were removed from an open set, but no irreducible
component of either divisor was lost: this is exactly the role of
saturation. The \(q\)-independence of the normalized coefficient then
identifies zero with zero in \(\mathbb F_2[b]\).

## 4. C7: every nonzero coefficient has an unrestricted witness

Write \(A(z)=1+z+z^2\). Since \(A^2=1+z^2+z^4\),
\[
F_7=\sum_{k\geq0}b^kz^{3k}A^{-(2k+1)}.
\]
For a given \(z\)-index only \(3k\leq j\) can contribute. A
chosen \(b^k\) witness therefore comes from exactly this summand,
with no interference from another \(k\).

The identity \(A^{-1}=(1+z)/(1+z^3)\) gives coefficients
\(a_t=1\) for \(t\equiv0,1\pmod3\), zero for
\(t\equiv2\pmod3\), and zero for negative \(t\).
For \(j=3m+r\), \(r=0,1\), take \(k=m\); the residual
constant or linear coefficient of \(A^{-(2m+1)}\) is one.
For \(r=2\), the same witness has value
\[
[z^2](1+z)^{2m+1}(1+z^3)^{-(2m+1)}
 =\binom{2m+1}{2}=m\pmod2.
\]
It is nonzero when \(m\) is odd. When \(m=0\), \(j=2\)
has only the \(k=0\) contribution, which is \(a_2=0\).

For every remaining case \(m>0\) even, uniquely write
\(m=2^vs\), \(v\geq1\), \(s\) positive odd. Choose
\[
k=m-2^{v-1}\geq0,\qquad
t=j-3k=3\cdot2^{v-1}+2.
\]
Then
\[
2k+1=1+2^v(2s-1),\qquad
A^{-(2k+1)}=A^{-1}B(z^{2^v}),\quad B=A^{-(2s-1)}.
\]
This Frobenius identity holds for negative unit powers as well
as for polynomials. The first three coefficients of \(B\) are
\(1,1,0\): its quadratic coefficient is
\(\binom{2s-1}{2}=s-1=0\) modulo two.

The inequality \(t<3\cdot2^v\) holds even for \(v=1\).
Only those three coefficients of \(B\) can contribute.
Their contribution is
\[
a_t+a_{t-2^v}.
\]
Here \(t\equiv2\pmod3\), whereas
\(t-2^v=2^{v-1}+2\) is nonnegative and congruent to
zero or one modulo three. The result is exactly one.

This covers every \(j\geq0\), with no bound on \(v\) or \(s\).
The unique zero index is \(j=2\). The ring bridge,
saturation and \(n=2j+3\) give C7, including the self case
and rejecting \(j=0,1\).

## 5. C11: prove the full conjunctive invariant

Let \(K=1+z^2+(1+b+b^2)z^3+b^2z^4\).
Its constant \(z\)-coefficient is one, so every coefficient
of \(N/K\) lies in \(\mathbb F_2[b]\); no negative powers
or convergence issues occur.

In characteristic two \(K^2=K(z^2,b^2)\). For the four
parity sections,
\[
C_{r,t}(N/K)=C_{r,t}(NK)/K.
\]
This follows by writing \(N/K=NK/K(z^2,b^2)\) and extracting
the common doubled-argument factor under the section.

The numerator space has monomials \(z^ib^h\) with
\(0\leq i\leq3,\ 0\leq h\leq2\). Multiplication by \(K\)
has \(z\)-degree at most seven and \(b\)-degree at most four;
selecting either parity and halving stays in that same
12-dimensional space. The initial numerator \(1+z+bz^2\)
belongs to it.

For a coefficient \(c(b)=[z^{2a+r}](N/K)\), its even and odd
parameter supports decompose uniquely as
\[
c(b)=c_0(b^2)+b\,c_1(b^2),\qquad
c_t(b)=[z^a]C_{r,t}(N/K).
\]
It vanishes if and only if both \(c_t\)'s vanish.
Quantifying over every \(N\) in a subspace \(W\) is thus
equivalent to quantifying over all \(L_{r,t}N\), and then
over their \(\mathbb F_2\)-linear span \(T_r(W)\).
This is a conjunction of the two parameter sections, not
a choice of a single branch or a union of separate zero sets.

Induction on the least-significant-first digits gives the
candidate's invariant for every residual index \(a\geq0\).
At \(a=0\), acceptance is exactly vanishing of the constant
\(z\)-coefficient of every numerator, since \(K(0,b)=1\).
With bit \(3i+h\) encoding \(z^ib^h\), the acceptance mask
is exactly bits 0, 1 and 2. Testing a basis is sufficient,
and the independent checker also checks every vector.

The invariant covers the empty word, arbitrary finite words,
and appended zeros. Appended zeros are leading zeros of the
usual binary integer, not a change in its value. No limiting
or canonical-word assumption is needed to obtain (15).

## 6. Independently reconstruct all finite certificate data

The reviewer implementation is divisor-review-2-certificate-v1.py.
It hard-codes the candidate's 15 bases and 30 proposed targets
as data, and constructs all maps from the actual six denominator
shifts
\[
(0,0),(2,0),(3,0),(3,1),(3,2),(4,2).
\]
It does not import a constructor function, operator column,
complete state or graph search. For each monomial, the appropriate
shifted parities directly give its section column by XOR.

The independently obtained columns, ordered by bit \(3i+h\), are:

| Section | Twelve column integers |
|---|---|
| 00 | 137, 0, 274, 192, 128, 384, 1096, 0, 2192, 1536, 1024, 3072 |
| 01 | 0, 137, 0, 64, 192, 128, 0, 1096, 0, 512, 1536, 1024 |
| 10 | 24, 16, 48, 137, 0, 274, 192, 128, 384, 1096, 0, 2192 |
| 11 | 8, 24, 16, 0, 137, 0, 64, 192, 128, 0, 1096, 0 |

The implementation uses canonical Gaussian elimination, in
addition to complete vector sets, to check each declared subspace
and every image equality. The dimensions are
\[
1,2,2,4,4,4,4,4,5,6,6,5,5,5,5.
\]
All 15 subspaces are distinct; all displayed bases are independent;
state zero is precisely the span of the actual initial numerator.
For each of the 30 edges it verifies the image span from a basis
and from all source vectors, then compares the entire target vector
set. Both parity sections are included in every image.

The full bases, complete finite vector sets, all image generators
and image vector sets, and all equality records are retained in
divisor-review-2-certificate-output-v1.json. After this independent
construction, they were also compared with the frozen constructor
certificate/output, and agree exactly. The comparison is not a
premise of constructing the reviewer maps.

Only states 8 and 14 satisfy the complete output test. The
partition \(S=\{0\},A=\{1\},B=\{3\},Z=\{8,14\}\) and the
ten-member \(X\) class respects every output and both outgoing
edges of every state. Its exact transition structure is
\[
S\xrightarrow0 A\xrightarrow0 B\xrightarrow1 Z,\qquad
Z\xrightarrow0 Z;
\]
each other edge goes to the rejecting sink class \(X\).
Thus the whole finite-word language is \(0010^*\).
The empty word rejects. A canonical positive integer word,
read least significant bit first, ends in one; the sole such
accepted word is \(001\), of value four. Zero padding
preserves that value and stays in \(Z\).

For completeness, all 15 states have explicit path witnesses
in the displayed graph: in state order they are
empty, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, 100,
111, 0001, 0010. This hand tracing is not a word scan.
Closure and the initial state already suffice for the invariant
argument even without a reachability claim.

Consequently the exact zero index is \(j=4\), and C11 follows
by the two algebraic bridges and \(n=2j+3\).

## 7. Necessary finite job, its bounds and provenance

The only new mathematical computation was this fixed symbolic
certificate. It was run by a separate reviewer harness:

    .venv/bin/python problems/2024-B4/reviews/divisor-review-2-run-v1.py

Child PID 77847 started at 2026-10-17T00:49:37.930799Z,
under an explicit five-second external timeout. It completed
with return code zero in 0.04090591595740989 seconds including
launch and was reaped. Five incremental checkpoints record
columns, full states, transitions, outputs/quotient and the
postconstruction comparison. Stderr is empty.

The harness creates new job, completion, stdout and stderr files
exclusively and would terminate only its identified child on
timeout. The fixed certificate output is also create-new.
Reproduction must use a new version/prefix, preserving this
frozen run. No native CAS, larger BFS, larger graph, coefficient
index scan, routine sample tests or separately billed API was
used. The finite complete subspaces are the required certificate,
not empirical evidence for an extrapolated coefficient pattern.

## 8. Absolute gcd, extension fields and finite sums

The original McGuire thesis defines the affine polynomial as
\(\phi_t(x,y,1)\). Its Theorem 2.1' applies for
\(t>3,\ t\equiv3\pmod4\), so it supplies the attributed
absolute irreducibility for \(t=7,11\). I checked the definition,
the theorem's exact hypotheses and its complete printed proof
on the cached author pages, rather than substituting APN
nonexceptionality.

For these odd \(t\), the coefficient of \(x^{t-1}y\) in
\(f_t(x,y,0)\) is one. Thus the specialization is nonzero,
as is \(R(x,y,0)=xy(x+y)\), and
\(\phi_t(x,y,0)\neq0\). Dehomogenization retains the full
degree \(t-3\); no extra \(z\) component disappears.
Rehomogenizing the absolute affine irreducibility therefore
gives absolute irreducibility of the homogeneous \(\phi_7\)
and \(\phi_{11}\), of degrees four and eight.

For any extension field \(L/\mathbb F_2\), the vector-space
map \(T/(G)\to(T/(G))\otimes_{\mathbb F_2}L\) is injective.
Its scalar extension is \(L[x,y,z]/(G)\). Therefore divisibility
of an \(\mathbb F_2\) polynomial by the fixed \(\mathbb F_2\)
polynomial \(G\) is unchanged by extending the field.
Over the algebraic closure the two fixed divisors are prime
and nonassociate. The certified failure of whole divisibility
is hence exactly absence of their common absolute components.
This proves the stated gcd formula, using the given
\(\mathbb F_2\) representatives for normalization.

A homogeneous principal ideal is graded: if a homogeneous
generator divides a polynomial, decomposition of its quotient
by degree makes every homogeneous component divisible by that
generator. The nonzero \(\phi_n\), \(n\) odd and at least
three, have distinct degrees \(n-3\). Thus divisibility of a
finite sum forces divisibility of every included component;
C7/C11 give exactly (17).

The zero sum is included: with all coefficients zero both
divisibilities hold and both right-hand conditions are
vacuous. Conversely distinct nonzero homogeneous degrees
cannot cancel each other. An empty index set is harmless.
No general factorization classification for sums follows.

## 9. Boundary cases, attribution and remaining conclusions

For odd \(n>1\), the mixed coefficient \(x^{n-1}y\) of \(f_n\)
is one, so \(f_n\), \(\phi_n\) and their degrees are nonzero.
At \(n=3\), \(j=0\) and \(\phi_3=1\), rejected by both
criteria. At \(n=7,11\), the certified self-divisor has unit
cofactor; the published absolute irreducibility rules out
a product of two nonconstant factors there.

At \(n=1\), \(f_n=0\). Both remaining factors demanded by
the official problem are nonconstant modulo two, hence
nonzero in the integral domain \(T\); their product with
nonzero \(R\) cannot be zero. The criterion intentionally
does not extend its index convention to this excluded case.

The selected-family gcd results in Delgado--Janwa were
checked in the actual theorem statements. Distinct Welch
degrees are one covered family. Their later designated Gold
divisor is not 7 or 11. Those results do not replace an
arbitrary-odd-index criterion for either fixed divisor.
The general automaticity/effectiveness is published and
correctly separated from identification of these two sets.
Unread Férard material and other incomplete literature
access prevent a priority or exhaustive-absence claim;
the candidate makes neither.

The accepted whole-phi13 result remains separate. The
unverified structural T1--T4 packet is not needed. Rejection
by C7 or C11 excludes only these two absolute factors, not
all other factors. No larger classification, new reducible
family, APN classification or novelty is accepted here.

## Integrity and review status

All input and proof-support hashes, including the original cached
thesis and accepted dependency, are recorded in the companion
manifest. All twenty-eight files previously frozen by this reviewer
remain unchanged. Only the assigned divisor-review-2 prefix is
written. No candidate, constructor output, peer divisor report,
earlier review, shared source or Git state was edited.

Requested model/reasoning: gpt-6.1-sol / max. Independent
effective-setting readback is unavailable. The most recent
authoritative weekly telemetry before this audit was 20%
total used, window 10080 minutes, reset 1792745187.
The 90% total-used cutoff and integration reserve remain
in force. The final manifest records a fresh completion
check. No new weekly window or separately billed service
was used.

This whole initial report, issue ledger, source checks and
independent finite run are frozen jointly before peer
comparison. Only the coordinator may promote the result.
