# WEB-12.6 — Enriquecimento de contactos públicos RNAL

## Objetivo
Recolher, de forma controlada, telefone e email que o RNT publica nas fichas individuais do RNAL.

## Fonte
Registo Nacional de Estabelecimentos de Alojamento Local — Turismo de Portugal.

Cada ficha pública RNAL apresenta os contactos dos titulares quando disponíveis e informa que esses contactos são divulgados nos termos do artigo 10.º do DL 128/2014. A existência dos campos foi verificada em fichas públicas do RNT.

## Regra
- somente dados efetivamente publicados pelo RNT;
- não recolher NIF/NIPC para o catálogo público;
- preservar o número RNAL como chave de origem;
- preservar URL da ficha oficial;
- registar estado de recolha e data;
- falhas de rede não são convertidas em ausência de contacto.

## Escala
O processo foi desenhado para a totalidade dos registros RNAL normalizados. A execução deve ser feita em Actions com controlo de taxa e artefato persistente, antes da promoção para publicação.

## Saída
`CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/RNAL_CONTACTOS_PUBLICOS_V1.json`