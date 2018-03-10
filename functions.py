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

            stringToWrite = (status.text.encode("utf-8"))
            stringToWrite += '\n'

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

        statuses.extend(api.GetHomeTimeline(count=getCount, max_id=oldestTweet))
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
