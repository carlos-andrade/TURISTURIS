# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE AZAMBUJA V1

**Data:** 2026-10-04  
**Estado:** NORMALIZAÇÃO CONCLUÍDA — LOTE 04  
**Município:** Azambuja  
**Distrito:** Lisboa  
**Fonte-base:** `CONTINENTE/DISTRITO/LISBOA/AZAMBUJA/README.md`  
**Esquema:** `CONTINENTE/DADOS/ESQUEMA_ENTIDADE_V1.md`

## 1. Objetivo

Normalizar os pontos turísticos já identificados na estrutura territorial de Azambuja, preservando a proveniência e sem preencher por inferência campos ainda não verificados.

## 2. Regras aplicadas

1. Um ponto turístico = um registro canônico.
2. ID único e estável.
3. Padrão `PT-[TIPO]-[TERRITORIO]-[SLUG]`.
4. Slug em maiúsculas e sem acentos/caracteres especiais.
5. Nome preservado conforme a fonte territorial.
6. Município e distrito derivados da estrutura territorial.
7. Nenhum horário, preço, contacto, coordenada ou website foi inventado.
8. Estado permanece `EM_VERIFICACAO`.
9. Confiança permanece `MEDIO`.
10. Normalização não equivale a validação operacional completa.

## 3. Registros normalizados

| # | ID canônico | Nome | Tipo | Município | Distrito | Estado | Confiança |
|---:|---|---|---|---|---|---|---|
| 1 | PT-PTT-LISBOA-AZAMBUJA-PALACIO-OBRAS-NOVAS | Palácio das Obras Novas | Ponto turístico | Azambuja | Lisboa | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-LISBOA-AZAMBUJA-MUSEU-MUNICIPAL | Museu Municipal | Ponto turístico | Azambuja | Lisboa | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-LISBOA-AZAMBUJA-IGREJA-MATRIZ | Igreja Matriz | Ponto turístico | Azambuja | Lisboa | EM_VERIFICACAO | MEDIO |
| 4 | PT-PTT-LISBOA-AZAMBUJA-LEZIRIA-TEJO | Lezíria do Tejo | Ponto turístico | Azambuja | Lisboa | EM_VERIFICACAO | MEDIO |

## 4. Resultado

- Registros de origem: **4**
- Registros normalizados: **4**
- Perdas: **0**
- Duplicações no lote: **0 identificadas**
- IDs ausentes: **0**
- IDs fora do padrão: **0**
- Estado do lote: **NORMALIZADO**
- Validação de conteúdo: **EM_VERIFICACAO**
- Confiança: **MEDIO**

## 5. Campos ainda pendentes

A validação individual deverá completar, quando aplicável:

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
- fontes específicas;
- data de verificação.

## 6. Proveniência

A fonte territorial declara CAOP/DGT. A referência turística declarada é VisitPortugal/Turismo de Portugal, complementada por municípios e entidades gestoras.

A seleção é **curadoria V1** e não estatística oficial de visitantes.

## 7. Cadeia de processamento

`PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO`

## 8. Próximo lote

Seguir a ordem territorial do distrito de Lisboa.

**Próximo município:** Cadaval.
