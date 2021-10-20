# syntax=docker/dockerfile:1
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8 as builder
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
#COPY . .
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#RUN apk add python3 py3-pip gcc python3-dev build-base

FROM builder as final
COPY app /code/app
#RUN python3 setup.py install
WORKDIR /code/
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]