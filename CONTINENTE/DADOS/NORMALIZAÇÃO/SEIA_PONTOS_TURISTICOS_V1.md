# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE SEIA V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: SEIA
Distrito: GUARDA
Fonte-base: CONTINENTE/DISTRITO/GUARDA/SEIA/README.md
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
| 1 | PT-PTT-GUARDA-SEIA-MUSEU-DO-PAO | Museu do Pão | Ponto turístico | SEIA | GUARDA | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-GUARDA-SEIA-MUSEU-NATURAL-DA-ELECTRICIDADE | Museu Natural da Electricidade | Ponto turístico | SEIA | GUARDA | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-GUARDA-SEIA-SERRA-DA-ESTRELA | Serra da Estrela | Ponto turístico | SEIA | GUARDA | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-GUARDA-SEIA-LAGOA-COMPRIDA | Lagoa Comprida | Ponto turístico | SEIA | GUARDA | EM_VERIFICACAO | MEDIO |

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
