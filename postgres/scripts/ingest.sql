INSTALL postgres;
LOAD postgres;
ATTACH '' AS psql (TYPE POSTGRES);

CREATE OR REPLACE TABLE psql.empresas AS (
    SELECT DISTINCT * FROM empresas
);

CREATE OR REPLACE TABLE psql.vagas AS (
    SELECT DISTINCT * FROM vagas
);

CREATE OR REPLACE TABLE psql.candidaturas AS (
    SELECT DISTINCT * FROM candidaturas
);