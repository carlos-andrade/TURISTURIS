# CARTA — CAPTURA RÍGIDA DE FICHAS OFICIAIS RNET E RNAL

**ID:** CARTA-CAPTURA-RNET-RNAL-V1  
**ESTADO:** REGENTE  
**PROJETO:** TURISTURIS  
**HIERARQUIA:** subordinada à CARTA-VITAL-001 e anterior ao LAYOUT MESTRE

## 1. Finalidade

Estabelecer a regra única para captura, preservação, estruturação e auditoria das fichas oficiais RNET e RNAL utilizadas pelo TURISTURIS.

Esta Carta não autoriza interpretação, correção ou complementação da informação publicada pela fonte.

## 2. Fontes oficiais

- RNET: https://rnt.turismodeportugal.pt/RNT/RNET.aspx?nr=6803
- RNAL: https://rnt.turismodeportugal.pt/RNT/RNAL.aspx?nr=15642

As URLs acima são as fontes de referência desta captura. Alterações futuras de fonte devem ser documentadas e persistidas antes de serem utilizadas.

## 3. Regras obrigatórias de captura

1. Capturar a ficha integralmente, sem selecionar apenas os campos considerados úteis.
2. Preservar todos os rótulos, valores, tabelas, listas, contactos, localização, classificação, identificadores, observações e demais conteúdo apresentado.
3. **raw_value** deve preservar exatamente o valor publicado pela fonte.
4. É proibido corrigir, traduzir, arredondar, interpretar, completar ou inferir valores durante a captura.
5. Qualquer normalização futura deve existir em campo separado e nunca substituir **raw_value**.
6. Preservar o HTML bruto da fonte como evidência primária.
7. Preservar a ordem dos elementos necessária para reconstituir a ficha.
8. RNET e RNAL nunca podem ser misturados nas pastas de evidência.
9. Dados provenientes de fonte secundária não podem ser usados para preencher lacunas da ficha oficial.
10. Uma fonte inacessível, incompleta ou tecnicamente indisponível deve gerar estado de falha/pendência, nunca uma ficha artificialmente completa.

## 4. Chave única e determinística

Cada campo deve possuir chave determinística e única:

**TIPO:NUMERO_REGISTO:FIELD_CODE:OCORRENCIA**

Exemplos:

- `RNET:6803:NOME:001`
- `RNAL:15642:MORADA:001`

A chave deve ser estável para a mesma estrutura de captura e suficientemente específica para impedir colisões.

## 5. Auditoria obrigatória

Cada captura deve registrar, no mínimo:

- URL oficial;
- tipo de registo;
- número do registo;
- data/hora UTC;
- HTTP status;
- content type, quando disponível;
- SHA-256 do HTML bruto;
- SHA-256 dos dados estruturados;
- quantidade de campos;
- quantidade de tabelas;
- ordem/sequência dos elementos;
- identificador da captura;
- versão desta Carta/regra aplicada;
- resultado da validação;
- erros ou limitações técnicas, quando existirem.

## 6. Organização física obrigatória

### RNET

`FICHAS OFICIAIS RNET/<numero>/raw/`  
`FICHAS OFICIAIS RNET/<numero>/structured/`  
`FICHAS OFICIAIS RNET/<numero>/audit/`

### RNAL

`FICHAS OFICIAIS RNAL/<numero>/raw/`  
`FICHAS OFICIAIS RNAL/<numero>/structured/`  
`FICHAS OFICIAIS RNAL/<numero>/audit/`

## 7. Persistência e rastreabilidade

Toda captura executada deve ser persistida no repositório GitHub correspondente.

A evidência mínima de conclusão é:

**fonte → captura → raw → structured → audit → commit**

Uma execução sem evidência persistida não pode ser apresentada como concluída.

A obrigação de persistência segue a **CARTA-VITAL-001**.

## 8. Alterações e novas capturas

Cada nova captura constitui um novo evento de auditoria.

Os hashes devem permitir identificar alterações na fonte entre capturas.

Uma alteração na fonte não deve apagar a evidência anterior; deve originar novo artefato/evento, preservando a rastreabilidade histórica.

## 9. Relação com o LAYOUT MESTRE

Esta Carta define **o que deve ser capturado e quais evidências devem existir**.

O LAYOUT MESTRE define **como a informação persistida será organizada para consumo posterior**.

O código de captura não pode criar regra de negócio que contradiga esta Carta.

## 10. Regra de falha

Se a fonte oficial não puder ser capturada ou validada conforme estas regras:

- a execução deve registrar a falha;
- nenhum valor deve ser inventado;
- nenhuma fonte secundária deve completar a ficha;
- a operação não deve ser declarada concluída;
- a pendência deve ser persistida quando tecnicamente possível.

## 11. Regra final

> **O código organiza e audita o que a fonte publica. Não inventa, corrige, interpreta ou completa o que a fonte não publicou.**

Esta Carta integra a governança permanente do TURISTURIS e deve ser aplicada antes de qualquer normalização ou povoamento do site com dados RNET/RNAL.