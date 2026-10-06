# TURISTURIS — FASE NACIONAL 1 — AUDITORIA TERRITORIAL

**ID:** AUDIT-NACIONAL-001  
**Projeto:** TURISTURIS  
**Título:** Reconciliação da estrutura territorial continental existente  
**Tipo:** Auditoria estrutural  
**Estado:** PASS — reconciliação estrutural  
**Versão:** 1.0  
**Data:** 2026-10-06  
**Função histórica:** primeiro checkpoint da integração nacional, garantindo que a camada territorial existente seja reutilizada sem duplicação antes da integração turística.

## 1. Escopo

Foi comparado o catálogo municipal publicável existente com a estrutura territorial já persistida em:

`CONTINENTE/DISTRITO/`

Fonte canónica de entrada:

`CONTINENTE/DADOS/PUBLICACAO/CATALOGO_MUNICIPIOS_NORMALIZADOS_V1.json`

## 2. Resultado

| Verificação | Resultado |
|---|---:|
| Municípios no catálogo | 278 |
| Municípios na estrutura de distrito | 278 |
| Distritos continentais identificados | 18 |
| Municípios no catálogo sem correspondência estrutural | 0 |
| Municípios estruturais sem correspondência no catálogo | 0 |
| Freguesias inferidas | 0 |
| Dados turísticos promovidos nesta etapa | 0 |

A comparação considerou a normalização do separador de palavras usado nos diretórios (hífen) contra o espaço usado no catálogo. Não houve perda ou acréscimo de municípios.

## 3. Artefato produzido

`CONTINENTE/DADOS/PUBLICACAO/TERRITORIO_CONTINENTE_RECONCILIADO_V1.json`

- `record_count = 278`
- `distrito_count = 18`
- `freguesia = null` em todos os registos
- estado estrutural: `ESTRUTURA_RECONCILIADA`
- data de verificação: `2026-10-06`

## 4. Regra de não inferência

A FASE NACIONAL 1 não tenta determinar freguesias a partir do município.

A ausência de freguesia não é tratada como erro. A freguesia só será preenchida quando houver fonte adequada e identificação inequívoca.

## 5. Regra de não duplicação

A nova camada não substitui o catálogo municipal existente. Ela cria uma camada territorial reconciliada para servir de referência às fases seguintes.

## 6. Conclusão

**PASS.**

Os 278 municípios continentais já existentes foram reconciliados com os 278 diretórios municipais estruturados em 18 distritos, sem divergência estrutural.

A próxima etapa é integrar os dados turísticos existentes sobre esta camada, começando pelos **68 pontos turísticos publicáveis**, sem duplicar os registos canónicos já existentes.

## 7. Persistência

Esta auditoria é submetida através de:

**branch → PR → PR Gate → merge**

Não há publicação direta no `main` nem alteração direta do SITE.
