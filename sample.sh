#!/bin/bash

SAMPLE_FILE=$1

cd torch-rnn;
#th sample.lua -checkpoint cv/checkpoint_150.t7 -length 2000 -gpu -1
#th sample.lua -checkpoint cv/checkpointTWITTER_1000.t7 -length 2000 -gpu -1
th sample.lua -checkpoint $SAMPLE_FILE -length 2000 -gpu -1
