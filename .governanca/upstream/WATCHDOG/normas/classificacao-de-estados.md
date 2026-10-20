# Classificação de estados

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-STATE-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | NORMA |
| **Fase** | WATCHDOG — classificação de estados |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | f2357073f81c5dcef36bf738a43ffd8f554ea9b6364fafff55c5ca095727634a |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/normas/classificacao-de-estados.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

- **PASS:** verificação executada, critério satisfeito e evidência válida.
- **WARN:** degradação, limiar preventivo, tendência adversa ou exceção dentro de prazo.
- **FAIL:** critério violado por evidência válida.
- **UNKNOWN:** verificação não executada, origem indisponível, evidência expirada, configuração não suportada ou dados insuficientes.

## Regras

1. Falta de dados nunca significa sucesso.
2. `UNKNOWN` não pode ser silenciosamente descartado; a criticidade determina se gera incidente.
3. A severidade não deve ser inferida apenas do estado: deve considerar impacto, urgência, extensão e obrigações.
4. A recuperação exige novo teste e registo da evidência.
5. Um resultado deve incluir timestamp, ID do controlo, origem, versão do avaliador e referência de evidência.
6. Os estados do controlo são distintos do estado do projeto e da percentagem de conclusão.
