FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

# Обновление списка пакетов и установка необходимых зависимостей
RUN apt-get update && apt-get install -y \
    pkg-config \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
