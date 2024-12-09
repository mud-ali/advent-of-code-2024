#!/bin/zsh

# Ask for the day number
echo "What day is it? "
read day

# Pad the day number to two digits
day_padded=$(printf "%02d" $day)

# Create the new folder
mkdir "day$day_padded"
cd "day$day_padded"

# create files to store input and sample data
touch input.txt
touch test.txt

echo "Choose a template: Python (py), Typescript (ts), Blank (b)"
read template

if [ "$template" = "py" ]; then
    cp ../templates/part1.py .
elif [ "$template" = "ts" ]; then
    cp ../templates/part1.ts .
    npm install "@types/node"
    tsc --init
    echo "node_modules" > .gitignore
    rm -f package-lock.json
fi
