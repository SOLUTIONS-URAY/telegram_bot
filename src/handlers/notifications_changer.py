from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import logging
from noti_type import add_notification_type, remove_notification_type, list_notification_types
 
NOTIFICATION_TYPES = [
    'CHANGE_PRIORITY',
    'CHANGE_TITLE',
    'CHANGE_ISSUED_USER',
    'CHANGE_ASSIGNED_USER',
    'CHANGE_STATUS',
    'ADD_COMMENTARY'
]


def notification_change_buttons(bot):
    @bot.message_handler(commands=['notifications'])
    def send_welcom(message):
        on_off = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
        if on_off == 'on':
            bot.send_message(
                message.chat.id,
                "Уведомлению включены!",
            )
            for i in NOTIFICATION_TYPES:
                add_notification_type(i)
        elif on_off == 'off':
            bot.send_message(
                message.chat.id,
                "Уведомлению выключены!",
            )
            for i in NOTIFICATION_TYPES:
                remove_notification_type(i)
        else:
            bot.send_message(
                message.chat.id,
                "❌Неверный аргумент! Используй on или off",
            )
    '''
    def generate_notification_keyboard():
        keyboard = InlineKeyboardMarkup()
        for notification_type in NOTIFICATION_TYPES:
            keyboard.add(
                InlineKeyboardButton(
                    text=f"Включить {notification_type}",
                    callback_data=f"enable_{notification_type}"
                ),
                InlineKeyboardButton(
                    text=f"Выключить {notification_type}",
                    callback_data=f"disable_{notification_type}"
                )
            )
            print(f"disable_{notification_type}", f"enable_{notification_type}")
        return keyboard


    @bot.message_handler(commands=['change'])
    def send_welcom(message):
        bot.send_message(
            message.chat.id,
            "Привет! Используй кнопки ниже, чтобы включать или выключать уведомления.",
            reply_markup=generate_notification_keyboard()
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("enable_"))#, "disable_")))
    def handle_callback(call):
        user_id = call.from_user.id
        action, notification_type = call.data.split("_", 1)

        if action == "enable":
            add_notification_type(notification_type)
            bot.answer_callback_query(call.id, f"Уведомление '{notification_type}' включено!")
        elif action == "disable":
            remove_notification_type(notification_type)
            bot.answer_callback_query(call.id, f"Уведомление '{notification_type}' выключено!")
'''