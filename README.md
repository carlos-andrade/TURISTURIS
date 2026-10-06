# TURISTURIS

## Inteligência turística de Portugal

> Como podemos obter informações valiosas sobre o turismo de Portugal em um só lugar?

O TURISTURIS é um projeto para coletar, organizar, validar e disponibilizar informação turística de Portugal com rastreabilidade de fontes e controle de atualização.

## Princípio arquitetural

CARTAS → LAYOUT MESTRE → DADOS → CÓDIGO

O Layout Mestre é a referência operacional para novos artefatos. As informações devem possuir proveniência identificável e dados voláteis devem ser datados.

## Estrutura inicial

- `CARTAS/` — regras e governança
- `LAYOUT/` — estrutura operacional canônica
- `PORTUGAL/` — organização territorial
- `PONTOS_TURISTICOS/` — atrações e património
- `ALOJAMENTOS/` — hospedagem
- `RESTAURANTES/` — alimentação
- `TRANSPORTES/` — mobilidade turística
- `EXPERIENCIAS/` — atividades
- `CALENDARIO/` — eventos
- `DADOS/` — ingestão e normalização
- `FONTES/` — catálogo de proveniência
- `PESQUISA/` — estudos e metodologia

## Estado

Fundação arquitetural criada em 2026-10-04. A expansão por cidades e entidades deve seguir as regras estabelecidas nas Cartas e no Layout Mestre.


## Regra vital de persistência

A **CARTA-VITAL-001** estabelece que resultados de pesquisa, execução, validação, análise, decisão técnica, evidência e demais artefatos relevantes não podem permanecer exclusivamente em chats. O repositório é a fonte oficial e persistente do projeto. Consulte `CARTAS/CARTA-VITAL-001_PERSISTENCIA_RESULTADOS.md`.
