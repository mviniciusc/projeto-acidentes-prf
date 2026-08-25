-- Criar a estrutura da tabela
CREATE TABLE bronze.acidentes AS 
SELECT 
    *,
    '' AS nome_origem -- uma coluna que vai trazer o nome do arquivo de origem de cada linha para identificar possíveis erros
FROM read_csv_auto('{modelo}', all_varchar=True, encoding = 'latin-1')
LIMIT 0; --para trazer apenas a estrutura, sem popular nenhuma linha