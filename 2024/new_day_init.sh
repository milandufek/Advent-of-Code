#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <day>"
    exit 1
fi

source ~/VirtualEnvs/Advent-of-Code/bin/activate

DAY="$1"
YEAR="$(date +%Y)"
URL_INPUT="https://adventofcode.com/${YEAR}/day/${DAY}/input"

# [ ${#DAY} -eq 1 ] && F_DAY="0${DAY}" || F_DAY="${DAY}"
FILE_INPUT="inputs/${DAY}.txt"
FILE_INPUT_EXAMPLE="inputs/test.txt"
FILE_CODE="d${DAY}p1.ts"


[ ! -d "inputs" ] && mkdir -p inputs
[ ! -f $FILE_INPUT ] && curl -s --cookie "session=$(cat ../.aoc_session)" $URL_INPUT >$FILE_INPUT
[ ! -f $FILE_INPUT_EXAMPLE ] && >$FILE_INPUT_EXAMPLE

if [ ! -f $FILE_CODE ]; then
    cat > $FILE_CODE <<EOF
import { readFileSync } from 'fs';

// https://adventofcode.com/${YEAR}/day/${DAY}

function readFile(path: string): string[] {
    const data: string = readFileSync(path, 'utf-8');
    return data.trim().split('\n').map(s => s.trim());
}

function solve(input: string[]): void {
    lines.forEach(line => {
        console.log(line);
    });
}

solve(readFile('inputs/test.txt'));
// solve(readFile('inputs/1.txt'));

EOF

fi
