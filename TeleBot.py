from utils import *
from Reddit import *
import telegram.ext
from uuid import uuid4
import pickle
from threading import Event
key = []
DailyManga = []
LastCommand = "None"
chatID = ""
greetings = "Welcome to the manga bot! \n Type /help to get the list of possible commands. \n " \
            "Type /create_list to make your first list. "


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=greetings)
    global chatID
    chatID = update.message.chat_id
    global key
    key = str(uuid4())
    if context.user_data.get(key) is None:
        context.user_data[key] = []

def manga(update, context):
    MangaList = context.user_data[key]

    if(LastCommand == "new_chapter"):
        message = (get_message(update.message.text))
        if(message != ""):
            context.bot.send_message(chat_id=update.message.chat_id, text=message)
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="Sorry no manga with this name found")
            
    elif(LastCommand == "create_list" or LastCommand == "add_to_list"):
        title = update.message.text
        MangaList.append(title)
        context.user_data[key] = MangaList
        if(title != ""):
            context.bot.send_message(chat_id=update.message.chat_id, text=title + " was successfullly added")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="Could not add entry")


    elif (LastCommand == "remove_from_list"):
        size = len(MangaList)
        for entry in MangaList:
            if update.message.text in entry:
                MangaList.remove(entry)
                context.user_data[key] = MangaList
                context.bot.send_message(chat_id=update.message.chat_id, text="Entry: " + entry + " was removed")
        if size == len(MangaList):
            context.bot.send_message(chat_id=update.message.chat_id, text="This entry is not found in your manga list")

    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Sorry I did not understand that command.")

def new_chapter(update, context):
    global LastCommand
    LastCommand = "new_chapter"
    if(len(context.args) == 0):
        context.bot.send_message(chat_id=update.message.chat_id, text="Please send me the manga name")
    else:
        message = ""
        for argument in context.args:
            message += argument + " "
        update.message.text = message
        manga(update, context)


def create_list(update, context):
    global LastCommand
    LastCommand = "create_list"
    if(len(context.args) == 0):
        MangaList = context.user_data[key]
        if (MangaList == []):
            context.bot.send_message(chat_id=update.message.chat_id, text="Please send me the manga name to add to list \n"
                                                                      "Be precise in your naming to avoid manga with similar name")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text="List already exists")
    else:
        message = ""
        for argument in context.args:
            message += argument + " "
        update.message.text = message
        manga(update, context)

def add_to_list(update, context):
    global LastCommand
    LastCommand = "add_to_list"
    if (len(context.args) == 0):
        context.bot.send_message(chat_id=update.message.chat_id, text="Please send me the manga name to add to list")
    else:
        message = ""
        for argument in context.args:
            message += argument + " "
        update.message.text = message
        manga(update, context)

def print_list(update, context):
    global LastCommand
    LastCommand = "print_list"
    context.bot.send_message(chat_id=update.message.chat_id, text="Here is the list of manga that I currently keep track of:")
    MangaList = context.user_data[key]
    for entry in MangaList:
        context.bot.send_message(chat_id=update.message.chat_id, text=entry)

def remove_from_list(update, context):
    global LastCommand
    LastCommand = "remove_from_list"
    if (len(context.args) == 0):
        context.bot.send_message(chat_id=update.message.chat_id, text="Please send me the name of the manga to remove")
    else:
        message = ""
        for argument in context.args:
            message += argument + " "
        update.message.text = message
        manga(update, context)

def clean_list(update, context):
    global LastCommand,MangaList
    context.user_data[key] = []
    LastCommand = "clean_list"
    context.bot.send_message(chat_id=update.message.chat_id, text="List was successfully cleaned")

def get_updates(update, context):
    global LastCommand
    LastCommand = "get_updates"
    MangaList = context.user_data[key]
    context.bot.send_message(chat_id=update.message.chat_id, text="These are the new chapters of your list:")
    for entry in MangaList:
        text = get_message(entry)
        context.bot.send_message(chat_id=update.message.chat_id, text=text)

def clear_chapters(bot, job):
    global DailyManga
    DailyManga = []

def send_update(bot, job):
    context.bot.send_message(chat_id=update.message.chat_id, text="You're loh")



def help(update, context):
    global LastCommand
    LastCommand = "help"
    context.bot.send_message(chat_id=update.message.chat_id, text="Here is the current list of commands: \n"
                                                              "/new_chapter sends you the last chapter of the manga that you"
                                                              " search \n"
                                                              "/create_list creates list of manga and notifies you whenever new"
                                                              " chapter will be posted on r/manga \n"
                                                              "/add_to_list adds new manga to your list \n"
                                                              "/remove_from_list removes selected manga from list \n"
                                                              "/clean_list removes all entries from the list \n"
                                                              "/get_updates sends you latest chapters of manga in your list")

