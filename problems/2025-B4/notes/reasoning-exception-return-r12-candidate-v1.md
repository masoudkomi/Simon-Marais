# Exact traces at the surviving diagonal center, ET12

2026-10-19 UTC. **Candidate proof - unverified.** Worker B
(`/root/review_2022_complexity_r2`) is the sole NEW constructor. The
coordinator supplied the generic research target only, no new inference.
Two OTHER initially blind ENTIRE WHOLE audits and coordinator reconciliation
are required. Requested inherited settings: `gpt-6.1-sol` / `max`;
independent effective backend readback is unavailable.

This packet proves a proposed exact arithmetic trace formula, with an
application to the ACTUAL ratio root in the surviving signed diagonal
sector. It does **not** exclude that sector, remove a class-number
hypothesis from a published theorem, or solve the annual problem. Its
individual height consequences are explicitly weaker than accepted R10.
There was no mathematical executable, CAS, scan, numerical experiment,
source/author/old helper replay, or finite certificate.

## 1. Exact domains and accepted interfaces

The official open target is 2025 B4(b): ordinary integer quadruples in
`1+X+...+X^n=Y^q`, with `n,q>=2`. Only the restricted signed
prime-diagonal domain is used for the actual application:

    p>=37 prime, |X|>=2, Phi_p(X)=Y^p.                    (D)

The official degree is p-1; the term count and exponent are p. This is not
a reduction of all annual solutions. Both signs of X are retained, and
Y>1 in (D). Let K=Q(zeta), O=Z[zeta], j be complex conjugation, e=p-1,
P=(zeta-1), and L=Q_p(zeta). We use v_p(p)=1 on Q_p; on L the
integer-valued valuation v_P has v_P(p)=e.

The unique ACTUAL integral characteristic ideal is

    A^p=(X-zeta), N_K(A)=Y.

Accepted R10 constructs it and gives the equivalence between

    (C) [A]=[jA] in Cl(K)

and the correctly twisted GLOBAL ratio root. This is equality of actual
ideal classes, not equality of ideals, principality, or a local condition.
Under (C), R10 forces a unique center 0 or -1 at finite depth at least 2.
At center -1 it gives the unique global root gamma in U_2=1+P^2 O_L:

    gamma^p=(X-zeta)/(zeta*X-1),
    gamma*jgamma=1, (gamma)=A/jA.                         (1)

The complete accepted GR11 body then leaves only

    s=v_p(X+1)=2                                         (2)

under (C). GR11 imports the published signed HB-minus upper bound; this
packet neither re-proves nor strengthens it. Its center-0 result and the
actual nontrivial-minus-class alternatives retain their accepted scopes.

I freshly read the COMPLETE current accepted R10 and GR11 bodies and
EACH current acceptance MD and JSON. My older WHOLE2 review roles on both
are disclosed; this is use of accepted inputs, not fresh independent
self-certification of all their foundations. Older UW/RS/BR/RD construction
and other review roles are historical. None supplies an unreviewed new
premise here. The mutable research map was read as a dated observation,
not as a frozen proof or a permanent identity guard.

## 2. The proposed statements

**ET1 (local exact trace ladder).** Let p>=5 be prime and let d in Z_p
have finite exact valuation s>=2. Write d=p^s*t, t in Z_p^times. Put
mu=(1+zeta)^-1, and let gamma_d in U_2 be the unique root

    gamma_d^p=(1-mu*d)/(1-zeta*mu*d).                    (3)

For eta=1 or -1 and every 1<=r<=p-2, define

    nu_r=(zeta^2-zeta)*(1+zeta)^(r-1),
    H_(r,eta)(d)=Tr_(L/Q_p)(nu_r*gamma_d^eta),
    k_r=(s-1)*r+1.

Then

    v_p(H_(r,eta)(d))=k_r,
    H_(r,eta)(d)/p^k_r
      =(-1)^(r+1)*(2*eta*t)^r/r! mod p.                 (4)

