# Start with Ubuntu base image
FROM ubuntu:16.04

# Install git, apt-add-repository and dependencies for iTorch
RUN apt-get update && apt-get install -y \
  git \
  software-properties-common \
  libssl-dev \
  libffi-dev \
  libzmq3-dev \
  python-pip \
  python2.7-dev \
  sudo

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install pyOpenSSL ndg-httpsclient pyasn1
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "lstm_server.py", "-dir", "data"]