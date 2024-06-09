from models.BaseModel import *

class Empresa(BaseModel):
    def __init__(self, **kwargs):
        kwargs.setdefault('id_empresa', None)
        kwargs.setdefault('nome', fake.name())
        kwargs.setdefault('cnpj', fake.cnpj())
        kwargs.setdefault('endereco', fake.address().replace('\n', ', '))
        kwargs.setdefault('cidade', fake.city())
        kwargs.setdefault('estado', fake.estado())
        kwargs.setdefault('pais', 'Brasil')
        kwargs.setdefault('telefone', fake.cellphone_number())
        kwargs.setdefault('email', fake.domain_name())
        super().__init__(**kwargs)