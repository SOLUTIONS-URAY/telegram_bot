def register_notisender_handler(bot, user_id, type, message, id):
    if type == 'CHANGE_PRIORITY':
        bot.send_message(user_id, f'🔔У вашей задачи под номером {id} сменился приоритет {message}')
    elif type == 'CHANGE_TITLE':
        bot.send_message(user_id, f'🔔У вашей задачи под номером {id} сменился заголовок {message}')
    elif type == 'CHANGE_ISSUED_USER':
        bot.send_message(user_id, f'🔔У вашей задачи под номером {id} сменился выданный пользователь: {message}')
    elif type == 'CHANGE_ASSIGNED_USER':
        bot.send_message(user_id, f'🔔У вашей задачи под номером {id} сменился назначенный пользователь: {message}')
    elif type == 'CHANGE_STATUS':
        bot.send_message(user_id, f'🔔У вашей задачи под номером {id} изменился статус: {message}')
    elif type == 'ADD_COMMENTARY':
        bot.send_message(user_id, f'🔔К вашей задаче под номером {id} добавлен комментарий: {message}')
    else:
        bot.send_message(user_id, f'🔔Уведомление не было доставлено {message}')
    #ТИПЫ УВЕДОМЛЕННИЙ
    #
    #CHANGE_PRIORITY,
    #CHANGE_TITLE,
    #CHANGE_ISSUED_USER,
    #CHANGE_ASSIGNED_USER,
    #CHANGE_STATUS,
    #ADD_COMMENTARY