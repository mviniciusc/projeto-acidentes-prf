-- Tabela dimensão para localização
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
FROM distintos;

-- Tabela dimensão para situação do tempo e via
CREATE OR REPLACE TABLE gold.dim_condicoes AS 
WITH condicoes_distintas AS (
    SELECT DISTINCT
        dia_semana,
        causa_acidente,
        fase_dia,
        condicao_metereologica,
        faixas_via,
        tracado_via,
        via_urbana
    FROM silver.acidentes
)
SELECT 
    -- Criar um id único para relacionamentos
    ROW_NUMBER() OVER () AS id_condicao,
    *
FROM condicoes_distintas;



-- Tabela fato com os registros de acidentes
CREATE OR REPLACE TABLE gold.fat_acidentes AS
SELECT 
    s.id,
    s.data_inversa,
    s.horario,
    s.qtd_envolvidos,
    s.qtd_mortos,
    s.qtd_feridos_leves,
    s.qtd_feridos_graves,
    s.qtd_ilesos,
    s.qtd_sit_desconhecida,
    s.qtd_total_feridos,
    s.qtd_veiculos,
    s.nome_origem,
    -- Chaves para relacionar com as dimensões
    loc.id_localizacao,
    cond.id_condicao
FROM silver.acidentes AS s

-- join com localizacao para pegar o id
JOIN gold.dim_localizacao AS loc 
    ON s.uf = loc.uf 
    AND s.br = loc.br 
    AND s.municipio = loc.municipio 
    -- refazer a lógica de classificação para obter os mesmos trechos
    AND CAST(FLOOR(s.km / 20) * 20 AS INT) || ' a ' || CAST((FLOOR(s.km / 20) * 20) + 19 AS INT) || ' km' = loc.trecho

-- join com condições para pegar o id
JOIN gold.dim_condicoes AS cond
    ON s.dia_semana = cond.dia_semana
    AND s.causa_acidente = cond.causa_acidente
    AND s.fase_dia = cond.fase_dia
    AND s.condicao_metereologica = cond.condicao_metereologica
    AND s.faixas_via = cond.faixas_via
    AND s.tracado_via = cond.tracado_via
    AND s.via_urbana = cond.via_urbana;