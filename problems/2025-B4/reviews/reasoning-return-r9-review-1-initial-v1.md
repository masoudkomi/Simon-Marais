# R9: complete initially blind OTHER WHOLE audit 1

2026-10-18 UTC. Reviewer /root, nonconstructor of NEW R9. **Candidate proof
unverified; one limited radius-domain repair is required.** The entire six-
claim argument and all48 obligations were reconstructed by hand. This is
not acceptance, a numerical experiment, or an audit of only the source
objection. No NEW B R9 report, finding, ledger, source record or metadata
was read before this ENTIRE initial packet froze.

Target: reasoning-return-r9-candidate-v1.md,22574B,
SHA2568fae8c0dd3e951fd4c847954f75186b8969f1dbdec9592b8cebcbda8394a9aa2.
Constructor freeze2790B,
SHA25693eed518f1584c8e4f1a7cbe4d6229c9532caae4269d18cf0393c1f0e934aa8f.
All eleven constructor files, including the complete live log and freezer
source, were read. The author's freezer was not executed.

The sole defect found is R9R1-01: Section4 allows0<R<H and then says the
short-point sets contain e16. This is false at, for example,H2,R1/2.
Those sets then contain only0. The intended counterexample at R=sqrt(H)
is valid, as are its perturbation and cofactor arguments in the proper
radius domain. Require a versioned author correction to1<=R<H (or a
precise split of the equality statement from the nonzero-point assertion),
then BOTH affected reaudits. All other new implications pass within their
explicit scopes; no complete annual result follows.

## Independence, exact target and accepted premises

C constructed R9 and is excluded. Root supplied the generic assignment and
scope cautions, without a NEW R9 proof inference. Root's OLD UW exploratory
contribution, original-weight work and earlier source/R6/R8 review roles
are disclosed. They do not independently recertify those old accepted
premises. B is the other NEW R9 whole reviewer. Both initials must entirely
freeze before peer comparison. Requested gpt-6.1-sol/max is separate from
unavailable independent effective-setting readback.

Fresh official2025 Paper B page2 B4(b) gives all integer quadruples, n,q>=2.
Only the restricted signed prime-diagonal sector is addressed: term count p,
official degree p-1, exponent p, p>=37, |X|>=2. The accepted valuation input
gives p not dividing X-1; G_p(X)>0 makes Y>0 and its nontrivial size gives
Y>1. No preliminary proof, generalized e1 case or all-integer classification
is supplied. R9A/B require the EXTRA q_p>=32, with937 a sufficient prime
threshold; R9D/E/F do not inherit that unnecessary restriction.

Read COMPLETE accepted R8 and its acceptance Markdown/JSON, and R6's full
conventions/classical input and COMPLETE operative section5. Operative R8
premises are actual nonconjugate original-weight orbits, pulled-back REAL
phase rows, every-order integral coefficients and majorants, canonical-
function independence and the GENERAL nfun Wronskian lemma. The old sparse
cofactor support bound is not an R9 premise. R6 supplies the exact matched-
prime Jacobi ideal formula and positive-ideal normalization argument. The
new extension to a binary half-weight product is reconstructed below.

## R9A: full integral matrix and the small-coordinate argument

Put m=(p-1)/2, q=ceil((p-4)/30). In O intersect Kplus, the t_h=ζ^h+ζ^-h,
h1..m, form an INTEGRAL basis. An integral coefficient vector for a real
element has conjugate difference a multiple of Phi_p; its zero constant
coefficient forces that difference to vanish. It is symmetric. The relation
1=-sum t_h eliminates its constant integrally. A dependence among the t_h
has zero constant and degree<=p-1, hence is a zero multiple of Phi_p.
No division by2 is used. Also t_u t_h=t_(u+h)+t_(u-h), t0=2=-2sum t_h.

For each of q m columns, ell=a+ζb has2m integral coordinates. The two
orders at m real representatives give at most2m^2 integral equations, so
U=2q m^2 and V<=2m^2. These are ACTUAL transported equations: τ depends
on the actual solution and row a, is a p-th root of unity, and is even
under a->-a. It is never chosen as a free controller. The factor ζb
just shifts that phase for its second real coordinate.

