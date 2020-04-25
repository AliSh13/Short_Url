FROM ubuntu:latest
MAINTAINER Anisimov Aleksandr 'alex-just2200@yandex.ru'
RUN apt-get update -y
RUN apt-get install -y python-pip
RUN apt-get install -y uwsgi

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements.txt

CMD ["bash", "create_db.sh"]
ENTRYPOINT ["../venv/bin/uwsgi"]
CMD ["--http", "127.0.0.1:5001", "--ini", "uwsgi.ini"]