#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Please install Python3 to use this tool."
    exit 1
fi

# Check if the user provided a number
if [ -z "$1" ]; then
    echo "Usage: ./factorize.sh <number>"
    exit 1
fi

# Call the Python script with the provided number
python3 factorize.py "$1"
