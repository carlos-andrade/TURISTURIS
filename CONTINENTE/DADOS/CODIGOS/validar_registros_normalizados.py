#!/usr/bin/env python3
"""TURISTURIS — validação técnica dos registros normalizados V1."""
import argparse, re
from pathlib import Path

ROOT = Path("CONTINENTE/DADOS/NORMALIZAÇÃO")
EXPECTED = ["#", "ID canônico", "Nome", "Tipo", "Município", "Distrito", "Estado", "Confiança"]
ID_RE = re.compile(r"^PT-PTT-[A-Z0-9-]+$")

def validate():
    files = sorted(ROOT.glob("*_PONTOS_TURISTICOS_V1.md"))
    records = 0
    errors = []
    municipalities = set()

    for path in files:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        header = None
        for line in lines:
            if line.startswith("| # | ID canônico |"):
                header = [x.strip() for x in line.strip("|").split("|")]
                break
        if header != EXPECTED:
            errors.append(f"{path}: cabeçalho de registros incompatível")
            continue

        for line in lines:
            if not line.startswith("|") or not re.match(r"^\|\s*\d+\s*\|", line):
                continue
            cells = [x.strip() for x in line.strip("|").split("|")]
            if len(cells) != len(EXPECTED):
                errors.append(f"{path}: registro com {len(cells)} campos")
                continue
            records += 1
            ident, name, typ, municipality, district, state, confidence = cells[1:]
            municipalities.add(municipality)
            if not ID_RE.fullmatch(ident):
                errors.append(f"{path}: ID inválido: {ident}")
            if not name or not typ or not municipality or not district:
                errors.append(f"{path}: campo canônico obrigatório vazio no ID {ident}")
            if state not in {"NAO_VERIFICADO","EM_VERIFICACAO","VERIFICADO","CONFLITO","DESATUALIZADO","ARQUIVADO"}:
                errors.append(f"{path}: estado inválido no ID {ident}: {state}")
            if confidence not in {"ALTO","MEDIO","BAIXO"}:
                errors.append(f"{path}: confiança inválida no ID {ident}: {confidence}")

    print("# Validação Técnica dos Registros Normalizados V1")
    print()
    print(f"- Ficheiros analisados: **{len(files)}**")
    print(f"- Registos analisados: **{records}**")
    print(f"- Municípios representados: **{len(municipalities)}**")
    print(f"- Erros de conformidade: **{len(errors)}**")
    print()
    if errors:
        print("## Resultado")
        print()
        print("**REPROVADO**")
        print()
        for error in errors[:100]:
            print(f"- {error}")
        return 1
    print("## Resultado")
    print()
    print("**APROVADO**")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.parse_args()
    raise SystemExit(validate())
