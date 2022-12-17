#!/bin/bash

DAY="$(date +%d)"

[ ! -d "inputs" ] && mkdir -p inputs

F_INPUT="inputs/${DAY}.in"
[ ! -f $F_INPUT ] && >$F_INPUT

F_INPUT_EXAMPLE="inputs/${DAY}_example.in"
[ ! -f $F_INPUT_EXAMPLE ] && >$F_INPUT_EXAMPLE



FILE_CODE="${DAY}_.py"

if [ ! -f $FILE_CODE ]; then

    cat > $FILE_CODE <<EOF
from utils import get_data





if __name__ == '__main__':
    example = get_data('inputs/${DAY}_example.in')
    #data = get_data('inputs/${DAY}.in')

EOF

fi
