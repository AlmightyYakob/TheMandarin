#! /usr/bin/env python

from functions import *
from Main import getAPI
import math
import time, sys
#import twitter
import urllib3


urllib3.disable_warnings()

SCREEN_NAME = "SamLuyk"
USER_ID = 767730307
OUTPUT_FILE = "output.txt"

api = getAPI()

statuses = getTweetsFromUser(api, USER_ID, 20, 0, 200)
printTweets(statuses, True, OUTPUT_FILE)
print(len(statuses))

exit()

