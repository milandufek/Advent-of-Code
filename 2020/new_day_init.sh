#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

source ~/VirtualEnvs/Advent-of-Code/bin/activate

DAY="$1"
YEAR="2020"
URL_INPUT="https://adventofcode.com/${YEAR}/day/${DAY}/input"

[ ${#DAY} -eq 1 ] && F_DAY="0${DAY}" || F_DAY="${DAY}"
FILE_INPUT="inputs/${F_DAY}.txt"
FILE_INPUT_EXAMPLE="inputs/test.txt"
FILE_CODE="day${F_DAY}.py"


[ ! -d "inputs" ] && mkdir -p inputs
[ ! -f $FILE_INPUT ] && curl -s --cookie "session=$(cat ../.aoc_session)" $URL_INPUT >$FILE_INPUT
[ ! -f $FILE_INPUT_EXAMPLE ] && >$FILE_INPUT_EXAMPLE

if [ ! -f $FILE_CODE ]; then
    cat > $FILE_CODE <<EOF
# https://adventofcode.com/${YEAR}/day/${DAY}


def get_data(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.readlines()


def solve_1(data: list[str]) -> int:
    ...


if __name__ == '__main__':
    data_input = get_data('inputs/test.txt')
    #data_input = get_data('inputs/${F_DAY}.txt')
    #print(f'#1: {solve_1(data_input)}')
    #print(f'#2: {solve_2(data_input)}')

EOF

fi
