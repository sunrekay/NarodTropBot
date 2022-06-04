   
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y firefox wget

RUN apt update \
	&& apt install -y python3 pip \
	&& cd /usr/bin \
	&& ln -s python3 python
COPY requirements.txt /mnt/data/requirements.txt

WORKDIR /mnt/data 
ADD bot.py /

RUN pip install -r requirements.txt
COPY . /mnt/data/




CMD ["python", "/bot.py"]