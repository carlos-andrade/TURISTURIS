# Norma — Barra de estado e percentual de conclusão

| Campo | Valor |
|---|---|
| **ID** | GOV-STD-STATUS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | NORMA |
| **Fase** | Standards e métricas de projeto |
| **Estado** | APROVADO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | 4469267eca0e42d1c0d6e28b38bff3c72ee10797956d9f27237772b27baaa992 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Carlos Andrade — aprovação expressa do modelo visual e dos critérios em 2026-10-17 |
| **Origem** | Conteúdo existente em `standards/status-e-percentual-de-conclusao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e [Norma de cabeçalho](../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo
Todo projeto deve expor, desde a sua abertura até ao encerramento, uma barra de estado e um percentual de conclusão calculados por evidências verificáveis. A regra aplica-se a projetos de software, dados, conteúdo, infraestrutura, investigação, operações e projetos híbridos.

## Modelo de progresso (100 pontos)

| Fase | Peso | Evidência mínima para contabilizar |
|---|---:|---|
| **Início** | 20 pontos | Objetivo e problema definidos (5); responsável e partes interessadas identificados (3); escopo e exclusões registados (4); riscos e dependências iniciais avaliados (4); critérios de aceitação e plano aprovados (4). |
| **Meio** | 60 pontos | Entregáveis executados contra o plano (até 30); requisitos e decisões rastreáveis (10); testes/revisões proporcionais ao risco (10); documentação e evidências atualizadas (5); desvios e riscos tratados ou formalmente aceites (5). |
| **Fim** | 20 pontos | Critérios de aceitação demonstrados (8); validação/revisão final aprovada (4); entrega/publicação e operação ou destino final confirmados (3); documentação e transferência de conhecimento concluídas (2); aprovação de encerramento e lições aprendidas registadas (3). |

Os pontos de cada item só são atribuídos quando a respetiva evidência está registada e verificável. Itens não aplicáveis devem ser justificados, aprovados pelo responsável de governança do projeto e redistribuídos dentro da mesma fase; não podem desaparecer silenciosamente do denominador.

## Cálculo e barra

- **Percentual = pontos comprovados ÷ 100 × 100.** Não estimar progresso com base em tempo decorrido, esforço percebido ou quantidade de commits.
- Usar uma barra de 20 segmentos. Cada segmento representa 5 pontos percentuais. Arredondar a barra para baixo; apresentar o percentual numérico exato ao lado.
- Exemplo: `Progresso: 65%  [█████████████░░░░░░░]`
- O percentual não pode diminuir por trabalho concluído que continua válido; pode diminuir apenas se evidência for invalidada, o escopo aprovado mudar ou uma entrega for reprovada. Registar motivo, data e decisão.
- O percentual mede **conclusão comprovada do escopo aprovado**, não qualidade global, probabilidade de sucesso nem cumprimento de prazo. Apresentar separadamente saúde/prazo/risco quando necessário.
- Um projeto só pode atingir **100% — Concluído** após cumprir os critérios da fase Fim e obter aprovação explícita de encerramento. 100% não significa ausência de defeitos futuros; significa que o escopo e os deveres de encerramento acordados foram satisfeitos.
- Projeto suspenso, bloqueado ou cancelado mantém o percentual comprovado e recebe estado próprio. Cancelado não equivale a 100%.

## Estados obrigatórios

- **Não iniciado — 0%:** ainda não há trabalho aceite como concluído.
- **Em início — 1–20%:** definição e autorização inicial.
- **Em execução — 21–79%:** produção dos entregáveis.
- **Em finalização — 80–99%:** validação, entrega e encerramento.
- **Concluído — 100%:** critérios finais aprovados.
- **Bloqueado / Suspenso / Cancelado:** estado adicional obrigatório quando aplicável, sem alterar artificialmente o percentual.

O nome da fase deriva dos critérios e gates efetivamente atingidos; não é inferido apenas do número. Se houver conflito, prevalecem as evidências e o gate aprovado.

## Frequência de atualização

Atualizar a barra a cada marco/gate, alteração material de escopo, aprovação/reprovação, bloqueio, release ou encerramento; em projetos ativos, rever pelo menos semanalmente. Cada atualização regista data, percentual anterior/novo, evidências, responsável e motivo.

## Onde apresentar

A barra deve estar:
1. no README ou painel principal do repositório do projeto;
2. no registo/charter do projeto;
3. no relatório de estado periódico, quando existir.

Projetos pequenos podem manter um único registo simples. Projetos grandes podem automatizar o cálculo, mas a automação só é considerada ativa após implementação, teste e validação dos dados de entrada.

## Integridade

- Não declarar uma percentagem sem lista de critérios e evidências.
- Não usar a percentagem como substituto de testes, auditoria, aprovação, gestão de risco ou aceitação do utilizador.
- Manter histórico das alterações e identificar quem atualizou/aprovou.
- A governança central define a regra; cada repositório de projeto mantém o seu valor e evidências.

## Implementação automatizada no GOVERNANCA

No repositório GOVERNANCA, a fonte canónica do painel é `registry/status-do-projeto.json`. O ficheiro `automation/sync_project_status.py` valida os dados e gera o bloco delimitado por `<!-- GOVERNANCA_STATUS_START -->` e `<!-- GOVERNANCA_STATUS_END -->` no `README.md`.

O workflow `.github/workflows/sync-project-status.yml` é acionado por alterações ao registo canónico na branch `main` ou manualmente via `workflow_dispatch`. Antes de escrever, executa os testes automatizados, valida as regras de pontuação e verifica que o README fica sincronizado. Se houver alteração, publica o README num commit do bot. O commit do bot altera apenas o README, não o registo de origem, evitando ciclos de execução.

**Procedimento para mudar o status:** editar `registry/status-do-projeto.json` na branch `main`, atualizar `updated_at`, ajustar os pontos apenas com evidências, indicar próximo marco/bloqueios e anexar evidências verificáveis. Depois, confirmar a execução do workflow e a atualização do README. Uma execução falhada significa que a sincronização não foi confirmada; corrigir a causa antes de comunicar o novo status como publicado.

**Limites:** o mecanismo mantém sincronizado o painel deste repositório. Não altera automaticamente os README de outros repositórios. A adoção noutros projetos exige instalação e teste do mecanismo em cada repositório, com permissões e regras de branch compatíveis.


## 13. Scorecard por critério e barra visual moderna

A versão 1.1.0 exige que a pontuação seja demonstrável por critério, não apenas declarada como total de fase. O registo canónico deve manter, para cada critério: ID único, descrição, pontos máximos, pontos atribuídos e lista de evidências HTTP(S). Critério com pontos atribuídos sem evidência é inválido.

- A soma dos pontos máximos dos critérios deve ser exatamente 20 para Início, 60 para Meio e 20 para Fim.
- Os pontos atribuídos por fase devem ser iguais à soma de `earned_points` dos seus critérios.
- Os pontos atribuídos a cada critério devem ser inteiros entre zero e o máximo definido.
- Critérios parcialmente cumpridos podem receber pontos parciais apenas quando o critério e o método de avaliação o justificarem; a justificação deve constar da evidência ou do registo.
- O total é a soma dos pontos comprovados. A barra de 20 segmentos continua a representar 5 pontos percentuais por segmento, arredondada para baixo.
- A barra visual SVG é um artefacto gerado a partir do mesmo registo canónico que gera o painel Markdown. Não manter números independentes dentro do SVG.
- A validação automatizada deve falhar quando o registo, a barra Markdown e o SVG divergirem.
- O painel deve mostrar o percentual comprovado, estado, fase, pontos por fase, número de bloqueios, data da revisão, próximo marco e links de evidência.
- A data de atualização do registo não prova, por si só, que todos os controlos externos foram revalidados. A nota de revisão deve delimitar o que foi efetivamente verificado e quais dependências continuam pendentes.
- Alterações de metodologia ou correções de pontuação exigem registo da razão e da evidência que sustenta a alteração. Uma queda percentual nunca deve ser ocultada; deve ser explicada no histórico.

## 14. Histórico de alterações

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.1.0 | 2026-10-17 | Scorecard por critério com evidências, validação da soma e geração sincronizada de painel Markdown e SVG | `registry/status-do-projeto.json`, `automation/sync_project_status.py` e `tests/test_sync_project_status.py` |
