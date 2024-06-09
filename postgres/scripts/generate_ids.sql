INSTALL postgres;
LOAD postgres;
ATTACH '' AS psql (TYPE POSTGRES);

CREATE OR REPLACE TABLE psql.empresas AS (
    SELECT
        ROW_NUMBER() OVER() AS id_empresa,
        * EXCLUDE(id_empresa)
    FROM empresas
);

CREATE OR REPLACE TABLE psql.vagas AS (
    SELECT
        ROW_NUMBER() OVER() AS id_vaga,
        * EXCLUDE(id_vaga)
    FROM vagas
);

CREATE OR REPLACE TABLE psql.candidaturas AS (
    SELECT
        ROW_NUMBER() OVER() AS id_candidatura,
        * EXCLUDE(id_candidatura)
    FROM candidaturas
);