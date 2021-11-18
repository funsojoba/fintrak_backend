FROM python:3.8.0-slim as builder

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY . /app

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

