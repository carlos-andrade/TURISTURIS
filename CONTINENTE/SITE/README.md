# SITE — TURISTURIS

## Objetivo

Esta pasta concentra a arquitetura, documentação e artefactos relacionados com a publicação do TURISTURIS na web.

A camada SITE não substitui as Cartas, o Layout Mestre ou os dados do projeto. Ela funciona como camada de publicação.

## Arquitetura conceitual

**CARTAS → LAYOUT MESTRE → DADOS → SITE → WORDPRESS**

O WordPress deve consumir informação estruturada e validada, evitando transformar o CMS na fonte primária dos dados turísticos.

## Objetivos da publicação

- apresentar destinos e entidades turísticas;
- permitir pesquisa por cidade, município, região e categoria;
- publicar pontos turísticos, alojamentos, restaurantes, transportes, experiências e eventos;
- disponibilizar roteiros;
- preservar proveniência das informações;
- indicar data de verificação de informações voláteis;
- permitir evolução futura para pesquisa avançada, mapas e filtros.

## Princípio de separação

- `CARTAS/` — governança e regras;
- `LAYOUT/` — modelo operacional;
- `DADOS/` — informação estruturada;
- `SITE/` — camada de publicação e arquitetura web;
- WordPress — CMS/interface de publicação.

## WordPress

A implementação WordPress deverá ser definida depois de especificarmos:

1. arquitetura de informação;
2. tipos de conteúdo;
3. taxonomias;
4. campos estruturados;
5. estratégia de importação/sincronização;
6. pesquisa e filtros;
7. mapas e geolocalização;
8. SEO;
9. desempenho;
10. segurança e RGPD;
11. fluxo editorial e atualização;
12. hospedagem e backups.

## Regra

Não criar conteúdo duplicado manualmente no WordPress quando o mesmo dado puder ser publicado a partir da base estruturada do TURISTURIS.
