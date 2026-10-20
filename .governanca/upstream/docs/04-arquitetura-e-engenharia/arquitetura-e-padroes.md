# Arquitetura e padrões de engenharia
| Campo | Valor |
|---|---|
| **ID** | GOV-ARQ-PAD-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | PADRAO |
| **Fase** | Arquitetura e engenharia |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | d441b699a4eb22f5e0b686167c7036f8f0710dbff0c2511112fbb4494e01ba79 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-13 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `docs/04-arquitetura-e-engenharia/arquitetura-e-padroes.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Desenhar para requisitos e ameaças reais. Registar limites de confiança, fluxos de dados, dependências, interfaces e modos de falha. Preferir interfaces documentadas e configuração reproduzível. Separar ambientes segundo o risco. Definir observabilidade e recuperação antes de produção. Registar decisões estruturais em ADR.

Rever arquitetura quando houver fronteira de segurança, dados pessoais, integração externa, persistência, autenticação, escala, dependência proprietária crítica ou alteração difícil de reverter.

Artefactos proporcionais: contexto, componentes, implantação, fluxos de dados, contratos, dependências, threat model, ADRs, requisitos não funcionais, capacidade, migração e rollback. Repositórios declaram versões, lint/formatação, testes, configuração, logging sem segredos e política de dependências.