# Carta/Contrato — padrão obrigatório de roadmap

| Campo | Valor |
|---|---|
| **ID** | GOV-CARTA-ROADMAP-001 |
| **Projeto** | GOVERNANÇA |
| **Repositório** | [carlos-andrade/GOVERNANCA](https://github.com/carlos-andrade/GOVERNANCA) |
| **Tipo documental** | CARTA_CONTRATO |
| **Fase** | Governação transversal |
| **Estado** | APROVADO |
| **Versão** | 1.1.0 |
| **SHA-256 (conteúdo canónico)** | 97b8cc2f7f73daea196b585a0ebc6d288cc18dd27358a79d9cd2a1447ae726c1 |
| **Commit de referência (versão anterior)** | N/A — documento inicial |
| **Data de criação** | 2026-10-17 |
| **Data de atualização** | 2026-10-17 |
| **Responsável** | Proprietário do repositório GOVERNANCA |
| **Aprovador** | Carlos Andrade — aprovação expressa nesta solicitação |
| **Origem** | Solicitação expressa de adoção do modelo de roadmap em 2026-10-17 |
| **Autoridade superior** | [CONSTITUICAO.md](CONSTITUICAO.md) |
| **Cadeia de autoridade** | PROMPTS → CARTAS → LAYOUT ÚNICO → CÓDIGO |

## 1. Objeto e compromisso

Esta Carta/Contrato institui [ROADMAP-PADRAO-GOVERNANCA.md](ROADMAP-PADRAO-GOVERNANCA.md) como padrão obrigatório para o repositório GOVERNANCA e todos os repositórios que adotem formalmente as regras de governança deste sistema, incluindo novos projetos que declarem essa adoção.

O padrão exige painel executivo, fases/gates, ações prioritárias, evidências, riscos/bloqueios, critérios de aceitação e histórico. A quantidade de fases pode variar; os controlos mínimos não podem desaparecer.

## 2. Hierarquia normativa

Respeitar a lei aplicável, contratos vinculativos, políticas formalmente aprovadas, esta Carta/Contrato, padrões e procedimentos. Conflitos devem ser registados e escalados, nunca resolvidos silenciosamente. Esta Carta não substitui a Constituição, a norma de cabeçalho, a norma de estados/percentuais ou contratos específicos.

## 3. Obrigações

O roadmap deve apresentar a barra visual de status definida na [Norma de estado e percentual de conclusão](standards/status-e-percentual-de-conclusao.md). A pontuação deve ser baseada em critérios com evidências; o painel Markdown e o SVG devem ser gerados a partir da mesma fonte canónica.

Cada repositório abrangido deve:
- manter roadmap publicado e ligado no README ou índice principal;
- adotar o padrão ou documentar mapeamento equivalente;
- declarar fase, estado, dependências, bloqueios, próximo marco e critérios de aceitação;
- ligar conclusões a evidências verificáveis;
- atualizar após cada fase e mudança material;
- preservar rastreabilidade por caminho, commit, issue, pull request, workflow, teste ou relatório;
- declarar pendências, UNKNOWN, exceções e decisões não aprovadas;
- cumprir requisitos documentais e de integridade da GOVERNANCA.

## 4. Proibições e fail-closed

É proibido declarar conclusão apenas porque o código foi escrito, ficheiro criado ou workflow configurado; apresentar testes não executados como aprovados; inventar percentuais, prazos, responsáveis ou evidências; ocultar bloqueios; converter UNKNOWN em sucesso; ou declarar adoção transversal concluída sem inspeção por repositório.

Sem evidência, aprovação ou dependência crítica satisfeita, a fase permanece bloqueada ou aguardando evidência. Exceções devem ser autorizadas, limitadas, rastreáveis e compatíveis com obrigações superiores.

## 5. Adoção transversal

A publicação desta Carta define o padrão normativo no repositório-mestre, mas não certifica retroativamente outros repositórios. Cada adoção exige referência à Carta e ao padrão, identificação do roadmap local e registo da inspeção, adaptação e resultado de conformidade.

Quando o formato literal não for adequado, documentar mapeamento, controlos preservados, motivo, risco, aprovador e validade. A simples referência à GOVERNANCA não substitui a verificação.

## 6. Responsabilidades

- **Proprietário da GOVERNANCA:** manter a norma-mãe e resolver ambiguidades.
- **Responsável do repositório:** manter roadmap, evidências e estado.
- **Responsável técnico:** garantir critérios e verificações rastreáveis.
- **Revisor/aprovador:** avaliar evidências e aprovar exceções dentro da sua autoridade.

## 7. Auditoria

Verificar estrutura, atualidade, estados, evidências, gates, exceções e coerência com o estado do projeto. Registar não conformidades com severidade, responsável, ação corretiva e critério de encerramento. Não declarar conformidade total enquanto controlos críticos não forem demonstrados.

## 8. Vigência e revisão

Esta versão foi aprovada em 2026-10-17 para a GOVERNANCA. Repositórios já abrangidos devem ser adaptados por inventário, inspeção, atualização e validação individual. Alterações futuras exigem revisão versionada e registo de decisão.

## 9. Checklist

- [ ] Roadmap publicado e ligado no README/índice.
- [ ] Painel executivo e próximo marco verificável.
- [ ] Fases com dependências e critérios objetivos.
- [ ] Conclusões apoiadas por evidências.
- [ ] Riscos, bloqueios, decisões e exceções visíveis.
- [ ] Estados e percentuais coerentes com a norma.
- [ ] Atualização após mudança material.
- [ ] Inspeção de conformidade local registada.

## 10. Histórico

| Versão | Data | Alteração | Evidência |
|---|---|---|---|
| 1.0.0 | 2026-10-17 | Instituição do padrão obrigatório de roadmap | Aprovação expressa do proprietário |
| 1.1.0 | 2026-10-17 | Tornada obrigatória a barra de status baseada em critérios e evidências | Norma GOV-STD-STATUS-001 v1.1.0 |
