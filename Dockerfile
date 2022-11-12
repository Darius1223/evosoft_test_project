FROM python:slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update

COPY requirements requirements

RUN pip install --no-cache-dir -r requirements/production.txt

COPY . .

CMD scripts/startup.sh
