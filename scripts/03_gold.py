import duckdb
import os

# abrir conexão
con = duckdb.connect("dados/acidentes_db.duckdb")

#criar schema gold
con.execute("CREATE SCHEMA IF NOT EXISTS gold;")

#criar star schema
caminho_sql = os.path.join('sql', '03_gold', 'star_schema.sql') #o caminho do sql
with open(caminho_sql,'r', encoding='UTF-8') as f:
    query=f.read() #ler o sql da camada silver
con.execute(query)
print("Star schema criado com sucesso!")

#salvar as tabelas em parquet para exportar
con.execute("COPY gold.dim_localizacao TO 'dim_localizacao.parquet' (FORMAT PARQUET);")
con.execute("COPY gold.dim_condicoes TO 'dim_condicoes.parquet' (FORMAT PARQUET);")
con.execute("COPY gold.fat_acidentes TO 'fat_acidentes.parquet' (FORMAT PARQUET);")

#não esqueça de fechar a conexão
con.close()