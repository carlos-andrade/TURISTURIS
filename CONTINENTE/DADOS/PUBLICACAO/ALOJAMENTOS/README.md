# WEB-12.5 — Catálogo público de alojamentos com contactos

## Objetivo

Melhorar a ficha pública de cada alojamento para apresentar, quando disponíveis e públicos:

- morada;
- telefone;
- email;
- website;
- ficha oficial no Registo Nacional de Turismo.

## Regra de publicação

O TURISTURIS não inventa contactos. Só publica telefone/email quando estes estiverem efetivamente presentes nos dados normalizados.

A ficha oficial do RNT permanece disponível para consulta dos dados públicos adicionais. O RNAL disponibiliza, nas fichas públicas individuais, a identificação e os contactos do titular da exploração; estes contactos serão incorporados ao catálogo por uma etapa específica de enriquecimento, sem substituir a fonte oficial.

## Estado

- WEB-12.4: catálogo nacional publicado com morada/endereço, email e website quando presentes.
- WEB-12.5: modelo de publicação ampliado para morada + telefone + email + ficha oficial.
- Enriquecimento telefónico RNAL: **pendente de execução controlada**; a camada ArcGIS RNAL não fornece telefone no conjunto estruturado utilizado na ingestão.
- Fonte oficial: Registo Nacional de Turismo / RNAL e RNET.

## Proveniência

Cada registro mantém:

- fonte;
- id_origem;
- ficha_oficial;
- estado_validação;
- grau_confiança.

A informação de contacto deve ser tratada como dado volátil e verificada na data da recolha.