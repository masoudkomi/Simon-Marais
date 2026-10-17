# A failed greedy rule for unmarked physical outputs

2026-10-17 UTC. **Failed argument / hand-checked observation, not an
accepted theorem.** Root. No exact growth, new bound or novelty claimed.
This concerns original unmarked outputs, unlike the earlier fixed-tape
greedy counterexample. It leaves the accepted language/overlap scopes
unchanged.

A proposed simplification was: when an odd output has a singleton1 run
at BOTH ends, remove the left1 and then the adjacent0 whenever available.
It would make a two-step canonical deletion choice. It is false.

Take z=0011110. The two balanced extensions have different memberships:

    10z=100011110 is admitted,
    z01=001111001 is not admitted.

The first is obtained by these legal additions, starting from1:

    1 -> 01 -> 011 -> 0011 -> 00111 -> 000111
      -> 0001111 -> 00011110 -> 100011110.

The added bits alternate0,1 and their ends are respectively
L,R,L,R,L,R,R,L. Thus membership is exhibited by an actual history,
not an equality of necessary bit counts.

For the second word, reverse deletion must first remove the FINAL1;
its first bit is0. This leaves00111100 and next requires0. Removing
the left0 leaves0111100, with BOTH ends0 while the next required bit
is1. Removing the right0 instead leaves0011110, again with BOTH ends0.
These are the only two possibilities. Both are dead, so no history exists.

Now take the original odd word

    w=10z01=10001111001.

It is admitted by applying the legal suffix operation S(v)=v01 to
the displayed admitted10z. Both outside1-runs of w are singletons.
Deleting the left10 leaves the rejected z01; deleting the right01
leaves the admitted10z. Thus even the extra singleton-end test does not
justify an arbitrary leftmost choice. This does not rule out a more
informed or longer-lookahead normal form.

The example also disproves the proposed equality of residual languages

    {z:10z is admitted} = {z:z01 is admitted}.

Reversal only exchanges these two residual languages after reversing z;
it does not prove their equality at the same z. It would be invalid to
close the overlap hierarchy by assuming this equality.

## Counterexample search and exact limits

A narrowly bounded exact search was used to FIND this possible
counterexample, then every membership/nonmembership above was checked
by hand. It started O={1}, used the four exact legal two-step maps
10v,1v0,0v1,v01 and compared the two residual sets. It stopped at k4,
original length9, on the first discrepancy. No asymptotic inference,
larger table, CAS or old certificate rerun was used. Executed command:

```text
.venv/bin/python -c 'O={"1"}
for k in range(9):
 L={w[2:] for w in O if w.startswith("10")}; R={w[:-2] for w in O if w.endswith("01")}
 if L!=R:
  z=min(L^R); print({"k":k,"z":z,"prefix_10_admitted":z in L,"suffix_01_admitted":z in R});break
 O={v for w in O for v in ("10"+w,"1"+w+"0","0"+w+"1",w+"01")}
else:print("no counterexample through length17; finite evidence only")'
```

Output: k4,z0011110,prefix_10_admittedTrue,suffix_01_admittedFalse.
The printed else branch was NOT executed. Minimality beyond this exact
search convention is not part of the mathematical observation.

A primary search also found Goldwurm-Wich *Unambiguous Turn Position*,
[author-repository search link](https://air.unimi.it/retrieve/dfa8b9a1-904f-748b-e053-3a05fe0a3a96/newklaus.pdf).
The direct retrieval returned403, so the paper's proof is UNREAD and no
theorem is imported. Search snippets about inherent ambiguity are not
evidence of that property for the present language. Earlier bounded
rational-relation and finite-fiber source limitations remain recorded
in the preceding follow-up. No purchase, contact or access bypass.
