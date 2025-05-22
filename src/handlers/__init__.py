from telegram import Update
from telegram.ext import ContextTypes

async def handle_message(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="You said: " + update.message.text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


__all__ = ['handle_start', 'handle_message', 'start']