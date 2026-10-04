# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE SANTIAGO-DO-CACEM V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: SANTIAGO-DO-CACEM
Distrito: SETUBAL
Fonte-base: CONTINENTE/DISTRITO/SETUBAL/SANTIAGO-DO-CACEM/README.md
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
| 1 | PT-PTT-SETUBAL-SANTIAGO-DO-CACEM-CASTELO-DE-SANTIAGO-DO-CACEM | Castelo de Santiago do Cacém | Ponto turístico | SANTIAGO-DO-CACEM | SETUBAL | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-SETUBAL-SANTIAGO-DO-CACEM-RUINAS-ROMANAS-DE-MIROBRIGA | Ruínas Romanas de Miróbriga | Ponto turístico | SANTIAGO-DO-CACEM | SETUBAL | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-SETUBAL-SANTIAGO-DO-CACEM-LAGOAS-DE-SANTO-ANDRE | Lagoas de Santo André | Ponto turístico | SANTIAGO-DO-CACEM | SETUBAL | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-SETUBAL-SANTIAGO-DO-CACEM-PRAIA-DE-SAO-TORPES | Praia de São Torpes | Ponto turístico | SANTIAGO-DO-CACEM | SETUBAL | EM_VERIFICACAO | MEDIO |

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
