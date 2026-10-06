# FICHAS OFICIAIS RNET

## Função

Repositório documental das **fichas oficiais RNET — Registo Nacional de Empreendimentos Turísticos**, obtidas diretamente das fontes oficiais do Turismo de Portugal.

## Fonte primária

- RNET nº **6803**
- Fonte oficial: https://rnt.turismodeportugal.pt/RNT/RNET.aspx?nr=6803

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

Esta pasta é exclusiva de **RNET**. Dados RNAL permanecem em `FICHAS OFICIAIS RNAL/`.

## Estado

**EVIDÊNCIA OFICIAL A VALIDAR.**

A existência desta estrutura e do código de captura não comprova que a ficha nº 6803 tenha sido capturada. A captura somente poderá ser considerada concluída após:

**fonte → raw → structured → audit → validação → commit**

Dados fornecidos como exemplos de teste não substituem o HTML oficial capturado.
