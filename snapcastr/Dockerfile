FROM debian:latest
RUN apt update && apt-get install -y gcc python3-dev linux-kernel-headers python3-pip && pip3 install poetry
RUN apt-get install -y git python3-venv && cd /root/ && git clone https://github.com/xkonni/snapcastr && cd snapcastr && poetry install
COPY snapcastrd.sh /root/snapcastr/snapcastrd.sh
EXPOSE 5011
ENTRYPOINT ["sh", "/root/snapcastr/snapcastrd.sh"]
