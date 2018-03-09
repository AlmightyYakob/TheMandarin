FILE1=$1
DATAPATH=../preProcess

source ~/.bashrc
cd torch-rnn

#if [$# -eq 0]; then
#    th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -init_from $FILE1 -gpu -1
#else
#    th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -model_type rnn -num_layers 3 -rnn_size 256 -gpu -1 #-gpu_backend opencl
#fi

#th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -init_from cv/checkpoint_150.t7 -batch_size 200 -seq_length 200 -gpu -1
#th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -num_layers 4 -rnn_size 512 -checkpoint_name "cv/checkpointTWITTER" -gpu -1
th train.lua -input_h5 $DATAPATH/my_data.h5 -input_json $DATAPATH/my_data.json -num_layers 4 -rnn_size 512 -checkpoint_name "cv/checkpointTWITTER" -gpu -1

