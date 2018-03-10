from functions import *
#import compileTweets
import time, sys
import glob
import os
import subprocess

SECONDS_TO_SLEEP = 60

while(True):
    #compileTweets

    list_of_files = glob.glob('/home/jake/twitterBot/torch-rnn/cv/*.t7')
    latest_file = max(list_of_files, key=os.path.getctime)
    print latest_file

    commandString = "./train.sh " + latest_file
    subprocess.call(commandString, shell=True)

    print("Sleeping for " + str(SECONDS_TO_SLEEP) + " seconds.")
    time.sleep(SECONDS_TO_SLEEP)
