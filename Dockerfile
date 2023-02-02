FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./Pipfile ./Pipfile.lock ./

RUN pip3 install pipenv gunicorn && pipenv install --system

COPY apps ./apps

COPY settings ./settings

COPY manage.py ./

ENTRYPOINT [ "gunicorn" ]

CMD [ "--bind", "0.0.0.0:8000", "settings.wsgi:application" ]
