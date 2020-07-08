FROM node:9-stretch

RUN apt update && apt-get -y install supervisor mpd

RUN mkdir -p /var/log/supervisor /fifo

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY ./plexamp /root/plexamp
COPY ./config /root/.config/Plexamp
COPY ./mpd.conf /etc/mpd.conf
EXPOSE 20000

CMD ["/usr/bin/supervisord"]
