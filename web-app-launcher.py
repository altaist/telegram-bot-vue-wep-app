#!/usr/bin/env python3
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""

Installation:

    pip install python-telegram-bot --upgrade


Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = '6631895320:AAE8noQdLXyWouOk6odHCp4hrnRKBlk2Y6U'
URL = 'https://altaist.github.io/telegram-bot-vue-wep-app/'
# This have to be configured with botfather
BOT_FATHER_URL = 'https://t.me/altaist_webapp_bot/myapp'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [InlineKeyboardButton("Launch Web App (WebAppInfo) only private chats", web_app=WebAppInfo(url=URL))],
        [InlineKeyboardButton("Launch Web App (Botfather link)", url=BOT_FATHER_URL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Press to launch the Web App [webapp](' + BOT_FATHER_URL + ')', parse_mode='MarkdownV2', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

