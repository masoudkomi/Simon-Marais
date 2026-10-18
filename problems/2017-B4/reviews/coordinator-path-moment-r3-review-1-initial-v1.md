# Independent whole PM9 R1 — initial report

18 October2026 UTC. OTHER reviewer C,
`/root/review_2017_coarsening_r1`. **Initially blind ENTIRE WHOLE audit**
of root's NEW PM9A–PM9C, operative constructor v2/ALL48. No corresponding
NEW B PM9 report, finding, file, hash or metadata was accessed before
this entire initial freeze. Mathematical findings are EMBARGOED until
root explicitly confirms BOTH entire initial checkpoints.

**Disposition: no substantive defect or required author repair found.
ALL48 obligations PASS in the exact partial scope.** Six scope/boundary
notes below are closed by the actual definitions and proof; none is an
additional premise supplied by this reviewer. Promotion is exclusively
the coordinator's responsibility after the other complete blind audit
and full reconciliation. This is not external validation or certainty.

C solely constructed OLD PM8. Its two OTHER audits and current separate
acceptance are the authority for that input; this is NOT an independent
recertification of C's own old proof. C was also an old WC/WO whole
reviewer. C did not construct NEW PM9, supply its moment/Hölder/comparison
inference, or consult another new PM9 reviewer. Root alone constructed
PM9 and is excluded from both required independent audits. Requested
inherited gpt-6.1-sol/max is separate from unavailable effective readback.

## 1. Exact target and complete input read

Audited the unchanged main12255B SHA
0af3e42df62385e086a53eec1d95461ba01ba26148a6f92bd34b1fb778924076,
operative freeze-v2.json4093B SHA
7210932f81b90afa8197fb40fe6c7cc3603fbfc85c39b58c67df4f36728b185d,
and ALL16 constructor files, including preserved v1 checklist/freeze,
working draft, corrected ALL48 v2 checklist, notation note, checks,
failures/source MDJSON/log, both admin scripts and ALL metadata. The
v2 change precedes reviewer handoff and changes no mathematical main
byte. Ambiguous old shorthand is not the operative checklist.

Freshly read the COMPLETE accepted WC, WO and PM8 mathematical bodies,
all three current MDJSON authorities, operative old source/failure records,
the full local official statement and actual official B4 PDF. A combined
read output clipped the beginning of PM8; a separate complete main read
recovered every line before any full-read credit. No constructor program,
old freezer, scan, CAS, optimizer or mathematical test was executed.

The official target is C(N) for a fixed unit regular2N-gon, integer N>=2,
with base2 logarithm divided by N². The accepted marked convention,
B2=1, C(N)=B_N and canonical insertion are preserved. No unmarked,
rotation, factorial or insertion-history quotient enters. PM9 only gives
a sharper symbolic upper bound, not the exact value or an effective
all-scale upper modulus R.

## 2. Actual geometry and the precise accepted interfaces

Use an actual simple marked arrangement, represented by once-crossing
x-monotone wires. A directed dual step crosses a previously uncrossed
wire from north to south, increasing rank by one. All complete paths
have exactly n steps, and a nonsouth cell has a lower exit. Thus normalized
positive outgoing weights have full continuation mass, including at
the intermediate point of a two-step block. Reverse orientation is a
bijection on the SAME complete path set.

I independently checked that the accepted PM8 local proof has the exact
scope PM9 uses. A cell is the region between the maximum of its below
wires and the minimum of its above wires. The cross-order inequalities
give one projection interval and lower/upper chains with distinct labels.
A middle lower edge has a bounded successor of indegree1. Such a
bounded cell has at least three edges, so outdegree>=2. The two adjacent
middle exits of an outdegree4 cell make a genuine four-cell diamond.
Its bottom has indegree exactly2: if it had at least3, one adjacent
incoming edge would be middle and the rotated middle lemma would force
its tail to have outdegree1, a contradiction. This is not an arbitrary
DAG assertion or an unbounded-unique converse.

