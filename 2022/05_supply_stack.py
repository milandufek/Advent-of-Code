from my_utils import get_data


# https://adventofcode.com/2022/day/5

STACKS_EXAMPLE = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P'],
}
STACKS = {
    1: ['D', 'L', 'J', 'R', 'V', 'G', 'F'],
    2: ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S'],
    3: ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C'],
    4: ['M', 'D', 'P', 'N', 'G', 'Q'],
    5: ['J', 'L', 'H', 'N', 'F'],
    6: ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z'],
    7: ['F', 'D', 'B', 'L'],
    8: ['M', 'J', 'B', 'S', 'V', 'D', 'N'],
    9: ['G', 'L', 'D'],
}


def cargo(stacks: dict, moves: list, move_in_order=True) -> str:
    for line in moves:
        # e.g.: 'move 3 from 4 to 6'
        _, count, _, source, _, target = tuple(line.split(' '))

        if move_in_order:
            stacks[int(target)].extend(stacks[int(source)][-int(count):])
            del stacks[int(source)][-int(count):]
        else:
            for _ in range(int(count)):
                item = stacks[int(source)].pop()
                stacks[int(target)].append(item)

    return ''.join([top.pop() for top in stacks.values()])


if __name__ == '__main__':
    example = [
        'move 1 from 2 to 1',
        'move 3 from 1 to 3',
        'move 2 from 2 to 1',
        'move 1 from 1 to 2',
    ]
    data = get_data('inputs/05.in')
    print('Example:', cargo(STACKS_EXAMPLE, example))
    print('Batch:', cargo(STACKS, data))
