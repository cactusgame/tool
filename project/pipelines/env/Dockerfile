# cuda 10.0 (and not 9.x or 10.1) is necessary for tf 1.13.1
FROM nvidia/cuda:10.0-cudnn7-devel-ubuntu18.04

WORKDIR /root

RUN mkdir /root/.m2/ /root/.pip/
COPY ./env/.ossutilconfig /root/.ossutilconfig
COPY ./env/sources.list /etc/apt/
COPY ./env/settings.xml /root/.m2/
COPY ./env/pip.conf /root/.pip/

# Base dependencies
# -----------------
RUN apt-get clean && apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ssh \
    rsync \
    libsnappy-dev \
    python3 \
    python-pip \
    python-setuptools \
    wget \
    vim \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install pip --upgrade
RUN pip --no-cache-dir install \
    numpy \
    click \
    pandas \
    requests \
    urllib3 \
    tensorflow==1.13.1

ADD ./env/entry_point.sh /root/entry_point.sh
RUN chmod +x /root/entry_point.sh
ADD ./env/exit_point.sh /root/exit_point.sh
RUN chmod +x /root/exit_point.sh

COPY ./ ./
