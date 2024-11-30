import psycopg2
import os
import logging
import redis
import json
import db
from handlers import start
from dotenv import load_dotenv

load_dotenv()

NOTIFICATION_TYPES = [
    'CHANGE_PRIORITY',
    'CHANGE_TITLE',
    'CHANGE_ISSUED_USER',
    'CHANGE_ASSIGNED_USER',
    'CHANGE_STATUS',
    'ADD_COMMENTARY'
]

BASE_DOMAIN = os.getenv("BASE_DOMAIN")


def send_push(bot, user_id, type, message, id, title):
    msg = f'🔔 У задачи <a href="{BASE_DOMAIN}/tickets/{id}">#{id} : "{title}"</a> '

    if type == 'CHANGE_PRIORITY':
        msg += f'сменился приоритет {message}'
    elif type == 'CHANGE_TITLE':
        msg += f'сменился заголовок {message}'
    elif type == 'CHANGE_ISSUED_USER':
        msg += f'сменился автор: {message}'
    elif type == 'CHANGE_ASSIGNED_USER':
        msg += f'сменился назначенный специалист: {message}'
    elif type == 'CHANGE_STATUS':
        msg += f'изменился статус: {message}'
    elif type == 'ADD_COMMENTARY':
        msg += f'новый комментарий: {message}'
    else:
        msg += f'новая информация. Спешите посмотреть'

    print(user_id, msg)
    bot.send_message(user_id, msg)

def read_message(p):
    while True:
        message = p.get_message()
        if message and message.get("type") == "message":
            return message["data"].decode('utf-8')


def getRecipientId(event):
    ticket = event["ticket"]
    userIds = []
    userIds.append(ticket["assignedUser"]["id"])
    userIds.append(ticket["issuedUser"]["id"])
    userIds.remove(event["author"]["id"])
    return userIds


def subscribe(bot, channel):
    logging.info("Загрузка Redis")

    r = redis.Redis(
        host=os.getenv("REDHOST"),
        password=os.getenv("REDPASS"),
        port=os.getenv("REDPORT"),
        db=0,
        ssl=False,
    )
    p = r.pubsub()
    p.subscribe(channel)

    logging.info("Успешная загрузка Redis")


    while True:
        event = json.loads(read_message(p))
        logging.info("Получено сообщение")
        logging.info(event["uuid"])

        userIds = getRecipientId(event)
        
        usersToSend = db.query('SELECT * FROM "telegram_match" WHERE "userId" = %s;', tuple(userIds))
        print(usersToSend)
        
        telegramIds = [user[1] for user in usersToSend]

        print(telegramIds)

        for tgId in telegramIds:
            try:
                send_push(bot, tgId, NOTIFICATION_TYPES[event["type"]], event["message"], event["ticket"]["id"], event["ticket"]["title"]) 
            except Exception as e:
                print(e)