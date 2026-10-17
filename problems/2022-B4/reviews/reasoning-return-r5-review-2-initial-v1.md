# Initially blind whole R2: rational-base fibers and the ordinary A/B obstruction

2026-10-17 UTC. Independent reviewer /root/review_2017_coarsening_r1.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
The new constructor and root contributed to R5 and are not independent
auditors. I did not construct F5A–F5E.

**Verdict:** all42 author obligations reconstruct in their stated
partial/conditional scopes; no substantive defect or required repair
was found. The strict q bound, complete eventual fiber description,
ordinary residue equivalence, arbitrary-expansion matching, exact-nine
conditional conclusion and real/10-adic distinctions have complete
arguments. Neither an infinite positive ordinary avoiding lift nor
termination of the restricted map is proved.

I authored the OLDER accepted R4 E1–E2/V1–V4 packet and earlier reviewed
complexity/R3 work. This is independent whole review of NEW R5,
not an independent re-audit of my old R4 theorem. Its accepted interface
was supported by two other whole audits and retains its exact scope.
The root carry note is unverified context and is proved again in R5;
it is not silently accepted as a theorem.

## 0. Exact target, reads and domain

Read the ENTIRE26928B candidate, all42 obligations, complete failure
ledger, full source audit/JSON, full worklog, root contribution note,
and all declared accepted proof bodies/scopes. Large combined tool
outputs were truncated; the missing ranges were explicitly reread
in bounded calls, including the complete R4 header/§0 and finite
representation facts. No argument is inferred from an omitted output.

Target main SHA256:
f08f3e579f9ddeec52746060ab81aec6055f1ecfce24fa2031608eadb7743bef.
Author freeze SHA256:
29a0ba60beda79572326525a2ab5fe20b23f0aff1c4129fc9645a86b83ff4601.
No new R5 peer findings were read before this full report, ledger,
source and integrity freeze. No math program/CAS/scan/old rerun was used.

The official2022 B4(b) was directly reopened: positive ordinary starts,
inclusive a0*b0>=600, simultaneous old-pair updates and the equality
question. No preliminary trapping proof is reproduced. The restricted
A/B input is only the accepted d1/r0 family, with full-time h blocks
(0,0) or(-1,1), block residues X0 or81 mod100 and
100X'=121X-w. Its positive infinite ordinary realization gives the
admissible pair(60X0+1,60X0). That realization does not identify all
contest avoiding paths with A/B.

## 1. Representation convention, finite uniqueness and global placement

Fix q>=2,p=q+1,beta=p/q, digits0,...,q and1/q weights. Modified
division qN=pN'+a,0<=a<p has N'=floor(qN/p)<N for positive N,
so produces a finite canonical representation. At fixed length an
integer value uniquely determines its last digit qN modp and
integer predecessor. Induction gives uniqueness, with leading
zeros allowed only to fix a length. Conversely any integer next
state with a digit in the full alphabet recovers that same
canonical predecessor, proving append admissibility.

For any nonnegative integer N the least valid digit is
qceil(pN/q)-pN in0,...,q-1. If N=0 modq the full choices are0,q;
otherwise there is exactly one digit in1,...,q-1. Thus every
finite prefix extends infinitely, including the root zero path.

A global expansion is an INDEXED sequence with zeros at every
sufficiently high index, all finite prefixes in0*L and value
(1/q)sum a_i beta^i. Translating EVERY index by -M is a bijection
of its whole fiber to the fiber at beta^(-M)V: the finite prefix
words are unchanged apart from leading zeros. For a fixed positive
V choose ONE M with beta^(-M)V<1/q. Nonnegative coefficients force
every digit of index>=0 to vanish in EVERY expansion of that value.
All are then root words with the same placement. This works for an
arbitrary fiber, not only a finite list selected in advance.
Repeated leading zeros are not different indexed representations.
Zero has only the all-zero expansion.

## 2. F5A: strict tail endpoint and the q bound

For a root word with real value rho,

    beta^k rho=N_k+T_k,
    T_k=(1/q)sum_(j>=1)a_(k+j) beta^(-j), 0<=T_k<=q.

Equality T_k=q would require every suffix digit to equal q.
Then the integer recurrence would give

    q(N_(n+1)+q)=p(N_n+q)

throughout that suffix. Coprimality forces q^m to divide the
fixed positive N_k+q for all m, impossible. Hence T_k<q, and
N_k is in the HALF-OPEN interval(beta^k rho-q,beta^k rho].
That interval has exactly q integers, including at integral
endpoints.

Any q+1 distinct infinite words can be separated at ONE finite
level (take the largest of finitely many pairwise first
differences). Fixed-length uniqueness makes their prefix values
distinct, contradicting that interval count. Selecting q+1
members also excludes an infinite fiber. Thus root fibers have
size<=q, and the common global placement gives the same bound
for all positive real fibers. The q2 boundary and zero singleton
are handled. There is no q1 assertion.

