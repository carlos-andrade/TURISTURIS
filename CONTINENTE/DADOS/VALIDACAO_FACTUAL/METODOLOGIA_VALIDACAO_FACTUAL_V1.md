# METODOLOGIA DE VALIDAÇÃO FACTUAL — V1

**Projeto:** TURISTURIS  
**Data:** 2026-10-05  
**Estado:** APROVADA PARA REUTILIZAÇÃO  
**Piloto concluído:** Amadora — 28/28 registros

## 1. Objetivo

Separar a validação factual da normalização estrutural e da publicação operacional.

A validação factual responde primeiro:

> A entidade existe, é identificável e está sustentada por fonte confiável?

Não responde automaticamente se está aberta, quanto custa, quando funciona ou se aceita reservas.

## 2. Hierarquia de fontes

1. Fonte oficial do Município ou entidade pública responsável.
2. Fonte institucional diretamente responsável pelo património/cultura.
3. Fonte oficial do proprietário/operador, quando aplicável.
4. Fonte secundária somente quando as fontes primárias não forem suficientes.

## 3. Procedimento

Para cada registro:

1. localizar a entidade pelo ID canônico;
2. confirmar nome e identidade;
3. confirmar município e enquadramento territorial;
4. confirmar existência/enquadramento por fonte;
5. registrar URL da fonte;
6. registrar conflitos de nomenclatura ou estado;
7. não inferir acesso turístico;
8. não promover automaticamente campos voláteis;
9. classificar o resultado;
10. preservar a evidência no lote de validação.

## 4. Estados

- **VERIFICADO:** identificação e evidência suficientes.
- **EM_VERIFICACAO:** evidência parcial ou pendente.
- **CONFLITO:** fontes confiáveis apresentam informação incompatível que exige reconciliação.
- **DESATUALIZADO:** evidência existente, mas sem segurança de atualidade.
- **ARQUIVADO:** entidade deixou de ser válida para a base atual.
- **NAO_VERIFICADO:** ainda sem evidência suficiente.

## 5. Campos que exigem tratamento separado

Horários, preços, contactos, disponibilidade, reservas, acessibilidade operacional, obras, encerramentos e condições de visita são **dados voláteis**.

A validação factual da entidade não autoriza preencher esses campos por inferência.

## 6. Regras de conflito

Conflito não deve ser apagado silenciosamente.

Quando duas fontes oficiais divergem:

- preservar ambas;
- registrar a divergência;
- procurar fonte oficial mais recente;
- somente depois classificar o estado;
- não converter uma hipótese em fato.

Exemplo encontrado no piloto: Quinta do Assentista apresentou documentação municipal de aquisição e fonte municipal com enquadramento de propriedade particular. O ponto foi mantido como entidade validada, mas a propriedade atual não foi tratada como fato operacional consolidado.

## 7. Resultado do piloto

Amadora:

- 28 registros previstos;
- 28 registros validados;
- 4 lotes;
- 28/28 = **100%**;
- nenhuma promoção automática de horários, preços ou acesso;
- conflitos identificados e preservados.

## 8. Critério de promoção

Um registro factual só poderá ser promovido para a camada canônica operacional quando:

- tiver ID estável;
- estiver inequivocamente identificado;
- possuir fonte rastreável;
- possuir estado de validação;
- possuir data de verificação;
- conflitos relevantes estiverem tratados;
- campos voláteis estiverem separados ou individualmente verificados.

## 9. Regra de governança

A validação factual **não altera a autoridade do LAYOUT MESTRE**.

Sequência oficial:

**PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → VALIDAÇÃO → SINCRONIZAÇÃO → PUBLICAÇÃO**

A partir deste ponto, novos municípios devem seguir esta metodologia antes de qualquer promoção operacional.
