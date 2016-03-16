import os, time
import twython as Twython
from urllib import quote

## Twitter application authentication ##
# The following strings are placeholders, with dummy keys that will not work!
# Replace these keys, with your own. http://dev.twitter.com/docs/api/1.1/overview/. 
APP_KEY = '8pLF53UUKYhz2wIoFV88iqrNh'
APP_SECRET = 'qjpqTrmSFIO6Ex8iDwzkTUyKqJDLGoghPvjtnv8MsvmKgAHxp6'
OAUTH_TOKEN = '700949419424808960-f1DRk0qc0ZUUBxzJUamMBZpK9Pt0jcG'
OAUTH_TOKEN_SECRET = 'ohNqr7n8ha5ceoJ8PFk7my0VU8MDRr3K4slscmA1CWDjX'

api = Twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
latest_tweet_id = 0

## Your Telegram Channel Name ##
channel_name = 'RasPi2_Bot'
## Telegram Access Token ##
telegram_token = '183020244:AAEJvzg7VqRfGJAAjleX9ZdGiIKfm9QweFQ'
## Twitter User Name to get Timeline ##
user_name = 'RasPiBot_'

def get_timeline(latest_tweet_id):
    user_timeline = api.get_user_timeline(screen_name=user_name, since_id=latest_tweet_id)
    return user_timeline
def writeToLog(msg):
    log_file = open(channel_name+"_latest_id.txt", "w")
    log_file.write(str(msg))
    log_file.close()
def read_latest_id():
    file_exists = os.path.exists(channel_name+"_latest_id.txt")
    if file_exists is False:
        writeToLog('0')
    else:
        log_file = open(channel_name+"_latest_id.txt", "r")
        line = log_file.read()
        log_file.close()
        if len(str(line)) < 2:
            return 0
        else:
            return line
def send_message(msg):
    msg = quote(msg, safe='')
    link = 'https://api.telegram.org/bot'+telegram_token+'/sendMessage?chat_id=@'+channel_name+'\&text="' + msg + '"'
    os.system('curl '+ link)
    
def main():
    latest_tweet_id = read_latest_id()
    user_timeline = get_timeline(latest_tweet_id)
    number_of_tweets = len(user_timeline)
    if number_of_tweets > 0:
        for i in reversed(range(0,number_of_tweets)):
            if user_timeline[i]['text']:
                print user_timeline[i]['text']
                send_message(user_timeline[i]['text'])
                time.sleep(4)
        latest_tweet_id = user_timeline[0]['id']
    writeToLog(latest_tweet_id)
   
main()
