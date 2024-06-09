CREATE SEQUENCE next_id_vaga START 1;
CREATE OR REPLACE TABLE Vagas (
    id_vaga INT PRIMARY KEY DEFAULT NEXTVAL('next_id_vaga'),
    id_empresa INT,
    titulo VARCHAR,
    descricao TEXT,
    departamento VARCHAR,
    localizacao VARCHAR,
    data_abertura DATE,
    data_fechamento DATE,
    FOREIGN KEY (id_empresa) REFERENCES Empresas(id_empresa)
);