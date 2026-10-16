# Independent R1 audit: degree-20 three-rational-witness candidate

Audit date: 2026-10-16 UTC (2026-10-17 in Brisbane).
Reviewer: independent `review_2021_three_witness_r1` agent; not a constructor.
Requested settings: `gpt-6.1-sol`, `max`. No effective-setting readback was
available; these requested settings are not asserted to be verified settings.

**Disposition: independent audit complete; no unresolved substantive objection
to T1, T2, or T3, with the frozen prior packets as the stated dependencies.**
I recommend accepting the three precisely scoped claims after the other blind
audit and the coordinator's promotion decision. I do not promote this packet,
assert a full degree-20 solution, or claim a solution of B4(b).

## Frozen object, scope, and independence

The reviewed note is
`notes/coordinator-three-rational-witnesses-v1.md`, SHA-256
`be91345a8511338d55f30b140ee2555698c21d0e341efe29fe2536bca4fffbda`.
The candidate manifest has SHA-256
`b01f42be62a8019fc6af3d6042434254e8f88fe6060dba6e454babf9eaa0cd78`.
All 50 manifest artifacts matched their frozen byte counts and hashes.

Only 2021 B4(b) is addressed. I checked the official part-(b) wording against
the cached official Paper B, page 2; I did not solve or reproduce the
preliminary part. The mathematical hypothesis remains a polynomial over Q
with a common **rational** root for every derivative order 1 through 19. Its
other roots may be irrational or nonreal.

I read the three supplied mathematical dependency notes, their relevant
primary sources, the new candidate, and its construction data. I read no other
review report, peer conclusion, shared issue log, status file, or research log.
The only other review-named JSON used was the explicitly permitted dependency
`reviews/newton-review-1-extension-result.json`; after independently deriving
the masks, I extracted only its
`combined_with_prior_j17_exclusion_masks` list. Its top-level key names were
printed to locate that data field; no prior reviewer conclusion was used.

Before opening raw certificates or examining constructor serialization, I
wrote and ran `three-witness-review-1-independent.py`. Its pre-raw and full-run
SHA-256 are both
`ed98ed514ac6dffa20e3c5779d7851437003326992f0619018f1837147386464`.
The code uses ordinary Hasse coefficients rather than the constructor's
normalized-a recurrence. No constructor module was imported or executed.
After this freeze I examined constructor serialization/traversal lines only
to compare the same ordered streams. The independent code needed no change.

The old J=17 29,928-family certificate and the old degeneration packet are
accepted separately reviewed inputs, as specified in the assignment. This
audit reconstructs their mathematical use; it is not a fresh rerun of every
old certificate or an adoption of an old reviewer conclusion. The complete
1,493,024-family certificate for this new candidate was independently
regenerated and checked in full, not sampled.

## Reconstruction of the mathematical reduction for T1

Assume there is a nontrivial f with a covering set containing at most three
rational roots. A one-value cover gives a pure power; the two-value cover is
excluded by the precisely relevant recycled-root obstruction. Select the
first-derivative witness **within the hypothesized cover**, translate it to
zero, and use the center as the second affine normalization point. The center
belongs to every cover because H_19(f) is linear. It is simple, so it is
different from the selected double root. Both points are rational; the
resulting monic affine normalization is rational and leaves a cover
{0,1,u}, with u rational and different from 0 and 1.

The CLO normalization gives c_20=1, c_19=-20, c_0=c_1=0,
c_(20-j)=C(20,j)a_j with a_j in Z_(19), and the center 1 as the only
valuation-zero root. Every other nonzero root has positive valuation. In
particular a rational noncenter witness has positive **integral** valuation;
this is not asserted for algebraic roots. These facts apply after the rational
affine map: the auxiliary minimum-valuation scaling in CLO can be followed by
scaling its unit center to 1, and the composite scaling is precisely by the
original rational center minus the translated rational double root.

For j=2,...,18, let a center bit mean that 1 is chosen whenever it is an
available common root. At a noncenter bit a witness reduces to zero modulo
19, so D_j(w)=0 forces a_j=0 modulo 19. At a center bit D_j(1)=0 gives the
stated residue equation. Since each C(20,j) has valuation exactly one, f(1)=0
divided by 19 gives the final necessary residue equation. J exists, since
otherwise this equation reduces to -1=0. Importantly, J is the largest
**unit coefficient index**, not the largest center-bit index; a center
equation can produce a zero residue.

