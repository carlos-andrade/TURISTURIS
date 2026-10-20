# Modelo de execução

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-EXEC-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | MODELO_TECNICO |
| **Fase** | WATCHDOG — execução |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | d78f781c88e4e82d77e94a32c94580ea81ba83f582a869da9b9f986844c26219 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/arquitetura/modelo-de-execucao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Modos

- **CI/agenda:** validações periódicas de repositórios, documentação e pipelines.
- **Serviço permanente:** verificações com requisitos de baixa latência ou execução contínua.
- **Agente local:** sinais que não podem ser recolhidos remotamente.
- **Verificação externa:** sondagem independente para confirmar disponibilidade e detetar falha do monitor principal.

## Ciclo mínimo

1. Carregar inventário e configuração versionados.
2. Validar esquema, permissões e dependências.
3. Executar verificações dentro de timeout.
4. Classificar o resultado e a qualidade da evidência.
5. Emitir registo estruturado.
6. Notificar conforme política.
7. Confirmar recuperação e encerrar incidente apenas com evidência.

## Resiliência

Definir timeout, retry limitado, backoff, deduplicação e prevenção de tempestade de alertas. O resultado antigo deve expirar segundo a frequência declarada. A falha do destino de alertas deve ter canal alternativo para controlos críticos.

## Limites

Não implementar ações de correção automática até que o proprietário defina autorização, impacto, rollback, limites e teste de segurança.
