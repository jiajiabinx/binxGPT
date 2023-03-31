FROM python:3.8.10

RUN mkdir /binxGPT 

COPY . /binxGPT

COPY pyproject.toml /binxGPT 

WORKDIR /binxGPT

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --only main

ENV PORT=443

CMD gunicorn --bind 0.0.0.0:$PORT app:app