This proposed ten bound at11/10 still permits nine. It is a
separately proved endpoint deduction, not a claimed exact
quotation or priority improvement over AFS Proposition37.

## 3. F5B: integer intervals, extremal paths and the ordinary iff

Children of N are the integer interval from ceil(pN/q) to
floor(pN/q)+1. For p=q+1 the next parent's first child equals
floor(pN/q)+2. Thus consecutive parents have consecutive,
disjoint child intervals, and the full level is exactly
0,...,G_k-1 with G_0=1,G_(k+1)=ceil(beta G_k).
This also proves its lexicographic/value ordering.

Order is preserved under arbitrary continuation: the difference
of next numerators for two distinct ordered parents is at least
p-q=1; next values are integers and remain strictly ordered.
Consequently rho is nondecreasing on infinite admissible words.
It need not be strictly increasing.

Consider a nonempty fiber, and in the F5B conclusions size s>=2.
If two fiber prefixes at one level enclose an intermediate
integer label, that label is admissible and has an infinite
continuation. Its word lies between the two bounding words, so
monotone rho forces its value to be the same. Thus no label holes
occur. The finite q bound permits one common level after ALL s
paths separate. At every later level they are exactly s
consecutive labels; increase that level until the least is
positive.

Write the largest as H_n and smallest as H_n-s+1. Constancy of
their width in the recurrences gives e_n-d_n=s-1. Thus the top
digit is0<=d_n<=q-s+1<=q-1 and its path is the ordinary ceiling
orbit. The path H_n-c has digit d_n+c,0<=c<=s-1. The bottom
digits are maximal; middle digits are1,...,q-1 and unary.
“Common level” means a common index across all paths, not a
common prefix word after the paths have separated.

It follows that a global fiber of size>=r,2<=r<=q, gives a
positive ORDINARY ceiling orbit with every digit in0,...,q-r+1.
For the reverse implication, advance any such positive orbit
until H0>r-1 and set Z_n^(c)=H_n-c,c0,...,r-1. Their digits
d_n+c lie in0,...,q, so actual positive integer trajectories
with canonical finite seeds exist. All have the same growth
coefficient C_H. Explicitly the extra constant digit series
sums to c because p-q=1, cancelling the seed subtraction c.
Pad all r seeds to ONE length m, also chosen so
beta^(-m)C_H<1/q. They give r distinct root expansions of that
same value. Distinct offsets give distinct tails. No inverse
limit or changing integer starts replaces this all-time
ordinary construction.

The ceiling digit is the least residue of -H modq. Therefore the
permitted residue set is exactly

    S_r={0,r-1,r,...,q-1}, size q-r+2.

For r2 it is ALL residues; for r=q it is{0,q-1}; q2/r2 is
valid. At11/10, at least9 expansions is equivalent to a positive
ordinary ceiling orbit staying forever in{0,8,9};10 expansions
is equivalent to one staying in{0,9}, using F5A. Neither
existence nor exclusion is supplied.

## 4. F5C: bounded-carry rigidity and matching EVERY expansion

A positive A/B lift has X_j>=81 and all full Q steps increase.
It has infinitely many B blocks, since an all-A tail would make
one fixed positive integer divisible by every power of100.
The REAL growth coefficient and uniform tails are

    C=X0-sum_j w_j100^j/121^(j+1)>=81-1/21>0,
    Q_n=C beta^n-U_n, |U_n|<=1.

These real sums are not equated with their10-adic evaluations.

For ANY bounded ordinary integer correction c_n=Q_n-Z_n with
digits0<=d_n<=10, subtracting recurrences gives
10c_(n+1)=11c_n+h_n-d_n. If c<=0, the next carry is
<=floor((11c+1)/10)<=c. A later h=-1 forces zero negative;
subsequent block-first h<=0 strictly decreases a negative
carry, contradicting boundedness. If c>=10, it cannot
decrease. A later h1 forces10 to at least11, and subsequent
block-second h>=0 strictly increases it, another contradiction.
The c10 endpoint uses ceil(-1/10)=0 correctly.

Hence all c_n lie in1,...,9. Now
10(c_(n+1)-c_n)=c_n+h_n-d_n is in[-10,10]. The extreme
multiples give forbidden exits0 or10. Thus the carry is
CONSTANT c in1,...,9 and d_n=h_n+c. Conversely every such
constant fits the full alphabet. No causality is assumed.

The new matching step covers an ARBITRARY expansion, not just
bounded translations already chosen. Choose ONE m long enough
for all nine finite seeds Q0-c and so V=beta^(-m)C<1/10.
The nine constructed expansions are admissible and evaluate
to V. Take ANY global expansion of V; its nonnegative
coefficients force it into the same root convention. Its
prefix Z_n=N_(m+n) satisfies

    Z_n=C beta^n-T_(m+n), 0<=T_(m+n)<10.

