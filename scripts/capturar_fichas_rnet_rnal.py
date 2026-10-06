#!/usr/bin/env python3
import csv, hashlib, json, re, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup

SOURCES = {
    'RNET': 'https://rnt.turismodeportugal.pt/RNT/RNET.aspx?nr=6803',
    'RNAL': 'https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr=15642',
}
ROOT = Path(__file__).resolve().parents[1]
HEADERS = {'User-Agent': 'TURISTURIS-Official-Ficha-Capture/1.0', 'Accept': 'text/html,application/xhtml+xml'}

def sha256(data): return hashlib.sha256(data).hexdigest()
def number(url): return parse_qs(urlparse(url).query).get('nr',['unknown'])[0]
def clean(s): return re.sub(r'\\s+', ' ', s).strip()
def code(label, n):
    x = re.sub(r'[^A-Z0-9À-ÖØ-Ý]+', '_', clean(label).upper()).strip('_')
    return x[:80] or f'FIELD_{n:04d}'

def capture(kind, url):
    nr = number(url)
    base = ROOT / ('FICHAS OFICIAIS RNET' if kind == 'RNET' else 'FICHAS OFICIAIS RNAL') / nr
    for name in ('raw','structured','audit'): (base/name).mkdir(parents=True, exist_ok=True)
    r = None; err = None
    for attempt in range(1,4):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30); r.raise_for_status(); break
        except Exception as e:
            err = e
            if attempt < 3: time.sleep(attempt*2)
    if r is None: raise RuntimeError(f'Falha de captura {kind} {nr}: {err}')
    html = r.content; source_hash = sha256(html); captured = datetime.now(timezone.utc).isoformat()
    (base/'raw'/'source.html').write_bytes(html)
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(['script','style','noscript','template']): tag.decompose()
    rows=[]; counts={}; seq=0
    for table_i, table in enumerate(soup.find_all('table'),1):
        for row_i, tr in enumerate(table.find_all('tr'),1):
            cells=tr.find_all(['th','td'])
            for col_i, cell in enumerate(cells,1):
                value=clean(cell.get_text(' ',strip=True))
                if not value: continue
                fc=code(value,len(rows)+1); counts[fc]=counts.get(fc,0)+1; seq+=1
                rows.append({'sequence':seq,'element_type':'table_cell','table_index':table_i,'row_index':row_i,'column_index':col_i,'raw_label':value,'raw_value':value,'field_code':fc,'occurrence':counts[fc],'record_key':f'{kind}:{nr}:{fc}:{counts[fc]:03d}','source_url':url,'capture_utc':captured,'source_sha256':source_hash})
    for tag in soup.find_all(['h1','h2','h3','h4','h5','h6','p','li']):
        value=clean(tag.get_text(' ',strip=True))
        if not value: continue
        fc=code(value,len(rows)+1); counts[fc]=counts.get(fc,0)+1; seq+=1
        rows.append({'sequence':seq,'element_type':tag.name,'table_index':'','row_index':'','column_index':'','raw_label':value,'raw_value':value,'field_code':fc,'occurrence':counts[fc],'record_key':f'{kind}:{nr}:{fc}:{counts[fc]:03d}','source_url':url,'capture_utc':captured,'source_sha256':source_hash})
    data=json.dumps(rows,ensure_ascii=False,indent=2).encode()
    (base/'structured'/'ficha.json').write_bytes(data)
    if rows:
        with (base/'structured'/'ficha.csv').open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    manifest={'capture_id':f'{kind}:{nr}:{captured}','type':kind,'registry_number':nr,'source_url':url,'capture_utc':captured,'http_status':r.status_code,'content_type':r.headers.get('Content-Type',''),'source_sha256':source_hash,'structured_sha256':sha256(data),'field_count':len(rows),'table_count':len(soup.find_all('table')),'rules':'CARTA-CAPTURA-RNET-RNAL-V1'}
    (base/'audit'/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    return manifest

def main():
    results=[]; failures=[]
    for kind,url in SOURCES.items():
        try: results.append(capture(kind,url))
        except Exception as e: failures.append({'type':kind,'url':url,'error':str(e)})
    print(json.dumps({'results':results,'failures':failures},ensure_ascii=False,indent=2)); return 1 if failures else 0
if __name__ == '__main__': sys.exit(main())