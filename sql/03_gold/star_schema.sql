-- Tabela dimensão para localização
--aplicar categorização de trechos da rodovia
CREATE OR REPLACE TABLE gold.dim_localizacao AS
WITH distintos AS(
    SELECT DISTINCT
        uf,
        br,
        municipio,
        -- Classificação de trechos a cada 20km
        CAST(FLOOR(km / 20) * 20 AS INT) || ' a ' || CAST((FLOOR(km / 20) * 20) + 19 AS INT) || ' km' AS trecho
    FROM silver.acidentes
)

SELECT
    -- Criar um id único para relacionamentos
    ROW_NUMBER() OVER () AS id_localizacao,
    *
FROM distintos

-- Tabela dimensão para situação do tempo e via
CREATE OR REPLACE TABLE

data_inversa
dia_semana
horario
causa_acidente
fase_dia
condicao_metereologica
faixas_via
tracado_via
via_urbana





-- Tabela fato com registros individuais de acidentes
id
qtd_envolvidos
qtd_mortos
qtd_feridos_leves
qtd_feridos_graves
qtd_ilesos
qtd_sit_desconhecida
qtd_total_feridos
qtd_veiculos
nome_origem