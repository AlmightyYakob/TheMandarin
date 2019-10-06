from twitter import Twitter, OAuth
from constants import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET


def getAPI():
    auth = OAuth(
        token=ACCESS_KEY,
        token_secret=ACCESS_SECRET,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
    )
    return Twitter(auth=auth)
