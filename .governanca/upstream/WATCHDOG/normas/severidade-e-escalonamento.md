# Severidade e escalonamento

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-SEV-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | NORMA |
| **Fase** | WATCHDOG — severidade e escalonamento |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 450c701504c4cebf9f3b2fbc46624243cb5c878229d37364db7d28450bb5fa5e |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/normas/severidade-e-escalonamento.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Níveis recomendados

- **SEV-1 — Crítico:** risco imediato para segurança, integridade, continuidade ou obrigação crítica. Notificação imediata e escalonamento para responsável e suplente.
- **SEV-2 — Alto:** impacto significativo ou controlo prioritário falhado. Resposta urgente dentro do SLA definido pelo proprietário.
- **SEV-3 — Moderado:** degradação localizada, risco limitado ou incumprimento não crítico. Tratamento no prazo operacional acordado.
- **SEV-4 — Baixo/Informativo:** aviso preventivo, tendência ou melhoria.

Os tempos de resposta devem ser definidos por serviço e risco, não presumidos globalmente. Cada regra deve identificar destinatário primário, suplente, canal alternativo, condição de escalonamento e confirmação de receção.

## Ciclo de alerta

Detetar → deduplicar → notificar → confirmar receção → escalar se necessário → registar decisão → verificar recuperação → encerrar com evidência.

Alertas críticos não podem depender exclusivamente do mesmo sistema monitorizado.
