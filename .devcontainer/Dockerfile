FROM ubuntu

RUN apt update
RUN apt -y dist-upgrade
RUN apt -y install git git-lfs python3 python3-pip htop screen unzip psmisc nvtop wget curl gnupg net-tools

RUN echo "root:root" | chpasswd
RUN useradd -ms /bin/bash -u 1000 mim
USER mim
WORKDIR /home/mim
RUN export PATH=$PATH:/home/mim/.local/bin

RUN python3 -m pip install --upgrade pip
RUN pip install simpleitk
