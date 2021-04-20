FROM python:latest
USER root
RUN apt-get update &&\
    apt-get install build-essential libssl-dev libffi-dev python3-dev python3-pip -y &&\
    pip3 install numpy pandas SQLAlchemy psycopg2