# ARQUITETURA WORDPRESS — TURISTURIS

## 1. Objetivo

Definir a arquitetura técnica para publicar o TURISTURIS em WordPress sem transformar o CMS na fonte primária dos dados turísticos.

A arquitetura deve preservar a cadeia:

**PROMPT → CARTAS → LAYOUT MESTRE → DADOS → SITE → WORDPRESS**

O WordPress é a camada de apresentação, publicação e pesquisa.

## 2. Princípio de fonte de verdade

A fonte canônica das regras é o LAYOUT MESTRE.

A informação turística estruturada deve permanecer na camada DADOS.

O WordPress recebe dados por sincronização/importação controlada.

**Regra:** uma informação existente em DADOS não deve ser mantida manualmente em duplicado no WordPress sem uma razão editorial explícita.

## 3. Tipos de conteúdo

A primeira versão deverá considerar os seguintes tipos:

| Tipo | Finalidade |
|---|---|
| Destino | cidade, vila, região ou destino turístico |
| Ponto Turístico | monumento, museu, castelo, igreja, praia, parque, atração |
| Alojamento | hotel, pousada, hostel, alojamento local |
| Restaurante | restaurante e estabelecimentos gastronómicos |
| Transporte | estação, aeroporto, serviço ou operador turístico |
| Experiência | passeio, visita, atividade, enoturismo, natureza |
| Evento | festival, exposição, celebração ou evento turístico |
| Roteiro | itinerário composto por várias entidades |

## 4. Taxonomias

As taxonomias devem refletir a hierarquia territorial e turística definida pelo LAYOUT MESTRE.

### Territoriais

- Região
- Distrito ou Arquipélago
- Município
- Localidade

### Turísticas

- Categoria
- Tipo de turismo
- Perfil de visitante
- Património
- Tema

Não criar taxonomias redundantes quando um campo estruturado ou relacionamento resolver melhor o problema.

## 5. Campos estruturados

Os tipos de conteúdo devem utilizar os campos previstos no LAYOUT MESTRE, incluindo, quando aplicável:

- ID canônico
- Nome
- Tipo
- País
- Região
- Distrito ou Arquipélago
- Município
- Localidade
- Endereço
- Coordenadas
- Descrição
- História
- Interesse turístico
- Telefone
- Email
- Website
- Horários
- Preços
- Acessibilidade
- Serviços
- Reservas
- Fontes
- Data de verificação
- Data de atualização
- Estado de validação
- Grau de confiança
- Observações

## 6. Proveniência

Cada entidade publicada deve permitir identificar:

1. origem dos dados;
2. fonte utilizada;
3. data de verificação;
4. estado de validação;
5. eventual conflito entre fontes.

Informações voláteis — horários, preços, disponibilidade, contactos, encerramentos, obras e transportes — devem possuir data de verificação.

## 7. Fluxo de dados

Fluxo preferencial:

**FONTES → DADOS RAW → DADOS NORMALIZADOS → VALIDAÇÃO → PUBLICAÇÃO → WORDPRESS**

O WordPress não deve ser utilizado para corrigir silenciosamente a base canônica.

Quando houver correção de origem:

**WORDPRESS → identificação do problema → DADOS → validação → nova sincronização**

## 8. Integração técnica

A implementação deverá privilegiar:

- plugin próprio TURISTURIS para regras específicas;
- WordPress REST API;
- importação idempotente;
- IDs canônicos estáveis;
- sincronização incremental;
- logs de importação;
- tratamento de erros;
- possibilidade de execução via WP-CLI;
- tarefas agendadas para atualização;
- mecanismos de rollback quando necessário.

Evitar dependência excessiva de page builders para conteúdo estrutural.

## 9. Pesquisa

A pesquisa deverá permitir combinar:

- nome;
- município;
- localidade;
- região;
- categoria;
- tipo de turismo;
- perfil;
- proximidade geográfica;
- estado de validação, quando apropriado.

A arquitetura deve permitir evolução futura para pesquisa geográfica e filtros avançados.

## 10. Mapas

Entidades com coordenadas poderão ser exibidas em mapas.

As coordenadas devem permanecer associadas à entidade canônica e não ser digitadas manualmente em múltiplas páginas.

## 11. SEO

A publicação deverá prever:

- URLs estáveis;
- títulos e descrições consistentes;
- dados estruturados quando aplicáveis;
- sitemap;
- canonical URLs;
- breadcrumbs;
- páginas territoriais;
- páginas de categoria;
- controlo de conteúdos duplicados.

## 12. Desempenho

Prioridades:

- cache;
- imagens otimizadas;
- carregamento diferido;
- consultas eficientes;
- redução de plugins;
- CDN quando justificável;
- páginas críticas rápidas;
- monitorização de erros e desempenho.

## 13. Segurança e RGPD

A implementação deverá contemplar:

- atualizações controladas;
- princípio do menor privilégio;
- autenticação forte;
- proteção de contas administrativas;
- backups;
- logs;
- controlo de acesso;
- política de privacidade;
- cookies e consentimento quando aplicável;
- tratamento adequado de dados pessoais.

## 14. Conteúdo editorial

O WordPress poderá conter elementos editoriais que não pertençam à base turística estruturada, como:

- artigos;
- notícias;
- guias;
- páginas institucionais;
- conteúdos de campanha.

Esses conteúdos devem ser claramente diferenciados dos dados canônicos importados.

## 15. Regra para alterações

Nenhuma alteração estrutural do WordPress deve contrariar o LAYOUT MESTRE.

Se surgir uma necessidade estrutural nova:

1. identificar a necessidade;
2. verificar as CARTAS;
3. atualizar o LAYOUT, se necessário;
4. só então alterar a arquitetura técnica;
5. implementar;
6. validar;
7. documentar.

## 16. Primeira versão do SITE

Antes da instalação definitiva do WordPress, deverão ser produzidos e validados:

- arquitetura de informação;
- modelo de tipos de conteúdo;
- taxonomias;
- mapa de campos;
- contrato de sincronização;
- estratégia de IDs;
- estratégia de imagens;
- arquitetura de pesquisa;
- arquitetura de mapas;
- SEO;
- segurança/RGPD;
- backup e recuperação;
- plano de testes.

## 17. Regra de implementação

Não instalar uma coleção de plugins para resolver problemas ainda não modelados.

Primeiro:

**MODELO → CONTRATO → DADOS → SINCRONIZAÇÃO → WORDPRESS → INTERFACE**

Depois:

**TESTES → SEGURANÇA → DESEMPENHO → PUBLICAÇÃO**

## 18. Estado

Este documento é a especificação inicial da arquitetura WordPress do TURISTURIS.

A seleção concreta de plugins, tema, hospedagem e infraestrutura só deve ocorrer após validação desta arquitetura.
