#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

source ~/VirtualEnvs/Advent-of-Code/bin/activate

DAY="$1"
YEAR="$(date +%Y)"
URL_INPUT="https://adventofcode.com/${YEAR}/day/${DAY}/input"

[ ${#DAY} -eq 1 ] && F_DAY="0${DAY}" || F_DAY="${DAY}"
FILE_INPUT="inputs/${F_DAY}.in"
FILE_INPUT_EXAMPLE="inputs/${F_DAY}_example.in"
FILE_CODE="${F_DAY}_.py"


[ ! -d "inputs" ] && mkdir -p inputs
[ ! -f $FILE_INPUT ] && curl -s --cookie "session=$(cat .aoc_session)" $URL_INPUT >$FILE_INPUT
[ ! -f $FILE_INPUT_EXAMPLE ] && >$FILE_INPUT_EXAMPLE

if [ ! -f $FILE_CODE ]; then
    cat > $FILE_CODE <<EOF
from my_utils import get_data


# https://adventofcode.com/${YEAR}/day/${DAY}





if __name__ == '__main__':
    example = get_data('inputs/${F_DAY}_example.in')
    #data_input = get_data('inputs/${F_DAY}.in')
    print(f'Example #1: {solve_1(example)}')
    #print(f'Score #1: {solve_1(data_input)}')
    #print(f'Example #2: {solve_2(example)}')
    #print(f'Score #2: {solve_2(data_input)}')

EOF

fi
