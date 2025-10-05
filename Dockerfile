FROM python:3-slim

RUN apt update && apt upgrade -y
RUN apt install git curl -y

WORKDIR /app/
COPY . /app/

RUN pip install -U pip
RUN pip install -U -r requirements.txt

EXPOSE 5000

CMD python3 main.py
