#!/usr/bin/env python3
"""Read project token accounting without copying prompts or account metadata.

Select only this root thread and spawned descendants by session metadata.
Sum per-response usage once per response ID; do not sum cumulative events
or inherited conversation history. This is a local observation, not billing.
"""
import argparse
from collections import Counter
import datetime
import json
import os
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root-thread-id', default=os.environ.get('CODEX_THREAD_ID'))
    parser.add_argument('--codex-home', type=Path, default=Path.home() / '.codex')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not args.root_thread_id:
        parser.error('--root-thread-id or CODEX_THREAD_ID is required')
    cutoff = datetime.datetime.now(datetime.timezone.utc).isoformat()
    metadata = {}
    for base in (args.codex_home / 'sessions', args.codex_home / 'archived_sessions'):
        for path in base.rglob('*.jsonl'):
            try:
                with path.open() as f:
                    first = json.loads(next(f))
            except (OSError, StopIteration, json.JSONDecodeError):
                continue
            if first.get('type') != 'session_meta':
                continue
            p = first.get('payload', {})
            source = p.get('source')
            spawn = source.get('subagent', {}).get('thread_spawn', {}) if isinstance(source, dict) else {}
            if p.get('id'):
                metadata[p['id']] = {'path': path, 'parent': spawn.get('parent_thread_id'),
                                     'agent': spawn.get('agent_path', '/root')}
    selected = {args.root_thread_id}
    while True:
        children = {i for i, m in metadata.items() if m['parent'] in selected}
        if children <= selected:
            break
        selected.update(children)
    if args.root_thread_id not in metadata:
        raise RuntimeError('Root session metadata was not found')
    all_responses, rows = {}, []
    for ident in selected:
        m = metadata[ident]
        own, last, last_at = {}, None, None
        for line in m['path'].open():
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue  # An actively appended final line can be incomplete.
            if record.get('type') != 'token_usage_record':
                continue
            p = record.get('payload', {})
            if p.get('thread_id') != ident:
                continue  # Never count copied ancestral records.
            at = record.get('timestamp')
            if at and at.replace('Z', '+00:00') > cutoff:
                continue
            response = p.get('response_id')
            if not response:
                raise RuntimeError('Usage record lacks response identity')
            usage = p['usage']
            assert usage['total_tokens'] == usage['input_tokens'] + usage['output_tokens']
            assert 0 <= usage['cached_input_tokens'] <= usage['input_tokens']
            own[response] = usage
            if response in all_responses and all_responses[response] != usage:
                raise RuntimeError('Conflicting usage for a response across sessions')
            all_responses[response] = usage
            last, last_at = p.get('thread_token_usage'), at
        summed = Counter()
        for usage in own.values():
            summed.update(usage)
        rows.append({'agent': m['agent'], 'distinct_responses': len(own),
                     'latest_record_utc': last_at, 'usage': dict(summed),
                     'matches_latest_thread_cumulative': dict(summed) == last if own else None})
    totals = Counter()
    for usage in all_responses.values():
        totals.update(usage)
    result = {'snapshot_cutoff_utc': cutoff, 'observed_sessions': len(selected),
              'distinct_responses': len(all_responses), 'usage': dict(totals),
              'uncached_input_plus_output_tokens': totals['input_tokens'] - totals['cached_input_tokens'] + totals['output_tokens'],
              'sessions_without_usage_records': sum(not r['distinct_responses'] for r in rows),
              'all_recorded_session_sums_match_cumulative': all(r['matches_latest_thread_cumulative'] for r in rows),
              'method': 'Deduplicated own-thread per-response usage records across root and recursively spawned descendants; cached input is a subset of input, reasoning output a subset of output.',
              'limits': 'Local recorded observation while work is active. Unreported in-flight usage is excluded. Not a bill or a conversion to subscription percentage. No prompts, account IDs, credentials, or response IDs exported.',
              'agents': sorted(rows, key=lambda r: r['agent'])}
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'agents'}, indent=2))


if __name__ == '__main__':
    main()
