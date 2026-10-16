#!/usr/bin/env python3
"""Write this review's provenance manifest without reading other reviews/logs."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[3]
here = Path(__file__).resolve().parent


def file_record(relative):
    path = root / relative
    data = path.read_bytes()
    stat = path.stat()
    return {"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "file_created_utc": datetime.fromtimestamp(stat.st_birthtime, timezone.utc).isoformat(),
            "file_last_written_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()}


frozen = {
    "problems/2025-B4/proof.md": "c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d",
    "problems/2025-B4/statement.md": "af0075dd635e8e4d31bb3ae9148d1731a7fbb57c06cf104763332e1496673f59",
    "problems/2025-B4/references.md": "95eee8484284dbca050d5ee71896073af58f291ae68c8b461c48505610921396",
    "problems/2025-B4/research.md": "72856e04048a313721a89e32ffa665a6b6bc470027f8e1f401776f79faae25f5",
    "problems/2025-B4/computations/literature-audit.md": "fa1921d05a974ddfd0d1cc862aa057688ea6ac063b1fbf32a33c44213505c0fe",
    "problems/2025-B4/computations/source-manifest.json": "b9abe6b4c186e50ecd78035842933aa3ec3b5d28435dc5f8c4d202b14f1b080b",
    "problems/2025-B4/computations/investigate.py": "a80a37b8ebe9bfa6811e4ff82f4960fe0ad03f48fbd9df7d595d5972f5cbc3c6",
    "problems/2025-B4/computations/initial-results.json": "ea79e5d1f11c96e04fdaba0ea0f2e4976d55672eade3332a6e2ff64e3cbb83a7"}
inputs = []
for path, expected in frozen.items():
    record = file_record(path)
    record.update(initially_observed_sha256=expected, unchanged_at_manifest=record["sha256"] == expected)
    inputs.append(record)
assert inputs[0]["unchanged_at_manifest"], "Frozen candidate changed; stop before mislabelling"

source_specs = [
    (".cache/official/2025-paper_b.pdf", "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf", "page 2, B4(b) text only", "c6d1d0c47c84521da836e766201224c84cae7c481449f28c72df842caa8e2893"),
    (".cache/official/2025-solutions.pdf", "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025solutions.pdf", "page 20, unsolved-part remark only", "46872f990326e1a0f484f02ce863b3341178a299622041768f4964a5cafd2e5e"),
    (".cache/literature/2025/bennett-levin-2015.pdf", "https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf", "published pages 15-17, equation (1), Proposition 1, Theorem 1; page 16 rendered", "ac38ad33a480068a707054a0a9acc7c937f70af84171cb7465b7d0fdd99b2b99"),
    (".cache/literature/2025/bennett-levin-1312.4037.pdf", "https://arxiv.org/pdf/1312.4037", "first two pages, theorem numbering only", "c821c8d505a22b77129f0010a515349ed6c921c7df357a5e80809d1409d296cc"),
    (".cache/literature/2025/bugeaud-mihailescu-2007.pdf", "https://journals.msp.org/mscand/article/download/659/658", "published pages 177-179, Theorem NL, Theorems 1-2; page 178 rendered", "105ea336a19143e6c9189843686185c4da6cf5d68ffdcc565664d4829fd8567c"),
    (".cache/literature/2025/son-2026-A44.pdf", "https://math.colgate.edu/~integers/aa44/aa44.pdf", "all five pages read; equation (6) on page 4 rendered", "e78734481aaa6cb88902eb87b14297376a13cade1fd23180e9d13752fe9076db"),
    (".cache/literature/2025/initial-review-1-chen-mihailescu-2026-complete.pdf", "https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1", "published pages 389-391 theorem/domain context and later proof context, not a full proof reconstruction; page 390 rendered", "0642006f404df9c8402c2394054eea9cfe63249bf38975d431fc2f553d9c1730")]
sources = []
for path, url, scope, expected in source_specs:
    record = file_record(path)
    assert record["sha256"] == expected, path
    record.update(url=url, audited_scope=scope, byte_hash_kind="original downloaded PDF bytes", reviewed_utc_date="2026-10-16",
                  redistribution="not verified; ignored local cache only; do not commit full source")
    if "initial-review-1-chen" in path:
        record.update(pages=24, pdf_header_and_eof_verified=True, retrieval_http_code=200,
                      retrieval_interval_basis="actual client file creation through last write timestamps above, 2026-10-16T15:34:10.171686Z to 2026-10-16T15:34:33.979792Z",
                      retrieval_note="A normal byte-range request received HTTP 200 and the entire 306724-byte PDF; ranges were ignored. No concatenation or access bypass.")
    else:
        record.update(original_retrieval_date_from_existing_manifest="2026-10-16", original_exact_retrieval_time="not independently available; filesystem timestamps above are not asserted to be retrieval timestamps")
    sources.append(record)

normalized = []
for path, urls, scope in [
    (".cache/literature/2025/initial-review-1-web-source-extractions.txt", ["https://www.preprints.org/manuscript/202512.0286/v1", "https://link.springer.com/article/10.1007/s11401-026-0018-7"], "Wang Theorem 7/8 full relevant context from public web tool; Springer first open returned only heading"),
    (".cache/literature/2025/initial-review-1-chen-web-context.txt", ["https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1", "https://link.springer.com/article/10.1007/s11401-026-0018-7"], "Chen theorem/domain context and publisher abstract/access preview")]:
    record = file_record(path)
    record.update(urls=urls, audited_scope=scope, byte_hash_kind="normalized web-tool response UTF-8 cache, NOT original HTML/PDF source-byte hash",
                  public_tool_access_date_utc="2026-10-16", exact_tool_request_start_time="not separately recorded", cache_time_basis="actual local file creation/last write above", ignored_cache_only=True)
    normalized.append(record)

failed_transfers = []
for path, code, diagnostic, command in [
    (".cache/literature/2025/initial-review-1-chen-mihailescu-2026.partial", 28, "Operation timed out after 45005 milliseconds with 218998 bytes received", "curl -L --fail --silent --show-error --max-time 45 'https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1' -o .cache/literature/2025/initial-review-1-chen-mihailescu-2026.pdf"),
    (".cache/literature/2025/initial-review-1-chen-mihailescu-2026-retry1.partial", 28, "Operation timed out after 60006 milliseconds with 196472 bytes received", "curl -L --fail --silent --show-error --connect-timeout 20 --max-time 60 'https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1' -o .cache/literature/2025/initial-review-1-chen-mihailescu-2026-retry1.pdf"),
    (".cache/literature/2025/initial-review-1-chen-mihailescu-2026-retry2.pdf", 18, "transfer closed with outstanding read data remaining; incomplete 278485-byte response", ".venv/bin/python -u problems/2025-B4/reviews/initial-review-1-cache.py; full curl argv/timestamps/PID in initial-review-1-cache-job.json")]:
    record = file_record(path)
    record.update(return_code=code, diagnostic=diagnostic, command=command, complete_pdf=False, excluded_from_mathematical_source=True)
    failed_transfers.append(record)

artifacts = []
for path in sorted(here.glob("initial-review-1*")):
    if path.is_file() and path.name not in {"initial-review-1-manifest.json", "initial-review-1-sha256.txt"}:
        artifacts.append(file_record(str(path.relative_to(root))))

manifest = {"created_utc": datetime.now(timezone.utc).isoformat(), "review_id": "2025-B4-initial-R1", "candidate_version": "P2025-v1",
            "review_status": "initial independent blind audit complete", "verdict": "recommend accepting C1-C4 as partial lemmas; no promotion or full solution",
            "blindness": "No other review or shared issues/status logs read before this report; no other reviewer conclusions received",
            "requested_model": "gpt-6.1-sol", "requested_reasoning": "max", "effective_setting_readback": "unavailable; requested settings only",
            "telemetry": {"source": "authoritative codex_app get_usage_limits", "weekly_used_percent": 8, "weekly_window_duration_mins": 10080, "resets_at": 1792745187, "cutoff_total_used_percent": 90},
            "frozen_inputs": inputs, "primary_pdf_sources": sources, "normalized_web_source_caches": normalized, "incomplete_transfers_preserved": failed_transfers,
            "wang_download_failure": {"url": "https://www.preprints.org/manuscript/202512.0286/v1", "command": "curl -L --fail --silent --show-error --max-time 45 https://www.preprints.org/manuscript/202512.0286/v1 -o .cache/literature/2025/initial-review-1-wang-v1-2026-10-17.html", "return_code": 56, "diagnostic": "The requested URL returned error: 403", "raw_html_cached": False, "fallback": "accessible public web-tool full text, normalized extraction hash above; no bypass"},
            "successful_chen_download_command": "curl -L --fail --silent --show-error --connect-timeout 20 --max-time 45 --range 278485- -D .cache/literature/2025/initial-review-1-chen-tail-headers.txt 'https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1' -o .cache/literature/2025/initial-review-1-chen-tail.bin; successful complete body subsequently renamed to initial-review-1-chen-mihailescu-2026-complete.pdf",
            "commands": {"exact_math_run": ".venv/bin/python -u problems/2025-B4/reviews/initial-review-1-run.py", "manifest_build": ".venv/bin/python problems/2025-B4/reviews/initial-review-1-build-manifest.py",
                         "pdf_extraction": "Python 3.12.14 pypdf.PdfReader; relevant pages/scopes in each source entry",
                         "rendering": "bundled pdftoppm -f PAGE -l PAGE -r 110 -png -singlefile INPUT_PDF /private/tmp/initial-review-1-SOURCE; pages: Bennett-Levin 2, Bugeaud-Mihailescu 2, Son 4, Chen-Mihailescu 2"},
            "review_artifacts": artifacts,
            "limits": "finite calculations are evidence only; published full proofs were not reconstructed; no preliminary proof reproduced; no global process cleanup; no charges, commit, push, promotion or candidate edit"}
(here / "initial-review-1-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
hash_lines = []
for path in sorted(here.glob("initial-review-1*")):
    if path.is_file() and path.name != "initial-review-1-sha256.txt":
        hash_lines.append(hashlib.sha256(path.read_bytes()).hexdigest() + "  " + str(path.relative_to(root)))
(here / "initial-review-1-sha256.txt").write_text("\n".join(hash_lines) + "\n")
print(json.dumps({"review_status": manifest["review_status"], "source_count": len(sources), "all_frozen_inputs_unchanged": all(r["unchanged_at_manifest"] for r in inputs),
                  "report_sha256": hashlib.sha256((here / "initial-review-1.md").read_bytes()).hexdigest(), "manifest_sha256": hashlib.sha256((here / "initial-review-1-manifest.json").read_bytes()).hexdigest()}, indent=2))
