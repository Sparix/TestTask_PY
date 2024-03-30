FROM python:3.11.6-alpine3.18
LABEL maintainer="oleksandr.hontarenko.dev@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR .

COPY requirements.txt requirements.txt
RUN  pip install -r requirements.txt
COPY . .