FILES = ${shell git diff --name-only --oneline HEAD "*.py"}

lint:
	pipenv run isort --recursive --force-single-line-imports --line-width 999 ${FILES}
	pipenv run autoflake --recursive --ignore-init-module-imports --in-place --remove-all-unused-imports ${FILES}
	pipenv run isort --recursive --use-parentheses --trailing-comma --multi-line 3 --force-grid-wrap 0 --line-width 140 ${FILES}
	pipenv run black ${FILES}

up:
	docker compose up -d web --build
	docker compose up -d nginx
	docker ps -a
	
ps:
	docker ps -a

down:
	docker compose down	-v

_prod:
	docker compose -f docker-compose.prod.yml up -d --build
	docker ps -a

collectstatic:
	docker compose exec web python manage.py collectstatic --no-input

migrate:
	docker compose exec web python manage.py migrate

build:
	docker compose build

logs:
	docker compose logs -f

test:
	docker compose run --rm --entrypoint="python" web manage.py test ${K}

prod: _prod migrate collectstatic ps

prod_restart: down prod
