# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE ARRUDA DOS VINHOS V1

**Data:** 2026-10-04  
**Estado:** NORMALIZAÇÃO CONCLUÍDA — LOTE 03  
**Município:** Arruda dos Vinhos  
**Distrito:** Lisboa  
**Fonte-base:** `CONTINENTE/DISTRITO/LISBOA/ARRUDA-DOS-VINHOS/README.md`  
**Esquema:** `CONTINENTE/DADOS/ESQUEMA_ENTIDADE_V1.md`

## 1. Objetivo

Normalizar os pontos turísticos já identificados na estrutura territorial de Arruda dos Vinhos, mantendo a proveniência e sem completar campos por inferência.

## 2. Regras aplicadas

1. Um ponto turístico = um registro canônico.
2. ID único e estável.
3. Padrão `PT-[TIPO]-[TERRITORIO]-[SLUG]`.
4. Slug em maiúsculas e sem acentos/caracteres especiais.
5. Nome preservado conforme a fonte territorial.
6. Município e distrito derivados da estrutura territorial.
7. Nenhum horário, preço, contacto, coordenada ou website foi inventado.
8. O estado permanece `EM_VERIFICACAO`.
9. A confiança permanece `MEDIO`.
10. Normalização não significa validação operacional completa.

## 3. Registros normalizados

| # | ID canônico | Nome | Tipo | Município | Distrito | Estado | Confiança |
|---:|---|---|---|---|---|---|---|
| 1 | PT-PTT-LISBOA-ARRUDA-DOS-VINHOS-IGREJA-MATRIZ | Igreja Matriz | Ponto turístico | Arruda dos Vinhos | Lisboa | EM_VERIFICACAO | MEDIO |
| 2 | PT-PTT-LISBOA-ARRUDA-DOS-VINHOS-CENTRO-HISTORICO | Centro Histórico | Ponto turístico | Arruda dos Vinhos | Lisboa | EM_VERIFICACAO | MEDIO |
| 3 | PT-PTT-LISBOA-ARRUDA-DOS-VINHOS-PAISAGEM-VITIVINICOLA | Paisagem vitivinícola | Ponto turístico | Arruda dos Vinhos | Lisboa | EM_VERIFICACAO | MEDIO |

## 4. Resultado

- Registros de origem: **3**
- Registros normalizados: **3**
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

A fonte territorial declara CAOP/DGT. A referência turística declarada é VisitPortugal/Turismo de Portugal, complementada por municípios, entidades gestoras e fontes institucionais específicas.

A seleção é **curadoria V1** e não estatística oficial de visitantes.

## 7. Cadeia de processamento

`PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO`

## 8. Próximo lote

Seguir a ordem territorial do distrito de Lisboa.

**Próximo município:** Azambuja.
