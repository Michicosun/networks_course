FROM ubuntu

WORKDIR /prog
COPY ./find_mtu.py find_mtu.py

RUN apt update && yes | apt upgrade
RUN yes | apt install python3 iputils-ping
RUN chmod +x find_mtu.py

CMD [ "./find_mtu.py", "yandex.ru", "-v" ]
