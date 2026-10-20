# Modelo operacional

| Campo | Valor |
|---|---|
| **ID** | GOV-FOU-MOD-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | MODELO_OPERACIONAL |
| **Fase** | Fundamentos |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 0f60c7b96ed8a60c811bb4ee8ef656b3d77e172f6bfcd2cfd1e40db04d9369d8 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/00-fundamentos/modelo-operacional.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Padrão de governança

Usar governança federada: princípios, níveis de risco, taxonomia, gates e formatos comuns no núcleo; execução autónoma pelos domínios dentro desses limites. Data Mesh é opção para domínios de dados maduros, não uma meta universal.

## Intensidade de controlo

- **A — Essencial:** protótipo reversível, baixo risco, sem dados sensíveis. Charter curto, owner, critérios de aceitação, versionamento e decisões críticas.
- **B — Normal:** integração ou uso por terceiros. Acrescentar análise de risco, desenho, revisão, testes, plano de lançamento e suporte.
- **C — Elevado:** produção crítica, dados pessoais/sensíveis ou impacto financeiro/operacional material. Revisão especializada, segregação quando possível, evidência formal, continuidade e autorização explícita.
- **D — Crítico:** serviços essenciais, segurança física, movimento de dinheiro ou alto impacto sobre pessoas. Governação setorial, revisão independente e salvaguardas específicas antes de avançar.

O nível depende da avaliação de risco e pode subir. Desconhecido não significa baixo risco. A classificação interna não substitui classificações legais ou regulatórias.

## Ciclo de controlo

Propor → classificar → planear → desenhar → executar → validar → lançar → observar → melhorar → encerrar. Cada transição tem responsável, evidência, decisão, pendências e risco residual.

## Repositório-mestre e repositórios de projeto

GOVERNANCA mantém políticas comuns, modelos, padrões, registos índice e taxonomia. Cada repositório de projeto mantém código, configuração, testes e evidência específica. Referenciar a versão normativa adotada; evitar duplicação e nunca guardar segredos em Git.

## Automação

Uma ferramenta não é por si só um controlo. Uma automação só é considerada ativa depois de implementada, testada, monitorizada, atribuída a um owner e acompanhada de procedimento de falha.