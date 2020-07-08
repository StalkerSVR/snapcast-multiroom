FROM ubuntu:16.04
RUN apt-get update && apt-get install -y software-properties-common curl wget
RUN add-apt-repository ppa:jean-francois-dockes/upnpp1

RUN apt-get update && apt-get install upmpdcli -y
RUN apt-get install -y mpd supervisor

RUN mkdir -p /var/log/supervisor /fifo

COPY mpd.conf /etc/mpd.conf
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 1900/udp
EXPOSE 49152

ENTRYPOINT ["/usr/bin/supervisord"]
