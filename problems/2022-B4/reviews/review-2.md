# Independent adversarial review R2: 2022 B4(b)

Initial audit completed 2026-10-16, 10:15 UTC. This report was completed
without reading any other review report, conclusion, or issue-log finding.
The coordinator acknowledged the objection below without supplying other
review findings. No proof source has been edited by this reviewer.

Requested launch settings: `gpt-6.1-sol`, reasoning `max`. No effective model
or reasoning-setting readback was available; requested settings are not
represented as verified effective settings.

## Frozen objects and verdict

The audited versions are:

- `proof.md`, version 1, SHA-256
  `8b35be18bb70f81b623f78e7dd1a148478c698c1f5ad32e4097def92ff75aed3`.
- `proof-extension-v2.md`, SHA-256
  `b41aff3fcfadd33f80fdec80570d5b2f61807a5b9e16a28becacefaa237743ed`.

**Version 1:** I found no substantive mathematical objection to P1-P4 as
partial results. I independently reconstructed their arguments, including
the full finite lifting and density argument and the periodic-state
divisibility argument. This is an R2 audit recommendation, not promotion
of status; the coordinator must apply the required two-review process.

**Extension v2:** repair required. Its local abstract control rules and
its bound for a path from an initial fixed difference are valid. Its
assertion that this same bound applies after every surviving prefix is
false. Consequently the repeated-block density deduction at lines 73-77
has a substantive gap. The counterexample below does not disprove the
fixed-offset density-one theorem or the displayed aggregate estimate;
it disproves the conditional premise used to establish that estimate.

Neither version solves the official universal question. A set of natural
density zero can contain admissible positive integer starts.

## Official statement and scope check

I compared `statement.md` with the cached official Paper B, page 2,
including a rendered page, and checked the B4 statement in the official
solution notes. The recurrence is simultaneous:

\[
F(a,b)=\bigl(a+2\lfloor b/20\rfloor,
             b+3\lfloor a/30\rfloor\bigr).
\]

The official hypotheses are positive integer starts and the inclusive
condition \(a_0b_0\ge600\); time zero counts for equality. The drafts match
these domains, the floor convention, and the equality question. Only
part (b) was audited. The established invariant strip is accepted as
attributed context from the official solution notes, whose printed page
19 explicitly states its invariance; I did not reconstruct or reproduce
the preliminary proof. No other competition problem was investigated.

Source fingerprints verified in this audit:

- `.cache/official/2022-paper_b.pdf`:
  `33b15241e89b2e4db54f78d3a565ee01afe357ade786f8bb7602c0b7e89e4519`.
- `.cache/official/2022-solutions.pdf`:
  `3e1670aef22b83cd2be13d027728ebed119072011e4150d7c3aa8dba3101295f`.

The drafts attribute their published input and do not claim established
novelty. I have not independently repeated the separate current-literature
search recorded in `references.md`; no novelty or current open-status
certification is part of this report.

## Reconstruction of version 1

### P1: quotient arithmetic, common shifts, and finite lifting

