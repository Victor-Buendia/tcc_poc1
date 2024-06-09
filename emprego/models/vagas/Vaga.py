from models.BaseModel import *

class Vaga(BaseModel):
    def __init__(self, **kwargs):
        kwargs.setdefault('id_vaga', None)
        kwargs.setdefault('id_empresa', fake.random_element(list(range(1, int(os.environ.get('N_EMPRESAS'))))))
        kwargs.setdefault('titulo', fake.job())
        kwargs.setdefault('descricao', fake.text(max_nb_chars=200))
        kwargs.setdefault('departamento', fake.word())
        kwargs.setdefault('localizacao', f"{fake.city()}, {fake.estado()}")
        kwargs.setdefault('data_abertura', fake.date_this_year().isoformat())
        kwargs.setdefault('data_fechamento', None)
        super().__init__(**kwargs)