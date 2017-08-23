FROM python:3.6-alpine
WORKDIR /web
RUN mkdir -p /web
ADD requirements.txt /web/
RUN pip install -r requirements.txt
ADD . /web
ENV FLASK_APP ./web/run.py
