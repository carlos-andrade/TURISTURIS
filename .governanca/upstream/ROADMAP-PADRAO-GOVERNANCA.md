# Roadmap padrão — Governança

| Campo | Valor |
|---|---|
| **ID** | GOV-ROADMAP-PADRAO-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PADRAO |
| **Fase** | Governação transversal |
| **Estado** | APROVADO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | 86db4b0ae75044a81f87da61b7798e1ef88401618239f46d8bbb75060ef2cee2 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-17 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Carlos Andrade — aprovação expressa nesta solicitação |
| **Origem** | Solicitação expressa de adoção do modelo de roadmap em 2026-10-17 |
| **Autoridade superior** | [CONSTITUICAO.md](CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Finalidade

Este é o modelo visual e operacional obrigatório para o roadmap da GOVERNANCA e dos repositórios que adotem formalmente as suas regras. O roadmap é instrumento de execução, decisão e auditoria, não uma lista informal de tarefas.

## 2. Vistas obrigatórias

O painel executivo deve apresentar uma barra de status visual, calculada por critérios com evidência, segundo a [Norma de estado e percentual de conclusão](standards/status-e-percentual-de-conclusao.md). A barra textual e o SVG devem derivar da mesma fonte canónica; percentuais não podem ser editados manualmente.

### Painel executivo
Nome do projeto, versão/data, estado global, fase atual, marcos prioritários, riscos e bloqueios, próximo marco verificável e progresso apenas quando calculado segundo a norma aplicável.

### Sequência de execução
Fases ou gates em sequência clara. Cada fase declara identificador, objetivo, entregáveis, estado, dependências, critérios objetivos de entrada/saída e evidências.

### Ações prioritárias
Ações ordenadas por prioridade e dependência, com resultado esperado, critério de conclusão e referência verificável.

### Evidências e auditoria
Ligações para commits, pull requests, issues, workflows, testes, relatórios, decisões e aprovações. Distinguir execução, validação técnica e aceitação formal.

### Riscos e bloqueios
Explicitar impacto, dependência, responsável, ação de desbloqueio, decisão pendente e exceções válidas.

## 3. Princípios

1. Evidência antes de estado: não declarar conclusão sem critérios satisfeitos e artefactos verificáveis.
2. Fail-closed: dependências críticas não satisfeitas bloqueiam a passagem do gate.
3. Sem progresso inventado: percentuais seguem a norma oficial.
4. Dados desconhecidos permanecem pendentes ou UNKNOWN, nunca sucesso presumido.
5. Conclusões ligadas a caminhos, commits, testes ou relatórios.
6. Atualização após cada fase ou mudança material.
7. Preservar histórico, inclusive resultados desfavoráveis.
8. Cumprir Constituição, políticas aprovadas, contratos e normas superiores.

## 4. Estados e aceitação

Usar estados controlados pela GOVERNANCA e pelo projeto. Como mínimo, distinguir `PLANEADA`, `EM_EXECUCAO`, `AGUARDANDO_EVIDENCIA`, `BLOQUEADA`, `EM_REVISAO`, `CONCLUIDA` e `ACEITE_COM_EXCECAO`. Se houver vocabulário local, documentar o mapeamento.

Uma fase só é concluída quando os entregáveis existem, os testes exigidos foram executados, os critérios foram satisfeitos, os bloqueios críticos foram resolvidos ou formalmente excecionados e as evidências estão acessíveis.

## 5. Modelo mínimo

1. Painel executivo.
2. Roadmap por fases/gates.
3. Ações prioritárias.
4. Riscos e bloqueios.
5. Evidências verificáveis.
6. Dependências e critérios de aceitação.
7. Decisões e exceções.
8. Histórico de alterações.
9. Próxima ação concreta.

## 6. Conformidade

Os repositórios abrangidos adotam esta estrutura ou um mapeamento equivalente documentado que preserve os controlos. Exceções exigem motivo, âmbito, risco, aprovador, validade e controlos compensatórios. Conformidade visual não prova execução; a adoção deve ser inspecionada por repositório.

## 7. Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-17 | Criação do padrão visual e operacional transversal | Aprovação expressa do proprietário |
| 1.1.0 | 2026-10-17 | Inclusão da barra de status baseada em critérios e evidências | Norma GOV-STD-STATUS-001 v1.1.0 |
