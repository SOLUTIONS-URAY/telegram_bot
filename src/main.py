import telebot as t
import logging
import os
import signal
import sys
import time
import redis_sub

from dotenv import load_dotenv
from handlers import register_handlers
from threading import Thread

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
t.logger.setLevel(logging.INFO)


def init_bot():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN not found in environment variables")

    bot = t.TeleBot(token=token, parse_mode='HTML', threaded=False)
    if not bot:
        raise ValueError("BOT not initialized")
    return bot


def start_bot(bot):
    register_handlers(bot)
    Thread(target=bot.polling, daemon=True).start()
    channel = os.getenv("CHANNEL")
    if channel:
        pass
    else:
        logging.warning("CHANNEL environment variable is not set. Subscriptions won't work.")
        sys.exit()
    redis_sub.subscribe(bot, channel)
    
    while True:
        time.sleep(1)
        # if stop_thread is True:
        #     bot.stop_polling()

def main():
    global bot_thread
    # global redis_thread

    bot = init_bot()

    bot_thread = Thread(target=start_bot, args=(bot,), daemon=True)
    # redis_thread = Thread(target=listen_redis, args=(bot,), daemon=True)

    bot_thread.start()
    # redis_thread.start()

    bot_thread.join()
    # redis_thread.join()

if __name__ == "__main__":
    main()
