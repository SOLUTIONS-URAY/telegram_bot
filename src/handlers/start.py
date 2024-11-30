import logging
import json
from telebot import TeleBot
import token_check
import noti_type
import noti_sender


referrals = {}

NOTIFICATION_TEMPLATE_TO_NUMBER = {
    0 : 'CHANGE_PRIORITY',
    1 : 'CHANGE_TITLE',
    2 :'CHANGE_ISSUED_USER',
    3 :'CHANGE_ASSIGNED_USER',
    4 :'CHANGE_STATUS',
    5 :'ADD_COMMENTARY'
}

def register_start_handler(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        try:
            # Получение реферального кода
            referral_code = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
            user_id = message.from_user.id
            try:
                if referral_code:
                    global user_api
                    referrals[user_id] = referral_code
                    user_api = token_check.check(referral_code, message.from_user.id, message.from_user.username)
                    print("Debug 6", user_api)


                    if user_api:
                        #notifications_changer.notifinotification_change_buttons(bot)
                        bot.send_message(user_id, f"✅Приветствуем {user_api}, вы авторизовались в боте!")
                        #bot.send_message(user_id, f"Твой user_api: {user_api}")
                        logging.info(f"User {user_id} was referred by {referral_code}")
                        
                       
                    else:
                        bot.send_message(user_id, "❌Ошибка приглашения, попробуй ещё раз.")
                else:
                    bot.send_message(user_id, "❌Ты запустил бота без <a href='https://solutions-team.ru/'>реферального кода</a>")
            except Exception as e:
               logging.error(f"Ошибка 2 в обработчике /start: {e}")
               bot.reply_to(message, "Произошла ошибка. Попробуй ещё раз.")
        except IndexError:
            bot.reply_to(message, "❌Некорректная команда. Используй /start (авторизационный код).")
        except Exception as e:
            logging.error(f"Ошибка в обработчике /start: {e}")
            bot.reply_to(message, "Произошла ошибка. Попробуй ещё раз.")
