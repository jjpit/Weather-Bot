# twitter bot that tweets out weather updates
# By: JJpit
# Date: 9-14-18
from bot import * #importing everything from bot.py (funcs)
from time import sleep

while True:
	tweet_msg() #calling the tweet_msg func from bot.py
	sleep(3600) #60 sec delay
