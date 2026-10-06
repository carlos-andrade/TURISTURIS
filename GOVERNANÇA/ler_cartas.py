#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TURISTURIS — Leitor de CARTAS de Governança

Lê todas as CARTAS Markdown existentes em:
    GOVERNANÇA/CARTAS/

Objetivo:
- tornar a governança consultável diretamente pelo código;
- nunca depender de uma lista manual de CARTAS;
- preservar a ordem alfabética dos ficheiros;
- produzir uma representação JSON auditável;
- falhar explicitamente quando a pasta não existe ou não contém CARTAS.

Uso:
    python GOVERNANÇA/ler_cartas.py
    python GOVERNANÇA/ler_cartas.py --json
    python GOVERNANÇA/ler_cartas.py --output GOVERNANÇA/cartas_lidas.json

O script é somente de leitura: não altera as CARTAS.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CARTAS_DIR = REPO_ROOT / "GOVERNANÇA" / "CARTAS"


def ler_carta(path: Path) -> dict:
    texto = path.read_text(encoding="utf-8")

    linhas = texto.splitlines()
    titulo = ""
    for linha in linhas:
        if linha.startswith("# "):
            titulo = linha[2:].strip()
            break

    return {
        "nome": path.name,
        "caminho": path.relative_to(REPO_ROOT).as_posix(),
        "titulo": titulo,
        "tamanho_bytes": path.stat().st_size,
        "linhas": len(linhas),
        "conteudo": texto,
    }


def ler_cartas() -> dict:
    if not CARTAS_DIR.exists():
        raise FileNotFoundError(
            f"Pasta de CARTAS não encontrada: {CARTAS_DIR}"
        )

    if not CARTAS_DIR.is_dir():
        raise NotADirectoryError(
            f"O caminho de CARTAS não é uma pasta: {CARTAS_DIR}"
        )

    ficheiros = sorted(
        (
            p
            for p in CARTAS_DIR.iterdir()
            if p.is_file() and p.suffix.lower() == ".md"
        ),
        key=lambda p: p.name.casefold(),
    )

    if not ficheiros:
        raise RuntimeError(
            f"Nenhuma CARTA Markdown encontrada em: {CARTAS_DIR}"
        )

    cartas = [ler_carta(path) for path in ficheiros]

    return {
        "schema_version": "1.0",
        "process": "LEITOR_CARTAS_TURISTURIS",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "cartas_dir": CARTAS_DIR.relative_to(REPO_ROOT).as_posix(),
        "record_count": len(cartas),
        "cartas": cartas,
    }


def imprimir_resumo(resultado: dict) -> None:
    print("TURISTURIS — LEITOR DE CARTAS")
    print(f"Diretório: {resultado['cartas_dir']}")
    print(f"CARTAS encontradas: {resultado['record_count']}")
    print()

    for indice, carta in enumerate(resultado["cartas"], start=1):
        titulo = carta["titulo"] or "(sem título H1)"
        print(f"{indice:02d}. {carta['nome']}")
        print(f"    título: {titulo}")
        print(f"    caminho: {carta['caminho']}")
        print(f"    linhas: {carta['linhas']}")
        print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Lê todas as CARTAS de GOVERNANÇA/CARTAS."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emite o resultado completo em JSON.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Guarda o resultado JSON neste caminho.",
    )
    args = parser.parse_args()

    try:
        resultado = ler_cartas()
    except (FileNotFoundError, NotADirectoryError, RuntimeError) as exc:
        print(f"ERRO: {exc}", file=sys.stderr)
        return 1

    if args.output:
        output = args.output
        if not output.is_absolute():
            output = REPO_ROOT / output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            json.dumps(resultado, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Resultado JSON guardado em: {output.relative_to(REPO_ROOT)}")

    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    elif not args.output:
        imprimir_resumo(resultado)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
