# Rational-base dynamics lead, 2026-10-16

**Exploratory direction, not a proof of universal equality.** The accepted
fixed-difference density theorem leaves ordinary integer points in a
zero-density exceptional set unresolved. This note distinguishes a useful
analogy from an established reduction.

## Primary sources inspected

- Akiyama, Frougny and Sakarovitch, *Powers of rationals modulo 1 and rational
  base number systems*, Israel J. Math. 168 (2008), 53–91,
  [author-posted manuscript](https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf),
  DOI [10.1007/s11856-008-1056-4](https://doi.org/10.1007/s11856-008-1056-4).
  The introduction and abstract motivate rational-base expansions and
  restricted fractional-part orbits. The full technical results have not
  yet been audited for applicability to this problem.
- Andrieu, Eliahou and Vivion, *A Normality Conjecture on Rational Base
  Number Systems*, [arXiv:2510.11723v2](https://arxiv.org/html/2510.11723v2),
  7 April 2026. The introduction and Section 2 define minimal/maximal
  words. Conjecture 1.6 concerns residues of iterates of ceil(p*x/q);
  Theorem 1.7 relates this conjecture to their word-normality conjecture.
  This is a conjectural distribution input, not an available theorem
  establishing that every integer orbit has every finite pattern.

The source checks above do not assert that the Simon Marais problem is
equivalent to Mahler's problem, a rational-base normality conjecture, or
the scalar ceiling iteration. No such bridge has been proved here.
Full paper copies remain in ignored local cache; citations and hashes
are recorded centrally.

## Exact quotient identity and a tempting but false shortcut

The accepted control formulation writes b=60q+r, 0<=r<60, d=a-b, and

    c=3*floor((r+d)/30),
    b'=66q+r+c,   r'=b' mod60,
    q'=(11q+h)/10,   h=(r+c-r')/6.

Here h is an integer depending on the finite residue/difference state
and the next residue. Thus there is a rational multiplier 11/10 with a
state-dependent correction. This does not imply q'=ceil(11q/10).
For example, at (a,b)=(599,600), q=10,r=0,d=-1,c=-3, and
b'=657, so q'=10 whereas ceil(11q/10)=11. At (601,600), with
the same q and r but d=1, b'=660 and q'=11. Both starts satisfy the
official domain. A result for the scalar ceiling map therefore cannot
be transferred by simply identifying q with its scalar state.

The finite control-word lifting theorem also does not assert that one
fixed ordinary integer has a normal control itinerary. Its quantifiers
range over congruence classes of initial integers for each fixed finite
length. An infinite avoiding itinerary can select a 10-adic initial
value that is not an ordinary positive integer.

## A direct bounded-error power identity

For an actual orbit let u_n=a_n mod30 and v_n=b_n mod20, using least
nonnegative remainders. If s_n=a_n+b_n and beta=11/10, exact arithmetic
gives

    s_(n+1)=beta*s_n-(u_n+v_n)/10.

The correction epsilon_n=(u_n+v_n)/10 lies in [0,48/10]. Hence the
series C=s_0-sum_(k>=0) epsilon_k/beta^(k+1) converges and

    C*beta^n = s_n-theta_n,
    theta_n=sum_(j>=0) epsilon_(n+j)/beta^(j+1),  0<=theta_n<=48.

These are elementary real identities; the bound is the geometric sum
(48/10)/(beta-1)=48. They do not give a useful single restricted
fractional-part interval of length less than 1: the error interval is
48 units wide. No conclusion about avoidance or equality follows.
This is another reason that merely noticing the multiplier is insufficient.

## Next research question

Seek an explicit finite-state coding or conjugacy that preserves ordinary
integer starts and sends equality avoidance to a verified restricted
rational-base language. Audit any proposed correspondence in both
directions; allow a negative conclusion if the state correction obstructs
it. Even a valid coding may lead to an unresolved normality question,
so distinguish a reduction from a solution. No new candidate theorem is
promoted by this exploratory note.
