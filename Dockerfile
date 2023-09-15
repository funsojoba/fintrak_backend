FROM python:3.10.6-slim as builder

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip install -r requirements.txt 


RUN chmod +x build.sh


