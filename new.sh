#!/bin/zsh

# Ask for the day number
echo "What day is it? "
read day

# Pad the day number to two digits
day_padded=$(printf "%02d" $day)

# Create the new folder
mkdir "day$day_padded"
cd "day$day_padded"
touch part1.py
touch input.txt
touch test.txt