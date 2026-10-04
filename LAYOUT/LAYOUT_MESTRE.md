# LAYOUT MESTRE — TURISTURIS

## 1. Função
Este documento transforma as Cartas do TURISTURIS em uma estrutura operacional única.

## 2. Hierarquia de referência
**CARTA REGENTE → CARTAS ESPECIALIZADAS → LAYOUT MESTRE → DADOS E CÓDIGO**

As Cartas definem regras; o Layout consolida a estrutura operacional; dados e código devem obedecer ao Layout.

## 3. Estrutura canônica
TURISTURIS/
├── README.md
├── LICENSE
├── CARTAS/
├── LAYOUT/
├── PORTUGAL/
├── PONTOS_TURISTICOS/
├── ALOJAMENTOS/
├── RESTAURANTES/
├── TRANSPORTES/
├── EXPERIENCIAS/
├── CALENDARIO/
├── DADOS/
├── PESQUISA/
├── FONTES/
└── .github/workflows/

## 4. Organização territorial
Portugal → região → distrito/arquipélago → município → localidade → entidade.

## 5. Categorias
ponto turístico, alojamento, restaurante, transporte, experiência, evento e serviço.

## 6. Domínios turísticos
O modelo deve suportar destinos, património, cultura, história, gastronomia, enoturismo, natureza, turismo religioso, turismo balnear, turismo urbano, turismo rural, turismo termal e bem-estar, eventos, roteiros e diferentes perfis de visitantes.

## 7. Modelo mínimo
id; nome; tipo; país; região; distrito ou arquipélago; município; localidade; endereço; coordenadas; descrição; história; interesse turístico; contactos; telefone; email; website; horários; preços; acessibilidade; serviços; reservas; fontes; data_verificação; data_atualização; estado_validação; grau_confiança; observações.

## 8. Proveniência
Toda entidade relevante deve apontar para sua fonte. Dados voláteis devem registrar data de verificação. Conflitos entre fontes devem ser preservados e explicitados até serem resolvidos.

## 9. Estados de validação
NAO_VERIFICADO; EM_VERIFICACAO; VERIFICADO; CONFLITO; DESATUALIZADO; ARQUIVADO.

## 10. Separação de dados
DADOS/raw = material original quando permitido.
DADOS/normalizados = dados estruturados.
DADOS/fontes = catálogo de fontes.

## 11. Regra contra invenção
Não preencher lacunas com suposições. Horários, preços, contactos, disponibilidade, eventos, endereços e websites devem ter origem identificável quando apresentados como fatos.

## 12. Regra para código
Código novo deve ser criado somente depois de necessidade, estrutura e origem dos dados estarem definidas.

## 13. Regra para novas cidades
Um município novo deve seguir o mesmo modelo dos anteriores. Não criar arquitetura particular para acomodar um destino.

## 14. Roteiros e comparações
Roteiros devem considerar duração, deslocações, custos, horários, proximidade, refeições, alojamento, transporte, perfil do visitante e época do ano. Comparações devem usar critérios explicitamente identificados.

## 15. Controle
Mudanças no Layout Mestre que alterem princípios do projeto devem ser deliberadas e refletidas nas Cartas.

## 16. Carta especializada de turismo
A CARTAS/CARTA_DE_TURISMO_PORTUGUES.md é a referência especializada para o domínio do turismo português e deve ser aplicada em novas pesquisas e entidades turísticas.

## 17. Sequência oficial
**PROMPT → CARTAS → LAYOUT MESTRE → ESTRUTURA → DADOS → CÓDIGO**

O Layout Mestre é a referência operacional para a criação dos novos artefactos do projeto.
