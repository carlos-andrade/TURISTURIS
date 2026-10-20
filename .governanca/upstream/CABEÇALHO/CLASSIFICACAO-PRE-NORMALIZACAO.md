# Classificação pré-normalização documental — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-CLASS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | RELATORIO_AUDITORIA |
| **Fase** | Classificação não destrutiva |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a73731197c2689561e976834904896f61b9e451420b04703d224257e3a89c521 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) e [inventário](INVENTARIO-DOCUMENTAL.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Resultado

Foram examinados de forma não destrutiva os 50 ficheiros Markdown pendentes do inventário: 24 documentos centrais e 26 documentos WATCHDOG. Esta classificação não altera os ficheiros auditados, não ratifica a norma e não significa que os controlos descritos estejam implementados.

## Achados e tratamento obrigatório

- `CONSTITUICAO.md`: já tem ID `GOV-001`, versão `1.0.0` e estado de proposta para revisão. Preservar a autoridade e não presumir ratificação.
- `README.md`: contém o estado global e os marcadores `GOVERNANCA_STATUS_START/END`, usados por automação. Preservar o bloco integralmente.
- `WATCHDOG/CARTA-WATCHDOG.md`: já tem ID `GOV-WD-001`, versão `1.0.0` e estado de proposta operacional. Preservar o estado.
- `WATCHDOG/README.md`, `WATCHDOG/registry/adocao-transversal.md` e `WATCHDOG/roadmap-de-implementacao.md`: distinguem fases de implementação e limites operacionais; não converter planeamento ou inspeção em prova de produção.
- `WATCHDOG/adapters/*/README.md`: vários adaptadores estão explicitamente planeados; não os marcar como implementados.
- `WATCHDOG/runbooks/operacao-de-alertas-e-sla.md`: tempos indicados são provisórios, não SLA aprovado.
- `standards/status-e-percentual-de-conclusao.md`: o título é normativo; o estado e a autoridade de aprovação precisam de confirmação, sem inferência.
- `templates/projeto/status-do-projeto.md` e `WATCHDOG/reports/modelos/relatorio-de-execucao.md`: preservar placeholders; não preencher como dados reais.
- Os restantes documentos centrais e WATCHDOG têm títulos e conteúdo temático, mas não apresentam todos os campos uniformes do cabeçalho proposto. As tabelas temáticas, os campos operacionais e os estados locais não substituem automaticamente a tabela normativa.

## Regras para a próxima fase

1. Preservar IDs e metadados legados verificáveis.
2. Não inventar IDs, aprovadores, datas de vigência, estados de aprovação ou referências históricas.
3. Usar `N/A — justificação` ou pendência explícita quando um dado não for demonstrável.
4. Tratar `CONSTITUICAO.md` separadamente por ser autoridade superior.
5. Validar diffs, links e SHA-256 canónico após cada publicação.
6. Atualizar inventário e roadmap somente após a verificação do resultado publicado.

## Bloqueio

A classificação não destrutiva está concluída. A normalização retroativa permanece bloqueada até aprovação formal explícita da versão exata da norma. A próxima execução após esse gate começa por `CONSTITUICAO.md` e `README.md`, com validação individual antes de avançar.
