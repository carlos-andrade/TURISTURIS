# TURISTURIS — AUDITORIA DE VALIDAÇÃO DE CONTEÚDO T1 TOMAR — 2026-10-06

## Cabeçalho histórico
- Projeto: TURISTURIS
- Processo: T1 — Validação de conteúdo dos pontos de interesse
- Tipo: Auditoria / evidência de validação
- Data: 2026-10-06
- Base: `CONTINENTE/DADOS/PUBLICACAO/TOMAR_PONTOS_INTERESSE_T1_ENRIQUECIDOS_V1.json`
- Regra: CARTA REGENTE + CARTA DE DADOS + CARTA DE FONTES
- Método: verificação fonte a fonte, priorizando Turismo de Tomar / Município de Tomar
- Promoção automática para estado interno: NÃO

## 1. Resultado

**22/25 registos possuem confirmação de conteúdo/proveniência em fonte oficial atual identificável.**

**3/25 permanecem PENDENTES de confirmação atual específica:** Jardim das Musas, Jardim Manuel Costa Rosa e Casa dos Vereadores.

A validação não transforma os 22 registos em estado público `VERIFICADO`. O resultado desta auditoria é evidência de conteúdo e proveniência para a próxima decisão de publicação/estado.

## 2. Registos confirmados

| Ordem | Registo | Resultado | Evidência oficial |
|---:|---|---|---|
| 1 | Pelourinho de Tomar | CONFIRMADO | Página oficial individual |
| 2 | Capela de Nossa Senhora da Piedade | CONFIRMADO | Página oficial individual |
| 3 | Parque do Mouchão | CONFIRMADO | Página oficial individual |
| 4 | Mata Nacional dos Sete Montes | CONFIRMADO | Página oficial individual |
| 5 | Igreja de Santa Maria do Olival | CONFIRMADO | Página oficial individual |
| 6 | Convento de Santa Iria | CONFIRMADO | Página oficial/rota histórica |
| 7 | Casa dos Cubos / CEFT | CONFIRMADO | Página oficial individual |
| 8 | Complexo Cultural da Levada | CONFIRMADO | Página oficial individual |
| 9 | Museu dos Fósforos | CONFIRMADO | Catálogo/página oficial |
| 10 | NAC — Núcleo de Arte Contemporânea | CONFIRMADO | Rota histórica/catálogo oficial |
| 11 | Capela de Nossa Senhora da Conceição | CONFIRMADO | Catálogo oficial |
| 12 | Igreja e Convento de São Francisco | CONFIRMADO | Página oficial individual |
| 13 | Central Elétrica de Tomar | CONFIRMADO | Página oficial individual |
| 14 | Fundição Tomarense | CONFIRMADO | Página oficial individual |
| 15 | Centro Interpretativo Tomar Templário | CONFIRMADO | Página oficial individual |
| 16 | Casa Memória Lopes-Graça | CONFIRMADO | Página oficial individual |
| 17 | Capela de São Gregório | CONFIRMADO | Página oficial individual |
| 18 | Cine-Teatro Paraíso | CONFIRMADO | Página oficial individual |
| 19 | Palácio de Alvaiázere | CONFIRMADO | Página oficial individual |
| 20 | Ponte D. Manuel I / Ponte Velha | CONFIRMADO | Rota histórica oficial |
| 21 | Roda do Mouchão | CONFIRMADO | Rota histórica oficial |
| 22 | Charolinha — Mata Nacional dos Sete Montes | CONFIRMADO | Página oficial da Mata |

## 3. Registos pendentes

| Ordem | Registo | Resultado | Motivo |
|---:|---|---|---|
| 23 | Jardim das Musas | PENDENTE | Não localizado no catálogo oficial atual nem em página individual oficial específica durante as verificações de 2026-10-06 |
| 24 | Jardim Manuel Costa Rosa | PENDENTE | Não localizado no catálogo oficial atual nem em página individual oficial específica durante as verificações de 2026-10-06 |
| 25 | Casa dos Vereadores | PENDENTE | Não localizado no catálogo oficial atual nem em página individual oficial específica durante as verificações de 2026-10-06 |

**Regra aplicada:** ausência de resultado não é convertida em inexistência. Estes três registos ficam pendentes até existir fonte oficial atual identificável.

## 4. Segunda verificação das três pendências

Em 2026-10-06 foi executada nova pesquisa dirigida nos domínios oficiais do Município de Tomar e Turismo de Tomar para os três nomes exatos:

- `Jardim das Musas`
- `Jardim Manuel Costa Rosa`
- `Casa dos Vereadores`

Também foi repetida a consulta ao catálogo oficial atual:
`https://turismo.cm-tomar.pt/Places/Index/wtd`

Resultado: **não foi localizada nova página turística oficial atual e específica que permita confirmar os três registos**.

A pesquisa encontrou documentos municipais antigos ou resultados não relacionados para algumas expressões, mas estes não foram usados como confirmação turística atual. Em particular, uma ata municipal de 2012 contém ocorrências da palavra “Vereadores”, mas não constitui evidência de que exista atualmente um ponto turístico denominado “Casa dos Vereadores”.

Fonte oficial de catálogo consultada:
`https://turismo.cm-tomar.pt/Places/Index/wtd`

Fonte institucional municipal consultada:
`https://www.cm-tomar.pt/`

**Decisão:** manter os três registos como PENDENTES. Não alterar nome, localização, descrição ou estado por inferência.

## 5. Verificações críticas

- O catálogo oficial atual de Turismo de Tomar confirma a presença de múltiplos registos do conjunto, incluindo Pelourinho, Capela da Piedade, Parque do Mouchão, Mata dos Sete Montes, Palácio de Alvaiázere, Museu dos Fósforos, Casa dos Cubos, Central Elétrica, Fundição Tomarense, Lopes-Graça, São Francisco e Centro Interpretativo Tomar Templário.
- A rota histórica oficial confirma especificamente a Ponte D. Manuel I/Ponte Velha e a Roda do Mouchão.
- A página oficial da Mata confirma a Charolinha como elemento da Mata.
- Os contactos encontrados permanecem em representação internacional, incluindo `+351`.
- Não foi feita inferência de freguesia.
- Não foram promovidos automaticamente estados internos para `VERIFICADO`.
- Dados operacionais continuam sujeitos à data de verificação e à volatilidade da fonte.

## 6. Conclusão

**VALIDAÇÃO DE CONTEÚDO T1: 22/25 CONFIRMADOS; 3/25 PENDENTES.**

A segunda verificação não produziu evidência oficial atual suficiente para retirar qualquer dos três registos pendentes.

O resultado não autoriza afirmar que os 25 registos estejam igualmente validados.

Os 3 pendentes devem permanecer explicitamente identificados no repositório até nova evidência oficial. Não devem ser preenchidos por inferência, fontes secundárias ou aproximação sem nova decisão governada.

## 7. Persistência

Esta auditoria é persistida no repositório através do fluxo:

**branch → PR → PR Gate → merge**

O chat não é o arquivo da validação.
