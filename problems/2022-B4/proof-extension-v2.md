# 2022 B4(b): density-one extension, version 2

**candidate proof - unverified**, 2026-10-16. This is a partial theorem,
not a solution of the official universal question. It extends P2 of
proof.md; that strip-only version is preserved. No independent review has
yet been completed. Novelty is not established.

## Claim and dependencies

For **every fixed integer** \(d\), the positive starts
\((a_0,b_0)=(b+d,b)\) satisfying the official product condition that ever
reach equality have natural density 1 as \(b\to\infty\).

Use the exact quotient formulas, common-shift identity, finite lifting
bijection, and finite counting-to-density argument P1-P2 in proof.md.
The extension below supplies an abstract equality path for every integer
difference, so it does **not** need the established preliminary trapping
result. Choosing abstract quotient controls is part of the equality
investigation; it is not a claim that the actual controls of an individual
integer orbit follow those choices.

## Analytic abstract control for arbitrary difference

At any state \((d,r)\), the next difference \(h=D(d,r)\) is fixed.
If \(h=0\), stop. Otherwise choose the next residue in the same intervals
as in P2. The available next residues cover the required class modulo 6,
so the indicated choice always exists.

If \(h>0\), choose \(s\in[30,35]\cap\mathbb Z\). Then
\[
D(h,s)=h+2-3\left\lfloor\frac{s+h}{30}\right\rfloor\le h-1.
\]
For \(h=1\) this is exactly 0. For \(h\ge2\),
\[
D(h,s)\ge h+2-\frac{s+h}{10}
\ge 0.9h-1.5>0.
\]
Thus a positive difference stays nonnegative and strictly decreases.

If \(h=-k<0\), choose \(s\in[20,25]\cap\mathbb Z\). Since
\(s-k<30\),
\[
D(-k,s)=-k+2-3\left\lfloor\frac{s-k}{30}\right\rfloor\ge-k+2.
\]
For \(k=1,2,3\), the respective values are 1,0,-1, since
\(s-k\in[17,24]\). For \(k\ge4\), using \(\lfloor x\rfloor>x-1\),
\[
D(-k,s)<-k+5-\frac{s-k}{10}
\le-0.9k+3<0.
\]
It therefore stays negative until it reaches -2 or -1, at which time
it maps to 0 or 1. The positive rule then maps 1 to 0.

Starting from a positive \(h\), at most \(h\) further steps are needed.
Starting from \(-k\), at most \(\lceil k/2\rceil+1\) further steps
are needed. For fixed initial \(d\), there are only 60 possible initial
residues \(r\), hence a finite common path bound is
\[
K(d)=1+\max_{0\le r<60} L(D(d,r)),
\quad
L(h)=
\begin{cases}
h,&h>0,\\
0,&h=0,\\
\lceil -h/2\rceil+1,&h<0.
\end{cases}
\]
This is an analytic bound defined by a finite maximum, not a result of a
computational search. When \(d=0\), equality already holds at time 0.

## Density conclusion

Apply P1's finite lifting bijection with this fixed finite \(K(d)\).
For each surviving prefix, at least one length-\(K(d)\) extension hits
equality. The density of starts surviving \(tK(d)\) steps is at most
\((1-10^{-K(d)})^t\). The upper natural density of never-hit starts is
therefore 0, by exactly the periodic-class counting argument in P2.
Positivity and the product condition exclude only finitely many values
of \(b\) on a fixed line, so do not change this conclusion.

## Remaining gap and required review

A density-zero subset of the positive integers need not be empty. The
proof does not control an individual exceptional control sequence. It
does not establish a two-dimensional density result when \(d\) varies
with \(b\), nor a universal positive answer to B4(b).

Two independent adversarial audits are required before promotion, one
reconstructing the full lifting and density argument. Particular checks:
the bounds at \(h=1,2\) and \(k=1,2,3,4\), finite controls versus actual
orbits, the exact modulus in the lifting bijection, and the passage from
finite periodic sets to upper natural density. Computations in the
directory are evidence only and are not premises of this proof.
