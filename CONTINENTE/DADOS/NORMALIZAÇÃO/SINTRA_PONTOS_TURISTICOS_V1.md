# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE SINTRA V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: SINTRA
Distrito: LISBOA
Fonte-base: CONTINENTE/DISTRITO/LISBOA/SINTRA/README.md
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
| 1 | PT-PTT-LISBOA-SINTRA-PALACIO-DA-PENA | Palácio da Pena | Ponto turístico | SINTRA | LISBOA | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-LISBOA-SINTRA-QUINTA-DA-REGALEIRA | Quinta da Regaleira | Ponto turístico | SINTRA | LISBOA | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-LISBOA-SINTRA-CASTELO-DOS-MOUROS | Castelo dos Mouros | Ponto turístico | SINTRA | LISBOA | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-LISBOA-SINTRA-PALACIO-NACIONAL | Palácio Nacional | Ponto turístico | SINTRA | LISBOA | EM_VERIFICACAO | MEDIO |
| 5 | PT-PTT-LISBOA-SINTRA-CABO-DA-ROCA | Cabo da Roca | Ponto turístico | SINTRA | LISBOA | EM_VERIFICACAO | MEDIO |

## Resultado

- Registros de origem: **5**
- Registros normalizados: **5/5**
- Perdas: **0**
- Duplicações no lote: **0 identificadas**
- IDs ausentes: **0**
- IDs fora do padrão: **0**
- Estado do lote: **NORMALIZADO**

## Cadeia de processamento

PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO

Este arquivo normaliza exclusivamente os pontos já presentes na fonte territorial.
