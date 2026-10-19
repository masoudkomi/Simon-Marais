# Primitive content at conductors with at most two prime factors

2026-10-19 UTC. **Candidate proof - unverified.** Constructor B,
/root/review_2022_complexity_r2. Requested inherited gpt-6.1-sol/max;
independent effective-setting readback unavailable. TWO OTHER initially
blind ENTIRE WHOLE nonconstructor audits and coordinator reconciliation
are required. B is excluded. Scope is official2020 B4(b) ONLY.

This is an actual binary/Sidon obstruction, not a construction of a norm
tuple. At an odd conductor with at most TWO DISTINCT prime factors, the
primitive character value of any nonempty Sidon subset has no ordinary
prime divisor coprime to the conductor. Consequently, for an ACTUAL
planar difference set at such a conductor, the SINGLE primitive value
has ordinary content1 and exact reciprocal clearing denominator q.
The accepted AR19 result required ALL character orders together at a
general composite conductor. No numerical order is newly excluded here.

Part of the underlying coefficient bound is already classical: Turyn's
1965 Lemma5 bounds an ordinary divisor m of a nonzero binary primitive
character value by 2^(omega(v)-1). The present hand argument uses the
Sidon property to remove the remaining content2 case when omega(v)=2.
No priority or literature-nonoverlap claim is made. In particular this
packet is NOT a new proof of Turyn's general bound.

## 0. Domain, accepted inputs and roles

The official question is to determine taut integers n>=2. Use the
accepted cyclic planar dictionary and put

    q=n-1>=2, k=q+1, v=q^2+q+1.

An ACTUAL planar D is a k-subset of C_v satisfying

    D D^- = q[0]+N, aug D=k, k^2=q+v.                 (0.1)

Here N is the full group sum. Every nonzero ordered difference of D
occurs exactly once, so D is Sidon in the following precise sense:

    x-y=x'-y' !=0, x,y,x',y' in D
    implies (x,y)=(x',y').                            (0.2)

The new combinatorial lemma assumes only a NONEMPTY subset satisfying
(0.2), and does not presume saturation. We impose v odd, v>1 and at
most two DISTINCT prime factors; repeated prime powers are allowed.
All official v are odd, but many have three or more distinct prime
factors and are outside the new conclusion. q1/n2 is not a new theorem
case. No preliminary existence argument is investigated or reproduced.

Fresh COMPLETE accepted R18 and AR19 bodies and EACH current acceptance
MD/JSON were read. A clipped middle R18 read was recovered exactly in
lines339--510; AR19's last nine lines were separately recovered. Their
INTEGRAL and ALL-orders qualifiers govern all comparisons. In particular:

* R18's prime-conductor integral norm-to-binary bridge is not a composite
  sufficiency theorem. Its general-composite denominator statement uses
  the whole character tuple.
* AR19's integral subfield unit obstruction is explicitly repaired by a
  quadratic unit inside the FULL polygon cyclotomic field. Neither that
  prescribed subfield nor the original false fractional SQ14/SQ15
  clauses can exclude an actual full-field realization.
* AR19 proves ordinary content1 and reciprocal denominator q jointly
  over ALL nontrivial character orders. The new conclusion below needs
  one primitive value, but has the stated restriction on omega(v).

B authored older R18/AR19/SQ14 and other accepted arithmetic packets,
and reviewed other inputs. These are imports in their TWO OTHER accepted
scopes, not independent self-recertifications. Root supplied only a
generic research goal, no new R20 inference. No corresponding NEW ET12
review or other active peer content/inventory/hash/metadata was accessed.

## Claims GR20A--GR20D

Let S be a nonempty Sidon subset of an odd C_v, v>1, omega(v)<=2.
Let zeta be a primitive complex v-th root and

    alpha_S=sum_(x in S) zeta^x in O_K=Z[zeta].

**GR20A, reduction and blocks.** If ell is a rational prime not dividing
v and alpha_S is in ell O_K, the reduced binary mask has zero primitive
Fourier values in characteristic ell. For v=r^a s^b, r,s distinct odd
primes, the mask decomposes into cosets of the subgroup of order rs;
each r-by-s binary block has zero mixed Fourier frequencies. In the
one-prime case the analogous blocks have length r and constant entries.

