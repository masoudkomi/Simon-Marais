# Independent Ghosh source audit R2 - blind initial report

2026-10-17 Australia/Brisbane (2026-10-16 UTC). Frozen initial review.

**Disposition:** uphold the narrow missing-inference objections, subject to the
source-date correction below. No specialized repair was identified in the full
22-page PDF or the corresponding queried HTML passages. This is not a
counterexample to the characteristic-zero Casas-Alvero statement, not a
refutation of Theorem A's conclusion, and not a promotion of a result.

## Independence and scope

I did not construct the candidate note, its local determinantal example, or the
coefficient-query example. Before freezing this report I read neither another
reviewer's program/conclusions nor shared issue/status files. The two reviewed
inputs are `notes/ghosh-full-context-audit-v1.md` and
`notes/ghosh-coefficient-descent-query.md`; their exact hashes are in the
companion manifest. I read AGENTS.md and reconstructed the argument from the
entire actual cached PDF, pp. 1-22, including the references. The primary
relevant pages 1, 9, 12 and 19 were also rendered and visually inspected.

Requested settings: `gpt-6.1-sol`, `max`. Effective-setting readback: unavailable;
no effective model or reasoning setting is asserted. No additional agents were
launched. No preliminary part (a) proof was investigated or reproduced. No
other year's problem was investigated. Git was used only for read-only checks;
no Git mutation, commit, push or promotion was performed.

## Source identity: a correction is required

