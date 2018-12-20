from tensorflow.keras.models import load_model
import numpy as np
from network import test, getBestCheckpoint
import os
import re
import numpy as np

def main():
    minLoss = getBestCheckpoint()
    print(test(minLoss, 200))


if __name__ == "__main__":
   main()
