# AUDITORIA DE PERSISTÊNCIA — WEB-12.6 / WEB-12.7

**Data:** 2026-10-06  
**Projeto:** TURISTURIS  
**Objetivo:** registrar no repositório o estado verificável da documentação e da implementação do enriquecimento de contactos RNAL.

## 1. Repositório auditado

carlos-andrade/TURISTURIS

Branch principal: main

## 2. Evidência encontrada no Git

A atividade WEB-12.6/WEB-12.7 existe no histórico de commits e PRs.

### WEB-12.6

- PR #45 — enriquecimento nacional de contactos públicos RNAL.
- PR #46 — prova controlada do enriquecimento RNAL.
- PR #47 — correção de dependência do snapshot e classificação dos contactos RNAL.

### WEB-12.7

- PR #48 — correção de contactos RNAL e publicação do catálogo V2.
- PR #49 — integração do enriquecimento RNAL no Pages.

## 3. Arquivos efetivamente associados ao trabalho

### WEB-12.6

.github/workflows/turisturis-web-12-6-enriquecimento.yml

CONTINENTE/DADOS/CODIGOS/enriquecimento_contatos_rnal_v1.py

CONTINENTE/DADOS/CODIGOS/gerar_publicacao_alojamentos.py

CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/README.md

### WEB-12.7

.github/workflows/turisturis-pages.yml

## 4. Constatação crítica

A auditoria não encontrou, no conteúdo pesquisável do repositório, um registro permanente com os termos:

- 37403480142;
- normalization_run_id;
- um relatório específico da execução do lote mencionado no contexto operacional.

Portanto, **não é correto considerar esse resultado de execução como persistentemente documentado no Git apenas porque o workflow existe**.

Este documento registra essa lacuna para impedir que ela seja perdida.

## 5. Regra de correção

A partir da CARTA-VITAL-001, toda execução relevante deverá gerar um registro persistente em:

OPERACAO/WEB-12.6/EXECUCOES/

ou no caminho operacional equivalente definido pelo Layout Mestre.

## 6. Estado

**Implementação WEB-12.6/WEB-12.7:** existente no Git.

**Evidência permanente de cada execução:** requer consolidação.

**Resultado específico identificado como run 37403480142:** não localizado no conteúdo pesquisável do repositório nesta auditoria.

## 7. Próxima ação

Auditar os workflows e artefatos de WEB-12.6, recuperar os resultados disponíveis no GitHub Actions e persistir no repositório os resultados relevantes, sem depender do histórico do ChatGPT.

## 8. Regra de encerramento

Nenhuma etapa de enriquecimento será considerada documentalmente encerrada enquanto sua evidência operacional relevante não estiver versionada no repositório.
