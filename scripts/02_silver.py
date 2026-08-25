import duckdb
import os

# abrir conexão
con = duckdb.connect("dados/acidentes_db.duckdb")

#criar schema silver
con.execute("CREATE SCHEMA IF NOT EXISTS silver;")

#dropar tabela (use caso necessário)
# con.execute("DROP TABLE IF EXISTS silver.acidentes")

