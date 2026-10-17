# Initially blind WHOLE review R2: 2021 R8A--R8D

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1`.
Requested gpt-6.1-sol/max; verified effective-setting readback unavailable.
Target: COMPLETE `notes/reasoning-return-r8-candidate-v1.md`,16961bytes,
SHA256 `6bffa3b70e9d228b09e0a2ee3f049d7f5261fb98d484ebacff7abcbfde5eea26`.
Target freeze3602bytes, SHA256
`9d366b0c0eee1a56dae269a2aeb197627516d00f2d87d17a4d6c93304b1919b8`.

This is a fresh whole nonconstructor audit of NEW R8. I did not construct
or contribute its controlled quadratic, cubic, four-depth or transport
argument. I authored OLD accepted R5 and reviewed older single-center/PN
restrictions. Those are separately accepted inputs supported by other
audits; this report is not an independent self-review of my own R5.
I read no new R8 peer/root report or conclusions before this ENTIRE
report,40-row ledger, source checks and integrity manifest froze.

**Result:** no substantive defect or required author repair found in
R8A--R8D's exact necessary-condition scope. I reconstructed every new
valuation, all nine cubic cases, the actual-witness assignments and
both affine frames. This recommends only the written partial fork.
Neither a remaining alternative nor the actual-double branch, J15,
degree20 or the annual classification is eliminated. Coordinator
reconciliation after both independent whole audits remains required.

## 1. Exact official and dependency boundary

The official part(b) requires f over Q and a RATIONAL common root with
each derivative1,...,d-1. The root may depend on the derivative; other
roots need not be rational or real. I reread that exact primary statement
and the complete local statement. No preliminary argument was researched.

The new theorem is only in the accepted rational normalized degree20,
J15,multiplicity-two,sole-H3 branch, with an ADDITIONAL ACTUAL double
small root s. The complete accepted R7/R6/R5 bodies and scope headers
were read, together with the seven-return accepted scope register.
Direct inputs are the full actual rational root set {0,1,r,s}, simple
center1, v(r)=v(s)=nu>=1, s/r=2mod19, global carrier exclusion,
R5D's first break, R7B's weighted triple, the Euler estimate and R7D's
exact involution. Their older finite certificates were not rerun or
independently recertified by metadata. The full fourteen-root global
carrier is required; excluding only one local cluster would not suffice.

Let v=v19, v(0)=infinity, e=2m, j=20-e, m3..7. Thus j runs through
14,12,10,8,6. All normalized D_j and beta_j are formed over Q BEFORE
reduction. Direct differentiation gives

    D_j'=jD_(j-1), H2(D_j)=j(j-1)D_(j-2)/2.

Every relevant binomial coefficient binom(20,j) has exactly one factor
19; beta_j=binom(20,j)/19 is a unit. All j,j-1,j-2 and the displayed
denominators2,3,(e+1)(e+2) are19-units. The exact rational beta ratio is

    beta_(j-2)/beta_j=j(j-1)/[(e+1)(e+2)].

An essential center has full monic gcd X-1: all global carrier roots
are excluded, the other eligible values are the three stated rational
noncenters, and1 is simple. Essential0/s would not have that automatic
multiplicity-one refinement. The candidate respects this distinction.

## 2. Euler input and endpoint checks

I checked the exact accepted Euler mechanism, not just its cited name.
With the preceding even ladder, the even Taylor polynomial is

    E(T)=[f(r+T)+f(r-T)]/2=T^e W(T²),
    W(Z)=h_e+h_(e+2)Z+...+Z^(10-m), h_k=H_k(f)(r).

Every nonleading even h_k has valuation>=1, h20=1. For
delta=s-2r and f=(X-s)²U,

    E(r)=delta²U(2r)/2,
    E'(r)=delta²U'(2r)/2-delta U(2r),
    2r^(e+1)W'(r²)
       =-delta U(2r)[1+delta(m/r-U'(2r)/(2U(2r)))].

Here v(U(2r))=3nu+1 and U'(2r)/U(2r)=2/r+an integral element.
For nonzero delta its valuation exceeds nu, so the bracket is a unit;
W'(r²) has valuation>=1. It follows that v(delta)>=(e-2)nu and
v(W(r²))>=(e-1)nu+1. For delta=0 the exact identity instead gives
W(r²)=0. No division by zero or unproved maximum displacement is used.
Subtracting W's nonconstant terms gives the accepted v(D_j(r))>=2nu
and v(a_j)>=nu. This works for arbitrary nu>=1. In the new proof the
worst leading term is jnu=6nu at m7, still safely above every stated
comparison level, including nu1. The old minimum witness bound10 is
irrelevant to these inequalities and is not used as a truncation.

## 3. R8A: the enlarged quadratic range is valid

Write A=a_(j-3), u=a_(j-2), sigma=v(A), tau=v(u)<infinity. Under

    tau<min(nu+sigma,2nu),

the expansion D_(j-2)(r)=u+(j-2)Ar+O(r²) has u as its UNIQUE
least-valuation term. Thus h_(e+2) has valuation tau+1. In W(r²),
the term h_(e+2)r² has valuation2nu+tau+1, while later nonleading
terms have at least4nu+1, the leading term has jnu>=6nu and W's
value is zero or at least5nu+1. Each is strictly higher: tau<2nu
and valuations are integral. Therefore

    v(h_e)=2nu+tau+1,
    D_j(r)/(u r²)=-c mod19,
    c=j(j-1)/[(e+1)(e+2)]!=0.

In particular r is not an H_e witness. If H_e has only the center,
its a_j is nonzero (otherwise0 is a witness) and nonunit by the
Euler estimate. This gives the claimed alternative immediately.

Otherwise an ACTUAL noncenter witness w is0 or s, with v(r-w)=nu.
The difference quotient at r,w has valuation nu+tau. Its quadratic
term has at least that valuation; its cubic term has at least
2nu+sigma>nu+tau; higher terms have at least3nu>nu+tau. A smaller
linear coefficient would be uniquely minimal, impossible. Hence
v(a_(j-1))>=nu+tau. Evaluation at w gives v(a_j)>=2nu+tau, including
exact a_j=0 at w0. This proves integrality BEFORE reduction of

    q(z)=D_j(rz)/(u r²) mod19
        =C+j*l*z+binom(j,2)z².

The two strict hypotheses separately suppress the cubic and all
degree>=4 terms. We have q(1)=-c and q(0)=0 or q(2)=0. If the
adjacent derivative had an actual noncenter zeta, its residue y=zeta/r
would be0,1 or2, and D_(j-1)(zeta)/(u r) reduces to

    l+(j-1)y=0.

Solving gives y=rho or2-rho, where rho=1/2+1/P and P=(e+1)(e+2).
For rho to be0,1,2, P must respectively be17,2,7. The five actual
P residues are18,14,18,11,12, so no case works. This calculation is
unchanged when tau>=nu because BOTH new strict bounds justify the
same reductions. The resulting l is nonzero since rho and2-rho are
nonzero. Thus the adjacent normalized constant has EXACT valuation
nu+tau, and its sole center has full gcd X-1. Sigma infinity is
allowed; zero u is properly excluded from this statement.

## 4. R8B valuation alternatives, including zeros and positive sigma

Take the actual first break provided by accepted R5D. Suppose the first
R8B alternative fails. Accepted R7B gives

    v(a_(j-2))>=nu, v(a_(j-1))>=2nu, v(a_j)>=3nu.

All three normalized constants are then nonunit. If any of the three
derivatives e,e+1,e+2 lacked a noncenter witness, the official hypothesis
would supply the center alone, and the constant would be nonzero
(zero would supply0); that is the excluded first alternative. Hence
all three have ACTUAL noncenter witnesses, with the first at0/s.

If sigma>=nu, a finite tau<2nu triggers R8A, a contradiction.
So tau>=2nu, including infinity. Then D_(j-2)(r) has valuation>=2nu;
all nonconstant terms of W(r²) and its possible value are at least
4nu+1. It follows that v(D_j(r))>=4nu. The quotient at r,w has
valuation>=3nu, as do all its terms beyond the linear coefficient.
Thus v(a_(j-1))>=3nu, and evaluation at w gives v(a_j)>=4nu.
This is the entire four-depth block, including zero coefficients.

Otherwise sigma is finite with0<=sigma<nu. If tau<nu+sigma, R8A
again applies, because nu+sigma<2nu. Thus tau>=nu+sigma, and the
same W/quotient/evaluation chain now gives

    v(D_j(r))>=3nu+sigma,
    v(a_(j-1))>=2nu+sigma, v(a_j)>=3nu+sigma.

This includes positive sigma; no hidden unit assumption is present.
After scaling by A*r³ all four coefficients are integral, all higher
terms vanish since nu-sigma>0, and Q is a cubic with EXACT leading
coefficient b=binom(j,3)!=0. No conclusion was drawn merely from a
nonintegral formal quotient.

## 5. Complete independent cubic reconstruction

Let w,u,t be the selected actual noncenter residues for e,e+1,e+2,
respectively. Then w is0 or2, u,t are0,1 or2. Differentiation before
reduction gives Q(w)=Q'(u)=H2(Q)(t)=0. The even Taylor relation,
divided by19 beta_j A r³, is exactly

    Q(1)+kappa H2(Q)(1)=0, kappa=2/[(e+1)(e+2)].

The factor2 is necessary: D_(j-2)(r)/(Ar) reduces to
2H2(Q)(1)/[j(j-1)], and the beta ratio cancels the remaining factors.
Later nonleading terms have excess>=nu-sigma>0; W's value has
excess>=(e-4)nu-sigma>0 or is zero; the leading term has excess
>=(j-3)nu-sigma-1>=3nu-sigma-1>0. The latter remains positive at
nu1,sigma0,m7. No tied leading contribution was lost.

The operation Q*(z)=-Q(2-z) preserves the leading coefficient and
the equation at1, while reflecting all three nodes. It converts w2
to w0 without assuming any exact rational symmetry. For w0 write

    Q(z)/b=(z-t)³-3(u-t)²(z-t)+d,
    d=t³-3t(u-t)².

This is the general cubic with the chosen inflection and critical
point; Q(0)=0 fixes d. The equation at1 reduces to

    1-3t+3t²-3(u-t)²+3kappa(1-t)=0.

I obtained all NINE cases directly, with1/3=13 in F19:

|t / u|0|1|2|
|---|---:|---:|---:|
|0: kappa=u²-1/3|6|7|10|
|1:1-3(u-1)²=0|false|false|false|
|2: kappa=7/3-(u-2)²|11|14|15|

The actual kappa values at m3,4,5,6,7 are17,11,17,14,16. Only
(m4,u0,t2) and(m6,u1,t2) remain for w0. Expanding the general cubic
then gives z²(z-6) and z(z-3)². Reflecting gives (z-2)²(z+4) and
(z-2)(z+1)². This is a full hand classification under the stated
three-node equations, not a numerical sample or a CAS certificate.

I separately differentiated each survivor to check uniqueness among
the AVAILABLE nodes, which is needed for ACTUAL witness assignments:

|Q/b|Q's available root|Q'/b factor|available critical|H2(Q)/b|inflection|
|---|---:|---|---:|---|---:|
|z²(z-6)|0|3z(z-4)|0|3z-6|2|
|(z-2)²(z+4)|2|3(z-2)(z+2)|2|3z|0|
|z(z-3)²|0|3(z-1)(z-3)|1|3z-6|2|
|(z-2)(z+1)²|2|3(z-1)(z+1)|1|3z|0|

The rational values0,r,s have distinct residues0,1,2 after division
by r. An actual selected witness is therefore forced to be the exact
listed value. In the first row this gives D_j(0)=D_(j-1)(0)=0,
hence a_j=a_(j-1)=0 and H_(e+2)(s)=0. In the second it gives
D_j(s)=D_(j-1)(s)=0 and a_(j-2)=0. The third gives a_j=0,
H_(e+1)(r)=H_(e+2)(s)=0; the fourth gives D_j(s)=0,
H_(e+1)(r)=0,a_(j-2)=0. These are exactly all four statements.
They do not assert that center1 is not also shared. Residue equations
alone are never promoted to a rational or Q19 lift.

## 6. R8C: both exact frames and the sign

The accepted change is f_new(Y)=(1-s)^(-20)f(s+(1-s)Y),
r_new=(r-s)/(1-s), s_new=-s/(1-s). Since v(s)>0 its denominator
is a unit. It fixes1, exchanges the double roots, preserves nu,
J15 and all actual witnesses, and scales every derivative by a
nonzero factor. Thus it preserves the first break. Applying it twice
returns the original polynomial, not a polynomial merely assumed
equivalent by symmetry.

Direct differentiation of this exact change gives

    D_new,k(Y)=(1-s)^(-k)D_k(s+(1-s)Y),
    a_new,k=(1-s)^(-k)D_k(s).

For k=j-h,h0..3, a term in D_k(s) involving one of the four block
coefficients has valuation at least(4-h)nu under T4; its lost depth
is exactly regained by its power of s. Every later term has exponent
at least4-h and integral coefficient. The unit factor does not change
the bound. The involution gives the reverse implication, so T4 holds
in both frames, also when some coefficients vanish.

In the cubic branch A=a_(j-3) has sigma<nu, so
D_(j-3)(s)=A+O(s) and a_new,j-3/A reduces to1. Thus sigma is
unchanged. Also r_new/r=-1mod19. At Y=r_new z, the OLD argument
is s+(r-s)z; divided by r it reduces to2-z. The ratio of the OLD
normalizing factor A*r³ to the new one reduces to-1. Consequently

    Q_new(z)=-Q(2-z).

The negative sign is essential and correctly supplied. The cubic
integrality bounds also persist: the same expansion has levels
(3-h)nu+sigma, while later terms are strictly deeper since sigma<nu.
The transformation pairs rows1/2 and3/4; it is an obstruction to an
automatic contradiction by renormalization, not such a contradiction.

## 7. R8D, diagnostics, sources and final audit scope

For odd m3,5,7 there is no cubic survivor. If sigma<nu or tau<2nu,
T4 fails. The first R8B alternative must therefore hold. The possible
orders are e,e+1,e+2 within6..16. These coefficient conditions are
additional hypotheses, not automatic for every branch member.

The older m3 diagnostic4z²+3z³ has H2=4+9z with root8, outside
0,1,2. It survives the former two-witness calculation but fails the
new third actual-node condition. That limited diagnostic was not an
actual polynomial or lift, and R8 does not misrepresent it as one.

Primary checks independently confirm the official rational-witness
domain, CLO's normalization and its strictly stronger all-root-rational/
unramified Proposition19 hypotheses. Marashdeh's one-nonzero-recycled-root
and two-support theorems do not supply a four-value exclusion. No new
external theorem beyond the accepted inputs and elementary algebra is
used. The source record distinguishes actual reads from uninspected
proofs and preserves the prime5 correction and residual-CA gap.

No mathematical program, CAS, scan, larger table, certificate replay
or constructor rerun was used. All characteristic19 computations above
are hand derivations. Administrative hashes establish identity only.
The full new fork remains a necessary restriction in the exact
ACTUAL-double branch. Every remaining alternative, rational/global
compatibility and the official classification remain unresolved here.
