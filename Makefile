ENV_FILE=docker.env
DB_PATH_ARG=/src/tcc_poc1.db
include docker.env
export

pipeline:
	$(MAKE) build
	$(MAKE) psql
	$(MAKE) generate
	$(MAKE) transform
	$(MAKE) ingest
	$(MAKE) load
	$(MAKE) patch



# ---------------------- COMMANDS ---------------------- #

build: # BUILDS ALL DOCKER IMAGES NEEDED FOR THE PROJECT
	docker build -t poc1-worker:latest -f ./docker/worker.Dockerfile .
	docker build -t poc1-duckdb:latest -f ./docker/duckdb.Dockerfile --build-arg DB_PATH_ARG=$(DB_PATH_ARG) .
clean: # REMOVES ALL GENERATED FILES
	rm -rf emprego/db/*
	rm -rf postgres/postgres_data
	rm -rf $$(find . -type d -name "__pycache__" | xargs)
	rm -rf $$(find . -type f -name "*.json" | xargs)
psql: # STARTS POSTGRES INSTANCE
	docker compose --env-file $(ENV_FILE) up -d postgres
duckdb: # STARTS DUCKDB INSTANCE AND OPENS DUCKDB CLIENT
	docker compose --env-file $(ENV_FILE) run -v $$(pwd)/emprego/db:/src --rm --name duckdb duckdb $(DB_PATH_ARG)
generate: # GENERATES RAW DATA
	docker compose --env-file $(ENV_FILE) run -v $$(pwd)/emprego:/src --rm --name generate_data worker generate_data.py
transform: # TRANSFORMS RAW DATA INTO CURATED DATA
	docker compose --env-file $(ENV_FILE) run -v $$(pwd)/emprego:/src --rm --name transform_data worker transform_data.py
ingest: # INGESTS DATA INTO DUCKDB
	docker compose --env-file $(ENV_FILE) run -v $$(pwd)/emprego:/src --rm --name ingest_data worker ingest_data.py
load: # LOADS DATA FROM DUCKDB TO POSTGRES
	docker compose --env-file $(ENV_FILE) run -v $$(pwd)/postgres:/src/postgres --rm --name duckdb duckdb -no-stdin -init ./postgres/scripts/generate_ids.sql $(DB_PATH_ARG)
	@echo "${BLUE}Data loaded finished!${END}"
patch: # MODIFIES DATA IN POSTGRES DATABASE
	docker exec $$(docker ps -f name=post -q) psql -U ${PGUSER} -d ${PGDATABASE} -f ./postgres/scripts/constraints.sql ${PGDATABASE}
	@echo "${BLUE}Data patching finished!${END}"
debug: # STARTS A DEBUG SESSION IN WORKER (PYTHON ENVIRONMENT)
	docker compose --env-file $(ENV_FILE) run -v $$(pwd)/emprego:/src --rm --entrypoint /bin/bash -i -t --name debug worker






PURPLE = \033[95m
CYAN = \033[96m
DARKCYAN = \033[36m
BLUE = \033[94m
GREEN = \033[92m
YELLOW = \033[93m
RED = \033[91m
BOLD = \033[1m
UNDERLINE = \033[4m
END = \033[0m