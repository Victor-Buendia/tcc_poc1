CREATE SEQUENCE next_id_empresa START 1;
CREATE OR REPLACE TABLE Empresas (
    id_empresa INT PRIMARY KEY DEFAULT NEXTVAL('next_id_empresa'),
    nome VARCHAR,
    cnpj VARCHAR,
    endereco VARCHAR,
    cidade VARCHAR,
    estado VARCHAR,
    pais VARCHAR,
    telefone VARCHAR,
    email VARCHAR
);

