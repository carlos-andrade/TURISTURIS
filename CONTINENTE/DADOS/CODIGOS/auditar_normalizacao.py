#!/usr/bin/env python3
"""TURISTURIS — auditoria integral da normalização de pontos turísticos."""
from pathlib import Path
import argparse
import re
import unicodedata

ROOT = Path("CONTINENTE")
DISTRICT_ROOT = ROOT / "DISTRITO"
NORM_ROOT = ROOT / "DADOS" / "NORMALIZAÇÃO"
OUT = ROOT / "DADOS" / "AUDITORIA_NORMALIZAÇÃO_V1.md"
ID_RE = re.compile(r"^PT-PTT-[A-Z0-9-]+$")

def slug(value):
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").upper()

def audit():
    municipalities = {}
    for p in DISTRICT_ROOT.glob("*/*/README.md"):
        municipalities[p.parent.name] = (p.parent.parent.name, p)

    normalized = {
        p.name[:-len("_PONTOS_TURISTICOS_V1.md")]: p
        for p in NORM_ROOT.glob("*_PONTOS_TURISTICOS_V1.md")
    }

    missing = sorted(set(municipalities) - set(normalized))
    orphan = sorted(set(normalized) - set(municipalities))
    duplicate_ids = []
    bad_ids = []
    mismatch = []
    empty = []
    ids = {}
    total = 0

    for municipality, path in sorted(normalized.items()):
        text = path.read_text(encoding="utf-8")
        district = municipalities.get(municipality, ("UNKNOWN", None))[0]
        file_ids = re.findall(r"(?m)^\|\s*\d+\s*\|\s*(PT-PTT-[A-Z0-9-]+)\s*\|", text)
        total += len(file_ids)
        if not file_ids:
            empty.append(municipality)

        for ident in file_ids:
            if ident in ids:
                duplicate_ids.append((ident, ids[ident], str(path)))
            else:
                ids[ident] = str(path)
            if not ID_RE.fullmatch(ident):
                bad_ids.append((municipality, ident))
            expected = "PT-PTT-" + slug(district) + "-" + slug(municipality) + "-"
            if not ident.startswith(expected):
                mismatch.append((municipality, district, ident))

    errors = missing + orphan + duplicate_ids + bad_ids + mismatch + empty
    status = "APROVADO" if not errors else "REPROVADO — existem anomalias"

    report = [
        "# Auditoria Integral da Normalização V1", "",
        f"- Municípios fonte: **{len(municipalities)}**",
        f"- Ficheiros normalizados: **{len(normalized)}**",
        f"- Registos/IDs encontrados: **{total}**",
        f"- Municípios sem ficheiro: **{len(missing)}**",
        f"- Ficheiros órfãos: **{len(orphan)}**",
        f"- IDs duplicados: **{len(duplicate_ids)}**",
        f"- IDs fora do padrão: **{len(bad_ids)}**",
        f"- IDs com território incompatível: **{len(mismatch)}**",
        f"- Ficheiros sem registos: **{len(empty)}**", "",
        f"## Resultado\n\n**{status}**", ""
    ]

    for title, values in [
        ("Municípios sem ficheiro", missing),
        ("Ficheiros órfãos", orphan),
        ("IDs duplicados", duplicate_ids),
        ("IDs fora do padrão", bad_ids),
        ("IDs com território incompatível", mismatch),
        ("Ficheiros sem registos", empty),
    ]:
        if values:
            report += [f"## {title}", ""] + [f"- {v}" for v in values[:100]] + [""]

    return errors, report

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="valida sem escrever o relatório; indicado para o PR Gate",
    )
    args = parser.parse_args()

    errors, report = audit()
    print("\n".join(report))

    if errors:
        return 1

    if not args.check:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text("\n".join(report) + "\n", encoding="utf-8")
        print(f"Relatório publicado: {OUT}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
