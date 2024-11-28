import telebot as t
import logging
import os
import sys
from dotenv import load_dotenv


from handlers import register_handlers
from subscriber import subscribe_to_channel

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
t.logger.setLevel(logging.INFO)


def init_bot():
    global bot
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN not found in environment variables")

    bot = t.TeleBot(token=token, parse_mode='HTML')
    if not bot:
        raise ValueError("BOT not initialized")
    return bot


def main():
    global channel
    bot = init_bot()
    channel = os.getenv("CHANNEL")
    if channel:
        pass
    else:
        logging.warning("CHANNEL environment variable is not set. Subscriptions won't work.")
        sys.exit()
    register_handlers(bot)
    bot.infinity_polling()


if __name__ == "__main__":
    main()
