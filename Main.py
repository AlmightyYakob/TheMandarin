#! /usr/bin/env python

from functions import *
import math
import time, sys
import twitter
import urllib3


urllib3.disable_warnings()

CONSUMER_KEY = 'prjiNXa8WHL5IOS4HNdnqxQRL'
CONSUMER_SECRET = 'hHQ2OJeI26tpHhooihfBvwZ6jNXrlME3DCOKsoaFPKHnaHVhZt'
ACCESS_KEY = '837807691414274051-WMs9arq1V4SHo4mXWgG6YLaDhNbyyKM'
ACCESS_SECRET = 'Cm8aWMQSQVEtlzR8nEXYEBZl2vtS6O4mj0dXdz0yQNyzV'

SCREEN_NAME = "SamLuyk"
USER_ID = 767730307
OUTPUT_FILE = "output.txt"

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_KEY,
                  access_token_secret=ACCESS_SECRET)


statuses = getTweetsFromUser(api, USER_ID, 20, 0, 200)
printTweets(statuses, True, OUTPUT_FILE)
print(len(statuses))


exit()


if (len(sys.argv) > 1):
    argfile = str(sys.argv[1])
    filename=open(argfile,'r')
    f=filename.readlines()
    filename.close()

