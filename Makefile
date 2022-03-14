-include .env
export

dev.install:
	@poetry install

lint:
	@echo -e 'start linting.\n-------mypy start-------'
	@mypy service || echo '\n-------flake8 start-------'
	@flake8 service

run:
	@python -m service

db.run:
	@docker-compose up -d db

db.log:
	@docker-compose logs --tail 100 -f db

db.create:
	@python -m service.models

stop:
	@docker-compose stop -tl

clean:
	@docker-compose down