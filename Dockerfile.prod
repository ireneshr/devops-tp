FROM alpine:3.18

RUN apk add --no-cache python3-dev py3-pip\
    && pip3 install --upgrade pip

WORKDIR /devops-app

COPY . /devops-app

ENV DD_SERVICE="devops-tp"
ENV DD_ENV="dev"
ENV DD_VERSION="0.1.0"

LABEL com.datadoghq.tags.service="devops-tp"
LABEL com.datadoghq.tags.env="dev"
LABEL com.datadoghq.tags.version="0.1.0"

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["ddtrace-run", "python3", "-m", "src/routes.py"]