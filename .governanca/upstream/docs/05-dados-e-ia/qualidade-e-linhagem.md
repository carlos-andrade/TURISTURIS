# Qualidade, proveniência e linhagem de dados
| Campo | Valor |
|---|---|
| **ID** | GOV-DATA-QLT-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PADRAO |
| **Fase** | Dados e IA |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 13da09e7ebc4f00533b44d203ff59323d25416943ceacb6ac9a57d821661856d |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/05-dados-e-ia/qualidade-e-linhagem.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Para cada dataset crítico, declarar owner, descrição, granularidade, esquema, origem, frequência, regras de qualidade, consumidores, classificação, retenção, limitações e contacto operacional.

Validar esquemas, tipos, domínios, obrigatoriedade, duplicados, nulos, atrasos, saltos e alterações de esquema. Registar contagens de entrada/saída e reconciliação em pipelines críticos. Preservar origem, timestamp e versão da transformação. Definir quarentena/reprocessamento para dados inválidos. Distinguir zero, nulo, desconhecido, não aplicável e não recebido.

Ligar origem → transformação → ativo derivado → relatório/modelo → consumidor. Mudanças semânticas exigem análise de compatibilidade.