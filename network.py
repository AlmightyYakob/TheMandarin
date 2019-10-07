from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, LSTM, CuDNNLSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from keras.backend.tensorflow_backend import _get_available_gpus

import numpy as np
import click

from constants import (
    INPUT_TEXT_SEQ_LENGTH as SEQ_LENGTH,
    DEFAULT_TRAINING_EPOCHS,
    DEFAULT_TRAINING_BATCH_SIZE,
)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def processInput(raw_text):
    chars = sorted(list(set(raw_text)))
    char_to_int = {c: i for i, c in enumerate(chars)}
    int_to_char = {i: c for i, c in enumerate(chars)}

    n_chars = len(raw_text)
    n_vocab = len(chars)

    dataX = []
    dataY = []
    for i in range(len(raw_text) - SEQ_LENGTH):
        seq_in = raw_text[i : i + SEQ_LENGTH]
        seq_out = raw_text[i + SEQ_LENGTH]
        dataX.append([char_to_int[char] for char in seq_in])
        dataY.append(char_to_int[seq_out])

    n_patterns = len(dataX)

    X = np.reshape(dataX, (n_patterns, SEQ_LENGTH, 1))
    # X = X / float(n_vocab)

    Y = np_utils.to_categorical(dataY)

    return ((X, Y), (dataX, dataY), chars, char_to_int, int_to_char, n_chars, n_vocab)


def create_model(X, Y):
    # Consider making input just single character
    model = Sequential()

    if _get_available_gpus():
        model.add(CuDNNLSTM(256, input_shape=(X.shape[1], X.shape[2])))
    else:
        model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))

    model.add(Dropout(0.2))
    model.add(Dense(Y.shape[1], activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model


@click.group()
def cli():
    """Functions to interface with ML Models"""
    pass


@cli.command("train")
@click.option(
    "-m", "--model", "model_path", help="The trained model to resume training on."
)
@click.option(
    "-i",
    "--input",
    "input_path",
    required=True,
    help="The path containing training data.",
)
def train_model(
    model_path=None,
    input_path=None,
    epochs=DEFAULT_TRAINING_EPOCHS,
    batch_size=DEFAULT_TRAINING_BATCH_SIZE,
    checkpoint=True,
):
    """Trains the model"""

    with open(input_path) as inputFile:
        raw_text = inputFile.read().lower()

    (X, Y), _, _, _, _, _, _ = processInput(raw_text)

    if model_path:
        model = load_model(model_path)
    else:
        model = create_model(X, Y)

    checkpoint = ModelCheckpoint(
        "model-{epoch:02d}-{loss:.4f}.hdf5",
        monitor="loss",
        save_best_only=True,
        mode="min",
    )

    model.fit(X, Y, epochs=epochs, batch_size=batch_size, callbacks=[checkpoint])


@cli.command("test")
@click.option(
    "-m",
    "--model",
    "model_path",
    required=True,
    help="The trained model to perform testing on.",
)
@click.option(
    "-i",
    "--input",
    "input_path",
    required=True,
    help="The path containing testing data.",
)
def test_model(model_path, input_path, LENGTH=500):
    """Tests the model"""

    with open(input_path) as inputFile:
        raw_text = inputFile.read().lower()

    _, (dataX, dataY), _, _, int_to_char, _, _s = processInput(raw_text)
    model = load_model(model_path)

    startIndex = np.random.randint(0, len(dataX) - 1)
    pattern = dataX[startIndex]
    output = "".join([int_to_char[v] for v in pattern])

    for i in range(LENGTH):
        print("Round", i)
        x = np.reshape(pattern, (1, len(pattern), 1))
        # x = x / float(n_vocab)

        pred_vector = model.predict(x)
        index = int(
            abs(0.5 - sigmoid(np.random.normal(scale=0.25))) * len(pred_vector[0])
        )
        index = len(pred_vector[0]) - index - 1

        # pred = np.argmax(pred_vector)
        pred = np.argsort(pred_vector[0])[index]

        output += int_to_char[pred]
        pattern.append(pred)
        pattern = pattern[1:]

    return output


if __name__ == "__main__":
    cli()
