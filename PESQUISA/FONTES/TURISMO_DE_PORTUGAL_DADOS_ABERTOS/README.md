# Turismo de Portugal — Dados Abertos

## Fonte oficial
https://dadosabertos.turismodeportugal.pt/

Plataforma de Dados Abertos Georreferenciados do Turismo de Portugal, I.P., com dados de informação turística para Portugal Continental.

## Categorias visíveis no portal
- Alojamento Turístico
- Equipamentos, Infraestruturas e Atividades Turísticas
- Ordenamento Turístico

## API oficial
Documentação:
https://dadosabertos.turismodeportugal.pt/api/search/definition/

A API é uma OGC API - Records, versão documentada 1.0.0.

## Endpoints identificados
- GET /api/search/v1/catalog
- GET /api/search/v1/collections
- GET /api/search/v1/collections/{collectionId}
- GET /api/search/v1/collections/{collectionId}/queryables
- GET /api/search/v1/collections/{collectionId}/items
- GET /api/search/v1/collections/{collectionId}/items/{itemId}
- GET /api/search/v1/collections/{collectionId}/items/{recordId}/related
- GET /api/search/v1/collections/{collectionId}/items/{recordId}/connected
- GET /api/search/v1/collections/{collectionId}/aggregations
- GET /api/search/v1
- GET /api/search/v1/conformance

Também existe uma área Geoservice-Beta com endpoints FeatureServer.

## Relevância para TURISTURIS
Esta fonte deve ser investigada como fonte estruturada nacional para:
- alojamento turístico;
- informação georreferenciada;
- reconciliação com RNAL;
- comparação com a fonte municipal de Tomar.

## Regra de qualidade
Não assumir que determinada coleção ou campo contém RNAL sem inspeção efetiva da coleção, queryables e itens.

## Estado da descarga
INVENTÁRIO_INICIAL_REGISTADO — a ferramenta atual conseguiu consultar a página oficial e a documentação da API, mas não conseguiu descarregar diretamente o catálogo completo/API de coleções. O portal/API deve ser descarregado de forma controlada numa execução com acesso HTTP funcional.

## Próximo passo
1. Obter /api/search/v1/catalog.
2. Obter /api/search/v1/collections.
3. Enumerar todas as collections.
4. Para cada collection, guardar metadados e queryables.
5. Descarregar os itens/datasets disponíveis em formatos suportados.
6. Preservar URLs, timestamps, metadados e checksums.
7. Identificar especificamente as collections de Alojamento Turístico.
