#https://github.com/florianheinemann/MPD.FM
FROM node:12

ENV MPD_HOST=mpd-radio
ENV MPD_PORT=6600
ENV PORT=4200
ENV STATION_FILE=/app/stations.json

EXPOSE $PORT

RUN apt-get update && apt install git
RUN mkdir /app
RUN cd /app && git clone https://github.com/florianheinemann/MPD.FM.git && cd MPD.FM && npm install

COPY stations.json /app/stations.json
CMD ["node","/app/MPD.FM/bin/www"]
