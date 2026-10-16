# A rational-witness restriction in degree p+1

2026-10-16, version 1.1 (presentation repairs). **Candidate proof - unverified.** This is a partial necessary
condition for the open B4(b) problem, not a classification of degrees. It
requires two independent adversarial audits before any promotion. The
existing `proof.md` mathematical body is unchanged. No novelty claim is made.

## Published ingredients and the field distinction

1. Castryck, Laterveer and Ounaïes (CLO),
   [*Constraints on counterexamples to the Casas-Alvero conjecture, and a
   verification in degree 12*](https://arxiv.org/abs/1208.5404), Math. Comp.
   83 (2014), 3017-3037. Cached PDF
   `.cache/literature/2021/cited-66c5af6a0f0239f5.pdf`, SHA-256
   `d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf`.
   Section 3.4, equations (9)-(10) and the argument before Lemma 17, provides
   the p-adic normalized shape below for degree p+1. Proposition 10 excludes
   a root of multiplicity >=d-2. These are attributed inputs, not new results.
2. Draisma and de Jong,
   [*On the Casas-Alvero conjecture*](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf),
   EMS Newsletter 80 (June 2011), printed pp. 29-33. Proposition 6 on printed
   pp. 31-32 (PDF pages 33-34, one-based) states that the chosen shared roots for all derivatives cannot
   form a set of exactly two values; the adjacent sentence observes that a
   single value gives a pure power. It attributes the observation to Draisma
   and Knopper. CLO §1.2 defines type(f) as the minimum size of a covering set
   of **recycled roots** minus one, and Proposition 7 gives type(f)>=2.

The second input concerns distinct common witness roots. A theorem merely
requiring at least three distinct roots somewhere in the full complex root
set would not justify the argument below. The contest supplies rational
witnesses for every derivative, so if only two rational roots of f were
available, those chosen witnesses would violate this precise input. All
other roots of f are allowed to be irrational and nonreal throughout.

The Draisma-de Jong article also contains a degree-family assertion later
corrected by CLO; only its separate Proposition 6 is used here.

The subsequently located Massri v6 PDF has SHA-256
`8e5dec6d9d3ca1cb6becd7fa7e3d4c6ef18927cff9521c5f4eb9a1c1b567952f`;
the coordinator owns the central retrieval entry. Its independent three-root
resultant claim is not assumed in this candidate argument.

## Normalization inherited from CLO

Fix an odd prime p and d=p+1. Suppose a nontrivial polynomial satisfying the
contest's rational-witness hypothesis exists. Let r be its rational shared
root with f', and let c be the rational shared root with f^(d-1). CLO Lemma
17 says c is simple, so r differs from c. Translating r to 0, scaling c to 1
and making f monic uses rational affine transformations. CLO §3.4 gives

    f(x)=x^d-d x^(d-1)+sum_(j=2)^(d-2) binom(d,j) a_j x^(d-j),
    a_j in Z_(p),  f(0)=f'(0)=0,  f(1)=0,

where Z_(p) denotes rational numbers with denominator prime to p. In this
normalization 1 is the unique root of valuation 0, and every other nonzero
root has positive p-adic valuation. These valuation statements about the
whole root set are the published facts used; no integrality of all algebraic
root valuations is assumed. In particular rational witnesses other than 1
are in p Z_(p), because a rational number's p-adic valuation is an integer.

Define the normalized degree-j derivative explicitly by

    D_j(x)=(j!/d!) f^(d-j)(x)
          =H_(d-j)(f)(x)/binom(d,j)
          =sum_(k=0)^j binom(j,k) a_k x^(j-k),
    a_0=1,  a_1=-1,  2<=j<=d-2.

The last expression shows that D_j has p-integral coefficients. Its roots
are the same as those of f^(d-j), since the scalar is nonzero over Q. Thus
modulo-p reduction below applies to D_j itself; it does not divide by a
nonunit after reduction.

For 2<=j<=d-2=p-1, the binomial coefficient binom(d,j) has valuation exactly
1. Thus f has p-integral coefficients and

    f mod p = x^(d-1)(x-1).

## Candidate lemma: the lowest nonzero coefficient is not p-Eisenstein

Write f=sum c_k x^k and let m>=2 be the multiplicity of 0, so c_m is its
first nonzero coefficient. Then

    v_p(c_m)>=2.

Candidate proof. By CLO Proposition 10, m<=d-3. Since 1 is a simple root,

    f=x^m(x-1)q,    D=deg(q)=d-m-1>=2.

Division by the monic factors x and x-1 keeps q in Z_(p)[x]. Reduction mod p
gives q mod p=x^D, and comparison of constant terms in x^(-m)f=(x-1)q gives
q(0)=-c_m. We already have v_p(c_m)>=1. If its valuation were exactly 1,
q would be an Eisenstein polynomial over Q_p of degree D>=2: it is monic,
every other coefficient is divisible by p, and its constant coefficient is
not divisible by p^2. It would therefore have no Q_p root and consequently
no rational root. The only rational roots of f would then be 0 and 1.

Every chosen common witness in the contest would belong to {0,1}, contrary
to Draisma-Knopper's two-recycled-root result. This contradiction establishes
the asserted necessary condition. End candidate proof.

This does not assume that all roots of f are rational and does not extend
CLO Proposition 19 by silently making that assumption. It instead uses the
rationality of the shared witnesses to rule out an Eisenstein residual factor.

## Exact necessary center-pattern filter, d=20 and p=19

For each j=2,...,18 choose whether H_(20-j) has the center 1 as a shared
witness. If it does, select 1; otherwise select a rational witness in
19 Z_(19). Define a_0=1 and a_1=-1 as above. The derivative equation gives
the following residue recursion:

    a_j = -(1-j+sum_(k=2)^(j-1) binom(j,k)a_k) mod 19
          if the center is selected;
    a_j = 0 mod 19 otherwise.

The second line follows because the selected rational witness reduces to 0
and the normalized Hasse derivative has p-integral coefficients. The first
line is its value at 1. Finally f(1)=0, divided by 19, requires

    -1+sum_(j=2)^18 (binom(20,j)/19) a_j = 0 mod 19.

The script visits all 2^17=131072 binary selections and uses only exact
integer arithmetic. It finds 6680 selections passing this last congruence.
This matches Massri v6, Remark 7.4, whose separately reported computation
also retains 6680 binary patterns in this normalization. That match is a
useful cross-check, not an independent verification of Massri's later
resultant computation.

Of the 6680 patterns, 3043 have a_18 nonzero mod 19. For those patterns
c_2=190 a_18 has valuation 1, so m=2 and the candidate lemma excludes them
under the rational-witness hypothesis. The remaining 3637 patterns have
a_18=0 mod 19. They are only survivors of necessary congruences. They need
not lift to Q_19 or Q, need not have c_2 nonzero, and need not satisfy any of
the full common-root equations. Thus the run proves no new complete degree
and provides no rational counterexample.

Files:

- `computations/rational_witness_p_plus_one.py` (standard library only);
- `computations/rational-witness-p-plus-one.jsonl` (parameters, PID,
  16384-pattern checkpoints, full residue histogram and sample selections).

Exact command from repository root:

    .venv/bin/python problems/2021-B4/computations/rational_witness_p_plus_one.py > problems/2021-B4/computations/rational-witness-p-plus-one.jsonl

The worker ran in a subprocess with an explicit 30-second timeout, PID 14665,
exit code 0, approximately 0.143 seconds. Python 3.12.14; no installs or
separately billed APIs. No process remains running. This finite arithmetic
run is evidence for the filter, never proof of an unrestricted statement.

## What remains

The lemma and its use of CLO's rational normalization need independent
reconstruction and a second adversarial audit. In particular reviewers should
check the rational affine change, p-integrality, m<=d-3 and the exact covering
set definition. The finite filter also needs independent verification.

A possible next bounded step is to impose mod 19^2 witness equations on the
3637 surviving patterns, keeping rational valuations integral and using
explicit subprocess timeouts. No assertion of finite sufficiency is available:
successive congruence tests could keep surviving forever. A general degree-20
three-recycled-root search would first need a certificate audit of Massri's
existing claim, so no 3^17 resultant computation was launched here.
