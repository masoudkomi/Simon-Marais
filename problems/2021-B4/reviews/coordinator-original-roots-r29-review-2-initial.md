# R29 OTHER initially blind WHOLE2: complete initial audit

19 October 2026 UTC. Reviewer B, `/root/review_2022_complexity_r2`.
**Sealed independent initial report; coordinator promotion required.** Only
official 2021 B4(b). Requested inherited `gpt-6.1-sol`/`max`; independent
effective backend readback unavailable. Root constructed NEW R29 and is
excluded. I did not construct R29. My earlier R24/R26/R27/R28 review roles
are accepted-input history, not a fresh independent recertification of my
old reports or of the older foundational chain.

## Disposition and exact audited scope

All sixteen obligations pass in the printed domain. I found no substantive
defect or required repair. Ten closed scope/provenance notes appear below.
The conclusion excludes **the ENTIRE retained actual R28 negative-frame
domain**. It establishes neither all frame III nor all degree twenty nor
the annual answer. In particular, the proof does not assert that a formal
interpolation family supplies actual common rational roots.

I read the author freeze FIRST, followed by all five complete payloads:
main, sources JSON including complete exploratory script/output, standalone
certificate code, documentary admin code, and baseline. Author executables
were read and NEVER executed. I freshly read the COMPLETE current accepted
R24/R26/R28 bodies and EACH acceptance MD/JSON, the local official statement
and the operative official PDF wording. Their exact necessary identities
are guarded once in my baseline. No corresponding NEW R29 peer finding,
file, actual inventory, hash, metadata or commentary was accessed. No R30
material was sought or read. The one compact OWN parent is my immutable
R28 WHOLE2 manifest; its historical inventories are not recursively copied.

## Whole hand reconstruction

**1. Actual domain and clocks.** The printed hypotheses retain rational
monic degree twenty, actual rational root VALUES (0,1,r,s), respective
multiplicities (2,1,1,2), the actual irreducible rational degree-fourteen
carrier and the entire stated R18(S),(W), adjacent-m4, J15 and oriented
frame-III interfaces. All original nineteen-adic/common-value/center
conditions remain hypotheses. Other roots may be nonrational or nonreal;
each derivative order can have a different rational common value. None of
those official or branch hypotheses is replaced by a local interpolation
solution.

The exact accepted normalization is (h=1/r=4H), (H) odd in
ℚ_(2), (S=s/r) odd, (S≠1), with finite (v_2(S-1)≥2), and
EXACT (A_9=A_{10}=0). For (F(Z)=r^{-20}f(rZ)), the two original
root equations are

\[
F(1)=r^{-20}f(r)=0,\qquad F(h)=r^{-20}f(1)=0.
\]

Here normalized (1) corresponds to original (r), whereas normalized
(h) corresponds to original (1). These are not derivative-witness
equations. Distinct actual root values give (r≠0,1), so rational
(h≠0,1). Scaling preserves monicity and the binomial coefficient
normalization (F(Z)=Σ_i\binom{20}{i}A_i Z^{20-i}).

**2. No free coefficient is lost.** R24 supplies

\[
\begin{split}
A_0&=1,\quad A_1=-h,\quad A_2=A_4=A_5=0,\\
A_3&=2h^3,\quad A_6=-35h^6,\\
A_7&=-1+7h-70h^3+245h^6,\\
A_8&=7-48h+448h^3-980h^6+b,\\
A_9&=-28+189h-1680h^3+2940h^6-9b+c,\\
A_{10}&=84-560h+4800h^3-7350h^6+45b-10c+k.
\end{split}
\]

Thus (A_9=0) forces (c=c_0+9b), with the printed (c_0).
Substituting this into (A_{10}=0) gives (k=k_0+45b): the coefficient
is (-45+10·9=45). Neither (c), (k) nor (b) is set to zero
without justification. The final (A_{19}=A_{20}=0) are the fixed actual
coefficients of the accepted family, not a later homothetic adjustment.

For every j=11,…,18, the actual witness equation is

\[
A_j=-\sum_{i<j}\binom ji A_i z_j^{j-i},\quad
(z_{11},\ldots,z_{18})=(h,h,h,1,h,1,h,1).
\]

This is a triangular recurrence with coefficient one on (A_j). It
introduces no denominator or alternative branch. Low coefficients are
affine in (b) over ℤ[h]; the recurrence preserves this. Consequently
(A_i=a_i+b d_i), with (d_8=1) and other low (d_i=0), and separate
recurrences compute precisely the two affine parts. All high centers,
including the final center (z_{18}=1), are retained.

**3. Elimination without division.** Evaluating the same full polynomial
at normalized (1,h) yields exactly

\[
Q_0+bQ_1=0,\qquad R_0+bR_1=0,
\]

with the printed binomial sums, including all indices 0 through 18.
Indices 19 and 20 vanish by their fixed values. Multiply the second
equation by (Q_1), the first by (R_1), and subtract. The result is
(N=R_0Q_1-R_1Q_0=0). No (Q_1), (R_1), (b), (c) or (k)
is divided out. Thus (b=0), a zero coefficient of (b), and simultaneous
zero coefficients are all covered. The proof needs only this necessary
implication; it does not claim the determinant condition is sufficient.

