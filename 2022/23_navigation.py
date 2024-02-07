from collections import defaultdict, deque
from utils import get_data


# https://adventofcode.com/2022/day/23


elves = set()
moves = deque([1j, -1j, -1, 1])  # NSWE
ADJACENT = [1j, 1 + 1j, 1, 1 - 1j, -1j, -1 - 1j, -1, -1 + 1j]
DIRECTIONS = {
    1j: [1j - 1, 1j, 1j + 1],
    -1j: [-1j - 1, -1j, -1j + 1],
    -1: [-1 - 1j, -1, -1 + 1j],
    1: [1 - 1j, 1, 1 + 1j],
}


def parse_input(file: str) -> None:
    for y, line in enumerate(get_data(file)):
        for x, i in enumerate(line):
            if i == '#':
                elves.add(x + y * -1j)


def show_score(iter: int) -> None:
    x_min = min(x.real for x in elves)
    x_max = max(x.real for x in elves)
    y_min = min(x.imag for x in elves)
    y_max = max(x.imag for x in elves)

    free = int((x_max - x_min + 1) * (y_max - y_min + 1) - len(elves))
    print(f'Score (iter={iter}): {free}')


def main(input_file: str) -> None:
    parse_input(input_file)
    prev_positions = set()

    for i in range(1, 10_000):
        proposals = defaultdict(int)

        for elf in elves:
            if all(elf + x not in elves for x in ADJACENT):
                continue

            for move in moves:
                if all(elf + x not in elves for x in DIRECTIONS[move]):
                    proposal_position = elf + move

                    if proposals[proposal_position] > 1:
                        break

                    proposals[proposal_position] += 1
                    break

        new_elves = elves.copy()

        for elf in new_elves:
            if all(elf + x not in new_elves for x in ADJACENT):
                continue

            for move in moves:
                if all(elf + x not in new_elves for x in DIRECTIONS[move]):
                    proposal_position = elf + move

                    if proposals[proposal_position] < 2:
                        elves.remove(elf)
                        elves.add(proposal_position)

                    break

        if i == 10:
            show_score(i)

        if prev_positions == elves:
            show_score(i)
            break

        prev_positions = elves.copy()
        moves.rotate(-1)


if __name__ == '__main__':
    # main('inputs/23_example.in')
    main('inputs/23.in')
