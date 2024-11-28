NOTIFICATION_TEMPLATES = [
    'CHANGE_PRIORITY',
    'CHANGE_TITLE',
    'CHANGE_ISSUED_USER',
    'CHANGE_ASSIGNED_USER',
    'CHANGE_STATUS',
    'ADD_COMMENTARY'
]

def add_notification_type(type_name):
    if type_name in NOTIFICATION_TEMPLATES:
        return f"Тип уведомления '{type_name}' уже существует."
    NOTIFICATION_TEMPLATES.append(type_name)
    return f"Тип уведомления '{type_name}' успешно добавлен."

def remove_notification_type(type_name):
    if type_name not in NOTIFICATION_TEMPLATES:
        return f"Тип уведомления '{type_name}' не найден."
    NOTIFICATION_TEMPLATES.remove(type_name)
    return f"Тип уведомления '{type_name}' успешно удален."

def list_notification_types():
    return list(NOTIFICATION_TEMPLATES)