The previously established Newton edge applies at J=18,17,16,15 because all
are at least 10. For h=20-J its line is (19-t)/(J-1). Every coefficient
point other than its endpoints (h,1),(19,0) lies strictly above that line:
middle points to the left have valuation at least 2 and line height below
2, and those to the right have valuation at least 1 and line height below
1. The edge therefore accounts for J-1 roots, **with multiplicity**, of
valuation 1/(J-1), unavailable as rational witnesses. The remaining count
gives at most h-m+2 distinct rational roots. This excludes J=18 using
the two-witness obstruction. The accepted J=17 compatibility result removes
J=17 completely; it is not replaced here by merely counting roots.

I reconstructed the mathematical center conditions used at J=16 and J=15.
For the width-one lemma, dividing by the upper endpoint term and multiplying
H_k(f)(u) by u^k reduces to
C(i+1,k)-C(i,k)=C(i,k-1), a unit for i<19 and 1<=k<=i+1.
This handles the low-order derivative witnesses in the J=16 argument.
In its equal-valuation quadratic case, subtracting F(alpha)=0 from
H_2(F)(alpha)=0 yields 2B+5C alpha=0. The two nonzero initial roots have
H_3 values -3B/5 and -7B/5, which are nonzero in characteristic 19. Thus
H_2(1)=0 or H_3(1)=0 is legitimately forced. No exceptional prime among
2,3,5,7 is being treated as a unit at itself.

For J=15, the degeneration argument chooses the smallest remaining small
root valuation nu, not a fractional long-edge valuation. Its supporting
line makes beta^(-1)f(alpha T) integral, with monic reduction of degree
h=5, divisible by T^m, and with a nonzero lower coefficient. This reduction
is nontrivial. If the center witnessed none of H_2,H_3,H_4, then each
rational witness of H_1 through H_4 lies at valuation at least nu, or is
zero. Dividing by alpha gives integral witnesses, and Hasse differentiation
commutes with reduction. A nontrivial degree-5 CA polynomial in
characteristic 19 would result, contrary to the cited good-prime input.
The argument also uses simplicity to exclude the center for H_1. Thus the
three-way center disjunction is applicable. No good-prime assertion at
h=6 or h=7 is needed. For J below 10, this audit uses none of these edge
claims; those families are included in the exact exhaustion.

I independently enumerated all 131,072 choices using ordinary coefficients
modulo 19^2. At a center bit, the unknown c_l is minus the known higher
terms of H_l(f)(1). At a noncenter bit it is zero modulo 19^2: each higher
middle coefficient already contains 19, and for t=19,20 the relevant
binomial coefficient contains 19 as well. Multiplication by a noncenter
witness supplies the additional factor. This independently reproduces the
normalized residue filter without importing a constructor helper.

There are exactly 6,680 congruence survivors. Their J histogram is
6:1, 7:1, 8:3, 9:5, 10:26, 11:32, 12:101, 13:131, 14:315,
15:461, 16:887, 17:1674, 18:3043. Removing J=18,J=17 and applying the
specified disjunctions leaves exactly 772 masks: 615 with J<=14, 69
with J=15, and 88 with J=16. The independently obtained ordered list
equals the permitted dependency list exactly. The dependency data file's
SHA-256 matches the frozen
`96f61ad6b173c1fd40bfc2dff3f87c44b616db87bd6db0a0ca77b1a019bee803`.

The filtering keeps a superset: a noncenter bit need not enforce failure at
the center. This cannot lose the canonical mask of an actual f. Canonical
choice is needed when applying a forced-center disjunction, and every actual
cover does supply that canonical choice.

## Exact families and complete certificate audit

For each retained mask I independently traverse all choices 0 or U at every
noncenter position. In ordinary coefficients, with l running down from 18
to 2, I construct

    c_l(U) = -sum_(t=l+1)^20 C(t,l)c_t(U) w_l^(t-l).

This is the exact H_l(f)(w_l)=0 equation: the unknown coefficient has
coefficient one. Its specialization at an actual u is forced inductively.
The elementary identity
C(t,l)C(20,t)=C(20,l)C(20-l,t-l) also confirms equivalence to the
normalized derivative equation. Every generated coefficient was checked
to be divisible coefficientwise by C(20,l).

