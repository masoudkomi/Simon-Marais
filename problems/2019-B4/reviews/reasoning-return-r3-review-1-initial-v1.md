# Initially blind WHOLE NR1–NR4 audit R1

2026-10-17 UTC. Reviewer: coordinator root. **No substantive defect found in the complete stated NR1–NR4 scope.** This is one fresh independent whole audit, not acceptance; the second initially blind nonconstructor report and coordinator reconciliation are still required.

Exact target: `notes/reasoning-return-r3-candidate-v1.md`,20957bytes, SHA256 `6530949cc16310fabb68a3405266ab5f376a9d153a930bafda0d969ba493f296`; eight-record manifest SHA256 `6e9dd78603daa564999d083f4234f2e83d6aa063d738c6936704eaca3f33b9cb`.

Root did not construct or contribute any proof step to NEW NR1–NR4. Root authored the older accepted moment-tail result; that is a disclosed background dependency only for the final numerical error comparison, and this is not an independent re-audit of root's own earlier result. The assignment requested conceptual language research without supplying this budget/pumping/reset argument. No peer NR findings were read before this COMPLETE initial freeze. No mathematics program, enumeration, cap enlargement, CAS or author-code rerun was used.

## Complete reads and official domain

Read the whole current candidate, all20 obligations, research log, source audit and source JSON. Read the COMPLETE accepted initial proof, second-pass register, all three linked canonical/rigid/staircase texts, the full accepted bounded-separation body, the full accepted moment-tail exposition and their four acceptance scopes. Historical unverified labels inside unchanged old bodies are governed by their exact accepted registers. Those accepted theorems, rather than their finite checks alone, supply the premises.

Freshly checked official2019 PaperB p2 B4(b). It counts distinct generated binary strings and asks for their lower/upper root growth. The candidate uses a different chronological marked-context language K, with one least history per context. The accepted polynomial marked-fiber comparison and all-length growth theorem identify the SAME lambda; they do not identify K with the original string language. This distinction is maintained throughout. Preliminary(a) is not researched.

## 1. Reconstructing the unrestricted prefix budget

For two histories h,g of the same complete tapes at the same source time t, each has consumed precisely the same alternating source prefix. If the upper path has left surplus d>0, it has consumed d extra left-tape symbols and d fewer right-tape symbols. The two extra strings must have the same zero/one multiplicities. Full tape order and the common alternating source, not merely equal final lengths, justify this conservation law.

In f=a(RL)^m b, write alpha for the bit on each displayed R and beta for the opposite bit on each L. Let U_a,V_a be the prefix tapes, u=#beta(U_a), K0=#beta(V_a). At j completed pairs the left and right prefixes are U_a beta^j,V_a alpha^j, and total available beta count is u+K0+j. These formulas also hold when |a| is odd, by complementing the phase.

Suppose m>=2K0+1 and take j=K0. Both a and b are nonempty by the accepted RR/LL endpoints of f. Thus t=|a|+2K0 is internal, even for K0=0, and the accepted strict upper witness has surplus d>0 there. If it has passed the whole left beta block, its left beta count alone is at least u+m>u+2K0, impossible. If it has not passed it, its left endpoint lies inside that block and its left beta count is u+K0+d, forcing d<=K0. Its right consumption is then at least |V_a| and at most |V_a|+K0, so its right beta count is exactly K0. Combined beta count is u+2K0+d, again impossible. At K0=0 the intermediate inequality already gives d<=0. This proves NR1 without any bound on the witness separation and without assuming exactly two histories.

I challenged the possibility that a witness jumps beyond the entire left block: the first case above explicitly excludes it. I also checked the inclusive endpoint when its left consumption reaches the block's end; counting that as either case gives the same contradiction. No future suffix symbol can rescue the source budget.

## 2. Pumping and the exact nonregularity consequences

An r-state DFA accepting a regular G subset F cannot accept a word with m>=r consecutive RL pairs. Along the m+1 pair-boundary states some two coincide. Repeating the intervening positive RL-power loop keeps the fixed prefix a, fixed suffix b and source phase, yet makes m unbounded. NR1 forbids this. Rejecting states or transient lead size do not affect the accepted-run argument. Thus every such G avoids (RL)^r as a factor.

The accepted staircase h_n contains (RL)^(n−1) in the first descending block for n>=2 and belongs to F by its unrestricted rigidity theorem. Taking n=r+1 disproves regularity of F. This uses the pumping constraint in addition to the sparse staircase family; unbounded word length alone would not suffice.

For factorial K containing L,R, a word is minimal forbidden exactly when its proper prefix and suffix lie in K but it does not: F=((Sigma K) intersect(K Sigma)) minus K. Factoriality covers every other proper factor. Hence regular K would imply regular F, contradicting the preceding conclusion. There is no length-one exception.

Appending R cannot complete a forbidden factor because all minimal factors end LL; factoriality gives the reverse implication hR in K => h in K. If K_even were regular, odd canonical words would be the odd-length part of its right quotient by R, so all K would be regular. The fixed two-letter block code from LL,LR,RL,RR has exactly K_even as the image of the blocked canonical language, proving that language nonregular. This proves nothing about arbitrary other cross-sections.

