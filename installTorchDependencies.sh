source ~/.bashrc

./installTorch.sh

luarocks install torch
luarocks install nn
luarocks install optim
luarocks install lua-cjson

# We need to install torch-hdf5 from GitHub
git clone https://github.com/deepmind/torch-hdf5 ~/torch-hdf5
cd ~/torch-hdf5
luarocks make hdf5-0-0.rockspec
