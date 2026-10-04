# ESQUEMA DE ENTIDADE TURÍSTICA V1

Status: estrutura operacional inicial
Data: 2026-10-04
Autoridade: GOVERNANÇA/LAYOUT/LAYOUT_MESTRE.md

## Identificador

Cada entidade deve possuir um id estável e único no TURISTURIS.

Formato recomendado: PT-[TIPO]-[TERRITORIO]-[SLUG]

O exemplo é ilustrativo e não constitui registro validado.

## Campos canônicos

| Campo | Obrigatório | Regra |
|---|---|---|
| id | Sim | estável e único |
| nome | Sim | nome oficial ou público verificável |
| tipo | Sim | categoria do Layout Mestre |
| país | Sim | Portugal |
| região | Sim | região territorial aplicável |
| distrito ou arquipélago | Sim | conforme território |
| município | Sim | município de localização |
| localidade | Quando aplicável | freguesia/localidade |
| endereço | Quando conhecido | não inventar |
| coordenadas | Quando verificadas | fonte identificável |
| descrição | Sim | factual e verificável |
| história | Quando aplicável | separar fato de interpretação |
| interesse turístico | Sim | classificação fundamentada |
| contactos | Quando disponíveis | fonte identificável |
| telefone | Volátil | verificar |
| email | Volátil | verificar |
| website | Quando disponível | preferir fonte oficial |
| horários | Volátil | verificar antes de publicar |
| preços | Volátil | verificar antes de publicar |
| acessibilidade | Quando disponível | verificar |
| serviços | Quando aplicável | verificar |
| reservas | Quando aplicável | canal verificável |
| fontes | Sim | origem do dado |
| data_verificação | Sim | última verificação |
| data_atualização | Sim | última alteração |
| estado_validação | Sim | conforme Carta de Dados |
| grau_confiança | Sim | ALTO/MÉDIO/BAIXO |
| observações | Quando necessário | conflitos e limitações |

## Estados

NAO_VERIFICADO
EM_VERIFICACAO
VERIFICADO
CONFLITO
DESATUALIZADO
ARQUIVADO

## Proveniência

Nenhum campo factual deve ser preenchido por invenção. Quando uma informação não estiver confirmada, o campo permanece vazio ou recebe estado compatível com a Carta de Dados.

## Volatilidade

Horários, preços, disponibilidade, contactos, encerramentos, obras, acessibilidade e condições de transporte são dados voláteis.

## Relação com o Layout

Este esquema operacionaliza o modelo de entidade para CONTINENTE/DADOS. Não substitui o Layout Mestre.

Sequência oficial:

PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → VALIDAÇÃO → SINCRONIZAÇÃO → PUBLICAÇÃO
