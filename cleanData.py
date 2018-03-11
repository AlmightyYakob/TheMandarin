from functions import *
from Main import *
import time, sys
import glob
import os
import subprocess

FILE_NAME = "/home/jake/twitterBot/RETRIEVED_TWEETS.txt"
NEW_FILE_NAME = "/home/jake/twitterBot/FIXED_RETRIEVED_TWEETS.txt"

fr = open(FILE_NAME, "r")
fw = open(NEW_FILE_NAME, "w")

#status = unicode(fr.read(), "utf-8")


for line in fr:
    line = cleanString(line)
    line = unicode(line, "utf-8")
    fw.write(line.encode("utf-8"))

fr.close()
fw.close()

exit()

status = cleanString(status)
print(status)

fr.write(status.encode("utf-8"))
fr.close()

