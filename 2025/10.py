from collections import deque
from my_utils import get_data


# https://adventofcode.com/2025/day/10


def find_min_presses(diagram: list[str], buttons: list[tuple[int, ...]], start: list[str]) -> int:
    queue = deque([(start, 0)])
    visited = set()

    while queue:
        state, step = queue.popleft()
        state_id = ''.join(state)

        if state_id in visited:
            continue

        visited.add(state_id)

        if state == diagram:
            return step

        for button in buttons:
            new_state = state.copy()
            for position in button:
                new_state[position] = '#' if state[position] == '.' else '.'
            queue.append((new_state, step + 1))

    return -1


def solve_1(data: list[str]) -> int:
    score = 0
    for line in data:
        items = line.split()
        diagram = list(items[0][1:-1])
        buttons = [tuple(map(int, i.strip('()').split(','))) for i in items[1:-1]]
        start = list('.' * len(diagram))
        score += find_min_presses(diagram, buttons, start)

    return score


if __name__ == '__main__':
    example = get_data('inputs/10_example.in')
    data_input = get_data('inputs/10.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score   #1: {solve_1(data_input)}')
    # print(f'Example #2: {solve_2(example)}')
    # print(f'Score   #2: {solve_2(data_input)}')
