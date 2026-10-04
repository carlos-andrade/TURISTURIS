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