**GR20B, actual Sidon obstruction.** Such divisibility is impossible.
Thus alpha_S!=0 and alpha_S is not in ell O_K for ANY prime ell not
dividing v. The characteristic2 case is part of the proof, not obtained
by lifting an integer rectangle congruence of size2.

**GR20C, primitive content and reciprocal denominator.** If D is ACTUAL
in(0.1) and omega(v)<=2, then alpha=alpha_D has ordinary content1:

    alpha/e integral, e in Z_(>0), implies e=1.       (0.3)

For EVERY integer h, including0 and negative,

    h/alpha integral IFF q divides h.                (0.4)

These statements concern the FULL cyclotomic field of the actual
primitive character. They do not require a chosen multiplier subfield.

**GR20D, no completion on a contentful primitive ideal.** At such an
official v, let beta be an integral element of K with beta*c(beta)=q.
If beta is divisible by an ordinary integer e>1, NO choice of the
other character orders can complete beta to an actual planar D.
The same holds for every norm-q generator of its SAME ideal, for
Galois conjugates and for translation phases. This rules out those
prescribed ideals/values, not all possible ideals or the order q.

## 1. From divisibility to characteristic-ell primitive vanishing

Represent S by its binary polynomial

    A(X)=sum_(0<=x<v) a_x X^x, a_x in{0,1}.

Since O_K=Z[zeta]=Z[X]/(Phi_v), alpha_S in ell O_K means
the class of A is zero in O_K/ell O_K. Equivalently

    Phi_v(X) divides A(X) in F_ell[X].                (1.1)

This uses the integral cyclotomic presentation and is not a claim that
the reduction O_K/ell is a field. Because ell does not divide v,
X^v-1 is separable in characteristic ell. Its Phi_v factor has exactly
the primitive v-th roots as roots in an algebraic closure. Thus(1.1)
annihilates EVERY primitive frequency, not just one residue-field root
or one irreducible factor. Conversely this simultaneous vanishing
would imply(1.1); we need only the forward direction.

Put h=rad(v), L=v/h. For v=r^a or r^a s^b one has

    Phi_v(X)=Phi_h(X^L).                             (1.2)

For a direct check in characteristic0, a root z on the right satisfies
ord(z^L)=h. For each prime r|v, the equation
max(v_r(ord z)-(v_r(v)-1),0)=1 forces v_r(ord z)=v_r(v),
and no other prime occurs. Hence ord z=v. Both polynomials are monic
and their roots have no repetitions; the degrees also agree. This
proves the identity over Z and hence after reduction.

There is a UNIQUE decomposition

    A(X)=sum_(t=0)^(L-1) X^t A_t(X^L), deg A_t<h.    (1.3)

The ring F_ell[X] is a free F_ell[X^L]-module on1,X,...,X^(L-1).
Taking the quotient by Phi_h(X^L), or dividing each A_t by Phi_h,
shows that(1.1) implies

    Phi_h(Y) divides A_t(Y) for EVERY t.             (1.4)

No cancellation between different t is possible in this direct module
decomposition. Each A_t is binary, and its support S_t is the subset
of a coset t+L C_h inherited from S. At least one is nonempty. It is
Sidon in C_h: two distinct ordered nonzero equal differences there
would remain distinct equal differences after multiplication by L
and translation in C_v. A nonzero class mod h remains nonzero mod v
after multiplication by L. Thus it suffices to refute a nonempty
Sidon block at h=r or h=rs.

## 2. One-prime block

For h=r, a prime>=3, (1.4) and deg A_t<r imply

    A_t(Y)=c_t(1+Y+...+Y^(r-1)) in F_ell[Y].

All its binary coefficients are congruent. Since0 and1 are distinct
in EVERY prime characteristic, they are all equal as ordinary binary
entries. A nonempty block is the full coset of the subgroup C_r.
Inside a full coset, any fixed nonzero subgroup difference has r
distinct ordered representations. This contradicts(0.2). The argument
allows arbitrary a, and does not assume v itself prime.

## 3. Two-prime block and mixed rectangles

