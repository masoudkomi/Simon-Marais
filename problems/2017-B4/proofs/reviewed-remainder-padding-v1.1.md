# Reviewed balanced-zonogon remainder padding

**Proved, independently reviewed partial results RP1-RP3**, accepted
exposition v1.1, 2026-10-17 UTC. BOTH fresh initially blind nonconstructor
whole auditors reconstructed exact ranks, physical weak-band placement,
restriction injectivity, uniform profile estimates and all-scale
quantifiers. The coordinator read both FULL reports, issue ledgers and
source records, verified their frozen bytes and found no substantive
objection. No repair required. Only this header is new; the frozen
candidate body below remains unchanged and historical candidate wording
is superseded within this scope.

RP1 injects every full balanced Z_n tiling into Z_q, 1<=n<=q, with its
exact fixed-origin core recoverable; no strict annulus needed. RP2 gives
uniform O_D((q-n)/q) normalized profile error. RP3 transfers a supplied
entropy bound at ALL sufficiently large multiples of a FIXED p0 to
all sufficiently large integer sizes by bounded remainder. It does NOT
produce those positive-entropy families at multiples. One finite base
can be dilated/subdivided and padded to provide one reference at every
size, with ZERO quadratic entropy. H, PR, EAI, arbitrary-window and
stratum recovery remain unresolved; no full solution or novelty claimed.
See ../reviews/remainder-padding-acceptance.md/json.

---

# Exact balanced-zonogon remainder padding

2026-10-17 UTC. **Candidate proof - unverified.** Constructor: coordinator.
Two fresh independent nonconstructor whole audits are required. This is an
elementary marked-word padding construction, with no novelty claim. It
does not provide an entropy lower bound at the multiples where none is
already known, nor prove H, EAI or PR.

## RP1: a smaller balanced zonogon has an injective exact extension

Use fixed D>=2 and v_i=(1,i-1). For integers 1<=n<=q let B_D(n) count
the full marked tilings of Z_n=sum_i[0,n v_i]. Then

    B_D(q)>=B_D(n).

More precisely there is one boundary-dependent padding, chosen before
varying the inner filling, which embeds every Z_n tiling into Z_q and
recovers it by restriction to the fixed physical Z_n at the marked origin.

Rank each color from1 through q. Let the outer lower and upper words be

    P0=1^q 2^q ... D^q,    Q0=D^q ... 2^q 1^q.

Let p=1^n...D^n and t=D^n...1^n use the first n ranks of every color,
and let b=1^(q-n)...D^(q-n) use the remaining ranks, in increasing color
order and increasing internal rank. These are valid globally ranked words.
The full words p b and t b satisfy

    P0<=p b<=t b<=Q0.

The extreme comparisons hold because every ranked color shuffle lies
between the sorted and reversed color blocks. The middle one is the
ordinary full block reversal on just the first n ranks. Inversion-creating
swap chains give actual planar tilings of the lower and upper bands.
Between p b and t b, the common final path b is a zero-area tail and the
only positive-area region is exactly the marked Z_n.

Fix the two band shellings once. Attach any input Z_n tiling in that
region; the three bands tile all of Z_q with disjoint interiors. The
inner zonogon may share boundary edges and its initial vertex with the
outer one, so this is a weak-band construction, not an invocation of a
strictly nested annulus theorem. Indeed Z_n is contained in Z_q directly
from its Minkowski definition. Every seam has the same actual rank
increments. Restriction to Z_n recovers the input; no fiber multiplicity,
label permutation or asymptotic error is present.

## RP2: normalized profiles change only by O_D((q-n)/q)

Let h_n(x)=a_n(n x)/n on Z_1. The tiling extension from RP1 has normalized
profile h_q on Z_1. Every such profile has a common Lipschitz bound G_D
and bounded norm, from the tile gradient formulas. Set alpha=n/q.
For x in alpha Z_1 the extension agrees with the input and therefore

    h_q(x)=alpha h_n(x/alpha).

If alpha>=1/2, this differs from h_n(x) by at most C_D(1-alpha), using
the uniform Lipschitz and norm bounds. Every point of Z_1 is within
diam(Z_1)(1-alpha) of alpha Z_1, by taking the point alpha x.
The same Lipschitz bounds on both functions consequently give

    ||h_q-h_n||_infinity<=C'_D (q-n)/q.

No common-reference word gap or height-to-label conversion is used.
This is a direct restriction identity plus the known uniform geometric
gradient bound.

For any h* in the compact closure X_D and a family F_n with
||h_n-h*||<=delta, the same extension obeys

    ||h_q-h*||<=delta+C'_D(q-n)/q,

and remains injective on F_n. The constant is independent of the
chosen tiling, n and q.

## RP3: bounded remainders remove a multiples-only restriction

Fix a positive integer p0. For every q>=p0 choose
n=p0 floor(q/p0), so 0<=q-n<p0. If families at ALL sufficiently large
multiples n of p0 already satisfy

    liminf_(n->infinity,p0|n) n^-2 log2 |F_n| >=s
    and ||h_n-h*||<=delta,

their padded images at every integer q have

    liminf_q q^-2 log2 |image(F_n)| >=s,
    and ||h_q-h*||<=delta+o(1).

Cardinality is unchanged and (n/q)^2 tends to one. For a target profile
ball epsilon, use delta<epsilon first and then q large enough for the
remaining term. If the multiples carry profiles converging uniformly to
h*, their padded images do too.

In particular, take one finite base tiling of size p0, enlarge each tile
by an integer factor M, and subdivide the enlarged ij tile into its
forced M-by-M ij grid. This produces a full Z_(Mp0) tiling with the SAME
normalized base profile. RP1 pads it to arbitrary q, with profile error
O_D(p0/q) from that base profile. This constructs a reference profile
at every sufficiently large scale, but ONE such tiling has zero
quadratic entropy. It does not reproduce an exponential family at
the multiples or supply PR by itself.

## Remaining scope and provenance

The repaired fixedD profile note correctly left all-scale padding as an
open program obligation there. This separate candidate discharges only
the bounded-remainder/reference-existence step if independently accepted.
It does not settle matching commensurate periodic cores, cutting, rank
phases, arbitrary slope strata or the entropy recovery construction.
Frozen earlier notes and their assertions about their own proof scope
remain unchanged.

The argument uses the already reviewed ranked-word/positive-shelling
dictionary, not an unreviewed annulus, CUT or stratum result. Empty
remainder q=n means empty b and zero-area outer bands. The marked origin
and full lifted boundary remain fixed. No computation, enumeration,
CAS, source-paper redistribution or separately billed API is involved.
