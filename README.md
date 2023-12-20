# Transactions

This is a simple Python and Flask app to ingest data from Kafka and store in Redis. It supports searching the data. It uses Flask as the web server since it's so easy to get up and running.


## Prerequisites

- Python 3.11 or greater
- Redis

## Installing
This is how I recommend doing things, if you're on a Mac

```bash
python3 -m venv .venv
source ./.venv/bin/activate
```

```bash
pip install -r requirements.txt
```

## Running
```bash
flask run
```

## Docker
You may run this service plus the Redis database from docker. We've provided a docker-compose files for the service,
as well as for Redis. You must build the service image, then run docker-compose to bring it up.

By default, this app is listening on port 5000, Redis on 6379

```bash
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

## Testing
```bash
pytest
```

Note the tests rely on a running Redis. I'll update this someday to use https://testcontainers-python.readthedocs.io/en/latest/README.html.

For now, it's easiest to just run the docker redis-stack image, e.g.,
```bash
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```

## Code
The main "router" for the various endpoints is found in `app/__init.py__`. From there you should be able to trace the
rest of the code.

Controllers are in `app/controllers`
Utility functions are in `app/utility`

There's a file `app/make_index.py` to generate the Redis search index. This is where you define the "schema" for searching.

There's a file `app/ingest_data.py` to read JSON data from a file and write to Redis. The search index is updated automatically.