Write mu=1/[2(V+1)]. Under the normalized WO measure an outdegree4
middle has probability mu, and every edge at degree3/4 has probability
at least mu. If a middle successor is already bad, sum its WHOLE second
row to one. Otherwise its degree is3/4, and the diamond gives a two-edge
success route with mass at least mu²=kappa. Hence success probability
is at least kappa after EVERY arriving prefix. High-degree exit choices
are never truncated. A degree4 start has at least four distinct wire
labels remaining, so two trial steps always exist.

The greedy rule takes two edges at degree4 and one elsewhere. A degree4
tail is either a trial start or the one skipped tail of a trial, so
c_F<=2T. Target ranks{j+1,j+2} of consecutive trials are disjoint even
when the next start is j+2. Charge a success to its first bad target.
These are distinct vertices, whose total is at most the BOTH-direction
penalty count b. Thus S<=b. The identical facts hold in reverse with
c_R, a separate trial count, the SAME b and the SAME kappa.

The other exact accepted interfaces are

    sqrt(P(p)Q(p)) >= K^(-n) rho^(-b(p)/2),
    sum_p chi^(-[c_F(p)+c_R(p)]/2) <= K0^n.

The second is the PAID rational tilt: chi is the raw degree4 violation,
and its row is divided by chi before finite flow. The proof does not
call those raw infeasible rows substochastic. These two pathwise/moment
interfaces hold on every actual arrangement at every n>=2, not merely
as a limiting entropy statement. PM8's old three-way count is not used
as a substitute for the new inference below.

## 3. Whole reconstruction of the new positive moment

For clarity I call the path's trial count T(p); the unrelated constant
called t in main Section4 is denoted tau in Section5 below. Set

    r=sqrt(rho), a*=1-kappa(1-r), z=(a*)^(-1/2).

All satisfy0<r,a*<1<z. At each trial the conditional success indicator
Y takes values0,1. Therefore

    sum_s P(s|prefix) r^Y(s)
       =1-(1-r)Pr(success|prefix)<=a*.

Unfold the finite block-prefix tree, preserving distinct prefixes after
graph reconvergence. Replace a trial's two-edge conditional weight by
itself times r^Y/a*, leaving ordinary rows alone. Every outgoing row
has sum<=1. Induction over the finite remaining-depth tree gives

    sum_p P(p) r^S(p) (a*)^(-T(p))<=1.          (R1)

Variable T does not invalidate this induction. Greedy scanning gives a
unique leaf decomposition of each path, and the product of its conditional
block weights is exactly P(p). No independence or optional stopping is
needed. In particular no future event concerning b or c has conditioned
the transition row.

Since z>1 and c_F<=2T, z^c_F<=(a*)^(-T). Since r<1 and S<=b,
r^b<=r^S. Multiplying these two pointwise inequalities gives

    sum P z^c_F r^b<=1,   sum Q z^c_R r^b<=1.   (R2)

The future-dependent b appears only in this AFTERWARD pointwise comparison;
it does not change the adapted tree law. The same b in both arrays is
essential and is exactly what the candidate uses.

Cauchy on the SAME finite set of complete paths gives

    sum sqrt(PQ) z^((c_F+c_R)/2) r^b<=1.

Insert the accepted per-path lower bound. Because r=sqrt(rho),
rho^(-b/2)*r^b=1 EXACTLY. Thus

    sum_p z^(c(p)/2)<=K^n.                       (R3)

This proves PM9A as an absolute sum. There is no division by the unknown
number of paths, inferred uniform sampling probability, lost factor two
in b, or assumption that the count is close to K^n.

## 4. Finite interpolation and the all-n count

Put q=-ln(a*)>0, B=ln(chi)>0 and
theta=2B/(2B+q). Then0<theta<1, ln z=q/2, and

    [z^(c/2)]^theta [chi^(-c/2)]^(1-theta)=1

on every path. Finite Hölder follows from the displayed elementary
Young inequality: u -> theta*u+(1-theta)-u^theta has its minimum zero
at one. Normalize the two strictly positive finite sums, apply it to
their term ratio and sum. An empty path set is trivial; the actual one
is nonempty by the normalized finite continuation process.

Combining(R3) with the separately PAID negative moment yields

    #paths <=(K^n)^theta (K0^n)^(1-theta)=H^n,
    H=K^theta K0^(1-theta),   1<K0<H<K.

