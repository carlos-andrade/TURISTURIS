# Ciclo de vida e gates
| Campo | Valor |
|---|---|
| **ID** | GOV-LCV-GATE-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PROCEDIMENTO |
| **Fase** | Ciclo de vida |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 1d2a5c8509f1ba35172dbb3512c7a0f7ff4a31ea03f9334436f24770e0e630dc |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/02-ciclo-de-vida/ciclo-de-vida-e-gates.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

| Gate | Objetivo | Evidência mínima | Decisão |
|---|---|---|---|
| G0 Entrada | Validar iniciativa | Problema, beneficiário, patrocinador e owner | Aceitar/devolver/rejeitar |
| G1 Viabilidade | Justificar investimento | Benefícios, alternativas, estimativa, riscos e dependências | Financiar/testar/suspender/cancelar |
| G2 Desenho | Construção segura e testável | Requisitos, arquitetura, dados, ameaças, aceitação e testes | Aprovar/corrigir/rejeitar |
| G3 Construção validada | Comprovar qualidade | Revisão, testes, artefactos e documentação | Aceitar/corrigir/bloquear |
| G4 Prontidão | Preparar operação | Segurança, backups, observabilidade, rollback, suporte | Lançar/bloquear |
| G5 Lançamento | Controlar implantação | Autorização, janela, métricas e rollback | Prosseguir/abortar/reverter |
| G6 Encerramento | Transferir/descontinuar | Aceitação, pendências, arquivo/eliminação e lições | Encerrar/transferir/prolongar |

Cada gate tem decisor autorizado, critérios prévios e registo de pendências. Combinar gates é admissível em baixo risco com justificação. Controlos críticos e obrigações não são dispensáveis. Cancelamentos registam dados, acessos, ativos, contratos e comunicações a tratar.