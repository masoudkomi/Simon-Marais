# Independent adversarial review R1: 2023 B4(b), resultant candidate v0.1

**Initial blind report completed 2026-10-16, 10:07 UTC.**

## Identity, independence and disposition

- Reviewer: independent R1 agent; not a constructor of the candidate.
- Requested launch settings: `gpt-6.1-sol`, `max`. Verified effective model/reasoning settings: unavailable; no readback was supplied.
- Reviewed file: `notes/candidate-resultant-v0.1.md`, SHA-256 `77d209d6a35ebf96a72d5d3a29f9f23d8f7456adae01d1572c180cf842c05365`.
- I did not read another review or receive another reviewer's conclusions before completing this initial report. I did not use the constructor's computation files. I reconstructed the whole argument, including the attributed-input interface, necessity, both arithmetic branches, and sufficiency.
- **R1 disposition: no substantive mathematical objection identified.** The candidate's classification follows from its stated published inputs and the new argument as written. The derivations below explain the checks behind this conclusion; finite computations are supplementary evidence.
- No mathematical repair is required by this report. Two optional exposition improvements appear at the end. This is one review, not promotion to **proved, independently reviewed**. The coordinator must consider the other independent audit, resolve any objections it raises, and decide promotion.

## Official-domain and citation audit

The authoritative [2023 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023_paper_b.pdf), printed p. 2, B4(b), fixes a positive nonsquare integer before asking for the positive exponent pairs admitting a real witness. The witness may be negative. Squarefreeness is not assumed. The candidate answers exactly this question for every such fixed integer, including nonsquare integers with square factors. Swapping the two exponents preserves the question. Zero is a real number allowed by the domain but cannot be a witness, because it would leave the irrational square root unchanged.

