# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE VIEIRA-DO-MINHO V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: VIEIRA-DO-MINHO
Distrito: BRAGA
Fonte-base: CONTINENTE/DISTRITO/BRAGA/VIEIRA-DO-MINHO/README.md
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
| 1 | PT-PTT-BRAGA-VIEIRA-DO-MINHO-BARRAGEM-DA-CANICADA | Barragem da Caniçada | Ponto turístico | VIEIRA-DO-MINHO | BRAGA | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-BRAGA-VIEIRA-DO-MINHO-SERRA-DA-CABREIRA | Serra da Cabreira | Ponto turístico | VIEIRA-DO-MINHO | BRAGA | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-BRAGA-VIEIRA-DO-MINHO-SENHORA-DA-LAPA | Senhora da Lapa | Ponto turístico | VIEIRA-DO-MINHO | BRAGA | EM_VERIFICACAO | MEDIO |

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
