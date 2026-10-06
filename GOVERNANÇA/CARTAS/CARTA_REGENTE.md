# CARTA REGENTE — TURISTURIS

## 1. Propósito
O TURISTURIS é um projeto de inteligência turística dedicado à coleta, organização, validação e disponibilização de informações úteis sobre o turismo em Portugal.

Pergunta central: Como podemos obter informações valiosas sobre o turismo de Portugal em um só lugar?

## 2. Princípios
1. Fonte antes de afirmação.
2. Dados turísticos devem possuir origem identificável.
3. Informação temporalmente sensível deve registrar data de verificação.
4. Não misturar fato confirmado com inferência.
5. Não duplicar informação quando uma entidade já existir.
6. Estrutura territorial e tipológica deve ser consistente.
7. Alterações estruturais devem ser refletidas no Layout Mestre.
8. O Layout Mestre é a referência para novos artefatos do projeto.
9. Nenhum dado deve ser considerado permanente quando horários, preços, contactos ou condições puderem mudar.
10. O repositório deve preservar rastreabilidade suficiente para auditoria.

## 3. Hierarquia documental
CARTA REGENTE → CARTAS ESPECIALIZADAS → LAYOUT MESTRE → DADOS E CÓDIGO.

## 4. Qualidade
Toda informação relevante deve, quando aplicável, conter fonte, URL ou referência, data de consulta, data de atualização, nível de confiança e observações sobre conflitos.

## 5. Escopo inicial
Portugal continental e regiões autónomas, com expansão progressiva por município e entidade turística.

## 6. Regra de prudência
Quando uma informação não puder ser confirmada, deve ser marcada como não confirmada ou omitida. O projeto não deve preencher lacunas com suposições.

## 7. Estado
Documento fundacional do projeto.


## 8. Regra fiel — identidade internacional dos contactos telefónicos

Todo contacto telefónico deve preservar obrigatoriamente o código telefónico internacional do país de origem. Esta regra é global: aplica-se a Portugal e a qualquer país que venha a ser incorporado no TURISTURIS. O código de país não pode ser eliminado, truncado ou substituído durante captura, normalização, validação, enriquecimento, armazenamento, exportação ou publicação. A representação internacional é a forma canónica; a apresentação nacional/local, quando existir, é derivada e nunca substitui o valor internacional.


## 9. Regra de publicação — estados internos não são conteúdo público

Os estados internos de validação e confiança pertencem à camada de governança, auditoria e dados do TURISTURIS. Valores como `CONFIRMADO_FICHA_OFICIAL`, `CONFIRMADO_FONTE_PUBLICA`, `ALTO` e equivalentes **não devem ser exibidos no site público**, salvo decisão futura expressamente documentada.

A interface pública deve apresentar a informação turística destinada ao visitante, sem expor etiquetas técnicas de validação, grau de confiança ou estados operacionais internos. Esses valores devem permanecer preservados nas camadas internas para auditoria e rastreabilidade.

## Regra permanente de publicação de alojamentos — Website oculto

Na camada pública do TURISTURIS, o campo **Website** e o respetivo link **não devem ser exibidos nas fichas públicas de alojamentos**. O valor pode permanecer preservado nas bases internas para auditoria, rastreabilidade e uso operacional autorizado, mas não pode ser renderizado na interface pública. Esta regra é independente dos estados internos de validação e aplica-se a novas publicações e futuras correções do catálogo, salvo autorização explícita posterior.
