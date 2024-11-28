import redis
import json

r = redis.Redis(
  host="127.0.0.1",
  password="",
  port=6379,
  db=0,
  ssl=False,
)

data = {
  "uuid": "test_userid",
  "type": 0,
  "message": "c 'Не назначен' на 'Высокий'",
  "created_at": "2024-11-28T01:34:31.977Z",
  "author": {
    "id": 1,
    "fullName": "Малыгин А.Е."
  },
  "ticket": {
    "id": 1,
    "priority": 2,
    "title": "Не работает принтер",
    "created_at": "2024-11-28T01:34:08.976Z",
    "status": 3,
    "issuedUser": {
      "id": 1,
      "fullName": "Малыгин А.Е.",
      "email": "test@yandex.ru"
    },
    "assignedUser": {
      "id": 3,
      "fullName": "Ермак М.А.",
      "email": "test3@yandex.ru"
    },
    "type": {
      "id": 2,
      "name": "Инциденты / Аварии"
    }
  }
}
message = json.dumps(data)
print(message)

r.publish('channel_1', message)
