# Diagonal moment MS1--MS5: whole initial review 2

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1`. Requested
gpt-6.1-sol/max; verified effective readback unavailable. This is a fresh
initially blind nonconstructor WHOLE audit of the coordinator's
consolidated v2. I did not construct MS1--MS5. I have read no new peer
moment review or its conclusions. The separate 2024 NV review was fully
frozen before I opened this task's candidate.

**Finding:** no substantive mathematical objection found to MS1--MS5 as
written. All fourteen submitted obligations pass. Their distinction
between Fourier and reciprocal maps, and between within-list and
cross-list separation, is essential and is retained. The packet neither
proves the original second-case application nor gives a new Diophantine
exclusion, complete annual classification or novelty result. This report
does not promote the candidate.

## Exact audited submission and scope

The consolidated main is `coordinator-diagonal-moment-candidate-v2.md`,
7096bytes, SHA256
`dae1907e2c3afe744ede7ffc89321d560ebbfab326afd78786f30dac960fcb2f`.
The manifest is 1545bytes, SHA256
`5d0d897d3ff89828e26d16919357bf0d283866bb3bb97b7aa9f1277b3a3d3654`.
I read the complete candidate, all fourteen obligations, its source JSON,
ALL four preserved moment notes v1/v1.1/v1.2/v1.3, the complete appendix
inspection note, the accepted CF1 body and the local reference/statement
files. I independently inspected the primary definitions and relevant
source contexts described in the source-check record. The author's
administrative script is fingerprinted only, not executed. No math
program, scan, CAS, author rerun or certificate is used.

The official 2025 B4(b) concerns integer quadruples \((x,y,n,q)\) with
\(n,q\ge2\), and its sum has DEGREE \(n\) and \(n+1\) terms. No
restriction to positive \(x,y\), diagonal exponents, or the first case
can answer that entire question. Here \(p\) is a separate odd prime
indexing cyclotomic algebra; applying it to a diagonal equation would
have official degree \(p-1\), term count \(p\), and power \(p\).
MS1--MS5 themselves have no variable \(x\) and no solution-exclusion
conclusion. This audit does not reproduce the preliminary part(a).

## Conventions: keep three different operations separate

Let \(G=\operatorname{Gal}(\mathbf Q(\zeta)/\mathbf Q)\) for a primitive
\(p\)-th root \(\zeta\). In the DIRECT basis
\(\sigma_a(\zeta)=\zeta^a\), write

\[
 \theta=\sum_{a\in\mathbf F_p^*}n_a\sigma_a,
 \quad M_-(\theta)=\sum_a n_a a^{-1}\in\mathbf F_p,
 \quad E(\theta)=\sum_a n_a\zeta^a.
\]

The domain has the regular left \(G\)-action \(\sigma_h\theta\).
"Conjugacy" of its elements here means this \(G\)-orbit relation, not
inner conjugation in the commutative ring. The reciprocal coordinates
are a DIFFERENT map:

\[
 R_c(\theta)=\sum_a n_a\frac{1-\zeta}{1-\zeta^{ac}}.
\]

Finally the multiplicative group-ring action on \(\zeta\) is
\(\zeta^\theta=\zeta^{\sum_a n_a a}\). Its vanishing exponent is the
DIRECT first moment \(\sum n_a a\), rather than \(M_-\). These three
operations are not identified anywhere in the audited proof.

## MS1 reconstructed: residues in one fixed localization

Put \(O=\mathbf Z[\zeta]\) and \(\lambda=1-\zeta\). The presentation
\(O=\mathbf Z[Z]/(\Phi_p(Z))\) gives

\[
 O/(\lambda)\cong\mathbf Z[Z]/(\Phi_p(Z),Z-1)
 \cong\mathbf Z/(\Phi_p(1))=\mathbf F_p.
\]

Thus \((\lambda)\) is a maximal ideal and the localization used in the
candidate is defined. For \(1\le t<p\),

\[
 \frac{1-\zeta^t}{1-\zeta}=\sum_{i=0}^{t-1}\zeta^i
 \equiv t\not\equiv0\pmod\lambda.
\]

It is therefore a unit in \(O_{(\lambda)}\); its reciprocal lies there
and reduces to \(t^{-1}\). For each product \(ac\), choose its nonzero
representative \(t\) modulo \(p\). The power \(\zeta^{ac}\) and that
of its representative are the same; no literal integer \(ac\) is being
inverted without reduction. Summation, allowing arbitrary signed
integer \(n_a\), gives

\[
 R_c(\theta)\equiv c^{-1}M_-(\theta)\pmod\lambda.
\]

If the moment is nonzero, the \(p-1\) residues are distinct and so are
the elements of the localization and its fraction field \(K\). A common
nonzero scalar preserves all inequalities of pairs. The argument does
not give that conclusion for unrelated scalars depending on \(c\).
No positivity, archimedean ordering or absolute-size estimate is used.

## MS2 reconstructed: faithful Fourier evaluation

For completeness, \(\Phi_p(Z)=1+Z+\cdots+Z^{p-1}\) is the minimal
polynomial of \(\zeta\): \(\Phi_p(Z+1)\) is Eisenstein at \(p\), by
the binomial coefficients of the prime \(p\). If \(E(\theta)=0\), the
polynomial

\[
 P(Z)=\sum_{a=1}^{p-1}n_a Z^a
\]

has degree at most \(p-1\), constant coefficient zero, and is divisible
by \(\Phi_p\) over \(\mathbf Q\). If it is nonzero, it must be a
constant multiple of \(\Phi_p\); its constant coefficient then makes
that multiple zero, a contradiction. Thus \(P=0\) and all coefficients
vanish. No weight constraint, common augmentation or positivity enters.

Multiplying direct indices shows exactly

\[
 E(\sigma_c\theta)=\sum_a n_a\zeta^{ca}
 =\sigma_c(E(\theta)).
\]

Injectivity now gives the claimed equality of stabilizers. It also
gives, from any equality of cross-list entries,

\[
 E(\sigma_c\theta_1)=E(\sigma_d\theta_2)
 \Longrightarrow\sigma_c\theta_1=\sigma_d\theta_2
 \Longrightarrow\theta_2=\sigma_{d^{-1}c}\theta_1.
\]

Consequently nonconjugate group-ring elements have disjoint Fourier
value SETS. This does not require either orbit to have \(p-1\) elements.
Also \(E\) is only asserted to be Z-linear and equivariant; it is not
being treated as a ring homomorphism.

## MS3 reconstructed: moment transformation and limits

For every \(h\in\mathbf F_p^*\),

\[
 M_-(\sigma_h\theta)
 =\sum_a n_a(ha)^{-1}=h^{-1}M_-(\theta).
\]

If \(\sigma_h\theta=\theta\) and the moment is nonzero, this forces
\(h=1\). Its stabilizer is trivial, and MS2 makes all Fourier orbit
entries distinct. Zero moment does not force a nontrivial stabilizer;
for example the integer group-ring element \(p\sigma_1\) has zero
moment modulo \(p\) and has trivial stabilizer. Thus sufficiency is
correctly distinguished from necessity.

The submission's norm-element warning is valid, including the module
membership implicit in that warning. For \(N=\sum_a\sigma_a\),
coefficients are positive and weight is \(p-1\), and
\(\zeta^N=1\) since \(\sum a\equiv0\pmod p\) for odd \(p\).
In the source Stickelberger setting,
\(N=(1+\jmath)\Theta_2\): opposite coefficients of \(\Theta_2\)
sum to one. Hence \(N\) belongs to that ideal and to its Fermat
kernel. Nevertheless it is fixed by all \(G\), and \(E(N)=-1\).
Those module/weight/positivity properties alone cannot supply the
needed freeness.

It would also be false to transfer MS2's injectivity to the reciprocal
map. For \(p\ge5\), the nonzero element
\(\sigma_1+\sigma_{-1}-\sigma_2-\sigma_{-2}\) has every reciprocal
coordinate zero: each opposite pair of reciprocals sums to one before
multiplication by \(\lambda\). Its inverse moment is zero, so this is
no counterexample to MS1. It is a hand-derived check of the excluded
map-identification route, not a new program or source-dependent claim.

## MS4 reconstructed: full square-sum argument and reindexing

Let \(p\ge5\), and let \(a\) be ANY positive integer prime to \(p\).
Define exactly as in the source's inverse basis

\[
 \Theta_a=\sum_{c=1}^{p-1} k_c\sigma_c^{-1},
 \qquad k_c=\left\lfloor\frac{ac}{p}\right\rfloor.
\]

Its DIRECT index is \(c^{-1}\). Therefore the inverse moment under
audit is \(\sum_c c k_c\), whereas its action-on-\(\zeta\) moment
is \(\sum_c c^{-1}k_c\). This explicit index inversion is required;
there is no inference from the latter moment being zero to the former
being zero or nonzero.

Put \(r_c=ac-pk_c\in\{1,\ldots,p-1\}\). Since multiplication by
\(a\) permutes nonzero residues, the \(r_c\) permute that entire set.
Writing \(S_2=\sum c^2\), \(S=\sum c k_c\), and \(T=\sum k_c^2\),
the EXACT integer equality is

\[
 S_2=\sum r_c^2=a^2 S_2-2apS+p^2T,
 \qquad 2aS=(a^2-1)\frac{S_2}{p}+pT.
\]

For \(p\ge5\),
\(S_2/p=(p-1)(2p-1)/6\) is an integer. The division by \(p\)
has occurred in the integers before any reduction. Modulo \(p\), six
and \(2a\) are invertible, giving

\[
 2aS\equiv\frac{a^2-1}{6},\qquad
 M_-(\Theta_a)=S\equiv\frac{a-a^{-1}}{12}.
\]

The proof covers arbitrary positive \(a\), including \(a>p\); no
coefficient bound for floors is needed. At \(a=1\), both sides vanish,
as a basic degeneracy check. The formula has not been extended through
the excluded prime \(p=3\), where division by six is invalid.

## MS5 reconstructed: constants, small primes and general Fueter elements

For primes \(p>7\), both \(2\) and \(3\) satisfy MS4's hypotheses.
Substitution and subtraction give

\[
 M_-(\Theta_2)=\frac{2-1/2}{12}=\frac18,
 \quad M_-(\Theta_3-\Theta_2)
 =\frac{3-1/3-2+1/2}{12}=\frac7{72}.
\]

Both are nonzero in \(\mathbf F_p\) in this range. Thus both concrete
elements satisfy MS1 and MS3 without ANY premise that they lie in a
particular solution's Fermat module. Their eligibility for the ORIGINAL
first-case selection is a distinct application condition and is not
granted unconditionally by these calculations.

For \(p=7\), the second moment is zero. That neither refutes separation
by another argument nor supplies it from the current hypothesis. For
\(p=3\), MS4/MS5 do not apply. MS1--MS3 remain valid for the stated
odd prime \(p=3\), subject to their own moment assumptions. The candidate
does not assert a false all-prime nonzero second constant.

When \(p\nmid n(n+1)\) and \(p\ge5\), subtraction at \(a=n+1,n\)
likewise gives

\[
 M_-(\Theta_{n+1}-\Theta_n)
 =\frac{n^2+n+1}{12n(n+1)}.
\]

This can vanish, as already illustrated by \(p=7,n=2\). It does not
grant all Fueter elements, nor any unspecified pair supplied in a second
case, a nonzero moment. No enumeration or modular table is needed.

## Primary-source application boundary

Actual primary passages were checked: the original author upload's
inverse-index definitions, Fermat kernel, first-case choices and Fourier
coefficient formula; and the later arXiv edition's reciprocal coefficient
definitions and appendix footnote. Their exact locations and read limits
are in the source record. They support the distinctions used here, not
an import of a full Diophantine proof.

For a pair ACTUALLY satisfying the original source's nonconjugacy
conclusion, MS2 proves cross-list Fourier disjointness. It proves neither
that such a pair exists nor trivial stabilizer of each member. MS5
verifies moments for the two concrete first-case elements; it does not
newly prove their solution-specific Wieferich prerequisites. The later
coefficient \(b_1\) has reciprocal normalization; the footnote's
correspondence of roles does not identify it with the original \(E\).
MS1 applies when the exact reciprocal normalization and nonzero moment
are present, not by transferring Fourier injectivity.

The appendix note's concerns are not mathematical counterexamples to an
external theorem. In particular bouquet dimension growth is a separate
local linear-algebra fact, and neither it nor the separation proved here
settles the intended augmented equations, propagation to EVERY
conjugate, or the nonzero-\(\delta\) branch. This review accepts no such
repair and no refutation of the source's conclusion. Accepted CF1 and PG
retain their independent scopes. No enlargement of the Diophantine
range, full annual solution, or priority conclusion follows from this
packet. No author repair requested for MS1--MS5; two-review coordinator
reconciliation is still required.
