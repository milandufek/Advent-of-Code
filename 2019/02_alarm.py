# https://adventofcode.com/2019/day/2


def parse_input(file_name: str) -> list[int]:
    with open(file_name) as f:
        return list(map(int, f.read().split(',')))


def solve_1(code: list[int]) -> int:
    code[1] = 12
    code[2] = 2
    for i in range(0, len(code), 4):
        if code[i] == 99:
            break

        if code[i] == 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
        elif code[i] == 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]

    return code[0]


def solve_2(code: list[int], target: int = 19690720) -> int:
    for noun in range(100):
        for verb in range(100):
            cc = code.copy()
            cc[1] = noun
            cc[2] = verb
            for i in range(0, len(cc), 4):
                if cc[i] == 99:
                    break

                if cc[i] == 1:
                    cc[cc[i + 3]] = cc[cc[i + 1]] + cc[cc[i + 2]]
                elif cc[i] == 2:
                    cc[cc[i + 3]] = cc[cc[i + 1]] * cc[cc[i + 2]]

            if cc[0] == target:
                return 100 * noun + verb

    return -1


if __name__ == '__main__':
    data_input = parse_input('inputs/02.in')
    print(f'Part 1: {solve_1(data_input)}')
    data_input = parse_input('inputs/02.in')
    print(f'Part 2: {solve_2(data_input)}')
