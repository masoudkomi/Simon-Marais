# 2024 B4 research log

## Research significance and connections

Opening overview updated 2026-10-18. After removing the three prescribed
linear factors, B4(b) asks which homogeneous polynomials \(\phi_n\) split
over \(\mathbb F_2\). The same polynomial records four-term additive
relations among powers in characteristic two. Its zeros and components link
the problem to almost perfect nonlinear (APN) power maps, used in the study of
differential properties in cryptography, and to the minimum distance of
binary cyclic codes. [Hernando–McGuire](https://arxiv.org/abs/0903.2016)
explain and use both connections.

The research also belongs to algebraic geometry over finite fields: singular
points, tangent cones, intersection multiplicities and Frobenius actions
constrain possible components. These distinctions are essential. Splitting
over an algebraic closure differs from splitting over \(\mathbb F_2\), and
having one absolutely irreducible component defined over \(\mathbb F_2\)
does not establish irreducibility of the whole polynomial. Consequently the
published exceptional-APN classification does not itself answer B4(b).

The project's reviewed results include exact occurrences of specified factors,
Kasami-family criteria, structural restrictions and exclusion of all
three-bit odd exponents from the requested factorization. The
[neighbor-Frobenius criterion](reviews/coordinator-neighbor-Frobenius-r1-acceptance.md)
has now passed both independent whole reviews: for q=2^a, a>=2 and odd
ell>=3, either ell|(q-2) or ell|(2q-1) gives whole absolute irreducibility
of phi_(q ell+1). In particular it excludes the four-bit family
7*2^a+1 when 3 does not divide a; it does not decide the 3|a branch.
The [F8-pencil theorem](reviews/coordinator-F8-pencil-r1-acceptance.md)
is now accepted after TWO OTHER initially blind ENTIRE WHOLE36 audits
and reconciliation. For q=8^k,k>=2 it proves a factor-degree gap and
one large absolute component defined overF2, while permitting a small
nonconstant cofactor. The stronger
[cofactor-symmetry theorem](reviews/cofactor-symmetry-r1-acceptance.md)
is now accepted after TWO OTHER initially blind ENTIRE WHOLE48/48
audits and full reconciliation; root sole constructor is excluded.
S4/Frobenius multiplicities and a classical reduced-curve bound rule
out EVERY nonconstant cofactor, proving whole absolute irreducibility
for n=7*8^k+1,k>=2. Combined with NF3 this excludes n=7*2^a+1 for
every a>=2,a!=3. The theorem excludes q8/n57 and a0/a1; it does not
classify all four-bit exponents. The unrestricted ordinary reducibility
classification and priority remain unresolved. A
[dated literature follow-up](notes/cofactor-symmetry-literature-followup-v1.md)
records primary searches/access limits.

The newly accepted [dominant-cofactor/symmetry R4 theorem](reviews/cofactor-dominant-r4-acceptance.md)
adds whole absolute irreducibility for EVERY n=15*16^k+1,k>=2, following
two OTHER complete whole48/48 audits and reconciliation. Its actual
bounded invariant cofactor also supports a new coefficient-Frobenius
candidate for n=31*32^k+1,k>=2, still UNVERIFIED pending two whole audits.
The general classification and priority remain open.

See the [current dashboard](../../progress/dashboard.md),
[references](references.md), and [review register](reviews/README.md).

## Current reviewed structural result

T1–T4 are now **proved, independently reviewed partial restrictions**.
For odd binary-weight>=3 exponents, no absolute line or F2 factor of
degree at most three occurs. Individual factors through P obey exact
Frobenius/tangent-field constraints; v2(n-1)=3 has the stated necessary
local trichotomy. Two fresh whole blind audits were fully read and
hash-verified by the coordinator. See proofs/reviewed-structural-v1.1.md
and reviews/structural-acceptance.md/json. The only copy change is the
heading binary -> ternary cubics. No full exponent classification or
novelty is claimed. Factors avoiding P remain unrestricted by T3/T4.

Status: serious initial investigation checkpoint, 2026-10-16. **No full solution claimed.** The fixed-factor family in proofs/fixed-factor-family-reviewed-v1.1.md is **proved, independently reviewed (partial result)** after two blind full reconstructions. Other mathematical deductions below remain **candidate proof - unverified** unless identified as attributed published results. The exact whole-phi13 criterion in notes/zero-automaton-criterion-reviewed-v1.1.md has also passed two additional fresh blind full reconstructions. Later small-divisor probes remain separate and unreviewed. Computational identities are exact finite certificates, not a classification of unrestricted n.

Requested worker settings: gpt-6.1-sol, max reasoning. Verified effective-setting readback: unavailable. Worker owns only this directory; no commits, pushes, helpers or installations performed.


The newly accepted [CG1–CG3 general-cofactor theorem](reviews/cofactor-global-r2-acceptance.md)
has passed TWO OTHER initially blind ENTIRE56/56 audits and full
reconciliation. For Q=2^s,s>=3,ell=Q−1,q=Q^k, it proves whole absolute
irreducibility of phi_((Q−1)Q^k+1) whenever
q>=max(2ell+7,(ell−1)(ell−2)(ell+1)^2/4), in particular EVERY k>=4.
General projective geometry and two global factor bounds replace any
assumption of special F8 orbit uniformity. The reduced-component c−1
correction is retained. General smaller-k families, the full annual
classification and possible overlap with unread Férard2017 remain open.

The stronger [cubic-threshold R3A/R3B](reviews/cofactor-cubic-r3-acceptance.md) is now accepted after A/B OTHER initially blind ENTIRE WHOLE20/20 audits and full reconciliation. It covers EVERY s>=3,k>=3, using the sharper accepted CG inequality and positivity before division. The SEPARATE [dominant/symmetry R4A-E theorem](reviews/cofactor-dominant-r4-acceptance.md) is now accepted after TWO OTHER whole48/48 audits and full reconciliation. For every s>=3,k>=2 it constructs a unique large absolute component and an F2/S4-invariant cofactor of degree<A. Its multiplicity obstruction proves whole absolute irreducibility for n=15*16^k+1, EVERY k>=2. The new [coefficient-Frobenius R5 candidate](notes/cofactor-Frobenius-r5-candidate-v1.md) proposes an extension to n=31*32^k+1,k>=2; its ENTIRE32-obligation packet is frozen UNVERIFIED, with two OTHER whole reviews queued. General k2/full annual/priority remain open.
HM16's contextual component theorem requires a PROPER divisor and is
not a premise of CG; no component assertion at k1 is accepted.

## Statement checks

The official wording and coefficientwise convention were checked both by extraction and visual inspection. See statement.md. The boundary cases n=1 and n=3 are excluded. The official solution notes' shorthand statement that n=3 mod 4 gives irreducibility must exclude n=3, where phi_3=1 is a unit. The cited literature states the relevant range as n>3.

## Approaches and results

### 1. Primary-literature separation

Hernando and McGuire, arXiv:0903.2016v4, distinguish absolute irreducibility from the existence of an absolutely irreducible factor defined over F2. Their main classification of exceptional exponents proves the latter for non-Gold/non-Kasami odd exponents. It does not determine whether phi_n itself factors over F2, which is this problem. Their Section 6 gives the counterexample n=205 to the stronger irreducibility conjecture. The official 2024 notes still present only partial results. A bounded 2026-10-16 search did not locate a complete later classification; this is not proof of absence.

The established preliminary Gold family is used only as attributed context; no proof of part (a) is reproduced here. The Kasami family and field-of-definition details are discussed in references.md.

### 2. Exact invariant recurrence

Let w=x+y+z and define

    Q=x²+y²+z²+xy+yz+zx,
    R=(x+y)(y+z)(z+x),
    D=xyz(x+y+z).

The four quantities x,y,z,w sum to zero and are the roots of T^4+QT²+RT+D. Their power sums give the exact generating identity

    sum_{n>=3} phi_n t^(n-3) = 1/(1+Qt²+Rt³+Dt⁴).

Thus phi_n can be built in the three formal invariants of weights 2,3,4. For odd n every exponent of R is even. This materially reduces expression size. A formal proof is in proof.md; injectivity/irreducibility transfer is not assumed. Reducibility in F2[Q,R,D] gives reducibility after substitution only when both substituted factors remain nonconstant; failure to factor in this invariant subring does not establish irreducibility in F2[x,y,z].

The supplied exact script independently constructs the numerator by Frobenius powering in x,y,z, divides by R, and compares it with the invariant recurrence for all odd n from 3 through 65. All 32 comparisons passed.

### 3. The published n=205 factor is exactly phi_13

Transcribing the 42 terms in the degree-10 factor printed by Hernando--McGuire, then homogenizing, gives

    A=Q^5+Q D²+R²D=phi_13.

This is an identification of their published factor, not a new factorization claim. Exact formal division gives phi_205=A B with B having 248 terms in the invariant variables and weighted degree 192. Independent direct x,y,z construction and division gives a 2709-term cofactor of total degree 192; multiplication reproduces all 11754 terms of phi_205. The degree-10 factor has 42 x,y,z terms. JSON records both exact cofactors. No irreducibility of either factor is asserted by this calculation.

A bounded search for this single formal invariant factor among odd n in [3,1025] found exactly n=13 and n=205. Since at n=13 the complementary factor is constant, that hit alone is not a qualifying factorization. These exclusions concern only this particular formal factor and do not imply irreducibility of any other phi_n.

After the coordinator made python-flint 0.9.0 available, a fixed bounded probe factored n=5,7,9,13,21,25,29,41,45,57,205, with exact multiply-back for every result. Nontrivial degree patterns were 9: 3+3; 57: 27+27; 205: 10+192. Each remaining sampled exponent was reported as one factor by FLINT; these irreducibility reports are computational evidence only. The first run completed all factorizations but failed while serializing FLINT integer objects to JSON. Conversion to built-in integers repaired serialization; an early rerun (exec session 39778) remained in native n205 factorization at handoff and was marked incomplete for coordinator cleanup. The revised script omits n205, uses a 30-second subprocess timeout per exponent, and saves exact factors after each result. Its bounded output/JSON record the completed small cases; the original sparse certificate remains the completed n205 evidence.

### 4. Frobenius orbit approach

The known absolute Kasami factorization has factors indexed by alpha in F_{2^k} minus F2, of degree 2^k+1, with P_alpha(x,0,1)=(x+alpha)^(2^k+1). Frobenius groups their products into F2-defined factors. Delgado--Janwa (arXiv:1612.05997, Section 3) explicitly describe these orbit products. This suggests a precise distinction at n=13 versus n=57: there is one orbit on F4 minus F2, but two orbits on F8 minus F2. It should yield an attributed theorem-based certificate of reducibility at n=57, while n=13 requires checking irreducibility of the orbit product over F2. A proof using the cited factorization, normalization, and orbit transitivity remains to be audited. No broad conclusion based merely on absolute splitting is recorded.

### 5. Unsuccessful shortcuts and limitations

- The old Gold/Kasami-only reducibility conjecture is false at 205. The exceptional APN theorem does not repair this proposed classification.
- SymPy 1.14.0 has no general multivariate finite-field factorization support; it is not being treated as a complete factor oracle. python-flint was absent at initial inspection; coordinator was informed rather than installing a shared dependency from this worker.
- Irreducibility of a specialization is not being used without a degree-preservation argument. Reducibility of a specialization can occur when the original polynomial is irreducible.
- Symmetry does not force every individual factor to be symmetric. The invariant recurrence organizes exact identities but is not a complete factorization method.
- A speculative sequence connecting 13 and 205, namely n=(4^j+1)/5 for odd j, is only a hypothesis. The test at n=3277 completed: exact formal division has remainder zero and a cofactor with 34414 invariant terms. No unrestricted family is claimed.

## Next steps

1. Audit the invariant recurrence and the exact n205 certificate with two fresh reviewers before promotion of any lemma.
2. The n3277 test also passed; seek a Frobenius recurrence proof for the speculative sequence or disprove it at a later term. Do not extrapolate finite evidence.
3. If an adequate CAS becomes available, factor exact phi_n for a bounded set of odd n=1 mod4, multiply every output back, and record F2 factor fields. Seek further small fixed divisors, rather than assuming all non-Gold/Kasami quotients are irreducible.
4. Verify the original Janwa--Wilson factorization theorem and original JMW irreducibility theorem in their primary publications, not just subsequent quotations.
5. A possible compact route for the phi_13 divisibility family: localize at Q, set a=R²/Q³ and b=D/Q². The divisor relation becomes 1+b²+ab=0, hence a=b+b^(-1). The odd-index generating function reduces to (1+s+b s²)/(1+s²+(b+b^(-1))s³+b²s⁴). Study its coefficient zeros by Frobenius/Cartier or Dickson identities. This is a proposed route only; neither a criterion nor an unrestricted family has been proved.

## Focused second pass, 2026-10-16

**Candidate proof - unverified.** The preceding initial-pass record is
preserved; its speculative-family status is superseded by the separate
versioned candidate `proofs/fixed-factor-family-v1.md`, which is not yet
independently reviewed. The coordinator supplied an exploratory construction
in `notes/coordinator-cartier-family-v0.1.md`; this owner joined as a
co-constructor, independently rebuilt its exact identities, and completed
the localization, saturation and degree arguments.

The candidate states phi_13 divides phi_n for
n=(64*16^m+1)/5, m>=0. For m>=1 this gives a qualifying B4(b) factorization
with actual factor degrees 10 and n-13. The m=0 cofactor is 1, so this
family argument alone does not decide n=13. No full classification or
novelty is claimed, and no preliminary Gold-family proof is investigated.

The normalized rational series has denominator
K(z,b)=1+z²+(b+b^-1)z³+b²z⁴. Exact symbolic computation of K^15 gives
361 terms. The relevant Cartier numerators have 49,24,25 terms and exactly
match the proposed L,M,J formulas. The operators select coefficients and
are linear over F2(b), with no inverse-Frobenius operation on coefficients.
The two-dimensional numerator span has zero constant term and is
preserved while b is replaced by b^16. This yields an unrestricted
induction on hexadecimal indices j_m=(32*16^m-7)/5, whose digits are m
copies of 6 followed by 5.

The formal divisor A=q^5+q*d²+u*d is primitive and linear in u, hence
prime in F2[q,u,d]. It divides neither q nor d. Thus vanishing after
inverting q,d descends to polynomial divisibility. Weighted homogeneity
plus a mixed coefficient of the original f_n proves that neither
substituted factor vanishes and gives the claimed actual degrees. No
injectivity of the invariant substitution, no full-ring factorization
oracle and no absolute-irreducibility theorem is assumed.

The exact certificate uses Python 3.12.14 standard library only. A child
process with PID 12474 and 30-second timeout completed with return code 0
in 0.182 seconds. Script, complete symbolic monomial arrays, incremental
output, empty stderr and job parameters are retained in computations/.
Separate direct Laurent-series checks at m=0,1,2 are labeled finite
evidence and are not the induction proof. See the computations README.

The original-source search identified Éric Férard's 2014 paper,
DOI 10.3934/amc.2014.8.497. Its publisher abstract announces phi_13
divisibility and an infinite family in the residue class 5 modulo 8.
The exact full theorem was not accessible in this pass: the publisher's
normal PDF-availability endpoint requires login; a HAL record exists
but supplies no main-file URL. The independent candidate does not rely
on it, and exact prior attribution remains pending. No charge, access
restriction bypass, installation, commit or push was performed by this
owner. See `notes/source-access-2026-10-16.md` for the bounded queries,
failed access attempts and source hashes.

The frozen manifest is `notes/fixed-factor-family-v1-manifest.json`.
Two fresh reviewers who did not construct the proof must complete blind
initial reports, one reconstructing the whole argument. Neither the
coordinator nor this owner can count as an independent reviewer.
