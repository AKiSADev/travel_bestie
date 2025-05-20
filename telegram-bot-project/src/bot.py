from asyncio import Queue
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from handlers import handle_start, handle_message

def main():

    # Initialize the bot with your token
    updater = Updater("7401386745:AAFX9qPnXAj9clvE7-z3gxIjRdrXt4haz0s", Queue())

    # Get the dispatcher to register handlers
    updater.initialize()

    # Register command and message handlers

    # Start polling for updates
    updater.start_polling()


if __name__ == '__main__':
    main()