The right side is nonzero. In particular, at r=p-2,

    H_(p-2,eta)(d)/p^[(s-1)(p-2)+1]
      =eta/(2*t) mod p.                                 (5)

These are Q_p statements for an actual p-adic root, not assertions that
gamma_d belongs to K or gives a Diophantine solution.

**ET2 (ACTUAL global integer traces).** Suppose (D), (C), and
X=-1 mod p^2. Set d=X+1 and s=v_p(d). For the SAME global root (1),
both numbers

    Delta_(r,eta)=Tr_(K/Q)(nu_r*Y*gamma^eta)              (6)

are nonzero ordinary integers, with the exact valuation and residue in
(4). Here Y=1 mod p, so no extra residue factor occurs. At the actually
surviving GR11 depth s=2 these valuations are r+1, and the last one is
exactly p-1. This requires no principality of A and no Vandiver assumption.
It uses the actual class equality (C) to obtain the global root.

For completeness, all these traces give the strict individual bounds

    Y > p^[(s-1)r+1]/[(p-1)*2^r].                       (7)

They do not improve R10: their strongest member, r=p-2, is smaller than
R10's lower bound by the factor 2/[(p-1)*p^(s-1)]. No joint strengthening
from many traces is claimed.

**ET3 (precise limit of the local higher-divisibility inference).** For
every p>=5, the ordinary parameter X=p^2-1, hence d=p^2, has a correctly
normalized local root (3), and its last trace has valuation p-1, not
at least 2(p-2). Thus the local expansion and the stated normalization
alone cannot establish divisibility by p^[2(p-2)]. This is an analytic
counterfamily to that LOCAL implication. No Y or solution of (D) is
supplied, no published Diophantine theorem is refuted, and no global
root is asserted to exist for these ordinary X.

The selector at r=p-2 is motivated by the inspected author-posted
Mihailescu chapter, Section 5. Attribution and literal source limits are
in Section 7. The complete proof below is independent hand algebra;
neither that section's stronger divisibility nor its Theorem 4 is an input.

## 3. Elementary trace and coefficient facts

### 3.1 The field, units, and trace of P

The Eisenstein polynomial Phi_p(1+T) gives [L:Q_p]=e and
O_L=Z_p[zeta], with basis 1,zeta,...,zeta^(p-2). Also 1+zeta is a
unit: its norm is Phi_p(-1)=1. Consequently mu and all its powers are
integral, both globally and locally. For 1<=a<=p-1,

    Tr(zeta^a)=-1, Tr(1)=p-1.

Thus, for a polynomial Q of degree at most p-1,

    Tr(Q(zeta))=p*Q(0)-Q(1).                             (8)

This formula permits degree p-1; degree p is not silently permitted.
For w in O_L, expansion in the displayed integral basis shows

    Tr((zeta-1)*w) in p*Z_p.                             (9)

Indeed the basis term w=1 gives -p; the other basis terms give zero,
because both exponents lie between 1 and p-1. Hence Tr(P O_L)=p Z_p.
Finally, pairing zeta^c and zeta^-c gives

    Tr(mu)=(p-1)/2,                                      (10)

since (1+zeta^c)^-1+(1+zeta^-c)^-1=1. All identities are the same
for global and local trace on elements of K.

### 3.2 The chosen series and ALL coefficient denominators

For eta in {1,-1}, put

    F_eta(T)=(1-mu*T)^(eta/p)
                  *(1-zeta*mu*T)^(-eta/p)
            =sum_(n>=0) A_(n,eta)*T^n.

All powers here are the binomial series with constant term 1. Explicitly,

    P_(n,eta)(Z)=sum_(a=0)^n binom(eta/p,a)
                              *binom(-eta/p,n-a)*Z^(n-a),
    A_(n,eta)=(-1)^n*P_(n,eta)(zeta)/(1+zeta)^n.          (11)

