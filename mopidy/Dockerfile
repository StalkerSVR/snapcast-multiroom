FROM debian:sid

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y curl gnupg apt-transport-https apt-utils python-pip\
    && curl -L https://apt.mopidy.com/mopidy.gpg -o /tmp/mopidy.gpg \
    && curl -L https://apt.mopidy.com/mopidy.list -o /etc/apt/sources.list.d/mopidy.list \
    && apt-key add /tmp/mopidy.gpg \
    && apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        mopidy \
        mopidy-scrobbler \
        mopidy-soundcloud \
        mopidy-spotify \
        mopidy-tunein \
        git \
        gstreamer1.0-libav \
        python-crypto \
        python-setuptools

#RUN curl -L https://bootstrap.pypa.io/get-pip.py | python -
RUN pip install --ignore-installed Mopidy-Iris
RUN pip install -U six \
    && pip install markerlib \
    && pip install Mopidy-Local-SQLite \
    && pip install Mopidy-Local-Images \
#    && pip install Mopidy-Party \
    && pip install Mopidy-Simple-Webclient \
    && pip install Mopidy-MusicBox-Webclient \
    && pip install Mopidy-API-Explorer \
    && pip install Mopidy-Mopify

#ADD snapserver.deb /tmp/snapserver.deb
#RUN apt-get install -y libavahi-client3 libavahi-common3 \
#    && dpkg -i /tmp/snapserver.deb \
#    && apt-get install -f \
#    && rm /tmp/snapserver.deb

ADD mopidy.conf /etc/mopidy.conf

ADD entrypoint.sh /entrypoint.sh

RUN chown mopidy:audio -R /var/lib/mopidy \
    && chown mopidy:audio /entrypoint.sh

ADD localscan /usr/bin/localscan
RUN chmod +x /usr/bin/localscan

WORKDIR /root
RUN git clone https://github.com/aawsome/mopidy-snapcast.git
RUN cd mopidy-snapcast && pip install .

VOLUME /var/lib/mopidy
VOLUME /media
VOLUME /mopidy.conf

EXPOSE 6600
EXPOSE 6680
EXPOSE 6681

#USER mopidy

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/usr/bin/mopidy"]

