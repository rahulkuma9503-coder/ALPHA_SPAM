FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip python3-venv -y

# Create and use a virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

WORKDIR /app/
COPY . /app/

# Install dependencies using the virtual environment's pip
RUN pip install -U pip
RUN pip install -U -r requirements.txt

CMD python3 main.py
