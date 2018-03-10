#! /usr/bin/env python

from functions import *
from Main import getAPI
import math
import time, sys
#import twitter
import urllib3


urllib3.disable_warnings()

#SCREEN_NAME = "SamLuyk"
#SCREEN_NAME = "_The_Mandarin_"
#USER_ID = 767730307
#USER_ID = 837807691414274051



def compileTweets(api=getAPI(), outputFile=None):
    if (outputFile==None):
        OUTPUT_FILE = "RETRIEVED_TWEETS.txt"
    else:
        OUTPUT_FILE = outputFile


    statuses = getTweetsFromTimeline(api, 800)

    printTweets(statuses, True, OUTPUT_FILE)
    print(len(statuses))

    return OUTPUT_FILE


compileTweets()
