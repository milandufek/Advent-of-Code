#!/bin/bash

DAY="$(date +%d)"
YEAR="$(date +%Y)"
F_INPUT="inputs/${DAY}.in"
F_INPUT_EXAMPLE="inputs/${DAY}_example.in"
FILE_CODE="${DAY}_.py"
URL_INPUT="https://adventofcode.com/${YEAR}/day/${DAY}/input"


if [ ! -d "inputs" ]; then
    mkdir -p inputs
fi

if [ ! -f $F_INPUT ]; then
    curl -s --cookie "session=$(cat .aoc_session)" $URL_INPUT > $F_INPUT
fi

if [ ! -f $F_INPUT_EXAMPLE ]; then
    >$F_INPUT_EXAMPLE
fi

if [ ! -f $FILE_CODE ]; then
    cat > $FILE_CODE <<EOF
from my_utils import get_data





if __name__ == '__main__':
    example = get_data('inputs/${DAY}_example.in')
    #data = get_data('inputs/${DAY}.in')

EOF

fi
