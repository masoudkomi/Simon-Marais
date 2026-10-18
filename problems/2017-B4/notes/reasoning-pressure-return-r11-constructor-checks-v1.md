# R11 hand reconstruction and adversarial checks

Candidate proof - unverified. No mathematical program or certificate
was used. These are constructor checks, not independent audits.

1. **The old feasible-family obstruction is retained.** The new raw
sigma2 is strictly above one. Flow is applied only AFTER row normalization
and an adapted two-edge target discount. The new certificate does not
contradict the unique optimum over simultaneously feasible raw rows.

2. **Both diamond routes really contribute.** A->w being middle
would force i(w)=1; PM8 gives i(w)=2. A has o>=2, so the edge is
extreme, not unique. The same holds for B. Even though routes end at
the same w, they differ at their first edge. Prefix-tree flow retains
both. No assumption that the whole dual is a tree appears.

3. **The most dangerous intermediate case is handled without a
degree cap.** If A is bad with very large outdegree, we use its own
discount and sum its ENTIRE normalized second row to one. A route
probability lower bound at a high-degree vertex would be false in
general; it is neither stated nor used. If A is good, its outdegree
is exactly3 or4, since i(A)=1 and boundedness gives o(A)>=2.

4. **Symmetric flags do not lose endpoints.** R counts degree2 or>=5
rows at BOTH orientations. Source indegree0 and sink outdegree0 are
not rows. Source outdegree2 or sink indegree2 still pay correctly.
Trial targets miss the current/source vertex, but R_full is SMALLER
than the partial target product. Missing factors<=1 help the required
inequality. If w were a terminal, its positive indegree2 is still a
reverse row; the local argument does not turn terminal degree0 into
a penalty. The outdegree4 rank qualification supplies two steps.

5. **Both signs and all rows in the cancellation were checked.**
Raw products may have total mass>1 and are used only pointwise.
S*S'<=chi^c*R^2 implies sqrt(PQ)*R>=sqrt(WW')*chi^(-c/2),
which is the lower bound needed in a Cauchy upper sum. The reward
z^(c/2) then leaves xi^(c/2), not its reciprocal. The intermediate
full R is the SAME on the forward and reversed path.

6. **The geometry-independent constants are fixed first.** No
future path, empirical class, size cutoff or optimized finite table
selects lambda. The comparisons prove mu>2/11 and chi<801/800 with
ample rational slack. For the discount, both candidate costs exceed
17/2200, while2mu>4/11. The bound chi^2-1<dstar is sufficient;
the exact positive cross term in chi^2*a only strengthens it.

7. **Integer and derivative arithmetic was hand expanded.**
2109^2=4447881;2109^3=9380581029;2109^4=19783645390161.
The chi numerator is22483332161. The all-j ratio starts at j3
and strictly decreases; no finite row scan stands for an infinite
argument. The comparison uses the old rational19/9 ONLY to identify
current H, and newlambda2109/1000 ONLY for G. All derivatives are
on the full positive-denominator interval[21/10,19/9].

8. **Small n and pressure endpoints.** At n2/3 no degree-four
trial can start, c=0 and the flow/cancellation proof still applies.
At N2 the unique class has D2=0 and E2=0, so the pressure bound is
equality. Generally0<=D_N<=2E_N. For real h>2E_N the actual tail
is empty; h0 simply recovers the unweighted upper bound. A pressure
weight is not an extra history multiplicity.

9. **Canonical versus all insertion histories.** The largest-label
deletion chain is uniquely fixed by the marked boundary. There may
be many reduced word representatives and many other deletion orders.
They are not summed. Degrees/path data survive commutations and
marked isomorphism. A hypothetical symmetry of the drawing does not
erase canonical boundary slots or introduce a factorial denominator.

10. **Strict comparison actually reaches PM9.** A new G<K alone
would not suffice. The hand comparison separately bounds
ln(K/G)>1/6000 and ln(K/H)<1/12309, hence the positive exact
ln(H/G) gap701/8206000. No floating point or unproved equality
of upper/lower rates enters this comparison.

11. **What is still missing.** This moment controls one canonical
degree statistic in actual classes. It does not identify its typical
distribution, construct many classes near the upper bound, evaluate
the official scalar, or establish effective convergence. Turning an
absolute upper tail into a uniform-class probability would require
a separately justified denominator. Published priority is unproved.
