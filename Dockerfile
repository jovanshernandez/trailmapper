FROM ubuntu:18.04

RUN apt update -y && \
    apt install -y software-properties-common && \
    add-apt-repository universe && \
    apt install -y python2.7-minimal && \
    apt install -y python-pip

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python2.7" ]

CMD [ "auth-demo/run.py" ]
