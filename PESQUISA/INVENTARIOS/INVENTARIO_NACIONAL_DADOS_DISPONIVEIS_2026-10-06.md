# TURISTURIS — INVENTÁRIO NACIONAL DE DADOS DISPONÍVEIS

**ID:** INVENTARIO-NACIONAL-001  
**Projeto:** TURISTURIS  
**Título:** Inventário nacional de dados já persistidos em repositórios relacionados  
**Tipo:** Auditoria / inventário de integração  
**Estado:** EM EXECUÇÃO — FASE NACIONAL 0  
**Versão:** 1.0  
**Data:** 2026-10-06  
**Repositório central:** `carlos-andrade/TURISTURIS`  
**Repositório turístico complementar identificado:** `carlos-andrade/TOMAR`  
**Função histórica:** registrar, antes de qualquer integração nacional, quais dados turísticos já existem, onde estão persistidos e quais são candidatos à consolidação no TURISTURIS.  
**Hierarquia:** CARTA REGENTE → CARTAS ESPECIALIZADAS → LAYOUT MESTRE → ESTRUTURA → DADOS → CÓDIGO → VALIDAÇÃO → PUBLICAÇÃO.  
**Regra de continuidade:** este inventário não substitui fontes nem duplica dados canónicos; serve como mapa de integração.  
**Regra de publicação:** alterações ao SITE permanecem sujeitas a branch → PR → checks → merge → GitHub Pages.

## 1. Objetivo

Inventariar os dados turísticos que já estão efetivamente persistidos nos repositórios disponíveis, reutilizando o modelo já comprovado em TOMAR.

A sequência nacional passa a ser:

**INVENTÁRIO → TERRITÓRIO → TURISMO → ALOJAMENTO → RESTAURAÇÃO → EXPERIÊNCIAS → TRANSPORTES → CULTURA → ACESSIBILIDADE → SITE**

A FASE NACIONAL 0 não promove dados para publicação. Ela identifica ativos existentes, evita duplicação e prepara a integração.

## 2. Regra de escopo

Entram neste inventário:

1. dados turísticos já existentes em `TURISTURIS`;
2. dados turísticos existentes no repositório específico `TOMAR`;
3. estruturas territoriais e normalizações que possam alimentar a camada nacional;
4. datasets públicos já consolidados;
5. fontes/evidências arquivadas que sustentam futura normalização.

Não entram, por não serem projetos turísticos, repositórios como B3 ou DECIO-BAZIN.

## 3. Repositório central — TURISTURIS

Snapshot da árvore `main` em 2026-10-06:

| Ativo | Quantidade / estado | Utilização nacional |
|---|---:|---|
| Arquivos totais na árvore | 4.854 | Inventário estrutural |
| Arquivos JSON | 948 | Dados e evidências estruturadas |
| Documentos de normalização municipal | 280 | Base para expansão territorial/turística |
| READMEs municipais em CONTINENTE/DISTRITO | 278 | Camada editorial/territorial |
| Catálogo municipal normalizado | 278 registos | Base territorial canónica inicial |
| Pontos turísticos publicáveis | 68 registos | Catálogo turístico já consolidado |
| RNAL Peso da Régua publicável | 182 registos | Alojamento |
| RNAL TOMAR publicável | 274 registos | Alojamento |
| Pontos TOMAR T1 enriquecidos | 25 registos | Turismo/cultura |
| Experiências TOMAR | 3 registos | Experiências |
| Transportes TOMAR | 3 registos | Transportes |
| Restauração TOMAR | 7 registos | Restauração |

### 3.1 Datasets publicáveis já existentes

#### Território
`CONTINENTE/DADOS/PUBLICACAO/CATALOGO_MUNICIPIOS_NORMALIZADOS_V1.json`

- `record_count = 278`
- SHA atual: `ccc98f77279b4220e9d5812df0c885d8f89a1a9e`
- função: catálogo territorial municipal normalizado.

#### Pontos turísticos
`CONTINENTE/DADOS/PUBLICACAO/PONTOS_TURISTICOS_PUBLICAVEIS_V1.json`

- `record_count = 68`
- SHA atual: `0c948adc91edc8e2e5788f337257e58d864211d7`
- função: camada pública transversal de pontos turísticos.

#### Alojamento — Peso da Régua
`CONTINENTE/DADOS/PUBLICACAO/RNAL_PESO_DA_REGUA_PUBLICAVEIS_V1.json`

- `record_count = 182`
- SHA atual: `d0fd8e0ea5541deec1b0b45ac24dc2c509b9184c`
- função: alojamento local publicável.

#### Alojamento — TOMAR
`CONTINENTE/DADOS/PUBLICACAO/RNAL_TOMAR_PUBLICAVEIS_V2.json`

- `record_count = 274`
- SHA atual: `c67124e25e143f7c854a44633b718b15d348787e`
- função: alojamento local publicável.

#### TOMAR — pontos T1
`CONTINENTE/DADOS/PUBLICACAO/TOMAR_PONTOS_INTERESSE_T1_ENRIQUECIDOS_V1.json`

- `record_count = 25`
- SHA atual: `0123915080b48905c1731a01ae6ca0c1da5bc84c`
- função: catálogo de pontos com proveniência e enriquecimento operacional persistidos.

