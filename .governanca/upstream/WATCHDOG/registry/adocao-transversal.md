# Registo de adoção transversal do WATCHDOG

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-REG-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | REGISTO |
| **Fase** | WATCHDOG — adoção transversal |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 2f59cd7ba75b3f603b045717a468aabfcc3abe3354fdcb0f6572a4657d8c8a64 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/registry/adocao-transversal.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Atualizado:** 2026-10-13  
**Estado:** inventário inicial baseado em inspeção dos repositórios públicos consultados; não equivale a integração operacional.  
**Regra:** um repositório só passa a IMPLEMENTADO após inspeção do workflow, teste positivo, teste de falha, evidência persistida e responsável identificado.

## Inventário inicial

| Prioridade | Repositório | Evidência de estrutura consultada | Estado inicial | Próxima ação |
|---|---|---|---|---|
| P0 | [B3](https://github.com/carlos-andrade/B3) | Monitor de execuções, monitor de atualidade, inventários e relatórios | PILOTO_IMPLEMENTADO; aceitação pendente | Resolver triagem das issues #7 e #8, aprovar limiares e ativar supervisão independente |
| P0 | [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) | Diretório WATCHDOG, workflow `bloomberg-mail-watchdog-supervisor.yml`, 20 workflows no total; workflow compila scripts, executa testes determinísticos, valida adapter COTAHIST e contrato | WATCHDOG_EXISTENTE_PARCIAL; aceite operacional pendente | Alterado `cancel-in-progress` para `false` para não interromper uma execução ativa; validação do supervisor após a alteração passou (https://github.com/carlos-andrade/BLOOMBERG_MAIL/actions/runs/38391557718); ainda falta testar falhas de adapter e verificar persistência/alerta externo e supervisão do próprio supervisor |
| P1 | [TURISTURIS](https://github.com/carlos-andrade/TURISTURIS) | 30 workflows GitHub Actions e fluxos de captura, normalização, validação e publicação | PENDENTE_INTEGRAÇÃO | Priorizar captura de fontes oficiais, normalização, validação de registos e publicação; definir checks por fase |
| P1 | [DECIO-BAZIN](https://github.com/carlos-andrade/DECIO-BAZIN) | 1 workflow e README | PENDENTE_INTEGRAÇÃO | Inventariar execução agendada, qualidade dos dados e evidência |
| P1 | [CURSO_GITHUB](https://github.com/carlos-andrade/CURSO_GITHUB) | 1 workflow e README | PENDENTE_INTEGRAÇÃO | Definir controlos de conteúdo, publicação e estado do curso |
| P2 | [FVG-ATLAS](https://github.com/carlos-andrade/FVG-ATLAS) | README, sem workflows na árvore consultada | PENDENTE_INTEGRAÇÃO | Confirmar se a automação é local/manual; não criar workflow sem contrato de dados e cadência |
| P2 | [O-ULTIMO-CIGARRO](https://github.com/carlos-andrade/O-ULTIMO-CIGARRO) | README, sem workflows na árvore consultada | PENDENTE_INTEGRAÇÃO | Definir validações documentais, capítulos, integridade e publicação |
| P2 | [PROJETO-COM-RASPBERRY](https://github.com/carlos-andrade/PROJETO-COM-RASPBERRY) | 1 workflow e README | PENDENTE_INTEGRAÇÃO | Inventariar testes, deploy e dependências físicas antes de escolher os controlos |
| P2 | [KDP](https://github.com/carlos-andrade/KDP) | README e poucos ficheiros, sem workflows na árvore consultada | PENDENTE_INTEGRAÇÃO | Confirmar o âmbito ativo; definir controlos documentais e de publicação proporcionais |
| A confirmar | [BRICKMASTER-CLAUDE](https://github.com/carlos-andrade/BRICKMASTER-CLAUDE) | A árvore `main` não foi acessível na consulta (404); o estado do repositório não foi inferido | NÃO_VERIFICADO | Confirmar nome, visibilidade ou branch antes de integrar |

## Sequência de execução

### Gate A — Auditoria antes de copiar
1. Ler workflows e contratos existentes.
2. Identificar dados, artefactos, ações de escrita, credenciais e dependências.
3. Determinar criticidade, periodicidade esperada e critério objetivo de falha.
4. Reutilizar o WATCHDOG existente se cobrir o requisito; não criar duplicação concorrente.

### Gate B — Adaptador mínimo por repositório
1. Adicionar registo de sistema e controlos obrigatórios.
2. Criar verificação somente de leitura por defeito.
3. Produzir evidência JSON/Markdown com timestamps UTC, fonte e resultado.
4. Implementar alerta deduplicado sem fechar incidentes automaticamente.
5. Testar PASS, FAIL, UNKNOWN, indisponibilidade da API e recuperação.

### Gate C — Aceitação
1. Executar validação e teste negativo.
2. Rever a evidência persistida.
3. Confirmar responsável, canal de alerta e política de retenção.
4. Registar aceitação explícita.
5. Só então alterar o estado para IMPLEMENTADO e atualizar a barra central.

## Critério de conclusão transversal

A adoção transversal não está concluída enquanto os repositórios ativos no âmbito não tiverem sido inspecionados e classificados como:
- **IMPLEMENTADO** — testes e aceitação comprovados;
- **NÃO APLICÁVEL** — decisão justificada e aprovada;
- **PENDENTE** — existe trabalho ou evidência em falta.

Uma pasta `WATCHDOG`, workflow existente ou README não prova, isoladamente, cobertura operacional.
