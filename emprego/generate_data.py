import os
import json
import multiprocessing

from logger.log import get_logger
from models import *

log = get_logger('generate_data')
processes = int(os.environ.get('PROCESSES_NO'))
raw_path = os.environ.get('RAW_PATH')

def generate_data(thread_id: int, model: BaseModel, record_amount: int) -> None:
    model_name = model().__class__.__name__
    log.info(f'Generating data for {model_name} in thread {thread_id}...')

    data = [model().__dict__ for _ in range(record_amount)]
    log.info(f'Data successfully generated for {model_name} in thread {thread_id}...')

    log.info(f'Saving data for {model_name} in thread {thread_id}...')

    with open(raw_path.format(model_name.lower(), model_name.lower(), thread_id), 'w') as file:
        path = raw_path.format(model_name.lower(), model_name.lower(), thread_id)
        log.info(f'Saving data for for {model_name} in thread {thread_id} at {path}...')

        file.write(json.dumps(data, indent = 4))
        log.info(f'Data successfully saved for {model_name} in thread {thread_id} at {path}...')

if __name__ == '__main__':

    pool = multiprocessing.Pool()
    for model, records in models:
        [
            pool.apply_async(
            func = generate_data,
            args = (i, model, records),
            ) for i in range(processes)
        ]
    pool.close()
    pool.join()
    log.info("Data generation completed")