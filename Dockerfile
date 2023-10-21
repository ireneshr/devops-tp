FROM alpine:3.18

RUN apk add --no-cache python3-dev py3-pip\
    && pip3 install --upgrade pip

WORKDIR /devops-app

COPY . /devops-app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/routes.py"]