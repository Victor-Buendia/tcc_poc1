CREATE OR REPLACE TABLE empresas AS (
    SELECT DISTINCT
        ROW_NUMBER() OVER() AS id_empresa,
        * EXCLUDE(id_empresa)
    FROM empresas
);

CREATE OR REPLACE TABLE vagas AS (
    SELECT DISTINCT
        ROW_NUMBER() OVER() AS id_vaga,
        * EXCLUDE(id_vaga)
    FROM vagas
);

CREATE OR REPLACE TABLE candidaturas AS (
    SELECT DISTINCT
        ROW_NUMBER() OVER() AS id_candidatura,
        * EXCLUDE(id_candidatura)
    FROM candidaturas
);