# Initially blind ENTIRE WHOLE R1: coefficient Frobenius cofactor extension

2026-10-18 UTC. Reviewer `/root/review_2021_reasoning_j15_r2` (A), OTHER nonconstructor. Requested inherited `gpt-6.1-sol` / `max`; independent effective-setting readback unavailable. Root is sole NEW R5 constructor and is excluded from the independent reviewer count. This is a recommendation, not promotion or external validation.

Target: `notes/cofactor-Frobenius-r5-candidate-v1.md`, 12486 bytes, SHA-256 `ff29bb1757d3f24229cb138bdfcca02b4d45c457200afc2ecc78104918c823ee`; constructor freeze 3932 bytes, SHA-256 `cda866d3b82dfe335c78643d15d857e21bcda5439c2ecf308956281b02a8b545`. I read the ENTIRE nine-file author packet, all 32 obligations, the full operative accepted CG/R4 copies and their current authority, and the primary sources within the exact limits in my source record. No corresponding NEW R2 R5 finding, report, ledger, source, code, hash or metadata was accessed before my ENTIRE initial packet froze. Findings are withheld until both entire initials are confirmed frozen.

## Recommendation and exact qualifications

I reconstructed R5A--R5D over the ENTIRE stated domain. I find **zero substantive defects and no required mathematical theorem repair**. I recommend the exact scoped conclusions, subject to the separate other whole audit and full coordinator reconciliation. I record **two nonsubstantive literal arithmetic/context errors** as closed corrective notes N1/N2, and four further scope notes. They must not be silently copied as true assertions:

- N1: for odd s, the correct residue is `2^s-1 = 1 (mod 3)`, not the frozen main's `2 (mod 3)`. Either nonzero residue would support the needed conclusion, and the required conclusion `3 does not divide Q-1` is true. The all-s argument is one line below and CF-13 already states the correct nondivisibility.
- N2: the same diagonal non-fixed-orbit calculation remains valid at s=3. The off-diagonal coprimality step fails there. The frozen contextual statement that the diagonal cube-root obstruction changes at s3 is inaccurate. s3 is already OUTSIDE R5's domain, and neither qualification changes R5A--R5D.

These are not missing global geometry, source hypotheses or new lemmas needed to repair a theorem. The exact corrected readings should be carried by coordinator reconciliation; frozen author bytes remain untouched. I do not endorse either inaccurate auxiliary sentence as a separate result.

The proposed theorem concerns an ordinary prime `s>=5`, integer `k>=2`, `Q=2^s`, `ell=Q-1`, `q=Q^k`. The notation `p=Q-2` is an ordinary positive integer, NOT a prime or the characteristic. The conclusions are the two strengthened multiplicity sums, the SAME positive `4s`-divisible D and its necessary threshold, and whole absolute irreducibility for `n=31*32^k+1`, every k>=2. There is no blanket decision for all prime-s k2, composite s, s3, k1 or all odd n, and no priority claim.

## 1. Actual cofactor and exact accepted interface

The official open question is coefficientwise factorization over F2, with integer lifts; it is not a question about polynomial functions on the eight F2 points. In the present family, `n=ell*q+1` is odd and greater than 3, and the quotient is nonzero homogeneous of positive degree `N=ell*q-2`.

I read the COMPLETE accepted CG body (19500 bytes) and R4 body (18793 bytes), their MD/JSON authorities and integrity records, including the accepted headers. CG1/CG2 and R4A--C are operative. CG3, the cubic threshold, HM's component theorem and any live Gauss/Frobenius source are not used in the R5 chain. Prior independent acceptance remains the authority for the old geometry; this is not a new independent recertification of an old result in which I participated.

For Q>=32 and k>=2,

```
q>=Q^2>2Q+5,
N-(3A-2)>=Q*(Q^2-4Q+9)>0,
A=Q(Q-3)>0.
```

The second inequality follows by subtracting `3A` from `(Q-1)Q^2`; its strict positivity is explicit. Thus the accepted size interface applies for EVERY parameter in R5. Assume absolute reducibility over K=F2bar. R4 then supplies its unique large absolute component G and ACTUAL nonconstant smaller cofactor H, normalized over F2 and exactly invariant under S4, with `0<e<A` and `e<N/2`. The irreducible case H=1 is not given a positive D.

CG supplies the COMPLETE projective singularity set, all F_Q-rational and all four values X,Y,Z,W nonzero. The non-P diagonal points have exactly two repeated values, and off-diagonal points have four distinct values. For the actual H, R4 supplies local diagonal multiplicity divisible by 4, six-/24-point S4 orbit sizes, `S=3(e-m)`, `4|D`, and CG supplies positivity of the SAME ordinary integer D. No assumption m>0, all points in H, or uniform multiplicity across unrelated orbits is made.

