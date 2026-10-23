#!/usr/bin/env python3
"""Offline documentation checks; never qualifies application behavior."""
import json,re,sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1];errors=[];count=0

def check(ok,message):
    global count
    count+=1
    if not ok:errors.append(message)

class Parser(HTMLParser):
    def __init__(self):super().__init__();self.urls=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for k in ('href','src'):
            if k in a:self.urls.append(a[k])
files=[p for p in root.rglob('*') if p.is_file() and not any(s in p.parts for s in ('node_modules','.git','__pycache__'))]
pages={}
for p in files:
    if p.suffix=='.html':
        parser=Parser();parser.feed(p.read_text());pages[p]=parser
for p in files:
    urls=pages[p].urls if p in pages else re.findall(r'\]\(([^\s)]+)\)',p.read_text()) if p.suffix=='.md' else []
    for url in urls:
        u=urlsplit(url)
        if u.scheme or u.netloc:continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p
        check(target.is_file(),f'Missing link: {p.relative_to(root)} -> {url}')
        if u.fragment and target in pages:check(unquote(u.fragment) in pages[target].ids,f'Missing anchor: {url}')
projects=json.loads((root/'data/projects.json').read_text())
check(len({p['name'] for p in projects})==len(projects),'Duplicate project names')
for p in projects:
    check(p['status'] in ('reported-tested','delivered-unverified','planned'),f'Invalid status: {p["name"]}')
    check((root/p['doc']).is_file(),f'Missing project doc: {p["name"]}')
    if p['status']=='reported-tested':check(bool(p['evidence']) and (root/p['evidence']).is_file(),f'Missing evidence: {p["name"]}')
for g in json.loads((root/'assets/diagrammes.json').read_text()):
    check((root/g['source']).is_file(),f'Missing DOT {g["id"]}')
    try:ET.parse(root/g['svg']);check(True,'')
    except (OSError,ET.ParseError):check(False,f'Invalid SVG {g["id"]}')
print(json.dumps({'result':'FAIL' if errors else 'PASS','checks':count,'errors':errors,'scope':'Documentation and local references only; imported application evidence not rerun.'},indent=2))
sys.exit(bool(errors))
