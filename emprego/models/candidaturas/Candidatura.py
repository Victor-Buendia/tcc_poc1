from models.BaseModel import *

class Candidatura(BaseModel):
    def __init__(self, **kwargs):
        kwargs.setdefault('id_candidatura', None)
        kwargs.setdefault('id_vaga', fake.random_element(list(range(1, int(os.environ.get('N_VAGAS'))))))
        kwargs.setdefault('nome', fake.name())
        kwargs.setdefault('cpf', fake.cpf())
        kwargs.setdefault('data_nascimento', fake.date_of_birth(minimum_age=18, maximum_age=60).isoformat())
        kwargs.setdefault('genero', fake.random_element(elements=('Masculino', 'Feminino', 'Outro')))
        kwargs.setdefault('estado_civil', fake.random_element(elements=('Solteiro', 'Casado', 'Divorciado', 'Viúvo')))
        kwargs.setdefault('endereco', fake.address().replace('\n', ', '))
        kwargs.setdefault('cidade', fake.city())
        kwargs.setdefault('estado', fake.estado())
        kwargs.setdefault('pais', 'Brasil')
        kwargs.setdefault('telefone', fake.cellphone_number())
        kwargs.setdefault('email', fake.email())
        kwargs.setdefault('escolaridade', fake.random_element(elements=('Ensino Fundamental', 'Ensino Médio', 'Ensino Superior', 'Pós-Graduação', 'Mestrado', 'Doutorado')))
        kwargs.setdefault('experiencia_profissional', fake.text(max_nb_chars=300))
        kwargs.setdefault('habilidades', ', '.join(fake.words(nb=5)))
        kwargs.setdefault('idiomas', ', '.join(fake.random_choices(elements=['Inglês', 'Espanhol', 'Francês', 'Alemão', 'Chinês', 'Japonês'])))
        kwargs.setdefault('portfolio_url', fake.url())
        super().__init__(**kwargs)
