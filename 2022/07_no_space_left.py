import re
from collections import defaultdict
from utils import get_data


# https://adventofcode.com/2022/day/7

MAX_SIZE = 100000
TOTAL_SPACE = 70000000
UPDATE_SIZE = 30000000


def parse_commands(commands: list) -> defaultdict:
    pwd = []
    sizes = defaultdict(int)
    for line in commands:
        if line.startswith('$ cd'):
            dir_name = line.split()[-1]
            if dir_name == '..':
                pwd.pop()
            else:
                pwd.append(dir_name)
        elif re.findall(r'^\d+ .*$', line):
            size, _ = line.split(' ')
            size = int(size)
            for i in range(len(pwd)):
                sizes['/'.join(pwd[:i + 1])] += size
        elif line.startswith(('$ ls', 'dir')):
            continue  # useless inputs
        else:
            raise Exception(f'Some nasty line occurred: {line}')

    # print(sizes)
    return sizes


def count_space(sizes: defaultdict, max_size: int = MAX_SIZE) -> None:
    total = 0
    for _, val in sizes.items():
        if val < max_size:
            total += val

    print('#1', total)


def find_smallest(sizes: defaultdict) -> None:
    used_space = sizes['/']
    free_space = TOTAL_SPACE - used_space
    required_space = UPDATE_SIZE - free_space
    options = []
    for _, val in sizes.items():
        if val > required_space:
            options.append(val)

    print('#2', min(options))


if __name__ == '__main__':
    example = [
        '$ cd /',
        '$ ls',
        'dir a',
        '14848514 b.txt',
        '8504156 c.dat',
        'dir d',
        '$ cd a',
        '$ ls',
        'dir e',
        '29116 f',
        '2557 g',
        '62596 h.lst',
        '$ cd e',
        '$ ls',
        '584 i',
        '$ cd ..',
        '$ cd ..',
        '$ cd d',
        '$ ls',
        '4060174 j',
        '8033020 d.log',
        '5626152 d.ext',
        '7214296 k',
    ]
    count_space(parse_commands(example))
    print('## Data input')
    data = get_data('inputs/07.in')
    fs = parse_commands(data)
    count_space(fs)
    find_smallest(fs)
