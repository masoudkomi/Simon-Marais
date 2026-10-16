# Reviewed degree-20 rational witness-count restriction

**Proved, independently reviewed (partial result)**, 2026-10-16 UTC.
This register accepts the unchanged complete argument in the
[frozen v1 proof](coordinator-three-rational-witnesses-v1.md). Its original
candidate label is historical. See [acceptance](../reviews/three-witness-acceptance.md)
and both independent full audits for the subsequent decision.

T1: a nontrivial degree-20 polynomial over Q satisfying the contest's
rational common-root condition needs at least four distinct rational
roots to cover all derivative witnesses. Its other roots need not be rational.

T2: in the specified 19-adic normalization, J=16 forces a double root
at 0 and precisely four distinct rational roots {0,1,u,v}. Every one is
needed. Removing x^2(x-1)(x-u)(x-v) leaves a degree-15 rational quotient
which is Eisenstein at 19.

T3: J=15 forces multiplicity 2 or 3 at 0. If it is 3, the corresponding
four-root statement holds and the residual degree-14 quotient is
Eisenstein at 19. The multiplicity-2 case has no such quotient conclusion.

Both fresh reviewers reconstructed the whole argument and independently
regenerated all 1,493,024 integer polynomial pairs and verified every
finite-field certificate, including the separately resolved modulo-131
case. Their different ordinary-Hasse constructions did not import the
constructor's helpers. Both independently derived the 772 necessary
masks, checked uniqueness and coverage, and verified all saved streams.
No substantive repair was requested.

This uses the separately reviewed normalization, Newton and degeneration
inputs. It solves no full degree or the annual classification. Massri v6,
Theorem 7.10, previously claimed a stronger complex-witness exclusion;
this rational reproduction establishes no novelty and does not validate
that paper's separate computational proof. A proposed extension to all
complex witnesses is a distinct unverified packet.
