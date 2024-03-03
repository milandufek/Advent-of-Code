from collections import deque
from itertools import takewhile, islice
from my_utils import get_data


# https://adventofcode.com/2016/day/9


def decompress_1(phrase: str) -> int:
    decoded_sequence = []
    phrase: deque = deque(phrase.strip())

    while phrase:
        char = phrase.popleft()

        if char == '(':
            marker = ''
            while (char := phrase.popleft()) != ')':
                marker += char

            length, times = map(int, marker.split('x'))
            sequence = ''.join(phrase.popleft() for _ in range(length))

            for _ in range(times):
                decoded_sequence.append(sequence)
        else:
            decoded_sequence.append(char)

    return len(''.join(decoded_sequence))


def decompress(phrase: str, recurse: bool = False) -> int:
    total = 0
    chars = iter(phrase.strip())

    for ch in chars:
        if ch == '(':
            length, times = map(
                int,
                [''.join(takewhile(lambda ch: ch not in 'x)', chars)) for _ in range(2)]
            )
            sequence = ''.join(islice(chars, length))

            if recurse:
                total += decompress(sequence, recurse) * times
            else:
                total += len(sequence) * times
        else:
            total += 1

    return total


if __name__ == '__main__':
    data_input = get_data('inputs/09.in')[0]
    print(f'Part 1: {decompress_1(data_input)}')
    print(f'Part 1: {decompress(data_input)}')
    print(f'Part 2: {decompress(data_input, True)}')
