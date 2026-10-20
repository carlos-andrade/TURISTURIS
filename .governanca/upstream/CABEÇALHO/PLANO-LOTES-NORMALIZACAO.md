# Plano de lotes — normalização documental

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-LOTES-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PLANO_EXECUCAO |
| **Fase** | Preparação da normalização |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.9 |
| **SHA-256 (conteúdo canónico)** | 2cdc2b89dfccb55a9c3e79151bbe5d49ddbb2d751c5d8d82a0b1b5996df1c67a |
| **Commit de referência (versão anterior)** | [b55de1f609e33e8b7cd190507e23f0d183cd6622](https://github.com/carlos-andrade/GOVERNANCA/commit/b97fa1b4164270b782c1bb04e7023406335b797a) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal |
| **Autoridade superior** | [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) e [CONSTITUICAO.md](../CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo

Preparar a normalização dos 30 ficheiros Markdown ainda pendentes no [inventário documental](INVENTARIO-DOCUMENTAL.md), com lotes pequenos e critérios verificáveis. Este plano não ratifica a norma nem autoriza alterações retroativas.

## Gate de autorização

A Norma de Cabeçalho Documental Padrão, versão 1.0.3, foi formalmente aprovada pelo proprietário em 2026-10-13. A evidência está no [registo de aprovação](REGISTO-APROVACAO-NORMA-1.0.3.md) e na [issue #2](https://github.com/carlos-andrade/GOVERNANCA/issues/2). O gate está satisfeito; a normalização prossegue por lotes com validação individual.

L1 foi aplicado a `CONSTITUICAO.md` e `README.md`. Os 48 documentos restantes serão tratados por lotes. Não alterar estados substantivos, inventar IDs históricos ou declarar conformidade sem evidência.

## Lotes propostos

| Lote | Âmbito | Ficheiros previstos | Regra especial |
|---|---|---:|---|
| L1 | Constituição e entrada do repositório | 2 | Tratar `CONSTITUICAO.md` como autoridade superior; preservar metadados históricos do `README.md` |
| L2 | Fundamentos e governança | 7 | Preservar significado normativo e decisões existentes |
| L3 | Ciclo de vida, portefólio e engenharia | 5 | Preservar requisitos, arquitetura e histórico |
| L4 | Dados, IA, segurança e privacidade | 6 | Não inventar requisitos ou aprovações |
| L5 | Operações, standards e templates | 4 | Preservar procedimentos e critérios existentes |
| L6 | WATCHDOG — arquitetura, normas e operação | 16 | Preservar contratos técnicos, políticas e runbooks |
| L7 | WATCHDOG — adaptadores, relatórios e testes | 10 | Preservar exemplos e estrutura operacional |

Os totais corrigidos refletem 24 documentos centrais e 26 documentos WATCHDOG, totalizando 50 pendentes. Os totais são uma proposta de agrupamento. Antes de cada lote, reconciliar os caminhos com o inventário atual; se houver divergência, corrigir o plano antes de editar.

## Procedimento e aceitação

1. Obter a versão atual e blob SHA antes de editar.
2. Mapear apenas metadados sustentados pelo documento ou histórico Git.
3. Preservar o corpo substantivo e os IDs existentes.
4. Registar dados desconhecidos como `N/A — justificação`; não inferir aprovação.
5. Aplicar cabeçalho Markdown nativo e recalcular o SHA-256 canónico segundo a norma.
6. Validar commit anterior, links, IDs, renderização e diff.
7. Atualizar inventário e roadmap somente após verificação da publicação.
8. Parar perante perda de conteúdo, conflito de metadados, link inválido ou hash divergente.

## Estado e próxima ação

**Estado:** gate de aprovação satisfeito; L1–L7 concluídos. Inventário atual: 62 ficheiros Markdown, 62 com campos canónicos e 0 pendentes.

**Classificação não destrutiva:** registada em [CLASSIFICACAO-PRE-NORMALIZACAO.md](CLASSIFICACAO-PRE-NORMALIZACAO.md). **L1:** concluído; GOV-001, versão e estado da Constituição preservados, assim como os marcadores automáticos do README. **Próxima ação:** concluir a Fase 5 com auditoria individual dos ficheiros Markdown dos repositórios P1; depois iniciar a Fase 6 por repositório.

## Histórico

| Versão | Data | Alteração |
|---|---|---|
| 1.0.0 | 2026-10-13 | Plano inicial de lotes e gates |
| 1.0.1 | 2026-10-13 | Contagem dos lotes corrigida e classificação não destrutiva concluída | CABEÇALHO/CLASSIFICACAO-PRE-NORMALIZACAO.md |

| 1.0.2 | 2026-10-13 | Aprovação formal satisfeita e L1 concluído; 48 documentos permanecem pendentes | Registo de aprovação, commits L1 e inventário v1.0.4 |
| 1.0.3 | 2026-10-13 | L2 concluído nos sete documentos previstos; 41 documentos permanecem pendentes | Inventário v1.0.5 e commits L2 |
| 1.0.4 | 2026-10-13 | L3 concluído nos cinco documentos previstos; 36 documentos permanecem pendentes | Inventário v1.0.6 e commits L3 |
| 1.0.5 | 2026-10-13 | L4 concluído nos seis documentos previstos; 30 documentos permanecem pendentes | Inventário v1.0.7 e commits L4 |
| 1.0.6 | 2026-10-14 | L5 concluído nos quatro documentos previstos; 26 documentos permanecem pendentes | Inventário v1.0.8 e commits L5 |
| 1.0.7 | 2026-10-14 | L6 concluído nos 16 documentos WATCHDOG previstos; 10 documentos permanecem pendentes | Inventário v1.0.9 e commits L6 |
| 1.0.8 | 2026-10-14 | L7 concluído nos dez documentos WATCHDOG restantes; 61/61 documentos com cabeçalho canónico | Inventário v1.1.0 e commits L7 |

| 1.0.9 | 2026-10-14 | Fase 5 iniciada; inventário transversal com 15 repositórios confirmados e um candidato com acesso não confirmado; linha de base inicial de 14 repositórios | CABEÇALHO/INVENTARIO-REPOSITORIOS-ABRANGIDOS.md |
