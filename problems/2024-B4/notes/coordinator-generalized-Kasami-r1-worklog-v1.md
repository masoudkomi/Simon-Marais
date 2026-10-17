# Generalized Kasami recurrence: reasoning and rejected routes

2026-10-17 UTC. Root constructor. Candidate proof — unverified. Requested gpt-6.1-sol/max for worker launches; no independent effective-setting readback is available. No mathematical computation or native CAS was run.

The complete CP1–CP3 packet had already passed two initially blind whole audits and root reconciliation. Its author explicitly left arbitrary-m/general-q composition unresolved. Root then followed the MCM/Dickson literature connection recorded separately, with coefficient fields visually checked. None of that paper's monodromy or factor theorems became a new input.

First attempted route: extrapolate an outer polynomial recurrence directly from the accepted r=2 four-term identity. This was insufficient: multiplication of existing exponents did not explain the index q^(2r+1)+1 and could introduce denominator or leading-cancellation errors. No guessed recurrence or finite test was retained as evidence.

The useful change was to adjoin A^(q+1)=a and B^(q+1)=a+1 at a transcendental a. The desired powers become exact dot products of v=(A,B) with odd Frobenius iterates. The identity v dot v^[1]=1 makes four neighboring pairings elementary. Their matrix determinant is c+1, nonzero as a rational function, where c=g_d(a²+a). This gives the exact relation v^[4]=A_q(c)v^[2]+B_q(c)v. Raising this relation to successive odd powers of Frobenius proves the displayed P_r recurrence for ALL indices, without searching a larger exponent table.

The following pitfalls were challenged in constructing the complete proof:

- The notation is not a Hermitian space over F_(q²); iterated Frobenius need not have order2. Every used pairing is computed explicitly.
- The (q+1)-st roots are auxiliary algebraic elements; each desired scalar is visibly a polynomial in the original transcendental a and independent of those choices.
- c+1 can vanish at finite points. The calculation first occurs in a function field, removes the denominator, and descends to a polynomial identity by injectivity. No finite point is excluded from the resulting polynomial statement.
- r=0 is n=1 and is only an initial value; CP1 is used at r>=1. q=2 gives only unit phi3. r=1 gives equality with unit cofactor. Genuine factors require q>=4 and r>=2.
- The second recurrence term has strictly smaller degree; its difference from the proposed leading degree is q^(2r)(q+1), so no unproved cancellation assumption remains.
- The whole-phi13 exclusion uses its exact accepted necessity, rather than merely an old sufficient progression. No claim about individual components follows.
- This construction supplies sufficient whole-divisor families. Other factors and a complete classification remain uncontrolled.

The source note, full candidate and inference obligations are frozen together with exact accepted inputs and earlier root records. Two OTHER nonconstructors must perform initially blind WHOLE audits. Root's own reconstruction here cannot count as one. No peer GK findings exist or were read during construction.

The only code in this packet is administrative fingerprint/freeze code. No q8/m2 calculation was run; n233017 is an elementary integer substitution in the formula. All existing author, review, source and acceptance bytes remain unchanged. No Git operation occurs in the freeze script, no separate API is used, and no charge, contact or access bypass occurred. Last worker account telemetry is31%TOTAL weekly used at10:48:51UTC, reset1792745187;90%TOTAL cutoff and integration reserve remain in force.
