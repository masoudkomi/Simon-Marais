# Full-context source audit of Ghosh's general proof claim

2026-10-16. **Candidate source objection - unverified by independent reviewers.**
This is a focused reconstruction and source-use audit, not a counterexample to
the Casas-Alvero conjecture, not a refutation of the theorem's conclusion, and
not an independent review of the coordinator's initial coefficient example.
The author of this note constructed the strengthened local model below and
must not count as an independent reviewer of that model.

## Sources, version and scope

- Soham Ghosh, *Proof of the Casas-Alvero conjecture*,
  [arXiv:2501.09272v2](https://arxiv.org/abs/2501.09272v2),
  [primary full HTML](https://arxiv.org/html/2501.09272v2).
- Cached PDF identified and checked, with focused reading of the argument
  on pp. 6-20 and the surrounding definitions and theorem statements:
  `.cache/literature/2021/cited-40f9614065b33fc5.pdf`.
  SHA-256 `562050e1bff0fbfae2493951b4456485c61181381ba374271889d81d96bb5daa`,
  22 pages; matches the coordinator's retrieval manifest. The v2 header is
  21 March 2026; the internal date is 24 August 2026. This discrepancy is
  reported, not resolved by guessing.
- Its distinct predecessor, *A finiteness result towards the Casas-Alvero
  Conjecture*, arXiv:2402.18717v3, is not the universal-proof claim. The
  reported acceptance of the finiteness paper does not validate this paper.

Requested launch settings were `gpt-6.1-sol` / `max`; no effective-setting
readback was available. Only `problems/2021-B4/` was edited. No agents were
spawned and no commits, pushes, installations or external messages were made.

## Exact applicability to the contest

Theorem A claims, for every characteristic-zero field K and every monic
degree d>=3 polynomial f in K[X], that all the gcd(f,H_i(f)) are nonconstant
if and only if f=(X-alpha)^d with alpha in K. The contest's rational common
root for each derivative implies its gcd hypothesis over K=Q. Dividing the
contest polynomial by its leading coefficient preserves the hypothesis, and
H_i=f^(i)/i! in characteristic zero. Thus a valid Theorem A would imply the
entire open contest statement, with the elementary d=2 boundary addressed
separately. The field/root distinction is in the safe direction. No part (a)
proof was investigated or reproduced here.

The obstacle to use is proof validation, not a mismatch of quantifiers.

## Dependency map reconstructed from the paper

Let R_n=K[x_1,...,x_n] and

    F(i,j,n) = Phi_(n,j)(e_(n+1-i)(x_1,...,x_n)).

Phi translates the marked root x_j to zero; the index n+1 means the identity.
The earlier finiteness paper supplies both the regular-sequence reformulation
and the lower height bound n-1 for the n-generator degree-(n+1) ideals.
The paper first reduces to algebraically closed fields; its topological
nonredundancy argument is over C, and the audited downward step is in
characteristic zero. These reductions do not turn rational shared witnesses
into a weaker contest requirement.

1. Proposition 3.3 claims equality of global and minimal-prime local numbers
   of generators, subject to explicit binomial-characteristic exclusions.
2. Theorem 3.6 claims the global number is n outside a finite prime set. Its
   characteristic-zero nonredundancy argument uses Lemma 3.7, an existence
   statement for a polynomial meeting selected higher derivative conditions
   while failing the next one, proved using Abel-Gontcharoff polynomials and
   Brouwer degree. Corollary 3.9 combines (1) and (2).
3. Section 4 assumes CA in degree n+1 and seeks CA in degree n. The n-1
   truncated generators in R_(n-1)[X] are linear in X=x_n:

       F_i = f_i X + g_i,  1<=i<=n-1.

   Their leading coefficients f_i are precisely the lower-degree generators.
   Marked identity indices are changed from n to n+1 as specified in §4.1.2.
4. A filtration of the first four Koszul modules, using X-degree k-homological
   degree, has successive quotient the lower-degree truncated Koszul complex
   for k>=3. At k=0 its degree-1 module is the image of the leading-coefficient
   Koszul differential; its H_0 is R_(n-1)/I, where I is the 2x2 minors ideal
   of the matrix with rows (f_i) and (g_i).
5. Proposition 4.3 seeks injectivity of the maps on H_0. It first proves that
   R_(n-1)/I is one-dimensional Cohen-Macaulay, then reduces contraction of
   (F_i) to I to localizations at minimal primes p of I. Where some f_i is
   a unit, eliminating X proves the contraction. Lemma 4.5 is the step meant
   to eliminate the remaining minimal primes containing every f_i.
6. Given Proposition 4.3, the long exact sequences, the earlier height bound
   and Koszul depth sensitivity give H_2=0 and then H_1=0 for the lower-degree
   complex. Downward induction from the known unbounded degree families
   finishes the claimed theorem.

The final homology argument is conditional on the preceding injectivity.
The finite-degree truncation retains enough terms to compute H_1 and H_2;
nonvanishing of its top H_3 does not itself contradict that argument. The
explicit coefficient interpretation of the wedge maps makes sense despite
some imprecise wedge notation. No separate flaw was established there in
this focused pass. The cited finiteness, determinantal and depth theorems
were not all independently reproved; this note does not certify them or
every inference in the 22-page paper.

## Main issue: Lemma 4.5 after equation (4.23)

Here p is a minimal prime over I, height p=n-2; S=(R_(n-1))_p and
A=S/I S is Artinian local. Adjoining the final linear generator with unit
X-coefficient gives minors Delta_(i,n) generating a height-(n-1) ideal, so
some Delta_(l,n) is outside p. The lemma assumes for contradiction that
f_l is in p. It correctly obtains g_l a unit and all f_i in p, and obtains
that F_l is a unit in A[X]. The claim at issue is the further implication

    F_l unit in A[X]  ==>  f_l=0 in A.

That implication is false for a general Artinian local A. If f_l is any
nonzero nilpotent and g_l is a unit, then

    (g_l+f_l X)^(-1)
      = g_l^(-1) sum_(j=0)^(N-1) (-g_l^(-1) f_l X)^j

whenever f_l^N=0. Artinianity makes every element of the maximal ideal
nilpotent; it does not make those elements zero. Thus the unit condition is
automatic under the contradiction's local hypotheses and does not imply
the displayed equality (4.24).

In coefficient terms the top relation does imply c_m in p if f_l is not in
I. But the next relation is

    c_(m-1) f_l + c_m g_l in I.

Knowing c_m in p only puts its second term in p, not in I. It cannot be
dropped modulo I. A unit c_(m-1) can cancel that term. The coordinator's
Q[t]_(t), I=(t^2), f=t, g=1 identity exhibits exactly this cancellation.

### Stronger local determinantal model

The following example additionally preserves the determinantal structure,
expected codimension and the generator count used for the contradiction.
It is still **not** the paper's specialized derivative family.

Take S=Q[x,y,z]_(x,y,z), p=(x,y,z), and columns

    (f_i,g_i) = (y^2,1), (xy,2), (x^2,3), (z,1).

Because g_4=1, the minors ideal is generated by

    a=x^2-3z,  b=xy-2z,  h=y^2-z.

The quotient is Q[x,y]_(x,y)/(x^2-3y^2,xy-2y^2). These two independent
quadrics have only the origin in their common zero set: if y is nonzero,
the second forces x/y=2 whereas the first requires (x/y)^2=3. Its graded
basis is 1,x,y,y^2, with y^3=0. Consequently z=y^2 is nonzero but z^2=0
in A=S/I. The quotient is Artinian and height I=3. Moreover

    J=(f_1,f_2,f_3,f_4)=(z,x^2,xy,y^2)

needs four generators at p, while I needs three. Thus the generator-count
condition mu(J)=4, height I=3 does not by itself remove the nilpotent case.
The proportionality of all columns in A^2 also holds: they are respectively
1,2,3,1 times (z,1).

An explicit certificate is

    z^2=(z+h)a+(-4z-b)b+3zh,

so

    (1-zX)(1+zX)+X^2((z+h)a+(-4z-b)b+3zh)=1.

The exact identities and their zero residuals are saved in
`computations/source_audit_certificates.py` and
`computations/source-audit-certificates.jsonl`. The child completed with
exit code 0 under a 30-second subprocess timeout; its PID and dependencies
are recorded in the output. Computations certify these finite identities,
not the full source objection or a CA counterexample.

### Why a full specialized counterexample was not produced

At a minimal prime p of I, if f_l is zero and g_l nonzero in the residue
field, the minors force every f_i to be zero there. The f_i are exactly the
lower-degree CA generators. Since height p=n-2 in n-1 variables, this would
produce a nontrivial lower-degree CA point over an algebraic closure.
Therefore finding a derivative-family counterexample to Lemma 4.5 is
substantially stronger than checking the disputed coefficient inference;
it would amount to a counterexample to the lower-degree conjecture itself.

No such example was found or claimed. The logical gap is that the proof
does not establish the needed vanishing of the nilpotent coefficient. The
preceding Artinianity and the numerical generator-count information do not
do so as abstract local assertions. An additional theorem using the actual
derivative polynomials could repair this; none was identified in the text.
One must not silently assume lower-degree CA to rule the phenomenon out,
because lower-degree CA is the downward induction's goal.

## Two additional source queries

These were found while reconstructing the dependency chain. They reinforce
the need for a repair but are not asserted to disprove the specialized
statements.

### Proposition 3.3, PDF page 9: localization of a zero divisor

After (3.8) the proof says that if t were a zero divisor in its quotient,
then inverting t would make the quotient ring zero. This inference is false
in general. In B=Q[t,y]/(ty), t is a zero divisor but

    B[t^(-1)] = Q[t,t^(-1)]

is nonzero. More closely matching a quotient by a maximal-ideal times an
ideal, take B=Q[t,y]/(t y^2,y^3), so its defining ideal is
(y)*(ty,y^2). The nonzero class y^2 is killed by t, while inverting t gives
Q[t,t^(-1),y]/(y^2), again nonzero. Nonzero localization therefore does not
prove t is regular. A specialized torsion-freeness argument is needed for
the degree-descent in (3.7); one was not identified in the passage.

### Lemma 3.7, PDF page 12: projective closure and special fibers

The proof identifies the fiber of the projective closure of an incidence
variety with the projective closure of the corresponding affine fiber,
then infers that a finite affine fiber excludes points at infinity in the
total closure over that parameter. This is not true in general.

For the polynomial map b -> (b,b^2), use parameter [k_1:k_2] for a line in
C^2. The affine incidence is k_2 b-k_1 b^2=0. Its closure in
P^1_b x P^1_k has equation

    B_1(k_2 B_0-k_1 B_1)=0.

At K=[0:1] the affine fiber is the finite set {0}, but the total closure
also has the point ([0:1],[0:1]) at infinity. It is approached by
b=1/u and K=[u:1] as u tends to zero. Thus finite affine fibers can lose
points at infinity, precisely the possibility that obstructs a uniform
Brouwer-degree domain in that proof. A proof that the paper's particular
Abel-Gontcharoff map excludes such escape is needed; none was established
in this audit. The abstract example is not that particular map.

## Checkpoint conclusion and next work

The universal claim cannot presently be used as a validated theorem in this
research packet. The main coefficient inference fails in general, and the
paper does not identify the extra specialized argument that would repair it.
The strongest supported wording is **specific missing proof steps identified;
specialized repair and theorem validity unresolved**. Calling the entire
theorem false or the conjecture refuted would overstate this audit.

The nilpotent model, the two other examples and the dependency interpretation
need fresh independent adversarial review before promotion even to a reviewed
source objection. In particular one reviewer should inspect whether a theorem
elsewhere in the paper supplies a repair missed here. The present worker is a
co-constructor and cannot provide either independent audit of this note.

The bounded new rational-witness direction and its limits are recorded in
`notes/rational-witness-p-plus-one-v1.md`; no general source reading or CAS
search was left running. The original `proof.md` mathematical body was kept
unchanged.
