# Independent adversarial review R1: fixed-factor family v1

Initial blind report completed 2026-10-16. This reviewer did not construct
the candidate and reconstructed its whole mathematical argument. No
other review, shared issue log, or shared review conclusion was read
before completing this report. The constructor's certificate script and
its mathematical output were not used to derive the checks below; their
bytes were read only to verify the frozen manifest hashes.

Requested reviewer settings: `gpt-6.1-sol`, `max` reasoning, as specified
in the launch request. No verified effective-setting readback is
available. The authoritative account-wide weekly telemetry read during
this audit reported 4% used in the 10080-minute window, reset timestamp
1792745187. No separately billed API or subagent was used.

## Verdict and exact scope

**R1 audit passes for the stated partial result.** I found no substantive
mathematical objection to the frozen v1 claim

\[
 \phi_{13}\mid\phi_{(64\,16^m+1)/5}\quad(m\geq0)
 \qquad\text{in }\mathbb F_2[x,y,z].
\]

For every integer `m>=1`, the argument supplies two nonconstant factors
over `F2` of the quotient prescribed by B4(b), and hence suitable integer
polynomials after coefficient lifting. At `m=0` the supplied cofactor
is 1; this argument makes no determination of the B4(b) status of
`n=13`. It does not classify exponents outside this family or establish
novelty. It does not use the preliminary Gold-family result.

This is one independent review, not a promotion of the candidate's
repository status. The coordinator must still receive the second
independent audit and resolve any substantive objections before any
promotion. The result remains a partial result toward B4(b).

## Frozen artifact and official target

- Reviewed proof: `proofs/fixed-factor-family-v1.md`, SHA256
  `1a1a8e6513d175cc075e13c6353371a9ece47e0c37d6781b16999a3544f9e376`.
- Every artifact hash in
  `notes/fixed-factor-family-v1-manifest.json` matched on reading.
- The cached [official 2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf),
  page 2, was independently text-extracted and visually inspected.
  Cached PDF SHA256:
  `1401f21218ad4c387c4d537ed8fd7de119b376cba52957ef788c772dc5ab4ddc`.
- The normalized `statement.md` hash is
  `60244f7752634772adb434efbdb41a63fb02029dc3be4238f3718c6e5ec84e5f`.

The original target is positive odd integer `n`, equality of every
coefficient modulo 2, integer `g,h`, with neither reduction constant.
The candidate uses precisely this coefficientwise interpretation. An
identity merely of functions on `F2^3` would not suffice and is nowhere
used. The initial blind audit did not investigate any other annual
problem or any preliminary proof.

## Whole-argument reconstruction

### 1. The generating function and independent invariants

Let `w=x+y+z` in the polynomial ring of characteristic two. The
elementary symmetric functions of the four-element list `x,y,z,w` are
`0,Q,R,D` as stated. In particular,

\[
 e_2=xy+xz+yz+w^2=Q,
 \qquad e_3=xyz+w(xy+xz+yz)=R.
\]

The last expression expands to the same six degree-three monomials as
`(x+y)(y+z)(z+x)`. No distinct-root assumption is present. Thus the
polynomial `E(t)=1+Qt^2+Rt^3+Dt^4` has unit constant term. The formal
product rule gives `E'/E=sum a/(1+at)`, with `E'=Rt^2` in characteristic
two. Expanding each reciprocal and multiplying by `t` proves

\[
 \sum_{n\geq1}f_n t^n=\frac{Rt^3}{E(t)}.
\]

All steps are valid in the formal series ring; they require no numeric
specialization or convergence. For `n>=3`, coefficient extraction
therefore proves polynomial divisibility by the nonzero `R`. The
quotient is unique because the coefficient ring is an integral domain.

The identity `1/E=E/E^2` is valid since `E` is a unit. Its denominator
has only even powers of `t`, so its even part has numerator
`1+Qt^2+Dt^4`. Substituting `s=t^2` proves equation (3), including its
index `phi_(2j+3)`. Replacing `Q,R^2,D` by independent `q,u,d` creates
the valid universal polynomial sequence `P_j`. Its recurrence is

\[
 P_j=q^2P_{j-2}+uP_{j-3}+d^2P_{j-4}
\]

after accounting for the three initial numerator terms and treating
negative indices as zero. In particular this gives
`P5=q^5+q*d^2+u*d=A`. The grading has weights `2,6,4`, and every term
of `P_j` has weight `2j`. The proof does not assume algebraic
independence of the eventual substituted invariants.

