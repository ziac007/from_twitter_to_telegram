import os
import time
import pickle

from twython import Twython
from telegram import Bot

from SETTINGS import *


api = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
bot = Bot(telegram_token)


def first_run():
    file_exists = os.path.exists('sav.p')
    if not file_exists:
        user_timeline = api.get_user_timeline(screen_name=user_name, count=2)
        tweet_id = user_timeline[-1]['id']
        file_pickle(tweet_id)


def get_timeline(latest_tweet_id):
    return api.get_user_timeline(screen_name=user_name, since_id=latest_tweet_id)


def read_latest_id():
    line = file_unpickle()
    if len(str(line)) < 2:
        return 0
    else:
        return line


def send_message(msg):
    bot.send_message(chat_id=channel_name, text=msg)


def file_pickle(var):
    pickle.dump(var, open("sav.p", "wb"))


def file_unpickle():
    saved = pickle.load(open('sav.p', "rb"))
    return saved


def main():
    latest_tweet_id = read_latest_id()
    user_timeline = get_timeline(latest_tweet_id)

    for tweet in reversed(user_timeline):
        if tweet['text']:
            print(tweet['text'])
            send_message(tweet['text'])
            time.sleep(4)

        latest_tweet_id = tweet['id']

    file_pickle(latest_tweet_id)

first_run()
main()
