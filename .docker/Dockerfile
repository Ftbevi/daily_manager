FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN apk update \
    && apk --no-cache add gcc build-base musl-dev \
    python3-dev jpeg-dev \
    zlib-dev libjpeg postgresql-dev \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install -r requirements.txt

EXPOSE 8000
