import os
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, PicklePersistence
from TeleBot import *
import logging
from utils import *
from flask import Flask, request
import pickle

mytoken = os.environ['mytoken']

#try:
#   from dev_settings import *
#except ImportError:
#   pass

bot = telegram.Bot(token=mytoken)
server = Flask(__name__)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

PORT = int(os.environ.get('PORT', '8443'))



if __name__ == "__main__":
    my_persistence = PicklePersistence(filename='my_file')
    updater = Updater(token=mytoken,persistence=my_persistence, use_context=True)
    manga_check = updater.job_queue
    clear_hourly = manga_check.run_repeating(clear_chapters, interval=3600, first=0)
#    send_new = manga_check.run_repeating(send_chapters, interval=600, first=0)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    new_chapter_handler = CommandHandler('new_chapter', new_chapter, pass_args=True)
    print_list_handler = CommandHandler('print_list', print_list)
    remove_from_list_handler = CommandHandler('remove_from_list', remove_from_list, pass_args=True)
    get_updates_handler = CommandHandler('get_updates', get_updates)
    create_handler = CommandHandler('create_list', create_list, pass_args=True)
    add_to_list_handler = CommandHandler('add_to_list', add_to_list, pass_args=True)
    clean_handler = CommandHandler('clean_list', clean_list)
    help_handler = CommandHandler('help', help)
    manga_handler = MessageHandler(Filters.text, manga)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(new_chapter_handler)
    dispatcher.add_handler(print_list_handler)
    dispatcher.add_handler(remove_from_list_handler)
    dispatcher.add_handler(get_updates_handler)
    dispatcher.add_handler(create_handler)
    dispatcher.add_handler(manga_handler)
    dispatcher.add_handler(clean_handler)
    dispatcher.add_handler(add_to_list_handler)
    dispatcher.add_handler(help_handler)
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=mytoken)
    updater.bot.set_webhook("https://fathomless-fortress-45000.herokuapp.com/" + mytoken)
    updater.idle()