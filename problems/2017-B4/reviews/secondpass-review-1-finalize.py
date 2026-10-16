#!/usr/bin/env python3
"""Freeze R1 evidence hashes; reads only explicitly named sources and own namespace."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
MANIFEST = HERE/"secondpass-review-1-manifest.json"

def record(p):
    raw = p.read_bytes()
    return {"path":str(p.relative_to(ROOT)),"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}

candidates = [
    ("problems/2017-B4/notes/secondpass-macmahon-candidate-v1.md","83f254ec69a31b5bf57dddd241bd0e29277300b4f1ba78dbf3c2c02191913ffe"),
    ("problems/2017-B4/notes/secondpass-boundary-fiber-candidate-v1.md","984ecfd11306304dd68310b0b20148577a7e8d43da6761a9bd570f95024cacbc"),
    ("problems/2017-B4/notes/secondpass-periodic-grid-candidate-v1.md","6e2a25e0bd94d230892c8c8eb31d931c4a09190826f1f210a97fcb207e852bd7"),
]
candidate_records = []
for name,expected in candidates:
    r = record(ROOT/name)
    assert r["sha256"] == expected, name
    candidate_records.append(r)

source_specs = [
    (".cache/official/2017-paper_b.pdf","https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf","p.2 B4"),
    (".cache/official/2017-solutions.pdf","https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf","p.12 B4 comments"),
    (".cache/literature/2017/cited-7f7251133b0c4ebc.pdf","https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf","Sections 1 and 4; equations 11-14"),
    (".cache/literature/2017/cited-b5bf6499a3fedd25.pdf","https://arxiv.org/pdf/2402.13107","v2: Sections 1,2,4,5.1; Appendix A"),
    (".cache/literature/2017/secondpass-review-1-felsner-weil.pdf","https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf","Theorems 7,8; Definition 1; proof of Theorem 7"),
]
sources = []
for name,url,sections in source_specs:
    sources.append(dict(record(ROOT/name),url=url,inspected=sections,redistribution_licence_verified=False,
                        full_file_ignored_cache_only=True,verification_date_local="2026-10-17"))

artifacts = [record(p) for p in sorted(HERE.glob("secondpass-review-1*"))
             if p.is_file() and p != MANIFEST]
job_names = ("algebra","fibers","fibers-v1-failed","grid","finite-grid")
jobs = [json.loads((HERE/("secondpass-review-1-"+j+"-job.json")).read_text()) for j in job_names]
assert all(j["status"] != "running" for j in jobs)
renders = json.loads((HERE/"secondpass-review-1-render-jobs.json").read_text())
assert all(j["status"] == "complete" for j in renders)

download = ["curl","-L","--fail","--silent","--show-error","--max-time","25",
            "https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf","-o",
            ".cache/literature/2017/secondpass-review-1-felsner-weil.pdf"]
manifest = {
    "completed_utc":datetime.now(timezone.utc).isoformat(),
    "reviewer":"R1 independent adversarial initial audit; full reconstruction",
    "other_reviewer_reports_or_conclusions_read":False,
    "shared_issue_or_status_logs_read":False,
    "requested_launch_settings":{"model":"gpt-6.1-sol","reasoning_effort":"max","launch_acceptance":"parent supplied"},
    "verified_effective_settings":None,
    "weekly_telemetry":{"authority":"mcp__codex_app__get_usage_limits","used_percent_observations":[7,8],
                        "window_duration_minutes":10080,"resets_at":1792745187,"cutoff_total_used_percent":90},
    "overall_verdict":"M1-M3/F1-F3/G1 supported on initial R1 audit; G2 author repair required before acceptance",
    "substantive_open_objections":[{"id":"R1-G2-01","packet_line":73,
        "description":"Uncovered fourfold crossings, e.g. (0,t) on the diamond boundary, remain nonsimple under the literal construction; require a fixed local resolution."}],
    "other_comments":["R1-F1-01: add Felsner-Weil Theorem 7 direct citation",
                      "R1-G1-01: use fixed minimal remainder strips or nonnegative superadditivity instead of unresolved original grid",
                      "M2: full ternary singleton trees have odd leaf count"],
    "candidate_records":candidate_records,"source_records":sources,
    "additional_primary_exposition":{"url":"https://jeffe.web.engr.illinois.edu/teaching/comptop/2023/notes/09-planar-graphs.html",
        "sections":"Planar maps; Rotation systems; designated outer face","retrieval":"web read only","local_hash":None},
    "new_source_retrieval_attempts":[{"argv":download,"sandbox":"default","exit_code":6,
        "stderr":"curl: (6) Could not resolve host: page.math.tu-berlin.de"},
        {"argv":download,"sandbox":"require_escalated","exit_code":0}],
    "source_extraction_limitation":{"tool":"pypdf.PdfReader(...).pages[14].extract_text()",
        "file":".cache/literature/2017/secondpass-review-1-felsner-weil.pdf",
        "exit_code":0,"result":"unreadable embedded-font glyph names; used bounded Poppler renders and visual inspection"},
    "jobs":jobs,"render_jobs":renders,"artifacts":artifacts,
    "candidate_files_unchanged":True,"candidate_statuses_promoted":False,
    "commits_or_pushes_performed":False,"separately_billed_api_used":False,
    "manifest_self_hash_excluded":True,
}
MANIFEST.write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps({"manifest":str(MANIFEST),"manifest_sha256":hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
                  "report_sha256":hashlib.sha256((HERE/"secondpass-review-1.md").read_bytes()).hexdigest(),
                  "artifacts":len(artifacts),"all_children_exited":True},indent=2))
