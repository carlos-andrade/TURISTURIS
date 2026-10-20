# Arquitetura geral

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-ARQ-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | ARQUITETURA |
| **Fase** | WATCHDOG — arquitetura |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | a763e45569cc5bb2105c99a72e74a5babf04a5f17020ac3c973948d0c385e2c4 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/arquitetura/arquitetura-geral.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Camadas

1. **Política e catálogo:** requisitos, critérios, responsáveis e severidade.
2. **Inventário:** sistemas, processos, dependências, localização e criticidade.
3. **Adaptadores:** recolha de sinais por API, agente, logs, métricas, eventos ou validação documental.
4. **Motor de avaliação:** normaliza resultados, aplica limites e trata dados ausentes.
5. **Evidências:** regista resultado, instante UTC, origem, versão, referência e integridade.
6. **Alertas e escalonamento:** encaminha por severidade, confirma receção e escala quando necessário.
7. **Relatórios e auditoria:** cobertura, incidentes, exceções, tendência e eficácia.
8. **Supervisão independente:** confirma que o motor e os canais de alerta estão vivos.

## Fluxo

`Inventário → recolha → validação → avaliação → evidência → alerta → resposta → verificação de recuperação`

A falha de recolha gera `UNKNOWN` ou um alerta de monitor indisponível; nunca é convertida automaticamente em `PASS`.

## Modelo de implantação

Pode combinar CI agendado, serviço permanente e agentes locais. A escolha depende de latência, criticidade, conectividade e custo. GitHub Actions é apropriado para validações periódicas de repositórios, mas não garante sozinho vigilância contínua 24×7.

## Segurança

Separar credenciais por adaptador, limitar permissões, proteger segredos fora do Git, validar entradas, limitar dados pessoais e registar alterações de configuração. A remediação deve ser desligada por defeito.