If the synchronous zipped equal-context relation E were regular, intersect it with the finite-state test g<h and project onto h. That yields exactly the noncanonical histories, since each finite context class has a least member. Projection and complement would make K regular. Equal contexts require equal lengths, so synchronous padding is unnecessary. This argument does not apply to an arbitrary asynchronous representation.

## 3. Universal bridge, minimal DFA and finite Perron argument

For regular G subset F use W=(RL)^r. In aWb with a,b avoiding G, a forbidden occurrence cannot lie wholly in an outside word. It cannot start inside W, including its last L, because it must start RR; nor can it end inside W, including its first R, because it must end LL. An occurrence across a seam must therefore span all W. That contradicts the no-(RL)^r property. Empty outside words create no exception.

Avoid(G) is regular as the complement of Sigma*G Sigma*. It is factorial and prefix-closed; the minimal complete DFA has just one rejecting sink. For any accepting state reached by a, the state after W accepts exactly the original language: aWb is accepted for all accepted b by the bridge, and if it is accepted then its factor b is accepted. Equality of right languages in the MINIMAL DFA makes W a reset to the initial state. All remaining states are reachable from that state and return via W, so the nonrejecting graph is strongly connected. Prepending L creates no new member of G starting at that L, giving an initial L-loop. This is a minimal-DFA statement, not a literal empty-queue assertion about an unminimized monitor.

Let A count its letter transitions, including multiplicities for two labels with the same endpoints. Positive right Perron vector v gives constant upper/lower bounds on e0^T A^n 1 by rho(A)^n. Thus its spectral radius is rho_G without a numerical or primitivity assumption.

Since regular G cannot equal nonregular F, take f in F minus G. Anti-factoriality of F ensures f avoids G, so an actual path labelled f exists. In the finite higher-edge graph whose vertices are legal(|f|−1)-paths and edges legal|f|-paths, strong connectivity follows by joining endpoint states in the original graph. Its path rate is rho_G; shifting path length by the fixed |f|−1 and finite starting multiplicity do not change that rate. Delete ALL edges labelled f, at least one. For the resulting B, 0<=B<A_H and A_H is irreducible.

The candidate's strict comparison is valid even if B is reducible. A nonzero nonnegative right Perron vector x of B and a positive left Perron vector w of A_H would, if the radii agreed, give w^T(A_H−B)x=0. Hence(A_H−B)x=0 and A_H x=rho_G x. Irreducibility forces x positive, so all entries of A_H−B vanish, contradiction. Every K-word has a B-path because K avoids f. Finite matrix powers, with a polynomial factor if needed, therefore give lambda<=rho(B)<rho_G. This proves the WHOLE NR3 statement, including infinite regular G. It imports no strict constrained-entropy theorem.

## 4. Explicit cap reset and an actual missing staircase

At the middle of W_D=(RL)^(2D), a strictly upper cap-D witness has1<=d<=D. Its extra left d symbols are beta from the second half; its missing right d symbols are alpha from the first half. They have different symbol multiplicities, contradicting the same source-prefix conservation. At d=D both segments reach a block endpoint but do not pass it. Both phases and D=1 are covered. RR/LL endpoints force any F_D occurrence across the bridge to span it; hence W_D universally bridges K_D and resets its MINIMAL accepting DFA.

For h_n the accepted rigidity gives exactly one alternative, its side exchange. Their separation is prefix#R−#L. Initial RR reaches2. Ascending(LR)^j R blocks raise the endpoint by one each; their internal fluctuation does not exceed the new endpoint, giving n+1 after the last ascending block. The central alternating block fluctuates below or at n+1 and LL lowers the endpoint to n−1. Each descending(RL)^j L decreases the endpoint by one with at most a one-step rise, never exceeding n+1. All internal differences stay positive and the final one is0. Directly n=1 is RRLL with maximum2. Thus the minimum witness width is exactly n+1, including the boundary cases n1,n2.

Therefore h_D is in F but outside F_D. Every proper factor is canonical and cannot contain an F_D factor, so h_D itself lies in K_D minus K. NR3, or the explicit bridge plus deletion of h_D, yields rho_D>lambda for EACH finite D. The previously accepted moment estimate supplies the upper error1/(D+1), and the accepted cap theorem supplies monotone convergence. No argument gives strict decrease between consecutive caps; plateaus remain possible.

## Outcome and limits

All20 author obligations and the additional adversarial endpoint/representation/Perron checks were addressed. No substantive counterexample or required repair emerged. The exact enclosure stays1.76522347<lambda<1.834856083. Neither nonrationality/algebraicity of the series or rate, nonregularity of the original binary-string language, an exact grammar, an evaluated constant, nor novelty follows. The candidate accurately retains these limits.

The separate source/integrity record gives actual reads and byte checks. No finite certificate was rerun and none proves these unrestricted new claims. This WHOLE initial is frozen before peer findings; the coordinator must await and reconcile a second fresh whole audit before any promotion.
