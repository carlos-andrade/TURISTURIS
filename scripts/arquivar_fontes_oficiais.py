#!/usr/bin/env python3
import hashlib, json, os, re, time
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

ROOT = Path("PESQUISA/FONTES")
TP = ROOT / "TURISMO_DE_PORTUGAL_DADOS_ABERTOS"
DGAL = ROOT / "DGAL_PORTAL_AUTARQUICO"
TP.mkdir(parents=True, exist_ok=True)
DGAL.mkdir(parents=True, exist_ok=True)

S = requests.Session()
S.headers.update({
    "User-Agent": "TURISTURIS-official-source-archiver/1.0",
    "Accept": "*/*",
})

def save_bytes(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    return {"path": str(path), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def get(url, timeout=60):
    r = S.get(url, timeout=timeout)
    r.raise_for_status()
    return r

manifest = {
    "schema_version": "1.0",
    "process": "TURISTURIS_ARQUIVO_FONTES_OFICIAIS",
    "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "sources": [],
}

# Turismo de Portugal — OGC API Records
tp_base = "https://dadosabertos.turismodeportugal.pt"
tp_api = tp_base + "/api/search/v1"
tp_urls = {
    "catalog.json": tp_api + "/catalog",
    "collections.json": tp_api + "/collections",
    "conformance.json": tp_api + "/conformance",
}
tp_src = {"authority": "Turismo de Portugal, I.P.", "base_url": tp_base, "files": [], "collections": []}

for name, url in tp_urls.items():
    r = get(url)
    target = TP / "API" / name
    rec = save_bytes(target, r.content)
    rec["url"] = url
    tp_src["files"].append(rec)

collections = json.loads((TP / "API" / "collections.json").read_text(encoding="utf-8"))
for c in collections.get("collections", []):
    cid = c.get("id")
    if not cid:
        continue
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", cid)
    cdir = TP / "API" / "collections" / safe
    meta_url = f"{tp_api}/collections/{cid}"
    query_url = f"{tp_api}/collections/{cid}/queryables"
    meta = get(meta_url)
    query = get(query_url)
    save_bytes(cdir / "collection.json", meta.content)
    save_bytes(cdir / "queryables.json", query.content)

    # Download every page exposed through OGC links. Each page is preserved as returned.
    next_url = f"{tp_api}/collections/{cid}/items?limit=1000"
    page = 0
    item_files = 0
    while next_url and page < 10000:
        r = get(next_url, timeout=120)
        page += 1
        fn = cdir / "items" / f"page_{page:05d}.json"
        save_bytes(fn, r.content)
        item_files += 1
        try:
            payload = r.json()
        except Exception:
            break
        next_url = None
        for link in payload.get("links", []):
            if link.get("rel") == "next" and link.get("href"):
                next_url = urljoin(tp_base, link["href"])
                break
        if not next_url:
            break
    tp_src["collections"].append({"id": cid, "items_pages": item_files})

manifest["sources"].append(tp_src)

# DGAL — preserve the official downloadable freguesias datasets currently published.
dgal_urls = [
    ("freguesias_2026_xls", "https://portalautarquico.dgal.gov.pt/ficheiros/?channel=266f4a32-848e-4d2c-99c6-ad5b5511d7fe&content_id=D00AE951-C5A9-4AC5-8CD4-B95B32A4F3FA&dtestate=2026-09-04113924&field=storage_image&filetype=xlsx&lang=pt&schema=f7664ca7-3a1a-4b25-9f46-2056eef44c33&ver=1"),
    ("freguesias_2026_ods", "https://portalautarquico.dgal.gov.pt/ficheiros/?channel=266f4a32-848e-4d2c-99c6-ad5b5511d7fe&content_id=3DEDD217-A6FD-4F6C-BD15-EC1ECC0EC058&dtestate=2026-09-04113946&field=storage_image&filetype=ods&lang=pt&schema=f7664ca7-3a1a-4b25-9f46-2056eef44c33&ver=1"),
]
dgal_src = {"authority": "DGAL", "files": []}
for name, url in dgal_urls:
    r = get(url, timeout=120)
    ext = ".xlsx" if name.endswith("xls") else ".ods"
    rec = save_bytes(DGAL / "DADOS_ABERTOS" / (name + ext), r.content)
    rec["url"] = url
    dgal_src["files"].append(rec)

# Preserve the source pages that document the datasets.
for name, url in [
    ("freguesias.html", "https://portalautarquico.dgal.gov.pt/pt-PT/administracao-local/entidades-autarquicas/freguesias/"),
    ("municipios.html", "https://portalautarquico.dgal.gov.pt/pt-PT/administracao-local/entidades-autarquicas/municipios/"),
]:
    try:
        r = get(url)
        rec = save_bytes(DGAL / "PAGINAS_OFICIAIS" / name, r.content)
        rec["url"] = url
        dgal_src["files"].append(rec)
    except Exception as e:
        dgal_src.setdefault("errors", []).append({"url": url, "error": str(e)})

manifest["sources"].append(dgal_src)
(TP / "MANIFESTO_ARQUIVO.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
(DGAL / "MANIFESTO_ARQUIVO.json").write_text(json.dumps(manifest["sources"][-1], ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(manifest, ensure_ascii=False, indent=2))
