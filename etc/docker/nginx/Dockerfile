FROM nginx:alpine

RUN apk update \
    && apk upgrade \
    && apk add --no-cache openssl \
    && apk add --no-cache bash

COPY ./nginx.conf /etc/nginx/
COPY ./conf.d/ /etc/nginx/conf.d/

COPY ./ssl/ /etc/nginx/ssl/
COPY ./release.txt /var/www/html/
COPY ./releaselog.txt /var/www/html/