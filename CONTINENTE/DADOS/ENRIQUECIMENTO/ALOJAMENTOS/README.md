# WEB-12.6 — Enriquecimento de contactos públicos RNAL

## Objetivo

Recolher, de forma controlada, telefone e email que o RNT publica nas fichas individuais do RNAL.

## Fonte

Registo Nacional de Estabelecimentos de Alojamento Local — Turismo de Portugal.

Cada ficha pública RNAL apresenta os contactos dos titulares quando disponíveis e informa que esses contactos são divulgados nos termos do artigo 10.º do DL 128/2014. A existência dos campos foi verificada em fichas públicas do RNT.

## Regras

- somente dados efetivamente publicados pelo RNT;
- não recolher NIF/NIPC para o catálogo público;
- preservar o número RNAL como chave de origem;
- preservar URL da ficha oficial;
- registar estado de recolha e data;
- falhas de rede não são convertidas em ausência de contacto;
- ausência de bloco de contactos e bloco sem telefone/email são estados distintos;
- nenhuma execução é iniciada automaticamente após alterações na `main`.

## Dependência de entrada

A execução recebe explicitamente o **Run ID do WEB-12.2** que contém o snapshot normalizado. O Run ID deixou de estar gravado no workflow.

Isto evita que uma execução utilize silenciosamente um snapshot diferente, mas **não transforma o artefato do WEB-12.2 em armazenamento permanente**. Antes da escala nacional, o snapshot de entrada deve ser tornado durável ou ser regenerado e validado de forma controlada.

## Execução

O workflow é manual e recebe:

- `normalization_run_id`;
- `rnal_offset`;
- `rnal_limit` — máximo 500 por execução;
- `rnal_workers` — máximo 4.

O lote é publicado como artefato separado. A agregação nacional dos lotes ainda é uma etapa posterior e obrigatória.

## Estados de recolha

- `CONTACTOS_ENCONTRADOS`
- `SEM_CONTACTOS`
- `PAGINA_SEM_BLOCO_CONTACTOS`
- `NAO_ENCONTRADO`
- `ERRO_HTTP`
- `ERRO_REDE`
- `SEM_ID`

## Saída

`CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/RNAL_CONTACTOS_PUBLICOS_V1.json`

A saída de um lote **não deve ser tratada como catálogo nacional completo** e não deve, isoladamente, promover contactos para publicação.
