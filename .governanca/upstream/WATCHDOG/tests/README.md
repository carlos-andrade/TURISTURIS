# Estratégia de testes WATCHDOG

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-TEST-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README_TESTS |
| **Fase** | WATCHDOG — testes |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a23c3bd0d13a22d52aa8ca6c417d03fedc6dfd8a4bf564bcb2f42d5c702b4214 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/tests/README.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Os testes unitários cobrem: estado UNKNOWN para verificações não suportadas, referência de evidência em verificações locais, rejeição de traversal de caminhos, JSON inválido, IDs duplicados e cálculo de cobertura. Antes de produção, acrescentar testes de integração para alertas, timeout, retries, deduplicação, indisponibilidade do monitor, segurança de credenciais e recuperação.
