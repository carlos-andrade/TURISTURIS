# CARTA VITAL — REGRA DE PERSISTÊNCIA DOS RESULTADOS

**Código:** CARTA-VITAL-001  
**Projeto:** TURISTURIS  
**Data:** 2026-10-06  
**Status:** REGRA OBRIGATÓRIA E PERMANENTE

## 1. Regra

Nenhum resultado de pesquisa, investigação, análise, validação, execução, decisão técnica, evidência, dado coletado, correção, configuração ou outro artefato relevante produzido durante o desenvolvimento do TURISTURIS pode permanecer exclusivamente em conversas do ChatGPT.

O **repositório GitHub correspondente é a fonte oficial e persistente da informação**.

## 2. Obrigação operacional

Sempre que uma atividade produzir informação que precise ser preservada, o resultado deve ser enviado para o respectivo repositório, em arquivo ou estrutura adequada, com:

- caminho do arquivo;
- conteúdo completo;
- fonte/proveniência, quando aplicável;
- data;
- estado/status;
- identificador da execução, quando existir;
- commit correspondente;
- relação com workflow, PR ou issue, quando aplicável.

## 3. O chat não é arquivo oficial

O histórico do ChatGPT pode servir exclusivamente como interface de trabalho e coordenação.

Ele **não é fonte de verdade, arquivo morto, sistema de auditoria nem mecanismo de backup**.

Se uma informação for importante o suficiente para ser utilizada posteriormente, ela deve existir no repositório.

## 4. Regra de continuidade

Uma nova sessão ou novo chat deve conseguir recuperar o estado do projeto consultando o repositório, sem depender da memória do chat anterior.

Se o estado necessário não estiver no repositório, a atividade deve ser considerada **não persistida** até que seja documentada.

## 5. Regra de evidência

Não basta executar um workflow com sucesso. O resultado relevante da execução deve possuir evidência persistida, incluindo, conforme o caso:

- parâmetros;
- entrada;
- saída;
- contagens;
- erros;
- logs relevantes;
- artefatos;
- validações;
- decisão;
- próxima ação.

## 6. Regra de transparência

Ao finalizar qualquer operação, o ChatGPT deve informar:

1. o que foi feito;
2. onde foi salvo;
3. quais arquivos foram criados ou alterados;
4. qual commit registrou a alteração;
5. qual foi o resultado;
6. o que ainda não foi persistido ou validado.

## 7. Regra de falha

Se o ChatGPT não conseguir escrever no repositório, **não deve apresentar a operação como concluída/persistida**.

Deve declarar explicitamente a falha e indicar o artefato que ficou pendente.

## 8. Hierarquia

Esta Carta integra a governança do TURISTURIS e deve ser considerada regra vital para todas as fases, workflows, pesquisas, ingestões, análises, publicações e desenvolvimentos futuros.

**CARTAS → LAYOUT MESTRE → DADOS → CÓDIGO**

Nenhum resultado importante pode ficar somente no elo ChatGPT.

## 9. Princípio permanente

> **SE FOI PRODUZIDO E É IMPORTANTE, DEVE ESTAR NO REPOSITÓRIO.**

Esta regra vale para todo o ciclo de vida do TURISTURIS.
