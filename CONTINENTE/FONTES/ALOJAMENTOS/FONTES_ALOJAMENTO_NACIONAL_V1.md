# WEB-12 — Fontes nacionais de alojamento

## Objetivo

Estabelecer as fontes oficiais para a ingestão nacional de alojamento do TURISTURIS, sem inventar dados e sem confundir consulta pública com dados já incorporados ao repositório.

## Fonte primária — Turismo de Portugal / Registo Nacional de Turismo

O Registo Nacional de Turismo (RNT) centraliza quatro registos de atividade turística, incluindo:

- RNET — Registo Nacional de Empreendimentos Turísticos;
- RNAL — Registo Nacional de Estabelecimentos de Alojamento Local.

O Turismo de Portugal informa que a plataforma de Dados Abertos Georreferenciados disponibiliza dados de alojamento turístico em vários formatos e que o acesso aos dados é livre para reutilização.

**Portal:** https://rnt.turismodeportugal.pt/RNT/RNET.aspx

**Verificação:** 2026-10-06.

## Fonte estruturada — RNET / ArcGIS REST

Serviço oficial:

https://geo.turismodeportugal.pt/server/rest/services/TDP/OpenData_ETExistentes/MapServer

Camada utilizada:

- ID: 0
- Nome: ET Existentes
- Tipo: Feature Layer
- Geometria: polígono
- Formatos de consulta: JSON, GeoJSON e PBF
- Paginação: suportada
- Ordenação: suportada
- Consultas avançadas/SQL: suportadas.

Campos relevantes confirmados na camada:

- NrRNET
- Denominacao
- EntProprietaria
- EntExploradora
- TipologiaET
- Categoria
- NrUnidAloj
- NrCamasFixas
- NrQuartos
- NrSuites
- NrApart
- NrMoradias
- NrCampistas
- DataTituloValAbert
- Website
- Email
- Endereco
- CodigoPostal
- LocalidadeCP
- LatLong
- FiabilidadeGeo
- Freguesia
- Concelho
- Distrito
- NUTSIII
- NUTSII
- ERT
- SeloCleanSafe

**Verificação:** 2026-10-06.

## Fonte estruturada — RNAL / ArcGIS REST

Serviço oficial:

https://geo.turismodeportugal.pt/server/rest/services/TDP/OpenData_AL/MapServer

Camada utilizada:

- ID: 6
- Nome: Alojamento Local
- Tipo: Feature Layer
- Geometria: ponto
- Formatos de consulta: JSON, GeoJSON e PBF
- Paginação: suportada
- Ordenação: suportada
- Consultas avançadas/SQL: suportadas.

Campos relevantes confirmados:

- NrRNAL
- Denominacao
- DataRegisto
- DataAberturaPublico
- Modalidade
- NrUtentes
- Endereco
- CodigoPostal
- LOCALIDADE
- LatLong
- FiabilidadeGeo
- Freguesia
- Concelho
- Distrito
- NUTSIII
- NUTSII
- ERT
- SeloCleanSafe

**Verificação:** 2026-10-06.

## Quantidade de referência observada no RNT

Na consulta do RNT em 2026-10-06:

- RNAL: 120.102 estabelecimentos registados;
- RNET: 6.098 empreendimentos registados.

Esses números são indicadores da fonte no momento da consulta. Não são ainda a quantidade de registros importados pelo TURISTURIS.

## Regra de proveniência

Cada registro ingerido deverá conservar:

1. identificador do registro oficial (RNAL ou RNET);
2. fonte oficial;
3. URL/endpoint de origem;
4. data de verificação;
5. estado de validação;
6. grau de confiança;
7. campos efetivamente disponíveis na fonte.

## Limites desta fase

Esta fase **não** publica ainda os alojamentos no site.

Não foram assumidos:

- preços;
- disponibilidade;
- avaliações;
- classificações comerciais de terceiros;
- contactos não presentes na fonte oficial.

Esses dados somente poderão entrar por fontes adicionais identificadas e verificadas.

## Licenciamento

O Turismo de Portugal declara acesso livre aos dados abertos georreferenciados para reutilização. A licença jurídica específica de cada recurso deverá ser registrada separadamente quando identificada na documentação/metadados do recurso.

## Próxima fase

**WEB-12.1 — Ingestão nacional controlada**

1. consultar RNET e RNAL pelos serviços estruturados;
2. preservar uma cópia RAW identificável;
3. normalizar para o esquema de entidade do TURISTURIS;
4. deduplicar sem eliminar identificadores oficiais;
5. validar cobertura territorial;
6. gerar catálogo nacional publicável;
7. somente então conectar a publicação ao GitHub Pages.
