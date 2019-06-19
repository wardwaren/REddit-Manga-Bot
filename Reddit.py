import praw
from utils import *
import os

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
user_agent = os.environ['user_agent']
username = os.environ['username']
password = os.environ['password']

try:
   from dev_settings import *
except ImportError:
   pass

reddit = praw.Reddit(client_id=client_id, \
                     client_secret=client_secret, \
                     user_agent=user_agent, \
                     username=username, \
                     password=password)

subreddit = reddit.subreddit('manga')

def get_message(name):
    message = ""
    for submission in subreddit.search(name,sort = "new",limit=100):
        if (("DISC" in submission.title) and (name.lower() in submission.title.lower())):
            message += submission.title
            message += ": "
            message += submission.url
            break
    return message

def get_title(name):
    message = ""
    foundlist = []
    for submission in subreddit.search(name, sort="new", limit=100):
        if ("DISC" in submission.title) and (name.lower() in submission.title.lower()):
            message += submission.title
            message = format_title(message)
            print(name.lower() + " " +  message.lower())
            if(name.lower() == message.lower()):
                foundlist = [name]
                break
            elif (message.lower() not in foundlist):
                foundlist.append(message.lower())
    return foundlist

def check_fresh(name):
    message = ""
    for submission in subreddit.new(limit=50):
        if (("DISC" in submission.title) and (name.lower() in submission.title.lower())):
            message += submission.title
            message += ": "
            message += submission.url
            break
    return message
