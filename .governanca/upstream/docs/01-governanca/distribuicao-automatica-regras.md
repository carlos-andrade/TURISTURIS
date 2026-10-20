# Distribuição automática das regras canónicas

| Campo | Valor |
|---|---|
| **ID** | GOV-DIST-001 |
| **Projeto** | GOVERNANÇA |
| **Estado** | IMPLEMENTAÇÃO INICIAL — validação operacional pendente |
| **Versão** | 1.0.0 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) |

## Objetivo

Quando um documento canónico de distribuição é alterado e publicado em `main`, gerar uma proposta de atualização nos repositórios consumidores registados em `registry/repositorios-consumidores.json`.

## Mecanismo

1. O workflow `propagar-regras-governanca.yml` é acionado por alterações aos ficheiros canónicos ou manualmente.
2. O script valida o registo e a allowlist de ficheiros.
3. Descobre automaticamente os ficheiros de texto dos diretórios normativos registados (`standards/`, `docs/`, `templates/`, `CABEÇALHO/`, `WATCHDOG/`) e os três documentos canónicos da raiz; copia-os para `.governanca/upstream/`.
4. Gera `UPSTREAM-MANIFEST.json` com commit de origem e SHA-256 de cada ficheiro.
5. Cria ou atualiza a branch `bot/sincronizar-regras-governanca` e abre uma Pull Request.
6. O repositório consumidor revê e aprova a PR segundo as regras locais.

## Controlos

- **Sem merge automático:** publicação significa propor alterações, não impor alterações na branch principal.
- **Sem sobrescrita de ficheiros locais:** a distribuição fica isolada em `.governanca/upstream/`.
- **Fail-closed:** registo inválido, ficheiros ausentes ou falha de autenticação bloqueiam o processo.
- **Rastreabilidade:** o manifesto inclui commit de origem e SHA-256.
- **Idempotência:** se o espelho já estiver igual, não abre nova PR.
- **Escopo explícito:** só repositórios ativos no registo recebem propostas.
- **Sem certificação implícita:** a presença do espelho não significa adoção ou conformidade.

## Configuração necessária

Criar o secret `GOVERNANCA_SYNC_TOKEN` no repositório GOVERNANCA. O token deve ter acesso mínimo aos repositórios listados, com permissões de escrita em Contents e Pull requests. Recomenda-se um fine-grained PAT limitado a esses repositórios.

O `GITHUB_TOKEN` padrão do repositório de origem não concede automaticamente escrita nos repositórios consumidores.

## Execução local

```bash
python automation/propagar_governanca.py --dry-run
python automation/propagar_governanca.py --repo carlos-andrade/B3 --dry-run
python automation/propagar_governanca.py
```

## Critérios de aceitação

- [ ] JSON válido e sem duplicados.
- [ ] `--dry-run` executado com autenticação real.
- [ ] PR criada/atualizada em cada repositório ativo.
- [ ] Manifesto com commit de origem e SHA-256 verificados.
- [ ] Falha de um destino visível no relatório.
- [ ] Idempotência verificada.
- [ ] Permissões revistas e ausência de merge automático confirmada.

## Limites conhecidos

A automação distribui cópias isoladas de todos os ficheiros de texto elegíveis dentro das raízes normativas explicitamente registadas. Não replica automaticamente o código de aplicação nem ficheiros fora dessas raízes; não altera documentos locais, não aprova decisões e não força adoção substantiva. Uma nova raiz normativa exige alteração explícita do registo, do validador, dos filtros do workflow e dos testes.
