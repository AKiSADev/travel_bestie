def handle_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Telegram Bot!")

def handle_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="You said: " + update.message.text)

__all__ = ['handle_start', 'handle_message']