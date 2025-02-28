FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean 

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 80

COPY . /app