# Roadmap de implementação do WATCHDOG

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-ROADMAP-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | ROADMAP |
| **Fase** | WATCHDOG — implementação |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 2a5f3c53a20d7cec74e494e658a85c12980880fdd6748f2396998599ba0e7842 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/roadmap-de-implementacao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e [Norma de cabeçalho](../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Atualizado:** 2026-10-13  
**Estado global:** MVP central validado; piloto B3 em expansão, ainda não certificado para operação universal 24×7.

## Fase 1 — Padrão central e motor local

**Estado: concluída para o MVP.**

- Carta WATCHDOG, política, estados, severidade, evidências e segurança documentados.
- Contratos JSON, inventário inicial, motor de validação e testes unitários criados.
- Workflow central de validação executado com sucesso.

## Fase 2 — Piloto de monitorização de workflows

**Estado: implementada; testes de ponta a ponta concluídos para evidências e alertas GitHub.**

- Monitor B3 a cada 15 minutos e análise das últimas 24 horas, com paginação da API até ultrapassar o corte temporal (corrigida a limitação anterior de apenas 100 execuções). O relatório agora inclui contagem total e agrupamento de falhas por workflow; a avaliação de 2026-10-13 identificou concorrência de publicação como causa dominante em REC-001 e na auditoria. A correção transversal está em execução e ainda não foi confirmada no main.
- Relatórios JSON/Markdown publicados como artefactos com retenção configurada de 30 dias.
- Issue de alerta criada/atualizada quando são detetadas execuções desfavoráveis.
- Validação do inventário e da configuração do monitor em GitHub Actions.

Limites: os artefactos não são armazenamento imutável; issues não confirmam que um responsável recebeu ou reconheceu o alerta; o monitor não deteta autonomamente a sua própria falha.

## Fase 3 — Atualidade de dados

**Estado: implementação inicial e primeira execução concluídas; calibração por proprietário pendente.**

- Catálogo explícito para BCB SGS 432, 11, 12, 1 e 433, B3 BDI DailyAverageStocks e manifesto COTAHIST 2026.
- Avaliação da idade baseada em data de observação declarada.
- UNKNOWN quando a data de observação não existe; a data de ingestão não é usada como substituto.
- Workflow agendado, testes, relatório JSON/Markdown, artefacto de 30 dias e issue de alerta para datasets fora do limite.

Primeira avaliação real (2026-10-13): 5 PASS, 1 STALE, 1 UNKNOWN. O monitor detetou BDI DailyAverageStocks em 2026-09-22, com 21 dias de idade, e abriu uma issue. O pipeline de captura foi corrigido para procurar a última data disponível até sete dias para trás, validar a resposta antes de gravar, preservar SHA-256 e não sobrescrever divergências. A captura encontrou dados BDI de 2026-10-09. A data de observação COTAHIST anual foi documentada com proveniência para o manifesto de qualidade NORMALIZED, e o catálogo passou a monitorizar também os manifestos COTAHIST diários. A reavaliação posterior resultou em **8 PASS, 0 STALE, 0 UNKNOWN**. Os oito controlos ficaram dentro dos limites configurados, mas os limiares estão marcados como PROVISIONAL e ainda carecem de aprovação pelos proprietários.

Foi criada uma [matriz de revisão e aprovação dos limiares](https://github.com/carlos-andrade/B3/blob/main/WATCHDOG/limiares-provisorios-revisao.md), com os oito controlos, perguntas de decisão e campos para registar proprietário, decisão, valor e justificação. A matriz não altera os limiares nem representa aprovação.

Critério de saída: o proprietário deve confirmar a semântica e aprovar cada limite, e a recuperação deve ser comprovada após atualizações futuras. A issue de atualidade permanece aberta para revisão humana, embora a última execução não tenha encontrado STALE ou UNKNOWN.

## Fase 4 — Alertas operacionais e resiliência

**Estado: procedimento documentado; implementação e aceitação operacional pendentes.**

- Runbook de [operação de alertas, confirmação e SLA proposto](runbooks/operacao-de-alertas-e-sla.md) criado.
- O runbook define severidades, tempos provisórios, ACK, escalonamento, deduplicação e critérios de fecho.
- Falta aprovar os tempos, nomear responsáveis primário/suplente, configurar canais reais e comprovar entrega, ausência de ACK, escalonamento e recuperação.
- Foi criado o [gate único de aceitação final do piloto B3 — issue #9](https://github.com/carlos-andrade/B3/issues/9), atribuído ao proprietário, reunindo decisões humanas e testes externos necessários.
- Issue #7 no piloto B3 contém execuções desfavoráveis que exigem triagem individual; não deve ser encerrada apenas por existir um relatório.

## Fase 5 — Supervisão independente

**Estado: hooks de heartbeat preparados no piloto B3; ativação externa pendente. Bloqueador para alegações de monitorização 24×7.**

- Escolher e configurar serviço externo independente do GitHub Actions monitorizado.
- Configurar as secrets `WATCHDOG_HEARTBEAT_WORKFLOWS_URL` e `WATCHDOG_HEARTBEAT_DATA_URL` conforme o [guia B3](https://github.com/carlos-andrade/B3/blob/main/WATCHDOG/heartbeat-supervisor-externo.md).
- Detetar falta de heartbeat e falha do pipeline de monitorização.
- Testar o mecanismo com falhas simuladas e registar evidências.
- Definir responsável e canal de contingência.

## Fase 6 — Integridade e reconciliação de dados

**Estado: planeada.**

- Integrar hashes, manifests, atualidade, cardinalidade e reconciliação para COTAHIST, BCB SGS e BDI.
- Distinguir falha de ingestão, atraso da fonte, lacuna de calendário e falha de validação.
- Preservar proveniência e evitar certificação baseada apenas em sucesso do workflow.

## Fase 7 — Adoção transversal

**Estado: inventário inicial criado; adoção por repositório pendente.**

- [Registo de adoção transversal](registry/adocao-transversal.md) criado a partir de inspeção dos repositórios prioritários.
- B3 permanece piloto com aceitação pendente.
- BLOOMBERG_MAIL já tem WATCHDOG próprio; o supervisor executa testes determinísticos e valida evidência histórica, mas não foi certificado como operação 24×7 independente. Foi corrigido o cancelamento de execução ativa e falta confirmar a execução após a alteração.
- TURISTURIS tem 30 workflows e requer adaptador específico por fase; não copiar o monitor B3 sem mapear contratos e dependências.
- Os restantes repositórios estão pendentes de inspeção e aceitação individual.
- Exigir workflow aprovado, evidência e responsável antes de marcar integração como operacional.

## Critérios de encerramento

O WATCHDOG só pode ser declarado operacional num âmbito quando os controlos obrigatórios estão inventariados, os resultados têm evidência válida, alertas foram testados ponta a ponta, a falha do próprio monitor é detetável independentemente, a retenção/acesso estão definidos e o proprietário aprovou formalmente a aceitação.
