# projeto-acidentes-prf

## Visão Geral
Este repositório contém o pipeline de dados e a documentação do projeto de análise de acidentes em rodovias federais brasileiras. O objetivo foi transformar milhares de registros brutos da Polícia Rodoviária Federal (PRF) em um painel interativo, permitindo assim extrair insights sobre severidade, letalidade e infraestrutura para direcionamento de políticas e recursos públicos. Para reforçar a relevância atual dos resultados obtidos, foram considerados dados de 2021 a 2025.

Os dados foram obtidos diretamente do portal de dados abertos da PRF e podem ser encontrados [clicando aqui](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf).


## Tratamento e prepadação dos dados
Para garantir performance e escalabilidade, o pipeline foi construído utilizando DuckDB para o processamento em lote da base histórica selecionada. O tratamento seguiu os princípios da Arquitetura Medalhão

### Camada bronze
Nessa camada os dados foram lidos de arquivos .csv e salvos no banco de dados. A estrutura do banco foi criada a partir dos próprios arquivos. Os dados foram salvos integralmente como vieram da fonte.

### Camada silver
Nessa camada ocorreu o tratamento inicial dos dados. Colunas que não seriam utilizadas na análise foram removida e o tipo dos dados foi corrigido.

### Camada gold
Aplicação de técnicas de análise e regras de negócio. Divisão da camada silver em tabelas dimensão e tabela fato. Criação de IDs únicos para promover relacionamentos entre as tabelas. Criação de medidas personalizadas para a análise, como o agrupamento dos registros em trechos de cada rodovia. As tabelas prontas foram exportadas em formato parquet para uso em ferramentas de visualização.

## O dashboard
Para a visualização e análise dos dados, produzi um dashboard usando PowerBI. A estrtutura do dashboard foi dividida em duas páginas. Na primeira página o foco é entender onde e quando as ocorrências foram registradas. Na segunda página busquei estudar as causas e circustâncias desses registros.

O dashboard final pode ser publicamente acessado [clicando aqui](https://app.powerbi.com/view?r=eyJrIjoiZDQ5NGU0ODUtN2E2ZC00OTA1LWE1ZGItYTkyODI3OTU3NmRlIiwidCI6IjY1OWNlMmI4LTA3MTQtNDE5OC04YzM4LWRjOWI2MGFhYmI1NyJ9).

## A análise
A análise completa, com as principais conclusões e propostas de decisão, está publicada [nesse artigo](https://medium.com/@mviniciusc93/an%C3%A1lise-de-acidentes-em-rodovias-federais-7ae0d15200c3). Lá explico melhor como as análises foram feitas e o raciocínio por trás das orientações. 

Agradeço a todos que prestigiaram meu projeto nesse repositório. Fiquem à vontade para contato e comentários acessando minha [página do Linkedin](www.linkedin.com/in/marcus-vinicius-121582306).