# Instalação

| Campo | Valor |
|---|---|
| **ID** | GOV-WD-INST-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | GUIA_OPERACIONAL |
| **Fase** | WATCHDOG — instalação |
| **Estado** | EM_REVISAO |
| **Versão** | 1.0.0 |
| **SHA-256 (conteúdo canónico)** | 8764d33a4bf8090095fffba16a80e17868f63a8d4e52a5ce2439988b01e9a4e6 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-14 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Pendente de aprovação formal deste documento |
| **Origem** | Conteúdo existente em `WATCHDOG/docs/instalacao.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) e [Norma de cabeçalho](../../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

Requisitos do MVP: Python 3.10 ou superior, sem dependências externas.

Na raiz do repositório:

```bash
python -m unittest discover -s WATCHDOG/tests -v
python WATCHDOG/engine/watchdog.py --check
```

O validador imprime JSON para stdout. Código de saída 2 indica erro de configuração/execução; código 1 indica falha verificável; código 0 indica que não foi encontrada falha verificável. Um resultado `UNKNOWN` permanece visível e não equivale a cobertura operacional completa.

O workflow GitHub Actions executa os testes quando há alterações no diretório WATCHDOG. Isso valida o código versionado, não instala um agente contínuo em sistemas externos.
