# Constituição do Sistema de Governança

| Campo | Valor |
|---|---|
| **ID** | GOV-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | CONSTITUICAO |
| **Fase** | Governação fundacional |
| **Estado** | PROPOSTA PARA REVISÃO |
| **Versão** | 1.0.1 |
| **SHA-256 (conteúdo canónico)** | fcdf39acc56d53b886815967080f0d183960e1ccbd2d0cca023181da9f80834d |
| **Commit de referência (versão anterior)** | [62a2354c6372417a36c4df256fff267e691d8495](https://github.com/carlos-andrade/GOVERNANCA/commit/62a2354c6372417a36c4df256fff267e691d8495) |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal da Constituição |
| **Autoridade superior** | Lei aplicável, contratos vinculativos e políticas formalmente aprovadas; ver secção 3 |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |


## 1. Finalidade

Estabelecer princípios superiores para governar projetos, produtos, dados, sistemas, conteúdos, operações e repositórios que adotem este sistema.

## 2. Princípios

1. Propósito verificável: cada iniciativa declara problema, beneficiários e resultado esperado.
2. Responsabilidade explícita: resultados, riscos e decisões relevantes têm responsáveis identificados.
3. Proporcionalidade: os controlos dependem do risco, impacto, exposição, irreversibilidade e obrigações aplicáveis.
4. Segurança e privacidade desde a conceção.
5. Evidência antes de alegação: estados e resultados são demonstrados por artefactos verificáveis.
6. Rastreabilidade entre requisitos, decisões, alterações, releases e incidentes.
7. Critérios mensuráveis definidos antes da aceitação.
8. Automatização responsável e revisão humana onde o impacto o exige.
9. Reversibilidade de mudanças de alto impacto.
10. Propriedade, origem, qualidade, acesso, retenção e eliminação dos dados explícitos.
11. Interoperabilidade e dependências justificadas.
12. Aprendizagem contínua a partir de incidentes e desvios.

## 3. Hierarquia de autoridade

A ordem de precedência é: (1) lei aplicável; (2) contratos vinculativos; (3) políticas formalmente aprovadas; (4) padrões e procedimentos; (5) recomendações e exemplos. Conflitos devem ser registados e escalados.

## 4. Direitos de decisão

- Patrocinador: valor, resultado e recursos.
- Responsável de projeto: coordenação de escopo, prazo, orçamento e dependências.
- Responsável técnico: arquitetura e implementação dentro do mandato.
- Proprietário de dados/processo: definição, uso permitido, qualidade e ciclo de vida.
- Segurança/privacidade/conformidade: avaliação especializada e bloqueio dentro do mandato definido.
- Operações: suportabilidade, observabilidade e recuperação.
- Revisor independente: avaliação imparcial quando o risco exige segregação.

Em equipas pequenas pode haver acumulação de funções; em risco elevado, a autoaprovação deve ser mitigada.

## 5. Gates mínimos

- G0 — Entrada: problema, beneficiário, patrocinador e owner identificados.
- G1 — Viabilidade: valor, alternativas, custos, riscos e dependências.
- G2 — Desenho: requisitos, arquitetura, dados, ameaças, aceitação e testes.
- G3 — Construção validada: revisão, testes e documentação.
- G4 — Prontidão operacional: segurança, recuperação, observabilidade, suporte e rollback.
- G5 — Lançamento: autorização explícita e observação pós-implementação.
- G6 — Encerramento: aceitação, transferência, arquivo/eliminação e lições.

Gates podem ser combinados em projetos de baixo risco com justificação registada. Obrigações legais, contratuais e controlos críticos não são dispensados.

## 6. Exceções

Registar regra afetada, motivo, risco, controlos compensatórios, aprovador, validade, responsável pela resolução e condição de revogação. Exceções não podem autorizar incumprimento legal ou contratual.

## 7. Integridade

Estados controlados: `PROPOSTO`, `EM_CURSO`, `BLOQUEADO`, `EM_REVISAO`, `APROVADO`, `REJEITADO`, `CONCLUIDO`, `DEPRECADO`. Nunca declarar teste, publicação, execução ou controlo ativo sem evidência.

## 8. Monitorização transversal — WATCHDOG

Os projetos que adotem a GOVERNANCA devem declarar como os seus sistemas, dados, processos e controlos serão monitorizados. O WATCHDOG é o padrão transversal para inventário, critérios, evidências, classificação de estados, alertas, escalonamento e verificação de recuperação. A monitorização deve ser proporcional ao risco e respeitar segurança, privacidade, obrigações legais e contratuais.

A ausência de dados ou de execução nunca equivale a sucesso. Os controlos devem distinguir `PASS`, `WARN`, `FAIL` e `UNKNOWN`. A indisponibilidade do próprio monitor deve ser detetável por mecanismo independente nos âmbitos críticos. Remediação automática fica desativada por defeito e exige autorização, limites, rollback e auditoria.

O padrão, os registos e os testes estão em [`WATCHDOG/`](WATCHDOG/README.md). A existência desta estrutura não prova monitorização universal ativa; cada integração deve ser implementada, testada e aceite com evidência.

## 9. Revisão

Rever anualmente e perante alterações materiais. Até aprovação formal, esta versão é uma proposta de base e não uma política corporativa ratificada.

## 9. Padrão transversal de roadmap

O repositório GOVERNANCA e os repositórios que adotem formalmente as suas regras devem cumprir a [Carta/Contrato — padrão obrigatório de roadmap](CARTA-CONTRATO-PADRAO-ROADMAP.md) e o [Roadmap padrão — Governança](ROADMAP-PADRAO-GOVERNANCA.md). A adoção exige roadmap local, evidências verificáveis, critérios de aceitação, estado atualizado e inspeção individual. A publicação da norma não implica conformidade automática dos demais repositórios.


## 10. Barra de status e progresso comprovado

O estado e o percentual dos projetos abrangidos devem cumprir a [Norma de estado e percentual de conclusão](standards/status-e-percentual-de-conclusao.md). A pontuação deriva de critérios explícitos e evidências verificáveis; o painel Markdown e a representação visual são gerados da mesma fonte canónica. A data de atualização do registo não substitui a validação dos controlos operacionais nem a aprovação formal de encerramento. A adoção pelos demais repositórios exige implementação e validação individual.
