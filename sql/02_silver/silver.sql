-- colunas que não serão usadas na análise
    -- sentido_via,
    -- latitude,
    -- longitude,
    -- regional,
    -- delegacia,
    -- uop;


-- tratar os tipos corretos e remover espaços
CREATE OR REPLACE TABLE silver.acidentes AS
    SELECT DISTINCT
        TRIM(id) AS id,
        TRY_CAST(data_inversa AS DATE) AS data_inversa, --já está no padrão americano
        TRIM(LOWER(dia_semana)) AS dia_semana,
        TRY_CAST(horario AS TIME) AS horario,
        TRIM(UPPER(uf)) AS uf,
        TRIM(br) AS br,
        TRY_CAST(REPLACE(km, ',', '.') AS DOUBLE) AS km, --muda para o padrão de decimal com ponto
        TRIM(LOWER(municipio)) AS municipio,
        TRIM(LOWER(causa_acidente)) AS causa_acidente,
        TRIM(LOWER(fase_dia)) AS fase_dia,
        TRIM(LOWER(condicao_metereologica)) AS condicao_metereologica,
        TRIM(LOWER(tipo_pista)) AS faixas_via,
        TRIM(LOWER(tracado_via)) AS tracado_via,
        TRIM(LOWER(uso_solo)) AS via_urbana,
        TRY_CAST(pessoas AS INT) AS qtd_envolvidos,
        TRY_CAST(mortos AS INT) AS qtd_mortos,
        TRY_CAST(feridos_leves AS INT) AS qtd_feridos_leves,
        TRY_CAST(feridos_graves AS INT) AS qtd_feridos_graves,
        TRY_CAST(ilesos AS INT) AS qtd_ilesos,
        TRY_CAST(ignorados AS INT) AS qtd_sit_desconhecida,
        TRY_CAST(feridos AS INT) AS qtd_total_feridos,
        TRY_CAST(veiculos AS INT) AS qtd_veiculos,
        TRIM(LOWER(nome_origem)) AS nome_origem
    FROM bronze.acidentes