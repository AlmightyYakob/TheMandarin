#! /usr/bin/env python

import math

import time, sys
import twitter
import urllib3
#from tweepy.models import Status
#from pip._vendor.requests.packages.urllib3.connectionpool import xrange


urllib3.disable_warnings()

CONSUMER_KEY = 'prjiNXa8WHL5IOS4HNdnqxQRL'
CONSUMER_SECRET = 'hHQ2OJeI26tpHhooihfBvwZ6jNXrlME3DCOKsoaFPKHnaHVhZt'
ACCESS_KEY = '837807691414274051-WMs9arq1V4SHo4mXWgG6YLaDhNbyyKM'
ACCESS_SECRET = 'Cm8aWMQSQVEtlzR8nEXYEBZl2vtS6O4mj0dXdz0yQNyzV'

#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_KEY,
                  access_token_secret=ACCESS_SECRET)




def printTweets(statuses):
    for i in statuses:
        print(i.text)

statuses = api.GetUserTimeline(screen_name="SamLuyk", count=200)
printTweets(statuses)

print("\n-----------------------\n")
oldest_tweet = (statuses[len(statuses)-1]).id

statuses = api.GetUserTimeline(screen_name="SamLuyk", max_id=oldest_tweet, count=200)
printTweets(statuses)

exit()



if (len(sys.argv) > 1):
    argfile = str(sys.argv[1])
    filename=open(argfile,'r')
    f=filename.readlines()
    filename.close()

