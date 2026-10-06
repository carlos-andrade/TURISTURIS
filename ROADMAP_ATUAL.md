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
| FASE NACIONAL 0 — inventário | 🔄 EM EXECUÇÃO | Inventário persistido em `PESQUISA/INVENTARIOS/` |
| FASE NACIONAL 1 — território | ⏳ PRÓXIMA | Reconciliar camada territorial nacional |
| FASE NACIONAL 2 — turismo | ⏳ PENDENTE | Integrar pontos turísticos existentes |
| FASE NACIONAL 3 — alojamento | ⏳ PENDENTE | Expandir RNAL/RNET disponíveis |
| FASE NACIONAL 4 — restauração | ⏳ PENDENTE | Integrar dados existentes e fontes oficiais |
| FASE NACIONAL 5 — experiências | ⏳ PENDENTE | Expandir por território |
| FASE NACIONAL 6 — transportes | ⏳ PENDENTE | Expandir por território |
| FASE NACIONAL 7 — cultura | ⏳ PENDENTE | Museus/património/equipamentos |
| FASE NACIONAL 8 — acessibilidade | ⏳ PENDENTE | Dados específicos por entidade |
| FASE NACIONAL 9 — SITE | ⏳ BLOQUEADA ATÉ VALIDAÇÃO | Publicar somente datasets nacionais validados |

## 3. FASE NACIONAL 0 — INVENTÁRIO

**Estado:** 🔄 EM EXECUÇÃO

Objetivo: localizar e catalogar tudo o que já está efetivamente persistido nos repositórios turísticos relevantes antes de reconstruir dados.

Inventário inicial confirmado:

- TURISTURIS: 4.854 caminhos na árvore;
- TURISTURIS: 948 JSON;
- normalização municipal: 280 documentos;
- READMEs municipais: 278;
- catálogo municipal publicável: 278 registos;
- pontos turísticos publicáveis: 68;
- RNAL Peso da Régua: 182;
- RNAL TOMAR: 274;
- TOMAR T1: 25;
- TOMAR experiências: 3;
- TOMAR transportes: 3;
- TOMAR restauração: 7;
- repositório turístico complementar TOMAR: 10 pontos turísticos documentados.

Inventário persistido em:

`PESQUISA/INVENTARIOS/INVENTARIO_NACIONAL_DADOS_DISPONIVEIS_2026-10-06.md`

## 4. FASE NACIONAL 1 — TERRITÓRIO

1. Reconciliar o catálogo municipal de 278 registos.
2. Ligar municípios aos distritos.
3. Preservar Açores e Madeira como estruturas próprias.
4. Não inferir freguesias.
5. Criar chaves canónicas sem duplicação.
6. Persistir evidência e auditoria.

## 5. FASE NACIONAL 2 — TURISMO

1. Reconciliar os 68 pontos turísticos publicáveis.
2. Reaproveitar o modelo T1 de TOMAR.
3. Integrar conteúdos municipais existentes.
4. Validar cada entidade por fonte.
5. Separar factual, operacional e volátil.
6. Não publicar estados internos de validação.

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

A mesma estrutura comprovada em TOMAR será aplicada, sem criar um segundo modelo:

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
- Repositório específico TOMAR é fonte de ativos a reconciliar, não segunda fonte canónica.
- Duplicação é proibida; a camada canónica permanece no TURISTURIS.

## 10. Situação atual

TOMAR permanece em povoamento ativo, com 22/25 pontos confirmados por fonte oficial e 3 pendentes.

Paralelamente, foi iniciada formalmente a integração nacional pela **FASE NACIONAL 0 — INVENTÁRIO**.

### Próximo checkpoint

**FASE NACIONAL 1 — TERRITÓRIO**

A integração nacional deve começar pelos dados já existentes. Não se parte do zero.
