# Inventário documental Markdown — GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-INV-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | INVENTARIO |
| **Fase** | Auditoria documental |
| **Estado** | EM_REVISAO |
| **Versão** | 1.1.1 |
| **SHA-256 (conteúdo canónico)** | c891849a9971013f6a279711c3cda3b4e0444c3a945a0f9bc1f426279593ab37 |
| **Commit de referência (versão anterior)** | [b55de1f609e33e8b7cd190507e23f0d183cd6622](https://github.com/carlos-andrade/GOVERNANCA/commit/b97fa1b4164270b782c1bb04e7023406335b797a) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo e âmbito

Inventariar todos os ficheiros Markdown presentes na árvore Git recursiva da branch `main`, classificar a presença dos elementos centrais do cabeçalho canónico e preparar a normalização controlada. Este inventário cobre ficheiros com extensão `.md`; não avalia ficheiros YAML, JSON, código ou binários.

## Método

- Fonte: árvore Git recursiva do repositório `main`, inspecionada em 2026-10-13.
- Total identificado na árvore Git recursiva da branch `main`, após inclusão do inventário transversal de repositórios: **62 ficheiros Markdown**.
- Critério de conformidade inicial: título Markdown, tabela de metadados `Campo | Valor`, linha SHA-256 canónico e linha de commit de referência.
- Os documentos com campos canónicos foram verificados quanto à presença dos campos; os hashes canónicos dos 11 documentos Markdown da pasta `CABEÇALHO` foram recalculados ou conferidos nesta revisão.
- A classificação é estrutural, não uma aprovação substantiva do conteúdo.
- Ficheiros de modelo, como `CABEÇALHO/MODELO-DOCUMENTO.md`, podem conter marcadores de preenchimento; a conformidade do modelo não torna automaticamente conformes os documentos criados a partir dele.

## Resumo

| Resultado | Quantidade |
|---|---:|
| Ficheiros Markdown inventariados | 62 |
| Com campos canónicos presentes | 62 |
| A normalizar ou avaliar individualmente | 0 |
| Cobertura estrutural do padrão | 100,0% |

## Inventário completo

| Caminho | Resultado da auditoria estrutural |
|---|---|
| `CABEÇALHO/CHECKLIST-VALIDACAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/HISTORICO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/MODELO-DOCUMENTO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/NORMA-CABECALHO-PADRAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/README.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/REGISTO-TIPOS-DOCUMENTAIS.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/REGISTO-APROVACAO-NORMA-1.0.3.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/ROADMAP-ADOCAO-TRANSVERSAL.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/INVENTARIO-DOCUMENTAL.md` | CONFORME — campos canónicos presentes (este inventário) |
| `CABEÇALHO/INVENTARIO-REPOSITORIOS-ABRANGIDOS.md` | CONFORME — inventário transversal da Fase 5 |
| `CABEÇALHO/PLANO-LOTES-NORMALIZACAO.md` | CONFORME — campos canónicos presentes |
| `CABEÇALHO/CLASSIFICACAO-PRE-NORMALIZACAO.md` | CONFORME — campos canónicos presentes |
| `CONSTITUICAO.md` | CABEÇALHO APLICADO — GOV-001 e estado de proposta preservados |
| `README.md` | CABEÇALHO APLICADO — marcadores de automação preservados |
| `WATCHDOG/CARTA-WATCHDOG.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/adapters/aplicacoes/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/adapters/dados/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/adapters/github-actions/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/adapters/infraestrutura/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/adapters/processos/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/arquitetura/arquitetura-geral.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/arquitetura/modelo-de-execucao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/arquitetura/modelo-de-integracao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/docs/configuracao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/docs/instalacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/docs/operacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/normas/classificacao-de-estados.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/normas/evidencias-e-auditoria.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/normas/politica-de-monitorizacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/normas/recuperacao-e-remediacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/normas/seguranca-e-privacidade.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/normas/severidade-e-escalonamento.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/registry/adocao-transversal.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/reports/exemplos/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/reports/modelos/relatorio-de-execucao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/roadmap-de-implementacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/runbooks/incidente-critico.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/runbooks/operacao-de-alertas-e-sla.md` | CABEÇALHO APLICADO — corpo preservado |
| `WATCHDOG/tests/README.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/00-fundamentos/modelo-operacional.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/00-fundamentos/principios-de-adaptacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/00-fundamentos/taxonomia-e-glossario.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/papeis-e-responsabilidades.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/politica-de-conformidade-documental.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/politica-de-decisoes.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/01-governanca/politica-de-excecoes.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/02-ciclo-de-vida/gestao-de-requisitos-e-escopo.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/03-portfolio-e-estrategia/priorizacao-de-portfolio.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/04-arquitetura-e-engenharia/arquitetura-e-padroes.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/04-arquitetura-e-engenharia/controle-de-versao-e-revisao.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/05-dados-e-ia/governanca-de-dados.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/05-dados-e-ia/qualidade-e-linhagem.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/05-dados-e-ia/uso-responsavel-de-ia.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/06-seguranca-e-privacidade/gestao-de-risco.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/06-seguranca-e-privacidade/politica-de-seguranca.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/06-seguranca-e-privacidade/privacidade-e-dados-pessoais.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/07-operacoes-e-resiliencia/continuidade-backup-recuperacao.md` | CABEÇALHO APLICADO — corpo preservado |
| `docs/07-operacoes-e-resiliencia/operacoes-e-observabilidade.md` | CABEÇALHO APLICADO — corpo preservado |
| `standards/status-e-percentual-de-conclusao.md` | CABEÇALHO APLICADO — corpo preservado |
| `templates/projeto/status-do-projeto.md` | CABEÇALHO APLICADO — corpo preservado |

## Achados e limitações

1. Os 11 documentos Markdown de controlo da pasta `CABEÇALHO` contêm os campos SHA-256 e commit de referência. Os hashes canónicos foram recalculados ou conferidos nesta revisão; a validação estrutural não constitui aprovação substantiva.
2. Os restantes 26 ficheiros não têm o conjunto de campos canónicos. Alguns contêm metadados antigos em texto corrido ou tabelas temáticas; esses elementos não equivalem ao cabeçalho normativo.
3. `CONSTITUICAO.md` recebeu o cabeçalho canónico; o ID GOV-001, a versão 1.0.0 e o estado de proposta para revisão foram preservados.
4. Os documentos WATCHDOG incluem cartas, políticas, runbooks, documentação operacional e modelos; devem ser normalizados preservando o conteúdo técnico e os estados reais.
5. L1 foi aplicado a `CONSTITUICAO.md` e `README.md`; L2 a sete documentos de fundamentos e governança; L3 a cinco documentos de ciclo de vida, portefólio e engenharia; L4 a seis documentos de dados, IA, segurança e privacidade. Os 30 documentos restantes não foram alterados. A alteração retroativa deverá preservar o corpo original, usar `N/A — justificação` quando os dados históricos não possam ser comprovados e manter os IDs existentes.
6. A Norma de Cabeçalho v1.0.3 foi formalmente aprovada pelo proprietário em 2026-10-13; esta aprovação não ratifica automaticamente outros documentos nem certifica conformidade substantiva.

## Próxima ação

L1–L7 publicados; hashes canónicos dos 10 documentos WATCHDOG L7 verificados após publicação. Fase 5 iniciada: inventário de repositórios criado e linha de base inicial recolhida para 14 repositórios.

## Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.1 | 2026-10-13 | Ajuste do inventário para incluir o próprio documento; total atualizado para 58 ficheiros | Árvore Git da branch `main` e histórico Git |
| 1.0.2 | 2026-10-13 | Inclusão do plano de lotes e da classificação; total reconciliado para 60 ficheiros | Árvore Git da branch `main` |
| 1.0.3 | 2026-10-13 | Recalculo do SHA-256 canónico e atualização do estado de verificação dos dez documentos da pasta CABEÇALHO | Auditoria canónica dos ficheiros publicados |

| 1.0.4 | 2026-10-13 | Aprovação formal registada e L1 aplicado; inventário reconciliado para 61 ficheiros, 13 com campos canónicos e 48 pendentes | Norma aprovada, registo de aprovação e commits L1 |

| 1.0.5 | 2026-10-13 | L2 aplicado a sete documentos; inventário reconciliado para 61 ficheiros, 20 com campos canónicos e 41 pendentes | Sete commits L2 e validação SHA-256 canónica |

| 1.0.6 | 2026-10-13 | L3 aplicado a cinco documentos; inventário reconciliado para 61 ficheiros, 25 com campos canónicos e 36 pendentes | Cinco commits L3 e validação SHA-256 canónica |

| 1.0.7 | 2026-10-13 | L4 aplicado a seis documentos; inventário reconciliado para 61 ficheiros, 31 com campos canónicos e 30 pendentes | Seis commits L4 e validação SHA-256 canónica |


| 1.0.8 | 2026-10-14 | L5 aplicado a quatro documentos de operações, standards e templates; inventário reconciliado para 61 ficheiros, 35 com campos canónicos e 26 pendentes | Quatro commits L5 e validação SHA-256 canónica |


| 1.0.9 | 2026-10-14 | L6 aplicado a 16 documentos WATCHDOG de carta, arquitetura, normas, documentação e operação; inventário reconciliado para 51 canónicos e 10 pendentes | 16 commits L6 e validação SHA-256 pós-publicação |


| 1.1.0 | 2026-10-14 | L7 aplicado aos dez documentos WATCHDOG restantes; cobertura estrutural do cabeçalho canónico atingiu 61/61 (100%) | Dez commits L7 e validação SHA-256 pós-publicação |


| 1.1.1 | 2026-10-14 | Inventário transversal de repositórios adicionado; total atualizado para 62 documentos Markdown, todos com cabeçalho canónico | CABEÇALHO/INVENTARIO-REPOSITORIOS-ABRANGIDOS.md e validação SHA-256 |
