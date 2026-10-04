# LAYOUT MESTRE — TURISTURIS

## 1. Função
Este documento transforma as Cartas do TURISTURIS em uma estrutura operacional única.

## 2. Estrutura canônica
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

## 3. Organização territorial
Portugal → região → distrito/arquipélago → município → entidade.

## 4. Categorias iniciais
ponto turístico, alojamento, restaurante, transporte, experiência, evento e serviço.

## 5. Modelo mínimo
id; nome; tipo; país; região; distrito ou arquipélago; município; localização; endereço; coordenadas; descrição; contactos; horários; preços; acessibilidade; website; fontes; data_verificação; estado_validação; observações.

## 6. Proveniência
Toda entidade relevante deve apontar para sua fonte. Para dados voláteis, registrar data de verificação.

## 7. Separação de dados
DADOS/raw = material original quando permitido.
DADOS/normalizados = dados estruturados.
DADOS/fontes = catálogo de fontes.

## 8. Regra para código
Código novo deve ser criado somente depois de necessidade, estrutura e origem dos dados estarem definidas.

## 9. Regra para novas cidades
Um município novo deve seguir o mesmo modelo dos anteriores. Não criar arquitetura particular para acomodar um destino.

## 10. Controle
Mudanças no Layout Mestre que alterem princípios do projeto devem ser deliberadas e refletidas nas cartas.
