# Dockerfile
FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements/base.txt /app/requirements/base.txt
RUN pip install -r requirements/base.txt
COPY . /app