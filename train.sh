#!/bin/bash

CHECKPOINT=$1
DATAPATH=~/twitterBot/preProcess

source ~/.bashrc
cd torch-rnn

#th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -init_from cv/checkpoint_150.t7 -batch_size 200 -seq_length 200 -gpu -1
#th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -num_layers 4 -rnn_size 512 -checkpoint_name "cv/checkpointTWITTER" -gpu -1

if [ -z "$1" ]; then
    th train.lua -input_h5 $DATAPATH/my_data.h5 -input_json $DATAPATH/my_data.json -num_layers 4 -rnn_size 512 -dropout 0.1 -batch_size 200 -seq_length 200 -checkpoint_name "cv/checkpointTWITTER" -gpu -1
else
    th train.lua -input_h5 $DATAPATH/my_data.h5 -input_json $DATAPATH/my_data.json -checkpoint_name "cv/checkpointTWITTER" -init_from $CHECKPOINT -gpu -1
fi
