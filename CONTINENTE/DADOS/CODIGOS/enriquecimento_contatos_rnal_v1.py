#!/usr/bin/env python3
"""WEB-12.6 — recolha controlada de contactos públicos das fichas RNAL do RNT."""
import json, os, re, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

BASE=Path("CONTINENTE/DADOS/NORMALIZAÇÃO/ALOJAMENTOS")
OUT=Path("CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/RNAL_CONTACTOS_PUBLICOS_V1.json")
UA="TURISTURIS/WEB-12.6 (+https://github.com/carlos-andrade/TURISTURIS)"

def clean(s):
    return re.sub(r"\s+"," ",s or "").strip() or None

def fetch(r):
    sid=((r.get("fontes") or [{}])[0]).get("id_origem")
    if not sid:
        return {"id":r.get("id"),"status":"SEM_ID"}
    url="https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr="+str(sid)
    try:
        req=Request(url,headers={"User-Agent":UA})
        html=urlopen(req,timeout=20).read().decode("utf-8","ignore")
    except (HTTPError,URLError,TimeoutError) as e:
        return {"id":r.get("id"),"id_origem":sid,"status":"ERRO_REDE","erro":str(e)[:200]}
    text=clean(re.sub(r"<[^>]+>"," ",html.replace("</tr>","\n").replace("</td>"," | "))) or ""
    m=re.search(r"Contactos\s+(.{0,500}?)(?:Nota:|Seguro de Responsabilidade Civil)",text,re.I|re.S)
    contacts=clean(m.group(1)) if m else None
    phones=sorted(set(re.findall(r"(?<!\d)(?:\+351\s*)?(?:2\d{2}|9\d{2})[\s.-]?\d{3}[\s.-]?\d{3}(?!\d)",contacts or "")))
    emails=sorted(set(re.findall(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}",contacts or "",re.I)))
    return {"id":r.get("id"),"id_origem":sid,"status":"OK","ficha_oficial":url,"telefone":phones,"email":emails,"data_recolha_utc":time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime())}

def main():
    src=BASE/"RNAL_NORMALIZADO_V1.json"
    rows=json.loads(src.read_text(encoding="utf-8"))["records"]
    offset=max(0,int(os.getenv("RNAL_OFFSET","0")))
    limit=int(os.getenv("RNAL_LIMIT","50"))
    workers=max(1,min(8,int(os.getenv("RNAL_WORKERS","4"))))
    if limit <= 0:
        raise ValueError("RNAL_LIMIT deve ser > 0")
    rows=rows[offset:offset+limit]
    results=[]
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures=[ex.submit(fetch,r) for r in rows]
        for i,f in enumerate(as_completed(futures),1):
            results.append(f.result())
            if i%25==0 or i==len(rows):
                print(f"processados={i}/{len(rows)}")
    results.sort(key=lambda x:x.get("id") or "")
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps({
        "schema_version":"1.0",
        "process":"WEB-12.6",
        "source":"RNT/RNAL",
        "offset":offset,
        "limit":limit,
        "record_count":len(results),
        "records":results
    },ensure_ascii=False),encoding="utf-8")
    print(json.dumps({"output":str(OUT),"offset":offset,"limit":limit,"record_count":len(results)},ensure_ascii=False))

if __name__=="__main__":
    main()
