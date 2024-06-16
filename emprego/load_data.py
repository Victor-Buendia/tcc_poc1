import os
import regex
import duckdb

from utils import *
from logger.log import get_logger

conn = duckdb.connect(database=os.environ.get('DUCKDB_PATH'), read_only=False)
log = get_logger('ingest_data')

def ingest(path: str, file_extension: str, regex_pattern: str, table_prefix: str = ''):
    files = find_files(path, file_extension)
    log.info(f"Found {len(files)} files to process: {files}")

    dirs = list({regex.search(pattern=regex.compile(pattern=regex_pattern), string=x).group(1) for x in files})
    batches = separate_files(files, regex_pattern)
    log.info(f"The files were separated in {len(batches)} batches, namely: {batches.keys()}")
    log.debug(f"Files in each batch: {batches}")

    for dir in batches.keys():
        log.info(f"Ingesting {dir} files into DuckDB")
        for i in range(len(batches[dir])):
            if i == 0:
                sql = f"CREATE OR REPLACE TABLE {table_prefix}{dir} AS (SELECT * FROM '{batches[dir][i]}');"
                log.info(f"Executing SQL: {sql}")
                conn.execute(sql)
                log.info(f"Table {table_prefix}{dir} created with data from {batches[dir][i]}")
            else:
                sql = f"INSERT INTO {table_prefix}{dir} (SELECT * FROM '{batches[dir][i]}');"
                log.info(f"Executing SQL: {sql}")
                conn.execute(sql)
                log.info(f"Data from {batches[dir][i]} inserted into {table_prefix}{dir}")

if __name__ == '__main__':
    ingest(
        path='./data/curated',
        file_extension='json',
        regex_pattern=os.environ.get('CURATED_REGEX'),
    )
    log.info("Ingestion completed")

