# CARTA PARA CARTAS — TURISTURIS

## 1. Finalidade

Esta Carta estabelece como as **Cartas** do TURISTURIS devem ser criadas, organizadas, revisadas e relacionadas entre si.

## 2. Origem

Toda Carta deve nascer de uma necessidade formalizada por um **PROMPT**.

Fluxo obrigatório:

**PROMPT → CARTA → LAYOUT → ESTRUTURA → DADOS → CÓDIGO/SITE**

## 3. Tipos

Podem existir:

- CARTA REGENTE;
- Cartas de dados;
- Cartas de fontes;
- Cartas de atualização;
- Cartas territoriais;
- Cartas metodológicas;
- Cartas de publicação;
- outras Cartas especializadas justificadas pelo projeto.

## 4. Regras

1. Toda Carta deve possuir finalidade e escopo explícitos.
2. Toda Carta deve identificar sua relação com a CARTA REGENTE.
3. Toda Carta deve indicar data e estado.
4. Toda Carta deve ser compatível com o LAYOUT MESTRE.
5. Conflitos entre Cartas devem ser registrados e resolvidos formalmente.
6. Uma Carta não pode alterar silenciosamente outra Carta.
7. Alterações estruturais devem refletir-se no LAYOUT MESTRE.
8. Cartas não substituem fontes factuais; estabelecem regras para trabalhar com elas.
9. Nenhuma Carta autoriza a invenção de dados.
10. Toda Carta nova deve ser versionada no Git.

## 5. Precedência

Em caso de conflito:

**CARTA REGENTE → CARTAS ESPECIALIZADAS → LAYOUT MESTRE → DADOS → CÓDIGO/SITE**

Quando uma alteração exigir mudança na hierarquia, a mudança deve ser documentada antes da implementação.

## 6. Estado

Estado inicial: ATIVO.
Data: 2026-10-04.


## 7. Regra fiel para cartas que tratem contactos

Quando uma regra de contacto telefónico afetar captura, dados, validação, enriquecimento ou publicação, ela deve ser refletida nas Cartas correspondentes. A preservação do código telefónico internacional é obrigatória e transversal. Nenhuma Carta especializada pode autorizar uma normalização que elimine ou substitua o código internacional.


## 8. Regra transversal de publicação pública

Quando uma Carta tratar de publicação, deverá distinguir obrigatoriamente entre **dados internos de validação/auditoria** e **conteúdo público apresentado no site**.

Estados como `CONFIRMADO_FICHA_OFICIAL`, graus como `ALTO` e etiquetas técnicas semelhantes não devem ser exibidos no site por defeito. Devem permanecer preservados nas camadas internas quando necessários à rastreabilidade.

Nenhuma Carta especializada deve introduzir na interface pública etiquetas técnicas de validação sem regra de publicação expressa.

## Regra permanente de publicação de alojamentos — Website oculto

Na camada pública do TURISTURIS, o campo **Website** e o respetivo link **não devem ser exibidos nas fichas públicas de alojamentos**. O valor pode permanecer preservado nas bases internas para auditoria, rastreabilidade e uso operacional autorizado, mas não pode ser renderizado na interface pública. Esta regra é independente dos estados internos de validação e aplica-se a novas publicações e futuras correções do catálogo, salvo autorização explícita posterior.
