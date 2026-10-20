# Operação de alertas WATCHDOG — confirmação, SLA e escalonamento

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-RUN-ALERT-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | RUNBOOK |
| **Fase** | WATCHDOG — alertas e SLA |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 5b38c23d743b1254707c812e63e6d6a5b5bac8e2dacb95f5539afdc3f7cd230d |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/runbooks/operacao-de-alertas-e-sla.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Estado:** procedimento preparado para adoção; tempos abaixo são propostas provisórias e não constituem SLA aprovado.  
**Âmbito inicial:** piloto WATCHDOG do repositório `carlos-andrade/B3` e futura adoção transversal.

## 1. Severidade operacional

| Severidade | Exemplos no piloto | Ação proposta | Tempo-alvo provisório |
|---|---|---|---|
| SEV-1 — Crítico | Falha de controlo crítico de integridade; perda simultânea do monitor e do canal de alerta; risco imediato de dados incorretos em uso operacional | Notificar primário e suplente por canal independente; preservar evidências; iniciar contenção autorizada | Confirmação em 15 min; escalonamento imediato se não houver confirmação |
| SEV-2 — Alto | Dataset obrigatório STALE/UNKNOWN; falha repetida de ingestão ou validação; ausência de heartbeat do monitor principal | Notificar primário; acionar suplente se não confirmado; abrir incidente rastreável | Confirmação em 1 h; escalonamento em 2 h |
| SEV-3 — Moderado | Falha isolada de workflow não crítico; degradação limitada sem impacto confirmado | Registar, classificar e atribuir responsável | Confirmação no mesmo dia útil |
| SEV-4 — Informativo | Aviso preventivo, tendência ou melhoria sem falha atual | Registar e rever na rotina operacional | Próxima revisão planeada |

**Importante:** os tempos são um ponto de partida para decisão. Não devem ser apresentados como SLA contratual nem ativados como política aprovada sem confirmação do proprietário.

## 2. Ciclo obrigatório de um alerta

1. **Detetar:** guardar identificador, controlo, severidade, timestamps UTC, estado, fonte e ligação para evidência.
2. **Deduplicar:** atualizar o incidente aberto da mesma classe/controlo; não criar uma nova issue por cada repetição sem mudança material.
3. **Notificar:** usar o canal primário definido no registo do sistema.
4. **Confirmar receção:** o responsável deve comentar com `ACK YYYY-MM-DDThh:mmZ — responsável — ação inicial`.
5. **Escalonar:** se não houver ACK dentro do tempo aprovado, notificar o suplente e usar o canal alternativo independente.
6. **Remediar:** executar apenas ações autorizadas; preservar logs, manifestos e hashes.
7. **Verificar recuperação:** executar de novo o controlo e verificar a evidência, não apenas o estado do workflow.
8. **Encerrar:** registar causa, impacto, ação corretiva, prevenção de recorrência, responsável e ligação para a execução de recuperação.

## 3. Regras para o piloto B3

- A issue `[WATCHDOG] Atualidade de dados — B3` não deve fechar automaticamente só porque uma execução posterior passou. É necessária revisão da causa e confirmação da recuperação.
- A issue `[WATCHDOG] Execuções desfavoráveis — B3` representa triagem de falhas da janela móvel de 24 horas. Cada execução listada deve ser classificada como incidente real, falha de desenvolvimento esperada, cancelamento operacional ou falso positivo, com evidência.
- `UNKNOWN` não significa saudável. O workflow de atualidade falha agora tanto em `STALE` como em `UNKNOWN`.
- O heartbeat confirma execução do monitor; não confirma a qualidade dos datasets.
- GitHub Issues são um registo rastreável, mas não comprovam notificação externa, receção ou SLA. A aceitação de alerta ponta a ponta depende de teste do canal.

## 4. Registo mínimo por sistema

Antes de declarar o controlo operacional, registar:
- responsável primário e suplente (identificadores reais);
- canal primário e canal alternativo independente;
- severidade e condição de abertura;
- deduplicação e regra de repetição;
- tempo aprovado de ACK e de escalonamento;
- procedimento de recuperação;
- evidência de teste de alerta, ausência de ACK, escalonamento e recuperação;
- data e identidade da aprovação.

## 5. Aceitação e fecho

| Teste | Evidência exigida | Estado |
|---|---|---|
| Alerta normal chega ao canal primário | Registo com timestamp UTC | PENDENTE |
| Responsável confirma receção | ACK rastreável | PENDENTE |
| Ausência de ACK aciona suplente | Evidência do escalonamento | PENDENTE |
| Canal primário indisponível usa alternativa | Evidência de entrega alternativa | PENDENTE |
| Repetições são deduplicadas | Uma issue incidente atualizada, sem tempestade de duplicados | PENDENTE |
| Recuperação é confirmada | Execução de controlo e evidência saudável | PENDENTE |
| Proprietário aprova tempos e responsáveis | Aprovação registada | PENDENTE |

**Critério de fecho:** nenhum item pode ser marcado como concluído apenas porque existe documentação ou porque uma GitHub Action terminou com sucesso.
