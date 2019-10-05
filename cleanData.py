from functions import cleanString
from constants import RETRIEVED_TWEETS_FILE, FIXED_TWEETS_FILE

fr = open(RETRIEVED_TWEETS_FILE, "r")
fw = open(FIXED_TWEETS_FILE, "w")

status = str(fr.read())

for line in fr:
    line = cleanString(line)
    if line[0] == " ":
        line = line[1:]
    line = str(line, "utf-8")
    fw.write(line.encode("utf-8"))

fr.close()
fw.close()

status = cleanString(status)
print(status)

fr.write(status.encode("utf-8"))
fr.close()
