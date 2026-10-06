# WEB-12.1 — Ingestão nacional de alojamento

## Estado

**IMPLEMENTAÇÃO PREPARADA — EXECUÇÃO CONTROLADA PENDENTE**

A ingestão foi implementada para consultar diretamente os serviços oficiais RNET e RNAL.

### Entradas

- RNET — ET Existentes, camada 0.
- RNAL — Alojamento Local, camada 6.

### Saída RAW

A execução deverá criar:

- `CONTINENTE/DADOS/RAW/ALOJAMENTOS/RNET_RAW_V1.json`
- `CONTINENTE/DADOS/RAW/ALOJAMENTOS/RNAL_RAW_V1.json`
- `CONTINENTE/DADOS/RAW/ALOJAMENTOS/MANIFESTO_INGESTAO_V1.json`

### Proteções

- Consulta com `where=1=1`.
- Paginação por `resultOffset`.
- Ordenação por `OBJECTID`.
- Preservação da geometria.
- Registro do instante UTC da coleta.
- Registro dos endpoints oficiais.
- Falha explícita quando a API retorna erro.
- Nenhuma publicação automática.

## Validação antes da publicação

A sequência obrigatória permanece:

`RAW → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO`

O RAW não será tratado como catálogo público até que a normalização e a validação sejam concluídas.

## Fonte

Os serviços oficiais confirmam suporte a JSON/GeoJSON/PBF e paginação. A camada RNAL é ponto e a RNET é polígono. Os campos oficiais incluem identificadores RNAL/RNET, denominação, endereço, município, distrito e informação de georreferenciação.

**Data de verificação:** 2026-10-06.
