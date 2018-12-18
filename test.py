from tensorflow.keras.models import load_model
import numpy as np
from network import SEQ_LENGTH, n_chars, n_vocab, chars, int_to_char

def generate_text(model, length):
    num = [np.random.randint(n_vocab)]
    y_char = [int_to_char[num[-1]]]
    X = np.zeros((SEQ_LENGTH, 1))

    for i in range(length):
        pred = model.predict([X])
        X[i] = pred
        y_char.append(int_to_char[pred])

    return ('').join(y_char)


model = load_model('weights-improvement-02-2.8127.hdf5')
generate_text(model, 500)