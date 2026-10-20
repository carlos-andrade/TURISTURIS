# Estado e percentual de conclusão do projeto

| Campo | Valor |
|---|---|
| **ID** | GOV-TPL-STATUS-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | TEMPLATE |
| **Fase** | Templates de projeto |
| **Estado** | EM_REVISAO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | 1ab808e3af9df3ddfd801c3dfa373e9169f8975fca234b9143d7cc072275d789 |
| **Commit de referência (versão anterior)** | N/A — referência de commit anterior não localizada nesta execução |
| **Data de criação** | N/A — data histórica de criação não verificada |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Proprietário do repositório GOVERNANCA — aprovação do padrão de status 1.1.0 |
| **Origem** | Conteúdo existente em `templates/projeto/status-do-projeto.md`; corpo substantivo preservado |
| **Autoridade superior** | [CONSTITUICAO.md](../CONSTITUICAO.md) e [Norma de cabeçalho](../CABE%C3%87ALHO/NORMA-CABECALHO-PADRAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

> Copiar para o README ou registo principal do projeto e atualizar com evidências.

**Projeto:** [nome]  
**Responsável:** [nome/papel]  
**Data da última atualização:** AAAA-MM-DD  
**Estado:** Não iniciado | Em início | Em execução | Em finalização | Concluído | Bloqueado | Suspenso | Cancelado  
**Progresso comprovado:** 0% — [░░░░░░░░░░░░░░░░░░░░]  
**Fase atual:** Início | Meio | Fim  
**Próximo marco:** [entrega/gate e data-alvo]  
**Bloqueios relevantes:** [nenhum ou descrição]  
**Evidência principal:** [links para issues, commits, testes, documentos, validações ou publicação]

## Pontuação (100 pontos)

### Início — 20 pontos
- [ ] Objetivo e problema definidos — 5
- [ ] Responsável e partes interessadas identificados — 3
- [ ] Escopo e exclusões registados — 4
- [ ] Riscos e dependências iniciais avaliados — 4
- [ ] Critérios de aceitação e plano aprovados — 4

**Subtotal Início:** [0–20]/20

### Meio — 60 pontos
- [ ] Entregáveis executados contra o plano — [0–30]
- [ ] Requisitos e decisões rastreáveis — [0–10]
- [ ] Testes/revisões proporcionais ao risco — [0–10]
- [ ] Documentação e evidências atualizadas — [0–5]
- [ ] Desvios e riscos identificados, acompanhados e com tratamento ou aceitação documentados — [0–5]

**Subtotal Meio:** [0–60]/60

### Fim — 20 pontos
- [ ] Critérios de aceitação demonstrados — 8
- [ ] Validação/revisão final aprovada — 4
- [ ] Entrega/publicação e operação ou destino final confirmados — 3
- [ ] Documentação e transferência de conhecimento concluídas — 2
- [ ] Aprovação de encerramento e lições aprendidas registadas — 3

**Subtotal Fim:** [0–20]/20

**Total comprovado:** [Início + Meio + Fim]/100 = [percentual]%

## Histórico de estado

| Data | Antes | Depois | Motivo/evidência | Atualizado por |
|---|---:|---:|---|---|
| AAAA-MM-DD | 0% | 0% | Registo inicial | [responsável] |

## Regra de conclusão
Só marcar **100% — Concluído** depois de todos os critérios finais estarem demonstrados e o encerramento ter sido aprovado. Se o projeto for cancelado, registar **Cancelado** e manter o percentual efetivamente comprovado; não forçar 100%.


## Painel visual obrigatório

Quando o projeto estiver no GitHub, incluir a barra textual e o painel visual gerado a partir do registo canónico:

```markdown
![Painel visual de status](assets/status-dashboard.svg)
```

O SVG deve ser gerado automaticamente a partir dos mesmos dados que alimentam a barra do README. Não editar manualmente a imagem nem manter uma percentagem duplicada.

## Registo canónico — esquema v2

O registo de status deve conter `schema_version: 2`, datas `updated_at` e `last_reviewed_at`, `points`, `criteria`, `next_milestone`, `blockers`, `evidence`, `review_note` e `closure_checks`.

Cada critério inclui:
- `id`: identificador único;
- `label`: descrição objetiva;
- `max_points`: pontos máximos;
- `earned_points`: pontos comprovados;
- `evidence`: uma ou mais URLs verificáveis quando `earned_points > 0`.

A soma de `max_points` dos critérios deve ser 20/60/20 por fase; `points` deve ser calculado como a soma de `earned_points`. O validador deve rejeitar discrepâncias, critérios pontuados sem evidência e 100% sem todos os controlos de encerramento aprovados.

## Regra de atualização e auditoria

Ao alterar o estado:
1. Atualizar os critérios, as evidências e as datas no registo canónico.
2. Executar os testes automatizados.
3. Gerar o README e o SVG através do script do projeto.
4. Executar a validação em modo `--check`.
5. Confirmar que o workflow terminou com sucesso e que os artefactos foram publicados.
6. Registar qualquer descida percentual e a respetiva justificação; não a ocultar.

A data de revisão significa apenas que o registo foi revisto; não prova que segredos, alertas, heartbeats, SLAs ou aprovações externas estejam operacionais.
