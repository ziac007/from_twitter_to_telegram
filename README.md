## Twitter > Telegram
### Auto post tweets from Twitter, to a Telegram bot

This bot simply takes a twitter user name, and fetches the latest tweets
from their timeline. Then reposts those tweets to a telegram bot(or channel via a bot)

####Requirements:
You need Twython installed. Twython is a twitter-python API

####Notes:
The script makes a txt file that holds the tweet ID of the latest tweet it 
recieved. That way, we can compare the tweet ID, and make sure that we
only get the new tweets, since we last ran the script.

You can schedual the script to run with something like using cron jobs, 
every 10 min for example. I run mine at every 5 min for my current bot.

#####If you have Lots of Tweets Already!
You may want to adjust the count of the get_timeline request.
Other wise, it may continually post up to the last 200 messages!
