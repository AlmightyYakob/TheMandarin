from Main import api
import time
import glob
import os
import subprocess

SECONDS_TO_SLEEP = 300

SAMPLE_FILE_NAME = "/home/jake/twitterBot/SAMPLE.txt"

while True:
    list_of_files = glob.glob("/home/jake/twitterBot/torch-rnn/cv/*.t7")
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file)

    commandString = "./sample.sh " + latest_file + " > " + SAMPLE_FILE_NAME
    subprocess.call(commandString, shell=True)

    fr = open(SAMPLE_FILE_NAME, "r")

    status = str(fr.read(), "utf-8")

    try:
        api.PostUpdate(status)
        print("Tweet Posted!")
        print("Sleeping for " + str(SECONDS_TO_SLEEP) + " seconds.")
        time.sleep(SECONDS_TO_SLEEP)
    except Exception as e:
        print(e)
        print("Posting Tweet failed! Continuing...")
    fr.close()