For EVERY n>=0, not just n<p,

    C_(n,eta)=p^n*n!*A_(n,eta) belongs to O.              (12)

To see this, multiply each summand in (11) by p^n n!. It becomes a
product of ordinary integers eta-p*j and -eta-p*j, the integer
binomial coefficient n!/[a!(n-a)!], powers of zeta, and the global
unit (1+zeta)^-n. No assertion that n! is globally invertible is used.
This proves the common denominator bound at ALL finite primes.

The familiar factorial estimate is

    v_p(n!)=sum_(i>=1) floor(n/p^i) <=(n-1)/(p-1)        (13)

for n>=1. It follows, for example, by writing n in base p and obtaining
v_p(n!)=(n-s_p(n))/(p-1), where the digit sum s_p(n)>=1. Therefore
A_(n,eta)*d^n has L-valuation bounded below by
e*[(s-1)n-v_p(n!)], which tends to infinity for s>=2. The series
converges. Its p-th power is the intended quotient or its inverse;
this also follows by formal binomial identities and convergence.

For n=1 the coefficient is

    A_(1,eta)=eta*(zeta-1)/[p*(1+zeta)].                  (14)

Its evaluated term has P-valuation (s-1)e+1. For n>=2, the coarser
bound from (12)--(13) is at least 2e when p>=5, s>=2. Thus
F_eta(d) belongs to U_2. The roots of unity mu_p intersect U_2 only
at 1: zeta^a=1+a*(zeta-1) mod P^2. The accepted local power identity
U_2^p=U_(p+1), also reconstructed in R10, makes the normalized root
unique. Alternatively two U_2 roots have quotient in that intersection.
We have

    F_eta(d)=gamma_d^eta.                                (15)

No global root or ordinary solution has been inferred.

### 3.3 Exact cancellation and the first nonzero coefficient

Fix 1<=r<=p-2 and let B_(n,r,eta)=Tr(nu_r*A_(n,eta)). For n<r,
the expression

    nu_r*A_(n,eta)
      =(-1)^n*(zeta^2-zeta)*(1+zeta)^(r-1-n)
                      *P_(n,eta)(zeta)

is a polynomial in zeta with rational coefficients, degree at most
r+1<=p-1, zero constant coefficient, and zero value at zeta=1 when
viewed as a polynomial. Formula (8) proves

    B_(n,r,eta)=0 for 0<=n<r.                            (16)

At n=r only one denominator 1+zeta remains. Abbreviate
P(Z)=P_(r,eta)(Z), and divide exactly:

    (Z^2-Z)*P(Z)=(1+Z)*Q(Z)+2*P(-1).

The quotient has degree at most r+1<=p-1. Direct evaluation gives
Q(0)=-2P(-1), Q(1)=-P(-1). Equations (8) and (10) now give

    Tr((zeta^2-zeta)*P(zeta)/(1+zeta))=-p*P(-1),
    B_(r,r,eta)=(-1)^(r+1)*p*P_(r,eta)(-1).             (17)

The residue of this coefficient must not be evaluated before clearing
its p denominator. Since r<p, reduction of its explicit numerator gives

    p^r*r!*P_(r,eta)(-1)
      =sum_(a=0)^r binom(r,a)*eta^a*(-eta)^(r-a)
                                      *(-1)^(r-a)
      =(2*eta)^r mod p.                                 (18)

This is a p unit. In particular

    v_p(B_(r,r,eta))=1-r,                                (19)
    p^(r-1)*B_(r,r,eta)
      =(-1)^(r+1)*(2*eta)^r/r! mod p.

The negative valuation in (19) for r>=2 is essential. Killing earlier
traces does not make the first surviving coefficient integral.

### 3.4 The complete infinite tail is strictly deeper

Because nu_r belongs to P and (12) is integral, (9) implies for ALL n

    v_p(B_(n,r,eta))>=1-n-v_p(n!).                        (20)

