# NORMALIZAÇÃO — PONTOS TURÍSTICOS DE AMADORA V1

**Data:** 2026-10-04  
**Estado:** NORMALIZAÇÃO CONCLUÍDA — LOTE 01  
**Município:** Amadora  
**Distrito:** Lisboa  
**Fonte-base:** `CONTINENTE/DISTRITO/LISBOA/AMADORA/README.md`  
**Índice de origem:** `CONTINENTE/DADOS/REGISTROS_PONTOS_TURISTICOS_V1.md`  
**Esquema:** `CONTINENTE/DADOS/ESQUEMA_ENTIDADE_V1.md`

## 1. Objetivo

Normalizar os pontos turísticos já identificados para uma estrutura canônica única, com IDs estáveis, sem duplicação e sem inventar campos ainda não verificados.

A normalização transforma:

`fonte territorial → registro canônico → entidade normalizada`

Este documento é o artefato de normalização do primeiro lote.

## 2. Regras aplicadas

1. Um ponto turístico = um registro canônico.
2. Cada registro possui ID estável.
3. IDs seguem o padrão `PT-[TIPO]-[TERRITORIO]-[SLUG]`.
4. O slug é padronizado em maiúsculas, sem acentos e sem caracteres especiais.
5. O nome preserva a forma pública registrada na fonte.
6. Município e distrito são derivados da estrutura territorial existente.
7. Não foram inventados horários, preços, contactos, coordenadas ou websites.
8. O estado de validação permanece `VERIFICADO` apenas porque o conjunto já foi validado na fonte municipal; isso não significa que todos os campos operacionais estejam completos.
9. Informações voláteis exigem nova verificação antes da publicação operacional.
10. O índice canônico continua sendo a referência dos IDs deste lote.

## 3. Registros normalizados

| # | ID canônico | Nome | Tipo | Município | Distrito | Estado | Confiança |
|---:|---|---|---|---|---|---|---|
| 1 | PT-PTT-LISBOA-AMADORA-AQUEDUTO-AGUAS-LIVRES | Aqueduto Geral das Águas Livres | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 2 | PT-PTT-LISBOA-AMADORA-NECROPOLE-CARENQUE | Necrópole de Carenque | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 3 | PT-PTT-LISBOA-AMADORA-CASA-ROQUE-GAMEIRO | Casa Roque Gameiro | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 4 | PT-PTT-LISBOA-AMADORA-CASAL-FALAGUEIRA | Núcleo Museológico do Casal da Falagueira | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 5 | PT-PTT-LISBOA-AMADORA-MOINHO-PENEDO | Núcleo Museológico do Moinho do Penedo | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 6 | PT-PTT-LISBOA-AMADORA-VILLA-ROMANA-BOLACHA | Villa Romana da Quinta da Bolacha | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 7 | PT-PTT-LISBOA-AMADORA-AQUEDUTO-ROMANO | Aqueduto Romano da Amadora | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 8 | PT-PTT-LISBOA-AMADORA-GARGANTADA | Aqueduto da Gargantada / Nascentes da Gargantada | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 9 | PT-PTT-LISBOA-AMADORA-ASSENTISTA | Quinta do Assentista | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 10 | PT-PTT-LISBOA-AMADORA-CONDESS-LOUSA | Palácio/Quinta dos Condes da Lousã | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 11 | PT-PTT-LISBOA-AMADORA-ORDEM-MALTA | Casa da Ordem de Malta / Casal da Falagueira de Cima | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 12 | PT-PTT-LISBOA-AMADORA-CASA-APRIGIO-GOMES | Casa Aprígio Gomes | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 13 | PT-PTT-LISBOA-AMADORA-CASA-INFANTADO | Fachada da Casa do Infantado / Palácio da Porcalhota | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 14 | PT-PTT-LISBOA-AMADORA-CHALET-DESIDERIA | Moradia Neorromântica / Chalet Desideria | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 15 | PT-PTT-LISBOA-AMADORA-IGREJA-MATRIZ | Igreja Matriz da Amadora | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 16 | PT-PTT-LISBOA-AMADORA-CAPELA-FALAGUEIRA | Capela da Falagueira / Nossa Senhora da Lapa | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 17 | PT-PTT-LISBOA-AMADORA-CHAFARIZ-PORCALHOTA | Chafariz da Porcalhota | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 18 | PT-PTT-LISBOA-AMADORA-MINA-AGUA | Mina de Água e Jardim da Mina | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 19 | PT-PTT-LISBOA-AMADORA-PARQUE-DELFIM-GUIMARAES | Parque Delfim Guimarães | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 20 | PT-PTT-LISBOA-AMADORA-PONTE-FILIPINA | Ponte Filipina / Ponte de Carenque de Baixo | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 21 | PT-PTT-LISBOA-AMADORA-QUINTA-OUTEIRO | Quinta do Outeiro | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 22 | PT-PTT-LISBOA-AMADORA-QUINTA-SAO-MIGUEL | Quinta de São Miguel | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 23 | PT-PTT-LISBOA-AMADORA-RECREIOS-AMADORA | Recreios da Amadora | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 24 | PT-PTT-LISBOA-AMADORA-PORTAS-BENFICA | Portas de Benfica | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 25 | PT-PTT-LISBOA-AMADORA-MOINHO-CASTELINHO | Moinho do Castelinho | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 26 | PT-PTT-LISBOA-AMADORA-QUINTA-GRANDE-ALFRAGIDE | Quinta Grande de Alfragide | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 27 | PT-PTT-LISBOA-AMADORA-VILA-MARTELO | Vila Martelo | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |
| 28 | PT-PTT-LISBOA-AMADORA-CABOS-AVILA | Edifício Torreado da Fábrica dos Cabos Ávila | Ponto turístico | Amadora | Lisboa | VERIFICADO | ALTO |

## 4. Resultado da normalização

- Registros de origem: **28**
- Registros normalizados: **28**
- Perdas: **0**
- Duplicações no lote: **0**
- IDs ausentes: **0**
- IDs fora do padrão: **0**
- ID corrigido durante o processo: **1** — Casa Aprígio Gomes
- Estado do lote: **NORMALIZADO**
- Próxima etapa: validação campo a campo para completar a entidade turística.

## 5. Campos ainda não preenchidos

O lote não deve ser considerado uma base operacional completa. Permanecem sujeitos a pesquisa e verificação individual:

- localidade/freguesia;
- endereço;
- coordenadas;
- descrição detalhada;
- história;
- interesse turístico detalhado;
- telefone;
- email;
- website;
- horários;
- preços;
- acessibilidade;
- serviços;
- reservas;
- observações específicas.

A ausência desses dados é intencional e segue a regra de não invenção.

## 6. Cadeia de autoridade

`GOVERNANÇA → CARTAS → LAYOUT MESTRE → ESTRUTURA TERRITORIAL → DADOS → NORMALIZAÇÃO → VALIDAÇÃO → PUBLICAÇÃO`

Este documento não substitui o Layout Mestre nem o índice canônico.

## 7. Próximo lote

Após verificação deste artefato, aplicar exatamente o mesmo procedimento ao próximo município, preservando a separação entre:

- fonte territorial;
- índice canônico;
- registro normalizado;
- validação;
- publicação.

<!-- TESTE OPERACIONAL V1: validação técnica; remover antes de qualquer promoção. -->
