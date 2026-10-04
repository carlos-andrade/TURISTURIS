# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE ALENQUER V1

**Data:** 2026-10-04  
**Estado:** NORMALIZAÇÃO CONCLUÍDA — LOTE 02  
**Município:** Alenquer  
**Distrito:** Lisboa  
**Fonte-base:** `CONTINENTE/DISTRITO/LISBOA/ALENQUER/README.md`  
**Esquema:** `CONTINENTE/DADOS/ESQUEMA_ENTIDADE_V1.md`

## 1. Objetivo

Normalizar os pontos turísticos já identificados no registro territorial de Alenquer para uma estrutura canônica única, com IDs estáveis e sem inventar informações que ainda não foram verificadas.

## 2. Regras aplicadas

1. Um ponto turístico corresponde a um registro canônico.
2. Cada registro recebe ID estável e único.
3. O formato aplicado é `PT-[TIPO]-[TERRITORIO]-[SLUG]`.
4. O slug utiliza maiúsculas, sem acentos e sem caracteres especiais.
5. O nome preserva a designação apresentada na fonte territorial.
6. Distrito e município são derivados da estrutura territorial existente.
7. Não foram inventados endereço, coordenadas, contactos, websites, horários ou preços.
8. O estado permanece `EM_VERIFICACAO`, conforme a fonte territorial.
9. O grau de confiança permanece `MEDIO`, conforme a fonte territorial.
10. A normalização não equivale à validação operacional completa.

## 3. Registros normalizados

| # | ID canônico | Nome | Tipo | Município | Distrito | Estado | Confiança |
|---:|---|---|---|---|---|---|---|
| 1 | PT-PTT-LISBOA-ALENQUER-CASTELO-ALENQUER | Castelo de Alenquer | Ponto turístico | Alenquer | Lisboa | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-LISBOA-ALENQUER-IGREJA-SAO-PEDRO | Igreja de São Pedro | Ponto turístico | Alenquer | Lisboa | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-LISBOA-ALENQUER-MUSEU-JOAO-MARIO | Museu João Mário | Ponto turístico | Alenquer | Lisboa | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-LISBOA-ALENQUER-SERRA-MONTEJUNTO | Serra de Montejunto | Ponto turístico | Alenquer | Lisboa | EM_VERIFICACAO | MEDIO |

## 4. Resultado

- Registros de origem: **4**
- Registros normalizados: **4**
- Perdas: **0**
- Duplicações no lote: **0 identificadas**
- IDs ausentes: **0**
- IDs fora do padrão: **0**
- Estado do lote: **NORMALIZADO**
- Validação de conteúdo: **EM_VERIFICACAO**, herdada da fonte territorial.

## 5. Campos ainda pendentes

Para transformar estes registros em entidades turísticas completas, será necessária validação específica de:

- localidade/freguesia;
- endereço;
- coordenadas;
- descrição;
- história;
- interesse turístico;
- contactos;
- telefone;
- email;
- website;
- horários;
- preços;
- acessibilidade;
- serviços;
- reservas;
- fontes específicas de cada ponto.

## 6. Proveniência

A seleção territorial de Alenquer declara como fonte territorial CAOP/DGT e como referência turística VisitPortugal/Turismo de Portugal, complementada por municípios e entidades gestoras.

A seleção é uma **curadoria V1** e não constitui ranking oficial de visitantes.

## 7. Cadeia de processamento

`PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO`

## 8. Próximo lote

Seguir a ordem territorial definida para o distrito de Lisboa.

**Próximo município:** Arruda dos Vinhos.
