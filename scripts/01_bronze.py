import duckdb
import os

# criar banco e abrir conexão
con = duckdb.connect("dados/acidentes_db.duckdb")

#criar schema bronze
con.execute("CREATE SCHEMA IF NOT EXISTS bronze;")

#dropar tabela (use caso necessário)
con.execute("DROP TABLE IF EXISTS bronze.acidentes")

#pasta com os dados csv
pasta_dados = 'dados/dados_brutos'

#criar uma lista com os arquivos csv originais
arquivos_csv = [arquivo for arquivo in os.listdir(pasta_dados) if arquivo.endswith('.csv')]

#criar a estrutura da tabela
modelo = os.path.join(pasta_dados, arquivos_csv[0]) #caminho para o primeiro csv na pasta

#criar a estrutura da tabela
caminho_sql = os.path.join('sql', '01_bronze', 'estrutura.sql') #o caminho do sql
with open(caminho_sql,'r',encoding='UTF-8') as f:
    query=f.read() #ler o sql pra criar o a estrutura

query=query.format(modelo=modelo,) #passa o parâmetro necessário

con.execute(query) #cria a estrutura

#percorrer os arquivos da pasta populando a tabela
for arquivo in arquivos_csv:
    caminho=os.path.join(pasta_dados,arquivo) #caminho completo do arquivo
    caminho_sql = os.path.join('sql', '01_bronze', 'populacao.sql') #caminho do sql
    with open(caminho_sql,'r',encoding='UTF-8') as f:
        query = f.read() #ler o sql que popula a tabela
    query = query.format( #passar os parâmetros necesssários
        arquivo=arquivo,
        caminho=caminho
    )

    con.execute(query)

# Consulta de validação
resumo = con.execute("""
    SELECT nome_origem, COUNT(*) AS qtd 
    FROM bronze.acidentes 
    GROUP BY nome_origem 
    ORDER BY nome_origem
    """).fetchall()

print("\n--- RESUMO DA INGESTÃO BRONZE ---")
for arquivo, qtd in resumo:
    print(f" {arquivo}: {qtd:,} linhas")

total = con.execute("SELECT COUNT(*) FROM bronze.acidentes").fetchone()[0]
print(f"\n Total acumulado no banco: {total:,} registros!")

print("Camada bronze criada com sucesso!")
#não esquecer de fechar a conexão
con.close()