The fixed c_0=c_1=0 impose f(0)=H_1(f)(0)=0, and
H_19(f)=20(x-1). For the remaining root conditions I compute directly
P=sum c_l=f_U(1) and Q=sum c_l U^l=f_U(U). The degree bound 20 and the
polynomial definitions are preserved even when leading symbolic terms
cancel. Repetition of a witness at several positions and unused U choices
are included. Actual u is distinct from 0 and 1, but including those
degenerate specializations makes a larger harmless family.

For every mask the checker verified that the generated U masks are all
distinct, are supported only on its noncenter positions, and have the
full required count 2^(17-popcount(mask)). The raw data have the same
unique keys and exactly that count in every group. There are no leftover
groups or extra records. Thus the total 1,493,024 is a coverage proof by
finite combinatorics, not merely a matching grand total.

For every nonconstant pair, I independently tested degree retention and
ran a fresh Euclidean algorithm in the finite field. I tried the listed
primes in order, then 131. All six primes were also checked by trial
division. The complete result is:

| Certificate | Independently verified families |
|---|---:|
| Nonzero constant P | 772 |
| 101 | 1,416,728 |
| 103 | 71,108 |
| 107 | 4,109 |
| 109 | 297 |
| 127 | 9 |
| 131 | 1 |

Every stored nonconstant row's two degrees and two leading residues equal
the independently regenerated values. Each stored constant equals the
independent nonzero P. The initial stream's single sentinel is exactly
[6436,24785,-1]; the checker regenerated both integer polynomials and
found the first additional certificate at 131, with degrees (16,20),
leading residues (8,102), and gcd degree zero. Both polynomials agree
coefficient for coefficient with the retained unresolved pair, and the
separate resolver JSON agrees. The initial five-prime incompleteness is
preserved, not silently removed.

The integer polynomial stream, in compact JSON [mask,U_mask,P,Q] order,
has SHA-256
`aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad`.
The uncompressed raw certificate stream has SHA-256
`4befc080569dbe0d4d978efaef502e51f644163d15ef9bd22ae7112cf1840387`.
Both exactly match the constructor's frozen values. All 25 gzip chunk
hashes and row counts match; they contain 9,431,158 compressed bytes,
24 chunks of 60,000 rows and a last chunk of 53,024 rows. These checks
are in the machine-readable full result and postcheck result.

The algebraic meaning of each certificate is sufficient. Degree retention
ensures that the integer Sylvester resultant reduces to the resultant of
the displayed finite-field polynomials. Their unit gcd makes that residue
nonzero. The integer resultant is therefore nonzero, so P and Q have no
common root in an algebraic closure of Q. This argument never reduces an
arbitrary rational u at a prime dividing its denominator. It is a uniform
algebraic incompatibility certificate, not a finite search over possible
witness heights. Together with the family coverage, it establishes the
claimed T1 conditional on the frozen dependencies.

## T2 and T3, including exact quotient and Eisenstein hypotheses

T1 says that a nontrivial f needs at least four rational roots to supply
the conditions. For J=16, h=4 and the bound h-m+2>=4 gives m<=2.
Since m>=2, m=2. Outside the long cluster there are only five slots:
zero twice, the center once, and two more. To supply four distinct
rational roots, those two slots must be distinct rational u,v, different
from 0 and 1, each occurring once. There is room for no further rational
root. Any set omitting one of these four would contradict T1.

Removing x^2(x-1)(x-u)(x-v) is exact monic division in Q[x] and leaves
a degree-15 quotient. Every one of its roots, counted with multiplicity,
belongs to the long cluster and has valuation 1/15. All removed roots
are 19-integral, so monic synthetic division keeps the quotient in
Z_(19)[x]. Its coefficient of degree 15-r is an elementary symmetric
sum of r such roots and has valuation at least r/15. Because that
coefficient is rational, its valuation is an integer or infinity and
is at least one for r>=1. The constant is one product of all 15 roots,
with exact valuation one. These are the full Eisenstein hypotheses
over the discrete valuation ring Z_(19), or after clearing denominators
prime to 19 in the usual integer formulation. Irreducibility over Q_19
and hence over Q follows. Thus T2 is justified.

For J=15, h=5 yields m<=3, so m is 2 or 3. If m=3, the six slots
outside the long cluster consist of three zeros, the center, and exactly
two other slots. The same four-distinct-rational-root requirement forces
two distinct simple rational u,v and no other rational roots. Removing
x^3(x-1)(x-u)(x-v) leaves the **rational**, monic degree-14 quotient.
All its roots have valuation 1/14, and the preceding coefficient and
constant-term argument supplies Eisenstein at 19. This proves exactly
T3's m=3 assertion. For m=2 one extra small slot remains, and this audit
does not infer a rational long-edge factor or the same quotient claim.

