# TURISTURIS — LAYOUT WEB-12.6 NACIONAL

> CONTEXTO HISTÓRICO: 2026-10-07 | Derivado da CARTA-WEB-12-6-NACIONAL.
> ESTADO: FONTE DE VERDADE PARA O CÓDIGO

## Fluxo
1. Ler RNAL_NORMALIZADO_V1.
2. Gerar catálogo único de municípios e target_total.
3. Selecionar município.
4. Dividir em lotes controlados.
5. Recolher contactos públicos.
6. Validar município, universo, offset e unicidade.
7. Persistir lote em diretório próprio.
8. Consolidar.
9. Validar cobertura integral.
10. Marcar VALIDADO.
11. Avançar para o próximo município.

## Persistência
CONTINENTE/DADOS/ENRIQUECIMENTO/ALOJAMENTOS/LOTES/<municipio_slug>/rnal_contactos_offset_<offset>.json

## Regressão
Peso da Régua deve continuar com 182 registos e quatro lotes válidos.