# Relatório do piloto F3 — STOCKS

| Campo | Valor |
|---|---|
| **ID** | GOV-INT-F3-PILOT-STOCKS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório consumidor** | [carlos-andrade/STOCKS](https://github.com/carlos-andrade/STOCKS) |
| **Tipo documental** | Relatório de validação de piloto |
| **Estado** | PILOTO ACEITE — CONFORMIDADE GLOBAL DESCONHECIDA |
| **Data** | 2026-10-20 |
| **Fonte normativa** | [DEC-GOV-INT-001](DEC-GOV-INTEGRATION-FRAMEWORK-001.md) |
| **PR de integração do consumidor** | [STOCKS #8](https://github.com/carlos-andrade/STOCKS/pull/8) |

## 1. Objetivo

Validar a invocação do workflow reutilizável oficial a partir de um repositório consumidor, em modo estritamente de diagnóstico, sem escrita automática nem substituição dos documentos locais.

## 2. Execução

- Workflow: [GOVERNANCA — piloto F3 (diagnóstico)](https://github.com/carlos-andrade/STOCKS/actions/workflows/governance-integration.yml)
- Execução final verificada após atualização do catálogo v1.1: [run 39481074174](https://github.com/carlos-andrade/STOCKS/actions/runs/39481074174)
- Artefacto do relatório final: [governance-integration-report](https://github.com/carlos-andrade/STOCKS/actions/runs/39481074174/artifacts/12291647106)
- Commit do consumidor executado: `587dfdde3a9ba9c05f908583b55b39407196b642`
- Commit exato da fonte reportado na execução final: `c9be6d5224c7b412aa78a2b1d417b8315e5730f1`
- Perfil: `dados`
- Modo: `diagnostico`
- Resultado do job: `success`
- Estado de conformidade emitido pelo motor: `DESCONHECIDO`

## 3. Evidência do relatório

| Verificação | Resultado | Interpretação |
|---|---|---|
| CFG-002 | PASS | Configuração válida segundo JSON Schema Draft 2020-12 |
| SRC-001 | PASS | Fonte configurada corresponde a `carlos-andrade/GOVERNANCA` |
| Commit de origem | PASS | `source_commit` coincide com o `pinned_ref` fixado |
| Hash da configuração | Registado | SHA-256: `900e1c419c9897b7e80d7562f0413601495781e03594686da36b88578158178c` |
| Hash do esquema | Registado | SHA-256: `c2090d3007509533137af8815d3eee977897ccbc06525c3a599731336241c0fb` |
| Catálogo estrutural v1.1 | PASS limitado | Baseline GOV-STR-001/002/003 e requisitos DAD-STR-001/002 passaram no run 39481074174; catálogo SHA-256 registado. Requisitos semânticos continuam incompletos. |

## 4. Preservação e segurança

- A configuração local seleciona exclusivamente `diagnostico`.
- O workflow reutilizável tem permissão `contents: read` e publica o relatório como artefacto.
- A integração foi proposta na [PR STOCKS #8](https://github.com/carlos-andrade/STOCKS/pull/8), com apenas dois ficheiros novos/modificados para o piloto.
- O motor F2 não implementa alterações ao repositório consumidor; o modo `aplicar` continua bloqueado.
- A PR STOCKS #8 foi integrada por autorização do proprietário em 2026-10-20, commit `4f2650394fd6bee6d86871d05518392f3a00261f`. Isto aceita a integração técnica de diagnóstico, não certifica conformidade global.

## 5. Avaliação dos critérios F3

| Critério | Estado | Evidência/pendência |
|---|---|---|
| Workflow reutilizável invocado num consumidor | PASS | Run 39467662909 |
| Relatório gerado e arquivado | PASS | Artefacto 12286047005 |
| Fonte e versão rastreáveis | PASS | SHA de origem presente no relatório |
| Configuração validada | PASS | CFG-002 |
| Alterações propostas por PR | PASS | STOCKS #8 integrada: commit `4f2650394fd6bee6d86871d05518392f3a00261f` |
| Preservação do conteúdo local | PASS limitado ao escopo da PR | A proposta não substitui os documentos de governança existentes; a aceitação final requer revisão da PR |
| Aceitação da integração técnica | PASS | PR STOCKS #8 integrada após instrução expressa de conclusão |
| Catálogo por perfil | PARCIAL | Baseline estrutural v1.1 executado; requisitos semânticos do domínio continuam por especificar e aprovar. Estado global `DESCONHECIDO`. |
| Distribuição transversal aos oito consumidores | BLOQUEADO | Secret `GOVERNANCA_SYNC_TOKEN` rejeitado; não foi executada propagação |

## 6. Evidência de atualização do catálogo — 2026-10-20

- PR GOVERNANCA #14 integrada: https://github.com/carlos-andrade/GOVERNANCA/pull/14
- Commit de integração: `b24e9580a145b0692abf9ea79aaf0cf35d260f48`
- Execução do piloto com o catálogo: [run 39476495677](https://github.com/carlos-andrade/STOCKS/actions/runs/39476495677)
- Artefacto: [governance-integration-report](https://github.com/carlos-andrade/STOCKS/actions/runs/39476495677/artifacts/12288803976)
- `DAD-STR-001` e `DAD-STR-002`: PASS; `source_commit` coincide com `pinned_ref`; SHA-256 do catálogo registado.
- Estado emitido: `DESCONHECIDO`, por decisão deliberada, pois o catálogo está marcado incompleto e apenas verifica presença estrutural de ficheiros.
- A configuração e o workflow do STOCKS foram atualizados na branch da PR #8 para fixar o commit de origem `b24e9580a145b0692abf9ea79aaf0cf35d260f48`. A PR #8 foi integrada após autorização expressa do proprietário; isto aceita a integração técnica, não a conformidade global.

## 7. Validação adversarial e execução atualizada — 2026-10-20

- Hardening fail-closed integrado na GOVERNANCA pela PR #16, commit `e5a7499d3a8a0877f4fc99774bb604a90f01e6f3`; CI [run 39476819589](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39476819589) passou.
- Foram adicionados testes para catálogo ausente, caminho com traversal e perfil sem definição no catálogo.
- Execução do STOCKS com referência atualizada: [run 39476916364](https://github.com/carlos-andrade/STOCKS/actions/runs/39476916364); artefacto [12289608239](https://github.com/carlos-andrade/STOCKS/actions/runs/39476916364/artifacts/12289608239).
- `source_commit` e `pinned_ref` coincidem em `e5a7499d3a8a0877f4fc99774bb604a90f01e6f3`; CFG-002, SRC-001, DAD-STR-001 e DAD-STR-002 passaram. O estado mantém-se `DESCONHECIDO` porque o catálogo é incompleto.

## 8. Execução final do catálogo v1.1 e aceitação do piloto — 2026-10-20

- Catálogo v1.1 integrado pela PR GOVERNANCA #18, commit `c9be6d5224c7b412aa78a2b1d417b8315e5730f1`; CI [run 39480798454](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39480798454) passou.
- Piloto STOCKS executado após atualização coordenada: [run 39481074174](https://github.com/carlos-andrade/STOCKS/actions/runs/39481074174); artefacto [12291647106](https://github.com/carlos-andrade/STOCKS/actions/runs/39481074174/artifacts/12291647106).
- `source_commit` e `pinned_ref` coincidem em `c9be6d5224c7b412aa78a2b1d417b8315e5730f1`.
- `CFG-002`, `SRC-001`, `GOV-STR-001`, `GOV-STR-002`, `GOV-STR-003`, `DAD-STR-001` e `DAD-STR-002`: PASS.
- Estado `DESCONHECIDO` mantido intencionalmente porque o catálogo continua `complete: false` e não avalia critérios semânticos específicos do domínio.
- PR STOCKS #8 integrada no commit `4f2650394fd6bee6d86871d05518392f3a00261f` após a instrução expressa de concluir o trabalho. O merge aceita o piloto de diagnóstico; não equivale a certificação global.

## 9. Conclusão

O piloto demonstrou a execução técnica do workflow reutilizável, a validação da configuração, a geração do relatório e a rastreabilidade do commit de origem. **O piloto F3 foi aceite no escopo de diagnóstico** e a PR STOCKS #8 foi integrada. A certificação global continua bloqueada por requisitos semânticos ainda não definidos e pela distribuição transversal não autenticada. O bloqueio da distribuição transversal por credencial inválida é independente deste piloto.

Não interpretar o sucesso do job como conformidade do STOCKS.
