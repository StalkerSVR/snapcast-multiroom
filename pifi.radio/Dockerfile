#https://github.com/rccavalcanti/pifi-radio
FROM debian

RUN apt-get update -y && apt-get -y install ruby-full tzdata build-essential bison openssl curl git-core zlib1g zlib1g-dev libssl-dev libyaml-dev libxml2-dev autoconf libc6-dev ncurses-dev automake libtool && apt-get clean

RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime &&\
    echo "Europe/Moscow" > /etc/timezone

RUN gem install pifi --no-document
RUN mkdir -p /etc/pifi

COPY config.json /etc/pifi/config.json
COPY streams.json /etc/pifi/streams.json

EXPOSE 3000

CMD ["pifi"]
