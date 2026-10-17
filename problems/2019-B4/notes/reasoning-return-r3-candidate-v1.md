# Alternating-block budgets and a finite-state obstruction

2026-10-17 UTC. **Candidate proof - unverified.** Constructor
`review_2021_reasoning_j15_r2`; requested gpt-6.1-sol/max, verified
effective-setting readback unavailable. Two OTHER fresh initially blind
nonconstructor whole audits are required. Only 2019 B4(b) is researched.
No exact growth constant, general nonalgebraicity or novelty is claimed.

## Scope and statements

Use the accepted chronological history model, lexicographic order L<R,
canonical language K, and actual minimal bad-factor set F. Thus a
history writes the alternating source bits0,1,0,1,... to the chosen
left/right tape, and K has one representative of each distinct marked
context. This does NOT identify histories with the official binary
strings. The accepted comparison between marked contexts and unmarked
strings shows that K and the official sequence have the same growth
constant lambda. That comparison, rather than a new history count,
allows the growth conclusions below to concern part(b).

The accepted second-pass results provide: K=Avoid(F); K is factorial;
F is factor-free and cross-bifix-free; every f in F starts RR, ends LL,
and has a strictly upper equal-context witness; and the staircase
histories h_n below belong to F and have exactly two histories for their
contexts. The accepted bounded-separation result provides the regular
sets F_D subset F and K_D=Avoid(F_D), with growth rho_D decreasing to
lambda. The accepted renewal and moment bounds remain unchanged.

The proposed new conclusions are:

**NR1. Prefix budget for alternating blocks.** Suppose

    f=a (RL)^m b belongs to F,  m>=1.

Let alpha be the source bit at the first R of the displayed block,
beta=1-alpha, and let V_a be the chronological right tape produced by
the prefix a. Then

    m <= 2 * number_of_beta_bits_in(V_a).                 (1)

In particular no fixed a,b can have a(RL)^m b in F for unbounded m.

**NR2. Nonregularity of the exact languages.** The languages F and K
are not regular. Neither is the lexicographically canonical language
in the four two-move generators A=LL,B=LR,C=RL,D=RR. The equal-context
relation on two synchronously read histories is not regular either.
These are statements about these exact representations, not about
every possible cross-section, asynchronous representation or counting
series.

**NR3. Every regular actual-obstruction subset has a strict entropy
gap.** If G is ANY regular language with G subset F, including infinite
G, then Avoid(G) is regular and its growth rho_G satisfies

    lambda < rho_G.                                      (2)

If an r-state DFA recognizes G, no word of G contains (RL)^r as a
factor. The word W=(RL)^r connects any two G-avoiding words, and resets
the minimal nonrejecting DFA for Avoid(G) to its initial state. That
DFA is strongly connected and has an L-loop at its initial state.
Thus (2) excludes attaining the exact rate by avoidance of any regular
subset of the actual minimal obstructions, not just by a finite list.

**NR4. Explicit bounded-separation reset and nonstabilization.** For
every integer D>=1, the shorter explicit word

    W_D=(RL)^(2D), length4D,                              (3)

connects arbitrary words in K_D and resets its minimal nonrejecting DFA.
Moreover the accepted staircase h_D has minimum upper-witness
separation D+1, belongs to K_D but not K, and

    lambda < rho_D  for every finite D>=1.                (4)

This does not say that consecutive rho_D must differ. Together with
the accepted convergence and moment estimate, it gives

    0 < rho_D-lambda <= 1/(D+1),  rho_D down to lambda.   (5)

There is no larger-cap computation or new numerical bound in this note.

## 1. Exact prefix accounting

For a history h and a time t, denote its numbers of left and right
moves by ell_h(t),r_h(t), with ell_h(t)+r_h(t)=t. For two legal paths
h,g for the SAME complete tape pair, write

    d(t)=ell_g(t)-ell_h(t)=r_h(t)-r_g(t).

