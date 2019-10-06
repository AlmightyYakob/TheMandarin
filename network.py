from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, LSTM, CuDNNLSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from keras.backend.tensorflow_backend import _get_available_gpus
import numpy as np

from constants import INPUT_TEXT_SEQ_LENGTH as SEQ_LENGTH


raw_text = open("shakespeare-julius-26.txt").read().lower()

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
# print("Total Patterns: ", n_patterns)

X = np.reshape(dataX, (n_patterns, SEQ_LENGTH, 1))
# X = X / float(n_vocab)

y = np_utils.to_categorical(dataY)

#####################################


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def get_model():
    # Consider making input just single character
    model = Sequential()

    if _get_available_gpus():
        model.add(CuDNNLSTM(256, input_shape=(X.shape[1], X.shape[2])))
    else:
        model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))

    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation="softmax"))
    model.compile(loss="categorical_crossentropy", optimizer="adam")
    return model


def main():
    model = get_model()

    # checkpoint
    filepath = "model-{epoch:02d}-{loss:.4f}.hdf5"
    checkpoint = ModelCheckpoint(
        filepath, monitor="loss", verbose=1, save_best_only=True, mode="min"
    )
    model.fit(X, y, epochs=50, batch_size=64, callbacks=[checkpoint])


def test(filepath, LENGTH=500):
    # model = get_model()
    # model.load_weights(filepath)
    model = load_model(filepath)

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
    main()
