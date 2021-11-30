FROM python:3.9.6-slim-buster

ADD . /tact

WORKDIR /tact

RUN pip install -r requirements.txt

EXPOSE 2000

CMD ["python3","app.py"]

