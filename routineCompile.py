from functions import *
from Main import *
from compileTweets import *
import time, sys
import glob
import os
import subprocess
import datetime

SECONDS_TO_SLEEP = 900
DATA_FILE_NAME = "RETRIEVED_TWEETS.txt"

while(True):
    compileTweets()

    commandString = "./preProcess.sh " + DATA_FILE_NAME
    subprocess.call(commandString, shell=True)



    print("---- Completed at " + str(datetime.datetime.now()))
    time.sleep(SECONDS_TO_SLEEP)

