# TURISTURIS — T1 ENRIQUECIMENTO TOMAR — EVIDÊNCIA DE FONTES OFICIAIS

**Data:** 2026-10-06  
**Projeto:** TURISTURIS  
**Âmbito:** TOMAR — pontos de interesse  
**Fase:** T1 — Enriquecimento das fichas  
**Estado:** EM EXECUÇÃO  

## Correção de processo

A verificação do estado atual mostrou que a proposta anterior de saltar diretamente para uma formalização de validação não era a próxima etapa correta. O ROADMAP determina primeiro T1 — enriquecimento das fichas.

Esta evidência corrige a sequência sem promover automaticamente registos para VERIFICADO.

## Fontes oficiais confirmadas

| Registo | Fonte oficial |
|---|---|
| Pelourinho de Tomar | https://turismo.cm-tomar.pt/poi/pelourinho-de-tomar |
| Capela da Nossa Senhora da Piedade | https://turismo.cm-tomar.pt/poi/capela-da-nossa-senhora-da-piedade |
| Parque do Mouchão | https://turismo.cm-tomar.pt/poi/parque-do-mouchao |
| Mata Nacional dos Sete Montes | https://turismo.cm-tomar.pt/poi/mata-nacional-dos-sete-montes-or-cerca-do-convento-de-cristo |
| Igreja de Santa Maria do Olival | https://www.turismo.cm-tomar.pt/poi/igreja-de-santa-maria-do-olival |
| Casa dos Cubos / CEFT | https://www.turismo.cm-tomar.pt/poi/casa-dos-cubos-or-centro-de-estudos-em-fotografia-de-tomar |
| Complexo Cultural da Levada | https://turismo.cm-tomar.pt/poi/complexo-cultural-da-levada-de-tomar |
| Museu dos Fósforos | https://turismo.cm-tomar.pt/poi/museu-dos-fosforos |
| NAC — Núcleo de Arte Contemporânea | https://turismo.cm-tomar.pt/poi/nucleo-de-arte-contemporanea-museu-municipal |
| Ermida de Nossa Senhora da Conceição | https://www.turismo.cm-tomar.pt/poi/ermida-de-nossa-senhora-da-conceicao |
| Igreja e Convento de São Francisco | https://turismo.cm-tomar.pt/poi/igreja-e-convento-de-sao-francisco |
| Centro Interpretativo Tomar Templário | https://turismo.cm-tomar.pt/poi/centro-interpretativo-tomar-templario |
| Convento de Santa Iria | https://turismo.cm-tomar.pt/poi/percurso-historico |

## Fonte oficial transversal

Mapa turístico municipal de Tomar 2025:
https://www.cm-tomar.pt/images/CMT/visitar/Mapa%20Tomar%202025%20-%2012%20-%20FINAL_compressed.pdf

O mapa oficial confirma o enquadramento de monumentos, igrejas/capelas, edifícios de interesse, núcleos museológicos, jardins/parques e equipamentos culturais do catálogo de Tomar.

## Regra de publicação

Esta evidência não altera por si só o estado de validação dos registos. A existência de uma página oficial confirma a fonte, mas cada campo operacional continua sujeito à verificação específica correspondente.

- horários são dados voláteis;
- contactos devem preservar o código internacional explícito;
- preços e disponibilidade só entram com fonte específica;
- não se infere freguesia;
- estados internos de validação não são expostos no SITE.

## Próximo checkpoint

Completar a ligação entre as fichas individuais existentes e as fontes oficiais específicas; depois executar validação estrutural e de conteúdo antes de qualquer promoção para VERIFICADO.

## Execução T1 — proveniência enriquecida

Foi criado `CONTINENTE/DADOS/PUBLICACAO/TOMAR_PONTOS_INTERESSE_T1_ENRIQUECIDOS_V1.json` com **25/25** pontos, `record_count` derivado da coleção real, data de verificação e `fonte_url` por registo.

- **20** registos apontam para páginas oficiais individuais identificadas.
- **5** registos mantêm a camada oficial de catálogo (`Places/Index/wtd`) porque não foi encontrada, nesta execução, uma página individual inequívoca sem risco de associação incorreta.
- Nenhum registo foi promovido para `VERIFICADO`.
- Dados voláteis não foram inventados nem acrescentados sem evidência específica.

