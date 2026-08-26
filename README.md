# projeto-acidentes-prf


## Tratamento e prepadação dos dados

### Camada bronze
Nessa camada os dados foram lidos de arquivos .csv e salvos no banco de dados. A estrutura do banco foi criada a partir dos próprios arquivos. Os dados foram salvos integralmente como vieram da fonte.

### Camada silver
Nessa camada ocorreu o tratamento inicial dos dados. Colunas que não seriam utilizadas na análise foram removidas. O tipo dos dados foi corrigido, pois todos estavam com string na camada bronze.

### Camada gold
Aplicação de técnicas de análise e regras de negócio. Divisão da camada silver em tabelas dimensão e tabela fato. Ciração de IDs únicos para promover relacionamentos entre as tabelas.