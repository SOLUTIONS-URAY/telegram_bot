def send(bot, user_id, type, message, id, title):
    if type == 'CHANGE_PRIORITY':
        bot.send_message(user_id, f'🔔У задачи #{id}:{title} сменился приоритет {message}')
    elif type == 'CHANGE_TITLE':
        bot.send_message(user_id, f'🔔У задачи #{id}:{title} сменился заголовок {message}')
    elif type == 'CHANGE_ISSUED_USER':
        bot.send_message(user_id, f'🔔У задачи #{id}:{title} сменился автор: {message}')
    elif type == 'CHANGE_ASSIGNED_USER':
        bot.send_message(user_id, f'🔔У задачи #{id}:{title} сменился назначенный специалист: {message}')
    elif type == 'CHANGE_STATUS':
        bot.send_message(user_id, f'🔔У задачи #{id}:{title} изменился статус: {message}')
    elif type == 'ADD_COMMENTARY':
        bot.send_message(user_id, f'🔔К задаче #{id}:{title} добавлен комментарий: {message}')
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