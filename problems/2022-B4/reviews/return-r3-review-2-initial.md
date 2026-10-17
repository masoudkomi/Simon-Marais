# 2022 return R3: independent whole audit 2

2026-10-17 UTC. Reviewer: coordinator root, a nonconstructor of this
2022 return and supplement. Initial report is frozen before reading
peer return-review1 findings. Author updates were visible; peer audit
findings were not. The reviewer read BOTH full candidate texts, the
accepted quotient/lifting and complexity arguments, original source
statements/proofs listed separately, and the recorded exact scopes.
No computation or larger enumeration was used for this audit.

## Verdict and boundaries

No substantive mathematical objection to R0-R3 and S1-S2 within their
stated scopes. Both directions of the A/B scalar reduction, run-position
obstruction, bounded real shadow, finite exact averaging and finite
initialization elimination were reconstructed below. This does not
prove that a positive integer avoids equality, that the two-residue
map terminates, or that every normalization is impossible. Review is
not coordinator acceptance: both complete independent reports must be
reconciled before promotion.

## Exact dynamics and admissible domain

For b=60Q+r,a=b+d, substituting in the official simultaneous update gives
b'=66Q+r+c and d'=d+2floor(r/20)-c, c=3floor((r+d)/30).
Write e=Q mod10. Then r'=(6e+r+c) mod60,
10Q'=11Q+h, h=(r+c-r')/6=-e mod10. All ten residue successors occur
once for the full strip state; a fixed actual integer start chooses
only one of them. The accepted finite common-shift identity gives
one Q0 class modulo10^N for each lengthN control word, with arbitrarily
large positive representatives. The audit retains the distinction
between that fact and an infinite ordinary-integer lift. The accepted
strip invariance is attributed preliminary context, not a new target.

## R0 reconstruction

Put u=a mod30 and v=b mod20. Each increment sum equals
s/10-(u+v)/10, so s'=beta s-(u+v)/10, beta11/10.
The backwards tail expansion is s_n=C beta^n+theta_n, with
C=s0-sum_j (u_j+v_j)/(11 beta^j),
theta_n=sum_j (u_(n+j)+v_(n+j))/(11 beta^j).
Since sum_j1/(11beta^j)=1 and 0<=u+v<=48, theta is in[0,48]
and C>=s0-48. If positive s0<=48, the product is at most576;
the official bound600 therefore gives s0>=49, C>=1. No assumption
about eventual strip entry is needed. This handles the inclusive
product boundary and small initial quotients.

## R1 reconstruction, including both directions

At (d,r)=(1,0), controls00 keep r0 and h00. Controls19 give
r0,6,0 and h(-1,1); at r6, d remains1. Grouping the two quotient
equations yields100X_next=121X-w for binary w. In Z10 the unique
initial lift is sum_j w_j100^j/121^(j+1); 121 is a unit and the
powers100 tend to zero, with no real-value identification.

For integer X, block integrality is exactly X0mod100 for w0 and
X81mod100 for w1, since21*81=1mod100. The intermediate A quotient
11X/10 is0mod10; the intermediate B quotient (11X-1)/10 is9mod10.
Thus the final congruence really suffices for both original steps,
and their necessity follows by reducing the same equations.

For positive X, X>=81 and gammaX-.01>X; both intermediate positive
steps also increase Q. With Y=X-1, the next numerator is
121Y+21-w. At Y99mod100 its least correction is21; at Y80 it is20.
Both are in0..99, so the quotient is exactly ceil(121Y/100).
Conversely any positive orbit of this scalar map staying in residues
99,80 reconstructs w and every intermediate integer quotient. The
contest pair (60(Y+1)+1,60(Y+1)) is positive with product>600 and
constant difference1 at every original time. This proves the stated
existence equivalence. Leaving the two residues is leaving this
family, not necessarily reaching equality for the full contest map.
The all-zero Z10 path has zero quotient, outside the official domain.

## R2 reconstruction

If X0=u/v is rational in Z10 with gcd(v,10)=1, recurrence and Z10
integrality cancel all powers2,5 from future rational denominators,
so vXj is integer for every j. If Xj=0, then modulo100 the next
binary correction must be0, and future X and w remain0. For a word
not eventually zero, every Xj is nonzero. A zero run of lengthM
starting at j gives100^M X_(j+M)=121^M Xj. Coprimality forces
100^M to divide the nonzero integer vXj. Real iteration, only now
reading the rational states in R, gives
|Xj|<=gamma^j(|X0|+1/21)-1/21. Hence
M<=j log(gamma)/log100+log(v(|X0|+1/21))/log100.
No assumption that a real infinite expansion equals the Z10 one
has entered this argument.

