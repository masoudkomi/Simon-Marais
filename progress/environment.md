# Execution environment

- Host: macOS; shell zsh; workspace `/Users/uqmkamga/Documents/ChatGPT/Website`.
- Agent capacity: four active agents total, including the coordinator. Local config changes do not override the active hosted allocation.
- User explicitly replaced the ten-owner requirement with three simultaneous owners and authorized groups/reassignment/review-slot rotation.
- Mathematical worker launch requests: `model=gpt-6.1-sol`, `reasoning_effort=max`, fresh context. Independent effective-settings readback is unavailable in the collaboration tools.
- Git remote: `https://github.com/masoudkomi/Simon-Marais.git`.
- Branch: `codex/smmc-b4-research`.
- System Git uses `osxkeychain`. GitHub browser sign-in and Git push authentication are distinct; test push at the initial checkpoint. Never print or commit stored credentials.
- Bundled Python: `/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.
- Bundled Node: `/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node`.
- Runtime bundle: `26.1013.11914`.

Mathematical scripts should document their own invocation and exact output. Cache downloaded source PDFs under ignored `.cache/official/`; preserve source URLs and SHA-256 hashes in tracked manifests. Do not include secrets, `.env`, or unrelated project files.
