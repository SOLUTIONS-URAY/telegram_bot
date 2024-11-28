import logging
import json
from telebot import TeleBot
import token_check
import subscriber
import noti_type
import noti_sender


referrals = {}

def register_start_handler(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        try:
            # Получение реферального кода
            referral_code = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
            user_id = message.from_user.id
            
            if referral_code:
                global user_api
                referrals[user_id] = referral_code
                user_api = token_check.main(referral_code)
                
                if user_api:
                    #notifications_changer.notifinotification_change_buttons(bot)
                    bot.send_message(user_id, f"✅Приветствуем {user_api}, вы авторизовались в боте!")
                    #bot.send_message(user_id, f"Твой user_api: {user_api}")
                    logging.info(f"User {user_id} was referred by {referral_code}")
                    
                    p = subscriber.subscribe_to_channel()
                    while True:
                        get_message = json.loads(subscriber.read_message(p))
                        if get_message.get('user_api') != user_api:
                            continue
                        
                        noti_list = noti_type.list_notification_types()
                        for i in noti_list:
                            if get_message.get('message_type') == i:
                                noti_sender.register_notisender_handler(
                                    bot, user_id, i, get_message.get('message')
                                )
                else:
                    bot.send_message(user_id, "❌Ошибка приглашения, попробуй ещё раз.")
            else:
                bot.send_message(user_id, "❌Ты запустил бота без <a href='https://solutions-team.ru/'>реферального кода</a>")
        except IndexError:
            bot.reply_to(message, "❌Некорректная команда. Используй /start <реферальный код>.")
        except Exception as e:
            logging.error(f"Ошибка в обработчике /start: {e}")
            bot.reply_to(message, "Произошла ошибка. Попробуй ещё раз.")
