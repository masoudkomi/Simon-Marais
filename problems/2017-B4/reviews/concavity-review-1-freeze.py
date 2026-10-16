#!/usr/bin/env python3
"""Freeze the completed blind review; reads only named files, never peer review."""
from pathlib import Path
import datetime
import hashlib
import json
import platform
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()


def fingerprint(path):
    p=ROOT/path
    return {"path":path,"bytes":p.stat().st_size,
            "sha256":hashlib.sha256(p.read_bytes()).hexdigest()}


sources=[
    (".cache/official/2017-paper_b.pdf",
     "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf",
     "PDF p. 2, B4 only", "official domains and conclusion"),
    (".cache/official/2017-solutions.pdf",
     "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf",
     "PDF p. 12, text and full-page visual inspection", "official intended counting convention"),
    (".cache/literature/2017/cited-7f7251133b0c4ebc.pdf",
     "https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf",
     "PDF pp. 1-4 and 7-10, with visual inspection of pp. 2-3",
     "marked dictionary, canonical labels, insertion recurrence, tree/transversal lemmas"),
    (".cache/literature/deep-literature-r2/2017-dallant-zone-2502.20909v2.pdf",
     "https://arxiv.org/pdf/2502.20909v2",
     "PDF pp. 1-7, Section 2 and Lemmas 3-7; visual inspection of p. 5",
     "simple marked hypotheses, extended cutpath bound, zone theorem, exact integer domain"),
]
ledger={"verified_utc":NOW,"retrieval":"reused existing ignored local caches; primary URLs opened read-only",
        "full_source_papers_copied_into_review":False,
        "redistribution_licence_verified":False,
        "sources":[dict(fingerprint(p),url=u,inspected=s,role=r) for p,u,s,r in sources],
        "python":sys.version,"platform":platform.platform(),
        "dependencies":"Python standard library fractions, math, hashlib, json, subprocess; pypdf for source inspection; bundled pdftoppm for rendering",
        "requested_model":"gpt-6.1-sol","requested_reasoning":"max",
        "effective_setting_readback":"unavailable",
        "usage":{"authority":"mcp__codex_app__get_usage_limits","used_percent":15,
                 "window_duration_mins":10080,"reset_unix":1792745187,
                 "stop_total_used_percent":90},
        "source_visual_commands":[
          "pdftoppm -f 5 -l 5 -scale-to 1500 -singlefile -png .cache/literature/deep-literature-r2/2017-dallant-zone-2502.20909v2.pdf /private/tmp/concavity-review-1-dallant-p5",
          "pdftoppm -f 2 -l 3 -scale-to 1500 -png .cache/literature/2017/cited-7f7251133b0c4ebc.pdf /private/tmp/concavity-review-1-fv",
          "pdftoppm -f 12 -l 12 -scale-to 1500 -singlefile -png .cache/official/2017-solutions.pdf /private/tmp/concavity-review-1-official-p12"
        ],
        "frozen_constructor_endpoint_comparison":{
            "method":"independently reconstructed Fraction atanh sums N=80 and compared exact endpoints read from the frozen certificate JSON",
            "result":"All five frozen constructor logarithm intervals equal independently reconstructed exact endpoints.",
            "constructor_script_executed":False,
            "independent_mercator_certificate_ran_before_constructor_script_read":True
        }}
(HERE/"concavity-review-1-sources.json").write_text(json.dumps(ledger,indent=2)+"\n")
construction_path="problems/2017-B4/notes/deep-literature-r2-concavity-freeze-v1.json"
construction=json.loads((ROOT/construction_path).read_text())
checked=[]
for original in construction["artifacts"]:
    current=fingerprint(original["path"])
    assert current["sha256"]==original["sha256"] and current["bytes"]==original["bytes"]
    checked.append(dict(current,matches=True))
names=["concavity-review-1.md","concavity-review-1-issues.md",
       "concavity-review-1-check.py","concavity-review-1-run.py",
       "concavity-review-1-certificate.json","concavity-review-1-job.json",
       "concavity-review-1-stdout.log","concavity-review-1-stderr.log",
       "concavity-review-1-sources.json","concavity-review-1-freeze.py"]
manifest={"status":"initial blind whole-argument audit and complete issue log frozen",
          "frozen_utc":NOW,"candidate_status":"candidate proof - unverified; coordinator promotion only",
          "reviewer":"review_2017_concavity_r1",
          "peer_concavity_review_files_or_conclusions_seen":False,
          "constructed_candidate":False,"spawned_agents":False,
          "requested_model":"gpt-6.1-sol","requested_reasoning":"max",
          "effective_setting_readback":"unavailable",
          "initial_disposition":"C1 survives this audit; no open substantive objection; one nonblocking n=1 scope clarification",
          "construction_freeze":fingerprint(construction_path),
          "all_six_construction_artifacts_unchanged":checked,
          "artifacts":[fingerprint("problems/2017-B4/reviews/"+n) for n in names]}
(HERE/"concavity-review-1-manifest-initial.json").write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps({"initial_report_sha256":manifest["artifacts"][0]["sha256"],
                  "initial_issues_sha256":manifest["artifacts"][1]["sha256"],
                  "manifest_sha256":hashlib.sha256((HERE/"concavity-review-1-manifest-initial.json").read_bytes()).hexdigest(),
                  "all_six_construction_artifacts_unchanged":True,
                  "peer_concavity_review_files_or_conclusions_seen":False},indent=2))
