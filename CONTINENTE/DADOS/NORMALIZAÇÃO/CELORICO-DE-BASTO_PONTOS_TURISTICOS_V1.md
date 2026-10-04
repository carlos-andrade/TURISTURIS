# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE CELORICO-DE-BASTO V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: CELORICO-DE-BASTO
Distrito: BRAGA
Fonte-base: CONTINENTE/DISTRITO/BRAGA/CELORICO-DE-BASTO/README.md
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
| 1 | PT-PTT-BRAGA-CELORICO-DE-BASTO-CASTELO-DE-ARNOIA | Castelo de Arnóia | Ponto turístico | CELORICO-DE-BASTO | BRAGA | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-BRAGA-CELORICO-DE-BASTO-MOSTEIRO-DE-ARNOIA | Mosteiro de Arnóia | Ponto turístico | CELORICO-DE-BASTO | BRAGA | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-BRAGA-CELORICO-DE-BASTO-CENTRO-HISTORICO | Centro Histórico | Ponto turístico | CELORICO-DE-BASTO | BRAGA | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-BRAGA-CELORICO-DE-BASTO-SERRA-DO-ALVAO | Serra do Alvão | Ponto turístico | CELORICO-DE-BASTO | BRAGA | EM_VERIFICACAO | MEDIO |

## Resultado

- Registros de origem: **4**
- Registros normalizados: **4/4**
- Perdas: **0**
- Duplicações no lote: **0 identificadas**
- IDs ausentes: **0**
- IDs fora do padrão: **0**
- Estado do lote: **NORMALIZADO**

## Cadeia de processamento

PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO

Este arquivo normaliza exclusivamente os pontos já presentes na fonte territorial.
