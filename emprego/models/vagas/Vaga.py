from datetime import datetime
from models.BaseModel import *
from . import *

class Vaga(BaseModel):
    def __init__(self, **kwargs):
        nro_empresas = list(range(1, int(os.environ.get('N_EMPRESAS'))))

        id_vaga = 1
        id_empresa = int(fake.random_element(elements=nro_empresas))
        titulo = fake.random_element(elements=job_titles)
        contrato = fake.random_element(elements=['Estágio', 'CLT', 'PJ', 'Freelancer'])
        modalidade = fake.random_element(elements=['Remoto', 'Presencial', 'Híbrido'])
        localizacao = fake.estado()
        data_abertura = fake.date_this_year().isoformat()
        data_fechamento = fake.date_between(start_date=datetime.strptime(data_abertura, '%Y-%m-%d')).isoformat()

        kwargs.setdefault('id_vaga', id_vaga)
        kwargs.setdefault('id_empresa', id_empresa)
        kwargs.setdefault('titulo', titulo)
        kwargs.setdefault('contrato', contrato)
        kwargs.setdefault('modalidade', modalidade)
        kwargs.setdefault('localizacao', localizacao)
        kwargs.setdefault('data_abertura', data_abertura)
        kwargs.setdefault('data_fechamento', data_fechamento)
        
        super().__init__(**kwargs)