For h=rs, use the CRT isomorphism C_h=C_r x C_s. Arrange a nonempty
block as an r-by-s binary matrix A=(a_ij). Frequencies with BOTH
coordinates nontrivial are exactly primitive h-th characters: r and
s are distinct primes. Since ell does not divide rs, choose primitive
r-th and s-th roots xi,eta in an algebraic closure of F_ell. All

    F(u,w)=sum_(i,j) a_ij xi^(ui) eta^(wj)

vanish for u!=0 mod r and w!=0 mod s by(1.4). Finite Fourier
inversion is valid, because rs is invertible. The geometric sums
sum_i xi^(ui) vanish for u!=0, and equal r for u0; similarly for s.
These identities give the inverse matrix directly. With no mixed
frequencies left it has the form

    a_ij = b_i+c_j in the algebraic closure.          (3.1)

Therefore every rectangular difference is zero in F_ell:

    a_ij-a_i'j-a_ij'+a_i'j'=0 mod ell.              (3.2)

This last expression is already in the prime field, so no descent
of the individual b_i,c_j is needed. One can use the concrete identity
a_ij=a_i0+a_0j-a_00 mod ell instead. The CRT choice of roots may
rescale the two frequency indices by units; it still ranges over
ALL pairs of nonzero indices. No primitive frequency is lost.

### Odd ell: exact integer rectangles

The ordinary integer on the left of(3.2) lies between-2 and2.
For ell>=3 the only divisible value is0. Hence the SAME binary
matrix has zero integer rectangular differences. Its rows differ
by integer constants. If a row contains both0 and1, any constant
shift preserving binary entries is0, so all rows are identical.
A nonempty matrix then contains a full vertical C_r coset. If every
row is constant, a nonempty row is a full horizontal C_s coset.
Both contradict Sidon as in Section2. This includes ell3 exactly;
no strict-inequality endpoint is omitted.

### ell2: complement rows and the Sidon pair count

Here a rectangular difference may be+2 or-2. Lifting(3.2) to an
integer equality would be FALSE. Instead fix the first row B. The
formula after(3.2) shows that EVERY row is B or its binary complement
B^c. Interchange r,s if necessary so s>=5; two DISTINCT odd primes
cannot both be3. There are r>=3 rows, so one type occurs at least
twice. Call that repeated pattern T, with weight w.

If w>=2, choose two distinct columns in T and two different identical
rows. The two ordered within-row pairs have the same nonzero difference
(0,j-j') in C_r x C_s and are distinct. Thus Sidon forces w<=1.
If the complementary row type occurs at all, it has weight s-w>=s-1.
Within this one row its w'*(w'-1) ordered distinct pairs must inject
into the s-1 nonzero horizontal differences. But for s>=5,

    w'*(w'-1)>s-1 when w'>=s-1.

This is impossible. If the complementary type is absent, every row
is T. Weight w0 makes the block empty; weight w1 makes it a full
vertical C_r coset, again not Sidon. These exhaust zero weights,
one exceptional row, both repeated types, and all repeated rows.
No parity or generic-size assumption replaces the actual pair count.

Every nonempty block has now been contradicted, proving GR20A/B.
If alpha_S were zero, it would be divisible by any prime ell not
dividing v, giving the same contradiction. Thus it is nonzero too.

## 4. Actual content1 and the reciprocal iff

For D actual, character evaluation of(0.1) gives

    alpha*c(alpha)=q>0.                            (4.1)

Suppose alpha/ell is integral for some rational prime ell. Taking its
relative product gives q/ell^2, a rational algebraic integer, so
ell^2 divides q. Also gcd(q,v)=1, since v=q(q+1)+1. Therefore ell
does not divide v, contradicting GR20B. If alpha/e were integral for
e>1, every prime divisor of e would give this contradiction. This
proves(0.3), including the conductor primes without extending the
characteristic-ell Fourier argument to them.

If q|h, then h/alpha=(h/q)c(alpha) is integral. Conversely suppose
h/alpha integral and q does not divide h. Choose ell with
f=v_ell(q)>t=v_ell(h). At EVERY prime ideal P above ell, integrality
of h*c(alpha)/q forces

    ord_P(c(alpha)) >= (f-t)*ord_P(ell)
                       >= ord_P(ell).