Independent exact calculations checked the elementary symmetric
expressions and `R*A(Q,R^2,D)=f13` directly in `F2[x,y,z]`. The latter
`phi13` has 42 nonzero monomials, all of total degree 10.

### 2. Localization and normalization

Write `S=F2[q,u,d]` and invert `q,d`. In this localization, `A=0` is
equivalent to

\[
 u=q^5/d+qd.
\]

Because the coefficient of `u` is a unit there, elimination is an
isomorphism with `F2[q,q^-1,d,d^-1]`, rather than merely a substitution
on some points. Introducing `b=d/q^2` gives the Laurent ring in
independent `q,b`, with `d=q^2b` and `u=q^3(b+b^-1)`. With `s=z/q`,
the normalized series is exactly the displayed `F(z,b)`, and its
`z^j` coefficient is the quotient image of `q^-j P_j`.

Both series denominators have constant term 1. Consequently their
formal inverses and coefficient maps commute with these coefficient
ring homomorphisms. The Laurent ring `F2[b,b^-1]` embeds into
`E=F2(b)`, so a zero Laurent coefficient established in `E` is zero
in the Laurent ring itself. This is an injective coefficient-ring
embedding, not a test on the finitely many points of a finite field.

### 3. Cartier operators and the three symbolic identities

The operator in the proof is explicitly **E-linear coefficient
selection**. For arbitrary formal series `H,G`, grouping the indices
in their coefficient convolution proves

\[
 C_r(H(z)G(z^{16}))=C_r(H(z))G(z).
\]

For example, the coefficient on either side at index `i` is the sum
over `0<=k<=i` of `h_(16(i-k)+r) g_k`. This derivation does not
require `E` to be perfect and takes no sixteenth roots.

The true Frobenius operation is confined to
`K(z,b)^16=K(z^16,b^16)`. Multiplying `P/K` by `K^15/K^15` and using
the preceding convolution identity gives equation (8), with
denominator `K(z,b^16)`. The numerator degree is at most `3+15*4=63`,
so selecting residues 5 or 6 leaves degree at most 3. Thus there are
only four coefficient identities per displayed Cartier identity to
check; no unexamined higher terms remain.

I independently expanded `K^15` by the integer multinomial theorem
applied to its **five** monomials

\[
 1,\ z^2,\ bz^3,\ b^{-1}z^3,\ b^2z^4.
\]

For each composition `(a,b0,c,d0,e)` of 15, its coefficient before
parity reduction is `15!/(a! b0! c! d0! e!)`, its `z` exponent is
`2*b0+3*c+3*d0+4*e`, and its Laurent `b` exponent is `c-d0+2*e`.
All 3876 compositions were included; 625 have odd multinomial
coefficient. After cancellation, the full symbolic `K^15` has 361
monomials. This algorithm uses neither the author's repeated
multiplication nor the author's binary product for `K^15`.

Multiplication by each specified numerator, followed by residue
selection, gave exactly:

| Identity | Constant | coefficient of z | coefficient of z^2 | coefficient of z^3 |
|---|---|---|---|---|
| (9) | 0 | L+M | L+J | b^16(L+J) |
| (10) | 0 | L | L | b^16 L |
| (11) | 0 | M | J | b^16 J |

The evidence file retains all 361 monomials and every selected
coefficient as complete Laurent exponent sets, as well as their
expected sets. Equality was checked symbolically, with `b`
indeterminate. These are general finite algebra identities, rather
than samples of `b` or a bounded search for exponents `n`.

### 4. Preserved span and unrestricted digit induction

The first identity places `C5 F` in `V(b^16)`. For any nonzero
`c=b^(16^k)` in `E`, substitution `b=c` in the Laurent identities is
a well-defined ring homomorphism. Equations (10),(11) map the two
numerator generators of `V(c)` into the stated generators of
`V(c^16)`. E-linearity proves the same for any `alpha,beta` in `E`.
The resulting coefficient vector is exactly

\[
 (\alpha L(c)+\beta M(c),\ \alpha L(c)+\beta J(c)).
\]

In particular, the outside scalars remain `alpha,beta`. Their
sixteenth powers would give a different operator. As an extra exact
discriminator, the independent script checks the outside scalar
`alpha=b`: the selected numerator is `b` times that in (10), and
differs symbolically from `b^16` times that numerator.

No invertibility, independence of the two span generators, or
nonvanishing of `L,M,J` is assumed. Therefore degenerate values or
rank loss cannot break this containment argument. All members of
`V(c)` have zero constant term because their numerator does and their
denominator has constant term 1.

Consequently induction on **every** nonnegative integer `m` gives

