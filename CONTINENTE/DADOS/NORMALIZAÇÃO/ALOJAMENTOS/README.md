# WEB-12.2 — NORMALIZAÇÃO NACIONAL DE ALOJAMENTOS

## Estado
IMPLEMENTAÇÃO PREPARADA — execução controlada pendente.

## Regra
RNET e RNAL são normalizados separadamente. Não existe deduplicação ou fusão automática entre fontes nesta fase.

## Mapeamento
O processo segue GOVERNANÇA/LAYOUT/LAYOUT_MESTRE.md e CONTINENTE/DADOS/ESQUEMA_ENTIDADE_V1.md.
Campos sem confirmação na fonte permanecem vazios. Não são criados dados por inferência.

## Identidade
- RNET preserva NrRNET.
- RNAL preserva NrRNAL.
- O ID canônico incorpora a fonte e o identificador de origem.
- A geometria é preservada quando fornecida.
- A proveniência acompanha cada registro.

## Validação inicial
Todos os registros entram como EM_VERIFICACAO e MÉDIO. A mudança para VERIFICADO exige etapa própria.

## Saídas
- RNET_NORMALIZADO_V1.json
- RNAL_NORMALIZADO_V1.json
- MANIFESTO_NORMALIZACAO_V1.json

## Sequência
FONTES → RAW → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO

A publicação não faz parte da WEB-12.2.
