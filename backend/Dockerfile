FROM python:3.11.7-slim-bookworm

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get -y install netcat-traditional gcc postgresql && apt-get clean

RUN pip install --upgrade pip
COPY ./backend-requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /backend