If d(t)>0, g has read d(t) more symbols of the left tape and d(t)
fewer of the right tape. Both paths have read exactly the same
alternating source prefix of length t. Therefore their combined
numbers of zeros and ones agree. Equivalently, the extra left symbols
read by g have the same symbol multiplicities as the extra right
symbols read by h. This elementary conservation identity is about
whole words with their chronological tape order. Equal tape lengths
alone would not imply it for arbitrary schedules or source words.

Now take f=a(RL)^m b in F. The prefix a is nonempty: otherwise f would
start RL, contrary to its accepted RR beginning. Similarly b is
nonempty, since otherwise f would end RL rather than LL. Thus times
at the start and inside the displayed block are internal to f.

Let U_a,V_a be the two tapes of a, and put

    u=#beta(U_a),  K0=#beta(V_a).

Here K0 is a nonnegative integer, unrelated to the language K. The
first R of the block is written at source phase alpha=|a| mod2, and
each following RL pair writes alpha to the right and beta to the left.
After j complete pairs, where0<=j<=m, the two prefixes on f are

    U_a beta^j,   V_a alpha^j,                           (6)

and the source prefix has exactly u+K0+j beta symbols.

Let g be a strictly upper equal-context witness for f, available by
the accepted minimal-factor witness lemma. Suppose for contradiction
that m>=2K0+1. Look at time t=|a|+2K0, so j=K0. This is an internal
time, including when K0=0, and strict upperness gives d=d(t)>0.

At this time g has consumed ell_f(t)+d=|U_a|+K0+d left symbols.
If it has passed all m left symbols of the displayed block, its left
tape prefix alone contains at least u+m beta symbols. But the entire
available source prefix has only u+2K0 such symbols, contradicting
m>2K0. Thus g's left endpoint is still within that constant-beta block.
Its left beta count is then u+K0+d, so availability gives d<=K0.

It follows that g has consumed

    |V_a|+K0-d >= |V_a|

right symbols, all its right symbols beyond V_a being alpha, because
g trails f on that tape. Its right beta count is exactly K0.
Consequently g has consumed in total u+2K0+d beta symbols, exceeding
the available u+2K0. This is a contradiction. For K0=0, the intermediate
conclusion d<=0 already contradicts strict upperness. Equation(1)
follows in all cases.

No upper bound on d was assumed. A witness cannot escape the argument
by consuming the left tape beyond the alternating block: that case
was explicitly ruled out by the first source-budget inequality. No
assumption that f has only two histories was used in NR1.

The argument works at either source phase. Replacing alpha,beta by
their complements preserves every step. It neither discards odd
prefix lengths nor normalizes a tape by an unproved scheduling rule.

## 2. Pumping inside an alternating block

Let G subset F be recognized by a DFA with r>=1 states. Suppose some
word a(RL)^m b in G has m>=r. On its accepting run, inspect the m+1
states at the boundaries between successive displayed RL pairs.
Two of them agree, so a positive power (RL)^p labels a loop there.
Repeating that loop preserves acceptance and produces

    a(RL)^(m+kp)b in G subset F,  k=0,1,2,... .          (7)

The a and b in (7) stay fixed; pumping inside the homogeneous RL block
only changes its exponent. The right tape V_a and the source phase
at the block's start are fixed as well. NR1 bounds that exponent by
the fixed finite integer2#beta(V_a), contradicting (7). Therefore

    no word of G contains (RL)^r.                       (8)

This proves a bounded alternating-factor property for EVERY regular
subset of F, without enumerating or classifying its other factors.
An incomplete automaton or a finite observed prefix would not suffice
for this reasoning; G must actually be regular and contained in F.

The accepted staircase theorem gives, for each n>=1,

    h_n = RR
          [product(j=1,...,n-1) (LR)^j R]
          (LR)^(n-1) LL
          [product(j=n-1,...,1) (RL)^j L]  in F.          (9)

