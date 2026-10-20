# WATCHDOG — Monitorização transversal da GOVERNANCA

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-README-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README |
| **Fase** | WATCHDOG — visão geral |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 53f8c0ad23eb532949ef5347cbf52411888b25c71b49c67385b9340b76b59519 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/README.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e [Norma de cabeçalho](../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

**Estado:** MVP normativo e validador local em implementação; monitorização externa ainda não configurada.  
**Objetivo:** tornar verificável a cobertura e a eficácia dos controlos de sistemas, dados, processos e organizações que adotem a GOVERNANCA.

## Começar por aqui

Consulte também o [roadmap de implementação e critérios de encerramento](roadmap-de-implementacao.md) para distinguir o MVP validado das fases pendentes.

1. Leia a [Carta WATCHDOG](CARTA-WATCHDOG.md) e a [política de monitorização](normas/politica-de-monitorizacao.md).
2. Registe os sistemas em [registry/sistemas-monitorizados.json](registry/sistemas-monitorizados.json).
3. Declare os controlos aplicáveis em [registry/controlos-obrigatorios.json](registry/controlos-obrigatorios.json).
4. Defina os critérios e as evidências conforme os [contratos](contratos/).
5. Execute o validador: `python WATCHDOG/engine/watchdog.py --check`.
6. Execute os testes: `python -m unittest discover -s WATCHDOG/tests -v`.
7. Integre adaptadores específicos e um monitor independente antes de afirmar cobertura operacional contínua.

## Estados

- `PASS`: verificação executada e satisfeita, com evidência gerada ou referenciada.
- `WARN`: condição degradada que exige avaliação.
- `FAIL`: condição verificada que viola o critério.
- `UNKNOWN`: não há dados suficientes, a verificação não está implementada ou o monitor está indisponível.

**Regra de segurança:** ausência de dados nunca equivale a `PASS`. O validador inicial verifica configuração e ficheiros locais; não afirma que serviços externos estejam saudáveis.

## Estrutura

- `arquitetura/`: desenho e integração.
- `normas/`: regras de monitorização, estados, escalonamento, evidência e segurança.
- `contratos/`: formatos de configuração, alerta e evidência.
- `registry/`: inventário e cobertura declarada.
- `adapters/`: pontos de integração por domínio.
- `engine/`: validador e avaliação inicial.
- `reports/`: modelos e exemplos.
- `runbooks/`: resposta a incidentes.
- `tests/`: testes unitários, integração e falhas simuladas.
- `docs/`: instalação, configuração e operação.

## Limites atuais

O MVP valida registos e verificações locais declaradas. Ainda não fornece recolha universal, agente 24×7, envio de alertas, armazenamento imutável de evidências, integração com sistemas externos ou remediação automática. Estas capacidades exigem adaptadores, infraestrutura, credenciais protegidas e testes próprios.

## Critério de adoção

Um projeto só pode declarar o WATCHDOG operacional quando: inventário aprovado; controlos prioritários definidos; adaptadores testados; alertas e responsáveis validados; indisponibilidade do monitor detetável por via independente; retenção e acesso às evidências definidos; e aceitação registada.
