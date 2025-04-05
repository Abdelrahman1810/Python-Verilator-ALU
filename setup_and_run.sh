#!/bin/bash

# Exit immediately if a command fails
set -e

echo "Installing Verilator..."
sudo apt update
sudo apt install verilator -y
which verilator
verilator --version

echo "Installing GTKWave..."
sudo apt install gtkwave -y
which gtkwave
gtkwave --version

echo "Installing Prerequisites..."
sudo apt-get install -y \
    git help2man perl python3 make autoconf g++ flex bison ccache \
    libgoogle-perftools-dev numactl perl-doc libfl2 libfl-dev \
    zlib1g zlib1g-dev python3-pip build-essential libssl-dev \
    libffi-dev python3-dev python3-venv

echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Installing important library
pip install typing 
pip install parsy
pip install pybind11

# Navigate to example directory and make scripts executable
cd example
sudo chmod +x *

echo "Running ALU testbench..."
make run

echo "Start WaveForm...(Without script)"
make sim

echo "Start WaveForm...(Without script)"
make sim_script