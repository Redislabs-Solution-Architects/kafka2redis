import os

import redis
from dotenv import load_dotenv

load_dotenv()

redis_conn = redis.StrictRedis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=os.getenv("REDIS_PORT", 6379),
    password=os.getenv("REDIS_PASS", ""),
    ssl=os.getenv("REDIS_TLS", False),
    ssl_cert_reqs=None,
    encoding="utf-8",
    decode_responses=True
)
