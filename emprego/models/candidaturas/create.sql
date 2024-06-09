CREATE SEQUENCE next_id_candidatura START 1;
CREATE OR REPLACE TABLE Candidaturas (
    id_candidatura INT PRIMARY KEY DEFAULT NEXTVAL('next_id_candidatura'),
    id_vaga INT,
    nome VARCHAR,
    cpf VARCHAR,
    data_nascimento DATE,
    genero VARCHAR,
    estado_civil VARCHAR,
    endereco VARCHAR,
    cidade VARCHAR,
    estado VARCHAR,
    pais VARCHAR,
    telefone VARCHAR,
    email VARCHAR,
    escolaridade VARCHAR,
    experiencia_profissional TEXT,
    habilidades TEXT,
    idiomas TEXT,
    portfolio_url VARCHAR,
    FOREIGN KEY (id_vaga) REFERENCES Vagas(id_vaga)
);