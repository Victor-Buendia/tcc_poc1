import os
import json

curated_path = os.environ.get('CURATED_PATH')

def transform_candidaturas(dir_name: str, file_path: str, thread_id: int) -> None:
    with open(file_path, 'r') as file:
        data = json.load(file)
        transformed_data = [
            {
                'id_candidatura': record['id_candidatura'],
                'id_vaga': record['id_vaga'],
                'nome': record['nome'],
                'cidade': record['cidade'],
                'estado': record['estado'],
                'pais': record['pais'],
                'telefone': record['telefone'],
                'email': record['email'],
                'experiencia_profissional': record['experiencia_profissional'],
                'habilidades': record['habilidades'],
                'idiomas': record['idiomas'],
                'portfolio_url': record['portfolio_url'],
            } for record in data
        ]
    with open(curated_path.format(dir_name, dir_name, thread_id), 'w') as file:
        file.write(json.dumps(transformed_data, indent=4))
        
def no_transform(dir_name: str, file_path: str, thread_id: int) -> None:
    with open(file_path, 'r') as file:
        data = json.load(file)
        transformed_data = [record for record in data]
    with open(curated_path.format(dir_name, dir_name[:-1], thread_id), 'w') as file:
        file.write(json.dumps(transformed_data, indent=4))

transformation_mapping = {
    'candidaturas': transform_candidaturas,
    'empresas': no_transform,
    'vagas': no_transform,
}