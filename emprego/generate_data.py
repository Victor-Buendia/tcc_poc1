import os
import json
import multiprocessing

from logger.log import get_logger
from models.BaseModel import faker
from models import *

log = get_logger('generate_data')
processes = int(os.environ.get('PROCESSES_NO'))
raw_path = os.environ.get('RAW_PATH')

def generate_data(process_id: int, model: BaseModel, record_amount: int) -> None:
    try:
        faker.Faker.seed(process_id)
        model_name = model().__class__.__name__
        log.debug(f'Generating data for {model_name} in process {process_id}...')

        data = [model().__dict__ for _ in range(record_amount)]
        log.debug(f'Data successfully generated for {model_name} in process {process_id}...')

        log.debug(f'Saving data for {model_name} in process {process_id}...')

        with open(raw_path.format(model_name.lower(), model_name.lower(), process_id), 'w') as file:
            path = raw_path.format(model_name.lower(), model_name.lower(), process_id)
            log.debug(f'Saving data for for {model_name} in process {process_id} at {path}...')

            file.write(json.dumps(data, indent = 4))
            log.debug(f'Data successfully saved for {model_name} in process {process_id} at {path}...')
            log.info(f"Generated {record_amount} records for {model_name} in process {process_id}")
    except Exception as e:
        log.error(e)

if __name__ == '__main__':

    pool = multiprocessing.Pool()
    for model, records in models:
        for i in range(processes):
            pool.apply_async(
                func = generate_data,
                args = (i, model, records),
            )
    pool.close()
    pool.join()
    log.debug("Data generation completed")