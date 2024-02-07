import sympy
from my_utils import get_data


# https://adventofcode.com/2022/day/21


def main(file: str, part: int = 1) -> None:
    monkeys = {}
    source = get_data(file)

    for line in source:
        name, expr = line.split(':')

        if expr.strip().isdigit():
            if part == 2:
                monkeys[name] = sympy.Symbol('x') if name == 'humn'\
                                else sympy.Integer(expr)
            else:
                monkeys[name] = int(expr)
        else:
            left, op, right = expr.split()

            if left in monkeys and right in monkeys:
                if part == 2 and name == 'root':
                    x = sympy.solve(monkeys[left] - monkeys[right], 'x')[0]
                    print(f'#2 humn x ({file}): {x}')
                    break

                number = evaluate(monkeys[left], monkeys[right], op)
                monkeys[name] = number
            else:
                source.append(line)

    if part == 1:
        print(f"#1 Monkey root ({file}): {int(monkeys['root'])}")


def evaluate(left: int, right: int, op: str) -> float:
    res = None
    if op == '+':
        res = left + right
    elif op == '-':
        res = left - right
    elif op == '*':
        res = left * right
    elif op == '/':
        res = left / right
    else:
        raise NotImplementedError(f"Operation '{op}' is not defined.")

    return res


if __name__ == '__main__':
    main('inputs/21_example.in', part=1)
    main('inputs/21.in', part=1)
    main('inputs/21_example.in', part=2)
    main('inputs/21.in', part=2)
