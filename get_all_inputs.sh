#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <year>"
    echo "  e.g. $0 2019"
    exit 1
fi

YEAR=$1
COOKIE_FILE=".aoc_session"

if [ ! -f "$COOKIE_FILE" ]; then
    echo "Please, create a file named $COOKIE_FILE with your session cookie."
    exit 1
fi

if [ ! -d "$YEAR/inputs" ]; then
    mkdir -p $YEAR/inputs
fi

for day in $(seq 1 25); do
    f_day=$(printf "%02d" $day)
    input_file="$YEAR/inputs/$f_day.txt"
    if [ ! -f "$input_file" ]; then
        echo "Downloading input for $YEAR day $day -> $input_file"
        curl -s --cookie "session=$(cat .aoc_session)" -o $input_file https://adventofcode.com/$YEAR/day/$day/input
    fi
done
