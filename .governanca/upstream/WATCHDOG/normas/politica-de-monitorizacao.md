# Política de monitorização

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-MON-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | POLITICA |
| **Fase** | WATCHDOG — monitorização |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 6ce25e852c3ab1cf0b3ede3e8462b65ee6906ba20bdb7746aa5fd74a55bd6ab7 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/normas/politica-de-monitorizacao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Obrigatoriedade

Cada projeto sob a GOVERNANCA deve identificar os objetos monitorizados, controlos aplicáveis, responsáveis, frequência, limites, evidências e resposta. A profundidade é proporcional ao risco; controlos legais, contratuais ou críticos não podem ser omitidos sem autoridade legítima.

## Requisitos por controlo

Cada controlo declara: ID, objetivo, âmbito, proprietário, criticidade, tipo de verificação, critério de sucesso, frequência, timeout, fonte de evidência, validade da evidência, destinatários, ação em caso de falha e procedimento de recuperação.

## Qualidade dos sinais

Os resultados devem ser autenticados quando possível, datados em UTC, rastreáveis à origem e protegidos contra alteração indevida. Resultados antigos ou sem origem válida são inválidos para declarar sucesso.

## Estados permitidos

`PASS`, `WARN`, `FAIL`, `UNKNOWN`. Estado de incidente e severidade são campos separados. A transição para recuperação exige nova verificação satisfatória.

## Revisão

Rever inventário e critérios em mudanças materiais, incidentes, alterações de risco e revisão periódica definida pelo proprietário.
