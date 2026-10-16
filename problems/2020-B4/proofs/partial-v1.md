# 2020 B4(b): partial package v1

**candidate proof - unverified**. Created 2026-10-16. This is not a full solution of B4(b). These are reconstructions of standard difference-set arguments and a weaker consequence of known restrictions; no originality claim is made. Published theorems used in computations are listed separately in references.md. No preliminary construction or proof of B4(a) is included.

Throughout, \(n\ge2\), \(q=n-1\), \(k=n=q+1\), and \(v=n^2-n+1=q^2+q+1\). A difference set means a subset of the specified cyclic group, with all its elements distinct.

## P1. Exact reduction, including the boundary

Label polygon vertices by \(\mathbb Z/v\mathbb Z\). Since \(v\) is odd, the possible nonzero undirected cyclic separations are \(1,\ldots,(v-1)/2\). On a circle of radius \(R>0\), their chord lengths are \(2R\sin(\pi r/v)\); these are strictly increasing on this range. Thus two unordered pairs have equal Euclidean distance exactly when their ordered differences agree up to sign.

If all unordered pairwise distances for a \(k\)-set \(D\) are different, its \(k(k-1)\) ordered differences are different: equality between differences for different unordered pairs would repeat a distance, while reversing one pair cannot leave its nonzero difference unchanged because 2 is invertible modulo odd \(v\). There are exactly \(k(k-1)=v-1\) nonzero residues, so every one occurs exactly once. Conversely, a repeated distance gives equality of ordered differences after reversing one pair if necessary. Therefore tautness is equivalent to a cyclic \((v,k,1)\) difference set.

For \(n=2\), the set \(\{0,1\}\subset\mathbb Z/3\mathbb Z\) works. This is outside the usual positive-exponent prime-power convention for \(q\).

This reduction is stated in the official 2020 solution discussion, pp. 25 and 27.

## P2. Precise projective-plane connection for q >= 2

From a difference set \(D\), take residues as points and translates \(D+t\) as lines. For \(t\ne0\), the difference-set property gives exactly one point in \(D\cap(D+t)\). In particular distinct translates are distinct lines and any two lines meet in exactly one point. Distinct points \(x,y\) determine a unique line: the unique expression \(x-y=a-b\), with \(a,b\in D\), determines the translate with parameter \(x-a=y-b\). Every line has \(q+1\) points, and every point is on \(q+1\) lines.

For nondegeneracy, choose two points \(A,B\) on a line \(L\) and \(P\notin L\). The three lines \(L,AP,BP\) have three different pairwise intersections and union size \(3(q+1)-3=3q\). Since \(v-3q=(q-1)^2>0\), choose \(Q\) outside their union. No three of \(A,B,P,Q\) are collinear. This proves the nondegenerate projective-plane axioms. Translation is a cyclic regular action on points and lines.

Conversely suppose a projective plane of order \(q\ge2\) admits a cyclic regular action on points by \(G\) of order \(v\). A line stabilizer \(H\) acts freely on its \(q+1\) points, since the point action is regular. Hence \(|H|\mid q+1\) and \(|H|\mid v\), whereas \(\gcd(q+1,v)=1\); thus \(H\) is trivial. Every line orbit consequently has size \(v\), the total number of lines, so the line action is regular as well. Identify points with \(G\) and choose a line \(D\). The unique line through any distinct \(x,y\) gives a unique ordered representation of \(x-y\) as a difference in \(D\). Thus \(D\) is a cyclic planar difference set.

This is a correspondence with planes having a cyclic regular collineation group. It does not claim that an arbitrary projective plane has such an action. It also does not claim that every cyclic plane is Desarguesian; that is a separate stronger conjecture. See Alexeev-Mixon, section 4, and the official discussion.

## P3. Two different translation normalizations

For direct search, the difference 1 occurs, say \(a-b=1\). Translating by \(-b\) makes both 0 and 1 members of \(D\). Searching increasing subsets containing 0 and 1 therefore loses no existence case. It need not enumerate each equivalence class once.

For multiplier arguments, let \(S=\sum_{d\in D}d\) in the cyclic group. Since \(v-q(q+1)=1\), \(k=q+1\) is invertible modulo \(v\). There is a unique translation \(c\) such that \(S+kc=0\). Use that translated set. If a numerical multiplier \(t\) satisfies \(tD=D+h\), summing gives \(0=kh\) and hence \(h=0\). Thus this single translate is fixed by every numerical multiplier simultaneously. This argument assumes the multiplier assertion, not its converse.