## 2. Commuting point actions and multiplicity invariance

Let F be coordinate squaring on projective points. Since all point coordinates have an F_Q normalization, `F^s` fixes every point projectively. Each S4 substitution has F2 coefficients; hence F and S4 commute on points. They preserve the central/diagonal/off-diagonal strata. F therefore acts on each finite set of S4 point-orbits with order dividing s. Since s is prime, cycle lengths are 1 or s. This statement concerns orbits of POINTS modulo S4, not factor-field Frobenius orbits.

The local multiplicity assertion can be checked without squaring the variables. Normalize Z=1 at P=(a,b,1), and write

```
H(a+x,b+y,1)=sum c_ij*x^i*y^j.
```

Applying the field automorphism only to coefficients gives `sum c_ij^2*x^i*y^j=H(a^2+x,b^2+y,1)` because H has F2 coefficients. A coefficient is zero iff its square is zero, so the least total degree is unchanged. This is NOT the polynomial square, which would double degrees. Projective chart normalizations multiply a homogeneous local equation by a unit and do not change multiplicity. Accepted exact S4 invariance likewise preserves it. Thus H's multiplicities are constant within each combined F/S4 orbit, with no cross-orbit equality needed.

## 3. Full diagonal calculation, including the minor residue correction

A standard noncentral diagonal point has four-coordinate multiset `{b,b,1,1}`, with `b in F_Q*` and b!=1. Two such standard points are S4-projectively equivalent precisely when their parameters are b and b^-1: either the common projective scalar preserves the two distinct values, or it interchanges them. Both possibilities are realized, and there is no third value to map to. The inversion sufficiency may be seen by swapping the two equal pairs and rescaling by b^-1.

Since F sends b to b^2, a fixed diagonal S4 orbit would require `b^2=b` or `b^2=b^-1`. The first gives b=1. The second gives b^3=1. For odd s,

```
2^s = -1 (mod 3),     Q-1 = -2 = 1 (mod 3).
```

Thus 3 does not divide the order Q-1 of F_Q*. A nontrivial cube root would generate a subgroup of order 3 and is impossible. This proves the desired exclusion, independently of the frozen main's incorrect numeric residue (N1). It needs only nondivisibility, not the wrong value 2. No code or field scan was needed.

Every diagonal orbit cycle consequently has s orbits. Each S4 orbit has six points. Its H multiplicity r is a multiple of 4 by the exact accepted two-tangent-translation argument, and it stays the same along the F cycle by Section 2. Hence a full cycle contributes `6*s*r`, a multiple of `24s`, to S. Adding disjoint cycles, including zero contributions, gives `24s|S`. The ordinary integer identity `S=3t` gives `8s|t`, including t=0. This reconstructs R5A.

As noted in N2, the same diagonal calculation works for s=3: Q-1=7 is still not divisible by 3. It does not extend the entire theorem there, because the NEXT stratum uses a different group argument that fails at 3.

## 4. Full off-diagonal calculation and projective scalars

At an off-diagonal point the four coordinate values are nonzero and distinct. If a projective permutation fixes it, a nonzero scalar c permutes that four-element set. Multiplication by c has a finite order d, and every orbit of a nonzero value has that exact length d. Hence d divides 4. In characteristic two, `c^4-1=(c-1)^4`, so c=1. The four distinct coordinate values then force the permutation to be the identity. This recovers the trivial projective stabilizer used in R5.

If F fixed an S4 orbit, choose a point P and sigma in S4 with `F(P)=sigma(P)` PROJECTIVELY. Commuting F and sigma yields `F^s(P)=sigma^s(P)=P`. By the trivial stabilizer, `sigma^s=id` as a permutation. Its order divides both s and 24, and `gcd(s,24)=1` for the stated primes s>=5. Therefore sigma=id and F(P)=P projectively.

Only now normalize the nonzero coordinate Z to 1. The projective equality becomes `(x^2:y^2:1)=(x:y:1)`, so x,y belong to F2. Nonzero four-coordinate values force x=y=1 and W=1, the central point, contrary to being off-diagonal. Thus no such orbit is fixed. All its F cycles have s orbits, each containing 24 points of the same H multiplicity. Summing gives `24s|V`, including V=0. This proves R5B without any assumption of uniformity on the entire off-diagonal set.

