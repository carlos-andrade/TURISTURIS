# RNET_RNAL — Arquivo e extração auditável

Fonte primária no repositório:

- `DADOS/RNET_RNAL.docx`

Objetivo desta pasta:

1. preservar a extração do DOCX;
2. manter o texto integral;
3. preservar parágrafos e tabelas em formatos estruturados;
4. preservar o pacote OOXML original descompactado;
5. preservar as imagens incorporadas;
6. manter manifesto com SHA-256, contagens e inventário dos componentes;
7. permitir futuras normalizações sem alterar a fonte original.

Fluxo:

`DADOS/RNET_RNAL.docx` → `scripts/extrair_rnet_rnal_docx.py` → `DADOS/RNET_RNAL/`

A extração não substitui a fonte original e não deve inferir ou corrigir silenciosamente dados.

Arquivos gerados:

- `TEXTO_COMPLETO.txt`
- `PARAGRAFOS.json`
- `TABELAS.json`
- `TABELAS.csv`
- `MANIFESTO_EXTRACAO.json`
- `RAW_DOCX/`
- `MEDIA/`
