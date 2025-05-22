import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from handlers import handle_message, start

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7401386745:AAFX9qPnXAj9clvE7-z3gxIjRdrXt4haz0s').build()
    
    start_handler = CommandHandler('start', start)
    test_response_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
    application.add_handler(start_handler)
    application.add_handler(test_response_handler)
    
    application.run_polling()