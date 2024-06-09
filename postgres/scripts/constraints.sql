ALTER TABLE empresas ADD CONSTRAINT id_empresa_pk PRIMARY KEY (id_empresa);
ALTER TABLE vagas ADD CONSTRAINT id_vaga_pk PRIMARY KEY (id_vaga);
ALTER TABLE candidaturas ADD CONSTRAINT id_candidatura_pk PRIMARY KEY (id_candidatura);

ALTER TABLE vagas ADD CONSTRAINT id_empresa__vagas_to_empresas_fk FOREIGN KEY (id_empresa) REFERENCES empresas(id_empresa);
ALTER TABLE candidaturas ADD CONSTRAINT id_vaga__candidaturas_to_vagas_fk FOREIGN KEY (id_vaga) REFERENCES vagas(id_vaga);