#### TOMAR — experiências, transportes e restauração
`CONTINENTE/DADOS/PUBLICACAO/TOMAR_EXPERIENCIAS_TRANSPORTES_RESTAURACAO_V1.json`

- 3 experiências
- 3 transportes
- 7 registos de restauração
- SHA atual: `8dc71c7c8f783d58c7aeff3f95040b85b24ef919`
- função: camada temática inicial de TOMAR.

## 4. Repositório complementar — TOMAR

Repositório: `carlos-andrade/TOMAR`

Snapshot da árvore `main` em 2026-10-06:

- 26 caminhos na árvore;
- 11 READMEs;
- 10 READMEs de pontos turísticos;
- 1 prompt/layout mestre do projeto;
- estrutura temática já criada para os principais pontos turísticos.

Pontos turísticos documentados no repositório TOMAR:

1. Convento de Cristo e Castelo Templário
2. Igreja de Santa Maria do Olival
3. Sinagoga de Tomar
4. Igreja de São João Baptista
5. Mata Nacional dos Sete Montes
6. Parque do Mouchão e Roda
7. Aqueduto dos Pegões
8. Ermida de Nossa Senhora da Conceição
9. Museu dos Fósforos
10. Museu da Levada

Esses documentos são candidatos a reaproveitamento na camada nacional, mas não devem ser copiados cegamente. Devem passar pelo esquema canónico e pela cadeia de evidência já adotada no TURISTURIS.

## 5. Ativos estruturais do TURISTURIS

A árvore atual já contém:

- `GOVERNANÇA/PROMPT/`
- `GOVERNANÇA/CARTAS/`
- `GOVERNANÇA/LAYOUT/`
- `CONTINENTE/DISTRITO/`
- `CONTINENTE/DADOS/NORMALIZAÇÃO/`
- `CONTINENTE/DADOS/PUBLICACAO/`
- `CONTINENTE/ALOJAMENTOS/`
- `ILHA/AÇORES/`
- `ILHA/MADEIRA/`
- `PESQUISA/FONTES/`
- `PESQUISA/AUDITORIAS/`
- workflows de captura, normalização, validação, orquestração e publicação.

A estrutura dos Açores e da Madeira já existe como território de trabalho, mas este inventário não considera que isso signifique que os dados turísticos nacionais dessas regiões estejam preenchidos. Estrutura existente ≠ conteúdo validado.

## 6. Fontes/evidências já arquivadas

Já existem no TURISTURIS arquivos de fontes oficiais, incluindo:

- Turismo de Portugal — Dados Abertos;
- DGAL — Portal Autárquico;
- snapshots/manifestações de arquivo;
- auditorias de publicação;
- auditorias T1 de TOMAR;
- fichas oficiais RNET/RNAL.

Estas fontes devem alimentar as fases nacionais seguintes, sem substituir a verificação específica de cada entidade.

## 7. Critério de integração

Um ativo inventariado só pode ser promovido para uma camada nacional se houver:

1. identificação inequívoca;
2. território definido;
3. fonte identificável;
4. data de verificação;
5. tratamento dos campos voláteis;
6. estado interno de validação;
7. compatibilidade com o LAYOUT MESTRE;
8. ausência de duplicação com um registro canónico existente.

## 8. Regra territorial

A apresentação pública deve manter:

**Freguesia → Município → Distrito**

A freguesia nunca será atribuída por inferência destrutiva.

Para Açores e Madeira, a hierarquia territorial será adaptada sem apagar a unidade administrativa efetivamente suportada pela fonte.

## 9. Regra de contactos

Todo contacto telefónico com código internacional explícito deve preservar esse código no armazenamento, validação e exibição.

Regra:

`preserve_explicitly`

É proibido remover, substituir ou inferir destrutivamente o código internacional de outro país.

## 10. Resultado da FASE NACIONAL 0

O inventário confirma que o TURISTURIS já possui uma base material significativa para integração nacional:

- território municipal normalizado;
- pontos turísticos;
- alojamento local de pelo menos TOMAR e Peso da Régua;
- catálogo específico TOMAR;
- experiências;
- transportes;
- restauração;
- fontes oficiais arquivadas;
- estrutura territorial para Açores e Madeira.

O próximo passo não é reconstruir esses dados. É **normalizar, reconciliar e ligar o que já existe**, preservando a proveniência e evitando duplicação.

## 11. Pendências

- concluir a reconciliação dos 3 pontos TOMAR ainda pendentes de validação de conteúdo;
- determinar quais dos 68 pontos turísticos transversais já podem ser reconciliados com os documentos municipais;
- mapear todos os ativos municipais para a camada nacional;
- separar dados já publicados de dados apenas arquivados/editoriais;
- iniciar integração específica dos Açores e Madeira somente após o inventário dos seus dados efetivamente disponíveis;
- manter o SITE fora de alterações diretas até existir dataset nacional validado.

## 12. Próxima fase

**FASE NACIONAL 1 — TERRITÓRIO**

Objetivo: consolidar a camada territorial nacional a partir dos ativos já existentes, sem duplicar o catálogo municipal de 278 registos e sem promover dados turísticos por inferência.

