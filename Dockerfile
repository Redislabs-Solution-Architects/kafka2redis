FROM python:3.11
RUN mkdir /app
WORKDIR /app
COPY requirements.txt README.md ./
COPY app ./app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip install -r requirements.txt
RUN python make_index.py
CMD ["flask", "run", "-p", "5050", "--host=0.0.0.0"]
