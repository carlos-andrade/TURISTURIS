# TURISTURIS — CARTA WEB-12.6 NACIONAL

> CONTEXTO HISTÓRICO: 2026-10-07 | Evolução do WEB-12.6 validado em Peso da Régua (182/182).
> ESTADO: PROPOSTA CONTROLADA PARA EXPANSÃO NACIONAL
> REGRA: PROMPT → CARTA → LAYOUT → CÓDIGO

## Objetivo
Aplicar o WEB-12.6 a todos os municípios presentes no universo RNAL normalizado, sem misturar municípios, sem perda de registos e com evidência persistida.

## Regras
- Município é a unidade operacional.
- target_total é derivado do universo RNAL normalizado.
- Cada lote é identificado por município + offset.
- id_origem é a chave de controlo.
- Contactos internacionais preservam explicitamente o código de país.
- Falhas ficam registadas e não são tratadas como sucesso.
- Peso da Régua permanece como regressão obrigatória: 182/182.

## Estados
PENDENTE → EM_PROCESSAMENTO → LOTES_PERSISTIDOS → CONSOLIDADO → VALIDADO.

## Conclusão nacional
Só existe conclusão quando todos os municípios do catálogo estiverem validados contra o respetivo target_total.