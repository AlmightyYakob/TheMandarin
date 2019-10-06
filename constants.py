import os
from dotenv import load_dotenv

LOCAL_DOTENV_PATH = ".env.local"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


if os.path.exists(LOCAL_DOTENV_PATH):
    load_dotenv(LOCAL_DOTENV_PATH, override=True, verbose=True)


# Grab environment variables

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

TWITTER_ID = os.getenv("TWITTER_ID")

RETRIEVED_TWEETS_FILE = os.getenv("RETRIEVED_TWEETS_FILE")
FIXED_TWEETS_FILE = os.getenv("FIXED_TWEETS_FILE")

INPUT_TEXT_SEQ_LENGTH = int(os.getenv("INPUT_TEXT_SEQ_LENGTH"))

TWEET_INTERVAL_SECONDS = int(os.getenv("TWEET_INTERVAL_SECONDS"))

DEFAULT_TRAINING_EPOCHS = int(os.getenv("DEFAULT_TRAINING_EPOCHS"))
DEFAULT_TRAINING_BATCH_SIZE = int(os.getenv("DEFAULT_TRAINING_BATCH_SIZE"))
