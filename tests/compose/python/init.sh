#!/bin/bash

apt update -y
apt upgrade -y
apt install -y curl wget mc htop nano git unzip \
    python3 python3-pip make build-essential \
    libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
    libsqlite3-dev llvm libncursesw5-dev xz-utils \
    tk-dev libxml2-dev libxmlsec1-dev libffi-dev \
    liblzma-dev python python2

pip3 install -r /tmp/dev_requirements_3.txt

curl https://bootstrap.pypa.io/pip/2.7/get-pip.py | python2
pip2 install -r /tmp/dev_requirements_2.txt
