FROM python:3.8
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

VOLUME /web
WORKDIR /web
COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN useradd -ms /bin/bash  django
USER django
