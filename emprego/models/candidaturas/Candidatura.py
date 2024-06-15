from models.BaseModel import *
from . import *

class Candidatura(BaseModel):
    def __init__(self, **kwargs):
        nro_vagas = list(range(1, int(os.environ.get('N_VAGAS'))))
                         
        id_candidatura = 1
        id_vaga = int(fake.random_element(elements=nro_vagas))
        nome = fake.name()
        cpf = fake.cpf()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=60).isoformat()
        genero = fake.random_element(elements=('Masculino', 'Feminino', 'Outro'))
        estado_civil = fake.random_element(elements=('Solteiro', 'Casado', 'Divorciado', 'Viúvo'))
        endereco = fake.address().replace('\n', ', ')
        cidade = fake.city()

        estado = fake.estado()
        estado_endereco = endereco.split('/')[-1].strip()
        while estado_endereco != estado[0]:
            estado = fake.estado()
            
        pais = 'Brasil'
        
        telefone = fake.cellphone_number()
        while regex.match(pattern=r'^.\d{2} \(\d{2}\) \d{5}-\d{4}$', string=telefone) == None:
            telefone = fake.cellphone_number()

        email = regex.sub(pattern=r'@example\....', repl=fake.random_element(elements=['@gmail.com', '@hotmail.com', '@yahoo.com', '@outlook.com']), string=fake.ascii_safe_email())
        escolaridade = fake.random_element(elements=('Ensino Fundamental', 'Ensino Médio', 'Ensino Superior', 'Pós-Graduação', 'Mestrado', 'Doutorado'))
        experiencia_profissional = ' e '.join(fake.random_choices(elements=professional_experiences))
        habilidades = ', '.join(fake.random_choices(elements=skills))
        idiomas = ', '.join(fake.random_choices(elements=['Inglês', 'Espanhol', 'Francês', 'Alemão', 'Chinês', 'Japonês']))
        portfolio_url = fake.url()

        kwargs.setdefault('id_candidatura', id_candidatura)
        kwargs.setdefault('id_vaga', id_vaga)
        kwargs.setdefault('nome', nome)
        kwargs.setdefault('cpf', cpf)
        kwargs.setdefault('data_nascimento', data_nascimento)
        kwargs.setdefault('genero', genero)
        kwargs.setdefault('estado_civil', estado_civil)
        kwargs.setdefault('endereco', endereco)
        kwargs.setdefault('cidade', cidade)
        kwargs.setdefault('estado', estado)
        kwargs.setdefault('pais', pais)
        kwargs.setdefault('telefone', telefone)
        kwargs.setdefault('email', email)
        kwargs.setdefault('escolaridade', escolaridade)
        kwargs.setdefault('experiencia_profissional', experiencia_profissional)
        kwargs.setdefault('habilidades', habilidades)
        kwargs.setdefault('idiomas', idiomas)
        kwargs.setdefault('portfolio_url', portfolio_url)
        super().__init__(**kwargs)
