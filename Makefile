#!/usr/bin/make -f

PROJECT_NAME := 'MODELS AUDITORY'

ROOT_FOLDER := $(shell pwd)
DOCKER_COMPOSE_FILE := $(ROOT_FOLDER)/docker-compose.yml
DOCKER_PROJECT_NAME := models_auditory
DOCKER_COMMAND := docker-compose -p $(DOCKER_PROJECT_NAME) -f $(DOCKER_COMPOSE_FILE)
DOCKER_COMPOSE_EXTRA_FILE := $(ROOT_FOLDER)/docker/docker-compose-extra.yml

ifeq ($(DOCKER_NAMESPACE),)
export DOCKER_NAMESPACE := mercadona
endif

ifeq ($(DOCKER_IMAGE_NAME),)
export DOCKER_IMAGE_NAME := acmo-api
endif

ifeq ($(DOCKER_IMAGE_TAG),)
export DOCKER_IMAGE_TAG := latest
endif

ifeq ($(DOCKER_BRANCH_NAME),)
export DOCKER_BRANCH_NAME := local
endif

build: ## Build project image
	$(DOCKER_COMMAND) build --no-cache --pull

env-start: ## Start project containers defined in docker-compose
	$(DOCKER_COMMAND) up -d

env-stop: ## Stop project containers defined in docker-compose
	$(DOCKER_COMMAND) -f $(DOCKER_COMPOSE_FILE) stop

migrate: ## Execute all pending Django migrations in project's main container
	$(DOCKER_COMMAND) exec -T api python manage.py migrate

create_admin_user: ## Execute all pending Django migrations in project's main container
	$(DOCKER_COMMAND) exec -T api python manage.py createsuperuser --username admin --email admin@example.com

reboot-database:
	$(DOCKER_COMMAND) exec -T api rm db.sqlite3 && $(DOCKER_COMMAND) exec -T api python manage.py migrate

bash: ## Open a bash shell in project's main container
	$(DOCKER_COMMAND) exec api bash

shell: ## Open a Django shell in project's main container
	$(DOCKER_COMMAND) exec api python manage.py shell

test: ## Run test suite in project's main container
	$(DOCKER_COMMAND) exec -T api pytest