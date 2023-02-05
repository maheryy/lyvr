FROM python:3.11-alpine

WORKDIR /app

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# required psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install project dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt