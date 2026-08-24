SELECT
    *,
    '{arquivo}' AS nome_origem
FROM read_csv_auto('{caminho}', all_varchar=True, encoding = '{enc}')