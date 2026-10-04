# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE VILA-NOVA-DE-CERVEIRA V1

Data: 
Estado: NORMALIZAÇÃO CONCLUÍDA — EXECUÇÃO AUTOMÁTICA
Município: VILA-NOVA-DE-CERVEIRA
Distrito: VIANA-DO-CASTELO
Fonte-base: CONTINENTE/DISTRITO/VIANA-DO-CASTELO/VILA-NOVA-DE-CERVEIRA/README.md
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
| 1 | PT-PTT-VIANA-DO-CASTELO-VILA-NOVA-DE-CERVEIRA-CASTELO-DE-VILA-NOVA-DE-CERVEIRA | Castelo de Vila Nova de Cerveira | Ponto turístico | VILA-NOVA-DE-CERVEIRA | VIANA-DO-CASTELO | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-VIANA-DO-CASTELO-VILA-NOVA-DE-CERVEIRA-BIENAL-DE-ARTE | Bienal de Arte | Ponto turístico | VILA-NOVA-DE-CERVEIRA | VIANA-DO-CASTELO | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-VIANA-DO-CASTELO-VILA-NOVA-DE-CERVEIRA-PARQUE-DO-CASTELINHO | Parque do Castelinho | Ponto turístico | VILA-NOVA-DE-CERVEIRA | VIANA-DO-CASTELO | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-VIANA-DO-CASTELO-VILA-NOVA-DE-CERVEIRA-ILHA-DOS-AMORES | Ilha dos Amores | Ponto turístico | VILA-NOVA-DE-CERVEIRA | VIANA-DO-CASTELO | EM_VERIFICACAO | MEDIO |

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
