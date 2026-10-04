# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE IDANHA-A-NOVA V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: IDANHA-A-NOVA
Distrito: CASTELO-BRANCO
Fonte-base: CONTINENTE/DISTRITO/CASTELO-BRANCO/IDANHA-A-NOVA/README.md
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
| 1 | PT-PTT-CASTELO-BRANCO-IDANHA-A-NOVA-MONSANTO | Monsanto | Ponto turístico | IDANHA-A-NOVA | CASTELO-BRANCO | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-CASTELO-BRANCO-IDANHA-A-NOVA-CASTELO | Castelo | Ponto turístico | IDANHA-A-NOVA | CASTELO-BRANCO | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-CASTELO-BRANCO-IDANHA-A-NOVA-CENTRO-CULTURAL-RAIANO | Centro Cultural Raiano | Ponto turístico | IDANHA-A-NOVA | CASTELO-BRANCO | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-CASTELO-BRANCO-IDANHA-A-NOVA-TERMAS-DE-MONFORTINHO | Termas de Monfortinho | Ponto turístico | IDANHA-A-NOVA | CASTELO-BRANCO | EM_VERIFICACAO | MEDIO |

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