For n>=r+1 this yields

    v_p(B_(n,r,eta)*d^n)
      >=(s-1)n+1-v_p(n!) > (s-1)r+1.                    (21)

Here is the strict inequality with all large n covered. For n<p,
v_p(n!)=0. For n>=p and r<=p-2,

    n-r >=n-(p-2) >(n-1)/(p-1) >=v_p(n!),

since n>=p. Multiplication by s-1>=1 preserves strictness. Thus no
large-index factorial jump, including n=p or higher prime powers, can
cancel the leading coefficient. The same estimates tend to infinity,
so tracing the convergent series term by term is legitimate.

Equations (16)--(21) show that only the n=r term survives at the lowest
valuation. Multiplying (19) by d^r proves (4). At r=p-2, r is odd,
(p-2)!=1 mod p by Wilson's identity, and Fermat's identity gives
2^(p-2)t^(p-2)=1/(2t). This proves (5) for BOTH eta. ET1 is complete.

The exclusion d=0 from ET1 is material: at d=0, gamma_d=1 and all the
traces in (16) vanish. Depth 1 is not covered by the convergence/tail
argument or the normalized-root assertion. No such endpoints are
silently included.

## 4. Applying the ladder to an ACTUAL solution

Assume the hypotheses of ET2. With d=X+1, direct division gives

    (X-zeta)/(zeta*X-1)=(1-mu*d)/(1-zeta*mu*d).

The SAME root gamma from accepted R10 lies in U_2 and solves this
equation. Uniqueness proves that its completion is gamma_d, rather
than one of the other p local roots. Also K has just one completion
over p, of degree e, so global trace on K equals local trace in L.
The p-adic formula is therefore a formula for the actual global number.

We must still prove global integrality of Y*gamma^eta. It is not a
consequence of membership in O_L. From unique ideal factorization,

    product_(sigma in Gal(K/Q)) sigma(A)=(Y).

Each of A and jA is an integral divisor of (Y). As
(gamma)=A/jA, both ideals

    (Y*gamma)=(Y)*A/jA,
    (Y/gamma)=(Y)*jA/A

are integral at EVERY prime. Hence both numbers belong to O. It follows
that (6) is an ordinary integer. Since X=-1 mod p,
Phi_p(X)=1 mod p and Y^p=Y mod p, so Y=1 mod p. In particular it is
p-free. Multiplying ET1 by Y proves exactly the valuation/residue
claims for Delta_(r,eta); no primitivity or principal generator of A
was substituted. This proves the first part of ET2.

The relation gamma*jgamma=1 gives |sigma(gamma)|=1 at every complex
embedding. Thus

    |Delta_(r,eta)| <=Y*sum_(c=1)^(p-1)
                      |zeta^(2c)-zeta^c|*|1+zeta^c|^(r-1)
                   <(p-1)*2^r*Y.

Every summand has the strict upper bound 2^r because p is odd. The
nonzero integer Delta_(r,eta) is divisible by p^k_r, so its ordinary
absolute value is at least p^k_r. This proves (7), with strictness.

The strongest individual trace bound occurs at r=p-2, since increasing
r multiplies its right side by p^(s-1)/2>1. R10 already proves

    Y>p^[1+(s-1)(p-1)]/2^(p-1).

The ratio of our last right side to this accepted right side is
2/[(p-1)*p^(s-1)]<1. Therefore no new height improvement or exclusion
follows from these individual bounds. Under GR11's accepted reduction,
s=2, which specializes the exact traces to valuations r+1.

At the last selector j(nu_(p-2))=-nu_(p-2), because in general
j(nu_r)=-zeta^(-r-2)*nu_r. Consequently
Delta_(p-2,-1)=-Delta_(p-2,1). Its leading residue changes sign,
as required by (5). Reciprocal orientation or a lost conjugation bar
cannot double this valuation. ET2 is complete.

## 5. The concrete local obstruction and the source boundary

