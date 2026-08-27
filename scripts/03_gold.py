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

#não esqueça de fechar a conexão
con.close()