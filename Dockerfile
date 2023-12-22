FROM python:3.11
RUN mkdir /app
WORKDIR /app
COPY requirements.txt README.md startup.sh ./
COPY app ./app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip install -r requirements.txt
CMD ["/bin/bash","-c","./startup.sh"]
