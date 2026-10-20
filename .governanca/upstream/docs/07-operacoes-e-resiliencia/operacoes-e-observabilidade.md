# Operações e observabilidade

| Campo | Valor |
|---|---|
| **ID** | GOV-OPS-OBS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | NORMA_OPERACIONAL |
| **Fase** | Operações e observabilidade |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 858057b350092da977125c6a60029799089a9c8f615b2323973ace02d69321d3 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/07-operacoes-e-resiliencia/operacoes-e-observabilidade.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Todo o serviço produtivo tem owner operacional, dependências, métricas, logs, alertas acionáveis, runbooks, suporte e escalonamento. Minimizar telemetria e retenção ao necessário.

Perguntas mínimas: como confirmar o serviço do ponto de vista do utilizador? Que falha gera alerta e quem responde? Como distinguir falha de serviço/dependência/telemetria? Que ações seguras pode o responsável executar? Qual o procedimento manual se a automação falhar?

Para serviços contínuos, definir SLIs/SLOs e janela. Não inventar SLAs contratuais. Alertas devem ser acionáveis e ruído persistente deve ser corrigido.