include .env
export

dev.install:
	@poetry install

lint:
	@mypy service
	@flake8 service

run:
	@echo $$DB_URL
	@python -m service

db.run:
	@docker-compose up -d db

db.log:
	@docker-compose logs --tail 100 -f db

db.create:
	@echo $$DB_URL
	@python -m service.models

db.stop:
	@docker-compose stop db

stop:
	@docker-compose stop -tl

clean:
	@docker-compose down