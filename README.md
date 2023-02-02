# django_drf
My Django DRF template

# Prerequisites
* [Docker](https://docs.docker.com/install/)

# Getting started
## Start local server
* `cp .env.example .env` and fill in the values
* `make up`
* `make migrate`
* navigate to `http://localhost:8000`

## Stop local server
* `make down`

## Logs  
* `make logs`

## Run tests
* `make test`

## Run linter
* `make lint`

# Why?
* custom user model
* `accounts` app (with create user and obtain token endpoints)
* settings with environment variables from .env file, drf settings, and logger
* docker-compose with nginx for proxy and static files

# Next step
* add main app and off you go. 