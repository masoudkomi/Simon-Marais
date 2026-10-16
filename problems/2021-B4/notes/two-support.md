# Two lower-term compatibility calculation, V1, 2026-10-16

Status: **candidate proof - unverified**. This is a necessary-condition
derivation for a restricted family, not a classification of degrees. Related
two-support reductions are attributed in references.md to Marashdeh's 2026
preprint; novelty is not claimed.

Let f=x^d+A x^a+B x^b, where A B !=0 and 1<=a<b<=d-2, over characteristic
zero. Suppose it meets the shared-root conditions. Write

    C_a=binom(d,a), C_b=binom(d,b), C_ba=binom(b,a).

The condition H_b(f)(v)=f(v)=0 forces v!=0 and

    B=-C_b v^(d-b),    A=(C_b-1)v^(d-a).

Indeed, H_b(f)=C_b x^(d-b)+B, and substituting this into f(v)=0 gives the
second identity. Similarly H_a(f)(u)=f(u)=0 has u!=0. Setting t=u/v, the two
equations are

    t^(d-a)-C_b t^(b-a)+(C_b-1)=0,
    C_a t^(d-a)-C_b C_ba t^(b-a)+(C_b-1)=0.

Subtract C_a times the first from the second, then substitute back, obtaining

    t^(b-a)=R=(C_a-1)(C_b-1)/(C_b(C_a-C_ba)),
    t^(d-a)=S=(C_b-1)(C_ba-1)/(C_a-C_ba).

All displayed denominators are nonzero: C_a>C_ba>1 because d>b>a>=1. If
g=gcd(b-a,d-a), a necessary condition is R^((d-a)/g)=S^((b-a)/g). This is
necessary even when u,v are complex; no sign or rational-power sufficiency is
used. The accompanying script compares these two rational numbers exactly
for every exponent pair in d=20,24,28,30. It does not verify a theorem for
unbounded d or for four or more terms.

The centered form excludes exponent d-1; the root zero supplies every
derivative condition other than the two active exponents a,b. Thus the
displayed equations cover all active conditions in this restricted family.