This proves PM9B uniformly for every actual arrangement and n>=2.
It improves the certificate without contradicting WO1: WO1 optimizes a
specified raw-feasible local weight family, whereas the present proof
uses an additional geometric block correlation and a paid second tilt.
There is no per-path or per-insertion prefactor4 in this deduction.

## 5. Independent exact check of H<J2<=J

It is necessary to compare with the CURRENT PM8 J, not just with K.
Use A=ln(K/K0)>0, B=ln chi>0, tau=-ln(1-kappa/2)>0,
h=-ln r>0 and delta=min(1,A/B)>0. The old eta and rho=r² give

    ln(K/J2)=delta*tau*h/(8 ln2).

The new theta gives ln(K/H)=A*q/(2B+q). I checked every strict
comparison rather than evaluating these constants numerically:

* ell<19/9 and rho>=2/ell imply rho>18/19. The exact square gap
  18*36²-19*35²=53 makes r>35/36.
* V>1 gives0<kappa<1/16. Thus x=kappa(1-r)<1/576 and the integral
  bound -ln(1-x)<=x/(1-x) gives q<1/575.
* chi=1+149/61731. The opposite integral bound gives
  B>149/61880>1/575; the last numerator gap is23795. Hence q<B.
* h<=(1-r)/r and r>1/2 give1-r>h/2. Consequently
  q>=kappa(1-r)>kappa*h/2.
* tau<=kappa/(2-kappa)<16*kappa/31, so
  q>31*tau*h/32.
* BOTH delta branches satisfy A>=delta B. Therefore
  ln(K/H)>delta*q/3>31*delta*tau*h/96.
* ln2>1/2 by direct integration. Hence
  ln(K/J2)<delta*tau*h/4=24*delta*tau*h/96.

The new gap is strictly greater, so H<J2<=J<K. All denominators and
multiplied quantities are strictly positive. There is no missing
branch where A/B>1 or tends to zero; these are fixed positive constants.
This proves the quantitative PM9C comparison by hand without an optimizer.

## 6. Official transfer and adversarial boundaries

Use the accepted canonical insertion on each size j>=2:
B_(j+1)<=H^j B_j. Since B2=1, the exact sum is

    log2 C(N)<=[N(N-1)/2-1]log2 H, N>=2.

At N2 this is the empty product and both sides are zero. Divide by N²
and take limsup: it is at most(1/2)log2 H, strictly below the old
(1/2)log2 J. Limit existence, an attaining arrangement and effective
all-scale convergence are not premises or consequences of this proof.

I specifically tested by reasoning the following possible failure modes:
b=0 or c=0; no trial at small n; variable trial numbers; a degree4 start
near south; a bad intermediate cell of arbitrarily high degree; one
vertex bad in both orientations; a later trial starting at the previous
endpoint; distinct graph prefixes that reconverge; reversing end-cell
degree conventions; and both delta branches. The accepted geometry and
the exact pointwise comparisons cover them. No abstract-DAG realization
or routine finite enumeration was used to bypass those cases.

## 7. Sources, notes and disposition limits

The source companion states literal fresh primary reads. The current
accepted bodies carry older representation/sharp-zone foundations; they
are not newly re-proved here. PM9's NEW finite flow/Cauchy/Young/log
inequalities were reconstructed fully by hand and need no unread
probability theorem. The MIT manuscript is explicitly unused context;
I did not newly claim its full54pagebody or operative theorem proof read.

Closed notes C1–C6 in the issue ledger retain same-b, full continuation,
paid-tilt, variable-count, old-author-role and exact-scope limitations.
No required repair is identified. ALL48 individual dispositions are
in the separate ledger. The constructor's notation-only pre-handoff v2
is preserved and correctly operative; no main mathematical repair is
silently supplied by this review.

This finding applies only to the stated PM9 upper improvement. Exact
value, matching lower bound, effective upper R, annual completion,
optimality over all certificates and published priority remain unproved
or unclaimed. ALL prior bytes are preserved. The entire report and all
companions/metadata must receive final readback and separate verification
before identity-only handoff; verdict remains embargoed until BOTH.
