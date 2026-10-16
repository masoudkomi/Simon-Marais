# 2024 B4 research log

Status: serious initial investigation checkpoint, 2026-10-16. **No full solution claimed.** Every mathematical deduction below is **candidate proof - unverified** unless explicitly identified as an attributed published result. Computational identities are exact finite certificates, not a classification of unrestricted n.

Requested worker settings: gpt-6.1-sol, max reasoning. Verified effective-setting readback: unavailable. Worker owns only this directory; no commits, pushes, helpers or installations performed.

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
