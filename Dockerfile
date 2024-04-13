FROM python:3.11.8-alpine3.19

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update
RUN apk add --update npm

COPY . .

RUN set -x \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && npm install \
    && npm run build \
    && npm run build-css \
    && alembic upgrade head

EXPOSE 8000

CMD python run.py