Take d=p^2 and X=p^2-1 for ANY prime p>=5. ET1 gives a normalized
local root, and (5) gives

    v_p Tr(nu_(p-2)*gamma_d^eta)=p-1,
    Tr(nu_(p-2)*gamma_d^eta)/p^(p-1)=eta/2 mod p.          (22)

Since p-1<2(p-2), this is a counterexample to the local implication
asserting that the normalized expansion at every depth-two parameter
has trace divisible by p^[2(p-2)]. The family is proved symbolically;
no selected numerical test or search is a premise. It proves no
global existence, Phi_p(X)=Y^p, actual class equality, or counterexample
to a theorem whose hypotheses also require a Diophantine solution.

For an actual solution satisfying (C) at depth two, ET2 gives the same
exact valuation after multiplying by its p-free Y. Any use of a stronger
trace divisibility for that SAME quantity therefore needs an additional
argument or a changed auxiliary, not just the displayed binomial
expansion. We do not import a theorem by treating this missing step as
already established.

The inspected Mihailescu author copy, Section 5, printed pages25--27,
motivates the last selector and states a larger trace divisibility in
its lower-bound argument. Its standing hypotheses include an actual
solution and Vandiver's condition. The local computation here is not
a counterexample to those combined hypotheses or its Theorem 4.
Conjugation bars and the source's changing gamma/delta notation require
care: (1), (3), (6) fix every quantity here, and both reciprocal
orientations are covered. The accessible PDF text and HTML agree on
the relevant exponent; attempted pixel screenshots failed. Final
publisher identity, a visual typesetting check, possible corrections,
and the whole external theorem are not certified. No source-refutation
or novelty claim is made.

ET3 is a precise local inference limit, coupled to a new exact actual
trace formula. It is not an unrestricted assertion that a whole family
of scalar, class-group or local methods cannot work.

## 6. Failed approaches and the genuinely remaining gap

**F1: promoting cancellation to large divisibility.** Earlier trace
coefficients vanish exactly, but the first surviving coefficient has
valuation 1-r, not zero. Discarding that denominator would replace
(s-1)r+1 by sr or more. Equations (17)--(21) retain it and prove no
tail cancellation. This failed inference is the reason for the packet.

**F2: extending center-0 even selection at center -1.** For even weights
n_c=n_(-c), pairing gives
sum n_c/(1+zeta^c)=(sum n_c)/2 exactly. The first-moment calculation
therefore differs from GR0's sum n_c*zeta^c. Moreover normalization by
1+zeta introduces a leading cyclotomic unit at infinity; its p-th root
in K has not been proved. A primary local root of the normalized number
does not supply that global leading root. No center-0 height bound is
transferred by replacing the center or by silently treating the unit as
a p-th power. This is an identified failed construction, not a new
universal obstruction theorem.

**F3: many exact traces versus an actual height improvement.** The
individual bounds are weaker than R10. Their simultaneous residues
do not themselves imply statistically independent conditions, a
nonzero small linear combination, or a sharper all-embedding bound.
Constructing such a controlled combination remains a possible route.

**F4: class equality versus principality or local roots.** The proof
works with (C), not [A]=1. Existence of (3) at an ordinary X does not
give (C), a global gamma, or a solution. Conversely nontrivial minus
classes outside (C) are untouched. No real-unit or ideal-class
obstruction is declared automatically satisfied or impossible.

**F5: published coverage.** The 2026 Chen--Mihailescu publisher abstract
is explicitly for distinct odd exponents; it cannot discharge q=p.
No new operative proof from that paper is used here. Bounded searches
did not locate a correction resolving this precise trace comparison;
that is not a claim that none exists. Complete unrestricted signed
diagonal classification, the exceptional actual sector, and the full
annual problem remain open in this packet. Publication overlap is open.

## 7. Sources, literal read scope, and worklog

Primary references:

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf),
  B4 setup and part(b), page2 lines59--61/67--71. Neighboring/preliminary
  text returned incidentally but was not investigated or reproduced.
