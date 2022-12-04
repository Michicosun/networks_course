# Поиск MTU на пути между 2мя хостами

В файле `find_mtu.py` реализован алгоритм поиска MTU, основанный на бинарном поиске по размеру отправляемого ICMP пакета, проверка достижимости производится через встроенную в ubuntu-20.04 программу ping

# пример использования

Собираем Docker образ
```bash
$ cd lab2
$ docker build . -f Dockerfile -t mtu_finder
Sending build context to Docker daemon  6.144kB
Step 1/7 : FROM ubuntu
 ---> a8780b506fa4
Step 2/7 : WORKDIR /prog
 ---> Using cache
 ---> 12e9279bcb9b
Step 3/7 : COPY ./find_mtu.py find_mtu.py
 ---> Using cache
 ---> 7c291b4cc96f
Step 4/7 : RUN apt update && yes | apt upgrade
 ---> Using cache
 ---> 62860d89043d
Step 5/7 : RUN yes | apt install python3 iputils-ping
 ---> Using cache
 ---> 8e9bbbf41dd5
Step 6/7 : RUN chmod +x find_mtu.py
 ---> Using cache
 ---> c185c8c9f79d
Step 7/7 : CMD [ "./find_mtu.py", "yandex.ru", "-v" ]
 ---> Using cache
 ---> acf4de674d53
Successfully built acf4de674d53
Successfully tagged mtu_finder:latest
```

Пример запуска
```bash
$ docker run --rm mtu_finder
checking connectivity... SUCCESS
sending ping with size 750...	 OK, 	current borders: [750, 1501)
sending ping with size 1125...	 OK, 	current borders: [1125, 1501)
sending ping with size 1313...	 OK, 	current borders: [1313, 1501)
sending ping with size 1407...	 OK, 	current borders: [1407, 1501)
sending ping with size 1454...	 OK, 	current borders: [1454, 1501)
sending ping with size 1477...	 FAIL, 	current borders: [1454, 1477)
sending ping with size 1465...	 OK, 	current borders: [1465, 1477)
sending ping with size 1471...	 OK, 	current borders: [1471, 1477)
sending ping with size 1474...	 FAIL, 	current borders: [1471, 1474)
sending ping with size 1472...	 OK, 	current borders: [1472, 1474)
sending ping with size 1473...	 FAIL, 	current borders: [1472, 1473)
result MTU: 1500
$ _
```

По умолчанию MTU будет искаться до серверов Yandex, это можно поменять в Dockerfile