In both arguments the quotient is explicitly a polynomial in Q[x] of
the full cluster degree. This avoids the invalid inference that an
arbitrary factor furnished by a Newton polygon over Q_19 must already
have rational coefficients.

## Source audit and attribution

I read the relevant original material directly, with cache hashes and
page locations saved in `three-witness-review-1-postcheck-result.json`:

- [CLO](https://arxiv.org/abs/1208.5404), especially PDF pages 4-5 and
  12-14: its Hasse convention, normalization, simple center, and published
  low-degree bad-prime lists apply in the fields used here. In particular
  19 is good for degree 5. The full-root rationality assumption of CLO
  Proposition 19 is not used.
- [Draisma-de Jong, EMS Newsletter 80](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf),
  PDF pages 33-34: Proposition 6 concerns the cardinality of chosen
  common witnesses, not just the total root set. Its proof and the
  Draisma-Knopper attribution support precisely the two-value obstruction.
  The later corrected degree-family claim is not used.
- [Stoll, *p-adic Analysis in Arithmetic Geometry*](https://mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf), PDF pages 15-16,
  Theorem 3.6: the segment-width count explicitly includes multiplicity.
  [Poonen](https://math.mit.edu/~poonen/papers/curves.pdf), PDF page 68,
  supplies the same slope convention; I use Stoll for the explicit
  multiplicity wording.
- [Massri v6](https://arxiv.org/abs/1806.09561v6), PDF pages 12-14:
  Remark 7.4 reports the 6,680 filter count and Theorem 7.10 states a
  stronger three-recycled-root exclusion over the complex setting.
  The candidate attributes this correctly and does not rely on its
  computational proof. I have not independently audited that paper's
  3^17-resultant computation. No novelty claim follows from this audit.

The full third-party papers remained in the ignored cache. Web screenshot
requests for Massri pages 13 and 14 failed with a cache-miss response;
the complete cached pages were successfully read by pypdf instead. This
access failure did not leave a mathematical input unchecked.

## Adversarial checks and limits

The principal attempted failure modes were: choosing a normalization
witness outside the supposed cover; confusing total roots with a covering
set; assuming algebraic valuations are integral; losing zero multiplicity;
using J as the largest center bit; omitting simultaneous center witnesses;
failing to include repeated 0/U assignments; duplicated or missing raw
refinements; leading-degree drops at certificate primes; an arbitrary
rational denominator; and mistaking a Q_19 Newton factor for a rational
quotient. Each is resolved by the explicit choices and checks above.
No counterexample or substantive gap was found in the frozen claims.

The computations are exact evidence certifying this explicitly finite
exhaustion. Their implications rely on the reconstruction and resultant
argument above. No unrestricted rational-height search, floating-point
calculation, all-roots-rational assumption, characteristic-19 degree-6
claim, or full B4(b) degree classification is asserted.

## Commands, resource controls, and artifacts

From the repository root:

    .venv/bin/python -u problems/2021-B4/reviews/three-witness-review-1-run.py --mode masks --timeout 20
    .venv/bin/python -u problems/2021-B4/reviews/three-witness-review-1-run.py --mode benchmark --limit 32768 --timeout 30
    .venv/bin/python -u problems/2021-B4/reviews/three-witness-review-1-run.py --mode full --timeout 420
    .venv/bin/python problems/2021-B4/reviews/three-witness-review-1-postcheck.py

Python was 3.12.14. The mathematical regeneration and finite-field audit
use only its standard library. pypdf was used for primary-source reading.
The masks child PID 33821 and benchmark child PID 33903 exited zero in
1.488 and 3.966 seconds, respectively. The full child PID 34054 exited
zero and was reaped in 127.620 seconds under the 420-second external
timeout, with 8,192-family incremental checkpoints. No timeout occurred,
no global process kill was used, and no native CAS operation was launched.

Authoritative account-wide weekly telemetry read 9% used both before and
after the full run, reset 1792745187, well below the 90% total-used stop
threshold. No separately billed API was used and no new window was spent.

All new files have the assigned `reviews/three-witness-review-1` prefix.
No candidate, dependency, other review, coordinator integration file,
Git commit, or push was modified. The accompanying manifest records
this report and the scripts, parameters, exact outputs, source hashes,
input validations, issue log, and machine-readable results.
