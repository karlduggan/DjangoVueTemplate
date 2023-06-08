FROM python:3.9-slim-buster

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY requirements.txt .

# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip pipenv flake8
COPY Pipfile* ./
RUN pipenv install --ignore-pipfile

RUN pip install -r requirements.txt

COPY . .

# Lint
RUN flake8 --ignore=E501,F401 ./backend
