from utils import get_data


# https://adventofcode.com/2023/day/7


MAPPING = {
    'T': 'a',
    'J': 'b',
    'Q': 'c',
    'K': 'd',
    'A': 'e',
}


def get_score(hand: str) -> int:
    count = [hand.count(h) for h in hand]

    if 5 in count:
        return 6

    if 4 in count:
        return 5

    if 3 in count and 2 in count:
        return 4

    if 3 in count:
        return 3

    if count.count(2) == 4:
        return 2

    if 2 in count:
        return 1

    return 0


def ranked_1(hand: str) -> tuple:
    return get_score(hand), [MAPPING.get(c, c) for c in hand]


def try_jokers(hand: str) -> list:
    return [''] if hand == '' else [
        x + y
        for x in ('23456789TQKA' if hand[0] == 'J' else hand[0])
        for y in try_jokers(hand[1:])
    ]


def evaluate(hand: str) -> int:
    return max(map(get_score, try_jokers(hand)))


def ranked_2(hand: str) -> tuple:
    return evaluate(hand), [MAPPING.get(c, c) for c in hand]


def game(data: list, part: int = 1) -> int:
    hands = [line.split() for line in data]

    if part == 1:
        hands.sort(key=lambda hand: ranked_1(hand[0]))
    else:
        MAPPING['J'] = '*'
        hands.sort(key=lambda hand: ranked_2(hand[0]))

    score = 0
    for rank, (_, bid) in enumerate(hands, start=1):
        score += rank * int(bid)

    return score


if __name__ == '__main__':
    example = get_data('inputs/07_example.in')
    data = get_data('inputs/07.in')
    print(f'Example #1: {game(example)}')
    print(f'Score #1: {game(data)}')
    print(f'Example #2: {game(example, 2)}')
    print(f'Score #2: {game(data, 2)}')
