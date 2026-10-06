# CARTA — CAPTURA RÍGIDA DE FICHAS OFICIAIS RNET E RNAL

## CABEÇALHO HISTÓRICO DA CARTA

| Campo | Informação |
|---|---|
| ID | `CARTA-CAPTURA-RNET-RNAL-V1` |
| Projeto | TURISTURIS |
| Título | Captura Rígida de Fichas Oficiais RNET e RNAL |
| Tipo | Carta operacional de captura e auditoria |
| Estado atual | **REGENTE** |
| Versão | V1 |
| Data de criação | 2026-10-06 |
| Primeiro commit | `8c5043041b5759552b20145e7dcbd2fd55f8fe58` |
| Primeiro commit — mensagem | `docs: criar carta de captura rígida RNET RNAL` |
| Data da primeira persistência | 2026-10-06 |
| Última atualização registrada | 2026-10-06 |
| Último commit | `4abe5732e980ae1cb263379ad95782f3e524dfc9` |
| Última atualização — mensagem | `GOV: atualizar Carta de captura RNET/RNAL e integrar persistência` |
| Dependência superior | `CARTA-VITAL-001_PERSISTENCIA_RESULTADOS.md` |
| Relação com o Layout | Define o que deve ser capturado e quais evidências devem existir; o LAYOUT MESTRE define a organização operacional |
| Fontes oficiais originais | RNET nº 6803 e RNAL nº 15642 |
| Regra de continuidade | Alterações devem preservar o histórico Git e gerar novo evento de auditoria |
| Regra de precedência | Esta Carta deve ser respeitada pelo código, workflows e normalizações que tratem RNET/RNAL |
| Origem documentada | Criada para formalizar a captura integral, preservação `raw`, estruturação e auditoria das fichas oficiais antes do povoamento do site |
| Histórico de versões | V1 criada em 2026-10-06; atualização posterior em 2026-10-06 para integrar a Carta Vital, reforçar falhas/pendências e explicitar a relação Carta → Layout → Código |
| Observação | A existência da Carta não comprova que as fichas tenham sido capturadas. A captura real exige execução validada e evidência persistida. |

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

## 12. Regra fiel — preservação do código internacional

1. Todo contacto telefónico capturado deve conservar o código internacional do país quando este estiver publicado ou puder ser confirmado por evidência confiável.
2. O valor bruto publicado pela fonte nunca pode ser destruído por normalização.
3. O valor internacional normalizado deve existir separadamente do valor bruto.
4. Nunca remover o prefixo internacional para produzir apenas o número nacional.
5. A regra é internacional e não pode ficar limitada a Portugal.
6. A auditoria deve permitir verificar a preservação do código de país e a natureza não destrutiva da normalização.


## 13. Regra de publicação — evidência interna não deve ser exposta por defeito

A captura integral e a auditoria devem preservar estados de validação, grau de confiança e referências da ficha oficial. Contudo, esses elementos pertencem à evidência interna e **não devem ser exibidos na interface pública por defeito**.

A existência do campo `ficha_oficial` ou de estados como `CONFIRMADO_FICHA_OFICIAL` e `ALTO` não obriga à sua apresentação ao visitante. O código de publicação deve separar claramente evidência/auditoria de conteúdo editorial público.

## Regra permanente de publicação de alojamentos — Website oculto

Na camada pública do TURISTURIS, o campo **Website** e o respetivo link **não devem ser exibidos nas fichas públicas de alojamentos**. O valor pode permanecer preservado nas bases internas para auditoria, rastreabilidade e uso operacional autorizado, mas não pode ser renderizado na interface pública. Esta regra é independente dos estados internos de validação e aplica-se a novas publicações e futuras correções do catálogo, salvo autorização explícita posterior.
