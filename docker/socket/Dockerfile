FROM alpine:3.6

COPY requirements.txt /
RUN apk update && apk add --no-cache --virtual build-deps \
        linux-headers \
        gcc \
        g++ \
        build-base \
        python3-dev \
     && apk add --no-cache \
        ca-certificates \
        python3 \
        uwsgi \
        uwsgi-python3 \
     && ln -s /usr/include/locale.h /usr/include/xlocale.h \
     && pip3 install -r requirements.txt \
     && mkdir -p /sorverte \
     && apk del build-deps
COPY ./server /sorverte/server
COPY ./run.py /sorverte
COPY ./server.ini /sorverte
RUN mkdir -p /log \
    && mkdir -p /socket
CMD uwsgi --ini /sorverte/server.ini