FROM python:3.11.6-alpine3.18
LABEL maintainer="oleksandr.hontarenko.dev@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR .

RUN apk update && \
    apk add postgresql-client

COPY wait-for-postgres.sh wait-for-postgres.sh
RUN chmod +x wait-for-postgres.sh

COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt
COPY . .