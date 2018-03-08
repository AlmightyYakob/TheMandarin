FILE1=$1

source ~/.bashrc
cd torch-rnn

if [$# -eq 0]; then
    th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -init_from $FILE1 -gpu -1
else
    th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -model_type rnn -num_layers 3 -rnn_size 256 -gpu -1 #-gpu_backend opencl
fi
