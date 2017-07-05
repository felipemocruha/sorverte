FROM alpine:3.6

ENV TZ=America/Sao_Paulo
RUN apk update && apk add --no-cache ca-certificates nginx \
    && mkdir -p /run/nginx \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

COPY ./nginx_conf /etc/nginx/conf.d/sorverte.conf
CMD ["nginx", "-g", "daemon off;"]