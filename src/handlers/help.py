from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from . import start
import logging

def register_help_handler(bot):
    @bot.message_handler(commands=['help'])
    def handle_help(message):
        try:
            user_id = message.from_user.id
            
            if hasattr(start, 'user_api') and start.user_api:
                keyboard = InlineKeyboardMarkup()
                #keyboard.add(
              #      InlineKeyboardButton(
               #         text="📣Настройка Уведомлений",
                #        callback_data="Notifications_menu"
               #     )
                #)
                bot.send_message(user_id, "⚙️Вот список доступных команд.\n")
                bot.send_message(user_id, "/notifications on || off - включить или выключить уведомления")
            else:
                bot.send_message(user_id, "⚙️Вот список доступных команд.\n")
                bot.send_message(
                    user_id,
                    "/start  &lt;ссылка&gt; - старт бота с <a href='https://solutions-team.ru/'>реферальной ссылкой</a>",
                    parse_mode="HTML"
                )
        except Exception as e:
            logging.error(f"Ошибка в обработчике /help: {e}")
            bot.reply_to(message, "Произошла ошибка. Попробуй ещё раз.")
   # @bot.callback_query_handler(func=lambda call: True)
   # def handle_message(callback):
     #   if callback.data == "Notifications_menu":
  #          try:
            #    notifications_changer.send_welcom(callback.from_user.id)
          #  except Exception as e:
           #     logging.error(f"Ошибка в обработчике Notifications_menu: {e}")
          #      bot.send_message(callback.from_user.id, "Произошла ошибка при открытии меню уведомлений.")
