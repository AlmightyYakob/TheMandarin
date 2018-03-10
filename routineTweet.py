from functions import *
from Main import *
import time, sys
import glob
import os
import subprocess

SECONDS_TO_SLEEP = 60

SAMPLE_FILE_NAME = "/home/jake/twitterBot/SAMPLE.txt"

while(True):
    list_of_files = glob.glob('/home/jake/twitterBot/torch-rnn/cv/*.t7')
    latest_file = max(list_of_files, key=os.path.getctime)
    print latest_file

    commandString = "./sample.sh " + latest_file + " > " + SAMPLE_FILE_NAME
    subprocess.call(commandString, shell=True)

    fr = open(SAMPLE_FILE_NAME, "r")

    status = unicode(fr.read(), 'utf-8')

    try:
        api.PostUpdate(status)
        print("Tweet Posted!")
        print("Sleeping for " + str(SECONDS_TO_SLEEP) + " seconds.")
        time.sleep(SECONDS_TO_SLEEP)
    except:
        print("Posting Tweet failed! Continuing...")

    fr.close()

