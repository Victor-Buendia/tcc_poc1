import os
import regex
import duckdb
import threading

from utils import *
from logger.log import get_logger

conn = duckdb.connect(database=os.environ.get('DUCKDB_PATH'), read_only=False)
thread_amount = 8
log = get_logger('load_data')

def query(thread_id: int, sqls: str):
    cur = conn.cursor()
    log.info(f"Thread {thread_id} started")
    cur.execute(''.join(sqls))
    log.info(f"Thread {thread_id} executed {len(sqls)} queries")

def load(path: str, file_extension: str, compiled_regex: str, table_prefix: str = ''):
    files = find_files(path, file_extension)
    log.info(f"Found {len(files)} files to process")
    log.debug(f"Files found: {files}")

    dirs = list({regex.search(pattern=compiled_regex, string=x).group(1) for x in files})
    batches = separate_files(files, compiled_regex)
    log.info(f"The files were separated in {len(batches)} batches, namely: {batches.keys()}")
    log.debug(f"Files in each batch: {batches}")

    log.info("Creating tables in DuckDB")
    create_sqls = []
    for dir in batches.keys():
        create_sqls.append(f"CREATE OR REPLACE TABLE {table_prefix}{dir} AS (SELECT * FROM '{batches[dir][0]}');")
    log.debug(create_sqls)
    conn.execute(''.join(create_sqls))

    log.info("Creating COPY queries for DuckDB ingestion")
    copy_sqls = []
    for dir in batches.keys():
        for i in range(1, len(batches[dir])):
            copy_sqls.append(f"COPY {table_prefix}{dir} FROM '{batches[dir][i]}' (FORMAT JSON, ARRAY true);")
    log.debug(copy_sqls)

    threads = []
    for i in range(thread_amount):
        start = i * len(files) // thread_amount
        end = (i + 1) * len(files) // thread_amount
        if i == thread_amount - 1:
            end = len(files)
        thread = threading.Thread(target=query, args=(i, copy_sqls[start:end]))
        threads.append(thread)

    log.info("Triggering queries in parallel")
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    load(
        path='./data/curated',
        file_extension='json',
        compiled_regex=regex.compile(os.environ.get('CURATED_REGEX')),
    )
    log.info("Ingestion completed")

