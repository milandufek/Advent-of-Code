from collections import Counter
from my_utils import get_data


# https://adventofcode.com/2016/day/4


def caesar_cipher(phrase: str, shift: int) -> str:
    offset = ord('a')
    return ''.join([chr((ord(ch) - offset + shift) % 26 + offset) for ch in phrase])


def solve(data: list[str]) -> None:
    valid = []
    decrypted = []

    for line in data:
        phrase, checksum = line.strip().split('[')
        checksum = ''.join(sorted(checksum[:-1]))
        phrase = phrase.split('-')
        _id = int(phrase.pop())
        phrase = '-'.join(phrase)
        letter_counts = Counter(phrase.replace('-', ''))
        top5 = sorted(letter_counts.items(), key=lambda x: (len, x[0]))[:5]
        top5 = ''.join([letter for letter, _ in top5])

        if top5 == checksum:
            valid.append(_id)

        decrypted.append((caesar_cipher(phrase, _id), _id))

    for phrase, _id in decrypted:
        if 'northpole' in phrase:
            break

    print(f'Part 1: {sum(valid)}')
    print(f'Part 2: {_id} ({phrase})')


if __name__ == '__main__':
    example_input = [
        'aaaaa-bbb-z-y-x-123[abxyz]',
        'a-b-c-d-e-f-g-h-987[abcde]',
        'not-a-real-room-404[oarel]',
        'totally-real-room-200[decoy]',
    ]
    data_input = get_data('inputs/04.in')
    solve(data_input)
