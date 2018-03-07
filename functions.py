def printTweets(statuses, fileName=None):
    if (fileName==None):
        for i in statuses:
            print(i.text)
    else:
        file1 = open(fileName, "a")

        for i in statuses:
            #print(i.text, file1)
            file1.write(i.text.encode("utf-8"))



def getTweetsFromUser(api, userID, numOfCalls, startingID, countPerCall=200):
    statuses = []
    oldestTweet = startingID
    countPerCall = min(200, countPerCall)

    for i in range(0, numOfCalls):
        statuses.extend(api.GetUserTimeline(user_id=userID, max_id=oldestTweet, count=countPerCall))
        oldestTweet = (statuses[len(statuses)-1]).id


    return statuses
