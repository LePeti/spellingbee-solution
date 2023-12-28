FROM python:3.11-alpine

WORKDIR /app

RUN apk add build-base
RUN apk add libffi-dev

COPY pyproject.toml .
# COPY poetry.lock .

RUN pip install --upgrade pip
RUN pip install poetry==1.7.1

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction \
    && rm -rf /root/.cache/pypoetry

RUN rm pyproject.toml

COPY app .

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
