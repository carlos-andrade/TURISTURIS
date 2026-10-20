# Inventário de repositórios abrangidos pela governança

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-REPOS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | INVENTARIO |
| **Fase** | Fase 5 — inventário transversal de repositórios |
| **Estado** | EM_REVISAO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | 56c970567639492f7cb11e8e7a669590874e4f463d648c619735b5f789f622a3 |
| **Commit de referência (versão anterior)** | [cb05bdaecd4f676fb024f3518abefffcb2b2810e](https://github.com/carlos-andrade/GOVERNANCA/commit/cb05bdaecd4f676fb024f3518abefffcb2b2810e) |
| **Data de criação** | 2026-10-14 |
| **Data de atualização** | 2026-10-16 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste inventário |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e [Norma de cabeçalho](NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Objetivo e limites

Registar os repositórios de projetos candidatos à adoção da norma de cabeçalho do GOVERNANCA, priorizar a inspeção e manter evidência verificável. A existência do repositório foi confirmada através dos metadados do GitHub em 2026-10-14 quando assinalada como confirmada abaixo; isso **não** significa que o conteúdo tenha sido auditado nem que a norma tenha sido aplicada.

A prioridade é operacional e provisória, não uma aprovação de escopo. A adoção só será declarada após inspeção dos ficheiros Markdown, comparação com a norma, verificação de hashes/links e registo dos resultados por repositório.

## Inventário inicial

| Repositório | Prioridade inicial | Existência no GitHub | Responsável de referência | Estado de adoção | Próxima ação |
|---|---|---|---|---|---|
| [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) | P0 — norma central | Confirmada; branch `main` | Proprietário do repositório | Norma aprovada; 62 ficheiros Markdown inventariados após inclusão deste registo | Executar auditoria final e manter controlos sincronizados |
| [STOCKS](https://github.com/carlos-andrade/STOCKS) | P1 — projeto ativo | Confirmada; branch `main` | Proprietário do repositório | AUDITORIA INDIVIDUAL CONCLUÍDA — 32/32 ficheiros Markdown sem cabeçalho canónico | Preparar lote de normalização STOCKS após concluir a linha de base dos restantes P1 |
| [DECIO-BAZIN](https://github.com/carlos-andrade/DECIO-BAZIN) | P1 — projeto ativo | Confirmada; branch `main` | Proprietário do repositório | AUDITORIA INDIVIDUAL CONCLUÍDA — 18/18 ficheiros Markdown sem cabeçalho canónico | Preparar lote de normalização DECIO-BAZIN após concluir a linha de base dos restantes P1 |
| [B3](https://github.com/carlos-andrade/B3) | P1 — dados e mercado | Confirmada; branch `main` | Proprietário do repositório | AUDITORIA INDIVIDUAL CONCLUÍDA — fotografia fixa do commit `6f156a2ea726b6f07a0c323cb1109e43a6c934e0`; 284/284 ficheiros Markdown inspecionados individualmente; 284/284 sem cabeçalho canónico completo. Um ficheiro contém cabeçalho parcial com SHA-256 pendente. | Preparar lote de normalização B3 após rever IDs, estados e metadados preexistentes; corrigir o cabeçalho parcial em lote próprio, sem alterar conteúdo substantivo. |
| [BLOOMBERG_MAIL](https://github.com/carlos-andrade/BLOOMBERG_MAIL) | P1 — ingestão de dados | Confirmada; branch `main` | Proprietário do repositório | AUDITORIA INDIVIDUAL CONCLUÍDA — fotografia fixa do commit `6a2e9622d05945de490477be5ea6eedf659937ba`; 123/123 ficheiros Markdown inspecionados individualmente sem cabeçalho canónico completo | Preparar lote de normalização após rever IDs, estados e metadados preexistentes. |
| [TURISTURIS](https://github.com/carlos-andrade/TURISTURIS) | P1 — dados e publicação | Confirmada; branch `main` | Proprietário do repositório | AUDITORIA INDIVIDUAL EM CURSO — fotografia fixa do commit `10c653f010e9ddf0abbe6a5c18f363a058afb03d`; 56/660 ficheiros Markdown inspecionados individualmente, sem cabeçalho canónico completo nos 56 examinados | Continuar a partir do caminho 57 da fotografia fixa; reconciliar a cobertura antes de fechar. |
| [XFI](https://github.com/carlos-andrade/XFI) | P1 — infraestrutura e operações | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 45 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [PROMPT_CHATGPT_CLAUDE](https://github.com/carlos-andrade/PROMPT_CHATGPT_CLAUDE) | P1 — cadeia de prompts | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 23 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [BRICKMASTER_GERAL](https://github.com/carlos-andrade/BRICKMASTER_GERAL) | P1 — estratégia de trading | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 41 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [FVG-ATLAS](https://github.com/carlos-andrade/FVG-ATLAS) | P1 — engenharia de dados de mercado | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 147 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [BITCOIN](https://github.com/carlos-andrade/BITCOIN) | P2 — projeto técnico | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 3 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [PROJETO-COM-RASPBERRY](https://github.com/carlos-andrade/PROJETO-COM-RASPBERRY) | P2 — projeto técnico | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 8 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [CURSO_GITHUB](https://github.com/carlos-andrade/CURSO_GITHUB) | P2 — formação | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 68 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [KDP](https://github.com/carlos-andrade/KDP) | P2 — publicação editorial | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 6 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [O-ULTIMO-CIGARRO](https://github.com/carlos-andrade/O-ULTIMO-CIGARRO) | P2 — conteúdo editorial | Confirmada; branch `main` | Proprietário do repositório | BASELINE INICIAL — README sem cabeçalho canónico; 122 ficheiros Markdown no repositório | Auditoria individual dos ficheiros Markdown e validação de exceções pendentes |
| [BRICKMASTER-CLAUDE](https://github.com/carlos-andrade/BRICKMASTER-CLAUDE) | A confirmar | Não confirmado; GitHub devolveu 404 para consulta de metadados | Proprietário do repositório | BLOQUEADO — existência/acesso não confirmados | Confirmar URL ou nome correto antes de incluir no escopo |

## Registo de progresso — B3 (2026-10-14)

Foram executadas 112 leituras individuais da branch `main`; os conteúdos devolvidos não apresentaram a tabela de cabeçalho canónico completa. A árvore mudou durante a execução e a última leitura contou 283 ficheiros Markdown. A cobertura única por caminho será reconciliada a partir de uma fotografia fixa antes de declarar percentagem ou conclusão. A inspeção é estrutural e não equivale à aprovação substantiva do conteúdo. A inspeção é estrutural e não equivale à aprovação substantiva do conteúdo.

## Critérios de inspeção por repositório

1. Confirmar URL, branch principal, acessibilidade e responsável.
2. Inventariar todos os ficheiros Markdown e distinguir documentação normativa, técnica, operacional e editorial.
3. Verificar cabeçalho canónico, ID único, versão, estado, autoridade, origem e commit de referência.
4. Recalcular SHA-256 canónico segundo a norma; não confundir com Git blob SHA.
5. Registar cobertura, exceções, ficheiros sem necessidade de cabeçalho e riscos de alteração.
6. Aplicar a norma apenas após o gate de autorização aplicável, preservando o corpo substantivo.
7. Atualizar este inventário com a evidência da inspeção e commits reais. Não inferir adoção pela mera existência de README.

## Próxima sequência

1. Linha de base inicial concluída para 14 repositórios acessíveis: árvore recursiva e README principal inspecionados; os 14 READMEs consultados não contêm o cabeçalho canónico. Os números de Markdown são contagens de ficheiros, não declarações de conformidade individual.
2. STOCKS auditado individualmente: 32/32 ficheiros Markdown sem cabeçalho canónico. DECIO-BAZIN auditado individualmente: 18/18 sem cabeçalho canónico. B3: auditoria concluída numa fotografia fixa do commit `6f156a2ea726b6f07a0c323cb1109e43a6c934e0` (árvore `6f156a2ea726b6f07a0c323cb1109e43a6c934e0`): 284/284 ficheiros Markdown inspecionados por caminho, sem cabeçalho canónico completo. O ficheiro `docs/governanca/PLANO_NORMALIZACAO_DOCUMENTAL_GOVERNANCA_V1.md` tem um cabeçalho parcial, mas o campo SHA-256 está pendente; por isso não conta como conforme. A auditoria confirma presença estrutural, não valida conteúdo, IDs, aprovações ou hashes individuais.
3. Registar resultados e exceções por caminho; só depois planear lotes de normalização por repositório.
4. Auditar os candidatos P2 após a primeira ronda P1. O repositório BRICKMASTER-CLAUDE permanece fora da contagem confirmada até resolução do 404.