Consequently c(alpha)/ell is integral at ALL those primes. At all
other primes it is integral because c(alpha) already is and ell is
a unit there. Hence it is an algebraic integer. Conjugating would
make alpha/ell integral, contradicting(0.3). No unramified shortcut
or arbitrary chosen prime valuation is required for this argument.
Negative h is covered by valuations/sign; h0 belongs to the q|h
branch and is not assigned a finite valuation. This proves(0.4).

This upgrades AR19's global content restriction to the primitive-order
component within this conductor sector. It does not assert an extreme
at EVERY prime, nor at every order or for every conjugate-ratio
displacement. R18's stronger prime-conductor ratio theorem is not
silently extended to composite v.

## 5. Whole-completion obstruction and its exact limits

Let beta be as in GR20D. If alpha=beta were the primitive value of
an actual D, (0.3) would be violated. This conclusion is independent
of ALL choices at proper character orders: changing those values
cannot change the prescribed primitive evaluation of the binary mask.

If another generator of the SAME nonzero integral ideal (beta) is
alpha=beta*u, then u and u^-1 are integral units. Therefore
beta in ell O_K IFF alpha in ell O_K. The same holds under a Galois
automorphism and multiplication by a root of unity. Requiring that
the generator additionally have exact norm q does not remove this
obstruction. More generally an actual primitive ideal cannot be
contained in ell O_K for any ordinary prime ell. Integrality of the
ideal and the FIXED full field are part of this assertion.

This is precisely where a unit repair cannot help: an integral unit
does not remove ordinary content. It is different from AR19's unit
correction of a norm discrepancy on an ideal. AR19's literal399-divisible
conductors have AT LEAST THREE distinct prime factors, so the present
lemma gives NO further exclusion of that family or its repaired beta.
No odd-degree/subfield obstruction is revived after its quadratic repair.

A concrete parameter-compatible diagnostic is q=36, v=1333=31*43.
Both31 and43 are prime (the only possible prime divisors below their
square roots are2,3,5, none divides). The element beta=6 in Q(zeta1333)
is integral with beta*c(beta)=36; (6) is an INTEGRAL principal ideal
of relative balance36 with no missing norm-unit correction. Nevertheless
neither6 nor ANY norm36 generator of this SAME ideal can be the
primitive value of an actual D, regardless of proper-order choices.
This is one hand diagnostic, not a parameter scan or a new claim that
q36 is nontaut: that order was already outside known necessary filters.

There is NO theorem here that every balanced ideal has content, that
every mixed q has at most two conductor primes, or that the remaining
content1 ideals admit or fail a joint integral Fourier lift. If q is
squarefree, (4.1) already prevents alpha/ell integral at every ell,
so the new content test adds nothing in that sector. For nonsquarefree
q it can remove prescribed primitive ideals, but does not evaluate
the alternatives, actual class/unit conditions or the annual target.

## 6. Literature, exact read scopes and failed routes

* The official PDF setup/(b), returned98--105, was freshly read. No
  preliminary proof was pursued. The saved complete statement was read.
