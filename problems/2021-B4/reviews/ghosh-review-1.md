# Independent initial source audit R1

2026-10-17 Australia/Brisbane (2026-10-16 UTC). **Initial adversarial review,
frozen independently. No promotion of any mathematical result.**

I did not construct the candidate, its determinantal example, or the
coordinator's coefficient example. I read neither another review nor a shared
issue/status file before completing this report. Requested launch settings:
`gpt-6.1-sol` / `max`; effective-setting readback: unavailable. I read the supplied
AGENTS.md and kept this review within 2021 B4(b). No preliminary (a) argument was
investigated or reproduced.

## Finding

The candidate's main, deliberately limited mathematical objection is supported:
the coefficient descent following (4.23) contains an unjustified inference.
The nilpotent examples, including the stronger determinantal example, check
correctly. The two other proposed generic countermodels also check correctly.
I found no argument elsewhere in the complete cached universal-proof paper that
supplies the three requested specialized repairs. The actual current HTML
retains the disputed passages, and does not repair them there.

This establishes a defect in the written justification, not a counterexample to
the specialized derivative-family statements, Theorem A, or Casas-Alvero.
The conclusion I support is: **specific proof gaps identified; the needed
specialized repairs and the universal theorem's validity remain unresolved.**
Theorem A should not currently be used as a validated solution of the entire
contest open part in this research packet.

The candidate has a source-metadata error that its author should repair before
the coordinator accepts the source audit: its August 24 date belongs to the
HTML artifact, not to the supplied PDF.

## Exact source objects and extent of reading

