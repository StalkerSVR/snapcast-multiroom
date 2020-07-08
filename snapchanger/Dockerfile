FROM frolvlad/alpine-python3
RUN pip install snapcast

RUN apk update && apk add tzdata &&\
    cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime &&\
    echo "Europe/Moscow" > /etc/timezone &&\
    apk del tzdata && rm -rf /var/cache/apk/*


COPY snapchanger.sh /root/snapchanger.sh
COPY snapchanger.py /root/snapchanger.py
ENTRYPOINT ["sh", "/root/snapchanger.sh"]
