# Governança de dados
| Campo | Valor |
|---|---|
| **ID** | GOV-DATA-GOV-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | POLITICA |
| **Fase** | Dados e IA |
| **Estado** | EM_REVISAO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | 4417d92f0d807c6b9d7b6daef023f363e4e073aca593e00553f98fb997e41308 |
| **Commit de referência (versão anterior)** | [a9cf80e](https://github.com/carlos-andrade/GOVERNANCA/commit/a9cf80e61b77409377ed8b92e2bf88ff09e8bc2e) |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-20 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/05-dados-e-ia/governanca-de-dados.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Modelo organizacional

Usar como padrão governança federada: padrões, classificação e controlos comuns no núcleo; responsabilidade operacional nos domínios. Modelos centralizado, descentralizado/autónomo e orientado a domínio/Data Mesh podem ser adequados conforme escala, maturidade, obrigações e natureza dos dados.

## Papéis

Proprietário do dado (definição e uso permitido); steward/curador (metadados e qualidade); custodiante técnico (armazenamento, backup e acesso); consumidor (uso autorizado); segurança/privacidade (risco e obrigações).

## Controlos

1. Inventário de conjuntos de dados e origens.
2. Catálogo e glossário para ativos relevantes.
3. Classificação por sensibilidade e impacto.
4. Proveniência, qualidade e linhagem conforme risco.
5. Menor privilégio e RBAC/ABAC quando apropriado.
6. Retenção, arquivo, eliminação e resposta a pedidos.
7. Regras de qualidade mensuráveis, owner e escalonamento.
8. Registo de partilha e uso por terceiros quando relevante.
9. Gestão de incidentes e obrigações de notificação.

Qualidade inclui completude, validade, unicidade, consistência, atualidade, exatidão e rastreabilidade. A relevância de cada dimensão depende do uso.

## Conformidade

Referências ao RGPD são pontos de triagem, não conclusão jurídica. Base legal, prazos e avaliações exigidas dependem do contexto e devem ser confirmados por pessoa competente.

## Documento-base fornecido

O ficheiro “Os modelos de governança de dados mais utilizados.docx” identifica governança centralizada, descentralizada/autónoma, federada/híbrida e orientada a domínio/Data Mesh; destaca pessoas, políticas, processos e tecnologia como pilares. Este documento usa esses conceitos como referência inicial e acrescenta controlos operacionais.

## Política transversal de aquisição de dados públicos gratuitos — adenda v1.1.0

**Diretriz operacional adotada para o projeto B3:** identificar e adquirir sistematicamente os dados e metadados que estejam gratuitamente disponíveis ao público em fontes públicas, priorizando fontes primárias e oficiais. A disponibilidade pública deve ser convertida em inventário, captura reprodutível, proveniência, validação e monitorização, em vez de ser descartada por falhas técnicas isoladas ou bloqueios genéricos sem evidência.

### Regras de execução

1. Priorizar APIs, endpoints próprios, feeds e ficheiros de download oficiais.
2. Investigar erros e procurar canais oficiais alternativos antes de declarar indisponibilidade.
3. Distinguir quatro dimensões: disponibilidade técnica, permissão de aquisição automatizada, permissão de uso/redistribuição e qualidade/certificação do conteúdo.
4. Só aplicar bloqueio quando existir fundamento específico documentado, como termos aplicáveis, licença, autenticação não disponível, obrigação legal ou restrição técnica explícita.
5. Não contornar autenticação, CAPTCHA, controlos de acesso ou proibições explícitas. Se uma interface proibir recolha automatizada, procurar um canal oficial apropriado ou obter autorização; não presumir que a restrição abrange automaticamente todos os canais do fornecedor.
6. Preservar RAW, fonte/canal, data/hora, parâmetros não secretos, status, checksum SHA-256, manifesto, logs, validações e histórico de falhas, conforme permitido pelos termos.
7. Não inferir que a captura técnica autoriza redistribuição irrestrita; registar separadamente as condições de utilização.
8. Usar estados específicos e reavaliáveis. Uma falha HTTP isolada não justifica um bloqueio geral permanente.

### Aplicação B3 — BVBG.028.02

O projeto B3 mantém a política operacional detalhada em [Política de aquisição de dados públicos e gratuitos](https://github.com/carlos-andrade/B3/blob/main/WIKI/01-GOVERNANCA/POLITICA_AQUISICAO_DADOS_PUBLICOS_GRATUITOS_V1.md). Para BVBG.028.02 / InstrumentsConsolidated, a execução bem-sucedida demonstra funcionamento técnico do canal testado, mas não resolve por si só os termos específicos de automatização e redistribuição. O aviso da página “Pesquisa por pregão” deve ser respeitado para essa interface; a próxima ação é verificar o canal próprio de download/API e documentar os termos aplicáveis, sem declarar o catálogo inteiro tecnicamente bloqueado.

Esta adenda estabelece a orientação operacional de aquisição; não é parecer jurídico nem revoga licenças, contratos ou legislação aplicável. Quando houver conflito ou ambiguidade material, documentar a restrição específica e escalar para validação competente.
