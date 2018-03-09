from functions import *
import time, sys
import glob
import os
import subprocess

while(True):
    list_of_files = glob.glob('/home/jake/twitterBot/torch-rnn/cv/*.t7')
    latest_file = max(list_of_files, key=os.path.getctime)
    print latest_file

    commandString = "./sample.sh " + latest_file
    subprocess.call(commandString, shell=True)
