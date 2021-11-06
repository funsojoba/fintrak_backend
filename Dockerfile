FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN adduser -D user
USER user