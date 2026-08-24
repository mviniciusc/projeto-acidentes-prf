import duckdb
import os
import chardet

# criar banco e abrir conexão
con = duckdb.connect("dados/acidentes_db.duckdb")

#criar schema bronze
con.execute("CREATE SCHEMA IF NOT EXISTS bronze;")

#dropar tabela (use caso necessário)
# con.execute("DROP TABLE IF EXISTS bronze.acidentes")

#pasta com os dados csv
pasta_dados = 'dados/dados brutos'

#criar uma lista com os arquivos csv originais
arquivos_csv = [arquivo for arquivo in os.listdir(pasta_dados) if arquivo.endswith('.csv')]

#criar a estrutura da tabela
modelo = os.path.join(pasta_dados, arquivos_csv[0]) #caminho para o primeiro csv na pasta

# detectar automaticamente o encoding.
def detectar_encoding (modelo):
    with open(modelo, 'rb') as f:
        amostra=f.read(102400) #pega apenas uma amostra de 100kb do arquivo
        resultado=chardet.detect(amostra)
        return resultado['encoding'] #o retorno de chardet.detect é um dicionário. Aqui se pega apenas a resposta do encoding

enconding_modelo = detectar_encoding(modelo)

#criar a estrutura da tabela
caminho_sql = os.path.join('sql', '01_bronze', 'estrutura.sql') #o caminho do sql
with open(caminho_sql,'r',encoding='UTF-8') as f:
    query=f.read() #ler o sql pra criar o a estrutura

query=query.format(modelo=modelo,
                   enconding_modelo=enconding_modelo) #passa os dois parâmetros necessários

con.execute(query) #cria a estrutura

#percorrer os arquivos da pasta populando a tabela
for arquivo in arquivos_csv:
    caminho=os.path.join(pasta_dados,arquivo) #caminho completo do arquivo
    caminho_sql = os.path.join('sql', '01_bronze', 'xxxxxx') #caminho do sql
    enc = detectar_encoding(caminho) #pegar o encoding de cada arquivo
    with open(caminho_sql,'r',encoding='UTF-8') as f:
        query = f.read() #ler o sql que popula a tabela
    query = query.format( #passar os parâmetros necesssários
        arquivo=arquivo,
        caminho=caminho,
        encoding=enc
    )

    con.execute(query)

print("Camada bronze criada com sucesso!")
#não esquecer de fechar a conexão
con.close()