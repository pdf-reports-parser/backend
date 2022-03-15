-include .env
export

dev.install:
	@poetry install

lint:
	@mypy service
	@flake8 service

run:
	@python -m service

service.run:
	@docker-compose up -d

db.run:
	@docker-compose up -d db

db.log:
	@docker-compose logs --tail 100 -f db

db.create:
	@python -m service.models

db.stop:
	@docker-compose stop db

stop:
	@docker-compose stop -t1

clean:
	@docker-compose down