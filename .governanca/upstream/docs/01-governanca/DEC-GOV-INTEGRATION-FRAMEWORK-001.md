# Decisão de Governação — Governance Integration Framework

| Campo | Valor |
|---|---|
| **ID** | DEC-GOV-INT-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | DECISÃO DE ARQUITETURA (ADR) |
| **Fase** | Governação e arquitetura |
| **Estado** | APROVADO — arquitetura; implementação por fases |
| **Versão** | 1.0.0 |
| **Data da decisão** | 2026-10-20 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Carlos Andrade — aprovação expressa em 2026-10-20 |
| **Autoridade superior** | [CONSTITUICAO.md](../../CONSTITUICAO.md) |
| **Políticas relacionadas** | [Política de decisões](politica-de-decisoes.md); [Distribuição automática das regras canónicas](distribuicao-automatica-regras.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Contexto e problema

Os repositórios que adotam a GOVERNANCA necessitam de uma forma consistente, repetível, auditável e segura de invocar as regras oficiais, diagnosticar a sua aplicabilidade, implementar controlos em falta e demonstrar conformidade. A simples cópia ou distribuição de documentos não prova implementação nem conformidade.

A distribuição automática por Pull Request já existe como implementação inicial, mas a sua operação transversal permanece sujeita à validação das credenciais, do modo de diagnóstico e da criação real de Pull Requests. O novo framework deverá reutilizar esse mecanismo quando adequado, sem declarar operacionalidade antes de existirem evidências.

## 2. Decisão

Fica aprovada a arquitetura de um **Governance Integration Framework** central, reutilizável, versionado e auditável, mantido no repositório oficial [GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA).

Invocar a Governança inicia um processo controlado de avaliação e, quando autorizado, de implementação das regras aplicáveis. A conformidade só pode ser declarada após a execução dos controlos e a verificação das evidências exigidas.

A aprovação desta decisão aprova a arquitetura e o plano de implementação faseada; não certifica que o framework já esteja implementado, implantado ou operacional nos repositórios consumidores.

## 3. Objetivos

1. Estabelecer uma fonte oficial única e versionada das regras de Governança.
2. Tornar a invocação consistente em repositórios de diferentes tipos.
3. Detetar lacunas antes de alterar ficheiros.
4. Propor e aplicar alterações de forma controlada, rastreável e reversível.
5. Preservar conteúdo local e evitar sobrescrita indiscriminada.
6. Produzir relatórios verificáveis com versão de origem, hashes, testes, alterações, bloqueios e pendências.
7. Permitir a adoção gradual, com validação individual por repositório.
8. Detetar alterações normativas e propor atualizações aos consumidores.

## 4. Componentes aprovados

| Componente | Responsabilidade |
|---|---|
| **Governance Bootstrap** | Inicializar a integração num repositório ainda não integrado. |
| **Governance Engine** | Interpretar regras versionadas e determinar a aplicabilidade. |
| **Governance Adapter** | Mapear requisitos para o perfil e a tecnologia do repositório. |
| **Governance Validator** | Executar verificações e avaliar critérios de aceitação. |
| **Governance Auditor** | Registar decisões, versões, hashes, evidências, desvios e resultados. |
| **Governance Updater** | Detetar alterações da fonte oficial e preparar propostas de atualização. |
| **GitHub Actions reutilizável** | Orquestrar diagnóstico, validação e propostas de alteração. |
| **Configuração declarativa local** | Definir perfil, opções e controlos aplicáveis em `.governanca/config.yml`. |

Os componentes podem ser entregues incrementalmente; a tabela define responsabilidades arquiteturais, não uma alegação de que todos já existem.

## 5. Fluxo normativo

1. **Invocação:** comando local, workflow manual ou automatizado, ou configuração de integração.
2. **Identificação da fonte:** resolver versão/commit oficial e validar a integridade dos artefactos.
3. **Diagnóstico:** inspecionar o estado atual sem alterações, identificar requisitos aplicáveis, lacunas, conflitos e riscos.
4. **Plano de alterações:** produzir diferenças propostas, dependências, testes e critérios de aceitação.
5. **Implementação controlada:** realizar alterações numa branch isolada e submetê-las por Pull Request.
6. **Validação:** executar testes e verificações adequados ao perfil e ao risco.
7. **Auditoria:** gerar relatório com versão, commit, hashes, ficheiros alterados, resultados e pendências.
8. **Aceitação:** revisão humana e aprovação conforme os controlos do repositório consumidor.
9. **Verificação posterior:** confirmar que as alterações aprovadas foram integradas e que os controlos funcionam.

## 6. Estados de conformidade

- **CONFORME:** todos os requisitos obrigatórios aplicáveis foram verificados e têm evidências válidas.
- **CONFORME_COM_PENDENCIAS:** os requisitos críticos de bloqueio estão satisfeitos; existem pendências não críticas explicitamente registadas, com responsável e prazo ou condição de resolução.
- **NAO_CONFORME:** pelo menos um requisito obrigatório ou gate de bloqueio não foi satisfeito.
- **DESCONHECIDO:** faltam dados, execução ou evidências suficientes para determinar conformidade.

A ausência de evidência nunca equivale a sucesso. O sucesso de um workflow técnico, isoladamente, não certifica a conformidade global.

## 7. Controlos obrigatórios

1. **Fonte oficial única:** `carlos-andrade/GOVERNANCA`; cada execução regista commit e versão exatos.
2. **Integridade:** validar manifestos e hashes antes de confiar em regras transferidas.
3. **Privilégio mínimo:** credenciais limitadas aos repositórios e operações necessários; segredos nunca são registados nos relatórios.
4. **Alterações isoladas:** usar branch e Pull Request; não fazer merge automático por defeito.
5. **Preservação:** não substituir ficheiros locais do projeto sem uma alteração específica, justificada e revista.
6. **Diagnóstico sem escrita:** disponibilizar modo de diagnóstico/dry-run que não altera o repositório consumidor.
7. **Fail-closed:** falha de autenticação, integridade, fonte, configuração ou teste bloqueante impede aplicação e declaração de conformidade.
8. **Auditoria:** guardar evidências de cada execução e manter histórico de resultados desfavoráveis.
9. **Reversibilidade:** documentar rollback para alterações de impacto relevante.
10. **Aprovação humana:** alterações de segurança, dados, permissões, migrações, operações destrutivas ou de alto impacto exigem aprovação explícita.
11. **Idempotência:** repetir uma execução sem alterações de entrada não deve gerar diferenças artificiais nem Pull Requests duplicadas.
12. **Segregação:** quando o risco o exigir, quem implementa não pode ser o único aprovador.
13. **Sem autorreferência circular:** GOVERNANCA terá perfil de validação próprio; a validação do repositório central não pode depender de se certificar como consumidor externo.
14. **Sem certificação implícita:** receber regras ou conter uma configuração não prova adoção, execução ou conformidade.

## 8. Interface de configuração

A configuração local proposta é `.governanca/config.yml`. O esquema definitivo deverá ser validado por JSON Schema ou mecanismo equivalente e documentado antes da adoção em produção.

Exemplo ilustrativo:

```yaml
governanca:
  fonte: carlos-andrade/GOVERNANCA
  modo: diagnostico
  perfil: automatico
  exigir_pull_request: true
  preservar_ficheiros_existentes: true
  auditoria: obrigatoria
```

Valores e opções não reconhecidos devem causar erro explícito, e não ser silenciosamente ignorados. O modo inicial recomendado é diagnóstico.

## 9. Roadmap aprovado

| Fase | Objetivo | Critério de saída |
|---|---|---|
| **F1 — Especificação** | Definir contrato, esquema de configuração, perfis, estados e critérios de aceitação. | Especificação versionada, revisada e com testes de esquema. |
| **F2 — Motor central** | Implementar Bootstrap, Engine, Adapter, Validator e Auditor, com workflow reutilizável. | Testes automatizados e relatório reproduzível em ambiente de teste. |
| **F3 — Piloto** | Executar num repositório consumidor de risco reduzido, começando por diagnóstico. | Relatório aceite; alterações propostas por PR; preservação local demonstrada. |
| **F4 — Validação adversarial** | Testar falhas de credenciais, fonte, hashes, conflitos, permissões, repetição e rollback. | Testes negativos passam e falhas bloqueantes são fail-closed. |
| **F5 — Expansão** | Integrar os restantes consumidores de forma gradual. | Cada repositório tem evidência individual de instalação, execução e aceitação. |
| **F6 — Atualização contínua** | Detetar alterações normativas e gerar propostas aos consumidores. | Deteção, idempotência, relatório e PR comprovados em execução real. |

A passagem entre fases depende dos critérios de saída e das evidências. Nenhuma fase é considerada concluída apenas por existir documentação ou código.

## 10. Critérios globais de aceitação

- [ ] A versão e o commit das regras são identificáveis e verificáveis.
- [ ] O diagnóstico não altera ficheiros nem cria efeitos laterais.
- [ ] O perfil aplicável é explícito e testado.
- [ ] O esquema de configuração é validado e rejeita valores desconhecidos.
- [ ] As alterações são isoladas numa branch e submetidas por Pull Request.
- [ ] Ficheiros locais são preservados, salvo alteração expressamente aprovada.
- [ ] Testes positivos e negativos demonstram comportamento fail-closed.
- [ ] Credenciais têm privilégio mínimo e não aparecem nos logs.
- [ ] Relatório de auditoria inclui evidências, hashes, bloqueios e pendências.
- [ ] Repetir a execução sem mudanças é idempotente.
- [ ] O piloto foi aceite com evidência real.
- [ ] Cada consumidor foi validado individualmente antes de ser declarado conforme.

## 11. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Regra incorreta ou comprometida na fonte | Fixar commit, validar hashes, rever alterações normativas e usar PR. |
| Sobrescrita de conteúdo do projeto | Espelho isolado, diff explícito, proteção de ficheiros e aprovação humana. |
| Credencial demasiado abrangente | Privilégio mínimo, rotação e escopo limitado. |
| Falso positivo de conformidade | Estados controlados, evidências obrigatórias e estado DESCONHECIDO quando insuficiente. |
| Incompatibilidade entre perfis | Adapters específicos, validação por perfil e exceções formalmente registadas. |
| Falha de propagação | Relatório por destino, retry controlado e ausência de declaração de sucesso global. |
| Ciclo de autorreferência | Perfil de validação próprio para o repositório central. |

## 12. Consequências

**Positivas:** maior consistência, menor duplicação, rastreabilidade, deteção antecipada de desvios e atualização transversal controlada.

**Custos e limitações:** manutenção do motor e dos adapters, testes por perfil, gestão de credenciais, revisão das Pull Requests e necessidade de aceitação individual. A adoção não será instantânea nem automaticamente certificada.

## 13. Condições de revisão ou reabertura

Reabrir esta decisão se forem identificados riscos de segurança não mitigáveis, incompatibilidade estrutural com os repositórios consumidores, custo de manutenção desproporcionado, falhas recorrentes de idempotência ou necessidade de permitir alterações automáticas de maior impacto.

## 14. Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-20 | Decisão de arquitetura e roadmap aprovados pelo proprietário do projeto | Aprovação expressa no chat do projeto; formalização nesta decisão |

## 15. Estado de implementação

**Estado atual:** arquitetura aprovada; implementação integral pendente.

A distribuição automática inicial de regras tem validação operacional pendente devido à autenticação do secret `GOVERNANCA_SYNC_TOKEN`. Esse bloqueio deve ser resolvido e verificado separadamente; não impede a aprovação arquitetural, mas impede declarar operacional a distribuição transversal até existirem evidências de autenticação, dry-run e Pull Requests reais.