**4. Independent exact finite certificate.** I designed ONE new
standard-library verifier, saved in `review-2-checker-v1.py`. It uses sparse
bivariate Fraction polynomials in (h,b), not the author's integer-pair
arrays, and uses (C_i=A_i/i!). The equivalent recurrence is

\[
C_j=-\sum_{i<j}C_i z_j^{j-i}/(j-i)!.
\]

It reconstructs (F(1)) and (F(h)) as (20!Σ C_i/(20-i)!),
shifting the latter by the appropriate powers of (h). It asserts there
are only (b)-degrees 0 and 1 and that the resulting four polynomials
have integer coefficients. Generic exact polynomial long division by
(125970(h^3-h^2)) produces zero remainder, an integer degree-26 (T),
and verifies the identity again coefficientwise. The independently found
degrees are (17,9,20,12,29,26) for (Q_0,Q_1,R_0,R_1,N,T).

The complete reconstructed integer coefficient lists, exact zero remainder,
all 27 coefficient residues and all 29 values are preserved in my
certificate JSON. Only AFTER reconstruction did the checker read the
author's declared JSON DATA and compare the seven complete coefficient/
value arrays. It executes no author script and imports no old checker.
All seven comparisons pass. The modular evaluations use direct power
sums, independently of the author's Horner evaluation. The leading residue
is 24 and the complete value row is

    [23,12,22,12,10,20,21,17,21,25,11,9,23,20,13,13,3,1,14,12,28,11,19,3,16,24,7,26,28].

Every value is nonzero. This is a finite proof-critical certificate, not
evidence from an unbounded experiment. I ran only this fixed-29 certificate
once. Child PID 84239 was monitored by an external 15-second timeout,
exited zero and was reaped. Complete code, command, dependencies, stdout,
stderr checkpoints, start/end and exit records are saved. No prime/depth/
height search, black-box irreducibility, author/source/helper replay or
routine mathematical test was run.

**5. Unrestricted rational denominator argument.** The prime 29 has no
divisor 2, 3 or 5 and √29<6. Suppose (T(u/v)=0) with coprime integers
(u,v), (v>0). Clearing (v^{26}), if (29\mid v), every lower
coefficient term vanishes modulo 29, leaving (24u^{26}≠0). If
(29\nmid v), reduction gives a zero at one of the 29 fully exhausted
residues, also impossible. Zero and negative numerators, arbitrary heights
and arbitrary powers of 29 in the denominator are covered. The nonzero
leading coefficient is essential to the nonunit-denominator case; merely
listing finite field values would not suffice.

Finally (N(h)=125970h^2(h-1)T(h)=0) and (h≠0,1) force (T(h)=0)
OVER ℚ, contradiction. The exact nonzero scalar and excluded factors
are divided over ℚ, never cancelled modulo 29. In particular rational
(h) reducing to 0 or 1 modulo 29 is still covered by the complete (T)
value row. No Taylor truncation, bound on (t), S-cover, (b≠0) or
larger modulus is used. The actual branch is empty; no remaining pattern
outside its printed hypotheses is thereby excluded.

## ALL16 separate obligation dispositions

|Review ID|Constructor ID|Outcome and independently reconstructed reason|
|---|---|---|
|R29R2-01|R29-01|PASS. Only official(b); retain ENTIRE actual branch and original rational-value wording, never assume its formal family is realizable.|
|R29R2-02|R29-02|PASS. Fresh complete R24/R26 interfaces give EXACT A9/A10zero; A19/A20 remain fixed zero throughout both evaluations.|
|R29R2-03|R29-03|PASS. Solve A9/A10 for c and k; k coefficient45 checked by substitution. Arbitrary b, including0, remains.|
|R29R2-04|R29-04|PASS. All eight centers checked; coefficient-one triangular recurrence preserves affine integer a/d parts. Independent factorial reconstruction agrees.|
|R29R2-05|R29-05|PASS. F(1)=f(r)/r20 and F(h)=f(1)/r20 are actual distinct ORIGINAL roots; h=1/r not an assumed new witness.|
|R29R2-06|R29-06|PASS. Direct cross-multiplication gives the printed determinant sign with no division, including simultaneous zero coefficients. No converse is needed.|
|R29R2-07|R29-07|PASS. Fresh exact long division/reconstruction proves all integer coefficients of N=125970h²(h−1)T, degrees29/26, zero remainder.|
|R29R2-08|R29-08|PASS. Independently reconstructed all27 residues match; leading24 is nonzero modulo29. Integer T, not merely a modular surrogate, is used.|
|R29R2-09|R29-09|PASS. Fixed direct-power evaluations at all29 residues, including0,1,28, reproduce the complete nonzero row.|
|R29R2-10|R29-10|PASS. Clearing v26 before reduction handles 29-divisible denominators of every order; coprimality gives u a29-unit.|
|R29R2-11|R29-11|PASS. Other rational denominators invert modulo29; all signs/heights map into exhausted field, with no height bound.|
|R29R2-12|R29-12|PASS. Actual r distinct0,1 makes h distinct0,1; division is inQ before any modular argument. No missed modular0/1 branch.|
|R29R2-13|R29-13|PASS. Full printed branch only. No fullframeIII/degree20/annual/priority conclusion; stronger formal family consequences are not silently promoted.|
|R29R2-14|R29-14|PASS. All author source/code/output/provenance read, never executed. Own new finite child saved in full, external timeout/PID/exit0/reaped; no routine search.|
|R29R2-15|R29-15|PASS. Old review roles/source limits explicit; fresh accepted bodies/EACHauthority/official operative wording read; no new external theorem or foundational recertification claimed.|
|R29R2-16|R29-16|PASS with handoff gate. Initial sealed before peer access; full final all5payload MODEL readbacks then manifest MODEL readback and separate readonly verification required before ADMIN handoff. Reserve/current-window stop retained.|

