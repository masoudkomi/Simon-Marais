# Independent fixed-trial integer certificate: derivation before execution

2026-10-17 UTC. This is a proof-critical finite arithmetic check for the
initially blind WHOLE R1 review. It is not a history/factor/count/automaton
enumeration, a new trial search, a constructor rerun, or a statement about
the full obstruction language. The reviewed word-set identities are
needed separately to identify the rational function with an actual subset.

Write a=1−2z^5−z^8, b=1−z². Combining the two removed prefixes by hand
gives

    G(z)=K(z)+z^12/a+z^12/b²,
    K=z^4−z^12+8z^19+20z^21+4z^22+40z^23+35z^24.

For E=1−48z/25+G−zG'/25, direct differentiation gives

    25E=A+z^12 C/a²+z^12 D/b³,
    A=25−48z+21z^4−13z^12+48z^19+80z^21
                      +12z^22+80z^23+35z^24,
    C=13−36z^5−21z^8,        D=13−17z².

Indeed 25z^12/a−z(z^12/a)'=z^12(13a+za')/a², and
25z^12/b²−z(z^12/b²)'=z^12(13b+2zb')/b³. These give exactly C,D.
Consequently the sign is the sign of the POLYNOMIAL

    a² b³ A + z^12 C b³ + z^12 D a².                 (I)

This is a different arithmetic certificate from the author's Fraction
evaluation of a rational function and its derivative. No Fraction,
symbolic differentiation or numerical root procedure is used below.

At the prescribed r=p/s, p=125000,s=220653, use homogeneous integer forms

    a_h=s^8−2p^5s³−p^8,      b_h=s²−p²,
    C_h=13s^8−36p^5s³−21p^8, D_h=13s²−17p²,
    A_h=25s^24−48ps^23+21p^4s^20−13p^12s^12
        +48p^19s^5+80p^21s³+12p^22s²+80p^23s+35p^24.

The degree46 homogenization of (I) is

    I_new=a_h² b_h³ A_h+p^12 C_h b_h³ s^20
                          +p^12 D_h a_h² s^16,
    E_G(r)=I_new/(25s^24 a_h² b_h³).                 (II)

For the OLD subset without the rigid tail, let

    A_old=25−48z+21z^4+22z^14+27z^16+28z^18+48z^19
                     +25z^20+80z^21+30z^22+80z^23+42z^24.

Its degree24 homogenization A_old,h gives the independent comparison

    I_old=a_h² A_old,h+p^12 C_h s^20,
    E_old(r)=I_old/(25s^24 a_h²).                   (III)

All denominator factors are positive: p,s>0; 5p=625000<3s=661959;
thus0<r<3/5, b>0 and 2r^5+r^8<2(3/5)^5+(3/5)^8<1.
The saved independent integer output evaluates (II)–(III) at THIS ONE
prescribed pair, records every integer and its reduced exact fraction,
and checks I_new<0<I_old. Its script reads no constructor input and
writes no file. A separate bounded parent records the one child PID,
explicit timeout, stdout/stderr, exit status and reaping. No additional
trial, derivative table, obstruction coefficient or language count is run.
