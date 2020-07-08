FROM debian

RUN apt-get update -y && apt-get -y install mpd tzdata && apt-get clean
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime &&\
    echo "Europe/Moscow" > /etc/timezone
RUN mkdir -p /fifo

COPY mpd.conf /etc/mpd.conf

#EXPOSE 6600

CMD ["mpd","--no-daemon","/etc/mpd.conf"]
