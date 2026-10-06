# WEB-12.3 — Validação nacional de alojamentos

## Estado

**IMPLEMENTAÇÃO PREPARADA — execução controlada em PR.**

A WEB-12.3 valida estruturalmente e quanto à proveniência os dados produzidos pela WEB-12.2.

## Escopo

- RNET e RNAL permanecem independentes.
- Contagens devem coincidir com o manifesto da WEB-12.2.
- IDs devem ser únicos dentro de cada conjunto.
- IDs devem respeitar os prefixos canônicos RNET/RNAL.
- A proveniência deve conter o identificador da fonte.
- Estado inicial permanece `EM_VERIFICACAO`.
- Grau de confiança permanece `MÉDIO`.
- Campos sem confirmação não são preenchidos por inferência.

## Entrada

Artefato `TURISTURIS-WEB-12.2-NORMALIZADO`, Run #1, proveniente da WEB-12.2.

## Saída

`TURISTURIS-WEB-12.3-VALIDACAO`, contendo a evidência JSON da validação.

## Sequência oficial

`FONTES → RAW → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO`

A publicação permanece bloqueada até a validação ser aprovada.