* Richard J. Turyn, [Character sums and difference sets](https://msp.org/pjm/1965/15-1/pjm-v15-n1-p32-p.pdf),
  Pacific J. Math.15(1965),319--346: the original returned text572--636,
  including COMPLETE Lemma5 statement/proof, was read. Its bound already
  covers odd ordinary prime divisors when omega(v)<=2. OCR inequalities
  were checked against the supplied induction. A screenshot call did
  not yield inspectable pixels; no pixel or entire31-page proof audit is
  claimed. Later returned theorem fragments are context, not premises.
* Lam--Leung [author preprint](https://arxiv.org/pdf/math/9511209),
  Section2 Theorem2.2 and its COMPLETE supplied proof153--264, and
  Section3 Theorem3.3/proof381--413 were read, with the introduction's
  explicit characteristic0 restriction95--96. Their classical kernel
  and positive-cycle results motivate the block approach; they are
  NOT invoked as a finite-field theorem. No full-paper audit is claimed.
* Mahatab--Sampath [author preprint](https://arxiv.org/pdf/1401.7696),
  introduction and complete Lemmas2.1/2.2 and Theorem2.4 proofs0--449
  were read. Integral cyclotomic CRT non-surjectivity is classical
  context. Neither its full Smith algorithm nor its later proofs are
  executed or used to certify a compatible tuple.
* [Author-hosted Reed notes](https://people.reed.edu/~jerry/361/lectures/kummer.pdf),
  COMPLETE Appendix9.2(1505--1553) was freshly read. The finite
  geometric-sum proof is reconstructed above in characteristic ell,
  where invertibility of rs is explicit. No whole-note audit.
* Alexeev--Mixon [author preprint](https://arxiv.org/pdf/2510.19804),
  returned299--335 only, confirms that cyclic/desarguesian hypotheses
  and the Prime Power Conjecture are distinct. No best finite cutoff,
  full-paper proof, current-status exhaustion or priority certification.

The finite-field and binary arguments above are hand proofs, not
applications of an unread vanishing-sum classification. No primary PDF
was written/downloaded into the repository or cache; raw PDF hashes
are unavailable, and no redistribution licence is inferred.

Failed routes retained:

F1. Individual exact norm-q/unit-corrected entries do not automatically
lie in the integral cyclotomic CRT image. The published cokernel issue
does not by itself prove a contradiction for actual difference sets.

F2. Trying to make an ordinary class cancellation or anti-real unit
repair create global coefficient integrality merely repeats AR19's
failed bridge; the quadratic repair stays mandatory and visible.

F3. The initial two-prime odd-ell argument overlaps Turyn's general
coefficient bound. That discovery was reported to root and attributed,
not labelled a novel nonexistence theorem. Sidon is essential for the
separate content2 argument presented here.

F4. Lifting a characteristic2 rectangular congruence to integer zero
would be false because+/-2 can occur. Complement rows and actual
ordered-difference injectivity, rather than that invalid lift, close it.

F5. At three or more distinct conductor primes, the primitive Fourier
kernel is not the two-dimensional row-plus-column space. This proof
does not propagate to that case. No counterexample or universal
content1 theorem for that larger domain is asserted.

F6. Removing one prescribed contentful primitive ideal is not removal
of the actual order: other ideals may have content1. No prime-power
classification, actual mixed-order construction, unrestricted actual
exclusion, full annual solution or novelty follows.

## 7. ALL40 natural obligations and author hand dispositions

These are constructor checks, not either independent whole audit.

|ID|Disposition / complete obligation|
|---|---|
|GR20-01|CHECKED exact official(b), n/q/k/v dictionary; no preliminary proof.|
|GR20-02|CHECKED q>=2, nonempty actual D, q1 boundary not exported.|
|GR20-03|CHECKED actual ordered Sidon convention excludes ONLY nonzero repeated differences.|
|GR20-04|CHECKED v odd>1 and omega(v)<=2, distinct primes versus arbitrary powers.|
|GR20-05|CHECKED integral O_K=Z[zeta] quotient, alpha/ell means all residue-field factors, not one.|
|GR20-06|CHECKED ell not dividing v, separability and ALL primitive roots.|
|GR20-07|CHECKED exact radical-power identity(1.2), including both prime exponents1.|
|GR20-08|CHECKED unique block decomposition, direct free module and no cross-block cancellation.|
|GR20-09|CHECKED every block binary and at least one nonempty.|
|GR20-10|CHECKED Sidon inherited by subgroup-coset identification, nonzero differences stay nonzero.|
|GR20-11|CHECKED one-prime block quotient constant, ordinary binary coefficients equal in every characteristic.|
|GR20-12|CHECKED full subgroup coset has repeated nonzero ordered differences, prime>=3.|
|GR20-13|CHECKED two-prime CRT identifies primitive frequencies with BOTH indices nonzero.|
|GR20-14|CHECKED finite-field Fourier inverse, rs unit, geometric sums and index rescalings.|
|GR20-15|CHECKED missing mixed frequencies give row+column and every rectangular congruence.|
|GR20-16|CHECKED no unsupported descent of auxiliary row/column values is used.|
|GR20-17|CHECKED ordinary rectangle in[-2,2], exact odd-ell lift includes ell3.|
|GR20-18|CHECKED integer additive binary matrix either identical rows or constant rows; nonempty full coset.|
|GR20-19|CHECKED ell2 NOT lifted to integer zero; rows B or B^c exhaust possibilities.|
|GR20-20|CHECKED primes can be interchanged to give column size>=5, row count>=3.|
|GR20-21|CHECKED repeated pattern has weight<=1 by two distinct within-row pairs.|
|GR20-22|CHECKED complementary row, if present, violates w'(w'-1)<=s-1.|
|GR20-23|CHECKED absent complementary row leaves only empty block or full vertical coset.|
|GR20-24|CHECKED zero/one weights, both repeated types, one exceptional row and nonempty requirement.|
|GR20-25|CHECKED alpha_S0 would imply impossible divisibility, so nonzero is not presumed for arbitrary Sidon S.|
|GR20-26|CHECKED actual relative norm q from nontrivial character of(0.1).|
|GR20-27|CHECKED alpha/ell integral forces ell²|q by rational algebraic integrality.|
|GR20-28|CHECKED gcd(q,v)=1 excludes conductor primes; no ramified finite-field argument.|
|GR20-29|CHECKED content1 for every ordinary positive e, not ideal primitivity at every prime.|
|GR20-30|CHECKED q|h suffices for reciprocal integrality, including h0/negative h.|
|GR20-31|CHECKED converse selects deficient ell-adic exponent and uses ALL primes above ell.|
|GR20-32|CHECKED conjugation, other-prime integrality and local-to-global algebraic integrality; no assumed unramifiedness.|
|GR20-33|CHECKED no every-prime extreme or exact composite conjugate-ratio theorem exported.|
|GR20-34|CHECKED no proper-order choices can change a forbidden prescribed primitive value.|
|GR20-35|CHECKED SAME ideal generators differ by integral units; ordinary content persists under units/conjugates/phases.|
|GR20-36|CHECKED q36/v1333/(6) hand diagnostic only, not a numerical scan/new order exclusion.|
|GR20-37|CHECKED no application to AR19's >=3-prime conductors; mandatory quadratic repair retained.|
|GR20-38|CHECKED squarefree-q automaticity, remaining content1 ideals and global realization OPEN.|
|GR20-39|CHECKED Turyn overlap/classical attribution, actual primary read limits, no novelty/annual claim.|
|GR20-40|PROCESS full compact packet, final payload+manifest MODEL reads, separate documentary verification; TWO OTHER whole audits needed.|

## 8. Issue log and research chronology

No independent R20 review has occurred. Retained notes: R20-N1 exact
ordinary divisibility rather than an arbitrary ideal factor; N2 actual
binary/Sidon hypothesis; N3 full character order versus one finite-field
root; N4 two DISTINCT primes with arbitrary powers; N5 characteristic2
endpoint; N6 actual fixed full-field ideal, no fractional repair; N7
squarefree/three-prime limits; N8 published Turyn overlap and no priority.

Chronology: released immutable CM16 disposition after root's explicit
BOTH confirmation; narrowly checked this namespace unused; freshly read
R18/AR19/current authorities and official scope; rejected isolated tuple,
unit and CRT-only reformulations; derived the two-prime binary matrix
argument by hand, then its radical-block extension; located Turyn's
existing general divisor bound and marked the overlap; checked the
remaining Sidon/content2 step independently; saved the precise limited
actual completion obstruction. Root supplied no construction inference.
No mathematical program, scan, CAS, tests, old source/author/freezer or
certificate replay was used. No pending native child/PID or incomplete
search. Documentary code and compact preservation are separate payloads.

Fresh direct telemetry02:20:00UTC:81% TOTAL,10080minutes, reset1792874445,
ordinaryUsageAllowed true, legacy/by-limit agree, account label...ac3a.
Only this user-authorized window may be spent;90%TOTAL ceiling with
integration/review reserve. No Git/shared/old/cache writes, charges,
contact, bypass, spawning or third-party full-paper redistribution.
