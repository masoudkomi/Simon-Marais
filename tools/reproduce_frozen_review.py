#!/usr/bin/env python3
"""Run an immutable year review against its frozen proof in an isolated cache copy."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("year", type=int, choices=range(2017, 2026))
    parser.add_argument("script", help="Script path relative to the year directory")
    parser.add_argument("snapshot", help="Frozen proof path relative to that directory")
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    year = root / "problems" / f"{args.year}-B4"
    script, snapshot = (year / args.script).resolve(), (year / args.snapshot).resolve()
    for path in (script, snapshot):
        if not path.is_relative_to(year.resolve()) or not path.is_file():
            parser.error("Script and snapshot must be existing files in the selected year")
    if not 1 <= args.timeout <= 600:
        parser.error("Timeout must be between 1 and 600 seconds")
    cache = root / ".cache/reproductions"
    cache.mkdir(parents=True, exist_ok=True)
    isolated = Path(tempfile.mkdtemp(prefix=f"{args.year}-", dir=cache))
    copied_year = isolated / "problems" / year.name
    shutil.copytree(year, copied_year)
    shutil.copyfile(snapshot, copied_year / "proof.md")
    (isolated / ".cache").mkdir()
    (isolated / ".cache/official").symlink_to(root / ".cache/official", target_is_directory=True)
    command = [sys.executable, str(copied_year / args.script)]
    record = {
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "snapshot": str(snapshot.relative_to(root)),
        "snapshot_sha256": hashlib.sha256(snapshot.read_bytes()).hexdigest(),
        "script": str(script.relative_to(root)),
        "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
        "isolated_root": str(isolated), "command": command, "timeout_seconds": args.timeout,
    }
    with (isolated / "stdout.txt").open("w") as stdout, (isolated / "stderr.txt").open("w") as stderr:
        child = subprocess.Popen(command, cwd=isolated, stdout=stdout, stderr=stderr)
        record["pid"] = child.pid
        (isolated / "job.json").write_text(json.dumps(record, indent=2) + "\n")
        print(f"Isolated review child PID {child.pid}; checkpoint {isolated / 'job.json'}", flush=True)
        try:
            code = child.wait(timeout=args.timeout)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()
            code = 124
            record["timed_out"] = True
    record.update(return_code=code, completed_at_utc=datetime.now(timezone.utc).isoformat())
    (isolated / "job.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"Return code {code}; complete stdout/stderr and copied evidence retained at {isolated}")
    print("Original proof versions, scripts, reports and evidence were not modified.")
    raise SystemExit(code)


if __name__ == "__main__":
    main()