For n>=2 the first descending block includes (RL)^(n-1). Thus F has
arbitrarily long powers of RL as factors. If F had an r-state DFA,
take h_(r+1) and contradict (8). Hence F is not regular.

Since K is factorial and contains both one-letter words, its minimal
forbidden set satisfies the exact regular-operation identity

    F = ((Sigma K) intersect (K Sigma)) minus K,
    Sigma={L,R}.                                        (10)

A word in the right side has its proper suffix and proper prefix in K;
factoriality then puts every proper factor in K. The converse is the
definition of F. There are no length-one exceptions, because both
letters belong to K. If K were regular, closure under concatenation,
intersection and complement would make (10) regular. Consequently K
is not regular.

This implication uses membership of all h_n in F from the accepted
unrestricted staircase proof, not its finite grid checks. No inference
from a sparse subfamily alone to the generating function is made.

## 3. Two representation consequences, precisely delimited

Let K_even be the even-length words of K. A word h is canonical if
and only if hR is canonical: forward, appending R cannot complete a
minimal forbidden factor, all of which end LL; reverse, K is
factorial. If K_even were regular, the odd part of K would be

    {h: |h| odd and hR in K_even},

a regular right quotient intersected with the odd-length language.
Adding K_even would make K regular, a contradiction. Thus K_even is
not regular. Under the fixed-length code
A->LL,B->LR,C->RL,D->RR, the four-generator canonical language maps
bijectively onto K_even. A regular four-generator language would have
a regular image, so this canonical language is nonregular too. The
code preserves lexicographic order and exact tape contexts; it is
not a claim about every possible auxiliary generating set.

For the synchronous relation assertion, let E be the language over
Sigma times Sigma whose zipped pair (h,g) has equal chronological
tape contexts. Equal contexts force |h|=|g|. If E were regular, its
intersection with the finite-state lexicographic test g<h would be
regular. Projection to h is the language of noncanonical histories,
since each context class is finite and has a least representative.
Projection of a regular zipped language is regular, and complement
would make K regular. This contradicts section2.

This rules out a finite synchronous equality recognizer in this
history encoding. It does not establish a theorem about arbitrary
asynchronous relations, all normal-form choices, a different regular
cross-section, or an automatic presentation of a different monoid.

## 4. Universal bridge and a reset for any regular G subset F

Let G and r be as in section2, and put W=(RL)^r. Let a,b avoid G.
I claim

    a W b avoids G.                                     (11)

If an occurrence of a word f in G is not contained in a or b, it
cannot start inside W: f starts RR and W has no RR, including at its
last letter L. It cannot end inside W either: f ends LL and W has no
LL, including at its first letter R. Hence any such occurrence must
cross the entire W, with its beginning on the a side and its end on
the b side. It would contain W as a factor, contradicting (8). This
also handles seam occurrences RR across a/W and LL across W/b; they
would still span the full block. Empty a or b cause no exception.
This proves (11).

Put L_G=Avoid(G). Regularity of G makes Sigma*G Sigma* regular, so its
complement L_G is regular. It is factorial, contains K and every
all-L word, and includes the empty word. Use its minimal complete DFA.
Because L_G is prefix-closed, every nonaccepting reachable state has
empty right language; all such states form one rejecting sink. Delete
that sink to get the minimal nonrejecting partial DFA M. Every state
remaining is accepting and reachable by a word a in L_G.

Let q be such a state and let q'=delta(q,W). Equation(11) says q'
exists and every b in L_G is accepted from q'. Conversely, if b is
accepted from q', then aWb is in L_G, and its factor b lies in L_G.
Thus q' has exactly the initial state's right language L_G. Minimality
gives q'=q_initial. In other words W resets EVERY state of M to its
initial state. Since every other state is reachable from that state,
M is strongly connected.

