# Modelo de integração

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-INT-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | MODELO_TECNICO |
| **Fase** | WATCHDOG — integração |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 7c3e8da4f31d1e5415c21691bcf297e897848ef0626dc170342efa5c04b298a1 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/arquitetura/modelo-de-integracao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Cada projeto adotante fornece:

- identificador único e proprietário;
- inventário de sistemas/processos e criticidade;
- controlos aplicáveis e justificativa para exclusões;
- adaptador e método de recolha;
- frequência, timeout e tolerância a dados atrasados;
- severidade, destinatários e prazos de resposta;
- formato e localização das evidências;
- procedimento de recuperação e contacto de escalonamento.

A integração começa em modo somente leitura. O adaptador deve demonstrar teste positivo, teste negativo, indisponibilidade, dados inválidos, timeout e recuperação. As credenciais são fornecidas pelo mecanismo de segredos do ambiente, nunca por ficheiros versionados.

Uma integração não pode declarar conformidade integral apenas porque o pipeline terminou com sucesso: a cobertura real e os controlos não implementados devem ser apresentados separadamente.
