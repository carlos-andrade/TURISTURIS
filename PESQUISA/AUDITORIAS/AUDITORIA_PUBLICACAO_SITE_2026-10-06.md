# TURISTURIS — AUDITORIA PUBLICAÇÃO → SITE

## Cabeçalho histórico
- Projeto: TURISTURIS
- Documento: AUDITORIA-PUBLICACAO-SITE-2026-10-06
- Tipo: Evidência / auditoria
- Estado: CONCLUÍDA
- Data: 2026-10-06
- Base: branch `main`
- Commit auditado: `668fc9a6307cc5f42b5eda333c902e162de11836`
- Ferramenta: `scripts/auditar_publicacao_site.py`
- Regra: dados sem estado explícito não são promovidos automaticamente.

## Inventário

| Ficheiro | Registos/coleções | Estado | Ação |
|---|---:|---|---|
| AMADORA_PONTOS_TURISTICOS_V1.json | 28 | 28 VERIFICADO | PUBLICAR/COMPLETAR |
| PONTOS_TURISTICOS_PUBLICAVEIS_V1.json | 68 | 28 VERIFICADO; 40 EM_VERIFICACAO | PUBLICAR 28; bloquear 40 |
| RNAL_PESO_DA_REGUA_PUBLICAVEIS_V1.json | 182 | 177 CONFIRMADO_FICHA_OFICIAL; 4 CONFIRMADO_FONTE_PUBLICA; 1 FONTE_HISTORICA_A_VALIDAR | PUBLICAR 181; bloquear 1 |
| RNAL_TOMAR_PUBLICAVEIS_V2.json | 274 | 274 sem estado por registo | REVISÃO MANUAL antes de nova promoção |
| TOMAR_PONTOS_INTERESSE_V1.json | 25 | 25 sem estado | REVISÃO MANUAL |
| TOMAR_EXPERIENCIAS_TRANSPORTES_RESTAURACAO_V1.json | 3 experiências; 3 transportes; 7 restauração | sem estado por item | REVISÃO MANUAL |
| CATALOGO_MUNICIPIOS_NORMALIZADOS_V1.json | 278 | catálogo territorial; operational_publication=false | NÃO PUBLICAR COMO CONTEÚDO TURÍSTICO |

## Resultado

Dados explicitamente prontos para publicação identificados:
- Amadora: 28
- Peso da Régua: 181
- Pontos turísticos nacionais: mais 28, ainda sem página municipal integrada
- Total mínimo imediatamente elegível por estado explícito: **237 registos**

Bloqueados:
- 40 pontos turísticos em `EM_VERIFICACAO`
- 1 RNAL histórico em `FONTE_HISTORICA_A_VALIDAR`

Revisão manual necessária antes de promoção automática:
- 274 RNAL de Tomar
- 25 pontos de interesse de Tomar
- 3 experiências
- 3 transportes
- 7 restaurantes

## Decisão

O mecanismo universal não deve publicar simplesmente "tudo que está em PUBLICACAO". A promoção automática exige estado de publicação explícito. Datasets sem estado individual permanecem em revisão até a regra de validação ser formalizada.

## Próximo passo do roadmap

1. Integrar os 28 pontos turísticos VERIFICADOS que ainda estão no catálogo nacional.
2. Formalizar a validação/publicação dos datasets de Tomar sem estado individual.
3. Só depois ativar o publicador universal.
4. Manter sempre o fluxo:
   CARTA → LAYOUT → DADOS → VALIDAÇÃO → PUBLICAÇÃO → SITE → PR → CHECKS → MERGE → PAGES.
