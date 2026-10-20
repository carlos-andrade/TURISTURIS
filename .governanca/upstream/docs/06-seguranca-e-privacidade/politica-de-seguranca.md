# Política-base de segurança
| Campo | Valor |
|---|---|
| **ID** | GOV-SEC-POL-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | POLITICA |
| **Fase** | Segurança e privacidade |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | c5d81d1c88d3726d1d66d091a1384622e9640a23a4f2808ba967e92746aac02e |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/06-seguranca-e-privacidade/politica-de-seguranca.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Proteger confidencialidade, integridade, disponibilidade e rastreabilidade dentro de um modelo de ameaça definido.

Controlos proporcionais: inventário; menor privilégio; autenticação robusta; revisão de acessos; separação de ambientes; credenciais por finalidade e prazo; cofre de segredos e rotação; correções priorizadas por exposição; análise de dependências e configurações; backups protegidos e testados; logs úteis sem segredos; canal de reporte de vulnerabilidades; resposta a incidentes; revogação no encerramento.

Antes de publicar código, verificar histórico por segredos, direitos, dados e configurações de produção. Apagar o segredo num commit novo não apaga as cópias históricas; revogar e rodar credenciais é prioritário. Notificações externas dependem do caso e da obrigação aplicável.