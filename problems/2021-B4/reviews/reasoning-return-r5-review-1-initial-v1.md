# Fresh initially blind WHOLE R5 audit R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; verified effective-setting readback unavailable.
This is a whole nonconstructor recommendation, not coordinator promotion.

**Recommendation:** no substantive defect found in R5A–R5E in the exact
stated scopes. I reconstructed all five arguments and their accepted
interfaces, including every selector, the disjoint-triple bound, the
symbolic p+1 carrier, RC2+PN4 and all five TA1 applications. No required
author repair was identified. The result does not exclude full J15,
degree20 or all remaining center masks, and does not classify the annual
problem or construct a rational counterexample. A second fresh whole
audit and coordinator reconciliation remain required before promotion.

Target:20083 bytes, SHA256
`0d546265a3f9b1f83c05fce46e5a97acb6cad5d8841518d891ffed91717166f6`.
Constructor freeze:3592 bytes, SHA256
`1626fa3981c78eb04f7fe41fc5a725b2500de0cf1647e7324941c6a5f3671533`.
The complete candidate, current worklog/source MD/JSON, all30 obligations
and constructor self-check were read. The self-check is construction
provenance, never an independent audit. Administrative scripts/metadata
are byte-checked without executing author code. The accompanying42-row
ledger covers every substantive obligation.

## Independence and old-premise boundary

I authored the SEVEN earlier return-r3 mathematical packets, including
G1/G2, RC2, PP1/PP2 and TA1/TA2. I previously held J15/PN review roles.
These facts are material and explicit: this audit does not count as an
independent re-review of those older auditor-authored theorems. They
have separate acceptance based on two other whole audits and are used
only at their accepted scopes. Their exact complete mathematical bodies
were reread and their new applications checked.

I did not construct the NEW R5 selector/valuation bound, symbolic
extension, RC2+PN4 combination or five-unit consequence, and supplied
no R5 strategy or proof clarification. Root supplied a clarification
of the author's already proposed triple-count mechanism and is not
counted independently. Neither constructor nor root inspection replaces
the two fresh R5 audits. No new R5 peer report, findings or later root
inspection was read before this COMPLETE initial freeze; no substantive
finding was sent before it.

I read all12 declared accepted-body/register texts, the seven exact
old return mathematical bodies, PN's full proof/application body,
normalization, the full Newton and rational-cover proofs, the full
J15 and both single-center expositions, and the relevant acceptance
records. Old large finite certificates are accepted dependencies, not
rerun or newly claimed independent audits here. Unused context and
earlier immutable source records are fingerprinted as metadata; they
supply no missing R5 inference.

## 1. Official domain, normalization and derivatives

The [official2021 paper,p.2 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf)
requires a polynomial over Q and an ACTUAL rational common root with
each derivative order1,...,d-1. A different root may serve each order.
The open task is the degree classification. All roots of f need not
be rational or real; a nonconstant rational gcd alone is insufficient.
No preliminary part(a) proof was investigated or reproduced.

The accepted CLO-based normalization for a hypothetical nontrivial
degree d=p+1 example uses a rational repeated H1 witness and the
distinct rational center to make0 a multiple root and1 the simple
center. The affine change is rational. In its binomial shape,
a0=1,a1=-1 and every a_j is in Z_(p); all other nonzero roots have
positive p-adic valuation. Only RATIONAL noncenter roots are therefore
known to have positive INTEGER valuation. This never asserts integral
valuations for all algebraic roots.

Throughout the report, a "positive witness valuation" means positive
p-adic valuation. No positivity of a rational root in the real order is
assumed. This interpretation is fixed by the normalization and the
explicit minimum defining nu_w.

The exact normalized derivative is

    D_j=H_(d-j)(f)/binom(d,j)
       =sum_(k=0)^j binom(j,k)a_k X^(j-k).

It is monic and p-integral BEFORE reduction; its rational zeros equal
the Hasse derivative's zeros. No nonunit is divided out in F_p.
H1 already uses0, and H_(d-1) has its sole zero1. Thus j2,...,d-2
are precisely the remaining selected equations. For2<=j<=p-1,
binom(p+1,j) has valuation1, so beta_j is an ordinary integer and
a p-unit. The exact divided center equation is

    -1+sum beta_j a_j=0.

## 2. R5A: every selector has a nonzero signed count and a divisibility constraint

Choose ANY actual rational witness w_j of f,D_j and let I include1
and exactly those selected indices with w_j=1. This is a choice of
center witnesses, not the mod-p coefficient support. A selected center
may have a nonunit coefficient; a center may also be available but not
selected. No center-priority rule, parity assumption or PN support
restriction enters the proof.

