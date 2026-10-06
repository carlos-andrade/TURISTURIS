# TURISTURIS — ROADMAP ATUAL

**Data de atualização:** 2026-10-06  
**Âmbito:** povoamento do site — TOMAR

## 1. Cadeia de execução

PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → FONTES → DADOS RAW → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO → SITE

## 2. Estado geral

| Frente | Estado | Resultado |
|---|---|---|
| Fontes oficiais Turismo de Portugal | ✅ CONCLUÍDA | Fontes preservadas no repositório |
| Fonte territorial DGAL | ✅ CONCLUÍDA | Referência territorial arquivada |
| Auditoria territorial TOMAR | ✅ CONCLUÍDA | Município/distrito/freguesias identificados |
| RNAL TOMAR — descoberta | ✅ CONCLUÍDA | 274 registos |
| RNAL TOMAR — captura de fichas | ✅ CONCLUÍDA | 274/274 capturados com sucesso |
| RNAL TOMAR — publicação | ✅ PUBLICADA | Catálogo público com 274 registos |
| TOMAR — pontos turísticos principais | ✅ PUBLICADO | 4 fichas principais |
| TOMAR — catálogo complementar | ✅ PUBLICADO | 12 pontos adicionais |
| TOMAR — T1 proveniência | ✅ CONCLUÍDO | 25/25 com proveniência persistida |
| TOMAR — T1 operacional | ✅ CONCLUÍDO | 25/25 com evidência operacional persistida |
| TOMAR — validação estrutural | ✅ PASS | Auditoria formal persistida no PR #70 |
| TOMAR — validação de conteúdo | 🔄 22/25 | 22 confirmados por fonte oficial; 3 pendentes |
| TOMAR — experiências | ✅ PUBLICADO | Seleção inicial com proveniência |
| TOMAR — transportes | ✅ PUBLICADO | CP, Rede Expressos e TUTomar |
| TOMAR — restauração | 🔄 INICIAL | Seleção inicial; expansão pendente |
| TOMAR — museus/cultura | 🔄 EM ENRIQUECIMENTO | Informação oficial a incorporar |
| TOMAR — acessibilidade | ⏳ PENDENTE | Recolher dados específicos por entidade |
| TOMAR — fotografias/imagens | ⏳ PENDENTE | Só após proveniência/licença adequada |
| Integração nacional do conteúdo TOMAR | ⏳ PENDENTE | Ligar catálogo Tomar à camada nacional |

## 3. Próxima sequência obrigatória

### FASE T1 — Validação de conteúdo

1. Confirmar os 22 registos com fonte oficial identificável.
2. Manter os 3 registos pendentes explicitamente identificados.
3. Não converter ausência de resultado em inexistência.
4. Não inferir conteúdo turístico.
5. Não promover automaticamente estados internos para VERIFICADO.
6. Persistir toda a evidência no repositório através de PR → Gate → merge.

### FASE T2 — Cultura e museus

Expandir o catálogo com equipamentos oficiais ainda não representados.

### FASE T3 — Restauração

Expandir a seleção a partir do catálogo oficial Turismo de Tomar.

### FASE T4 — Experiências

Expandir visitas guiadas, animação turística e atividades.

### FASE T5 — Acessibilidade

Criar camada específica para acessibilidade física e de visita.

### FASE T6 — Imagens

Associar imagens somente quando a proveniência e os direitos de utilização estiverem determinados.

### FASE T7 — Integração nacional

Ligar o conteúdo Tomar à camada nacional do SITE sem duplicar dados canónicos.

## 4. Regras permanentes

- ChatGPT não deixa resultados de pesquisa apenas no chat: resultados úteis devem ser persistidos no repositório.
- Fonte → evidência → validação → publicação.
- Não inventar dados.
- record_count deriva da extração real.
- Território público: Freguesia → Município → Distrito.
- Freguesia não é inferida destrutivamente.
- Telefone: preserve_explicitly; nunca remover ou substituir o código internacional explícito.
- Estado interno de validação não é publicado no site.
- Fases concluídas não são repetidas nem executadas fora de ordem.
- Alterações de SITE seguem branch → PR → checks → merge → GitHub Pages.

## 5. Situação atual

**TOMAR está em povoamento ativo do SITE.**

T1 — enriquecimento está concluído. A validação estrutural passou e foi formalmente persistida pelo PR #70.

A validação de conteúdo identificou **22/25 registos confirmados por fontes oficiais atuais identificáveis** e **3/25 pendentes**:
- Jardim das Musas;
- Jardim Manuel Costa Rosa;
- Casa dos Vereadores.

A evidência detalhada está em:

PESQUISA/AUDITORIAS/TOMAR_T1_VALIDACAO_CONTEUDO_2026-10-06.md

Os três pendentes não devem ser preenchidos por inferência nem considerados confirmados até surgir nova evidência oficial.
