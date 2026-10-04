# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE SERTA V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: SERTA
Distrito: CASTELO-BRANCO
Fonte-base: CONTINENTE/DISTRITO/CASTELO-BRANCO/SERTA/README.md
Esquema: CONTINENTE/DADOS/ESQUEMA_ENTIDADE_V1.md

## Regras

- Um ponto turístico = um registro canônico.
- ID único e estável no padrão PT-PTT-[DISTRITO]-[MUNICÍPIO]-[SLUG].
- Slug em maiúsculas, sem acentos ou caracteres especiais.
- Nome preservado conforme a fonte territorial.
- Não inventar horários, preços, contactos, coordenadas ou websites.
- Preservar estado e confiança declarados pela fonte.
- Normalização não equivale a validação operacional.

## Registros normalizados

| # | ID canônico | Nome | Tipo | Município | Distrito | Estado | Confiança |
|---:|---|---|---|---|---|---|---|
| 1 | PT-PTT-CASTELO-BRANCO-SERTA-CASTELO-DA-SERTA | Castelo da Sertã | Ponto turístico | SERTA | CASTELO-BRANCO | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-CASTELO-BRANCO-SERTA-PONTE-FILIPINA | Ponte Filipina | Ponto turístico | SERTA | CASTELO-BRANCO | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-CASTELO-BRANCO-SERTA-PRAIA-FLUVIAL-DA-RIBEIRA-GRANDE | Praia Fluvial da Ribeira Grande | Ponto turístico | SERTA | CASTELO-BRANCO | EM_VERIFICACAO | MEDIO |

## Resultado

- Registros de origem: **3**
- Registros normalizados: **3/3**
- Perdas: **0**
- Duplicações no lote: **0 identificadas**
- IDs ausentes: **0**
- IDs fora do padrão: **0**
- Estado do lote: **NORMALIZADO**

## Cadeia de processamento

PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO

Este arquivo normaliza exclusivamente os pontos já presentes na fonte territorial.
