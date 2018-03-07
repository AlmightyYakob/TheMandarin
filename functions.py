def printTweets(statuses, fileName=None):
    if (fileName==None):
        for i in statuses:
            print(i.text)
    else:
        file1 = open(fileName, "a")

        for i in statuses:
            #print(i.text, file1)
            file1.write(i.text.encode("utf-8"))