## Issue ledger: zero substantive defects, ten closed notes

1. **C1, scope.** The rational degree-fourteen carrier and all actual
   branch/witness hypotheses remain. The new eliminant does not derive
   them or exclude other center arrangements. Closed, no repair.
2. **C2, root clock.** F(h) uses original root 1, not a derivative's common
   rational value or normalized root S. Closed by exact substitution.
3. **C3, missing-coefficient challenge.** c/k are determined affine
   functions; A19/A20 fixed zero enter BOTH evaluations. Closed by the
   low-row substitution and full 21-index reconstruction.
4. **C4, determinant degeneracy.** No division by either b-coefficient;
   simultaneous zero and b0 cases survive elimination. Closed.
5. **C5, necessary versus sufficient.** N0 is only necessary. Its
   impossibility suffices; no lifting or converse is claimed. Closed.
6. **C6, rational reduction.** A finite root-free row alone could miss
   denominator29. Leading24 closes this case separately. Closed.
7. **C7, removed factors.** h0,h1 are genuinely excluded OVERQ. Their
   modular residues remain in the tested T row; no illicit cancellation.
   Closed. Extending the conclusion to those formal endpoints is invalid.
8. **C8, certificate independence.** Own bivariate factorial/Fraction and
   direct-power algorithm reconstructs before declared-data comparison;
   only one fixed finite execution, no old/author code replay. Closed.
9. **C9, source-process history.** The source exploration record retains
   a literal intermediate `status: running` field alongside the complete
   final exit0/reaped/finish record. I interpret those fields as a saved
   incremental history, not proof of a still-running job or a mathematical
   defect. No author repair required. Failed prime23 is historical data,
   not a new necessary reviewer test; later primes were unattempted.
10. **C10, source and independence limits.** Fresh accepted interfaces and
    operative official wording only; no fresh original Casas--Alvero or
    degree-twenty/R18 foundational proof certification. NEW peer remained
    unopened/uninventoried/unhashed; no broader priority claim. Closed.

## Source checks, failures, worklog and preservation

Sources JSON records literal scopes. The original official PDF at
https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf
was freshly opened for setup lines67--76 and open(b)81. Incidental
preliminary/neighbor visibility is not research or reproduction of part(a).
No new external mathematical theorem is used: finite polynomial arithmetic,
field reduction and coprime denominator reasoning suffice once the accepted
actual interpolation interface is retained. Historical external references
inside those accepted bodies were read as attributed context; their entire
original proofs were not freshly re-audited or downloaded.

Counterexample attempts targeted h0/h1, zero and simultaneous zero affine
coefficients, b0, fixed final coefficients, roots reducing0/1 modulo29,
nonunit denominators, and an unjustified sufficiency/lifting converse.
The first pair of formal endpoints shows why the h exclusions are needed;
the remaining cases are handled above. F(1) alone leaves an affine curve
and cannot yield the two-equation obstruction. No untested prime, generic
formal realization, local lift or root-free ordinary polynomial theorem
was inserted. No unresolved substantive issue remains in this scoped proof.

Worklog: author freeze first and all payloads/source code read; all operative
accepted body/authority/official reads completed, with clipped tool output
recovered in exact subsequent ranges; no clipped range treated as read.
Own one fixed child ran04:24:46UTC/PID84239/15s external timeout/exit0/reaped.
Documentary preparation then bound eighteen necessary paths exactly once.
Fresh authoritative account telemetry began87%TOTAL at04:20:27UTC and was
88% at04:25:08UTC, reset1792874445,10080min,ordinaryAllowedtrue,legacy and
by-limit agreeing, account…ac3a. No later window or separately billed API
is authorized; immediate checkpoint at89 and hard90 including reserve.

Only this NEW review prefix was written. All author, accepted, old review,
shared, cache and Git bytes remain untouched. A single exact OWN R28
manifest is the outerguard; no mutable map guards or historical inventory
recursion. Documentary modes read metadata only and do not rerun the
certificate. Final payload MODEL readbacks, then manifest MODEL readback,
then a SEPARATE readonly verification gate the sealed ADMIN handoff.
Any substantive future objection requires a versioned AUTHOR repair and
BOTH affected reaudits. Coordinator alone may promote after both complete
initials and reconciliation.
