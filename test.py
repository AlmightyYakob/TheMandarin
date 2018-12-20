from tensorflow.keras.models import load_model
import numpy as np
from network import test
import os
import re
import numpy as np

def main():
    baseFileString = 'weights-improvement-'
    files = os.listdir('./')
    fileRegex = re.compile(baseFileString + '(\d+-([\d\.]+))\.hdf5')

    matches = [fileRegex.match(x) for x in files]
    matches = [x for x in matches if x != None]
    minLoss = matches[np.argmin([x.group(2) for x in matches])].group()
    print(test(minLoss, 200))


if __name__ == "__main__":
   main()
