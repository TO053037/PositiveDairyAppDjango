FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apt update
RUN apt-get update
RUN apt install -y nodejs
RUN apt install -y npm
RUN apt install -y firefox-esr
RUN pip install -r requirements.txt
ADD . /code/