# TURISTURIS — ROADMAP ATUAL

**Data de atualização:** 2026-10-06  
**Âmbito:** povoamento TOMAR + integração nacional Portugal

## 1. Cadeia de execução

PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → FONTES → DADOS RAW → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO → SITE

## 2. Estado geral

| Frente | Estado | Resultado |
|---|---|---|
| Fontes oficiais Turismo de Portugal | ✅ CONCLUÍDA | Fontes preservadas no repositório |
| Fonte territorial DGAL | ✅ CONCLUÍDA | Referência territorial arquivada |
| Catálogo municipal continental | ✅ CONCLUÍDO | 278 registos |
| Pontos turísticos publicáveis | ✅ DISPONÍVEL | 68 registos |
| RNAL Peso da Régua | ✅ DISPONÍVEL | 182 registos |
| RNAL TOMAR | ✅ PUBLICADO | 274 registos |
| TOMAR — T1 proveniência | ✅ CONCLUÍDO | 25/25 |
| TOMAR — T1 operacional | ✅ CONCLUÍDO | 25/25 |
| TOMAR — validação estrutural | ✅ PASS | PR #70 |
| TOMAR — validação de conteúdo | 🔄 22/25 | 3 pendentes após segunda verificação |
| TOMAR — experiências | ✅ PUBLICADO | 3 registos |
| TOMAR — transportes | ✅ PUBLICADO | 3 registos |
| TOMAR — restauração | 🔄 INICIAL | 7 registos; expansão pendente |
| Açores — estrutura territorial | 🟡 ESTRUTURA EXISTENTE | Conteúdo turístico ainda por inventariar |
| Madeira — estrutura territorial | 🟡 ESTRUTURA EXISTENTE | Conteúdo turístico ainda por inventariar |
| FASE NACIONAL 0 — inventário | ✅ CONCLUÍDO | Inventário persistido e PR #73 integrado |
| FASE NACIONAL 1 — território | 🔄 EM EXECUÇÃO | 278/278 municípios reconciliados com 18 distritos |
| FASE NACIONAL 2 — turismo | ⏳ PRÓXIMA | Reconciliar 68 pontos turísticos existentes |
| FASE NACIONAL 3 — alojamento | ⏳ PENDENTE | Expandir RNAL/RNET disponíveis |
| FASE NACIONAL 4 — restauração | ⏳ PENDENTE | Integrar dados existentes e fontes oficiais |
| FASE NACIONAL 5 — experiências | ⏳ PENDENTE | Expandir por território |
| FASE NACIONAL 6 — transportes | ⏳ PENDENTE | Expandir por território |
| FASE NACIONAL 7 — cultura | ⏳ PENDENTE | Museus/património/equipamentos |
| FASE NACIONAL 8 — acessibilidade | ⏳ PENDENTE | Dados específicos por entidade |
| FASE NACIONAL 9 — SITE | ⏳ BLOQUEADA ATÉ VALIDAÇÃO | Publicar somente datasets nacionais validados |

## 3. FASE NACIONAL 0 — INVENTÁRIO

**Estado:** ✅ CONCLUÍDO

O inventário nacional foi persistido em:

`PESQUISA/INVENTARIOS/INVENTARIO_NACIONAL_DADOS_DISPONIVEIS_2026-10-06.md`

PR #73 foi submetido, passou o **PR Gate Run #85** com sucesso e foi integrado em `main`.

## 4. FASE NACIONAL 1 — TERRITÓRIO

**Estado:** 🔄 EM EXECUÇÃO

Checkpoint estrutural concluído no branch `fase-nacional-1-territorio`:

- 278 municípios no catálogo;
- 278 municípios na estrutura `CONTINENTE/DISTRITO/`;
- 18 distritos identificados;
- 0 divergências;
- 0 freguesias inferidas;
- 0 dados turísticos promovidos nesta etapa.

Dataset produzido:

`CONTINENTE/DADOS/PUBLICACAO/TERRITORIO_CONTINENTE_RECONCILIADO_V1.json`

Auditoria:

`PESQUISA/AUDITORIAS/NACIONAL_FASE_1_TERRITORIO_2026-10-06.md`

Próximo passo: submeter este checkpoint por PR → Gate → merge.

## 5. FASE NACIONAL 2 — TURISMO

Após a conclusão da FASE 1:

1. reconciliar os 68 pontos turísticos publicáveis;
2. reutilizar o modelo T1 de TOMAR;
3. ligar cada entidade ao território canónico;
4. integrar conteúdos municipais existentes;
5. validar cada entidade por fonte;
6. separar factual, operacional e volátil;
7. não publicar estados internos.

## 6. FASE NACIONAL 3 — ALOJAMENTO

Integrar progressivamente os ativos RNAL/RNET já disponíveis e expandir por território, mantendo:

- ficha oficial;
- contactos públicos;
- código internacional explícito;
- data de verificação;
- proveniência;
- estado interno;
- não duplicação.

## 7. FASES NACIONAIS 4–8

Aplicar o modelo comprovado em TOMAR:

**proveniência → enriquecimento → validação estrutural → validação de conteúdo → publicação**

Categorias:

- restauração;
- experiências;
- transportes;
- cultura;
- acessibilidade.

## 8. FASE NACIONAL 9 — SITE

Nenhuma alteração nacional do SITE será feita por commit direto em `main`.

Fluxo obrigatório:

**branch → PR → checks → merge → GitHub Pages**

O SITE consumirá datasets canónicos publicados, e não documentos editoriais isolados.

## 9. Regras permanentes

- Resultados úteis não permanecem apenas no chat: são persistidos no repositório.
- Fonte → evidência → validação → publicação.
- Não inventar dados.
- `record_count` deriva da extração real.
- Território público: Freguesia → Município → Distrito.
- Freguesia não é inferida destrutivamente.
- Telefone: `preserve_explicitly`; nunca remover ou substituir o código internacional explícito.
- Estado interno de validação não é publicado.
- Fases concluídas não são repetidas nem executadas fora de ordem.
- Dados de outros projetos não turísticos não entram na integração nacional.
- TOMAR é fonte de ativos a reconciliar, não segunda fonte canónica.
- Duplicação é proibida; a camada canónica permanece no TURISTURIS.

## 10. Situação atual

**FASE NACIONAL 0 está concluída.**

**FASE NACIONAL 1 está em execução**, com o checkpoint estrutural de 278/278 municípios reconciliado.

### Próximo checkpoint

**PR da FASE NACIONAL 1 — TERRITÓRIO**

Depois do merge, avançamos linearmente para:

**FASE NACIONAL 2 — TURISMO → 68 pontos turísticos existentes.**

A integração nacional continua a partir dos dados que já temos; não se parte do zero.