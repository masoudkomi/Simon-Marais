# NR1–NR4: independent whole initial audit R2

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`; requested gpt-6.1-sol/max, verified effective-setting readback unavailable. This is a fresh initially blind nonconstructor WHOLE audit. The constructor is `review_2021_reasoning_j15_r2`. I did not construct NR1–NR4. The coordinator's independent NR report and findings have not been read. Only the coordinator can promote a result after reconciliation; the submitted proof remains **candidate proof — unverified** at this initial freeze.

## Outcome and submitted scope

I find no substantive objection to NR1–NR4 in the stated scope, and request no author repair. I reconstructed all new arguments, including the unrestricted prefix budget, the pumping consequences, the bridge/reset and higher-edge Perron proof, and the cap-specific midpoint and staircase-width arguments. The companion ledger records 45 individual checks and targeted counterexample attempts. This is not an exact evaluation of the official growth constant, nor a conclusion about nonrational counting series or every possible representation.

The full reviewed candidate is `problems/2019-B4/notes/reasoning-return-r3-candidate-v1.md`, 20957 bytes, SHA256 `6530949cc16310fabb68a3405266ab5f376a9d153a930bafda0d969ba493f296`. Its eight-record manifest is 3091 bytes, SHA256 `6e9dd78603daa564999d083f4234f2e83d6aa063d738c6936704eaca3f33b9cb`. I read the complete candidate, research log, source audit, twenty obligations, administrative freeze script and source metadata. All exact accepted mathematical inputs and their acceptance scopes were read, rather than relying on a summary of new NR claims.

Prior context is disclosed. I previously independently audited the accepted 2019 moment/tail M1–M3 packet, which the coordinator constructed; the current NR author was its other reviewer. That prior review did not construct the new prefix budget, pumping argument or NR1–NR4. My earlier all-D global construction and GK review were frozen before this task and remain unchanged. Knowledge that the coordinator's NR initial exists reveals no finding; its body was not read.

## 1. Official counting problem and accepted input scope

The [official 2019 Paper B, page2 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf) was reopened directly. It counts distinct output binary strings generated from the seed1, with the bit appended or prepended determined by the current length parity. The requested quantities are lower and upper limiting root growth. Histories are not those output strings. I use only part(b) and accepted background results; no proof of preliminary part(a) is reproduced.

A history h on Sigma={L,R} routes the alternating source sequence to two chronological tapes. The physical left context is the reverse of its chronological left tape. Reversing that tape is a bijection, so it changes neither context equality nor its counts, but its order cannot be silently reversed in the new prefix argument. K consists of the lexicographically least history, L<R, for each chronological context pair; c_n counts these contexts after n moves. The initial accepted marked-fiber proof shows the official length-(n+1) outputs and marked contexts have fibers of size at most n+1, and the accepted even-block subadditivity proves the same growth lambda. The second-pass extension gives the same root growth for all c_n. This is equality of exponential growth rates, not an identification of K with the official string language B.

I read the full initial `proof.md`, the second-pass acceptance register and all three linked complete mathematical notes, the accepted third-pass body, and the full accepted moment/tail body. Their exact used conclusions are:

- K is factorial and K=Avoid(F), where F is the actual minimal noncanonical factor set. F is anti-factorial and cross-bifix-free. Every f in F starts RR, ends LL, and has a strictly upper equal-context witness at every internal time. This holds even for contexts having more than two histories.
- For every n>=1 the displayed staircase h_n is in F. Its context has exactly two histories, h_n and its side-exchange. Proper factors have unique contexts. The proof is an unrestricted forced-choice argument, not a table extrapolation.
- For every integer D>=1, F_D is exactly the subset of F admitting a strictly upper witness of maximum separation at most D. It is regular; K_D=Avoid(F_D) is regular and factorial; F_D agrees with F through length 2D+1. The rates rho_D are nonincreasing and converge to lambda. The envelope lemma is part of this accepted identification; a mere guessed subset of bad histories would not suffice.
- The accepted renewal identity and first-moment theorem imply rho_D−lambda<=1/(D+1). No new sign computation or numerical tightening is needed by NR4.

The acceptance registers grant precisely these statements. Historical candidate labels inside unchanged source texts do not cancel their accepted scope. I did not rerun any historical history enumeration, cap monitor, grammar certificate or numerical sign program.

## 2. NR1: the symbol budget with no bound on the lead

For legal paths f,g with the SAME complete tape pair, define d(t)=ell_g(t)−ell_f(t)=r_f(t)−r_g(t). If d(t)>0, g has read the next d left-tape symbols beyond f, while f has read d additional right-tape symbols beyond g. Each has read the same alternating source prefix of length t. Removing their common consumed tape prefixes therefore shows those two extra segments have equal zero and one multiplicities. This conservation uses the actual chronological tape words. It does not follow from equal tape lengths alone.

Take f=a(RL)^m b in F, m>=1. Its RR start and LL end make both a and b nonempty: a word beginning or ending with the displayed RL block could not have the required endpoint. Let alpha be the source bit at the first R, beta its opposite, U_a,V_a the chronological tapes of the prefix a, u=#beta(U_a), and K0=#beta(V_a). At j complete RL pairs the f-prefix tapes are U_a beta^j and V_a alpha^j. The entire source prefix contains exactly u+K0+j beta symbols, regardless of whether |a| is even or odd.

Choose a strictly upper witness g, available for this actual minimal factor. Suppose m>=2K0+1 and take t=|a|+2K0. This is strictly inside the full history: a is nonempty and K0<m, while b is nonempty. Hence d=d(t)>0, including K0=0. At this time f has consumed |U_a|+K0 left symbols and |V_a|+K0 right symbols.

The possibility of an arbitrarily large lead needs explicit treatment. If g has consumed all m left beta symbols of the displayed block, its left tape alone contains at least u+m beta symbols. The entire available source prefix contains only u+2K0. Since m>2K0, this is impossible, even if g tries to continue into the later suffix. Thus g's left endpoint is still inside the beta block. Its left beta count is exactly u+K0+d. Availability forces d<=K0.

That inequality implies g has consumed |V_a|+K0−d>=|V_a| right symbols. It trails f, so every right symbol beyond V_a lies in the alpha block. Its right beta count is consequently exactly K0. Its combined beta count is therefore u+2K0+d, exceeding the available u+2K0. This contradiction proves m<=2K0. For K0=0, the intermediate d<=0 is already a contradiction. No strictness at time0, bounded-separation assumption, two-history assumption, or assumption that g shares the prefix a was used.

Changing the source phase complements alpha,beta and the tape bits throughout. Every displayed count and inequality is preserved. Thus odd prefix lengths and embeddings at the other source phase introduce no exception. Equality m=2K0 is not asserted impossible; only the bound needed for the subsequent pumping argument is claimed.

## 3. NR2: pumping, F and K, and the two precise encodings

Let a DFA with r>=1 states recognize a regular G subset F. If an accepted word has a factor (RL)^m with m>=r, inspect its m+1 states at the pair boundaries. A repeated state gives a positive loop (RL)^p. Repetition produces a(RL)^(m+kp)b in G for every k>=0, with the ORIGINAL a,b fixed. The inserted length is even, so the source phase and V_a are also fixed. Applying NR1 to these actual F words gives a fixed upper bound on an unbounded exponent, a contradiction. Therefore no member of G contains (RL)^r. This uses an actual recognizing DFA and G subset F, not a finite observed prefix or an assumed sound approximation.

The accepted h_n contains (RL)^(n−1) in its first descending block when n>=2. If F had an r-state DFA, h_(r+1) would violate the preceding bound. This supplies the missing logical step beyond sparse staircase evidence and proves F nonregular.

For factorial K containing both letters and the empty word,

    F=((Sigma K) intersect (K Sigma)) minus K.

A word on the right has its length-(n−1) prefix and suffix in K, hence every proper contiguous factor in K. The converse is immediate for a minimal bad factor. Length-one words cause no exception because both letters are canonical; the empty word is not in Sigma K. Thus regular K would give regular F by regular closure, proving K nonregular.

The even-word consequence requires an extra argument and is present. For every h, h is canonical iff hR is canonical. Forward, appending R cannot complete a forbidden factor ending LL. Reverse, factoriality applies. If K_even were regular, its right quotient by R, intersected with the odd-length language, would be K's odd part. Their union would make all of K regular. Therefore K_even is nonregular. The fixed two-letter code A->LL,B->LR,C->RL,D->RR is a bijection onto even-length histories and preserves their lexicographic order. Every competing context history has the same even length, so blocked canonicality is exactly the inverse image of K_even. A regular blocked language would have a regular homomorphic image, a contradiction.

For synchronous equality, a context equality forces equal history lengths because total tape length equals the move count. The lexicographic test g<h on a zipped pair is finite-state. If the zipped equal-context relation were regular, intersecting with that test and projecting to h would give the noncanonical histories: each finite context class has a least element, and every other element has a smaller equal-context partner. Complementation would give regular K. This contradiction proves only the asserted synchronous representation is nonregular. It does not rule out every asynchronous relation, different normal form, regular cross-section, or other monoid presentation.

## 4. NR3: seams, follower reset and strong connectivity

For regular G subset F with r-state recognizer set W=(RL)^r. Let a,b avoid G. Any new G occurrence in aWb must span W completely. It cannot start inside W: every member starts RR, while each R in W is followed by L and W's last letter is L. It cannot end inside W: every member ends LL, while each internal L has preceding R and W's first letter is R. This includes starts or ends adjacent to a seam. An RR seam across a/W starts on the a side, and an LL seam across W/b ends on the b side; such an occurrence would still contain the whole W. Occurrences contained in a or b are excluded. The remaining spanning occurrence would contain (RL)^r, which the pumping result forbids. Empty a or b remove possibilities and create no exception.

Thus aWb is always in L_G=Avoid(G). L_G is regular because its complement is Sigma*G Sigma*. It is factorial and prefix-closed, contains the empty word, both letters and all-L words. In its minimal complete DFA, every reachable rejecting state has empty right language, so all such states, if present, collapse to a single sink. Removing that sink gives the minimal nonrejecting partial DFA M, all of whose states are accepting and reachable. For G empty there is no rejecting state to remove; M is simply the one accepting state with two loops. The proof's sink-deletion convention is interpreted this way, with no mathematical exception to its claimed result.

Suppose q is reached by a in L_G. The bridge gives an existing state q'=delta(q,W), from which every b in L_G is accepted. Conversely acceptance of b from q' puts aWb in L_G, and factoriality puts b in L_G. Therefore q' has exactly the initial right language. Minimality forces q'=q_initial. W resets every state to that state. Because every other state is reachable from it, M is strongly connected.

Prepending L cannot create an occurrence starting at the new letter, since every G word starts R. Hence Lb is in L_G iff b is. Minimality gives an initial L-loop. The loop verifies aperiodicity, but it is not required for the subsequent strict comparison. Reset is asserted for the minimal follower-language DFA, not for the raw residual-subset implementation of an earlier cap monitor.

## 5. NR3: the actual missing factor and entropy deletion

Let A count M's letter edges, with multiplicity when two letters share endpoints. Strong connectivity gives a finite irreducible nonnegative matrix. A positive right Perron vector v with eigenvalue rho gives

    (v_initial/max v)*rho^n <= e_initial^T A^n 1
                            <= (v_initial/min v)*rho^n.

These follow by multiplying v/max v<=1<=v/min v by nonnegative A^n. Because M is deterministic and all its states are accepting, the middle count is exactly the number of L_G words. Thus rho_G=rho, including the possibility of a periodic irreducible graph; no aperiodicity hypothesis is being silently inserted.

F is nonregular and G regular, so f exists in F minus G. It avoids G: a contained G word could not be a proper factor of another F word by anti-factoriality, and equality is excluded by f not in G. Therefore f labels an actual legal path from M's initial state. This is more than choosing an abstract missing word without a path.

Put ell=|f|>=4. Build H with vertices actual legal M paths of length ell−1 and edges actual legal M paths of length ell, joining the overlapping path windows. M's strong connectivity makes H strongly connected: follow a first vertex-path, a connector in M to a second path's initial state, then that second path; the successive windows give an H path. Each length-n H path corresponds bijectively to a length-(n+ell−1) M path with an arbitrary initial state. There are only finitely many M states, and the positive Perron-vector bounds apply at each, so the shift and summation preserve the root growth rho_G. Equivalently, determinism gives at most the number of M states many paths with a given label. The higher-edge matrix A_H is irreducible and has spectral radius rho_G.

Delete all H edges whose full ell-letter label is f. At least one is present because of the actual f path. Parallel edges, if any, are counted, so deletion makes a strictly smaller matrix B, with 0<=B<A_H. The deleted matrix need not be irreducible. If its spectral radius equalled rho_G, take a nonzero nonnegative right Perron vector x of B and a positive left Perron vector w of A_H. Then

    w^T(A_H−B)x=0.

All terms are nonnegative and w is positive, so (A_H−B)x=0. Thus A_H x=rho_G x. Irreducibility makes x positive; a nonzero nonnegative matrix A_H−B cannot annihilate a positive vector. This contradiction proves rho(B)<rho_G. This is the standard finite Perron theorem with its exact hypotheses established, and the strict comparison is proved in the packet rather than inferred from numerics.

Every canonical word is accepted by M and avoids f. For length at least ell−1, its unique initial-state M path defines an H path using only B edges. Its initial H vertex stores the first ell−1 letters; the remaining edges store the remainder, so different canonical words are not identified. Summing over finitely many possible starting vertices gives an upper bound by B path counts. A finite matrix's path counts have root limsup at most its spectral radius, allowing a polynomial prefactor if B is reducible. Hence

    lambda <= rho(B) < rho_G.

No complement-language regularity, new word count, or numerical eigenvalue estimate was assumed. The conclusion applies to every regular G subset of the ACTUAL F, including infinite G and empty G. It is not a theorem about every regular superlanguage or another representation with the same counts.

## 6. NR4: exact cap bridge and every finite cap gap

For D>=1 set W_D=(RL)^(2D). A forbidden F_D occurrence across aW_Db, with a,b in K_D, must span W_D by the same RR/LL endpoint argument. Inside that occurrence take a strictly upper witness of cap D, guaranteed by the accepted exact definition of F_D. At the midpoint of W_D, f has consumed D of its right alpha bits and D of its left beta bits. The current surplus is an integer d with 1<=d<=D. Its next d extra left symbols are all beta and its missing d right symbols are all alpha, since D such symbols remain/precede within the block on the respective tapes. Their multiplicities cannot agree. This contradicts source conservation.

At d=D the segments reach exactly the two ends of the relevant block portions; they do not pass them. The midpoint is internal to the occurrence. Complementing the starting phase changes neither contradiction. D=1 is included; indeed the accepted cap1 language is universal. The same right-language proof therefore makes W_D a reset for the minimal nonrejecting DFA for K_D. Its length is exactly4D. No statement about a literal empty state of an unminimized monitor is needed.

For the explicit missed factor, the accepted rigidity leaves only bar(h_n) besides h_n. Their left-count difference is #R−#L in the h_n prefix. After RR it is2. Before ascending block P_j=(LR)^j R its value is j+1; the alternating pairs lower it to j and return it to j+1, then the final R raises it to j+2. Thus the ascending endpoint maximum is n+1, attained after the last ascending block. For n=1 it is already attained after RR.

The central (LR)^(n−1)LL starts at n+1, oscillates between n and n+1, then ends at n−1. A descending block T_j=(RL)^j L starts at j, oscillates between j and j+1, then ends at j−1. All internal values are positive and only the final endpoint is zero; the n=1 history RRLL gives 1,2,1,0 directly. The maximum is therefore exactly n+1. This reconstructs the width, rather than using finite grid evidence or assuming some other smaller witness does not exist: the accepted two-history theorem excludes one.

Take n=D. Then h_D is in F but not F_D. All its proper factors are canonical, so none can contain an F_D member; the whole h_D is not one either. Thus h_D lies in K_D minus K. Its length from the block sums is2D(D+1). Using this actual f in the higher-edge deletion argument, or applying NR3 to the accepted regular F_D, yields lambda<rho_D for EVERY finite D>=1. It does not imply rho_D>rho_(D+1) at every step.

Finally the accepted moment theorem applies because F_D agrees with F through2D+1: take N=2D+2 to obtain rho_D−lambda<=rho_D/(2D+2)<=1/(D+1). Combining this OLD bound and accepted nonincreasing convergence with the NEW strictness gives precisely

    0<rho_D−lambda<=1/(D+1),     rho_D down to lambda.

No claim that the actual error has this order, or that the accepted numerical enclosure improves, follows.

## 7. Source and preservation conclusions

I read the complete accepted input bodies and acceptance scopes, the deep literature report and cache metadata, and directly inspected the relevant primary bounded-delay and queue-equivalence definitions. Mohri's finite-residual result assumes a genuine uniform path-delay bound. The queue-action normal forms concern transformations on every initial FIFO queue, a different equivalence from these tape-output contexts. Neither theorem is transferred to NR1–NR4. Standard pumping, regular closure and finite Perron existence are used with the explicit conditions established above. No inference from nonregularity to a nonrational series, transcendental growth, universal absence of a regular cross-section, or nonregularity of the official B language is made.

The full source-check record identifies actual read limits and exact fingerprints. Eight author artifacts and their manifest, 26 source-record occurrences and 276 constructor input-validation occurrences were checked; the latter counts are administrative and include earlier records. All seven initial, fourteen second-pass, seven third-pass and six moment acceptance hash entries were verified without reading new NR peer findings. All153 earlier own paths, including the entire all-D global packet and GK review, were checked unchanged. Only new files under the assigned `reasoning-return-r3-review-2-*` prefix were written. No math program, history or cap enumeration, certificate replay, CAS, shared/Git edit, spawning, contact, charge or access bypass occurred.

The latest coordinator telemetry supplied for this task was32% TOTAL weekly used at11:01:58UTC, reset1792745187. The90% TOTAL ceiling and reserve remain applicable. No repair is requested, and no result is promoted by this report.