On 2026-10-16 I opened the [official 2023 download index](https://www.simonmarais.org/20231.html), which links the same Paper B and [solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023solutions.pdf). I checked the cached statement visually and extracted the relevant solution pages, then inspected their renders. The cited solution notes, printed pp. 14-16, support the input interface: the diagonal family, exclusion of positive off-diagonal witnesses, the opposite-parity restriction for remaining pairs, and the complete exponent-1 case. Their hypotheses match the candidate's integer and real domains. I have not re-solved or reproduced preliminary part (a).

The official source gives the negative witness `1/2-sqrt(N)` for the pair `(1,2)`. The candidate's lift to odd common multiples is valid. The candidate correctly attributes the published restrictions and treats its exclusion of the other coprime pairs as the proposed new argument. No primitive-divisor theorem or other unverified external theorem is needed.

The live official files still present partial results; this does not establish that no subsequent solution exists elsewhere. I have not performed a comprehensive literature or priority audit and make no novelty claim.

Input fingerprints:

| File | SHA-256 |
| --- | --- |
| `statement.md` | `fda8eb54dd99b5fea498e72fd3196063b743c93194ae73bc86457710b0fdc42e` |
| `.cache/official/2023-paper_b.pdf` | `7d8ec51774224eeb1d66c1bae5ba6df98c0f7b41b0635811105a669be7a6eee2` |
| `.cache/official/2023-solutions.pdf` | `446d9d19f962e9bbc727422be6a5c1de62fcf0fc3d0cf424494861d7eb7d832c` |

## Independent reconstruction and inference audit

### 1. Original exponents, gcd reduction and signs (candidate lines 25-60)

For an off-diagonal pair, the published restrictions give a negative nonzero witness and exponents of opposite parity. Their gcd `d` is therefore odd, so `x=r^d` remains negative and the reduced exponents retain their respective parities. The reduced exponents `e,o` are coprime. Both nonzero powers belong to the quadratic field `K=Q(sqrt(N))`. If integers `s,t` satisfy `se+to=1`, then `x=(x^e)^s(x^o)^t` belongs to `K`; negative powers cause no problem because neither power is zero.

The field has degree two even when `N` is not squarefree, because `N` is an integer nonsquare. Conjugation sends the irrational coefficient `-1` in each rational-minus-square-root power to `+1`; consequently both conjugate differences equal `2sqrt(N)`. The odd equation gives `x'>x`, while the even equation gives `|x'|>|x|`. With `x<0`, these statements force `x'>-x>0`. Thus `U=x'`, `V=-x` satisfy `U>V>0`, with positive rational `D=U-V` and `P=UV`.

The two real equations become `U^e-V^e=U^o+V^o=2sqrt(N)`. The first ensures `U>1`. If `e<o`, the strict inequalities obtained by comparing `U^e` and `U^o` contradict the equality. Equal indices have incompatible parity. Hence `e>o`; `o=1` is exactly the published exponent-1 input, and every still-unsettled case has `e>o>=3` with the asserted parity and coprimality. No assumption about a rational original witness is introduced.

### 2. Recurrence, positivity and degrees (lines 66-108)

The characteristic polynomial is `T^2-DT-P`, whose distinct roots are `U,-V`. Its standard difference-of-powers formula has denominator `U+V>0` and satisfies the stated initial values and recurrence. It gives `F_e=F_o` and `(D^2+4P)F_o^2=4N`, since `D^2+4P=(U+V)^2`.

All `F_j` with `j>=1` are positive for `D,P>0`: the initial values are `1,D`, and the recurrence has positive terms. If `D>=1`, the step from `F_j` to `F_{j+1}` is strict for `j>=2`, because `P F_{j-1}>0`. This covers the entire interval from `o` to `e`, so `F_e=F_o` forces `0<D<1`. Rationality then supplies coprime positive integers `p<q`, `q>=2`.

The coefficient formula follows by induction using Pascal's identity. Its last nonzero term is `(e/2)D P^((e-2)/2)` for even `e`, and `P^((o-1)/2)` for odd `o`. In particular `F_o` is monic in the elimination variable, and `m=(e-2)/2>=n=(o-1)/2`. These degree statements are over the rational-function coefficient field, before specialization.

### 3. Unit resultant, including roots and scaling (lines 114-142)

For every nontrivial `o`th root of unity `zeta`, `1+zeta` is nonzero because `o` is odd. The proposed two characteristic roots have sum 1 and product `-P_zeta`, so their difference-of-powers formula vanishes at index `o`. A fixed nonzero value of `P_zeta` gives the quadratic

`P_zeta*zeta^2+(2P_zeta+1)*zeta+P_zeta=0`.

Its two roots are reciprocal. Repeated roots would have `zeta=zeta^-1`, hence `zeta=+1` or `-1`, both excluded here. Thus precisely inverse pairs give the same parameter, producing `n` distinct roots and exhausting the monic degree-`n` polynomial `F_o(1,P)`.

The displayed evaluation of `F_e` follows by dividing the difference of `e`th powers of those characteristic roots by their difference. Coprimality permutes all nontrivial `o`th roots under the `e`th-power map, so the product of the numerator ratios is 1. Evaluation of `(T^o-1)/(T-1)` at `-1` gives the other product `prod(1+zeta)=1`, with no missing minus sign because `o-1` is even. Hence the product over all these roots is 1. It is the square of the product over the `n` distinct parameters; that product is therefore `+1` or `-1`. Monicity and the root-product definition of the resultant give a unit, up to the irrelevant order sign.

To verify the scaling exponent explicitly, use

`Res_Z(f(cZ),g(cZ)) = c^(mn) Res_P(f(P),g(P))`

for degrees `m,n`, together with homogeneity in the two polynomial coefficient lists. For `c=D^2`, the exponent remaining after the variable-change factor is

`n(e-1)+m(o-1)-2mn = n(e-1) = (e-1)(o-1)/2`.

This is an identity over `Q(D)` and therefore a polynomial identity. It does not assume `D` is an algebraic integer or divide by its later specialized value.

### 4. Elimination, weighted support, and the constant term (lines 146-204)

`A=F_e-F_o` has degree `m` in `P` over `Q(D,N)`, and `B` has degree `o` and leading coefficient 4. When `e=o+1`, `m=n` and the leading coefficient of `A` is `(e/2)D-1`, still a nonzero polynomial. A numerical value of `D` may make this coefficient vanish. This does not invalidate the necessary common-root implication for the generic Sylvester determinant: after specialization a common finite root still gives a nonzero evaluation vector in its null space. The proof never infers existence of a root from a vanishing resultant, so spurious zeros would be harmless.

For the weighted bound, substituting `P=t^2 Z` in `A(tD,P)` extracts `t^(e-1)` and leaves `F_e-t^-delta F_o`; the analogous substitution in `B(tD,t^(2o)N,P)` extracts `t^(2o)`. The variable-change factor is `t^(2mo)`. Thus the total exponent left outside the resultant is

`o(e-1)+2om-2mo = o(e-1)=L`.

The remaining determinant is polynomial in `t^-delta`, with coefficients independent of `t`; its highest possible `t` exponent is zero. Comparing with the ordinary polynomial `R(tD,t^(2o)N)` establishes `i+2oj<=L` for every supported `D^i N^j`. The Laurent-field calculation is legitimate; no polynomiality of negative powers is claimed.

For `N=0`, multiplicativity splits the second argument into `D^2+4P` and `F_o^2`. The identity `Res(A,F_o)=Res(F_e,F_o)` is valid here because `F_o` is monic, `deg(A)=deg(F_e)=m` generically, and `A` and `F_e` have identical values at every root of `F_o`. Its square contributes `D^((e-1)(o-1))`.

At `P=-D^2/4`, substitution in the recurrence itself verifies `F_j=j(D/2)^(j-1)` (so there is no illicit division by coincident characteristic roots). The linear-factor root formula contributes, up to sign,

`4^m A(D,-D^2/4) = D^(o-1)[(e/2)D^delta-2^(delta-1)o]`.

The product is exactly the claimed constant-in-`N` term. It is nonzero as a polynomial: the bracket has a nonzero constant and a distinct positive-degree term. All these identities are formed before specializing coefficient values. I found no erroneous degree, omitted leading coefficient, or unsupported specialization inference.

### 5. Denominators and the first arithmetic branch (lines 208-245)

Since `R` has integer coefficients and supported weights at most `L`, every term with `N` exponent `j>=1`, after substitution and multiplication by `q^L`, is an integer multiple of `q^(2oj)` and hence of `q^(2o)`. Integrality of `N` is essential and is available from the official statement. Furthermore,

`e(o-1)+delta = L`.

Thus the constant-in-`N` part becomes exactly `+/-p^(e(o-1)) H`, with the candidate's integer `H`. Coprimality cancels the entire power of `p`, for arbitrary composite as well as prime `q`. The divisibility (17) follows.

When `delta<2o`, reduction modulo `q^delta` gives `q^delta | e/2`. Positivity then gives `e>=2q^delta>=2^(delta+1)`. The elementary induction `2^(h+1)>=3h` implies `o=e-delta>=2delta`. In particular `e/2<o`. Since `2^(delta-1)o>=o` and `p^delta<q^delta`, `H` is strictly negative; since its first summand is positive, `-H<2^(delta-1)o q^delta`. It cannot vanish. Divisibility therefore supplies a positive multiple of `q^(2o)` below that strict upper bound.

The resulting inequality is `q^(2o-delta)<2^(delta-1)o`. The exponent `2o-delta` is positive in this branch, so replacing `q` by its lower bound 2 is justified. After division this gives `2^(2o-2delta+1)<o`. But `o>=2delta` makes the left side at least `2^(o+1)>o`. Every inequality direction, strictness, and nonzero assertion needed in this contradiction is valid.

### 6. Second arithmetic branch and real contradiction (lines 247-290)

When `delta>=2o`, the second summand of `H` is a multiple of `q^(2o)`. Coprimality with `p` now yields `q^(2o) | e/2`, hence `e>=2q^(2o)>=2^(2o+1)`.

The original real equality and `U>V>0` imply `U^o>sqrt(N)>=sqrt(2)`. The factorization of `U^e-V^e` contains `D U^(e-1)` and at least one more positive term. Hence

`1/q <= D < 2 U^(-(delta-1)) < 2^(1-(delta-1)/(2o))`.

The final inequality is strict because `delta-1>0` in this branch. Taking reciprocals and then the positive integer power `2o` gives `q^(2o)>2^(delta-1-2o)`. Combining with `e/2>=q^(2o)` gives exactly `e>2^(e-3o)`, including the factor of 2 in the exponent conversion.

For integer `o>=3`, `2^(2o+1)>=6o`, so `e>=6o`. Therefore `e-3o>=e/2`; since `e` is even and at least 4, `2^(e/2)>=e`. This contradicts the preceding strict inequality. The proof does not discard a possible equality endpoint.

### 7. Exhaustion and sufficiency (lines 294-296)

Every off-diagonal solution was reduced to a coprime pair with the described signs and parity. The only remaining pair is `(e,o)=(2,1)`, so the original exponents are `(2d,d)` in either order with `d` odd. There is no missed common even factor: opposite parity excluded that before reduction. For each positive odd `d`, the negative real `d`th root of the published witness exists and its powers at `d,2d` have the required rational shifts. The published diagonal family covers all remaining listed pairs. Positive exponents, both orderings, `d=1`, and all nonsquare positive integers are covered.

## Independent exact evidence and reproducibility

These checks supplement the preceding unrestricted derivations and are not proofs of them. Files are disjoint R1 evidence:

- `reviews/review-1-checks.py`: standard-library Python implementation of the recurrence and a Sylvester determinant by subset expansion, with sparse exact integer polynomials in `D,N`. SHA-256 `c452fa780081026f360c2ee4e3cd845e299cbbbe6f6584972954180b8e0b9d70`.
- `reviews/review-1-checks.log`: preserved checkpoints and complete output. SHA-256 `4c9463e580a3a2125e0ac0acaed768d6c1698e13e99d5d3c6f2581871dbfbfe8`.

Run from the repository root:

```text
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2023-B4/reviews/review-1-checks.py
```

The launcher used child PID `10030`, an explicit 55-second subprocess timeout, incremental flushed checkpoints, and targeted child-only cleanup on timeout. The run completed normally, exit code 0, in under one second; no incomplete search or cleanup was needed. No native CAS was invoked, no installation was performed, and no unrelated process was touched.

Results:

1. All eight pairs `(4,3),(6,5),(8,3),(8,5),(8,7),(10,3),(10,7),(10,9)` passed exact symbolic checks of recurrence degrees and leading coefficients, the unit resultant, the weighted support bound, and the constant-in-`N` identity up to sign.
2. The degree-drop specialization `(e,o,D,N)=(4,3,1/2,0)` gave resultant `1/128`, confirming that a leading coefficient drop alone need not force vanishing and must not be inverted. The candidate uses only the valid necessary implication.
3. The modular scan checked 138,369 coprime-parameter cases with even `4<=e<=256`, odd `3<=o<e`, `gcd(e,o)=1`, `2<=q<=8`, `1<=p<q`, `gcd(p,q)=1`. No first-branch divisibility survivor occurred. The only second-branch survivors were `(e,o,p,q)=(128,3,1,2),(256,3,1,2)`; both failed the derived real inequality. No combined survivor occurred. This explicitly shows why denominator divisibility alone is not the final contradiction.

Dependencies: bundled Python `3.12.14`; the check script uses only its standard library. Source inspection additionally used `pypdf 6.10.0` and Poppler `pdftoppm 26.05.0`. An attempted `import sympy` in the bundled interpreter and `/usr/local/bin/python3` returned `ModuleNotFoundError`; the independent checks consequently avoid SymPy entirely.

Source-inspection commands included `shasum -a 256` for the fingerprints above, `pypdf.PdfReader` extraction of printed pp. 15-16 and a short excerpt beginning with the preliminary result's statement, and:

```text
pdftoppm -f 2 -l 2 -r 110 -png -singlefile .cache/official/2023-paper_b.pdf /private/tmp/2023-review-1-statement
pdftoppm -f 15 -l 16 -r 110 -png .cache/official/2023-solutions.pdf /private/tmp/2023-review-1-published
```

The rendered relevant pages were visually inspected. Intermediate renders remain outside Git under `/private/tmp`. No third-party paper was copied into Git.

Authoritative account-wide telemetry was checked at review start and at its concluding audit: the 10080-minute weekly window increased from 2% to 3% used, with reset Unix time `1792745187`. No separately billed API was used.

## Objections and optional author clarifications

**Substantive objections: none identified in the assigned version.** In particular, the possible specialized leading-degree drop, a negative witness, non-squarefree `N`, composite denominators, and both exponent-order/parity cases do not produce a gap.

The following are optional exposition improvements, not blockers and not independent mathematical defects:

- **R1-C1, lines 142 and 173-182:** add the two explicit exponent calculations given in this report, or state the variable-change and scalar resultant formulas. This makes the two scaling identities easier to audit without reconstructing their factors.
- **R1-C2, line 191:** add that the replacement of `F_e-F_o` by `F_e` inside the resultant with `F_o` is performed generically and follows from monicity/root evaluation. This guards readers against overgeneralizing an additive resultant rule when degrees drop after specialization.

I edited only this report and the two R1 evidence files. I did not alter the candidate or the shared issue log and made no Git commit or push.