At k0 a trace entry is t_d; multiplication by a basis t_h and eliminating
t0 bounds each coordinate by2. At k1 it is -sum n_c t_(c+d), n_c0/1/2.
After multiplication, each nonzero folded index receives at most FOUR
terms, of total negative size at most8. The two possible zero-index
terms have total negative size at most4 and produce the same positive
correction at most8 at every basis index. Combining the two contributions
therefore lies in[-8,8], even when shifted indices coincide. Bounding each
contribution separately by8 and adding absolute values would lose this
sign improvement, but the candidate uses the correct common correction.

The2^U binary vectors have at most(16U+1)^(2m^2) images. Under2^q>16U+1
two images coincide, and their NONZERO difference has coordinates in
{-1,0,1}. This remains valid with dependent or zero rows. Since
m<=(30q+3)/2<=16q forq>=2, U<=512q^3. Atq32,2^32>2^28+1; the inequality
(1+1/q)^3<2 inductively keeps2^q>8192q^3+1. Thusq>=32 suffices.
The ceiling equivalence requiresp>934, so937 is a sufficient first prime,
without claiming this sufficient threshold optimal.

Every conjugate of a or b is bounded by2m. Hence |σell|<=4m and the
sum overq m columns is at most A=4q m^2. A nonzero coordinate vector
gives some ell!=0, since1,ζ are independent over Kplus. The vector can
be dense and can depend on the actual phase. No escape from the evaluated
equality space has been obtained at this point.

## R9B: both branches and the dense-support correction

R8's actual real-embedding identities and coefficient majorant give
|σδ|<=4A|X|^(-1-1/p) after the first two orders cancel. Ifδ!=0, its
Kplus norm is a nonzero integer. Multiplication over allm embeddings
gives |X|<=(4A)^(p/(p+1))=(16q m^2)^(p/(p+1))<16q m^2. All conjugates
are handled; no one-embedding smallness substitutes for this norm step.

Forδ0 the formal radical combination is nevertheless nonzero: the selected
θ_v and jθ_v have distinct canonical coefficient vectors modulo p, and
monodromy characters isolate every constant coefficient. This is a theorem
about FUNCTIONS, not about their values at1/X. Dense support allows up to
n*=2q m functions. R8's GENERAL Wronskian proof bounds the first nonzero
order by T*=(p-2)n*(n*-1)/2+n*-1. It does not require the old vector to be
the sparse cofactor construction. The new cancellation gives t>=2.

At every order p^t t!h_t is an integral real algebraic number, nonzero at
that first t, with every conjugate bounded by H_t=2A p^t t!. Its norm
gives |h_t|>=(p^t t!)^-1 H_t^(-(m-1)). The evaluated zero and the analytic
tail give |h_t|<=4A/|X|. Thus |X|<=2H_t^m<=2[2A p^T* T*!]^m. Negative X
only changes alternating signs, removed by the absolute estimate.
All factorial and dense-function costs remain. The new polynomial
coefficient height is not a useful new unconditional height theorem.

## Binary half-weight lifts, needed for D/E/F

In the accepted e0 sector (X-ζ)=A^p, with integral nonunit A, Norm A=Y,
pairwise coprime conjugate ideals and primes over ell1modp. For each
binary Fueter ψ, the classical matched-character Jacobi sum at each prime
of A has ideal L^ψ, modulus sqrt(ell) and minus normalization1modλ^2.
Multiplying with the ACTUAL ideal valuations gives bψ integral,
(bψ)=A^ψ, bψ jbψ=Y and bψ1modλ^2. All moduli are sqrt(Y).

Two such generators with the same ideal have an integral-unit quotient.
All its conjugate moduli are1, so Kronecker makes it +/-ζ^h. The common
λ^2 normalization removes both the sign and h. This is a valid use of
Kronecker, since SAME ideals already prove integrality. Consequently the
construction is equivariant and multiplicative on the generated group,
and β_N=Y. Positive final exponents give integral final ideals; intermediate
fraction products do not invalidate this statement.

For θ+jθ=2kN and Fθ0 withk1or3, βθ^p and (X-ζ)^θ have the same ideal
and all conjugate moduliY^(kp). Their quotient is again a unit of modulus
one. Locally r=X-1 is a λ-unit; its augmentation is k(p-1). Fermat's
congruence r^(p-1)=1modp and Fθ0 give (X-ζ)^θ1modλ^2. βθ^p has the same
normalization, removing its root of unity. This proves the exact identity
in the required weight domain, for signed r also. It does not extend to
the source's generalized e1 setting or silently to an odd relative weight.
Finally Y is odd for either parity/sign of X: the geometric sum is1mod2.