\[
 T_m=C_6^m C_5F\in V(b^{16^{m+1}}),\qquad [z^0]T_m=0.
\]

For the digit order, if `G=sum a_j z^j`, then `C6 C5 G` has
coefficient `a_(256i+101)` at index `i`; extraction starts at the
least significant digit. A direct induction on the number of
selections gives

\[
 C_6^m C_5F=
 \sum_{a\geq0}[z^{16^{m+1}a+5+6\cdot16+\cdots+6\cdot16^m}]F\ z^a.
\]

The selected index is
`j_m=5+6*16+...+6*16^m=(32*16^m-7)/5`. Thus `[z^j_m]F=0` for all
`m>=0`. This is the unrestricted argument; no extrapolation from
the bounded coefficient checks is needed or permissible.

### 5. Saturation and descent to the unlocalized ring

In the coefficient UFD `F2[q,d]`, the two coefficients of the linear
polynomial `A=d*u+q*(q^4+d^2)` have gcd 1. Indeed, a common factor
with `d` would divide `q^5`, which is coprime to the independent
variable `d`. This checks the primitivity hypothesis of Gauss's
lemma. Over `F2(q,d)`, `A` has degree one in `u` and hence is
irreducible. Gauss's lemma therefore makes it irreducible in `S`;
the polynomial ring `S` is a UFD, so this irreducible element is
prime. Degree in `u` shows `A` divides neither nonzero `q` nor `d`.

Zero in the normalized quotient means `P_(j_m)` is in `A U`.
Clearing finitely many inverted powers yields
`A | q^a d^b P_(j_m)` in `S`. Primality and the two exclusions then
imply `A | P_(j_m)`. This rigorously recovers the loci discarded
when `q,d` were inverted. The proof is not trying to infer a global
divisibility statement from generic numeric points.

Specializations such as `q=0` or `d=0` may themselves make the
specialized `A` reducible or change its degree in `u`. They do not
invalidate the primitivity or primeness statement in the independent
ring `S`. I found no saturation gap.

### 6. Substitution, nonzero factors, and integer lifting

Writing `P_(j_m)=A B_m`, weighted homogeneity forces `B_m` to have
weight `2j_m-10`: wrong-weight components cannot survive multiplication
by the nonzero homogeneous `A` in an integral domain. Substitution
gives `phi_(2j_m+3)=phi13 B_m(Q,R^2,D)` with no need for the
substitution to be injective.

For every odd `n>1`, the mixed monomial `x^(n-1)y` in the original
`f_n` has coefficient `n=1` in `F2`. Its exponent pattern is mixed,
so none of the three pure powers contributes. Hence `f_n` is
nonzero, and its homogeneous quotient by the nonzero degree-three
`R` is nonzero of degree `n-3`. In particular `phi13` has degree
10. The displayed product then ensures that the substituted cofactor
cannot vanish. Every one of its terms has total degree `n-13`, so
its nonzero total degree is exactly that value; cancellation cannot
produce a lower degree from a homogeneous polynomial.

Here `2j_m+3=(64*16^m+1)/5`. This is a positive integer because
`16=1 mod5` and `64=-1 mod5`; it is odd because its numerator and
divisor are odd. For `m>=1`, it is at least 205, so the two degrees
are 10 and at least 192. Both reductions are therefore nonconstant.
Lifting their finitely many coefficients to integers 0 or 1 gives
the coefficientwise congruence required in the official question.

At `m=0`, `P5=A` and the cofactor is exactly 1, as the candidate
explicitly acknowledges. The unrelated boundaries `n=1` (zero
numerator) and `n=3` (unit quotient) do not enter the family. The
normalized statement's exclusion of them is also consistent with
the official convention: in the domain `F2[x,y,z]` a product of
two nonconstant polynomials and nonzero `R` cannot be zero or have
unit quotient.

## Adversarial checks and issue disposition

| Potential failure | Audit result |
|---|---|
| Equality of polynomial functions substituted for coefficients | No; all rings and coefficient operations remain symbolic. |
| Repeated elements of `x,y,z,x+y+z` invalidate the log derivative | No distinctness hypothesis is used. |
| Odd/even extraction or the `n=2j+3` index is shifted | Reconstruction agrees with the stated formulas. |
| `E=F2(b)` incorrectly assumed perfect; outside scalars Frobenius-twisted | Neither occurs; E-linearity is explicit and independently distinguished. |
| The Cartier identities were tested only at finitely many `b` | They were verified as full Laurent-polynomial identities. |
| The induction is inferred from finitely many `m` | The preserved span and ordered digit extraction prove it for all `m>=0`. |
| Inverting `q,d` loses a component of `A` | Primitivity, primality, and saturation restore full polynomial divisibility. |
| Substitution sends a claimed factor to zero or a constant | Original numerator nonzero and positive homogeneous degrees rule this out for `m>=1`. |
| Extension-field factors are mistaken for F2 factors | `A,B_m` and their substitutions lie in F2 polynomial rings throughout. |
| `m=0` is silently counted as two nonconstant factors | Explicitly excluded from that conclusion. |
| Partial family or unread literature is promoted to a classification | The candidate makes neither inference. |

