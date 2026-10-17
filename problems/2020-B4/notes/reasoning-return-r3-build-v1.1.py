"""Create a full fixed-subgroup quantifier repair without changing v1."""
from pathlib import Path
import hashlib
import difflib

ROOT=Path(__file__).resolve().parents[3]
B=ROOT/"problems/2020-B4/notes"
old_path=B/"reasoning-return-r3-candidate-v1.md"
raw=old_path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="2cb5803b20cdcc96961956773f02a3fe2e00f0ae9a4bee8df56af0ec2cd86796"
old=raw.decode()
new=old


def replace(before,after):
    global new
    assert new.count(before)==1,before
    new=new.replace(before,after,1)


replace("2026-10-17 UTC. **Candidate proof - unverified.** Constructor",
        "2026-10-17 UTC, full author repair v1.1. **Candidate proof - unverified.** Constructor")
replace("is claimed.\n\nOnly B4(b)",
        "is claimed.\n\nVersion1.1 repairs2020R2-01: the prime-order orbit congruence uses\n"
        "the fixed subgroup of that single element, with explicit h_t,f_t,m_t,\n"
        "rather than the common fixed subgroup of a larger T. The full exact\n"
        "counterexample and all downstream checks are in the new repair ledger.\n"
        "All v1 and both initial audit bytes remain frozen; both affected\n"
        "reaudits and coordinator resolution are required. No other theorem\n"
        "or extension is introduced.\n\nOnly B4(b)")
replace(
    "If t has prime order ell as an automorphism of G, every nonfixed orbit\n"
    "on D has size ell. Hence, when h>1,\n\n"
    "    q-m is divisible by ell.                            (F4)\n\n"
    "When h=1, q+1 is congruent to f in{0,1} modulo ell. The same singleton\n"
    "0 must be used consistently for different subgroups; its membership is\n"
    "not a new independent choice for each projection.\n",
    "For the following prime-order conclusion, let t be a known multiplier\n"
    "of prime order ell and define its OWN fixed subgroup and intersection:\n\n"
    "    H_t=G^<t>, h_t=|H_t|, E_t=D intersect H_t, f_t=|E_t|.\n\n"
    "Apply F1 specifically to T=<t>. If h_t>1, set m_t=f_t-1,\n"
    "so h_t=m_t^2+m_t+1. Every t-orbit on D has length1 or ell,\n"
    "and its length1 points are precisely E_t. Therefore\n\n"
    "    q-m_t is divisible by ell when h_t>1.               (F4)\n\n"
    "When h_t=1, q+1 is congruent to f_t in{0,1} modulo ell,\n"
    "where f_t is1 exactly when0 belongs to D. The same actual singleton\n"
    "membership is retained for every such element. These h_t,f_t,m_t\n"
    "refer only to <t>. If <t> is contained in a larger chosen T, its\n"
    "common fixed subgroup H=G^T may be strictly smaller and must NOT\n"
    "be substituted into this orbit congruence. No prime-order congruence\n"
    "for |D^T| is asserted merely from the existence of t in T.\n")
replace("Use the known multiplier p. Its fixed subgroup has size",
        "Use the known multiplier p and apply F1 with T=<p>; its\norder need not be prime. Its own fixed subgroup has size")
replace("Apply F1 to B: f=|D intersect B|=s+1 and",
        "Apply F1 with T=<t> to B: f=|D intersect B|=s+1 and")
replace("have a difference in B, whose unique difference representation must\nbe between fixed points by F1.",
        "have a difference in B, whose unique difference representation must\nbe between points fixed by this involution, by F1 with T=<t>.")
replace("Applying them\nrecursively to E is legitimate only because E is a genuine subset with\nthe full unique-difference property; a homomorphic image of D does not\nhave this property in general.",
        "Applying these\nstructural statements recursively to E requires resetting every\nhypothesis in its group H, including the actual restricted multiplier\norder and that element's own fixed subgroup. E is a genuine subset\nwith the full unique-difference property; a homomorphic image of D\ndoes not have this property in general.")
out_path=B/"reasoning-return-r3-candidate-v1.1.md"
with out_path.open("x") as out:
    out.write(new)
with (B/"reasoning-return-r3-diff-v1.1.patch").open("x") as out:
    out.write("".join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=old_path.name,tofile=out_path.name)))
assert old_path.read_bytes()==raw
print("Complete v1.1 and exact diff created; original v1 unchanged.")
