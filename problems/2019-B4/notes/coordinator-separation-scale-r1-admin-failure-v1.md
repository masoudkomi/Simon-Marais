# Administrative path-format failure,2026-10-17 UTC

The first documentary-freeze invocation failed BEFORE writing any source, validation or manifest output. The old secondpass authority uses problem-relative paths such as notes/secondpass-canonical-renewal.md. The first checker assumed every path was repository-relative and raised FileNotFoundError. Its complete source is preserved as freeze-before-path-repair-v0.py.

The metadata-only repair resolves an existing repository path first, otherwise the exact2019 problem-relative path. Every declared SHA and available byte size is still checked. No mathematical script, old certificate or sign child was rerun. This failure has no bearing on SS1--SS3 and no frozen mathematical input was edited.
