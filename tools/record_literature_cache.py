#!/usr/bin/env python3
"""Fingerprint an already downloaded public PDF; never download or upload it."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('year', type=int)
    parser.add_argument('url')
    parser.add_argument('cache_path')
    parser.add_argument('--reference', required=True, help='Tracked citation or research note')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    path = (root / args.cache_path).resolve()
    if not path.is_relative_to(root / '.cache'):
        parser.error('Full papers must remain under the ignored root .cache directory')
    if not args.url.startswith(('https://', 'http://')):
        parser.error('Record the original public source URL')
    data = path.read_bytes()
    if not data.startswith(b'%PDF'):
        parser.error('The local file is not a PDF; do not record an HTML/empty response as a paper')
    manifest_path = root / 'sources/literature-retrieval.json'
    manifest = json.loads(manifest_path.read_text())
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    record = {
        'year': args.year,
        'url': args.url,
        'reference_file': args.reference,
        'cache_path': str(path.relative_to(root)),
        'redistribution_licence_verified': False,
        'inspection_status': 'retrieval only; precise mathematical applicability documented separately',
        'status': 'cached locally',
        'sha256': hashlib.sha256(data).hexdigest(),
        'bytes': len(data),
        'pages': len(PdfReader(path).pages),
        'fingerprinted_at_utc': now,
    }
    matches = [r for r in manifest['records'] if r['url'] == args.url]
    if matches:
        for previous in matches:
            if previous.get('sha256') and previous['sha256'] != record['sha256']:
                parser.error('Source bytes changed: preserve an explicit version/history rather than overwrite')
        print('Already recorded:', args.url)
        return
    manifest['records'].append(record)
    manifest['updated_at_utc'] = now
    manifest['scope'] = 'Public primary PDF sources cited in year references or research notes; additional owner manifests may contain other cached papers.'
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
