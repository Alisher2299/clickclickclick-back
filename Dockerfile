FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1 COLUMNS=200 TZ=Asia/Almaty

ADD ./src/requirements.txt /src/

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    gettext \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY ./src /src

CMD ["./entrypoint.sh"]
