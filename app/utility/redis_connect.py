import os
from dotenv import load_dotenv

import redis

load_dotenv()


def connect_to_redis(host):
    print(f"Connecting to {host}")
    try:
        r = redis.StrictRedis(
            host=host,
            port=os.getenv("REDIS_PORT", 6379),
            db=0,
            ssl=os.getenv("REDIS_TLS", False),
            ssl_cert_reqs=None,
            decode_responses=True,
            encoding="utf-8"
        )
        print(f"Redis connection: ${r.info()}")
        r.ping()  # Check if the connection is alive
        return r
    except redis.ConnectionError as e:
        print(f"Redis connection error {e}")
        return None
    except redis.TimeoutError as e:
        print(f"Redis timeout error {e}")
        return None
    except Exception as e:
        print(f"Redis timeout error {e}")
        return None
