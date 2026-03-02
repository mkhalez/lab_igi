FROM python:3.13.12-slim-trixie

RUN apt-get update && apt-get install -y git

WORKDIR /app

RUN git clone https://github.com/smartiqaorg/geometric_lib

WORKDIR /app/geometric_lib

COPY main.py .

ENV VALUE_TO_PUT=5

CMD [ "python", "main.py" ]
