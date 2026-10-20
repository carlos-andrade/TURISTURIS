# CABEÇALHO — Estrutura documental canónica

| Campo | Valor |
|---|---|
| **ID** | GOV-CAB-README-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | README |
| **Fase** | Validação do padrão |
| **Estado** | EM_REVISAO |
| **Versão** | 1.5.0 |
| **SHA-256 (conteúdo canónico)** | 9b5342f235b6db19b226fd09a887a3465f9a39348ef14d05b9ec4e304707201c |
| **Commit de referência (versão anterior)** | [b55de1f609e33e8b7cd190507e23f0d183cd6622](https://github.com/carlos-andrade/GOVERNANCA/commit/5d552b1d6217ccbe7a3fe24871d7e4a5195fa122) |
| **Data de criação** | 2026-10-13 |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## Finalidade

Esta pasta centraliza o padrão de cabeçalho documental utilizado nos projetos. **O cabeçalho visível dos ficheiros Markdown deve ser escrito em Markdown nativo, compatível com a renderização do GitHub**, usando título, tabela de metadados e secções hierárquicas.

O YAML é apenas um modelo auxiliar opcional para automação ou catalogação. Não substitui o cabeçalho Markdown visível.

O cabeçalho inclui também um **SHA-256 canónico** para verificação de integridade e um **commit de referência** para navegação até à versão anterior. O algoritmo e as limitações estão definidos na norma.

## Estrutura

- [NORMA-CABECALHO-PADRAO.md](NORMA-CABECALHO-PADRAO.md) — regras e aplicação.
- [MODELO-DOCUMENTO.md](MODELO-DOCUMENTO.md) — modelo canónico Markdown para GitHub.
- [MODELO-CABECALHO.yml](MODELO-CABECALHO.yml) — metadados YAML auxiliares.
- [REGISTO-TIPOS-DOCUMENTAIS.md](REGISTO-TIPOS-DOCUMENTAIS.md) — tipos documentais.
- [CHECKLIST-VALIDACAO.md](CHECKLIST-VALIDACAO.md) — checklist de validação.
- [HISTORICO.md](HISTORICO.md) — histórico de alterações.
- [INVENTARIO-DOCUMENTAL.md](INVENTARIO-DOCUMENTAL.md) — inventário dos 62 ficheiros Markdown e estado estrutural do cabeçalho.
- [INVENTARIO-REPOSITORIOS-ABRANGIDOS.md](INVENTARIO-REPOSITORIOS-ABRANGIDOS.md) — inventário inicial dos repositórios candidatos à adoção transversal.
- [REGISTO-APROVACAO-NORMA-1.0.3.md](REGISTO-APROVACAO-NORMA-1.0.3.md) — evidência da ratificação formal da norma.
- [CLASSIFICACAO-PRE-NORMALIZACAO.md](CLASSIFICACAO-PRE-NORMALIZACAO.md) — classificação não destrutiva dos 50 documentos pendentes.
- [PLANO-LOTES-NORMALIZACAO.md](PLANO-LOTES-NORMALIZACAO.md) — lotes, gates e critérios de execução.
- [ROADMAP-ADOCAO-TRANSVERSAL.md](ROADMAP-ADOCAO-TRANSVERSAL.md) — fases e critérios de adoção.

## Cadeia de autoridade

`PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO`

## Regra de adoção

1. Usar o cabeçalho Markdown definido em `MODELO-DOCUMENTO.md` nos ficheiros Markdown.
2. Usar YAML apenas quando necessário para integração automática.
3. Ao rever documentos existentes, normalizar os metadados sem apagar o histórico nem alterar silenciosamente o conteúdo.
4. Validar IDs, estado, datas, responsável, origem, autoridade e rastreabilidade.
5. Registar exceções justificadas.
6. Não declarar adoção transversal antes da validação em cada repositório.

## Estado de validação

O formato Markdown nativo foi aprovado formalmente na Norma v1.0.3. Após a aplicação dos lotes L1–L7 e a criação do inventário transversal, o inventário identifica 62 ficheiros Markdown: 62 com campos canónicos presentes e 0 pendentes de normalização individual. A aprovação da norma autoriza a execução controlada, mas não constitui aprovação substantiva de cada documento.

## Roadmap de adoção

Consultar [ROADMAP-ADOCAO-TRANSVERSAL.md](ROADMAP-ADOCAO-TRANSVERSAL.md) para fases, critérios de conclusão, evidências e pendências da adoção nos repositórios. A conformidade só é declarada após inventário, verificação e registo por repositório.