With \(b=60q+r\), \(0\le r<60\), and \(a=b+d\), the two floor quotients
are \(3q+\lfloor r/20\rfloor\) and
\(2q+\lfloor(r+d)/30\rfloor\), respectively. Subtraction therefore gives
the displayed \(D(d,r)\), and the second updated coordinate is
\(66q+r+c(d,r)\). Reduction modulo 60 gives
\(r'\equiv6(q\bmod10)+r+c(d,r)\pmod{60}\).
The ten controls give ten distinct residues, exactly the required class
modulo 6. These calculations also hold when \(r+d<0\); the floor identity
with an integer translate has no positivity restriction.

Adding \(60t\) to both coordinates adds \(3t\) and \(2t\) to the
respective floor quotients, so both new coordinates increase by \(66t\).
For an initial common shift \(60\cdot10^m z\), its size at time
\(i\le m\) is \(60\cdot11^i10^{m-i}z\), a multiple of 60. Thus the
states \((d_i,r_i)\) through time \(m\) agree, while \(q_m\) changes by
\(11^m z\).

To reconstruct the lifting induction explicitly, suppose a control prefix
of length \(m\) corresponds to one class \(q_0\bmod10^m\). Its ten
refinements modulo \(10^{m+1}\) are represented by adding \(10^m z\),
\(0\le z<10\). They preserve the existing prefix and time-\(m\) state.
Since \(11^m\) is invertible modulo 10, they supply the ten possible
values of the next control once each. The length-zero case is immediate,
so every length-\(N\) word corresponds to precisely one class modulo
\(10^N\). Fixing \(r\) converts this to one class of
\(b_0\bmod60\cdot10^N\).

Each such finite class has arbitrarily large positive representatives;
for fixed \(d\), these also satisfy \(b+d>0\) and the product condition.
This does not produce an ordinary positive integer realizing an infinite
word. Compatible finite classes can specify a 10-adic integer whose
digits are not eventually zero. The draft correctly preserves this
distinction.

### P2: strip control and density counting

The first next difference is fixed before the current control is chosen.
The attributed invariance of \(I=[-13,23]\cap\mathbb Z\) applies to every
abstract state used here: any such \((d,r)\) has an arbitrarily large
admissible representative, and its next difference depends only on
\((d,r)\). For positive next difference \(h\), the selectable residues
30 through 35 satisfy \(31\le h+s\le58\), so the next difference is
\(h-1\). For negative \(h\), residues 20 through 25 give
\(7\le h+s\le24\), so the next difference is \(h+2\).

The worst displayed positive case needs 23 further steps. A negative
odd value can pass from -1 to 1, followed by 0; the endpoint -13 needs
eight further steps. Including the first step gives the uniform bound
24 for every current state in the strip, including states reached after
arbitrary surviving prefixes. This uniformity is exactly what extension
v2 lacks with its smaller initial-only bound.

For each surviving prefix, P1 makes its \(10^{24}\) length-24 extensions
equally numerous residue classes of initial integers. At least one such
extension hits, and extending a shorter hitting word to length 24
preserves the property of having hit. Thus the number of surviving
classes loses a factor at most \(1-10^{-24}\) in each block. This is
finite counting, without any independence assumption about actual
integer orbits. Averaging over the 60 initial residues gives the same
bound for a fixed initial difference.

For every fixed number of blocks the survival set is periodic modulo
\(60\cdot10^{24t}\), up to finitely many ineligible small starts. Its
density exists. The never-hit set is contained in each such survival
set, so its upper natural density is at most
\((1-10^{-24})^t\) for every \(t\), and hence is zero. This uses no
interchange of a density limit with an infinite intersection. Positivity
and the product threshold remove only finitely many \(b\) for fixed
\(d\); \(d=0\) hits immediately. I found no density quantifier gap in P2.

### P3: long finite delays

For the proposed start, write
\(C_n=60\cdot11^n10^{N-n}t\). At \(n<N\), \(C_n\) is divisible by 60,
and the remainder terms satisfy \(0\le r\le19\) and
\(1\le r+1\le20\). Both updates add exactly \(C_n/10\), giving
\(C_{n+1}=11C_n/10\). The additional factor of 10 needed for the next
state to have the same 60-divisibility is present whenever \(n<N\).
This proves the formula through time \(N\), including both stated
remainder endpoints. The starts have product greater than 600 and retain
nonzero difference 1 for arbitrarily long finite times. No inference
about an infinite avoiding orbit is made or justified by this family.

### P4: no ultimately periodic full residue state

If \((d_n,r_n)\) is eventually periodic with period \(p\ge1\), then
\(r_{n+1}\equiv r_n+c(d_n,r_n)\pmod6\), so
\(h_n=(r_n+c-r_{n+1})/6\) is an integer and has that period. The quotient
recurrence is exactly \(q_{n+1}=(11q_n+h_n)/10\).

On a fixed phase, composition of \(p\) updates has
\(A=11^p\), \(B=10^p\), and integer constant
\[
H=\sum_{i=0}^{p-1}11^{p-1-i}10^i h_{n+i}.
\]
With \(C=(A-B)x_0+H\), iteration gives
\((A-B)B^j x_j=A^jC-HB^j\). Integrality implies
\(B^j\mid A^jC\), and coprimality implies \(B^j\mid C\) for every
\(j\). Since \(B>1\), necessarily \(C=0\), and the phase quotient is
constant. Its residue and difference also repeat, so both actual
coordinates return exactly after \(p\) steps.

Both coordinates are nondecreasing for positive starts. Therefore every
increment in this period is zero, requiring \(a\le29\), \(b\le19\), and
\(ab\le551\). At every time the product is at least its initial value
600, a contradiction. The argument does not require the strip and does
not rule out periodicity of \(d_n\) alone. I found no divisibility or
boundary gap here.

## R2-2022-01: extension v2 needs a prefix-uniform bound

**Substantive; open.** Location: `proof-extension-v2.md`, lines 54-77,
especially 73-75. The definition of \(K(d)\) bounds an abstract hitting
path from a state with initial difference \(d\). After an avoiding prefix
the current difference can be different, so this does not establish the
same bound from that later state.

The failure occurs at an actual block boundary, with the product exactly
at the allowed lower boundary. For initial difference 1, the displayed
formula gives \(K(1)=4\). The admissible integer orbit begins

\[
(25,24)\longmapsto(27,24)\longmapsto(29,24)
\longmapsto(31,24)\longmapsto(33,27).
\]

Its first four controls are all zero. It has not hit equality, and its
time-4 abstract state is \((d,r)=(6,27)\). From this state the first next
difference is 5, and the next residue is a multiple of 6. No length-4
abstract continuation can reach equality. Here is a direct finite
verification independent of relying on the evidence script:

1. After the first continuation step the difference is 5, and its residue
   is in \(\{0,6,12,\ldots,54\}\).
2. The next difference lies in \(\{4,5,6,7\}\). A value of 4 can arise
   only from previous residues 30 or 36; in that case the next residue is
   congruent to 3 modulo 6.
3. From differences 4 through 7, the following difference is between 2
   and 9.
   Obtaining 2 requires difference 4 and residue at least 56. Combined
   with the previous restriction, that residue must be 57. The ensuing
   difference-2 state's residue is again 3 modulo 6.
4. A difference of at least 3 in this finite range cannot map to zero
   in one step: the next difference is at least its current value minus
   2. From difference 2 the only zero-producing residues are 58 and 59,
   both excluded by the residue class just established. Thus the fourth
   continuation step also has nonzero difference.

Five steps do suffice, for example along the abstract path

\[
(6,27)\to(5,30)\to(4,57)\to(2,33)\to(1,30)\to(0,33),
\]

whose controls are \((0,4,5,9,0)\). Hence the shortest abstract hitting
length from the time-4 state is exactly 5, greater than \(K(1)\).
In particular all \(10^4\) length-4 extensions of this surviving
four-control prefix avoid equality. The counting induction cannot use
the claimed loss factor conditionally at its second block.

The local control inequalities preceding this passage are sound. For
\(h\ge2\), the lower bound \(0.9h-1.5\) is positive; \(h=1\) maps to
zero. For negative inputs, the explicit \(k=1,2,3\) cases and the strict
negative upper bound at \(k\ge4\) are valid. They prove finite abstract
hitting paths from every state, with a bound depending on that state's
current difference. They do not by themselves give a uniform bound over
all descendants of a fixed initial difference.

**Required repair:** the author should supply and prove a finite bound
uniform over all states reachable from a fixed initial difference, then
repeat the finite counting with that bound. One possible route is a
coarse bounded interval for the reachable differences followed by a
finite maximum of the valid state-dependent bounds. Merely replacing
the initial symbol \(d\) by the current difference leaves a changing
block length and does not justify the displayed geometric estimate.
The repaired argument must receive an affected-argument re-review.

This objection applies to extension v2, not P2 of version 1: P2 uses the
attributed invariant strip and a common bound 24 at every prefix.

## Finite evidence, commands, and reproducibility

Evidence files are `review-2-evidence.py`, `review-2-evidence.txt`, and
`review-2-official-paper.png` in this directory. The script uses Python's
standard library only. It was run with repository `.venv/bin/python`
(Python 3.12.14, macOS arm64); no SymPy, FLINT, native CAS, network access,
or external mathematical package is a premise. The bounded script
completed in under one second, with incremental printed checkpoints.
No long-running CAS job or child cleanup was required.

Commands used for evidence, from the repository root:

```sh
.venv/bin/python -u problems/2022-B4/reviews/review-2-evidence.py > problems/2022-B4/reviews/review-2-evidence.txt
pdftoppm -f 2 -singlefile -scale-to 1800 -png .cache/official/2022-paper_b.pdf problems/2022-B4/reviews/review-2-official-paper
shasum -a 256 problems/2022-B4/proof.md problems/2022-B4/proof-extension-v2.md
shasum -a 256 .cache/official/2022-paper_b.pdf .cache/official/2022-solutions.pdf
```

The finite checks cover 108,360 quotient/common-shift cases, 32,000
enumerated quotient classes for finite lifting, local control inequalities
for positive magnitudes through 10,000, the 2,220-state strip graph, all
10,000 four-step control extensions of the block-boundary witness,
200 sampled delay-family starts through \(N=50\), and 2,340 affine
composition checks. Their output includes the proof fingerprints and
the exact witness. These computations are finite audit evidence; the
unrestricted accepted arguments above are the mathematical reasoning.
No conclusion about emptiness of the never-hit set follows from them.

The only substantive objection from this initial independent audit is
R2-2022-01. Version 1 is eligible for the coordinator's two-review status
decision; extension v2 must retain its unverified status pending repair
and affected-argument re-review.
