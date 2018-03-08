source ~/.bashrc
cd torch-rnn
th train.lua -input_h5 ../my_data.h5 -input_json ../my_data.json -model_type rnn -num_layers 3 -rnn_size 256 -gpu -1 #-gpu_backend opencl
