from models.BaseModel import *
from . import *

class Empresa(BaseModel):
    def __init__(self, **kwargs):
        id_empresa = 1
        nome = fake.random_element(elements=companies)
        cnpj = fake.cnpj()
        endereco = fake.address().replace('\n', ', ')
        cidade = fake.city()

        estado = fake.estado()
        estado_endereco = endereco.split('/')[-1].strip()
        while estado_endereco != estado[0]:
            estado = fake.estado()
        
        endereco = endereco.replace(' /', ',')
        pais = 'Brasil'

        telefone = fake.cellphone_number()
        while regex.match(pattern=r'^.\d{2} \(\d{2}\) \d{5}-\d{4}$', string=telefone) == None:
            telefone = fake.cellphone_number()

        dominio = fake.domain_name()
        
        kwargs.setdefault('id_empresa',     id_empresa)
        kwargs.setdefault('nome',           nome)
        kwargs.setdefault('cnpj',           cnpj)
        kwargs.setdefault('cidade',         cidade)
        kwargs.setdefault('estado',         estado)
        kwargs.setdefault('endereco',       endereco)
        kwargs.setdefault('pais',           pais)
        kwargs.setdefault('telefone',       telefone)
        kwargs.setdefault('dominio',        dominio)
        super().__init__(**kwargs)