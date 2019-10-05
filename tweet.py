import click

from time import sleep
from api import getAPI
from constants import TWEET_INTERVAL_SECONDS as INTERVAL


@click.command()
@click.option("-c", "--count", help="Limit the program to this many tweets.")
@click.option(
    "-m",
    "--model",
    "model_path",
    required=True,
    help="The saved model to use for sourcing text.",
)
def main(count, model_path):
    """Repeatedly tweets text generated from the trained model."""
    from keras.models import load_model

    model = load_model(model_path)
    api = getAPI()

    i = 0
    while count is None or i > 0:
        # TODO Replace with call from model
        status = ""

        try:
            api.PostUpdate(status)
            i -= 1

            print("Tweet Posted!")
            print("Sleeping for " + str(INTERVAL) + " seconds.")
            sleep(INTERVAL)

        except Exception as e:
            print(e)
            print("Posting Tweet failed! Continuing...")
            sleep(1)


if __name__ == "__main__":
    main()
