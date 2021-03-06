-include .env
export

dev.install:
	@poetry install

lint:
	@mypy service
	@flake8 service

run:
	@python -m service run

service.run:
	@docker-compose up -d

db.run:
	@docker-compose up -d db

db.log:
	@docker-compose logs --tail 100 -f db

db.create:
	@python -m service create-db

db.stop:
	@docker-compose stop db

stop:
	@docker-compose stop -t1

clean:
	@docker-compose down

db.makemigration:
	@alembic revision --autogenerate -m "${message}"

db.migrate:
	@alembic upgrade head

alembic:
	@alembic ${command}

gunicorn:
	@gunicorn -w 4 -b 0.0.0.0:5000 'service.app:create_app()'
