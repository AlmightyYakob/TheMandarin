from functions import *
from Main import *
import math
import time, sys
#import twitter
import urllib3
import re


def cleanString(string):
    string = re.sub(r'http\S+', '', string)
    string = re.sub(r'@\S+', '', string)
    string = re.sub(r'RT ', '', string)
    return string

    #return re.sub(r'^https?:\/\/.*[\r\n]*', '', string)

def printTweets(statuses, includeDatesToConsole=False, fileName=None):
    if (fileName==None):
        for i in statuses:
            print(i.text)
    else:
        file1 = open(fileName, "a")

        for i in range (0, len(statuses)):
            status = statuses[i]
            if ((i > 0) and (status == statuses[i-1])):
                continue

            stringToWrite = status.text
            stringToWrite = cleanString(stringToWrite)
            stringToWrite += '\n'
            stringToWrite = (stringToWrite.encode("utf-8"))

            file1.write(stringToWrite)

            if (includeDatesToConsole):
                print(status.created_at)

        file1.close()


def getTweetsFromTimeline(api, numOfTweets=1, startingID=None):
    statuses = []
    oldestTweet = startingID

    numOfTweets = min(800, numOfTweets)        #limits number of tweets retrieved to 800

    while (numOfTweets > 0):
        getCount = min(numOfTweets, 200)
        numOfTweets -= getCount

        new_statuses = api.GetHomeTimeline(count=getCount, max_id=oldestTweet)

        for i in range( (len(new_statuses)-1), -1, -1):
            if (new_statuses[i].id == TWITTER_ID):
                print("DELETED SELF TWEET")
                del new_statuses[i]

        statuses.extend(new_statuses)
        oldestTweet = (statuses[len(statuses)-1]).id

    return statuses

def getTweetsFromUser(api, userID, numOfCalls=1, startingID=None, countPerCall=200):
    statuses = []
    oldestTweet = startingID
    countPerCall = min(200, countPerCall)

    for i in range(0, numOfCalls):
        statuses.extend(api.GetUserTimeline(user_id=userID, max_id=oldestTweet, count=countPerCall))
        oldestTweet = (statuses[len(statuses)-1]).id


    return statuses


def compileTweets(api=getAPI(), outputFile="RETRIEVED_TWEETS.txt", num=800):
    statuses = getTweetsFromTimeline(api, num)

    printTweets(statuses, True, outputFile)
    print(len(statuses))

    return outputFile