**Substantive objections requiring author repair: none found.**
There are no unresolved proof issues from R1. The outstanding
identification of Férard's exact family is a literature/attribution
task, not a premise needed by the proof. It must remain labelled
unverified until the full theorem is read.

## Attribution check

I independently text-extracted and visually checked section 6, printed
page 18, of Hernando--McGuire's
[arXiv:0903.2016v4](https://arxiv.org/pdf/0903.2016). The cached PDF
SHA256 is
`bc9389858756658a7a2769a74ebb40b4df05523ddfe24a4639cd7d79ef31df16`.
It explicitly reports an F2 factorization at `t=205` and prints a
degree-ten factor. I transcribed its 42 monomials independently of
the constructor's certificate and verified that it equals
`phi13(x,y,1)`. Attribution of that case is justified. No APN or
absolute-irreducibility theorem from that paper is needed here.

The cached original
[Férard publisher abstract](https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497)
was also checked directly; its hash matches the source-access note.
It discusses `t=5 mod8`, divisibility by `phi13`, and an infinite
family. The v1 text accurately treats this as an attribution lead
and explicitly declines a novelty claim. I did not read or infer
the unavailable full theorem. The abstract's absolute-irreducibility
language is not used as a substitute for factorization over F2.

## Reproduction, evidence, and limits

The independent standard-library script is
`reviews/family-review-1-independent-check.py`, with complete output in
`family-review-1-independent-check.json` and flushed checkpoints in
`family-review-1-output.txt`. The run record is
`family-review-1-run.json`; standard error is
`family-review-1-stderr.txt` (empty on this successful run).

Command from the repository root:

```sh
.venv/bin/python -u problems/2024-B4/reviews/family-review-1-independent-check.py
```

It used Python 3.12.14 and no third-party modules. The recorded run
was supervised as dedicated child PID 14260 with an explicit
40-second timeout, completed with return code 0, and took about
0.26 seconds including supervision. No native CAS, factorization
oracle, install, long search, process-wide cleanup, commit, or push
was used. The script's source and evidence remain available for
independent rerunning.

The following extra calculations are **bounded evidence only**:

- The direct Laurent recurrence from `K F=1+z+bz^2` gave zero
  coefficients at `j=5,101,1637`, corresponding to `n=13,205,3277`.
- The independent `P_j` recurrence through `j=101` gave exact
  polynomial division `P101/A` with zero remainder. Its cofactor
  has 248 monomials, all of weight 192.
- Direct sparse division of the original polynomial `f205` by
  the original `f13`, followed by a full multiplication check,
  gave zero remainder and a nonzero degree-192 cofactor with
  2709 monomials. Cancelling the common nonzero `R` confirms
  `phi13 | phi205` in this case without a factorization oracle.
- Arithmetic/digit examples through `m=12` were checked. They are
  evidence for implementation consistency; the formulas and their
  unbounded meaning are proved in the reconstruction above.

The symbolic Laurent identities are general identities, as explained
above; the bound on their finite expansions is a degree bound, not a
restriction on the theorem's parameter `m`. The separate bounded
calculations do not replace the span/digit induction.

Executed source-verification commands used the bundled Poppler
`pdftotext` and `pdftoppm` executables under
`/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/poppler/bin/`:

```sh
pdftotext -f 2 -l 2 -layout .cache/official/2024-paper_b.pdf -
pdftoppm -f 2 -l 2 -r 120 -png -singlefile .cache/official/2024-paper_b.pdf problems/2024-B4/reviews/family-review-1-official-page2
pdftotext -layout .cache/literature/2024/cited-3e7f3cb84c20c6b1.pdf -
pdftoppm -f 18 -l 18 -r 120 -png -singlefile .cache/literature/2024/cited-3e7f3cb84c20c6b1.pdf problems/2024-B4/reviews/family-review-1-hm-page18
```

These commands inspected the original statement and the existing
attribution source. They did not investigate the other printed
competition problems or use the surrounding paper's theorems to
establish this family. No full third-party paper was added to tracked
source material by this reviewer.
