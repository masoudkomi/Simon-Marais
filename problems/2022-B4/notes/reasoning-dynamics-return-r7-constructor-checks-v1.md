# D7 constructor hand reconstruction checks

18 October 2026 UTC. Candidate proof - unverified. These are constructor
checks, not either of the TWO OTHER independent audits. No mathematical
executable or finite test supplied a check.

| ID | Hand disposition |
|---|---|
| D7-01 | CHECKED: O requires a,b positive integers and ab>=600; both new coordinates use the old pair; Omega excludes time zero too. |
| D7-02 | CHECKED: no trapping proof is needed. All new ancestry is in O and the exact full map; the scalar ceiling literature is context only. |
| D7-03 | CHECKED: Omega is defined with a universal all-future quantifier and may be empty; D7C alone has its nonemptiness hypothesis. |
| D7-04 | CHECKED: full accepted D6/CF and current MD/JSON read; only unconditional CF growth imported; C's CF/SR construction and old review roles disclosed. |
| D7-05 | CHECKED: S_next=1.1S-(r+s)/10, r<=29,s<=19, with a negative remainder correction. |
| D7-06 | CHECKED: geometric coefficients in E sum to (1/11)/(1-10/11)=1, so E belongs to [0,48]; Lambda is a real sum limit. |
| D7-07 | CHECKED: S<=48 implies ab<=576, contradicting 600; integer S>=49 yields Lambda>=1. |
| D7-08 | CHECKED: starting the actual orbit k clocks later multiplies Lambda by beta^k; it is never ignored in a collision comparison. |
| D7-09 | CHECKED: S<=L+48 gives at most M(M-1)/2 positive pairs; product filtering only lowers this number. |
| D7-10 | CHECKED: F(z_n)=x_n and z_n differs from x_(n-1); there is no parent indexed at the output clock itself. |
| D7-11 | CHECKED: k=0 includes z_n in A_n, and every y is official in its own starting clock. |
| D7-12 | CHECKED: every ancestor's Lambda<=Lambda(z_n), so it is in a finite G_L. No p-adic or compactness inference occurs. |
| D7-13 | CHECKED: Lambda(y)>=1 bounds k<=n-1+log_beta Lambda(x); finite nonempty depths attain K_n and minimum (1.2). |
| D7-14 | CHECKED: beta^(n-1-k)Lambda(x)=beta^(m-1-l)Lambda(x) forces equal exponents, hence l-k=m-n. |
| D7-15 | CHECKED: m-n>=1 makes F^(m-n)(z_n)=F^(m-n-1)(x_n)=x_(m-1), not x_m. This contradicts proper z_m. |
| D7-16 | CHECKED: the contradiction works for ANY common official ancestor, so entire sets A_n are disjoint. |
| D7-17 | CHECKED: each set meeting the fixed finite G_L uses a different point of it; at most |G_L| clocks qualify. |
| D7-18 | CHECKED: for each fixed L, only finitely many clocks have even ONE small ancestor. All choices escape uniformly along the infinite clock set. |
| D7-19 | CHECKED: formula (1.2) and beta>1 turn the minimum-growth escape into n-1-K_n->infinity; initial negative values are allowed. |
| D7-20 | CHECKED: K_n>=n-1-R implies minimum Lambda<=beta^R Lambda(x); finite G at that threshold gives (0.7), without locating events. |
| D7-21 | CHECKED: an ordered nonzero input gap remains positive in at least one output coordinate, so a same-output pair must be unordered. |
| D7-22 | CHECKED: output congruences a mod2 and b mod3 force differences multiples2 and3; relabeling gives positive u,v. |
| D7-23 | CHECKED: floor(t+h)-floor(t)<=ceil h for positive rational h holds under ordinary negative division as well. |
| D7-24 | CHECKED: u<3v/20+1<u/100+23/20 gives u<115/99; positive integer u=1, then v<=ceil(1/15)=1. |
| D7-25 | CHECKED: gap(2,-3) cancels iff the a remainder crosses30 and the b remainder crosses its preceding20 boundary, giving precisely (3.1)/(3.2). |
| D7-26 | CHECKED: three preimages would include a pair at twice the only allowed gap, impossible; at most two follow without an onto theorem. |
| D7-27 | CHECKED: the listed modulo60 diagonal residues miss both paired modulo20 sets; this works for every ordinary integer c. |
| D7-28 | CHECKED: (3.3) is about F(c,c)'s fiber, not about whether an arbitrary diagonal output has a diagonal parent. |
| D7-29 | CHECKED: a bounded coordinate becomes constant and forces the other coordinate below its floor threshold; final a<=29,b<=19 violates ab>=600. |
| D7-30 | CHECKED: late x_(n-1) has both coordinates arbitrarily large, and the sole possible alternative moves them by at most3; it is then official. |
| D7-31 | CHECKED: a diagonal z_n would have a singleton image fiber by (3.3), contrary to the different parent x_(n-1). |
| D7-32 | CHECKED: z_n is itself off-diagonal, then maps to x_n; if x avoids for every future time, so does z_n. |
| D7-33 | CHECKED: z_n belongs to A_n^Omega, a finite set with bounded possible depths; a deepest source exists. |
| D7-34 | CHECKED: an official off-diagonal parent has no earlier clock before itself, and its future is the avoiding source; it lies in Omega and extends the chain. |
| D7-35 | CHECKED: if an official parent is diagonal, (3.3) makes it the only ordinary parent. Otherwise no official parent exists at a source. |
| D7-36 | CHECKED: these are full positive-domain sources, with no inside-strip claim; an ordinary outside-strip predecessor is a separate issue. |
| D7-37 | CHECKED: source sets are subsets of disjoint A_n; their growth escapes with all A_n and they are distinct actual Omega starts. |
| D7-38 | CHECKED: after the last proper official collateral, any second ordinary parent would be official by size, a contradiction. No exclusion of this branch is claimed. |
| D7-39 | CHECKED: restriction to Omega ancestry is explicit; a full official ancestor can have a past diagonal hit and cannot automatically transfer a counterexample. |
| D7-40 | CHECKED: N=0 gives (138,137), and larger N increase both coordinates; all products exceed600. |
| D7-41 | CHECKED: t_j=2*11^j*10^(N-j); for j<N, common floor contributions multiply60t by11/10 and leave residues18/17. |
| D7-42 | CHECKED: at j=N the next common term is132*11^N; 11^N=1 mod10 makes it60k+12 with k=(11^(N+1)-1)/5. |
| D7-43 | CHECKED: state (60k+30,60k+29) maps to (66k+32,66k+32); all prior differences were1, so the first hit is N+2. |
| D7-44 | CHECKED: flat residues18/17 miss both double-input rectangles; the last avoiding state has residues0/9 and also misses them. All image fibers are singleton. |
| D7-45 | CHECKED: arbitrary finite avoiding prefixes with no branch refute a uniform finite-window criterion; they do not decide branching for a truly infinite avoider. |
| D7-46 | CHECKED: P3 delay, Q1 geometry and CF proper growth are old and attributed; new contribution is disjoint ancestry/escaping phase plus its exact route obstruction. |
| D7-47 | CHECKED: original scalar proof scopes are read literally; no conjectural residue escape or matrix digit finiteness substitutes for the coupled ordinary map. |
| D7-48 | CHECKED: only new exclusive prefix written; full packet must freeze, receive full final model readback and separate read-only verify before handoff. Independent review remains outstanding. |
