# Especificação F1 — Contrato de integração da GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-INT-SPEC-001 |
| **Projeto** | GOVERNANÇA |
| **Tipo documental** | ESPECIFICAÇÃO TÉCNICA |
| **Estado** | F1 — ESPECIFICAÇÃO CONCLUÍDA; CI aprovada |
| **Versão** | 1.0.0 |
| **Data** | 2026-10-20 |
| **Decisão de origem** | [DEC-GOV-INT-001](DEC-GOV-INTEGRATION-FRAMEWORK-001.md) |
| **Esquema canónico** | [governanca-config.schema.json](../../schemas/governanca-config.schema.json) |
| **Responsável** | Proprietário do repositório GOVERNANCA |

## 1. Objetivo

Definir o contrato mínimo, estável e verificável usado para invocar a Governança num repositório consumidor. Esta especificação encerra a Fase F1 quando o esquema e os testes associados passarem na CI. Não declara concluídas as fases de implementação, piloto, expansão ou atualização contínua.

## 2. Localização e formato

Cada repositório integrado pode declarar a configuração em `.governanca/config.yml`. O ficheiro usa YAML e deve conter o objeto raiz `governanca`. A validação normativa é definida pelo JSON Schema 2020-12 em `schemas/governanca-config.schema.json`.

O leitor de configuração deve rejeitar propriedades desconhecidas, tipos incorretos, valores não enumerados e violações das constantes. Não deve corrigir silenciosamente configurações inválidas.

## 3. Contrato mínimo

| Campo | Obrigatório | Valores/condição | Finalidade |
|---|---|---|---|
| `fonte` | Sim | `carlos-andrade/GOVERNANCA` | Identifica a fonte oficial única. |
| `modo` | Sim | `diagnostico`, `aplicar`, `auditar` | Declara a intenção da execução. |
| `perfil` | Sim | `automatico`, `generico`, `dados`, `trading`, `aplicacao`, `documentacao`, `turismo`, `watchdog` | Determina o conjunto de requisitos a avaliar. |
| `exigir_pull_request` | Sim | Sempre `true` | Impede alterações diretas à branch principal como mecanismo normal de aplicação. |
| `preservar_ficheiros_existentes` | Sim | Sempre `true` | Protege ficheiros locais contra substituição automática. |
| `auditoria` | Sim | Sempre `obrigatoria` | Exige evidências e relatório de execução. |
| `ref` | Não | String não vazia | Fixa tag, branch ou commit de origem para reprodução. |

O esquema contém valores por defeito informativos. O motor deve materializar e registar os valores efetivos; não deve assumir que todos os validadores de JSON Schema aplicam automaticamente os valores `default`.

## 4. Modos de execução

- **`diagnostico`** — somente leitura. Inspeciona, compara e reporta; não escreve no repositório consumidor, não cria branches e não abre Pull Requests.
- **`aplicar`** — prepara alterações isoladas numa branch e propõe-as por Pull Request. Não faz merge automático. Até existir aprovação e evidência, o resultado não significa conformidade.
- **`auditar`** — verifica estado e evidências existentes, produzindo resultados sem alterar o código do projeto.

O modo predefinido recomendado é `diagnostico`. Uma execução sem modo explícito é inválida no contrato mínimo; a interface que gera configurações pode inserir o valor recomendado antes de validar.

## 5. Exemplo canónico

```yaml
governanca:
  fonte: carlos-andrade/GOVERNANCA
  modo: diagnostico
  perfil: automatico
  exigir_pull_request: true
  preservar_ficheiros_existentes: true
  auditoria: obrigatoria
```

## 6. Resultado e estados

Toda execução futura do motor deve emitir um relatório estruturado que identifique, no mínimo:

- repositório de destino e instante da execução;
- modo e perfil efetivos;
- commit/ref e versão das regras oficiais;
- hashes dos artefactos normativos consumidos;
- requisitos avaliados, resultado e evidências por requisito;
- ficheiros lidos e, quando aplicável, alterações propostas;
- testes executados e respetivos resultados;
- bloqueios, exceções, pendências e próxima ação.

Estados globais de conformidade: `CONFORME`, `CONFORME_COM_PENDENCIAS`, `NAO_CONFORME` e `DESCONHECIDO`. Sem evidência suficiente, o estado é `DESCONHECIDO`; uma falha crítica conduz a `NAO_CONFORME`.

## 7. Segurança e integridade

1. A fonte oficial é `carlos-andrade/GOVERNANCA`; não aceitar uma fonte alternativa através da configuração básica.
2. A execução deve registar o commit exato, mesmo quando a configuração aponta para uma branch ou tag.
3. Segredos e tokens nunca devem constar da configuração versionada, dos logs ou do relatório.
4. Falhas de rede, autenticação, integridade, esquema ou requisitos bloqueantes devem falhar em segurança.
5. `diagnostico` e `auditar` não podem alterar ficheiros do consumidor.
6. `aplicar` deve usar alterações isoladas e Pull Request, preservando conteúdo local por defeito.
7. Alterações de segurança, dados, permissões, migrações ou alto impacto exigem aprovação humana explícita.

## 8. Critérios de aceitação da F1

- [x] Contrato mínimo e modos de execução documentados.
- [x] Fonte oficial, perfis, estados e controlos de segurança definidos.
- [x] Esquema JSON Schema versionado.
- [x] Exemplo canónico consistente com o esquema.
- [x] Testes do esquema e exemplos aprovados na CI ([run 39459837269](https://github.com/carlos-andrade/GOVERNANCA/actions/runs/39459837269)).
- [x] Pull Request da F1 integrada em `main` ([PR #5](https://github.com/carlos-andrade/GOVERNANCA/pull/5), commit `3904c00bd80786d3e8a64d2beab1d076b70410a8`).

A F1 só deve ser declarada concluída depois de os dois últimos critérios serem confirmados por evidência. F2 começa depois disso e implementa o motor, não apenas a configuração.

## 9. Limites explícitos

Esta especificação não implementa o motor de governança, não instala automaticamente a configuração em consumidores, não certifica repositórios e não resolve as credenciais pendentes do mecanismo de distribuição transversal. Esses itens pertencem às fases seguintes ou a bloqueios operacionais separados.
