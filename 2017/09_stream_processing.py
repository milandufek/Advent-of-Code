# https://adventofcode.com/2017/day/9


def parse_input(file_name: str) -> str:
    with open(file_name) as f:
        return f.read().strip()


def solve_1(string: str) -> int:
    score = 0
    group_level = 0
    in_garbage = False
    skip_next = False

    for char in string:
        if char == '!' or skip_next:
            skip_next = not skip_next
            continue

        if in_garbage:
            if char == '>':
                in_garbage = False
            continue

        if char == '{':
            group_level += 1
            score += group_level
        elif char == '}':
            group_level -= 1
        elif char == '<':
            in_garbage = True

    return score


def solve_2(string: str) -> int:
    garbage_count = 0
    in_garbage = False
    skip_next = False

    for char in string:
        if char == '!' or skip_next:
            skip_next = not skip_next
            continue

        if in_garbage:
            if char == '>':
                in_garbage = False
            else:
                garbage_count += 1
        elif char == '<':
            in_garbage = True

    return garbage_count


if __name__ == '__main__':
    data_input = parse_input('inputs/09.in')
    print(f'Part 1: {solve_1(data_input)}')
    print(f'Part 2: {solve_2(data_input)}')
