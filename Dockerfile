FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /movie_review_app

COPY Pipfile Pipfile.lock /movie_review_app/
RUN pip install pipenv && pipenv install --system

COPY . /movie_review_app