## R9C: the complete counterexample, its boundary defect and safe substitute

W'' has14 independent rows, W' has15. The equations of S' are
w1+H w2=0,w3=...=w15=0; adding v=e1 gives w1=w2=...=w15=0 for S.
If an integer vector has sup norm<R<H, the same conclusion follows;
with the stated non-strict norm<=R andR<H it also follows. Thus the
short-point sets are equal. AtR=sqrt(H),H>1, they contain e16 and no
vector outside S. This is the intended generic avoidance obstruction.

For everyj16..d, the perturbed row v+e_j imposes w1+w_j=0. A short point
still has w1=w2=0 and therefore w_j=0, while any e_k withk16..d,k!=j
is a unit solution. d>=17 supplies suchk. These are counterexamples to a
generic inference from short homogeneous solutions to a short escaping
solution. They do not realize an actual Jacobi matrix or refute a special
arithmetic theorem. Fukshansky's sharpness discussion corroborates that
avoidance can require the last successive minimum, without being a new
quantitative premise in this proof.

R9R1-01: as written the construction permits0<R<1. Then NO nonzero
integer vector lies in[-R,R]^d, so the sentence that both sets contain
e16 is false. H2,R1/2 is an exact counterexample to that sentence; equality
of the two zero-only sets still holds. Require1<=R<H for the nonzero-point
counterexample and corresponding perturbations, or explicitly separate
those assertions. No alteration of the valid R=sqrt(H) application or
any A/B/D/E/F inference is mathematically needed. Preserve frozen v1;
the author must issue the correction, and both reviewers must reaudit it.

For the valid replacement, b outside row(A0) makes augmented rankr+1.
Choose r+1 columns with nonzero augmented determinant; the first r rows
have rankr there. Their signed r-minors give z with A0z0 and bz equal
to that nonzero determinant. Each minor is bounded byr!B^r. At r0 use
one coordinate whereb is nonzero and the empty minor1. This is a genuine
avoidance statement with full-minor cost, not an ordinary first minimum.

## R9D: actual overlap valuations, not an ideal-data shortcut

Each binary half support hasm indices, half of G. They are disjoint iff
their sum isN. The selected original-weight pair is notN because M1!=0.
At an overlapping index choose a prime Q of that conjugate of A, with
valuatione>0. All other conjugates are coprime to it. Therefore both
b1,b2 have valuatione, and (Y)=product_(a)σ_a A gives v_QY=e too.

If b1b2-Y=Dχ with a nonzero rational D coprime toY, then v_QD0.
The two summands on the left have unequal valuations2e,e, so v_Qχ=e
exactly. Each b_i dividesY by b_i jb_i=Y, divides the product, and is
coprime toD; thus b_i dividesχ separately. Their product does not:
v_Q(χ/(b1b2))=-e. The quotient Y/(b1b2) has every complex modulus1
but has a pole; it is not an integral unit. The only disjoint binary
half repair sums toN and hasM10. This proves the stated conditional
ideal obstruction. It does not give a solution of the Diophantine equation.

## R9E: all actual finite-two congruences and the weight barrier

For ψ=ψ(1,1)=sum_(c=m+1)^(p-1)σ_(c^-1), inverse moments in DIRECT
indices give M1ψ=sum_c c=-m(m+1)/2=1/8modp. For
Θ=2σ2ψ+4jψ, positivity and I membership hold; coefficients are0,2,4,6,
all<p. The complement is6N, augmentation3(p-1), FΘ=(4-4)Fψ0 and
M1Θ=(1-4)M1ψ=-3/8!=0. The latter excludes a norm/p reduction and
gives a free G orbit. Relative weight6 means precisely sourceJ3,
with3<=m. It is not original weight.

For every u inO, σ2u=u^2mod2 by the characteristic-two binomial formula.
No splitting at2 is needed. Thus the ACTUAL normalized multiplicative
lift satisfies βΘ=(σ2b)^2(jb)^4=b^4(jb)^4=Y^4=1mod2, and the same holds
for every conjugate. Choosew=X ifeven, otherwiseX-1; it is nonzero even,
and removing its odd p-part keeps it even. Each ideal(w',βΘ-σβΘ) is
contained in(2). Their intersection contains(w') and is nonzero, hence
is a nonunit ideal divisible by(2), with the stated inclusion direction.

The homogeneous substitutions are (X,-1,Y) for positive X and(A,1,Y)
for X=-A. The source characteristic ideal is a conjugate of A: the
linear source number is a unit times j(X-ζ). All-conjugate congruences
survive this change. For F0/even-augmentation Θ the normalized identity
does not acquire an uncontrolled root of unity. The relevant even source
coordinate is among x,y,x+y. No actual solution or final source theorem
counterexample is asserted by this conditional consequence.

The ONLY norm shift making complement2N is Θ-2N. The equal-size binary
supports ψ andσ2ψ differ since their nonzeroM1 values differ by1/2.
At an index in supportψ minus supportσ2ψ, both σ2ψ andjψ have coefficient0.
Thus Θ-2N has coefficient-2. Translating only moves that negative
coefficient. This prevents exactly the asserted norm-shift repair; it
does not rule out every unrelated arithmetic construction. Finite-two
Frobenius does not prescribe the infinity signature of R8 columns.

## R9F: the unconditional model retains its failed hypothesis

Forc=2p^2,a0=1+cζ, Norma0=(c^p+1)/(c+1)=Z>1 is positive odd, and
a01modλ^2. A common prime of two conjugate ideals would divide c or
a difference of pth roots, hence λ; neither can divide a0. At a prime
overell of A0, ζ=-1/c in the prime field, with exact orderp, soell1modp
and the prime splits completely. No factorization experiment is used.

For an accepted original-weight pair ψ1,ψ2 letb_i=a0^ψ_i. It is integral,
normalized and has the required ideal. Also b_i jb_i=a0^N=Z, giving
sqrt(Z) at EVERY embedding, not merely one. The same-ideal normalized
Jacobi uniqueness therefore applies. Original weight/F0/M1nonzero are
retained. Sincea01mod2, βθ and every conjugate are1mod2; withw'2 the
equality ideal is EXACTLY(2). χ=(b1b2-Z)/2 is integral and the same overlap
valuation gives a genuine pole inχ/(b1b2).

This is not an equation solution. Moduloζ^p1, the coefficients of a0^p
at degreesp-2 andp-1 are p(p-1)c^(p-2)/2 andpc^(p-1); equality would
requirec=(p-1)/2, impossible forc2p^2. A degree<=p-1 polynomial equal to
a linear number has all coefficients at degrees2..p-1 equal, because
their difference is a multiple ofPhi_p. These two unequal coefficients
prove a0^p is not linear. The crucial linear characteristic p-th-power
hypothesis has explicitly failed, so the model refutes only the shortcut
that discarded that hypothesis. It refutes no Diophantine nonexistence
theorem.

## Sources, falsification and verdict

Fresh primary source inspection checks CURRENT v4's authors, date/status,
relative weight/Jk/β definitions and the COMPLETE operative Definition4/
Lemma4/Lemma5 product step. The separate divisibilities at source
lines926–929 do not multiply without the missing coprimality/integrality
argument. The v1 operative Section4.3.4 is a DIFFERENT short-vector route;
the generic lattice counterexample is not attributed to v4. Fukshansky's
Theorems1.1–1.2 and sharpness/height definitions were read; its quantitative
theorem is not needed by the new elementary counterexample. Exact fresh
read limits and accepted classical-import boundaries accompany this audit.

Actively challenged integral versus archimedean matrix bounds, coincident
indices, ceil endpoints, zero row rank, dense support, real versus complex
phase transport, fractional intermediates, sign/root-of-unity removal,
zero/nonzero evaluation, norm degrees, R<1, all perturbed kernels, r0 minors,
overlap valuation directions, signed homogeneous normalization, original
weight shifts and the model's failed linear hypothesis. Only R9R1-01
requires correction. No math program, CAS, scan, sign child, author rerun
or historical certificate replay was used. Reported byte checks are
administrative integrity, not proof. No fee, contact or access bypass.

Verdict: obtain the other OTHER whole initial, preserve v1, commission the
limited versioned radius repair and BOTH affected reaudits. No promotion
before that process. Even after correction, evaluated nonvanishing/useful
zero-branch cost, a new Diophantine exclusion and the full annual answer
remain open. Requested settings/effective-readback and current authorized
weekly3%/reset1792874445 are recorded separately from mathematical status.
