import twitter

CONSUMER_KEY = "Aa8aI1RI9Em3EVfL4OnDE1I3o"
CONSUMER_SECRET = "8GDcdttyTHDp2xFKEEkkP69pJYMVxuoJlpCSboStNzDHGnCSdx"
ACCESS_KEY = "837807691414274051-GQkziCILwMNFj0uIFOJJnkf8KnniY5a"
ACCESS_SECRET = "CVOCnATCsMqSbiB80RcjpqXExe8F0bUsmUqLMg1wOJ2yO"

TWITTER_ID = 837807691414274051

api = twitter.Api(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET,
)


def getAPI():
    return api
