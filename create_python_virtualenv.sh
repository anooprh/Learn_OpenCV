#!/bin/bash


# 
#  Run this file as 
#  source ./create_python_virtual_env.sh

# Check if virtual env is there or not
hash virtualenv 2>/dev/null || 
{ echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }

# Set the working directory
THIS_DIR=`dirname $0` > /dev/null
cd $THIS_DIR

# Create a virtual env
virtualenv opencv_python

# Avtivate the virtual env
source opencv_python/bin/activate

# Install the dependencies
pip install -r requirements.txt