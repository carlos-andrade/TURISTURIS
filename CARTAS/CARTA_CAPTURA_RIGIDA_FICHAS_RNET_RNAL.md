# CARTA — CAPTURA RÍGIDA DE FICHAS OFICIAIS RNET E RNAL

ID: CARTA-CAPTURA-RNET-RNAL-V1
ESTADO: REGENTE

## Fontes oficiais
- RNET: https://rnt.turismodeportugal.pt/RNT/RNET.aspx?nr=6803
- RNAL: https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr=15642

## Regras obrigatórias
1. Capturar a ficha integralmente, sem selecionar apenas os campos considerados úteis.
2. Preservar todos os rótulos, valores, tabelas, listas, contactos, localização, classificação, identificadores, observações e demais conteúdo apresentado.
3. raw_value deve preservar o valor publicado pela fonte. Não corrigir, traduzir, arredondar, interpretar ou completar.
4. Qualquer normalização futura deve existir em campo separado e nunca substituir raw_value.
5. Preservar o HTML bruto da fonte como evidência primária.
6. Cada campo deve possuir chave determinística e única: TIPO:NUMERO_REGISTO:FIELD_CODE:OCORRENCIA.
7. Cada captura deve registrar URL, data/hora UTC, HTTP status, SHA-256 do HTML bruto, SHA-256 dos dados estruturados, quantidade de campos e tabelas e ordem dos elementos.
8. RNET e RNAL nunca podem ser misturados nas pastas de evidência.
9. Se a fonte não puder ser capturada, o processo deve falhar. É proibido preencher lacunas por inferência ou por fonte secundária.
10. Nova captura é novo evento de auditoria; hashes devem permitir detectar alterações da fonte.

## Organização
FICHAS OFICIAIS RNET/<numero>/raw, structured e audit.
FICHAS OFICIAIS RNAL/<numero>/raw, structured e audit.

## Regra final
O código organiza e audita o que a fonte publica. Não inventa, corrige ou completa o que a fonte não publicou.