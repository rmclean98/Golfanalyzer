FROM ubuntu:22.04 as Base

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install build-essential cmake git libgtk-3-dev pkg-config \
    python3-dev python3-numpy python3-opencv python3-pip -y

COPY . .