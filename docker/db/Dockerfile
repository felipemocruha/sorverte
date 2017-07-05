FROM alpine:3.6

RUN apk update && apk add --no-cache mongodb \
    && rm /usr/bin/mongoperf \
    && mkdir -p /data/db

CMD mongod