FROM frolvlad/alpine-python3
RUN pip install snapcast

RUN apk update && apk add tzdata &&\ 
    cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime &&\ 
    echo "Europe/Moscow" > /etc/timezone &&\ 
    apk del tzdata && rm -rf /var/cache/apk/*

COPY crontab /etc/crontabs/root
COPY scripts /scripts
CMD chown root:root /etc/crontabs/root && /usr/sbin/crond -f
