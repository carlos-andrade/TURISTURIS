# FICHAS OFICIAIS RNET

## Função

Repositório documental das **fichas oficiais RNET — Registo Nacional de Empreendimentos Turísticos**, obtidas a partir das fontes oficiais do Turismo de Portugal.

## Objetivo

Concentrar, preservar e organizar fichas RNET de forma integral, rastreável, reproduzível e auditável, mantendo separação absoluta dos dados RNAL.

## Fonte primária

A captura deve ser feita diretamente das páginas oficiais RNET do RNT.

- RNET nº **6803**
- Fonte: https://rnt.turismodeportugal.pt/RNT/RNET.aspx?nr=6803

## Estrutura

Para cada ficha:

- `<numero_registo>/raw/` — evidência bruta da fonte.
- `<numero_registo>/structured/` — dados estruturados em JSON/CSV.
- `<numero_registo>/audit/` — manifesto, hashes e metadados da captura.

## Integridade e auditoria

O conteúdo original não deve ser sobrescrito por normalizações.

Cada registro estruturado deve possuir chave única e determinística, permitindo rastrear o dado até a ficha e à posição capturada. A evidência bruta e seus hashes permitem comparar futuras capturas.

## Regra de captura

A captura deve obedecer à `CARTAS/CARTA_CAPTURA_RIGIDA_FICHAS_RNET_RNAL.md`.

É proibido completar, corrigir ou inferir dados que não estejam publicados na fonte oficial.

## Separação

Esta pasta é exclusiva de **RNET**. Dados RNAL permanecem em `FICHAS OFICIAIS RNAL/`.

## Estado

Esta é a camada de **evidência documental oficial RNET** do TURISTURIS. Os dados somente podem alimentar normalização e povoamento do site depois da validação da captura.
