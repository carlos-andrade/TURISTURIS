# Registo de tipos documentais

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-REG-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | REGISTO |
| **Fase** | Validação do padrão |
| **Estado** | PROPOSTA PARA VALIDAÇÃO |
| **Versão** | 1.0.2 |
| **SHA-256 (conteúdo canónico)** | 90d242e204022a4e61265f547afed7d508779cf7d7f2d4fdaef3ba0f0275e919 |
| **Commit de referência (versão anterior)** | [414a12843bb528ba9eedfe2322772d71f3e5c597](https://github.com/carlos-andrade/GOVERNANCA/commit/414a12843bb528ba9eedfe2322772d71f3e5c597) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Autoridade superior** | [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Tipos documentais

| Tipo | Uso | Prefixo sugerido |
|---|---|---|
| PROMPT | Instrução versionada para execução por pessoa ou sistema | PROMPT |
| CARTA | Mandato, princípios e autoridade de um domínio | CARTA |
| NORMA | Regra comum de cumprimento obrigatório após aprovação | NORMA |
| POLITICA | Regras e responsabilidades de governança | POL |
| ESPECIFICACAO | Requisitos e comportamento esperado | SPEC |
| PLANO | Sequência de trabalho, marcos e dependências | PLAN |
| RELATORIO | Resultado de análise, auditoria ou execução | REL |
| PROCEDIMENTO | Passos operacionais reproduzíveis | PROC |
| RUNBOOK | Resposta operacional a uma condição ou incidente | RUN |
| REGISTO | Estado estruturado ou histórico de decisões/artefactos | REG |
| MODELO | Estrutura reutilizável de documento ou artefacto | MOD |
| CODIGO | Código-fonte e componentes executáveis | CODE |
| TESTE | Teste unitário, integração ou aceitação | TEST |
| EVIDENCIA | Artefacto que comprova execução ou decisão | EVD |
| DECISAO | Decisão formal, incluindo ADR quando aplicável | DEC |

Os prefixos são sugestões. Se um projeto já tiver convenção aprovada, manter a convenção existente e documentar o mapeamento. Não alterar IDs históricos apenas para uniformizar nomenclatura.

## Regras de identificação

- O ID é estável, único e não reutilizável.
- O ID não substitui o título, a versão nem o estado.
- Referências devem apontar para artefactos existentes.
- Documentos derivados devem referenciar origem e autoridade superior.
- Documentos substituídos passam a `DEPRECADO` e apontam para o sucessor, quando exista.
- Documentos rejeitados não devem ser usados como autoridade normativa.
