FROM python:3.10.8-alpine3.16

WORKDIR /code

RUN apk update && \
apk add --virtual build-deps gcc musl-dev && \
apk add postgresql-dev

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt


COPY . /code

EXPOSE 3000

CMD ["ls"]

CMD ["uvicorn", "src.main:api.app", "--host", "0.0.0.0", "--port", "3000", "--reload"]