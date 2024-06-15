CREATE OR REPLACE TABLE vagas AS (
    SELECT DISTINCT
        v.* EXCLUDE(data_fechamento, localizacao),
        IF(RANDOM()<=0.8, NULL, v.data_fechamento) AS data_fechamento,
        IF(v.modalidade = 'Remoto', ['Remoto', 'Brasil'], e.estado) AS localizacao
    FROM vagas AS v
    LEFT JOIN empresas AS e ON v.id_empresa = e.id_empresa
);

CREATE OR REPLACE TABLE candidaturas AS (
    SELECT DISTINCT
        c.* EXCLUDE(estado, endereco),
        IF(v.modalidade = 'Remoto', c.estado, v.localizacao) AS estado,
        IF(v.modalidade = 'Remoto', REGEXP_REPLACE(c.endereco, '/ (..)', '/ '||c.estado), REGEXP_REPLACE(c.endereco, '/ (..)', '/ '||v.localizacao[1])) AS endereco
    FROM candidaturas AS c
    LEFT JOIN vagas AS v ON c.id_vaga = v.id_vaga
);