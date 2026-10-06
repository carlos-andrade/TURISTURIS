# CARTA VITAL — REGRA DE PERSISTÊNCIA DOS RESULTADOS

## CABEÇALHO HISTÓRICO DA CARTA

| Campo | Informação |
|---|---|
| ID | `CARTA-VITAL-001` |
| Projeto | TURISTURIS |
| Título | Regra de Persistência dos Resultados |
| Tipo | Carta central de governança |
| Estado atual | **REGRA OBRIGATÓRIA, PERMANENTE E REGENTE** |
| Versão | V1 / consolidação vigente |
| Data de criação | 2026-10-06 |
| Primeiro commit | `826e1d37e847b0c898d86fc641ee2e8bfc3729ac` |
| Primeiro commit — mensagem | `GOV: criar CARTA-VITAL-001 sobre persistência obrigatória dos resultados` |
| Data da primeira persistência | 2026-10-06 |
| Última atualização registrada | 2026-10-06 |
| Último commit | `57a8b10d7147add5a88916dd95a47864adee63dc` |
| Última atualização — mensagem | `GOV: consolidar Carta Vital e cadeia CARTA-LAYOUT-CODIGO` |
| Função histórica | Estabelecer o repositório como fonte oficial e impedir que decisões, evidências e resultados relevantes permaneçam apenas no ChatGPT |
| Regra arquitetural consolidada | `CARTA → LAYOUT MESTRE → DADOS → CÓDIGO → VALIDAÇÃO → EVIDÊNCIA → REPOSITÓRIO` |
| Alcance | Todas as Cartas, Layouts, workflows, pesquisas, ingestões, análises, publicações, dados, código e desenvolvimentos do TURISTURIS |
| Relação com outras Cartas | Carta de governança superior; Cartas operacionais devem respeitar esta regra |
| Histórico de versões | V1 criada em 2026-10-06; atualização posterior em 2026-10-06 para incorporar explicitamente Carta → Layout → Dados → Código → Validação → Evidência → Repositório, regras de não invenção e rastreabilidade |
| Regra de continuidade | Uma nova sessão deve recuperar o estado pelo repositório, sem depender do histórico de chats |
| Observação | O histórico Git é parte da evidência da evolução da Carta; versões anteriores não devem ser apagadas sem justificativa de governança. |

**Código:** CARTA-VITAL-001  
**Projeto:** TURISTURIS  
**Data:** 2026-10-06  
**Status:** REGRA OBRIGATÓRIA, PERMANENTE E REGENTE

## 1. Regra fundamental

Nenhum resultado de pesquisa, investigação, análise, validação, execução, decisão técnica, evidência, dado coletado, correção, configuração, Carta, Layout, código ou outro artefato relevante produzido durante o desenvolvimento do TURISTURIS pode permanecer exclusivamente em conversas do ChatGPT.

O **repositório GitHub correspondente é a fonte oficial e persistente da informação**.

O chat é apenas interface de trabalho e coordenação.

## 2. Cadeia obrigatória de governança

A produção técnica deve obedecer à seguinte cadeia:

**CARTA → LAYOUT MESTRE → DADOS → CÓDIGO → VALIDAÇÃO → EVIDÊNCIA → REPOSITÓRIO**

Nenhum código novo deve ser tratado como fonte normativa quando existir Carta ou Layout aplicável.

As Cartas estabelecem regras e restrições.

O LAYOUT MESTRE consolida as regras aplicáveis em uma referência operacional única.

Os dados e o código devem obedecer ao Layout e às Cartas que o sustentam.

## 3. Obrigação operacional de persistência

Sempre que uma atividade produzir informação que precise ser preservada, o resultado deve ser enviado para o respectivo repositório, em arquivo ou estrutura adequada, com:

- caminho do arquivo;
- conteúdo completo;
- fonte/proveniência, quando aplicável;
- data;
- estado/status;
- identificador da execução, quando existir;
- commit correspondente;
- relação com workflow, PR ou issue, quando aplicável;
- evidência suficiente para permitir auditoria posterior.

