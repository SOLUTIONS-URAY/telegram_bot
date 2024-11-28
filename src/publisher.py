import redis
import json

r = redis.Redis(
  host="127.0.0.1",
  password="",
  port=6379,
  db=0,
  ssl=False,
)

data = {'message_type' : "CHANGE_ASSIGNED_USER", 'message' : "1", 'user_api' : 'test_userid'}
message = json.dumps(data)
print(message)

r.publish('channel_1', message)
