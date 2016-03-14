import os, time
import twython as Twython

## Twitter application authentication ##
# The following strings are placeholders, with dummy keys that will not work!
# Replace these keys, with your own. http://dev.twitter.com/docs/api/1.1/overview/. 
APP_KEY = 'f123abcjfdj9939123abcwe90u'
APP_SECRET = '123123AbCAbc4asoiDgF8HDF123lkjreogDHFNnweDHJHNBF'
OAUTH_TOKEN = '1231231111111191919-asdfj39ejfjasljDJLf0wFhhskFHgg9'
OAUTH_TOKEN_SECRET = 'oNsdfhNFJD123123njn2A94ufdsa4JFRehf9i43FHewhf'

api = Twython.Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
latest_tweet_id = 0

## Your Telegram Bot Name ##
bot_name = 'geremysays'
## Telegram Access Token ##
telegram_token = '111101011123:Asd63Sdfh8HS3YdgQksd843'
## Twitter User Name to get Timeline ##
user_name = 'GeremySays'

def get_timeline(latest_tweet_id):
    user_timeline = api.get_user_timeline(screen_name=user_name, since_id=latest_tweet_id)
    return user_timeline
def writeToLog(msg):
    log_file = open(bot_name+"_latest_id.txt", "w")
    log_file.write(str(msg))
    log_file.close()
def read_latest_id():
    file_exists = os.path.exists(bot_name+"_latest_id.txt")
    if file_exists is False:
        writeToLog('0')
    else:
        log_file = open(bot_name+"_latest_id.txt", "r")
        line = log_file.read()
        log_file.close()
        if len(str(line)) < 2:
            return 0
        else:
            return line
def send_message(msg):
    link = 'https://api.telegram.org/bot'+telegram_token+'/sendMessage?chat_id=@'+bot_name+'\&text="' + msg + '"'
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
