FROM python:3.10.2-slim

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml /app/
RUN poetry install --no-dev

COPY service /app/service

CMD ["python", "-m", "service", "run"]
