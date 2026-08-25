import duckdb
import os

# abrir conexão
con = duckdb.connect("dados/acidentes_db.duckdb")

#criar schema silver
con.execute("CREATE SCHEMA IF NOT EXISTS silver;")

#dropar tabela (use caso necessário)
# con.execute("DROP TABLE IF EXISTS silver.acidentes")

caminho_sql = os.path.join('sql', '02_silver', 'silver.sql') #o caminho do sql

with open(caminho_sql,'r', encoding='UTF-8') as f:
    query=f.read() #ler o sql da camada silver

con.execute(query)

print("Camada silver criada com sucesso!")

#não esqueça de fechar a conexão
con.close()