# Simon Marais B4 research protocol

Work only on the **portion of annual B4 explicitly designated open**: all of 2017 B4, the general 2018 enumeration (excluding research on the already known m=5 preliminary case), and **part (b) only for 2019-2025**. Do not solve or reproduce preliminary part (a); refer to established preliminary results only as attributed context when needed for the open part. Never substitute or investigate A1-A4 or B1-B3. Initial authorized scope is 2017-2025; 2026 is deferred until an official source is supplied or verified.

The coordinator owns README.md, sources/, tools/, progress/, integration, Git commits, and pushes. Each owner edits only its assigned `problems/<year>-B4/` directory. Reviewers edit only the assigned review report and issue-log entries; the proof author handles repairs. Do not commit or push from a worker.

Use one coordinator and at most **three active workers**, including reviewers. Keep up to three distinct-year research owners running together. Checkpoint before replacing an owner with a reviewer or reassigning it. Give all nine problems an initial investigation before concentrating remaining resources. Request `gpt-6.1-sol` with `max` reasoning through the agent launch interface. Record requested settings separately from any verified effective-setting readback.

Every proposed proof begins as **candidate proof - unverified**. A full solution must match the official domains, hypotheses, quantifiers, boundary cases, and conclusion. Published work must be attributed and separated from new contributions. Label computations as evidence, never proof of an unrestricted statement.

For each candidate proof, obtain two independent adversarial reviewer agents who did not construct it. Their initial reports must be completed without seeing each other's conclusions. One must reconstruct the whole argument. Audit each substantive inference and cited theorem's hypotheses; search for counterexamples and degenerate cases. Maintain an issue log, repair and re-review affected arguments. Only the coordinator may promote a result to **proved, independently reviewed**, after both audits and all substantive objections are resolved. No Lean formalization is required. No absolute-certainty claims.

Save successful and failed approaches, exact computations, commands, dependencies, outputs, proof versions, references and verification dates. Do not overwrite unrelated work. Avoid computational searches that cannot finish within the monitored budget; record parameters and incomplete runs honestly.

Use authoritative account-wide weekly telemetry. Stop at or preferably below **90% total weekly used**, not 90% of the remaining allowance. Reserve capacity for review, integration, commits and push; recheck at group transitions and periodically during sustained work. If telemetry becomes unavailable, checkpoint and request a measurable substitute. Do not automatically spend into a new weekly window. Do not use separately billed APIs.

Git destination: `https://github.com/masoudkomi/Simon-Marais.git`; research branch: `codex/smmc-b4-research`. No force pushes, deletions of existing work, or merge into a default branch. Commit and push meaningful coordinator checkpoints, including before stopping. If push fails, preserve local commits and record the exact failure. Never commit credentials or authentication data.