Thus c_n=Q_n-Z_n=T_(m+n)-U_n is an ordinary bounded integer
sequence, with the exact common time index and growth
coefficient required for the lemma. It is one constant
c1,...,9. Fixed-length uniqueness recovers the ENTIRE
length-m seed, and d=h+c recovers the entire remaining
tail. Hence the full global fiber at V, and by one common
index translation at C, has EXACTLY9 expansions. This is
conditional on the hypothetical positive ordinary lift.

Infinitely many B blocks give infinitely many h=-1,h1.
So exactly c1,...,8 are eventually minimal, exactly c2,...,9
eventually maximal, and exactly c2,...,8 eventually unary.
The two extremes have infinitely many branching positions.
These are eventual tail statements, not extra radix copies.

For the ordinary ceiling growth map G(z)=lim beta^(-n)T^n(z),
the eight seeds Q0-c,c1,...,8 have growth coefficient C.
Any other positive ordinary ceiling seed with that coefficient
has the same bounded difference and hence one constant c1,...,9.
The value c9 is impossible because it requires digit10
infinitely often. Thus its ENTIRE positive integer fiber is
exactly{Q0-8,...,Q0-1}. Monotonicity of T gives nondecreasing
G; an eight-point plateau is a necessary condition, not a
contradiction or an established ordinary orbit.

## 5. F5D: different real and10-adic images

For unrestricted binary words the real image is I=[0,1/21].
The branch maps f_i(t)=(i+100t)/121 send I to two overlapping
closed intervals whose union is I. Recursive inverse branch
choices remain in I. Their bounded residual multiplied by
(100/121)^N tends to zero, proving surjectivity. This says
nothing about ordinary admissible loops.

In Z10, if two words first differ at j, their difference is

    (100^j/121^(j+1))*(epsilon+100t), epsilon=±1.

The last factor is a unit at BOTH2 and5. Therefore its two
valuation exponents are exactly2j. This proves injectivity
and2^N different prefix classes modulo100^N. The space is
a ring/inverse limit, not a field.

If Psi_10(w)=X0 is an ordinary POSITIVE integer, the identity
121X0-w0=100Psi_10(shift w) implies ordinary divisibility
by100. Its quotient is an ordinary positive integer:
121X0-w0>=120. Cancelling100 is legitimate because it is
injective on both completions, not because it is a unit.
Iterating gives all positive ordinary quotients and exactly
the residues0/81, hence the accepted complete A/B controls.
Conversely an actual ordinary lift gives the finite series
plus(100/121)^N X_N. This remainder tends to0 at both primes
since every integer X_N has nonnegative valuations. This
proves the stated iff, preserving the distinction from
ordinary REAL evaluation.

Finite compatible congruences may have positive representatives
that change with N. Neither they nor real interval surjectivity
produce ONE positive ordinary integer in the full10-adic image.

## 6. F5E: strict interval, exact local witness and source scope

All-B ordinary tails are also impossible: Y=21X-1 is positive
and would satisfy100Y'=121Y indefinitely, forcing arbitrary
powers of100 to divide one fixed positive integer. Both
letters therefore occur infinitely often in every tail.
The real suffix errors satisfy0<R_j<1/21 and

    gamma^j C=X_j-R_j, gamma=121/100,
    {gamma^j C}=1-R_j in(20/21,1).

This is BLOCK time, distinct from the beta full-time convention.
No endpoint or all-time converse is smuggled in.

At a single transition the integer discrepancy121R-100R'
can fall outside{0,1}. The given exact witness has
R1=1/121,R0=342/14641,X0=62,X1=75. Both errors are in the
open interval;121R0-100R1=2 and121*62-100*75=2, so
gamma(62-R0)=75-R1. This refutes only a LOCAL binary-digit
inference. It is not an all-time interval counterexample or
an actual avoiding start.

Actual AFS conventions, full alphabets and theorem hypotheses
were checked. Its bound permits11 at11/10; Corollary38's
p>=2q-1 fails. AEV's stronger assertions remain conjectural.
Original DM's residue problem has a NONEMPTY PROPER allowed
set; the proven termination result is singleton-only.
The two- and three-class sets in F5B are not covered, and
the full-residue r2 case cannot be inserted into that
proper-set question. Source conjectures and a conditional
fractional-part theorem are not termination proofs.

## 7. Final disposition

All42 rows pass in the scope in the companion ledger. No
substantive issue was found in F5A–F5E. Acceptance should
remain a SCOPED partial result after the other fresh whole
audit and coordinator reconciliation.

The key ordinary questions remain open: existence/termination
of the restricted all-time ceiling or A/B trajectories, and
whether the binary10-adic image contains a positive ordinary
integer. The q bound still permits nine, and excluding this
restricted family would not settle all contest avoiding paths.
No full annual answer, no-ninefold theorem, ordinary infinite
counterexample, novel method or source-proof repair is claimed.

