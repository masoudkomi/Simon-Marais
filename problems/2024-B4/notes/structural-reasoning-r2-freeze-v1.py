"""One-time integrity freeze for an analytic candidate; no mathematical search."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BASE = Path("problems/2024-B4/notes/structural-reasoning-r2")


def record(path):
    path = Path(path)
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def save(suffix, value):
    with (ROOT / (str(BASE) + suffix)).open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def main():
    now = datetime.now(timezone.utc).isoformat()
    manifest_path = ROOT / (str(BASE) + "-manifest-v1.json")
    if manifest_path.exists():
        raise SystemExit("Existing freeze preserved; make a new version instead of overwriting")

    old_manifest = json.loads((ROOT / "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json").read_text())
    old_matches = all(record(row["path"])["sha256"] == row["sha256"] for row in old_manifest["records"])
    if not old_matches:
        raise SystemExit("Old blind-review freeze differs; no files modified by this script")

    inputs = [
        "AGENTS.md", ".gitignore", "problems/2024-B4/statement.md",
        "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
        "problems/2024-B4/reviews/criterion-acceptance.md",
        "problems/2024-B4/reviews/family-acceptance.md",
        "problems/2024-B4/notes/deep-literature-r2-report-v1.md",
        "problems/2024-B4/notes/deep-literature-r2-kasami-orbit-lead-v1.md",
        "problems/2024-B4/notes/deep-literature-r2-search-sources-v1.json",
    ]
    paper_data = [
        {
            **record(".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf"),
            "title": "McGuire PhD thesis, Caltech1995",
            "url": "https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf",
            "read_scope_this_task": "Full scanned source available; visually inspected printed pp10-11,24-25,29-38, including PropositionB/9 and Kasami13/57 examples. Not all97pages or every thesis proof audited.",
        },
        {
            **record(".cache/literature/deep-literature-r2/2024-delgado-janwa-1612.05997v1.pdf"),
            "title": "Delgado-Janwa arXiv1612.05997v1",
            "url": "https://arxiv.org/pdf/1612.05997v1",
            "read_scope_this_task": "Full §3 source text; whole PDFp7 visually inspected; eq5/6 field and specialization premise checked; Lemma1 parity inference on pp8-9 checked and found insufficient. OriginalJW1993proof not verified.",
        },
        {
            **record(".cache/literature/2024/cited-3e7f3cb84c20c6b1.pdf"),
            "title": "Hernando-McGuire arXiv0903.2016v4, published J.Algebra343(2011)",
            "url": "https://arxiv.org/pdf/0903.2016",
            "read_scope_this_task": "§2.1 precise component theorem, §§4-5 theorem premises, Theorem15 irreducibility assumption. This task did not independently reconstruct the entire published proof.",
        },
    ]
    derived = [
        record(".cache/literature/structural-reasoning-r2-delgado-janwa-page7.png")
    ]
    derived.extend(
        record(f".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-{page:02d}.png")
        for page in [15, 16, 29, 30, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]
    )
    queries = [
        '"Hyperplane sections of Fermat varieties" Janwa Wilson pdf',
        '"Kasami" "McGuire" "thesis" factorization',
        '"Janwa" "Wilson" "P_alpha" "1993"',
        '"Hyperplane sections of Fermat varieties in P3" filetype:pdf',
        '"Janwa" "Wilson" "1993" "Hyperplane" pdf -site:researchgate.net -site:dblp.org -site:dblp.uni-trier.de',
        '"Hyperplane Sections" "180" "194" "pdf" "Janwa"',
        'site:ramanujan.uprrp.edu "Wilson" "Fermat"',
        'site:authors.library.caltech.edu "Hyperplane sections" pdf',
        '"Kasami" "factors" "P" "q+1" polynomial phi',
        '"Kasami" "divides" "phi" polynomial 3641',
        '"Kasami" "13" "205" "factor" irreducibility',
        '"Fermat" "2^{2" "2^k+1" "Janwa" factor',
        '"10.3934/amc.2014.8.497" filetype:pdf',
        '"Férard" "phi" "13" "2014" "irreducibility" pdf',
        '"Férard" "Fermat varieties" "497" pdf -site:researchgate.net -site:aimsciences.org',
        '"On the irreducibility of the hyperplane sections" "pdf" "Férard"',
        '"irreducible" "absolutely irreducible" "2^i" "prime power" "Janwa" tangent',
        '"McGuire" "irreducible over" "symmetric" "Frobenius" polynomial',
        '"phi" "linear factor" "Gold" polynomial APN',
        '"g_t" "linear factors" "Gold" irreducible',
        '"Janwa" "linear factors" "binary weight"',
        '"Fermat" "linear factors" "2^i" "phi" APN',
        'APN "linear factor" "phi_t"',
        'APN "linear factors" "Gold exponent"',
        '"linear factor" "Hernando" "McGuire"',
        '"linear factors" "Janwa" "Wilson" polynomial',
    ]
    source_record = {
        "recorded_at_utc": now,
        "status": "source audit for candidate proof - unverified",
        "settings": {"requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "verified_effective_settings": None},
        "scope": "2024B4partb only, no preliminary construction proof",
        "tracked_inputs": [record(path) for path in inputs],
        "ignored_full_papers": paper_data,
        "derived_read_only_renderings": derived,
        "queries_exact": queries,
        "access_checks": [
            {"url": "https://link.springer.com/chapter/10.1007/3-540-56686-4_43", "outcome": "Subscriptionpreview; fulloriginalJW1993notobtained; accesslimitrespected"},
            {"url": "https://authors.library.caltech.edu/records/wcxdz-pkj80", "outcome": "Originalchaptermetadataonly"},
            {"url": "https://biblio.cerist.dz/hrbdonf5214/ouvrages/00000000000000595119000000_2.pdf", "outcome": "NewlyindexedordinarypublicHTTPSroute returned404"},
            {"url": "http://biblio.cerist.dz/hrbdonf5214/ouvrages/00000000000000595119000000_2.pdf", "outcome": "OrdinaryHTTProute unavailable"},
            {"url": "https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497", "outcome": "Abstractpage; publicHTMLcitation_pdf_urlinspected"},
            {
                "url": "https://www.aimsciences.org/data/article/export-pdf?id=35639722-1f4a-4d82-b06d-fb1493ba278d",
                "outcome": "Exactpubliccitation-PDFendpoint exited0butreturnedzero bytes; not a paper and no theorem premise inferred",
                "failed_retrieval_artifact": record(".cache/literature/structural-reasoning-r2-ferard2014.pdf"),
            },
        ],
        "exact_commands": [
            {
                "cmd": "curl -L --fail --silent --show-error https://www.aimsciences.org/article/doi/10.3934/amc.2014.8.497 | rg -n 'citation_pdf|pdfUrl|pdfurl|downloadPdf|downloadpdf|downloadFile|pdfFile|article-pdf|showPdf|viewPdf|pdfPath|PDF'",
                "outcome": "SandboxDNSfailurefirst; requiredescalatedretrysucceeded andexposedcitation_pdf_url; noauthdata",
            },
            {
                "cmd": "curl -L --fail --silent --show-error --max-time 60 'https://www.aimsciences.org/data/article/export-pdf?id=35639722-1f4a-4d82-b06d-fb1493ba278d' -o .cache/literature/structural-reasoning-r2-ferard2014.pdf",
                "outcome": "exit0;0bytes;failedretrieval",
            },
            {
                "cmd": ".venv/bin/python -c 'import fitz; p=fitz.open(\".cache/literature/deep-literature-r2/2024-delgado-janwa-1612.05997v1.pdf\"); p[6].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(\".cache/literature/structural-reasoning-r2-delgado-janwa-page7.png\")'",
                "outcome": "exit1;ModuleNotFoundError:fitz;bundledPythonretryfailedsameway;noinstall",
            },
            {
                "cmd": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm -f 7 -l 7 -singlefile -scale-to 1600 -png .cache/literature/deep-literature-r2/2024-delgado-janwa-1612.05997v1.pdf .cache/literature/structural-reasoning-r2-delgado-janwa-page7",
                "outcome": "exit0;0.109420166seconds;wholepagevisuallyinspected",
            },
        ],
        "proof_dependency": "T1-T4self-contained;finitefieldfactsandUFD/Frobeniusargumentsreconstructed;KasamiandHMtheoremsareattributedcontext,notpremises",
        "mathematical_computation": "None;noCAS,enumerationorfinitefieldscan",
        "old_J15_review_unchanged": old_matches,
        "weekly_telemetry": {"verified_at_utc": "2026-10-16T22:25:49Z", "authoritative_account_wide_total_used_percent": 18, "window_minutes": 10080, "resets_at": 1792745187, "stop_total_used_percent": 90},
        "access_policy": "Nocharge,subscription,login,contact,accessbypassorpaidAPI;fullpapersandrenderingsignored;redistributionlicencenotinferred",
        "no_git_or_shared_status_write": True,
    }
    save("-sources-v1.json", source_record)

    proof = record(str(BASE) + "-candidate-v1.md")
    output = {
        "frozen_at_utc": now,
        "status": "candidate proof - unverified; freeze before two fresh independent nonconstructor reviews",
        "candidate": proof,
        "old_J15_review_unchanged": old_matches,
        "new_mathematical_enumeration_or_CAS": False,
        "proof_claims": ["T1noabsolutelinefactor", "T2noF2factorofdegree1-3", "T3individualfactorordinarytangentfielddescent", "T4i3localfactortrichotomy"],
    }
    save("-freeze-output-v1.json", output)
    artifacts = [
        str(BASE) + suffix for suffix in [
            "-candidate-v1.md", "-source-audit-v1.md", "-research-log-v1.md",
            "-sources-v1.json", "-freeze-v1.py", "-freeze-output-v1.json",
        ]
    ]
    freeze = {
        **output,
        "constructor": "review_2021_reasoning_j15_r2",
        "requested_model": "gpt-6.1-sol",
        "requested_reasoning": "max",
        "verified_effective_settings": None,
        "required_reviews": "Two fresh independent nonconstructors, initialreportsblindtoeachother, onefullreconstruction;onlycoordinatorpromotes",
        "scope_limits": "Noexponentclassification;noall-componentsthroughPclaim;nogeneralAPN-to-F2substitution;originalJW1993proofandFerardfullpremisesremainunread",
        "command": ".venv/bin/python problems/2024-B4/notes/structural-reasoning-r2-freeze-v1.py",
        "records": [record(path) for path in artifacts],
    }
    save("-manifest-v1.json", freeze)
    print(json.dumps(output))


if __name__ == "__main__":
    main()