The nested word construction appends a finite concatenation of all
binary k-words, then as many zeros as the full length at that moment.
At positions j=N_k it therefore has zero runs M=N_k, and N_k tends
to infinity. Since alpha=log(gamma)/log100<1, the rational run bound
fails for large k. Yet the word has every binary k-factor and is not
eventually zero. Its Z10 lift is thus irrational despite maximal
binary factor complexity. Aligned length-two correction codes are
injective, giving at least2^k distinct correction factors of length2k.
This is an explicit symbolic family, with no executed enumeration.
It shows a different obstruction than an asymptotic linear-complexity
slope, without excluding every high-complexity word.

## R3 reconstruction

Canonical ceiling normalization of Z=Q+k requires
10Z'=11Z+delta, delta=h+10k'-11k in0..9.
For fixed integer k,h the next k is uniquely determined by its
mod10 congruence. A fixed initial m with causal continuation therefore
has fixed k_n on each finite control prefix.

Define the bounded REAL shadow Qhat_n=-sum_j h_(n+j)/(11beta^j).
It has absolute value<=10 and satisfies the same affine recurrence,
independently of any Z10 or actual integer lift. Set bhat=60Qhat+r,
ahat=bhat+d. The algebraic sum update still holds with artificial
integer residues u=r+d-30floor((r+d)/30),v=r-20floor(r/20).
This does not take floors of the noninteger shadows. Bounded backwards
iteration gives shat=sum_j(u+v)/(11beta^j) in[0,48]. At state(1,0),
shat0=120Qhat0+1, so Qhat0 lies[-1/120,47/120].

Uniformly average all10^N lengthN controls, extending by zero solely
to define the shadows. At each finite prefix k_n is fixed while
h=-e mod10. Thus delta=-e-k_n mod10 runs once over0..9, and its exact
conditional finite average is9/2. Iterating Zhat=Qhat+k gives
Avg k_N=beta^N(m+9/2+Avg Qhat0)-9/2-Avg QhatN.
For integer m<=-5 the exponential coefficient is<=-13/120;
for m>=-4 it is>=59/120. The final error has absolute value<=29/2.
Some input therefore has |k_N|>=13beta^N/120-29/2. This proves
unbounded worst-input carries, with no statistical claim about one
actual orbit and no claim about equality-avoiding sublanguages.

## S1 reconstruction

On A/B only, h in{-1,0,1} and all positive quotient states are>=81.
For each c1..8, Z=Q-c stays positive and satisfies
10Z'=11Z+(h+c), now with canonical correction0..9. Thus these are
eight parallel scalar-ceiling orbits. For c2..8 corrections1..9 never
vanish, so those seven orbits never visit a multiple10. Any theorem
that every positive scalar orbit eventually visits a multiple10 would
exclude A/B, but that theorem has not been proved here. Constant
normalization on this restricted family does not contradict R3.

## S2 reconstruction and arbitrary initialization

For any current strip state put t=2r+d. The same real shadow has
Qhat0 in[-t/120,(48-t)/120]. If11<=t<=57, then for every integer m
the coefficient m+9/2+Avg Qhat0 stays at least1/40 from zero:
for m>=-4 it is>=3/120; for m<=-5 it is<=-23/120.
The identical finite averaging therefore supplies an escape input
with |k_N|>=beta^N/40-29/2, uniformly in state and initial carry.
From every state, d' is fixed in[-13,23] and the ten controls can
choose the unique r' in12..17 of the needed mod6 class. This makes
11<=2r'+d'<=57. One transition plus a sufficiently long fixed N(K)
therefore escapes every proposed uniform boundK from any current carry.

For each of the2K+1 possible initial carries, deterministic continuation
on a chosen prefix specifies its current carry. Append one escape word
for a still-uneliminated choice. At least that choice has then violated
the bound; an earlier violation is permanent for this logical test even
if the carry later returns. After at most2K+1 such extensions a SINGLE
prefix defeats all initial choices in[-K,K]. Any future-aware selection
in that set is covered. Finite lifting chooses a large positive integer
Q0 in the prefix class, producing an actual official start and the same
counterexample prefix. The witness may pass equality; the theorem does
not apply to every avoiding sublanguage. It only forbids uniformly
bounded UNIT-Q integer-offset maps to the SMALL ceiling alphabet0..9.
Nonuniform bounds depending on Q0, scaling, unbounded carries and the
larger canonical rational-base alphabet are outside its scope.

## Sources and remaining question

Direct primary reads are in the source record. The AFS right transducer
has output0..10 for p11, not0..9. Its terminal boundary also differs;
there is no contradiction. DM singleton termination does not cover two
residues. AEV2026 presents normality and residue equidistribution as
conjectures. None is used as an unrestricted theorem. The arithmetic
proofs above supply all claimed hypotheses directly. No novelty claim
or universal equality proof follows. Both author files are unchanged.
