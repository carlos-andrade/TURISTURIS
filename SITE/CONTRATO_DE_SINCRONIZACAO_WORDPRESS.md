# CONTRATO DE SINCRONIZAÇÃO WORDPRESS — TURISTURIS

## 1. Finalidade

Este documento define o contrato técnico e operacional entre o repositório TURISTURIS e o WordPress de publicação.

O contrato existe para garantir que a publicação seja previsível, auditável, idempotente e reversível, sem transformar o WordPress na fonte canônica dos dados turísticos.

Cadeia oficial:

**PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → VALIDAÇÃO → SINCRONIZAÇÃO → WORDPRESS**

## 2. Hierarquia de autoridade

A autoridade dos componentes é:

1. CARTAS — governança e regras;
2. LAYOUT MESTRE — modelo canônico;
3. DADOS — informação turística estruturada;
4. CÓDIGO/SYNC — implementação do contrato;
5. WORDPRESS — publicação e apresentação;
6. conteúdo editorial próprio do WordPress — somente para conteúdo explicitamente editorial.

O WordPress não pode alterar silenciosamente o significado dos campos canônicos.

## 3. Unidade canônica

Toda entidade sincronizada deve possuir um **ID canônico TURISTURIS**, estável e permanente.

Exemplo:

`PT-SANTAREM-TOMAR-PT-000001`

O ID canônico deve ser armazenado no WordPress em campo técnico próprio e utilizado como chave de reconciliação.

O `post_id` interno do WordPress não substitui o ID canônico TURISTURIS.

## 4. Regra de propriedade dos dados

### 4.1 Campos controlados pelo TURISTURIS

São, por padrão, somente leitura no WordPress:

- ID canônico;
- nome canônico;
- tipo;
- país;
- região;
- distrito/arquipélago;
- município;
- localidade;
- endereço;
- coordenadas;
- descrição canônica;
- história;
- interesse turístico;
- telefone;
- email;
- website;
- horários;
- preços;
- acessibilidade;
- serviços;
- reservas;
- fontes;
- data de verificação;
- data de atualização;
- estado de validação;
- grau de confiança;
- observações canônicas.

### 4.2 Campos editoriais do WordPress

Podem ser administrados no WordPress, desde que não alterem os dados canônicos:

- título editorial;
- destaque;
- ordem de apresentação;
- banner;
- chamada;
- texto editorial;
- conteúdo de campanha;
- blocos de apresentação;
- configurações visuais.

Quando um campo editorial tiver relação direta com um dado canônico, deve existir identificação clara dessa relação.

## 5. Fluxo de publicação

O fluxo padrão é:

**FONTES → RAW → NORMALIZAÇÃO → VALIDAÇÃO → DADOS CANÔNICOS → TESTES → SYNC → WORDPRESS**

Nenhuma sincronização para produção deve ignorar a validação.

## 6. Estados de sincronização

Cada entidade poderá possuir um estado operacional:

- `PENDING` — ainda não sincronizada;
- `SYNCED` — sincronizada com sucesso;
- `CHANGED` — alteração detectada;
- `FAILED` — falha de sincronização;
- `BLOCKED` — bloqueada por regra/validação;
- `DEPRECATED` — entidade retirada do conjunto canônico;
- `CONFLICT` — conflito que exige decisão.

O estado de sincronização é diferente do `estado_validacao` definido pela CARTA DE DADOS.

## 7. Idempotência

A sincronização deve ser idempotente.

Executar o mesmo lote duas vezes não pode criar duplicações.

Regra:

**mesmo ID canônico + mesma versão de dados = mesma entidade WordPress.**

A sincronização deve:

1. localizar o ID canônico;
2. comparar a versão existente;
3. não alterar se não houver mudança;
4. atualizar somente quando houver mudança válida;
5. registrar o resultado.

## 8. Versionamento

Cada entidade deverá possuir, sempre que possível:

- `canonical_id`;
- `data_atualizacao`;
- `data_verificacao`;
- `source_hash` ou equivalente;
- versão do registro ou commit de origem.

O commit Git que originou uma publicação deve poder ser identificado no log de sincronização.

## 9. Mapeamento para WordPress

O mapeamento inicial recomendado é:

| TURISTURIS | WordPress |
|---|---|
| Destino | CPT `destino` |
| Ponto Turístico | CPT `ponto_turistico` |
| Alojamento | CPT `alojamento` |
| Restaurante | CPT `restaurante` |
| Transporte | CPT `transporte` |
| Experiência | CPT `experiencia` |
| Evento | CPT `evento` |
| Roteiro | CPT `roteiro` |

Taxonomias territoriais e turísticas devem seguir o LAYOUT MESTRE.

## 10. Regra de atualização

Quando um registro canônico for alterado:

1. o Git recebe a alteração;
2. testes são executados;
3. o sistema identifica os registros afetados;
4. o Sync Engine calcula o delta;
5. somente registros válidos são enviados;
6. o WordPress atualiza a entidade correspondente;
7. o resultado é registrado;
8. a publicação fica associada ao commit de origem.

## 11. Criação de entidades

Nova entidade:

**GitHub → validação → sincronização → WordPress**

Nunca:

**WordPress → criação canônica automática**

O WordPress pode receber conteúdo editorial independente, mas não deve criar uma entidade turística canônica fora do fluxo TURISTURIS.

## 12. Alterações e exclusões

### Alteração

Atualização normal ocorre mediante novo registro/versão no GitHub.

### Exclusão

Não apagar imediatamente uma entidade WordPress apenas porque ela desapareceu de um lote.

Primeiro classificar a situação:

- erro de ingestão;
- ausência temporária;
- mudança de ID;
- entidade desativada;
- entidade realmente arquivada.

Quando aplicável, utilizar estado `DEPRECATED`/arquivado antes da remoção física.

## 13. Conflitos

Se fontes diferentes apresentarem informações incompatíveis:

**não sobrescrever silenciosamente.**

O registro deve permanecer em estado de conflito até resolução conforme as CARTAS.

Enquanto bloqueado, o Sync Engine não deve publicar uma alteração não validada.

## 14. Falhas

Uma falha de sincronização não pode resultar em publicação parcial silenciosa.

O sistema deve registrar:

- entidade;
- ID canônico;
- operação;
- commit de origem;
- data/hora;
- erro;
- tentativa;
- resultado.

Quando possível, o lote deve permitir reexecução segura.

## 15. Rollback

O rollback deve ocorrer preferencialmente revertendo a alteração de origem no Git e executando nova sincronização.

Não utilizar edição manual do WordPress como mecanismo principal de rollback.

Para incidentes críticos, o WordPress poderá ter restauração técnica independente, mas a reconciliação posterior deve partir do estado canônico.

## 16. Segurança

A integração deve utilizar credenciais separadas e princípio do menor privilégio.

Credenciais, tokens e segredos:

- não podem ser armazenados nos arquivos do repositório;
- não podem ser gravados em conteúdo WordPress;
- devem utilizar secrets/variáveis seguras;
- devem possuir rotação quando aplicável.

O mecanismo de sincronização deve autenticar o destino e validar respostas.

## 17. Ambientes

Recomendação:

**DESENVOLVIMENTO → STAGING → PRODUÇÃO**

Alterações estruturais e novas versões do Sync Engine devem ser testadas em staging antes da produção.

## 18. GitHub Actions

GitHub Actions poderá executar:

- validação do schema;
- testes de integridade;
- detecção de alterações;
- geração do lote de sincronização;
- sincronização staging;
- verificações pós-publicação;
- relatórios;
- sincronização de produção após os gates definidos.

A automação não deve publicar dados que estejam bloqueados por validação.

## 19. Logs de sincronização

Cada execução deve produzir um registro mínimo:

```
run_id
commit_sha
started_at
finished_at
environment
entity_count
created
updated
unchanged
blocked
failed
duration
status
```

