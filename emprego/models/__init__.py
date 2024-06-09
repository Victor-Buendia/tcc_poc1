import os

from models.BaseModel import BaseModel
from models.empresas.Empresa import Empresa
from models.candidaturas.Candidatura import Candidatura
from models.vagas.Vaga import Vaga

models = [
    (
        Empresa, 
        int(os.environ.get('N_EMPRESAS'))//int(os.environ.get('PROCESSES_NO'))
    ), 
    (
        Vaga,
        int(os.environ.get('N_VAGAS'))//int(os.environ.get('PROCESSES_NO'))
    ),
    (
        Candidatura,
        int(os.environ.get('N_CANDIDATURAS'))//int(os.environ.get('PROCESSES_NO'))
    )
]
