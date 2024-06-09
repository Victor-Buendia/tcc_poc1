import os
import multiprocessing

from logger.log import get_logger
from models import *
from utils import *
from transform import *

log = get_logger('transform_data')
processes = int(os.environ.get('PROCESSES_NO'))

def transform_data(thread_id: int, dir_name: str, file_path: str) -> None:
    log.info(f"Transforming {dir_name} {file_path} {thread_id}")

    transformation_mapping[dir_name](dir_name, file_path, thread_id)
    log.info(f"Completed transforming for {dir_name} {file_path} {thread_id}")

if __name__ == '__main__':
    files = find_files('./data/raw', 'json')
    log.info(f"Found {len(files)} files to process: {files}")

    batches = separate_files(files, os.environ.get('RAW_REGEX'))
    log.info(f"The files were separated in {len(batches)} batches, namely: {batches.keys()}")
    log.debug(f"Files in each batch: {batches}")

    pool = multiprocessing.Pool()
    for dir_name in batches.keys():
        [
            pool.apply_async(
            func = transform_data,
            args = (i, dir_name, batches[dir_name][i]),
            ) for i in range(len(batches[dir_name]))
        ]
    pool.close()
    pool.join()
    log.info("Transformation completed")