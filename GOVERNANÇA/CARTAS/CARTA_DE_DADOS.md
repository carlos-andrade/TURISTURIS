# CARTA DE DADOS — TURISTURIS

## Objetivo
Definir como informações turísticas serão modeladas, armazenadas, atualizadas e auditadas.

## Entidades principais
- destino
- município
- ponto turístico
- alojamento
- restaurante
- transporte
- evento
- experiência
- serviço turístico
- fonte

## Campos mínimos
- nome
- tipo
- localização
- descrição
- contactos, quando existentes
- horário, quando aplicável
- preços, quando aplicável
- acessibilidade, quando conhecida
- fonte
- data de verificação
- estado da informação

## Estados de validação
NAO_VERIFICADO, EM_VERIFICACAO, VERIFICADO, CONFLITO, DESATUALIZADO, ARQUIVADO.


## Regra fiel — contactos telefónicos internacionais

1. O código telefónico internacional do país é parte integrante do contacto.
2. A representação canónica deve preservar o número em formato internacional e, quando aplicável, compatível com E.164.
3. O formato nacional/local pode existir como campo derivado, mas nunca apagar ou substituir o internacional.
4. A normalização é não destrutiva: o valor bruto da fonte permanece preservado e o normalizado fica em campo próprio.
5. O país e o código não podem ser inventados; quando não confirmados, o estado deve refletir essa incerteza.
6. É proibido aplicar uma regra portuguesa globalmente. O modelo deve nascer preparado para contactos de qualquer país.
7. Imports, exports, APIs, workflows, validações, enriquecimentos e o site devem respeitar esta regra.

Estrutura recomendada: telefone_raw; telefone_internacional; codigo_pais; numero_nacional; pais_telefone; telefone_formatado; estado_validacao.


## Regra de publicação — separação entre dados internos e apresentação pública

Campos de validação, auditoria e confiança são dados internos e não constituem conteúdo obrigatório da apresentação pública.

Em particular, valores como `CONFIRMADO_FICHA_OFICIAL`, `CONFIRMADO_FONTE_PUBLICA`, `ALTO` e equivalentes devem ser preservados nos dados estruturados, mas **não devem ser renderizados no site público**.

A camada de publicação deve selecionar apenas os campos destinados ao utilizador final. A remoção da apresentação não significa remoção do dado: a informação interna continua disponível para auditoria, validação e futuras decisões editoriais.

## Regra permanente de publicação de alojamentos — Website oculto

Na camada pública do TURISTURIS, o campo **Website** e o respetivo link **não devem ser exibidos nas fichas públicas de alojamentos**. O valor pode permanecer preservado nas bases internas para auditoria, rastreabilidade e uso operacional autorizado, mas não pode ser renderizado na interface pública. Esta regra é independente dos estados internos de validação e aplica-se a novas publicações e futuras correções do catálogo, salvo autorização explícita posterior.
