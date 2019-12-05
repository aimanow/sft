FROM ubuntu:latest

RUN apt-get update --fix-missing
RUN apt-get install --fix-missing -y \
    python3-dev python3-pip python3-numpy \
    gunicorn3

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade \
    requests \
    python-dotenv

WORKDIR /usr/src/app