The initial state also has an L self-loop. Indeed prepending L cannot
create a G occurrence that starts at that new letter, since every
member of G starts R; all other factors lie in the original word.
Thus Lb belongs to L_G exactly when b does, and the two right languages
are equal. This verifies aperiodicity too, although the strict entropy
argument below only needs strong connectivity.

## 5. Strict growth gap for every regular actual-obstruction subset

Let A be the finite adjacency matrix of M, counting each of its
defined letter transitions, including both letters if they share an
edge's endpoints. Strong connectivity makes A irreducible. If v>0
is a right Perron vector with eigenvalue rho, then deterministic
path counting gives

    a_n=|L_G intersect Sigma^n|=e_initial^T A^n 1,
    (v_initial/max v)rho^n <= a_n
                   <= (v_initial/min v)rho^n.            (12)

Thus rho_G=rho. Only the standard finite Perron–Frobenius existence
of positive left/right eigenvectors for an irreducible nonnegative
matrix is used, with its hypotheses established above. The same
finite theorem is already used with its comparison proof in the
accepted staircase note.

Since F is nonregular whereas G is regular, choose f in F minus G.
The anti-factor property of F implies that f avoids every member of
G, so f labels an actual legal path of M from the initial state.
Every canonical history avoids f.

For completeness, put ell=|f|>=4 and form the finite higher-edge graph
H: its vertices are legal M-paths of length ell-1, and its edges are
legal M-paths of length ell, joined by their overlapping ell-1 paths.
It is strongly connected. To join two vertex-paths, follow the first
to its end, use an M-path to the beginning of the second, then follow
the second. Successive windows give the desired H-path. Its path
growth equals that of M, since H-paths are in bijection with M-paths
longer by ell-1; summing over finitely many starting states changes
only constants in the root rate. Hence its irreducible adjacency
matrix A_H has spectral radius rho_G.

Remove all H-edges whose full ell-letter label is f. At least one
is removed, because f lies in L_G. Let B be the resulting nonnegative
matrix, with the same vertex set, so 0<=B<A_H. The strict finite
Perron comparison gives

    spectral_radius(B) < spectral_radius(A_H)=rho_G.    (13)

Here is its short proof, including the possibility that B is reducible.
If equality held, choose a nonzero nonnegative Perron vector x of B
and a positive left Perron vector w of A_H. Then
w^T(A_H-B)x=0. Nonnegativity forces (A_H-B)x=0, hence
A_H x=rho_G x. Irreducibility makes x positive, which forces
A_H-B=0, a contradiction.

Every word in K is accepted by M and avoids f, so its representing
H-path uses only B-edges. Finite matrix path counting, or Jordan
normal form with a polynomial prefactor, bounds its root growth by
the spectral radius of B. Therefore

    lambda <= spectral_radius(B) < rho_G.

This proves NR3 for infinite as well as finite regular G. It neither
assumes that G's complement inside F is regular nor tries to count
that complement. The source of strictness is an actual missing
minimal factor and an irreducible finite avoiding graph, not an
observed numerical gap or a fitted polynomial.

## 6. An explicit bridge at a separation cap

The preceding theorem applies to each accepted regular F_D. One can
also prove the sharper, state-count-independent bridge (3) directly.
Suppose a member f of F_D occurred across W_D in a W_D b with
a,b in K_D. Its RR/LL endpoints again force it to contain the whole
W_D. Let g be a strictly upper witness for f with maximum separation
at most D. At the time halfway through W_D, h=f has consumed D right
symbols alpha and D left symbols beta from that block; another D
of each remain.

The witness's positive surplus d lies in1,...,D. Its extra left
symbols are the next d beta symbols still inside W_D, while its
missing right symbols are the last d alpha symbols already inside
W_D. These two constant strings have different symbol multiplicities,
contradicting the exact conservation identity in section1. Thus no
F_D occurrence can cross W_D, and

    a W_D b belongs to K_D for all a,b in K_D.            (14)

