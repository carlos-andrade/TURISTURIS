# TURISTURIS — ROADMAP OPERACIONAL

> Cabeçalho histórico: documento de governação operacional do projeto TURISTURIS. Atualizado em 2026-10-06.

## Princípio

**CARTAS → LAYOUT MESTRE → DADOS → CÓDIGO**

Resultados relevantes devem ser persistidos no repositório; o chat não é fonte oficial do projeto.

## Estado atual

- RNAL Peso da Régua: **182/182 manifestos validados**.
- Falhas de validação: **0**.
- Fonte cadastral: OpenData do Turismo de Portugal.
- Tabela-mestra cadastral criada a partir do snapshot validado.
- Contactos públicos continuam como camada separada de enriquecimento e não devem sobrescrever o cadastro oficial.

## Fluxo

1. **GOVERNAÇÃO** — CARTAS e regras canónicas.
2. **LAYOUT MESTRE** — define a estrutura dos artefatos.
3. **CAPTURA OFICIAL** — dados de RNET/RNAL e demais fontes primárias.
4. **NORMALIZAÇÃO** — identidade, nomes, endereços, contactos e chaves.
5. **TABELA-MESTRA** — consolidação sem perda de registros.
6. **ENRIQUECIMENTO** — telefone/e-mail públicos, com fonte e data de recolha.
7. **VALIDAÇÃO** — checks automáticos e evidência.
8. **PR CONTROLADO** — revisão antes do merge.
9. **MERGE** — somente após checks obrigatórios.
10. **SITE** — publicação apenas a partir de dados persistidos e validados.

## Próxima etapa

**WEB-12.6 — consolidar os lotes de contactos públicos RNAL na tabela-mestra, preservando os 182 registros e mantendo estado_contacto, fonte e data de recolha.**

### Correção aplicada em 2026-10-06

O workflow WEB-12.6 não persistia os lotes no repositório. Isso foi corrigido: o workflow agora usa `contents: write` e grava cada lote em `CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/LOTES/`. Também foi criado `CONTINENTE/DADOS/CODIGOS/consolidar_contactos_rnal_v1.py` para consolidar os lotes sem perda de registros.

**Execução:** pendente de disparo manual do workflow, pois a integração GitHub disponível nesta sessão não expõe a operação `workflow_dispatch`. Não foi simulado sucesso.

### Regra de segurança

A ausência de contacto não é motivo para eliminar um alojamento. Contactos genéricos do Turismo de Portugal não devem ser atribuídos ao alojamento.

## Evidências

- `DADOS/INDICES/rnal_peso_da_regua.json`
- `DADOS/INDICES/rnal_peso_da_regua_manifest_validation_report.json`
- `CONTINENTE/DADOS/CODIGOS/enriquecimento_contatos_rnal_v1.py`
- `DADOS/INDICES/rnal_peso_da_regua_tabela_mestra.csv`
