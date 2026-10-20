# Configuração

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-CONFIG-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | GUIA_OPERACIONAL |
| **Fase** | WATCHDOG — configuração |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | d9cef131f4296837766181f341817e518886305304d60fbea115ff937aada658 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/docs/configuracao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Edite `WATCHDOG/registry/sistemas-monitorizados.json`. Cada sistema deve ter ID único, nome, proprietário, criticidade e lista de verificações com IDs únicos.

Tipos locais suportados no MVP:
- `file_exists`
- `nonempty_file`
- `json_valid`

Tipos externos ainda não implementados resultam em `UNKNOWN`. Os caminhos são relativos à raiz do repositório e caminhos que escapem dessa raiz são rejeitados.

Antes de declarar um controlo obrigatório, definir o critério de sucesso, frequência, timeout, validade da evidência, severidade e responsável pela resposta. Não guardar credenciais no JSON.