Por entidade, quando necessário:

```
canonical_id
operation
wordpress_post_id
source_commit
result
error
timestamp
```

## 20. Verificação pós-publicação

Após uma sincronização, o sistema deve verificar pelo menos:

- quantidade enviada versus quantidade recebida;
- existência dos IDs canônicos;
- ausência de duplicações;
- campos obrigatórios;
- estado publicado;
- URLs;
- taxonomias;
- coordenadas quando aplicáveis;
- erros HTTP/API;
- integridade dos registros alterados.

## 21. Conteúdo volátil

Para horários, preços, disponibilidade, contactos, encerramentos, obras e transportes:

- manter data de verificação;
- preservar a fonte;
- permitir atualização incremental;
- não considerar a informação permanentemente válida apenas porque já foi publicada.

## 22. Imagens

Imagens devem possuir identificação de origem e direitos de utilização quando aplicável.

O WordPress pode gerar derivados otimizados para apresentação.

A origem e o vínculo da imagem com a entidade canônica devem permanecer rastreáveis.

## 23. Correções vindas do site

O visitante poderá sinalizar um problema no WordPress.

Esse evento deve gerar uma ocorrência, não uma alteração silenciosa no dado canônico.

Fluxo:

**WORDPRESS → OCORRÊNCIA → PESQUISA/VALIDAÇÃO → GITHUB → NOVO COMMIT → SYNC → WORDPRESS**

## 24. Proibição de dupla fonte de verdade

É proibido estabelecer simultaneamente:

**GitHub = fonte canônica**

e

**WordPress = fonte canônica**

para o mesmo campo.

Cada campo deve possuir um proprietário definido.

## 25. Contrato mínimo de API

A futura API de sincronização deverá suportar, no mínimo:

- autenticação;
- identificação do lote;
- identificação da entidade;
- operação;
- payload;
- versão;
- commit de origem;
- resposta de sucesso/erro;
- idempotência;
- logs.

O contrato exato de endpoints será definido em documento técnico posterior, depois da escolha da implementação.

## 26. Critérios de aceitação

O contrato será considerado tecnicamente implementável quando for possível demonstrar:

1. criação de entidade;
2. atualização de entidade;
3. execução idempotente;
4. detecção de alteração;
5. bloqueio de registro inválido;
6. tratamento de conflito;
7. tratamento de falha;
8. rastreamento por commit;
9. rollback;
10. verificação pós-publicação;
11. ausência de duplicação;
12. separação entre dados canônicos e editoriais.

## 27. Sequência oficial de implementação

**FASE 1 — Modelo**
→ tipos, taxonomias e campos.

**FASE 2 — Identidade**
→ IDs canônicos e versionamento.

**FASE 3 — Dados**
→ formato estruturado e validação.

**FASE 4 — Contrato**
→ este documento e contrato de API.

**FASE 5 — Sync Engine**
→ transformação e sincronização.

**FASE 6 — WordPress**
→ CPTs, taxonomias e campos.

**FASE 7 — Staging**
→ primeira sincronização controlada.

**FASE 8 — Testes**
→ criação, atualização, idempotência, conflitos e rollback.

**FASE 9 — Produção**
→ publicação somente após aprovação dos gates.

## 28. Regra de alteração deste contrato

Este contrato não pode ser alterado por uma necessidade isolada do WordPress.

Alteração estrutural:

**necessidade → CARTAS → LAYOUT MESTRE → contrato → implementação → testes → publicação**

Qualquer alteração relevante deve preservar a rastreabilidade entre regra, modelo, código e publicação.

## 29. Estado

**Estado: CONTRATO INICIAL V1**

Este documento define o contrato conceitual e operacional mínimo para a futura integração GitHub/WordPress do TURISTURIS.

Ele não autoriza, por si só, a publicação em produção.

A implementação técnica deverá ser criada somente após validação do contrato, do modelo de dados e da estratégia de autenticação.
