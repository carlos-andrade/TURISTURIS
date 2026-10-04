# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE FAFE V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: FAFE
Distrito: BRAGA
Fonte-base: CONTINENTE/DISTRITO/BRAGA/FAFE/README.md
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
| 1 | PT-PTT-BRAGA-FAFE-TEATRO-CINEMA | Teatro-Cinema | Ponto turístico | FAFE | BRAGA | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-BRAGA-FAFE-MUSEU-DO-MOINHO-E-DO-POVO | Museu do Moinho e do Povo | Ponto turístico | FAFE | BRAGA | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-BRAGA-FAFE-PRACA-25-DE-ABRIL | Praça 25 de Abril | Ponto turístico | FAFE | BRAGA | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-BRAGA-FAFE-BARRAGEM-DE-QUEIMADELA | Barragem de Queimadela | Ponto turístico | FAFE | BRAGA | EM_VERIFICACAO | MEDIO |

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