Esta execução fecha o checkpoint de **proveniência T1** para os 25 pontos, mas não fecha toda a FASE T1, porque ainda há campos operacionais a enriquecer quando houver evidência específica.


## Correção de classificação de proveniência — 2026-10-06

Foi corrigida a classificação dos registos sem página individual inequívoca. Os **5 pontos** ligados apenas ao catálogo oficial `Places/Index/wtd` passam a ter `tipo_fonte = catalogo_oficial`; não são classificados como `pagina_oficial`. Os **20 pontos** com URL individual inequívoca permanecem como `pagina_oficial`.

A correção não altera `record_count` (25), não promove estados de validação e não acrescenta dados operacionais sem evidência específica.


## Correção de contagem da proveniência — 2026-10-06

A verificação do artefacto publicado em `main` confirmou `record_count = 25`, dos quais **20** possuem `fonte_url` de página oficial individual e **5** apontam exclusivamente para o catálogo oficial `Places/Index/wtd`. A redação anterior desta auditoria indicava 19/6 e estava incorreta. Esta correção alinha a evidência com o conteúdo efetivamente persistido no repositório. Não há alteração dos 25 registos nem promoção de estado de validação.


## Correção de fontes genéricas de percurso — 2026-10-06

A verificação semântica das URLs identificou dois registos — Ponte D. Manuel I / Ponte Velha e Roda do Mouchão — que apontavam para `poi/percurso-historico`, uma página transversal de percurso, e não para uma ficha individual inequívoca. Ambos foram reclassificados como `catalogo_oficial` e passaram a usar a fonte de catálogo oficial. O conjunto fica em **20 páginas individuais + 5 catálogo oficial**, mantendo `record_count = 25` e sem promoção de validação.


## Execução T1 — enriquecimento operacional — 2026-10-06

Foi executado enriquecimento operacional com base exclusivamente em páginas oficiais do Turismo de Tomar. Foram enriquecidos **17/25** registos com um bloco `operacional` persistido no JSON, contendo apenas campos encontrados na fonte correspondente (horários, contactos, moradas, email, website e/ou aviso/estado operacional quando explicitamente apresentado).

- Código telefónico internacional preservado explicitamente como `+351` quando apresentado pela fonte.
- A Mata Nacional dos Sete Montes e a Capela de São Gregório mantêm o aviso de encerramento temporário encontrado na fonte oficial.
- A Ermida de Nossa Senhora da Conceição é persistida como encerrada porque a fonte oficial apresenta explicitamente “Encerrada”.
- Os restantes **8/25** continuam sem dados operacionais específicos suficientes nesta execução; não foram preenchidos por inferência.
- Nenhum registo foi promovido para `VERIFICADO`.

O checkpoint operacional T1 foi executado parcialmente: a proveniência permanece completa para 25/25 e o enriquecimento operacional agora cobre 17/25. A validação formal continua bloqueada até conclusão do enriquecimento T1 definido no ROADMAP.


## Nova execução — evidências operacionais adicionais — 2026-10-06

Nova verificação das fontes oficiais acrescentou dados operacionais/proveniência específica a **5 pontos**: Convento de Santa Iria, Palácio de Alvaiázere, Ponte D. Manuel I / Ponte Velha, Roda do Mouchão e Charolinha. O total com bloco operacional persistido passa de 17/25 para **22/25**.

- Convento de Santa Iria: horário, contacto +351 249 329 823, morada e email.
- Palácio de Alvaiázere: morada oficial.
- Ponte D. Manuel I / Ponte Velha: descrição específica na rota histórica oficial.
- Roda do Mouchão: descrição específica e morada oficial.
- Charolinha: descrição específica na fonte oficial do catálogo.

Persistem **3/25** registos sem dados operacionais específicos suficientes nesta execução: Jardim das Musas, Jardim Manuel Costa Rosa e Casa dos Vereadores. Não foram preenchidos por inferência.

A validação formal continua bloqueada enquanto estes três registos não tiverem evidência operacional suficiente, salvo decisão formal de encerramento de T1 por suficiência de dados.
