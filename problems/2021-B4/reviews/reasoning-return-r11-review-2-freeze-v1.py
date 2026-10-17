"""Administrative whole-initial freeze only; no mathematics or peer inspection."""
import hashlib,json
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[3]
P="problems/2021-B4/reviews/reasoning-return-r11-review-2-"
def record(path):
    p=Path(path)
    if not p.is_absolute(): p=ROOT/p
    b=p.read_bytes()
    return {"path":str(p.relative_to(ROOT)) if p.is_relative_to(ROOT) else str(p),
            "bytes":len(b),"sha256":hashlib.sha256(b).hexdigest()}
def check(row):
    got=record(row["path"])
    assert got["sha256"]==row["sha256"],row["path"]
    if "bytes" in row: assert got["bytes"]==row["bytes"],row["path"]
    return got
def write(suffix,obj):
    path=ROOT/(P+suffix)
    with path.open("x") as f: json.dump(obj,f,indent=2);f.write("\n")
    return record(path)
author_path="problems/2021-B4/notes/reasoning-return-r11-freeze-v1.json"
author=check({"path":author_path,"bytes":3477,
"sha256":"c0b3a0650274e899fb97f84ec042e1edb9d5e6db0f603c7f22ee5bd691e12ca4"})
packet=json.loads((ROOT/author_path).read_text())
rows=[author]+[check(r) for r in packet["artifacts"]]
validation=json.loads((ROOT/"problems/2021-B4/notes/reasoning-return-r11-input-validation-v1.json").read_text())
direct=[check(r) for r in validation["direct_inputs"]]
parents=[{"metadata":check(r["metadata"]),
          "historical_declared_occurrences_BOUND_NOT_FRESHLY_REEXPANDED":r["declared_fingerprint_occurrences_verified"]}
         for r in validation["immutable_parent_bindings"]]
rows+=direct+[r["metadata"] for r in parents]
unique={}
for r in rows:
    if r["path"] in unique: assert unique[r["path"]]==r
    unique[r["path"]]=r
integrity=write("integrity-v1.json",{
"verified_at_utc":datetime.now(timezone.utc).isoformat(),
"administrative_only":True,"whole_NEW_constructor_artifacts_verified":rows[:len(packet["artifacts"])+1],
"all_direct_inputs_verified":direct,"immutable_parent_metadata_verified":parents,
"fingerprint_occurrences_actually_verified":len(rows),"unique_paths_actually_verified":len(unique),
"historical_author_occurrences_bound_NOT_freshly_replayed":validation["fingerprint_occurrences_verified"],
"historical_author_unique_paths_bound_NOT_freshly_replayed":validation["unique_paths_verified"],
"no_NEW_peer_R11_metadata_findings_or_reports_read":True,
"new_math_code_CAS_scan_author_rerun_certificate_replay":False,
"command":".venv/bin/python "+P+"freeze-v1.py","exit_code":0})
payload=[record(P+s) for s in ["initial-v1.md","ledger-v1.md","source-audit-v1.md",
"worklog-v1.md","freeze-v1.py"]]+[integrity]
manifest=write("manifest-v1.json",{
"frozen_at_utc":datetime.now(timezone.utc).isoformat(),
"reviewer":"/root","constructor":"/root/review_2021_reasoning_j15_r2",
"status":"COMPLETE initially blind OTHER WHOLE audit; pending other whole initial/reconciliation",
"whole_obligations":56,"whole_checks":56,"substantive_objections":0,"required_repairs":0,
"all_new_math_hand_reconstructed":True,"ENTIRE_initial_before_ANY_peer_NEW_findings_metadata":True,
"old_roles_disclosed":["PN constructor","R5 strategy contributor","earlier accepted-input reviewer"],
"own_old_inputs_independently_recertified":False,"requested_settings":{"model":"gpt-6.1-sol","reasoning":"max"},
"effective_settings_readback":None,"candidate":rows[1],"constructor_manifest":author,
"fingerprint_occurrences_actually_verified":len(rows),"unique_paths_actually_verified":len(unique),
"no_math_program_CAS_scan_certificate_replay_or_author_rerun":True,
"budget_boundary":{"last_consistent_total_used_percent":65,"old_reset_unix":1792745187,
"conflicting_live_used_percent":0,"changed_live_reset_unix":1792874445,
"automatic_new_window_spending_authorized":False,"queued_NEW_work_held":True},
"artifacts":payload})
for r in payload:check(r)
print(json.dumps({"manifest":manifest,"artifacts":len(payload),
"fingerprint_occurrences_verified":len(rows),"unique_paths_verified":len(unique)},indent=2))
