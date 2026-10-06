# FICHAS OFICIAIS RNAL

## Função

Repositório documental das **fichas oficiais RNAL — Registo Nacional de Alojamento Local**, obtidas diretamente das fontes oficiais do Turismo de Portugal.

## Fonte primária

- RNAL nº **15642/AL**
- Fonte oficial: https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr=15642

## Estrutura obrigatória

`<numero_registo>/raw/` — HTML recebido da fonte, preservado byte a byte.  
`<numero_registo>/structured/` — representação estruturada, sem substituir os valores brutos.  
`<numero_registo>/audit/` — manifesto, hashes, metadados e resultado da captura.

## Modelo de captura

A captura é regida por:

`GOVERNANÇA/CARTAS/CARTA_CAPTURA_RIGIDA_FICHAS_RNET_RNAL.md`

O capturador deve preservar:

- rótulo original;
- valor original;
- relação rótulo → valor quando identificável;
- ordem/posição dos elementos;
- HTML bruto;
- SHA-256 do bruto;
- SHA-256 do estruturado;
- estado da execução.

O campo `raw_value` nunca pode ser corrigido, traduzido, arredondado, interpretado ou completado.

## Regra de separação

Esta pasta é exclusiva de **RNAL**. Dados RNET permanecem em `FICHAS OFICIAIS RNET/`.

## Estado

**EVIDÊNCIA OFICIAL A VALIDAR.**

A existência desta estrutura e do código de captura não comprova que a ficha nº 15642/AL tenha sido capturada. A captura somente poderá ser considerada concluída após:

**fonte → raw → structured → audit → validação → commit**

Dados fornecidos como exemplos de teste não substituem o HTML oficial capturado.