The collapse recursion gives ordinary integers b0=1,b1=-1 and
b_j=0 off I. Adding a new largest selected index m changes nothing
earlier and gives

    b_m=-F_previous(m),
    F_new(Z)=F_previous(Z)-F_previous(m)binom(Z,m).

There is no denominator in the integer coefficient recursion.
The [classical descent recurrence,Proposition2.1](https://arxiv.org/html/1710.11033v2)
has the opposite sign at this step. Induction from the empty set gives
exactly F_I=(-1)^|I| d(I;Z), with the SAME I. The source's count
domain is n>max I; here d>max I because max I<=d-2. No complement,
reversal or substitution of a unit support has occurred.

Nonvanishing also has a standalone direct proof. Split the d positions
into the ascending runs prescribed by I; give the first run the largest
available values, the second run the next largest, and continue,
increasing within each run. Every join is a descent and no run contains
one. Thus d(I;d)>=1 for every I, including consecutive indices and
arbitrary parity. This is positivity over Z, not a p-unit assertion.

At Z=d the first two terms are1-d=-p and all later terms are
p beta_j b_j. Hence

    p q_I=F_I(d)=(-1)^|I| d(I;d),
    q_I=-1+sum beta_j b_j in Z minus{0}.

The factor p and the nonzero conclusion are exact. If every selected
w_j were0 or1, triangular induction would force a_j=b_j over Q.
The actual center equation would then give F_I(d)=0, impossible.
Consequently the selected nonzero noncenter witness set is NONEMPTY.
Its valuations are finite positive integers, so nu_w is a legitimate
positive integer minimum; zero is omitted rather than assigned a finite
valuation.

For comparison modulo p^nu_w, the base coefficients a0,a1 agree
exactly with b0,b1. At a selected center, subtracting the triangular
equations propagates the earlier coefficient differences. At any other
selected witness, b_j=0 and every summand for a_j contains
w_j^(j-k) with j-k>=1. If w_j is nonzero its valuation is at least
nu_w; if w_j=0 all summands vanish exactly. All earlier a_k and
binomial coefficients are p-integral. This proves a_j-b_j belongs to
p^nu_w Z_(p) for EVERY j, including selected nonunit center positions.

Subtracting the actual divided center equation gives
q_I=sum beta_j(b_j-a_j) in p^nu_w Z_(p). Since q_I is a nonzero
ordinary integer, this is ordinary divisibility p^nu_w|q_I.
Multiplying by p gives p^(nu_w+1)|d(I;d). The extra exponent is
essential. The proof does not identify q_I with a unit or prove
liftability from this finite divisibility.

For an old D5 constant defined by precisely this0/1 collapse, q0
is now known nonzero. A differently defined constant is not covered
merely by having the same name.

## 3. R5B: a disjoint-position-block bound and the exact degree20 exponent

For a fixed descent set, the two comparisons inside a triple of distinct
entries permit respectively1,2,2,1 relative orders for patterns
++,+-,-+,--. The middle two sets are{132,231} and{213,312};
the monotone patterns have just123 and321. Thus each triple permits
at most two of six orders. A final prescribed pair permits one of two;
a singleton contributes no condition.

Partition POSITIONS into s triples and a final block of size t, where
n=3s+t,0<=t<=2. First allocate the values to the blocks. The number
of allocations is n!/((3!)^s t!). Internal orders can then be chosen
independently in these DISJOINT blocks. Dropping all comparisons between
blocks only enlarges the set. Therefore the exact upper bound is

    d(I;n)<=n! 2^s/((3!)^s t!)
           =n!/(3^s*2^[t=2])=U_n.

No independence of overlapping comparisons or probabilistic model is
being used. This proves the bound for every valid I, and no maximum
zigzag-count theorem is needed.

For n=p+1, positivity and R5A imply p^(nu_w+1)<=U_(p+1).
With K_p the largest exponent allowed by that upper bound,
nu_w<=v_p(q_I)<=K_p-1. The subtraction of one is due to
F_I(d)=p q_I, not an indexing convention.

At d20, six triples and one pair give

    U_20=1668657070080000,
    1458 U_20=2432902008176640000=20!,
    19^12=2213314919066161>U_20.

I reconstructed this small arithmetic by hand. For example19^6=47045881;
squaring(47000000+45881) gives the displayed19^12, since
45881^2=2105066161. Multiplying U_20 by1400 and58 gives
2336119898112000000+96782110064640000=20!.
Thus nu_w+1 cannot be12 or larger, and1<=nu_w<=10.
No numerical program or descent-support scan supplies the argument.

The quantifier is important: EVERY chosen witness selector contains
some selected noncenter witness of valuation at most10. This is a
bound on the MINIMUM among selected witnesses, not on every root,
every witness individually, unused roots or global rational heights.
It says nothing about v(d0-2r), the different collision-depth variable
in RC2. In an equal-valuation J15 branch, every eligible selected
noncenter nonzero witness comes from the small slots with that same
integer nu; fractional long-cluster roots cannot be rational. Hence
nu_w=nu and nu<=10. Unequal cases retain only the minimum bound.
No complete leading pattern or mask is thereby excluded.

## 4. R5C: exact local edge, local Eisenstein factor and GLOBAL unrecycling

Let h=d-J and e=J-1 under p>=5,J>=d/2. Then
e>=2,2<=h<p and e<=p-2. The center equation guarantees J exists.
Write f=sum c_l X^l. We have v(c_h)=1,c_p=-d a unit,
all middle valuations>=1 and all c_l with2<=l<h at least2
or zero. For the line(p-l)/e:

- Below h, its value is at most(p-2)/e<2, using2J>p.
- Between h and p its value is strictly below1.
- At l=d=p+1 it is negative, while the leading coefficient is a unit.
- The constant and linear coefficients vanish.

Only h,p lie on this supporting edge. Its width e therefore accounts
for EXACTLY e roots of valuation1/e, counted with multiplicity.
I checked the multiplicity convention in the original Stoll
[Theorem3.6 and its product proof](https://www.mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf),
as well as the exact accepted Newton application.

The valuation cluster is invariant under the absolute Q_p Galois group.
Its monic product g therefore has coefficients in Q_p. Every nonleading
coefficient, as a symmetric sum of products of roots with positive
valuation, has positive valuation. Since it lies in Q_p that valuation
is an integer and hence at least1, or the coefficient is zero. The
constant term has exact valuation e/e=1. Thus g is Eisenstein of
degree e. It is irreducible and separable in characteristic0. Repeated
slots are not discarded before this conclusion; the conclusion itself
shows the cluster is separable.

Choose pi with pi^e=p in an algebraic p-adic extension. The same
supporting-line inequalities give integral P(T)=pi^(-p)f(pi T),
with reduction

    Pbar=-T^p+lambda T^h,
    lambda=c_h/p mod p !=0.

Pi is not asserted to belong to Q_p. For any cluster root alpha,
T0=alpha/pi is a unit, and T0bar^e=lambda. For1<=k<=h,

    H_k(f)(alpha)=pi^(p-k)H_k(P)(T0),
    H_k(Pbar)(T0bar)=lambda binom(h,k)T0bar^(h-k)!=0.

The first term's binom(p,k) vanishes modulo p, while binom(h,k)
is a unit because h<p. Reduction commutes with Hasse differentiation.
This proves the EXACT value v_p(H_k(f)(alpha))=(p-k)/e,
not merely a lower bound. It excludes every low-order common root
in the cluster without assuming any rationality of those roots.

Let Q be alpha's monic irreducible polynomial over Q, of degree M.
It divides f; over Q_p the local minimal polynomial g divides Q,
so M>=e and the SAME Q contains the whole cluster. This step does
not infer that the local g itself has rational coefficients. A rational
irreducible polynomial shares a root with a rational derivative iff it
divides that derivative. For k<=h the exact evaluation at alpha rules
this out for the whole global Q, including any other global conjugates.

For k>=h+1 the derivative degree is d-k<=e. If M>e this rules
out divisibility. If M=e, equality of monic polynomials gives Q=g
over Q_p, and only k=h+1 has sufficient degree. Divisibility there
would force Q=D_e. But D_e has X^(e-1) coefficient-e, a p-unit
because2<=e<=p-2. The corresponding g coefficient is divisible by p.
This excludes the borderline case; larger k have smaller degree.
Consequently Q is coprime to EVERY H_k,1<=k<=d-1.

With R=f/Q in Q[X], coprimality implies every gcd(f,H_k) divides R
and deg R<=d-e=h+1. No Casas-Alvero property of R follows: its
own derivatives differ from those of f. A Galois classification is
unnecessary. In the J15,m3 corollary, accepted T3 separately proves
that the two residual small nonzero slots are rational and the degree14
quotient is rational Eisenstein. R5C excludes that carrier, so all
derivative common-root values there are rational as claimed. This
does not assume that all roots of f are rational or exclude the branch.

## 5. R5D: the exact repeated-root ladder is excluded by compatible premises

The full setup is J15,d20,m2 with sole H3 at the low center and
the TWO2R slots actually coinciding at d0. Accepted D3 gives the
rational simple r sharing H2,H4 and all three small valuations nu.
The ratio d0/r has residue2. It need not equal2r, and its finite
displacement depth is unrestricted in this new hypothesis.

If d0 were not rational, the only rational root values would be
0,1,r: fractional-valuation roots cannot be rational. Accepted T1
requires at least four rational witness values, so d0 is rational.
Thus the exact rational root set is{0,1,r,d0}; zero and d0 are double,
while1 and r are simple. The roots are distinct because their scaled
residues and valuations differ as stated.

Now additionally impose the FIVE exact equations
H6(r)=H8(r)=H10(r)=H12(r)=H14(r)=0. I matched RC2's full accepted
body: under precisely this normalization, sole-H3 repeated-root setup,
ladder and full rational-witness hypothesis, H18 cannot use1.
Its proof permits arbitrary initial nu and both finite and exact
displacement; R5D does not borrow a sample lift or only its depth bound.

The full contest hypothesis must therefore supply an ACTUAL rational
noncenter H18 common witness. Accepted PN4 excludes exactly the
repeated-root setting PLUS this ladder PLUS such a rational witness.
All its hypotheses now hold, so there is a contradiction. The proof
does not substitute a Q19-only root, residue witness, a3 unit or
parity hypothesis not provided by the accepted application.

This is a valid NEW combination of separately accepted partial inputs.
The old RC2 depth15/16 outcomes were necessary possibilities, not
realizations satisfying every other accepted restriction. They remain
correct in the preserved old text; the combination now rules out their
FULL-ladder rational-witness realization. It does not contradict the
low-order-only family or exclude distinct2R roots, missing ladder
equations, other center patterns, m3 or lower J.

## 6. R5E: five specified units force one higher sole center and a full linear gcd

Retain the full repeated-root setup, without assuming the ladder.
Suppose a5,a7,a9,a11,a13 are units; no condition is placed on a3.
If every H6,H8,H10,H12,H14 had at least one rational noncenter
common root, TA1 would apply successively at m=3,4,5,6,7.
Its linear-unit indices19-2m are respectively13,11,9,7,5.
For m3 the preceding H2,H4 equations are accepted D3 facts.
Each transfer then supplies the next exact H_(2m)(r)=0 needed by
the following transfer. The witness hypothesis is actual noncenter
existence, even if the center is also available; center nonvanishing
has not been silently assumed. The complete forbidden ladder follows,
contrary to R5D.

Therefore at least one of those five derivatives has NO rational
noncenter common root. The official hypothesis still supplies a
rational common root, and1 is the only possible value. This proves
the sole-rational-center statement.

For the stronger complete-gcd assertion, the actual rational factors
X^2(X-1)(X-r)(X-d0)^2 remove exactly six slots. Their rational monic
degree14 quotient consists entirely of the fractional cluster and is
Eisenstein at19; it is the unrecycled carrier of accepted G1, or of
the separately reconstructed R5C. Thus it adds no derivative common
root over the algebraic closure. Every remaining value is one of the
four rational values, and the selected derivative has only1 among them.
Since1 is simple in f, its monic gcd is EXACTLY X-1. Scalar extension
does not add a common root to coprime rational factors.

The a3 condition in old TA2 was used for the H16/three-value-cover
construction. That construction is not needed here: contradiction
already occurs after the five transfers at m3 through7. Hence dropping
a3 is justified. Missing any of the FIVE required units prevents the
corresponding automatic transfer; neither their presence in all masks
nor the impossibility of a higher sole center is established.

## 7. Source and unresolved-boundary disposition

The [CLO normalization passage,Section3.4 and Lemma17](https://arxiv.org/pdf/1208.5404)
was checked with its actual CA hypotheses and the separately accepted
rational affine map. Its all-roots-rational Proposition19 is not a
rational-witness theorem. The [one-root/MacMahon connection in Marashdeh](https://arxiv.org/html/2608.14726v1),
TheoremB and Section4, is prior attribution, not an unrestricted
multi-root classification or a direct identification of R5's different
coefficient indexing. R5 rederives that identification explicitly.
No novelty, priority or claim of an exhaustive literature search is made.

The five arguments withstand the challenged distinctions: selector versus
unit support, integer positivity versus a p-unit, selected minimum versus
all roots, rational valuation versus algebraic ramification, local g
versus global Q, a residual factor versus a smaller-degree CA system,
same reduced2R versus actual repeated value, full ladder versus partial
ladder, actual rational witnesses versus Q19 roots, and sole rational
center versus complete derivative gcd. No substantive gap was found.

The old prime5 bad quartic residue and2011 correction remain in force.
No CRT/second-prime exclusion, all-real-root interpolation or application
of the prime-degree theorem to an unproved CA critical-value polynomial
is made. The numerical depth bound leaves1,...,10 and does not solve
the actual rational-lifting problem. No complete degree, J15 branch,
surviving mask or annual classification is promoted.

No mathematical program, scan, CAS, support-table enlargement or author
certificate rerun was used. Metadata hashing/JSON creation writes only
this assigned review prefix and preserves all38 older own frozen packets
plus the separate GK telemetry addendum. The complete initial report,
ledger, actual-source scope and integrity records freeze before any new
peer R5 findings. Root alone may promote after both whole audits and
complete reconciliation.