- P. Mihailescu, *Class Number Conditions for the Diagonal Case of the
  Equation of Nagell and Ljunggren*, Developments in Mathematics16
  (2008),245--273, [DOI](https://doi.org/10.1007/978-3-211-74280-8_15).
  [Author-posted record](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren)
  and [accessible author PDF](https://www.researchgate.net/profile/Preda-Mihailescu/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren/links/546326840cf2c0c6aec1e13c/Class-Number-Conditions-for-the-Diagonal-Case-of-the-Equation-of-Nagell-and-Ljunggren.pdf).
  Version2.0 dated September17,2007; not asserted publisher-identical.
- B. Bartolome and P. Mihailescu,
  [arXiv:1412.5798](https://arxiv.org/pdf/1412.5798), complete Theorem2.2
  statement freshly read here, no fresh Appendix or proof import.
- H. Chen and P. Mihailescu,
  [2026 publisher record](https://doi.org/10.1007/s11401-026-0018-7),
  abstract/domain only freshly inspected; distinct exponents only.

The source selector is attributed. The exact general-r trace algebra,
all-index tail control and actual integrality step are the proposed
new hand reconstruction, not a copied external proof or a novelty claim.
The sources JSON supplies literal line/page ranges, failed access and
the distinction between this fresh rotation and older source reads.
No binary download, binary hash, cache write or full-paper redistribution
occurred. Public bounded web calls only; no CUA/native browser, contact,
charge or bypass. The broken author-record download link returned404;
its publicly linked profile path then yielded PDF text. The CiteSeer
endpoint returned Internal Error; all three screenshot attempts returned
Cache miss. These are source-read limitations, not approval blockers.

Work sequence: exact unused-prefix check; complete local official statement,
R10/GR11 and EACH authority MDJSON reads; current map observation; bounded
primary theorem/proof and status search; hand coefficient/trace calculation;
reciprocal-sign and tail checks; actual all-prime denominator clearing;
comparison with the accepted norm bound; complete proof, failures and
obligation ledger; documentary-only freeze preparation. No corresponding
NEW R25/R26 review or exploratory files were accessed. The immediate own
JC15 review parent is frozen and independently released; it is not a
mathematical input. IT12's later acceptance is unrelated context.
The first final readback clarified that the local counterfamily supplies
no Y; it does not assert that these ordinary X have no possible Y.

The initial budget reading supplied by the coordinator was77% TOTAL of
authorized weekly reset1792874445; the ceiling remains90% TOTAL with
integration/review reserve and no automatic later-window spending.
Fresh final telemetry and exact compact guards are in the baseline.

## 8. Complete natural obligations and constructor dispositions

Every row is a constructor hand check, not an independent audit.

| ID | Obligation and disposition |
|---|---|
| ET12-O01 | Official2025(b) only; D is a restricted signed prime diagonal, degree p-1 versus term count p. Checked. |
| ET12-O02 | Exact local p>=5 and actual p>=37 domains are separate; no endpoint3 or annual reduction inserted. Checked. |
| ET12-O03 | C concerns the unique ACTUAL A and is not principality/local solvability. Kept explicit. |
| ET12-O04 | d has finite exact depth s>=2, t a p-unit; d0/depth1 excluded, both ordinary X signs allowed. Checked. |
| ET12-O05 | Complete accepted R10/GR11 bodies and EACH MDJSON read, old WHOLE2 roles disclosed without self-review. Checked. |
| ET12-O06 | Eisenstein/local integral basis and p-only completion; v_p versus v_P normalizations consistent. Checked. |
| ET12-O07 | 1+zeta is a GLOBAL unit, mu and nu_r integral at every prime; no fractional ideal qualifier lost. Checked. |
| ET12-O08 | Local quotient (3) and global quotient (1) agree by direct d=X+1 substitution; both reciprocal orientations fixed. Checked. |
| ET12-O09 | Binomial coefficient identity (11) includes (-1)^n and correct zeta exponent; eta sign tracked. Checked. |
| ET12-O10 | p^n n! A_n is integral for EVERY n; no incorrect global inversion of n! or n<p tail cutoff. Proved. |
| ET12-O11 | Legendre bound and convergence include factorial jumps at n=p and all larger indices. Proved. |
| ET12-O12 | F_eta(d) lies in U2; exact normalized-root uniqueness, not any local root, identifies gamma_d^eta. Proved. |
| ET12-O13 | Polynomial trace formula degree<=p-1 has correct constant term; degree p is not admitted. Proved. |
| ET12-O14 | Trace(P O_L)=p Z_p by the integral basis; supplies the needed tail p factor. Proved. |
| ET12-O15 | Trace(mu)=e/2 by reciprocal pairing; no rational denominator prime issue. Proved. |
| ET12-O16 | For n<r polynomial degree r+1<=p-1, zero constant/value at1; exact trace cancellation including n0. Proved. |
| ET12-O17 | At n=r divide by1+Z, Qdegree<=p-1, Q0=-2P(-1),Q1=-P(-1). Proved. |
| ET12-O18 | First nonzero trace coefficient is (-1)^(r+1)pP_r(-1); sign and one p factor exact. Proved. |
| ET12-O19 | p^r r!P_r(-1)=(2eta)^r modp, nonzero since1<=r<p; coefficient valuation1-r retained. Proved. |
| ET12-O20 | ALL later trace terms have strictly deeper valuation by n-r>v_p(n!), including n>=p. Proved. |
| ET12-O21 | Tail converges and can be traced termwise; its terms cannot cancel the unique minimal one. Proved. |
| ET12-O22 | Exact valuation and residue (4) for every r and eta; no mere lower bound promoted to equality. Proved. |
| ET12-O23 | Last residue uses r=p-2 odd, Wilson and Fermat; eta/(2t) nonzero. Proved. |
| ET12-O24 | Global canonical root equals its local branch; no arbitrary local-to-global lift introduced. Proved using exact R10. |
| ET12-O25 | Both Ygamma and Y/gamma integral at EVERY prime from product of actual conjugate ideals; no principality presumed. Proved. |
| ET12-O26 | Y>1,p-free,Y1modp and global/local trace agreement give ordinary integer Delta with same exact residue. Proved. |
| ET12-O27 | Norm-one at every embedding, strict |nu|<2^r and nonzero integer divisibility imply (7). Proved. |
| ET12-O28 | Strongest individual bound occurs at r=p-2 and is weaker than R10 by exact ratio2/[e p^(s-1)]. Checked. |
| ET12-O29 | jnu_r=-zeta^(-r-2)nu_r; highest two reciprocal traces are exact negatives, not different valuations. Proved. |
| ET12-O30 | GR11 leaves s2 only underC; actual exact trace then p-1 at last level, with no class-number inference added. Checked. |
| ET12-O31 | Symbolic d=p² local counterfamily disproves ONLY the local higher-divisibility implication; no actual Diophantine counterexample asserted. Checked. |
| ET12-O32 | Inspected source has extra actual/Vandiver hypotheses and gamma/delta notation; Theorem4/final publisher/errata not recertified or refuted. Limit explicit. |
| ET12-O33 | Fresh full Section5 text and bounded other statements distinguished from unread pixels/foundations; failed accesses recorded. Checked. |
| ET12-O34 | Center-0 selection transfer, leading cyclotomic unit, joint trace combination and nontrivial minus-class gaps all retained. No failed route hidden. |
| ET12-O35 | No new exclusion, useful height bound, unrestricted prime range, annual solution or publication priority claimed. Checked. |
| ET12-O36 | No mathematical execution or source/author/old replay; only NEW documentary helper; TWO OTHER whole audits required before promotion. Checked. |
