FROM debian

RUN apt-get update -y && apt-get -y install supervisor python3-pip tzdata&& pip3 install pip --upgrade && apt-get clean
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime &&\
    echo "Europe/Moscow" > /etc/timezone
RUN pip3 install python-mpd2 arrow snapcast
RUN mkdir -p /var/log/supervisor /fifo

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY radio_supervisor.py /root/radio_supervisor.py
COPY radio_supervisor2.py /root/radio_supervisor2.py
COPY radio_supervisor2.sh /root/radio_supervisor2.sh

CMD ["/usr/bin/supervisord"]