The First Multiplier Theorem, in the planar abelian case, says that each prime divisor of \(q\) is such a multiplier. Here its coprimality hypothesis is satisfied because \(\gcd(q,v)=1\). This is an attributed theorem, not proved in this package.

## P4. Quotient occupancy equations

Let \(d\mid v\), \(h=v/d\), and let \(a_i\) count the elements of \(D\) in residue class \(i\pmod d\). Then \(\sum_i a_i=k\). Counting ordered differences in each residue class gives

\[
\sum_i a_i^2=q+h,\qquad
\sum_i a_i a_{i-r}=h\quad(1\le r<d),
\]

with indices modulo \(d\). For the zero class, the \(k\) diagonal pairs contribute zero and the \(h-1\) nonzero multiples of \(d\) contribute once each. For a nonzero class there are \(h\) nonzero residues and each occurs once. These are necessary equations, not sufficient conditions for a difference set in the original group.

Equivalently, if \(A(X)=\sum_{a\in D}X^a\), then in \(\mathbb Z[X]/(X^v-1)\),

\[
A(X)A(X^{-1})=q+\sum_{r=0}^{v-1}X^r.
\]

For every nontrivial \(v\)th root of unity \(\zeta\), this implies \(|A(\zeta)|^2=q\). This spectral identity alone does not supply a prime-power proof.

## P5. An elementary necessary norm restriction

Suppose \(q\equiv1\pmod3\), so \(3\mid v\), and apply P4 with \(d=3\). Write the three occupancies as \(a,b,c\). We have

\[
a+b+c=q+1,\quad a^2+b^2+c^2=q+v/3,\quad ab+bc+ca=v/3.
\]

Subtracting the last equation from the preceding one, and setting \(x=a-c\), \(y=b-c\), yields

\[
q=x^2-xy+y^2.
\]

Every prime \(p\equiv2\pmod3\) must therefore occur to an even exponent in \(q\). To check this without invoking algebraic number theory, first show that \(p\mid x^2-xy+y^2\) forces \(p\mid x,y\). For \(p=2\), inspection of the four pairs modulo 2 proves it. For odd \(p\equiv2\pmod3\), if \(y\not\equiv0\), the ratio \(t=x/y\) satisfies \(t^2-t+1=0\). Then \((-t)^3=1\) but \(-t\ne1\) since \(p\ne3\), contradicting that \(3\nmid p-1\). If \(y\equiv0\), also \(x\equiv0\). Dividing \(x,y\) by \(p\) divides the form by \(p^2\); repetition proves the even-valuation assertion.

In particular \(q\equiv10\pmod{12}\) is impossible: then \(q\equiv1\pmod3\), but \(v_2(q)=1\). Equivalently, no \(n\equiv11\pmod{12}\) is taut. This is weaker than the published even-order restrictions and is recorded as a self-contained reconstruction, not a new contribution. It excludes \(n=11\) using cyclic structure, even though Bruck-Ryser's sum-of-two-squares test alone allows \(q=10=1^2+3^2\).

## P6. Arithmetic orbit sizes used in the residual computation

Let \(M\le(\mathbb Z/v\mathbb Z)^\times\) be a known multiplier subgroup, with \(D\) normalized as in P3. For every divisor \(d\mid v\), the residues \(x\) with \(\gcd(x,v)=v/d\) number \(\varphi(d)\). Write \(x=(v/d)u\), where \(u\) is a unit modulo \(d\). Its orbit has length \(|M\bmod d|\), since \(tu=t'u\pmod d\) exactly when \(t=t'\pmod d\). Thus this stratum consists of \(\varphi(d)/|M\bmod d|\) orbits of that size. The divisor \(d=1\) accounts for \(\{0\}\).

Consequently \(k\) must be a bounded subset sum of these orbit lengths. Passing the subset sum condition does not test differences between or within selected orbits and does not establish existence. The computation uses exact integer arithmetic only.

## Published square descent used separately

Gordon (1994), Theorem 6, attributes the following to Jungnickel-Vedder: a planar difference set of square order \(q=m^2\) in an abelian group \(G\) implies a planar difference set of order \(m\) in a subgroup of \(G\). In the cyclic case the subgroup is cyclic. Therefore order \(2304=48^2\) is impossible: Wilbrink's necessary condition says an order divisible by 3 is either 3 or divisible by 9, whereas \(48\) is neither. This is an application of published theorems, not a reproduction of their proofs.

## Unresolved work

No argument here excludes every non-prime-power \(q\). No necessary condition is silently reversed. The finite range in the logs and the much larger published verification range are distinct. Every substantive inference above, and the hypotheses of each imported theorem, await two independent adversarial reviews; one review must reconstruct the complete partial package.