1. Soham Ghosh, *Proof of the Casas-Alvero conjecture*,
   [arXiv:2501.09272v2](https://arxiv.org/abs/2501.09272v2).
   I read the complete 22-page cached PDF, including definitions, the proof's
   last homology argument, and references. SHA-256:
   `562050e1bff0fbfae2493951b4456485c61181381ba374271889d81d96bb5daa`.
   I separately downloaded the current
   [versioned PDF](https://arxiv.org/pdf/2501.09272v2): it has exactly that hash.
   Both its extracted first page and rendered first page say **March 24, 2026**;
   its arXiv header says **21 Mar 2026**. Its regular-sequence reformulation is
   numbered **Proposition 1.4**.
2. The actual current
   [versioned HTML](https://arxiv.org/html/2501.09272v2), fetched into my own
   ignored cache, has SHA-256
   `ff66da8d20a4ca8161b458de02c0d39afc53cac628c4dfa760c4a34efed3127b`.
   It displays **August 24, 2026**, the same arXiv header, and calls the
   reformulation **Proposition D**. I inspected its mathematical sections and
   compared each disputed passage directly. I do not infer complete
   mathematical or byte identity merely from the shared version label.
3. The separate *A finiteness result towards the Casas-Alvero Conjecture*,
   [arXiv:2402.18717v3](https://arxiv.org/abs/2402.18717v3), is the 29-page cached
   file `cited-78d1801ffc618164.pdf`. Its header is 14 Jan 2025, and its internal
   date is January 15, 2025. I checked the statements and relevant surrounding
   discussion of Proposition 4.14, Proposition 5.2, Theorem 5.6, and Corollary
   5.7, rather than treating the whole predecessor as a proof of CA. Its
   dimension/finiteness conclusions permit nonempty finite sets of hypothetical
   counterexamples. Nothing in those cited conclusions asserts reducedness of
   the minors quotient or the required torsion-freeness. I make no inference
   about acceptance of one paper validating the other paper.

PDF pages 1, 9, 12, and 19 were rendered and visually inspected. The displayed
claims audited below are present in both source artifacts. The manifest binds
all hashes, input snapshots, commands, and review artifacts.

## Dependency chain reconstructed

Write `R_n=K[x_1,...,x_n]` and
`F_i=Phi_(n,j_i)(e_(n+1-i))`. The source's reductions are to algebraically
closed fields and then to C for its topological argument. The characteristic
exclusions in Proposition 3.3 are harmless in characteristic zero.

The proof uses the predecessor's regular-sequence characterization and height
bound; Proposition 3.3 is meant to transport the global generator count to
minimal primes. Theorem 3.6 obtains the global count using Lemma 3.7's
Abel-Gontcharoff/Brouwer argument. Together they give Corollary 3.9. In the
downward step, upper-degree generators have the form `F_i=f_i X+g_i`, where
the `f_i` are exactly the lower-degree generators, with the specified identity
index changed from n to n+1. Proposition 4.3 proves injectivity of H_0 in a
filtered, truncated Koszul complex by proving contraction to the minors ideal
`I=I_2[(f_i);(g_i)]`. Lemma 4.5 is essential to that contraction proof. Given
that injectivity, the long exact sequences and the height bound force lower
H_1 to vanish. Downward induction starts from known unbounded degree families.

Here is the conditional last step in sufficient detail to check its logic.
The degree-q piece of filtration level k has X-degree at most k-q. For k>=3,
coefficient extraction in each degree gives the lower truncated complex as
the quotient of two successive filtration levels. At level 0, the degree-1
module is the image of the lower Koszul d_2, so its H_0 is R_(n-1)/I. The
predecessor's height bound gives grade of `(f_1,...,f_(n-1))` at least n-2;
Koszul depth sensitivity consequently gives H_2=0. Thus H_1 of successive
filtration levels injects for k>=3. Their direct limit has H_1=0 by upper
regularity, so each level k>=2 has H_1=0. The connecting map from the lower
H_1 is then injective; H_0 injectivity makes its image zero. This gives lower
H_1=0, and regularity in the positive homogeneous Noetherian setting.

I find no defect in this last *conditional* implication. Truncation through
d_3 retains the terms needed to compute H_1 and H_2. It need not retain the
full Koszul H_3. The explicit coefficientwise definition of the maps resolves
their imprecise exterior-power notation for this purpose.

For the determinantal input, I checked Bruns-Vetter's actual Theorem (2.7) in
the [author-posted book](https://www.home.uni-osnabrueck.de/wbruns/brunsw/detrings.pdf),
printed p.13 / PDF p.21: expected grade of the maximal minors gives a perfect
ideal. Its hypotheses fit a 2 by (n-1) matrix over the polynomial ring once
the asserted height n-2 is known. This supports the Cohen-Macaulay conclusion,
but gives no reducedness. The height bound is also recorded in that book's
Theorem (2.1). The regular/Koszul/H_1 equivalence needs local or graded
hypotheses, which the positive homogeneous setup supplies; see the
[Stacks discussion](https://stacks.math.columbia.edu/tag/062D). These facts
cannot replace Proposition 4.3. I have not independently reproved every cited
result in the predecessor or the Brouwer-degree books; this is not a
certificate of the remainder of the universal-proof paper.

## Lemma 4.5: the precise failure

Let p be a minimal prime over I, `S=(R_(n-1))_p`, and `A=S/IS`. In the
source p has height n-2, hence A is Artinian local. An augmented minor
`Delta_(l,n)` is a unit in S. Under the contradiction hypothesis `f_l in p`,
one obtains that g_l is a unit. The internal minors then imply all f_i are in
p. In A, all columns are proportional to the l-th column, and F_l generates
the unit ideal of A[X]. These steps do not require A to be reduced. The
Artinian version of the Nakayama step can be justified by nilpotence of its
maximal ideal even though A[X] is not a finite A-module.

The next step is the problem. A unit `g+fX` in A[X] need only have nilpotent
f; it need not have f=0. Indeed, if `f^N=0` and g is invertible, its inverse is

    g^(-1) sum_(j=0)^(N-1) (-g^(-1)fX)^j.

Thus Artinianity supplies precisely the possible phenomenon that the proposed
coefficient descent must rule out.

Taking the intended summands of (4.23) to be elements of I, its top relation
gives `c_m f_l in I`. If `f_l notin I`, then `c_m in p`, since otherwise c_m
is invertible in S. The next relation is

    c_(m-1) f_l + c_m g_l in I.

Membership of c_m in p supplies no membership of c_m g_l in I. The second
term can cancel the first even when c_(m-1) is a unit. In the coordinator's
model `S=Q[t]_(t), I=(t^2), f=t, g=1`, the exact identity

    (1-tX)(1+tX)+X^2 t^2=1

has c_1=-t in p and c_0=1 outside p. It meets the local domain, Artinian
quotient, nonzero f modulo I, unit g, and degree conditions used in that
coefficient descent. It is not an instance of the source's derivative family.

There is an additional indexing discrepancy in printed (4.23): its summation
is `2<=i<j<=n`, whereas the preceding minors ideal uses the n-1 unaugmented
columns. My objection gives the argument its more favorable intended reading
as a certificate modulo I. A correction of that range would not repair the
coefficient inference.

### Independent reconstruction of the strengthened model

For `S=Q[x,y,z]_(x,y,z)` take columns

    (y^2,1), (xy,2), (x^2,3), (z,1).

With `a=x^2-3z`, `b=xy-2z`, `h=y^2-z`, the internal minors generate exactly
`I=(a,b,h)`: the last bottom entry is 1, and every other minor is an S-linear
combination of the last-column minors. Eliminating z gives

    A = Q[x,y]_(x,y)/(r1,r2),
    r1=x^2-3y^2, r2=xy-2y^2.

The identity `y r1-(x+2y)r2=y^3` shows y^3=0. It follows that xy^2,
x^2y, and x^3 vanish as well. The two degree-2 relations are independent in
the basis `(x^2,xy,y^2)`, and y^2 is not their linear combination: the first
two coordinates would force both coefficients to be zero. Consequently the
quotient has basis `1,x,y,y^2`. It is already local, since (x,y) is nilpotent,
so localization creates no new relation killing y^2. In particular z=y^2 is
nonzero and z^2=0. Thus I is maximal-primary, height I=3 and mu(I)=3.

The ideal `J=(z,x^2,xy,y^2)` has four minimal generators at the maximal
ideal: these monomials are pairwise nondivisible, and their classes remain
independent modulo (x,y,z)J. Every column of the matrix is proportional to
`(z,1)` modulo I, with factors 1,2,3,1. Finally,

    z^2=(z+h)a+(-4z-b)b+3zh

and therefore

    (1-zX)(1+zX)+X^2((z+h)a+(-4z-b)b+3zh)=1.

These conclusions confirm the candidate's claimed properties. They show that
the local determinantal structure, expected codimension, generator counts,
and even this complete-intersection Artinian quotient do not force f_l=0.
The model does not supply all global hypotheses of the downward induction.
In particular it is not a choice of the source's actual Phi-transformed
elementary symmetric polynomials or a CA counterexample.

No result elsewhere in either universal-proof artifact asserts the additional
radicality or comparable special property needed at this point. The later
generator-count contradiction depends on (4.24); it does not independently
establish (4.24). The earlier Cohen-Macaulay conclusion is insufficient, as
the model also illustrates. The conditional homology argument later in the
paper does not supply a noncircular repair.

## Proposition 3.3: localization query

On PDF p.9, following (3.8), the source deduces that its t is regular from
nonvanishing of a localization, arguing that inverting a zero divisor would
give the zero ring. The same sentence remains in current HTML. In general
localization is the zero ring exactly when a power of the inverted element
is zero; a zero divisor need not be nilpotent.

The candidate's simple example `Q[t,y]/(ty)` verifies the distinction. Its
factorized-ideal example is also correct:

    B=Q[t,y]/(t y^2,y^3),
    (t y^2,y^3)=(y)*(ty,y^2).

Here y^2 is nonzero by monomial-ideal membership, t y^2=0, and after inverting
t the quotient is `Q[t,t^(-1),y]/(y^2)`, which is nonzero. Nonvanishing of the
localized quotient, including the further localization used in the paper,
does not establish t-regularity. To cancel successive powers in the relevant
quotient, a saturation/torsion-freeness statement is required.

The proof's special H polynomials arise from the homogeneous derivative
generators by the coordinate construction in (3.3)-(3.6). The examples above
are not those H polynomials. I found no separate t-saturation proof or cited
theorem with that conclusion in the universal-proof paper. Therefore the
generic inference fails and the specialized Proposition 3.3 remains
unvalidated by this audit; it is not proved false by these examples.

## Lemma 3.7: projective closure query

On PDF p.12, the total incidence closure's fiber is identified with the
closure of the corresponding affine fiber. This same identification remains
in the current HTML. The inclusion from closure of an affine fiber into the
total closure's fiber is automatic; equality can fail.

For `Theta(b)=(b,b^2)`, the affine incidence equation is
`k2*b-k1*b^2=0`. Its closure in `P^1_B x P^1_k` is

    B1*(k2*B0-k1*B1)=0.

This is indeed the closure: both of its components meet the chart B0!=0
densely. At K=[0:1], the affine fiber is {b=0}; its own closure is the single
point [1:0]. The total closure fiber has equation B0*B1=0 and contains also
the point [0:1]. The path `B=[u:1], K=[u:1]` lies on the total closure and
for u!=0 has b=1/u. It tends to the additional point over K=[0:1]. All these
identities were independently checked. In this example the finite base-zero
set is {0} and the selected affine fiber equals that set, so those extra
abstract features do not prevent escape.

Properness of projection from the *total* projective closure does make its
infinity image closed. It does not exclude the distinguished parameter from
that image just because the affine fiber there is finite. The source needs
an argument specific to its dehomogenized Abel-Gontcharoff map to obtain the
neighborhood and uniform bounded domain used by Brouwer-degree invariance.
Finiteness of the arithmetic CA scheme supplies finiteness of appropriate
normalized solution sets, not that missing interchange of fiber and closure.

I checked Remark 3.8 rather than ignoring possible alternative proofs. It
provides special cases (few distinct later indices, or a permutation of all
indices), not a general proof of the required no-escape property. The model
above is not the actual Abel-Gontcharoff map. It does not disprove Lemma 3.7
for that family, or invalidate the cited Brouwer-degree theorem.

## Scope and contest implication

The quantifiers of the universal Theorem A would cover the contest's rational
case: normalize the leading coefficient and use `H_i=f^(i)/i!`. A rational
common root implies a nonconstant gcd over Q. The theorem's conclusion over
Q would provide the rational linear power required in B4(b), for its d>=3
range. The d=2 boundary is outside that theorem and must be handled separately
by established elementary context; I give no preliminary-part proof here.

A derivative-family example with a minimal p of height n-2 containing all
the lower f_i would produce a nonzero projective point of the lower CA
generator ideal over an algebraic closure. It would therefore already amount
to a lower-degree CA counterexample. No such point was constructed or found
in this review. The gap should not be exaggerated into a requirement that
one first produce such a counterexample before questioning the inference.

My recommendation is to repair the candidate's artifact/date attribution and
retain its narrow unresolved-source wording. Do not promote the universal
proof or a general contest solution on this evidence. The source objections
and any eventual specialized repair require the coordinator's normal
two-independent-review integration; this report alone makes no promotion.

## Reproducibility and limitations

`ghosh-review-1-check.py` independently expands the coordinator identity, all
internal-minor identities, the determinantal nilpotence/unit certificates,
and the projective path identities using exact rational coefficients. It also
records the finite linear/monomial arguments described above. Its separate
supervised subprocess had PID 43870, a 30-second timeout, exit 0, elapsed
0.044 seconds, empty stderr, and flushed checkpoints. These are finite
certificates, not computational proof of any unrestricted source statement.

The backend is Python 3.12.14 standard-library rational arithmetic. Bundled
`pypdf` served extraction and Poppler served rendering. `bs4` and `sympy` were
unavailable; I used the standard HTML parser and exact polynomial code instead
of installing dependencies. The first-page rendering emitted Fontconfig cache
warnings but completed with exit 0; the displayed page was readable. No
calculation or render remains running. I used no separately billed API,
external message, purchase, commit, push, or global process kill. Both
authoritative telemetry checks showed 10% total weekly usage, same reset
1792745187; this review did not cross a weekly window.
