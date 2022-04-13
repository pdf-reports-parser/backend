FROM python:3.10.2-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev

COPY service /app/service

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "service.app:create_app()"]