The exclusion s=3 is substantive for this step: a permutation can have order 3. In fact CG1 counts 24 off-diagonal points at Q=8, one S4 orbit, so its quotient orbit is necessarily Frobenius-fixed. This hand incidence check explains the failed extension; it does not alter the current prime>=5 claim or enumerate a field.

## 5. SAME-integer divisibility and sign-sensitive optimization

For an ordinary prime s>=5, multiplication by 2 permutes the nonzero residue classes modulo s. Multiplying all those residues and cancelling their nonzero product gives `2^(s-1)=1 (mod s)`, hence s divides Q-2=p. Here modular cancellation is in F_s for this elementary congruence; the polynomial curve still has characteristic 2. The two meanings of a prime are not conflated.

The actual integer satisfies

```
D=(ell-3)e+2m-V=p*m+(p-2)*t-V.
```

By `s|p`, `8s|t` and `24s|V`, s divides D. The SAME D is positive and divisible by 4 from accepted CG/R4. Since gcd(4,s)=1, it is a positive multiple of `4s`; set `d=4s`. There is no independent auxiliary D, arbitrary candidate multiplicity assignment or field-valued division here. Central multiplicity m need not be divisible by s, since its coefficient p already is.

The old actual-factor step has already established `B=q+1-2ell*e/A>0` and `T=p(e-e^2/A)>0`. With `a=(ell+2)/p>0`, the UNSIMPLIFIED CG inequality is

```
D*B<=T-a*D^2/A.
```

Divide by positive D, and use D>=d in BOTH terms to obtain

```
q+1 <= (p/d+2ell/A)e -p*e^2/(dA)-a*d/A.
```

Its maximum over ALL real e is

```
(dA/(4p))*(p/d+2ell/A)^2-a*d/A
 = pA/(4d)+ell+d*(ell^2-ell-2)/(pA)
 = pA/(4d)+ell+d/p.
```

The coefficient of e^2 is strictly negative. Allowing every real e can only enlarge the upper bound on an actual degree; no attainability or integrality of the maximizing vertex is needed. Subtracting 1 and setting d=4s gives exactly R5's necessary weak bound. Only its STRICT reverse yields a contradiction and whole absolute irreducibility. Equality and failure of the test give no converse. This reconstructs R5C.

## 6. Q32, the official integer factors, and remaining source boundaries

At s=5, `ell=31,p=30,A=928,d=20`, the exact threshold is

```
30*928/80 + 30 + 20/30 = 348+30+2/3 = 378+2/3 <1024.
```

For every k>=2, q=32^k>=1024 and all size conditions in Section 1 hold. Thus an actual nonconstant H would contradict the necessary threshold. This excludes ABSOLUTE reducibility, not merely a factor defined over a chosen extension. It proves the proposed whole Q32 family for all k, with no finite-field evidence or extrapolation.

An official integer factorization would reduce to two nonconstant polynomials over F2 with `f=R*gbar*hbar`. Since `f=R*phi` and R is a nonzero polynomial, cancellation in the polynomial domain gives `phi=gbar*hbar`, an absolute factorization. Conversely F2 factors have ordinary integer coefficient lifts, but no reverse factor descent is needed to exclude them here. The n=1/3 zero/unit endpoint issues lie outside this family; n here is positive odd and much larger than 3. No preliminary part (a) construction was investigated.

The possible overlap with Férard2017 remains UNRESOLVED: I freshly checked the original publisher's abstract/bibliographic page, not its inaccessible operative body. The institutional entry confirms a citation and HAL identifier, not a proof or a novelty assessment. The 2014 publisher abstract is contextual and concerns another residue branch. There is no HM proper-divisor component theorem or recent Gauss-map result imported into R5. Exact current and inherited source scopes are in the companion.

I did not construct R5 or supply any new inference to root. I previously authored some accepted 2024 T1/T4/C7/C11/component work and performed earlier CP/GK/jet/NF/FP/FS and R4 whole reviews. Those old roles remain disclosed accepted-input context, not fresh independent recertification of my own work. All new R5 inferences above were reconstructed independently of every new peer review.

## Disposition

All 32 author obligations have an explicit independent disposition in the ledger. N1/N2 require accurate editorial qualification of the frozen text, not a new mathematical theorem argument. N3--N6 preserve the domain, projective/actual-factor and source boundaries. No candidate file was edited, no mathematical program or routine test was run, and no peer material was accessed. The entire report, ledger, issues, source records, log, administrative code and all compact metadata must freeze and be fully read back/postverified before the identity-only completion is sent. Only after both ENTIRE initials freeze may these findings be released.
