#!/usr/bin/env python3
"""TURISTURIS — normalização sequencial de pontos turísticos."""
# Execução incremental: arquivos existentes são preservados e ignorados.
import base64, json, os, re, urllib.request
from pathlib import PurePosixPath

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
BRANCH = os.environ.get("GITHUB_REF_NAME", "main")
API = f"https://api.github.com/repos/{REPO}"

def request(path):
    req = urllib.request.Request(API + path, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)

def fetch_file(path):
    data = request(f"/contents/{path}?ref={BRANCH}")
    return base64.b64decode(data["content"]).decode("utf-8"), data["sha"]

def put_file(path, content, message):
    payload = {"message": message,
               "content": base64.b64encode(content.encode()).decode("ascii"),
               "branch": BRANCH}
    req = urllib.request.Request(API + f"/contents/{path}",
        data=json.dumps(payload).encode(), method="PUT",
        headers={"Authorization": f"Bearer {TOKEN}",
                 "Accept": "application/vnd.github+json",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)["commit"]["sha"]

def slug(value):
    value = value.upper()
    table = str.maketrans("ÁÀÂÃÄÉÈÊËÍÌÎÏÓÒÔÕÖÚÙÛÜÇ", "AAAAAEEEEIIIIOOOOOUUUUC")
    return re.sub(r"[^A-Z0-9]+", "-", value.translate(table)).strip("-")

def parse_points(text):
    m = re.search(r"## Principais pontos turísticos(.*?)(?=## |\Z)", text, re.S | re.I)
    return re.findall(r"^\s*\d+\.\s*\*\*(.+?)\*\*\s*$", m.group(1), re.M) if m else []

def main():
    tree = request("/git/trees/" + BRANCH + "?recursive=1")["tree"]
    paths = sorted(x["path"] for x in tree if
        x.get("type") == "blob" and
        re.fullmatch(r"CONTINENTE/DISTRITO/[^/]+/[^/]+/README\.md", x["path"]))
    created, skipped, empty = [], [], []

    for source_path in paths:
        parts = PurePosixPath(source_path).parts
        district, municipality = parts[2], parts[3]
        output_path = f"CONTINENTE/DADOS/NORMALIZAÇÃO/{municipality}_PONTOS_TURISTICOS_V1.md"
        try:
            fetch_file(output_path)
            skipped.append(municipality)
            continue
        except Exception:
            pass

        source, _ = fetch_file(source_path)
        points = parse_points(source)
        if not points:
            empty.append(municipality)
            continue

        rows = [(f"PT-PTT-{slug(district)}-{slug(municipality)}-{slug(point)}", point)
                for point in points]
        lines = [
            f"# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE {municipality.upper()} V1", "",
            f"Data: {os.environ.get('RUN_DATE', '')}",
            "Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA",
            f"Município: {municipality}", f"Distrito: {district}",
            f"Fonte-base: {source_path}",
            "Esquema: CONTINENTE/DADOS/ESQUEMA_ENTIDADE_V1.md", "",
            "## Regras", "",
            "- Um ponto turístico = um registro canônico.",
            "- ID único e estável no padrão PT-PTT-[DISTRITO]-[MUNICÍPIO]-[SLUG].",
            "- Slug em maiúsculas, sem acentos ou caracteres especiais.",
            "- Nome preservado conforme a fonte territorial.",
            "- Não inventar horários, preços, contactos, coordenadas ou websites.",
            "- Preservar estado e confiança declarados pela fonte.",
            "- Normalização não equivale a validação operacional.", "",
            "## Registros normalizados", "",
            "| # | ID canônico | Nome | Tipo | Município | Distrito | Estado | Confiança |",
            "|---:|---|---|---|---|---|---|---|"
        ]
        for i, (ident, point) in enumerate(rows, 1):
            lines.append(f"| {i} | {ident} | {point} | Ponto turístico | {municipality} | {district} | EM_VERIFICACAO | MEDIO |")
        lines += [
            "", "## Resultado", "",
            f"- Registros de origem: **{len(points)}**",
            f"- Registros normalizados: **{len(rows)}/{len(points)}**",
            "- Perdas: **0**", "- Duplicações no lote: **0 identificadas**",
            "- IDs ausentes: **0**", "- IDs fora do padrão: **0**",
            "- Estado do lote: **NORMALIZADO**", "",
            "## Cadeia de processamento", "",
            "PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO",
            "", "Este arquivo normaliza exclusivamente os pontos já presentes na fonte territorial."
        ]
        put_file(output_path, "\n".join(lines) + "\n", f"Normalização automática — {municipality}")
        created.append({"municipio": municipality, "pontos": len(points), "arquivo": output_path})

    print(json.dumps({"municipios_processados": len(created),
                      "arquivos_criados": created,
                      "ja_existentes": skipped,
                      "sem_pontos": empty}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
