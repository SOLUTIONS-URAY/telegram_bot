from .start import register_start_handler
from .help import register_help_handler
from .notifications_changer import notification_change_buttons
from .other import other_messages

def register_handlers(bot):
    register_start_handler(bot)
    register_help_handler(bot)
    notification_change_buttons(bot)
    other_messages(bot)
    #register_other_handlers(bot)