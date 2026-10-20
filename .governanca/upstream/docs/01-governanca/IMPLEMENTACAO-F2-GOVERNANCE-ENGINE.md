# Implementação F2 — Núcleo de diagnóstico do Governance Integration Framework

| Campo | Valor |
|---|---|
| ID | GOV-INT-F2-001 |
| Estado | Implementação inicial; testes CI aprovados na PR #7 |
| Origem | [DEC-GOV-INT-001](DEC-GOV-INTEGRATION-FRAMEWORK-001.md) |
| Contrato | [Especificação F1](ESPECIFICACAO-GOVERNANCE-INTEGRATION-FRAMEWORK-001.md) |

## Entrega

- Leitura segura de YAML com `yaml.safe_load`.
- Validação da configuração contra o JSON Schema canónico Draft 2020-12.
- Relatório JSON com modo, perfil, commit local detetável, hashes SHA-256 da configuração e do esquema, verificações, bloqueios e estado.
- Estados conservadores: configuração ausente/inválida resulta em `NAO_CONFORME`; configuração válida sem catálogo de requisitos executáveis resulta em `DESCONHECIDO`.
- Modo `aplicar` bloqueado explicitamente até à entrega do adaptador de Pull Request.
- Sem escrita em ficheiros do repositório-alvo em diagnóstico/auditoria; o relatório é enviado para stdout.

## Limites

O motor ainda não resolve nem verifica criptograficamente a versão oficial remota por si só, não implementa catálogo de requisitos por perfil, não cria Pull Requests e não instala configurações em consumidores. `source_commit` só é preenchido quando existe evidência explícita via variável de ambiente; não é inferido a partir do commit do repositório-alvo. Estas capacidades pertencem às fases seguintes e não são simuladas.

## Execução

```bash
python -m pip install pyyaml jsonschema
python automation/governance_engine.py --root /caminho/do/repositorio
```

Código de saída 0 significa apenas estado conforme emitido pelo motor; código 2 indica bloqueio, configuração inválida ou estado ainda desconhecido. O relatório não declara conformidade global sem um catálogo executável e evidências completas.
