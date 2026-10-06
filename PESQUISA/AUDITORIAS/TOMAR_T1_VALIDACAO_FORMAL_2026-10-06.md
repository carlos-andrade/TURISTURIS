# TURISTURIS — AUDITORIA FORMAL T1 TOMAR — 2026-10-06

## Cabeçalho histórico
- Projeto: TURISTURIS
- Processo: T1 — Enriquecimento TOMAR
- Tipo: Auditoria / evidência de validação
- Data: 2026-10-06
- Base: `CONTINENTE/DADOS/PUBLICACAO/TOMAR_PONTOS_INTERESSE_T1_ENRIQUECIDOS_V1.json`
- Regra: CARTA REGENTE + CARTA DE DADOS + CARTA DE FONTES
- Resultado: PASS ESTRUTURAL / T1 LIBERADO PARA VALIDAÇÃO DE CONTEÚDO
- Promoção automática de estado: NÃO

## 1. Checks executados

| Check | Resultado |
|---|---|
| `record_count = 25` e 25 registos efetivos | PASS |
| IDs únicos | PASS |
| Nome presente em todos os registos | PASS |
| Fonte e tipo de fonte presentes | PASS |
| Data de verificação = 2026-10-06 | PASS |
| Bloco operacional persistido em 25/25 | PASS |
| Contactos internacionais preservados com `+` | PASS |
| Nenhum registo promovido automaticamente para `VERIFICADO` | PASS |
| Freguesia não inferida | PASS |

## 2. Regra de prudência

Os três registos que não apresentavam dados operacionais específicos na fonte oficial atual receberam uma indicação explícita de ausência de dados específicos. Isso não é uma invenção de conteúdo e não transforma ausência de informação em facto turístico.

## 3. Contactos

Os contactos encontrados foram mantidos em representação internacional, incluindo `+351`. O código internacional não foi removido, substituído ou inferido.

## 4. Conclusão

**T1 — ENRIQUECIMENTO: CONCLUÍDO.**

A validação estrutural do conjunto passou todos os checks definidos nesta auditoria.

**Importante:** este PASS não significa que todos os 25 pontos tenham horários, preços ou contactos. Significa que a estrutura, proveniência, datação, prudência e regras permanentes aplicáveis ao T1 foram satisfeitas.

A próxima etapa é a **validação de conteúdo dos 25 pontos**, seguindo fonte oficial por registo e sem promoção automática de estados.

## 5. Persistência

Este documento é a evidência oficial persistida no repositório. O chat não é o arquivo desta validação.
