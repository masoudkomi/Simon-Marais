"""Create a complete versioned scope repair, preserving every v1 byte."""
from pathlib import Path
import hashlib
import difflib

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "problems/2017-B4/notes"
old_path = BASE / "rank-mesh-reasoning-r1-candidate-v1.md"
old_raw = old_path.read_bytes()
assert hashlib.sha256(old_raw).hexdigest() == "e0f2e55e62aabe5547120f4fc72c506c3f680844a90aa98ece7147d404178d27"
old = old_raw.decode()
new = old


def replace_once(before, after):
    global new
    assert new.count(before) == 1, before
    new = new.replace(before, after, 1)


replace_once(
    "2026-10-17 UTC. **Candidate proof - unverified.** Constructor",
    "2026-10-17 UTC, full author repair v1.1. **Candidate proof - unverified.** Constructor")
replace_once(
    "No mathematical computation, enumeration or CAS was used.\n",
    "No mathematical computation, enumeration or CAS was used.\n\n"
    "Version1.1 repairs RMR1-01/RM2-01 by restricting the auxiliary\n"
    "window estimate to one rectifiable Jordan boundary and recording the\n"
    "actual sum for multiple such windows. It also corrects N1's general-D\n"
    "tile alphabet. No other result or new extension is introduced. The\n"
    "complete v1 and unchanged UR3 supplement remain frozen; both affected\n"
    "independent reaudits and coordinator resolution are still required.\n")
replace_once("the six finite tile types", "the binom(D,2) finite tile types")
replace_once(
    "If a rectifiable window has perimeter O(L), discard faces touching its\n"
    "boundary before using interior good disks. Their diameter bound places\n"
    "all their tiles in an O_D(r)-tube of that boundary. Finite integer tile\n"
    "origins bound the additional loss by O_D(rL+r^2). At fixed r this is\n"
    "lower order than L^2. No assertion that an unbounded number of repeated\n"
    "physical windows can be paid for with this same one-window bound is made.\n",
    "For this auxiliary estimate, a window W must be the bounded interior\n"
    "of one rectifiable Jordan curve, with boundary length P. Discard every\n"
    "selected face whose closure meets that boundary before using interior\n"
    "good disks. The diameter bound places all tiles of those faces in the\n"
    "O_D(r)-tube of this one curve. This tube has area O_D(rP+r^2):\n"
    "sample its arclength parametrization at spacing at most rho=C_D r;\n"
    "at most ceil(P/rho)+1 disks of radius2rho cover its rho-tube.\n"
    "Every original tile has area at least1 and the tiling interiors are\n"
    "disjoint, so the additional whole-tile loss is O_D(rP+r^2).\n"
    "Consequently P=O(L) gives O_D(rL+r^2), lower order than L^2\n"
    "when r is fixed and L tends to infinity.\n\n"
    "This is a one-Jordan-boundary estimate. It is not asserted for an\n"
    "arbitrary connected region with rectifiable boundary and many tiny\n"
    "holes. For an actual finite collection W_1,...,W_M of such Jordan\n"
    "windows, each with perimeter P_j, charge each application separately:\n"
    "the safe total upper loss is O_D(r sum_j P_j+M r^2), with any\n"
    "overlap only reducing the union. It is lower order only under the\n"
    "actual chosen scales and this summed bound. No unbounded collection\n"
    "is paid for by a single O_D(rL+r^2) allowance.\n")
replace_once(
    "Work with an interior F; outer-boundary\n"
    "faces may be discarded at the O_D(rL+r^2) cost above.\n",
    "Work with an interior F. The full outer zonogon boundary is one\n"
    "rectifiable Jordan polygon of perimeter O_D,c(L), so its touching\n"
    "faces may be discarded at the O_D,c(rL+r^2) cost just proved.\n")
replace_once(
    "The local mask-boundary cost must be summed over the actual\n"
    "chosen windows before taking limits.",
    "The local mask-boundary helper applies only to the stated Jordan\n"
    "windows. Its r*sum P_j+M*r^2 cost must be summed over the actual\n"
    "chosen windows before taking limits.")
out_path = BASE / "rank-mesh-reasoning-r1-candidate-v1.1.md"
with out_path.open("x") as out:
    out.write(new)
patch = "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                   fromfile=old_path.name, tofile=out_path.name))
with (BASE / "rank-mesh-reasoning-r1-diff-v1.1.patch").open("x") as out:
    out.write(patch)
assert old_path.read_bytes() == old_raw
print("Full v1.1 and exact diff created; old v1 unchanged.")
