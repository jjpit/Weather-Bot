# twitter bot that tweets out weather updates
# By: JJpit
# Date: 9-14-18

# to handle JSON data
import requests

# datetime is to be used for converting the unix timestamp
import datetime
# twitter api
import tweepy
# keys for the twitter bot
from keys import *

def tweet_msg():

	latitude = 33.21441
	longitude = -96.64295
	# excluding some data from the dark sky api call
	# ?exclude --> excluding the data that comes after it
	exclude = "?exclude=minutely,hourly,daily,flags,alerts"

	# for the API call url
	# these are the cordinates for richardson tx --> 32.985335, -96.748936
	# these are the cordinates for mckinney tx --> 33.21441, -96.64295
	url_call = "https://api.darksky.net/forecast/" + darksky_key + "/"+str(latitude)+","+str(longitude)+""+str(exclude)+""
	# right now the call is getting the current weather

	# data collected from the url_call
	data = requests.get(url_call).json()

	# making sure the data is actually collected + just showing the data 
	#print(data)`
	# from here you can copy the data and parse through it via an online json parser

	# setting the variable for the current temp
	curr_temp = data['currently']['temperature']
	# within data goto currently
	# within currently goto tempature

	# setting the feels like temp
	feel_like_temp = data['currently']['apparentTemperature']
	# within data goto currently
	# within currently goto apparentTempature

	# setting the humidity
	curr_humidity = data['currently']['humidity']
	# withinh data goto currently
	# within currently goto humidity

	# converting the humidity to a percent
	curr_humidity = curr_humidity * 100

	# setting the curr conditions
	curr_conditions = data['currently']['summary']
	# within data goto currently
	# within currently gotp summary

	tweet_msg = "McKinney, TX\nCurrent Conditions\n-----------------\n"+str(curr_conditions)+ "\n""-----------------\n""Current temperature -- "+str(curr_temp)+"°F \nfeels like -- "+str(feel_like_temp)+"°F \nhumidity -- "+str(curr_humidity)+"%"
	#adding str(your_var_name) converts the data to a string

	# for twitter api account
	# bothe Ckey and Csec come from keys import
	# this is auth your twitter acc
	twitter_account = tweepy.OAuthHandler(consumer_key,consumer_secret)

	# both A_toke and A_toke_Sec come froms keys import
	twitter_account.set_access_token(access_token,access_token_secret)

	# creating the actual bot that will tweet
	bot = tweepy.API(twitter_account)

	#bot.update_status("Hello Twitter!! \nThis is my first tweet")
	bot.update_status(tweet_msg)
	print("The tweet has been sent")

def update_msg():
	# for twitter api account
	# bothe Ckey and Csec come from keys import
	# this is auth your twitter acc
	twitter_account = tweepy.OAuthHandler(consumer_key,consumer_secret)

	# both A_toke and A_toke_Sec come froms keys import
	twitter_account.set_access_token(access_token,access_token_secret)

	# creating the actual bot that will tweet
	bot = tweepy.API(twitter_account)

	update_msg = "I will be going offline for a bit"
	bot.update_status(update_msg)
