FROM debian:latest

RUN apt-get update --fix-missing
RUN apt-get install -y \
    python3-dev python3-pip python3-numpy

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade \
    gunicorn \
    requests

WORKDIR /usr/src/app