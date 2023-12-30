FROM ubuntu
COPY . /opt/esp32

WORKDIR /opt/esp32

RUN apt-get update
RUN apt-get install -y python3.9 python3-pip
RUN apt-get install -y pkg-config
RUN apt-get install -y libmysqlclient-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PYTHONPATH=/opt/esp32

ENTRYPOINT ["python3", "app.py"]