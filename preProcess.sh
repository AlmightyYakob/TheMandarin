#!/bin/bash

INPUT_FILE=$1

if [ -z $INPUT_FILE ]; then
    python torch-rnn/scripts/preprocess.py --input_txt output.txt --output_h5 preProcess/my_data.h5 --output_json preProcess/my_data.json
else
    python torch-rnn/scripts/preprocess.py --input_txt $INPUT_FILE --output_h5 preProcess/my_data.h5 --output_json preProcess/my_data.json
fi
