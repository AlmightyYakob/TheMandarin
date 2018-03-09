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

OUTPUT_FILE = "output.txt"

api = getAPI()

statuses = getTweetsFromTimeline(api, 2)

printTweets(statuses, True, OUTPUT_FILE)
print(len(statuses))

exit()

