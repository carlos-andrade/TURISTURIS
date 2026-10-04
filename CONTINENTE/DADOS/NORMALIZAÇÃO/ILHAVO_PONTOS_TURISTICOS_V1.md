# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE ILHAVO V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: ILHAVO
Distrito: AVEIRO
Fonte-base: CONTINENTE/DISTRITO/AVEIRO/ILHAVO/README.md
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
| 1 | PT-PTT-AVEIRO-ILHAVO-MUSEU-MARITIMO-DE-ILHAVO | Museu Marítimo de Ílhavo | Ponto turístico | ILHAVO | AVEIRO | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-AVEIRO-ILHAVO-VISTA-ALEGRE | Vista Alegre | Ponto turístico | ILHAVO | AVEIRO | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-AVEIRO-ILHAVO-COSTA-NOVA | Costa Nova | Ponto turístico | ILHAVO | AVEIRO | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-AVEIRO-ILHAVO-PRAIA-DA-COSTA-NOVA | Praia da Costa Nova | Ponto turístico | ILHAVO | AVEIRO | EM_VERIFICACAO | MEDIO |

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
