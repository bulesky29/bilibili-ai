#!/usr/bin/env python3
"""Build a portable offline reader from the reviewed, frozen Day 1 source snapshot."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'episodes/day001/prototype'
data = json.loads((BASE / 'snapshot.json').read_text())
for page in data['pages']:
    assert page['quote'] in data['sources'][page['source']], page['source']
payload = json.dumps(data, ensure_ascii=False).replace('<', '\\u003c')
html = (BASE / 'template.html').read_text().replace('/*__SNAPSHOT__*/', payload)
(BASE / 'dist').mkdir(exist_ok=True)
(BASE / 'dist/index.html').write_text(html)
print('Built offline reader; all four evidence excerpts match the frozen sources.')
