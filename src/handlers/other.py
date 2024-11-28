def other_messages(bot):
    @bot.message_handler(func=lambda message: True)
    def error_command(message):
        bot.send_message(message.from_user.id,
                         "⁉️Ошибка! Такой команды не существует.\n\n" +
                         "/help - список всех команд.\n" + 
                         "/start &lt;ссылка&gt; - старт бота с <a href='https://solutions-team.ru/'>реферальной ссылкой</a>"
                        )