# Operação

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-OPER-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | GUIA_OPERACIONAL |
| **Fase** | WATCHDOG — operação |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a135ea2dd22debd4e82da37cd563ff6e8f6d15cede89337dc16567070618afbd |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/docs/operacao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Executar testes após cada alteração ao motor, registo ou adaptador. Rever resultados `FAIL` e `UNKNOWN`; atribuir proprietário e prazo para lacunas relevantes. Manter inventário e cobertura atualizados.

O relatório CLI é transitório e não é, por si só, um repositório de evidências persistente ou imutável. A operação em produção exige backend de evidências, alertas, monitor independente, política de retenção e controlo de acesso. Não declarar 24×7 antes de testar estes componentes de ponta a ponta.
