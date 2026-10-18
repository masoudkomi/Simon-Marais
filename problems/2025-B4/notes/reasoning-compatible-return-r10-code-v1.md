# R10 code and exact execution boundary

All mathematics is hand-derived in the candidate and constructor ledger.
No mathematical program, CAS, scan, numerical family test or old replay
was run. No child PID exists and no process cleanup was needed.

The NEW `reasoning-compatible-return-r10-integrity-v1.py` only:

* snapshots necessary immutable local inputs and verifies directly
  declared MDJSON/parent payload fingerprints;
* binds the immediate own FR11 parent by its freeze identity and compact
  pre-existing count/deduplicated summary, without copying its growing
  historical input inventory;
* records documentary metadata, counts the64 obligation/check labels,
  and writes a new freeze after the actual full payload model readback;
* in a SEPARATE `verify` invocation, rereads bytes, hashes and JSON and
  confirms preservation. It proves no mathematical proposition.

Exact new commands, run only in this assigned namespace:

    python3 .../reasoning-compatible-return-r10-integrity-v1.py prepare
    cat <ALL new payloads, in bounded batches for complete model readback>
    python3 .../reasoning-compatible-return-r10-integrity-v1.py seal
    cat .../reasoning-compatible-return-r10-freeze-v1.json
    python3 .../reasoning-compatible-return-r10-integrity-v1.py verify

The last command is read-only and is not folded into the seal/readback
call. It does not mutate a frozen file. No old freezer or author script
is invoked. Third-party paper bytes were not downloaded or redistributed
by this packet. Source retrieval used ordinary public web tools only.
