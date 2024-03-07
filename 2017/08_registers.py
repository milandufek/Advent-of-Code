from collections import defaultdict
from my_utils import get_data


# https://adventofcode.com/2017/day/8


def evaluate_condition(registers: dict, cond_reg: str, cond: str, cond_val: int) -> bool:
    match cond:
        case '==':
            return registers[cond_reg] == cond_val
        case '!=':
            return registers[cond_reg] != cond_val
        case '>':
            return registers[cond_reg] > cond_val
        case '<':
            return registers[cond_reg] < cond_val
        case '>=':
            return registers[cond_reg] >= cond_val
        case '<=':
            return registers[cond_reg] <= cond_val

    raise ValueError(f'Invalid condition: {cond}')


def solve(instructions: str, part: int = 1) -> int:
    registers = defaultdict(int)
    max_value = 0

    for line in instructions:
        reg, op, val, _, cond_reg, cond, cond_val = line.split()

        if evaluate_condition(registers, cond_reg, cond, int(cond_val)):
            val = int(val)

            if op == 'inc':
                registers[reg] += val
            elif op == 'dec':
                registers[reg] -= val
            else:
                raise ValueError(f'Invalid operation: {op}')

        max_value = max(max_value, registers[reg])

    if part == 1:
        return max(registers.values())

    return max_value


if __name__ == '__main__':
    data_input = get_data('inputs/08.in')
    print(f'Part 1: {solve(data_input)}')
    print(f'Part 2: {solve(data_input, 2)}')
