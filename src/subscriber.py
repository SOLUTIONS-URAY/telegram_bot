import redis
import time
import os
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host="127.0.0.1",
    password="",
    port=6379,
    db=0,
    ssl=False,
)


def subscribe_to_channel():
    p = r.pubsub()
    p.subscribe(os.getenv("CHANNEL"))
    return p


def read_message(p):
    while True:
        message = p.get_message()
        if message and message.get("type") == "message":
            return message["data"].decode('utf-8')
        time.sleep(0.01)
