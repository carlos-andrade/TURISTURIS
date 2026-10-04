# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE PORTO V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: PORTO
Distrito: PORTO
Fonte-base: CONTINENTE/DISTRITO/PORTO/PORTO/README.md
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
| 1 | PT-PTT-PORTO-PORTO-RIBEIRA | Ribeira | Ponto turístico | PORTO | PORTO | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-PORTO-PORTO-TORRE-DOS-CLERIGOS | Torre dos Clérigos | Ponto turístico | PORTO | PORTO | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-PORTO-PORTO-LIVRARIA-LELLO | Livraria Lello | Ponto turístico | PORTO | PORTO | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-PORTO-PORTO-PALACIO-DA-BOLSA | Palácio da Bolsa | Ponto turístico | PORTO | PORTO | EM_VERIFICACAO | MEDIO |
| 5 | PT-PTT-PORTO-PORTO-SAO-BENTO | São Bento | Ponto turístico | PORTO | PORTO | EM_VERIFICACAO | MEDIO |
| 6 | PT-PTT-PORTO-PORTO-PONTE-D-LUIS-I | Ponte D. Luís I | Ponto turístico | PORTO | PORTO | EM_VERIFICACAO | MEDIO |

## Resultado

- Registros de origem: **6**
- Registros normalizados: **6/6**
- Perdas: **0**
- Duplicações no lote: **0 identificadas**
- IDs ausentes: **0**
- IDs fora do padrão: **0**
- Estado do lote: **NORMALIZADO**

## Cadeia de processamento

PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO

Este arquivo normaliza exclusivamente os pontos já presentes na fonte territorial.