## 4. O chat não é arquivo oficial

O histórico do ChatGPT:

- não é fonte de verdade;
- não é arquivo morto;
- não é sistema de auditoria;
- não é mecanismo de backup;
- não substitui GitHub;
- não pode ser requisito oculto para continuidade do projeto.

Se uma informação for importante o suficiente para ser utilizada posteriormente, ela deve existir no repositório.

## 5. Regra de continuidade entre chats

Uma nova sessão ou novo chat deve conseguir recuperar o estado do projeto consultando o repositório, sem depender da memória do chat anterior.

Se o estado necessário não estiver no repositório, a atividade deve ser considerada **não persistida** até que seja documentada.

## 6. Regra especial para Cartas

Toda Carta que estabeleça uma regra operacional deve:

1. possuir identificador único;
2. possuir estado/status;
3. estar persistida no repositório;
4. indicar sua relação com a governança superior, quando aplicável;
5. ser considerada antes da implementação de código que dependa dela;
6. não ser contradita silenciosamente por código, workflow ou documentação posterior.

Quando uma regra for alterada, a versão anterior não deve ser apagada sem justificativa de governança. A alteração deve gerar novo evento de auditoria e preservar o histórico Git.

## 7. Regra de evidência

Não basta executar um workflow com sucesso.

O resultado relevante da execução deve possuir evidência persistida, incluindo, conforme o caso:

- parâmetros;
- entrada;
- saída;
- contagens;
- erros;
- logs relevantes;
- artefatos;
- validações;
- decisão;
- próxima ação;
- commit ou identificador equivalente.

Para captura de fontes, a evidência deve preservar a fonte bruta e os hashes quando definidos pela Carta específica.

## 8. Regra de transparência

Ao finalizar qualquer operação, o ChatGPT deve informar:

1. o que foi feito;
2. onde foi salvo;
3. quais arquivos foram criados ou alterados;
4. qual commit registrou a alteração;
5. qual foi o resultado;
6. o que ainda não foi persistido;
7. o que ainda não foi validado;
8. quais limitações técnicas permaneceram.

## 9. Regra de falha

Se o ChatGPT não conseguir escrever no repositório, **não deve apresentar a operação como concluída ou persistida**.

Deve declarar explicitamente:

- a falha;
- o artefato pendente;
- o ponto em que a cadeia foi interrompida;
- o que precisa ser executado para concluir a persistência.

## 10. Regra de não invenção

Quando uma fonte, workflow, arquivo ou execução não estiver acessível ou não puder ser validado:

- não inventar conteúdo;
- não inferir resultado como se fosse evidência;
- não fabricar commit, hash, execução ou sucesso;
- não preencher lacunas sem base documental;
- declarar o estado como pendente, falho ou não verificável.

## 11. Regra de auditoria e reversibilidade

Toda alteração relevante deve ser rastreável por Git.

A persistência deve permitir identificar:

**regra → implementação → execução → evidência → commit → estado**

Correções devem preservar histórico suficiente para reconstruir o que ocorreu.

## 12. Hierarquia

Esta Carta integra a governança central do TURISTURIS e aplica-se a todas as fases, Cartas, Layouts, workflows, pesquisas, ingestões, análises, publicações, dados, código e desenvolvimentos futuros.

**CARTAS → LAYOUT MESTRE → DADOS → CÓDIGO → VALIDAÇÃO → EVIDÊNCIA → REPOSITÓRIO**

Nenhum resultado importante pode ficar somente no elo ChatGPT.

## 13. Princípio permanente

> **SE FOI PRODUZIDO E É IMPORTANTE, DEVE ESTAR NO REPOSITÓRIO.**

> **SE NÃO ESTÁ PERSISTIDO E VALIDADO, NÃO DEVE SER APRESENTADO COMO CONCLUÍDO.**

Esta regra vale para todo o ciclo de vida do TURISTURIS.