The versioned arXiv abstract for
[2501.09272v2](https://arxiv.org/abs/2501.09272v2) independently reports v1 on
16 January 2025 and v2 on 21 March 2026, 01:41:44 UTC. The unversioned abstract
also currently resolves to v2. The fresh download from the
[versioned PDF URL](https://arxiv.org/pdf/2501.09272v2) is byte-for-byte identical
by SHA-256 to the specified cached PDF:

`562050e1bff0fbfae2493951b4456485c61181381ba374271889d81d96bb5daa`.

It has **22 pages** and its first-page internal date is **March 24, 2026**.
The PDF's arXiv margin says 21 Mar 2026. In contrast, the current
[versioned HTML](https://arxiv.org/html/2501.09272v2) says **August 24, 2026** and
labels the PDF's Proposition 1.4 as Proposition D. The freshly retrieved
[versioned TeX source](https://arxiv.org/src/2501.09272v2) explicitly contains
`\date{\today}`. Thus these internal dates are rendering-date strings, not
additional arXiv submission dates or evidence of a later mathematical revision.
The source archive is 31,091 bytes and its hash is recorded in the manifest.
These artifacts must not be silently identified. I verified that all three queried mathematical passages
are present in both; I do not assert that the artifacts are identical elsewhere.
The candidate's statement assigning the August date to the cached PDF is
incorrect and should be repaired by its author.

[2402.18717v3](https://arxiv.org/abs/2402.18717v3) is a different paper,
*A finiteness result towards the Casas-Alvero Conjecture*. Its abstract history
reports v3 on 14 January 2025, 05:58:13 UTC. Its current experimental HTML also
prints an August 24, 2026 internal date; that is not its arXiv submission date.
Its Theorem A/5.6 is a dimension bound, and Theorem B/Corollary 5.7 is a
finiteness statement. Neither states the universal characteristic-zero
conjecture. I did not independently investigate an acceptance announcement;
acceptance of the finiteness paper would not validate the different universal
claim.

## Applicability to the open 2021 question

Theorem A in the universal-proof PDF is stated for every characteristic-zero
field, every monic polynomial of degree at least 3, and every derivative order
1 through d-1, using nonconstant gcds with Hasse derivatives. This would apply
to the normalized rational contest polynomial: rational shared roots imply
the requisite gcds over Q, scalar division preserves shared roots, and ordinary
derivatives differ from Hasse derivatives by nonzero factorials. Its conclusion
over Q has the required rational linear factor. The rational-root hypothesis
is stronger than the paper's gcd hypothesis; they are not equivalent.

The official B4(b) question was independently rechecked in the downloaded
[2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
p. 2. The repository normalization in `statement.md` supplies the full rational
hypotheses for this applicability check. The paper's degree range starts at 3;
it does not by itself establish the degree-2 boundary. I have supplied no
preliminary or boundary-case proof in this review.

## Reconstructed dependency chain and hypothesis checks

Write R_m=K[x_1,...,x_m], and let F(i,j,m) be the translated elementary
symmetric form of degree m+1-i defined in Sections 2-3. The translation has the
marked root at zero, with j=m+1 denoting the identity. The following chain is
what the paper actually needs, rather than an inference from its title.

1. The finiteness paper's Proposition 5.2, restated as PDF Proposition 1.4,
   identifies degree d CA with regularity of each of the d-1 specified
   homogeneous forms in R_(d-1). Its algebraic-closure setting is relevant.
   Its Theorem A/5.6 gives height at least d-2. This is an almost-complete-
   intersection bound, not the missing full height d-1.
2. Proposition 3.3 seeks equality of global and minimal-prime local generator
   counts, with characteristic excluding prime divisors of the displayed
   product of binomial coefficients. It uses the height lower bound to reduce
   to homogeneous primes of height m-1. The coordinate change to a line and
   K(t)-residue field is justified over the algebraically closed working field.
   The cancellation of t after (3.8) is the first audited missing step.
3. Theorem 3.6 seeks global generator count m outside finitely many prime
   characteristics. Its degree-by-degree argument reduces to a form not lying
   in the ideal of the higher-order forms. Producing a polynomial violating
   the corresponding vanishing consequence is sufficient for that purpose;
   ideal membership and mere set-theoretic vanishing need not be equivalent.
   The paper obtains such a polynomial through Lemma 3.7 over C and then
   appeals to nonzero integer minors of finite Macaulay matrices. The
   projective-closure/fiber step in Lemma 3.7 is the second audited missing step.
4. Corollary 3.9 combines (2) and (3). In characteristic zero the binomial and
   finite-prime exclusions do not obstruct application. The downward step uses
   this corollary in the lower-degree ring, at its minimal primes.
5. Assume CA in degree n+1 for all marked-index choices. Fix the desired
   lower-degree tuple, and replace its identity index n by n+1 when lifting
   to R_n. Equations (4.4)-(4.6) give F_i=f_i X+g_i in R_(n-1)[X], with
   f_i exactly the desired lower-degree forms and X=x_n.
6. The truncated Koszul complexes retain homological degrees 0,1,2,3. Filtering
   degree h by X-degree at most k-h gives the lower-degree truncated complex
   as the quotient for k>=3. The displayed wedge notation is imprecise if
   read as the exterior power of the large R_(n-1)-module; the explicit
   coefficient-on-the-fixed-wedge-basis interpretation in the paper makes
   the asserted maps and short exact sequences well defined. Truncating at
   degree 3 does not damage H_1 or H_2.
7. At k=0, the special degree-1 module is im d_2(f). Its image under d_1(F)
   is the 2x2 minors ideal I of the matrix with rows (f_i),(g_i). Thus H_0
   is R_(n-1)/I. The expected height n-2 gives a one-dimensional
   Cohen-Macaulay quotient. The determinantal theorem is applicable to a
   **2 by (n-1)** matrix once grade(I)=n-2 is established, since the ambient
   polynomial ring is Cohen-Macaulay. Bruns-Vetter Theorem 2.7, checked in
   the author-posted book, establishes perfection at expected grade; it
   does not establish reducedness. Its Appendix Proposition 16.19 supplies
   the Cohen-Macaulay consequence.
8. Lemma 4.4, passage from minimal-prime injectivity to global injectivity,
   works because a Noetherian Cohen-Macaulay ring has no embedded associated
   primes. With a unit f_i at a minimal prime, elimination of X is valid and
   proves the desired local contraction. The height calculation can be made
   local after eliminating the monic linear equation; it should not rely on
   an unrestricted dimension-subtraction rule in a nonlocal polynomial ring.
9. The remaining primes have every f_i in p. Adding the final linear form
   with unit X-coefficient produces the regular-sequence minors Delta_(i,n),
   so one is outside p. Lemma 4.5 then seeks a contradiction. Its passage
   from (4.23) to the vanishing needed for (4.24) is the third audited missing
   step and is analyzed below.
10. Conditional on the contraction and Proposition 4.3, its extension to all
    filtration steps is sound: a relation among the highest X-coefficients
    gives a constant minor combination; the skew-symmetric coefficients
    used to lower the relation introduce no unwanted lower term, because
    sum q_(ij) g_i g_j=0. The apparent F_n in this passage is a notation slip;
    the contraction needed is for the truncated n-1 generators.
11. Since the lower-degree ideal has grade at least n-2 and has n-1
    generators, depth sensitivity gives H_i=0 for i>1. The hypotheses are a
    Noetherian polynomial ring, the stated grade bound, and a finite sequence.
    In the filtration long exact sequence this makes the H_1 transition
    maps injective. Filtered direct limits of modules are exact, so their
    injection into the zero limiting H_1 forces them to vanish. Injectivity
    on H_0 then forces lower-degree H_1 to vanish. Positive homogeneous
    degrees permit localization at the irrelevant maximal ideal and the
    Noetherian-local regularity criterion; see
    [Stacks tag 09CC](https://stacks.math.columbia.edu/tag/09CC).
12. That would prove downward induction. The unbounded prime-power degree
    families in
    [Graf von Bothmer et al.](https://arxiv.org/abs/math/0605090) provide the
    starting degrees. Field independence/extension and descent then give the
    asserted characteristic-zero fields. None of this removes a missing
    injectivity proof earlier in the chain.

The conditional final homology mechanism is coherent. I found no repair of
the three identified steps in the introduction, global definitions, remaining
Section 3 results, Section 4 filtration, final argument, or references.
This is a reconstruction and targeted source audit, not a new independent
proof of every theorem in the cited literature.

## Lemma 4.5: precisely what is justified and what fails

Let S=(R_(n-1))_p and A=S/I S. The already-established height and minimality
make A Artinian local. Under the contradiction's assumptions,
Delta_(l,n) is a unit, f_l is in p, and g_l is a unit. The minors imply
f_i g_l=f_l g_i, hence every f_i belongs to p. These assertions are valid.

The unit-ideal step (4.20)->(4.21) is also valid. Although A[X] need not be
finite as an A-module, its maximal-ideal extension is nilpotent; iterating
that nilpotence proves the required form of Nakayama. Similarly, the
proportionality of columns is valid here because the pivot column has a
unit entry, or equivalently Delta_(l,n) is invertible. General rank-one
language over an arbitrary ring alone would not suffice, but that is not
the situation here.

Consequently F_l=g_l+f_l X is a unit in A[X]. This does **not** say f_l=0
in A. If f_l is nilpotent, a finite geometric series is its inverse after
dividing by g_l. In this Artinian local situation that nilpotence is already
automatic from f_l in p. The polynomial-unit fact therefore supplies no
extra information toward the claimed zero.

The coefficient argument shows c_m in p from c_m f_l in I and f_l not in I.
At the next coefficient, however, it gives only

    c_(m-1) f_l + c_m g_l in I.

Membership c_m in p is insufficient to discard c_m g_l modulo I. Thus
the repeated inference that c_(m-1) belongs to p has not been proved.
The rational localized example in the query note exactly exhibits this
failure, with no approximation:

    (1-tX)(1+tX)+t^2 X^2=1,  I=(t^2),  f=t,  g=1.

I interpret the minors in (4.23) as the intended generators of I. Its printed
index range appears inconsistent with the preceding truncated matrix; the
objection survives this favorable interpretation and does not depend on a
typographical error.

### Independent check of the stronger local model

For the note's four columns (y^2,1),(xy,2),(x^2,3),(z,1), the minors ideal
in S=Q[x,y,z]_(x,y,z) is exactly (a,b,h), where

    a=x^2-3z,  b=xy-2z,  h=y^2-z.

The quotient identifies with Q[x,y]_(x,y)/(x^2-3y^2,xy-2y^2).
The two quadrics are independent, and y^2 is not in their degree-2 span.
All cubic monomials belong to the ideal: in particular

    x*(xy-2y^2)-y*(x^2-3y^2)+2y*(xy-2y^2)=-y^3.

Their relations also reduce every other cubic to a multiple of y^3.
Thus 1,x,y,y^2 is a basis, z=y^2 is nonzero, and z^2=0. This checks
Artinianity, height(I)=3, and nonreducedness. Since S is regular local
of dimension 3 and I is generated by 3 elements of height 3, mu(I)=3.
For J=(z,x^2,xy,y^2), z and the three independent quadratic classes give
mu(J)=4. All columns are proportional to (z,1) in A^2. The identity

    z^2=(z+h)*a+(-4z-b)*b+3z*h

was independently expanded exactly, as was the resulting polynomial-unit
certificate in the candidate. This example therefore preserves the listed
local codimension, determinantal, unit-pivot and generator-count data.

It does not preserve the actual derivative polynomials or all global
inductive hypotheses. For example the actual first column satisfies
g_1=-x_(j_1) f_1 (or g_1=0 for the identity index); the model does not.
That specialized identity does imply f_1=0 in A under this unit-pivot
contradiction, since g_l+x_(j_1)f_l is a unit. I found no argument in the
paper extending that partial observation to every f_i. It must not be
silently strengthened into the necessary full vanishing.

In the actual family, the same contradiction would give J contained in a
homogeneous height-(n-2) prime of a ring with n-1 variables. After passing
to an algebraic closure, that yields a nonorigin lower-degree CA point.
Thus an actual characteristic-zero derivative-family countermodel would
already imply a CA counterexample. None is produced here. Conversely,
appealing to lower-degree CA to exclude the prime would assume the goal of
the downward induction. This is why the defensible finding is a missing
specialized proof, rather than falsity of Lemma 4.5's specialized conclusion.

## Proposition 3.3: nonzero localization is insufficient

PDF p. 9, after (3.8), and the current HTML both infer that localizing at a
zero divisor makes the entire ring zero. This is false. Localization is zero
only if an element of the multiplicative set annihilates 1; a zero divisor
need annihilate only a nonzero element.

Both proposed examples check out:

    Q[t,y]/(ty) localized by t = Q[t,t^(-1)],
    Q[t,y]/(t*y^2,y^3) localized by t
        = Q[t,t^(-1),y]/(y^2).

In the second example y^2 is nonzero before localization and is killed by t;
its ideal is (y)*(ty,y^2), preserving the quotient-by-m-times-J shape. The
localization remains nonzero. These are not the paper's particular H_i.

Even translated homogeneous families can have this issue generically. For
I_0=(x^3,xy,z) and the line point (0,1,0), the translated forms are
u^3,u(v+t),w. In the relevant quotient by m times their ideal, t kills u^3:

    u^2*[u(v+t)]-v*u^3=t*u^3.

The class u^3 is nonzero, as specialization t=v=w=0 sends the product ideal
into (u^4). Adjoining v as a generator, as in the paper's J-plus construction,
does not remove this example. This is still a generic example, not a
counterexample in the derivative family. Distinct homogeneous degrees,
translation coordinates, or a nonzero generic localization are insufficient
on their own. A torsion-freeness/saturation argument for the particular H_i
is needed for cancellation of t; none was supplied elsewhere in the paper.

## Lemma 3.7: closure of fibers versus fibers of closure

For the map b -> (b,b^2), the incidence of values lying on [k_1:k_2]
has affine equation k_2 b-k_1 b^2=0. Its genuine closure in
P^1_B times P^1_K has equation

    B_1*(k_2 B_0-k_1 B_1)=0.

No extraneous component is supported entirely in B_0=0. At K=[0:1],
the affine fiber is {0}, whose own projective closure is just [1:0].
The fiber of the total closure also contains [0:1] at infinity. It is the
limit of the affine points b=1/u, K=[u:1]. This verifies both the candidate's
fiber objection and the precise escape-to-infinity mechanism. The example
has finite common-zero set {0} and an isolated zero for the projected map,
so those features do not repair the general inference either.

In the paper, properness does make the image of the total infinity locus
closed. It does not establish that the designated parameter lies outside
that image. The incorrect interchange of closure and fiber is exactly what
is used for that exclusion. Without the exclusion the later compact path
does not supply the claimed uniform bounding ball. Positivity of holomorphic
local index and Brouwer homotopy invariance are appropriate only once a
bounded domain with no boundary zeros has been justified.

The map in this generic model is not the paper's Abel-Gontcharoff map.
Remark 3.8 does give alternative arguments in two special index classes:
few distinct higher witnesses, and all witnesses distinct. These do not
cover every tuple; for example n=4,l=1, tuple (1,1,2,3) is in neither
class. The finiteness theorem gives finiteness of the designated affine
CA fiber, but not properness of this incidence family near that parameter.
No additional no-escape argument for the actual map was identified.

## Exact computations, negative attempt, and operational record

The standard-library certificate program and complete final JSONL are saved
under this review's prefix. Empty polynomial residuals represent exact zero;
all final identity residuals are empty. Rational ranks give degree-2 rank 2,
rank 3 after adjoining y^2, and full degree-3 rank 4 for the Artinian model.

A small additional test was deliberately attempted in the actual derivative
family in characteristic 11: n=4, tuple (1,2,2,1), root vector (0,1,4,6).
All four forms vanish, and 11 avoids the binomial-exclusion product 96.
Exact finite-field coefficient linear algebra gives **global mu=3** and
Jacobian rank 3 at the line. The highest-degree form is already redundant
globally. Thus this is a **failed attempt to contradict Proposition 3.3**,
not evidence of a mismatch of its local and global counts. It is also in
positive characteristic and has no bearing as a CA counterexample over Q/C.
No search beyond this single tuple was conducted.

Execution used a dedicated subprocess with a 30-second timeout, unbuffered
incremental JSONL output, and recorded PID. The final child PID was 44155,
Python 3.12.14, exit 0; only the standard library was needed. The launcher
is saved in the ignored review cache. Earlier child 44024 failed immediately
because SymPy is not installed; its source and traceback are preserved.
The first standard-library run, PID 44105, caught a sign error in my auxiliary
y^3 certificate via a nonzero residual; that output is preserved in the
ignored cache, the sign was repaired, and the full child was rerun successfully.
These bounded calculations are finite identity/rank evidence, not proof of an
unrestricted source objection or a general conjecture.

Initial PDF rendering without a fontconfig override emitted cache errors and
was interrupted through its own execution session 74582 (exit 130). A minimal
fontconfig pointing its writable cache into this review's ignored directory
fixed rendering. Subsequent renders had explicit 25-second child timeouts
and all four inspected page images were produced. No global process kill,
installation, charge, permission bypass, or outside message was used.

Authoritative account-wide weekly telemetry was available: 10% total used
at start, then 11% at the sustained-work check, reset Unix 1792745187.
This was well below the 90% total-used cutoff and did not cross a reset.
All full third-party sources and rendered intermediates remain in ignored
`.cache/`. The manifest records their source links and hashes. No licence
permitting redistribution of the full papers is asserted.

## Frozen conclusion

The exact generic countermodels and the dependency interpretation support
the candidate's narrow conclusion: **specific missing proof steps identified;
specialized repairs and validity of the universal theorem unresolved by this
audit**. The candidate should correct the cached PDF's internal date and keep
its abstract examples distinct from the derivative family. On the checked
evidence, this universal-proof paper cannot be treated as a validated theorem
for closing the contest problem in this research packet. The different
finiteness result is neither a universal solution nor invalidated by this
audit. Promotion and integration remain the coordinator's responsibility.