This is valid at either starting phase and at d=D, where the extra
left segment reaches exactly the end of the block and the right
deficit reaches its beginning. No endpoint is passed. The same
right-language argument as in section4 makes W_D reset the MINIMAL
nonrejecting DFA for K_D. This does not assert a literal empty-subset
reset in an unminimized residual-queue implementation.

For an explicit missing factor, use h_n from (9). Its only alternative
history is its side-exchange bar(h_n), by the accepted staircase
rigidity theorem. Its strictly upper separation equals

    ell_bar(h_n)(t)-ell_h_n(t)
                  = #R_in_h_n_prefix(t)-#L_in_that_prefix(t).

After RR this difference is2. Each ascending block (LR)^j R raises
the endpoint difference by1 and never exceeds that new endpoint;
therefore its maximum after the ascending blocks is n+1. The central
block has alternating fluctuations at that height followed by two L
moves, so it ends at n-1 and never exceeds n+1. Each descending
(RL)^j L lowers the endpoint by1, fluctuating upward by at most1;
none exceeds n+1. The final endpoint is0 and all internal differences
are positive. For n=1 the history is RRLL and the maximum is2.
Thus the unique strictly upper witness has maximum separation exactly
n+1. There is no other smaller equal-context witness available.

Taking n=D gives h_D in F but not F_D. Its proper factors are
canonical, so none can contain an F_D member; the whole word is not
an F_D member either. Hence h_D belongs to K_D minus K. The strict
Perron deletion argument can use this explicit f=h_D, of length
2D(D+1), with the explicit reset length4D. It proves (4) for every
D>=1 without a state enumeration. Combining it with accepted
convergence and the accepted moment error proves (5).

Nothing here proves rho_D>rho_(D+1) at every step; plateaus between
successive finite caps remain possible. No finite cap attains lambda.

## 7. What this says about renewal closure, and what remains open

The accepted exact identity is

    C(z)=1/(1-2z+F(z)), R=1/lambda,
    F(R)=2R-1, F'(R)<=2.

The accepted cap3 grammar and the accepted first-moment tail theorem
remain valid. The new candidate adds a language obstruction: a finite
automaton cannot recognize the full actual F or lexicographic K, and
regular actual subsets of F always leave a strict rate gap. In
particular the accepted sequence of rational cap-renewal approximants
never becomes exact at any finite cap.

Nonregularity of a language does NOT imply that its ordinary counting
series is nonrational or nonalgebraic. It also does not imply that its
exponential growth is transcendental, or preclude another regular
cross-section or finite weighted representation of the same counts.
Those stronger assertions are not made. The official distinct binary
string language B is not identified with K, and no claim that B itself
is nonregular follows here.

An exact unrestricted grammar, a summation of F(z), tail analyticity
beyond R, the sign of the full derivative gap2-F'(R), and an evaluated
exact lambda all remain unresolved. The known enclosure is unchanged:
1.76522347<lambda<1.834856083. No algebraic candidate value is proposed.

## Attribution and verification boundary

The staircase family, its rigidity, strict upper witnesses, factoriality,
renewal and bounded-separation hierarchy are repository accepted inputs,
attributed to their original constructors and two independent reviews.
Their finite certificates are not rerun here. Pumping, right-language
DFA minimization and finite Perron comparison are standard methods;
the proposed application is NR1–NR4 and no priority is asserted.

The deeper primary-source report was read in full. Fresh primary
inspection of [Mohri's bounded-delay definition](https://cs.nyu.edu/~mohri/pub/edit.pdf)
and [queue-action normal forms](https://eiche.theoinf.tu-ilmenau.de/kuske/Publications/HusKZ14.pdf)
confirms that neither automatically supplies an exact
recognizer for this coupled two-tape equality. No theorem identifying
these monoids or giving bounded delay is imported. Full source/read
scope, unsuccessful directions, commands and preservation hashes are
in the companion records. No mathematical program, CAS, larger cap,
history scan, native download, contact, charge, Git operation or
shared-file change was used in this construction.
