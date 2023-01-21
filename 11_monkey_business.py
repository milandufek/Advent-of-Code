from typing import List, Tuple, Generator


# https://adventofcode.com/2022/day/11


class Parser:

    def __init__(self, file_input) -> None:
        self.file = file_input

    def get_plan(self) -> list:
        with open(self.file) as f:
            return f.read().split('\n\n')

    def get_last_int(self, line: str) -> int:
        return int(line.split()[-1].strip())

    def generate_monkeys(self):
        monkeys = []
        common_divider = 1
        plan = self.get_plan()

        for name, m in enumerate(plan):
            for line in m.split('\n'):
                if line.startswith('    If true'):
                    if_true = self.get_last_int(line)
                elif line.startswith('    If false'):
                    if_false = self.get_last_int(line)
                elif line.startswith('  Starting items:'):
                    items = []
                    for i in line.split(' '):
                        val = i.replace(',', '')
                        if val.isdigit():
                            items.append(val)
                elif line.startswith('  Operation:'):
                    _, ops_type, ops_num = line.split('=')[-1].split()
                elif line.startswith('  Test:'):
                    divider = self.get_last_int(line)
                    common_divider *= divider

            monkeys.append(
                Monkey(name, items, ops_type, ops_num, divider, if_true, if_false))

        return monkeys, common_divider


class Monkey:

    def __init__(self, name: int, items: list, operation_type: str,
                 operation_num: str, test_div: int, true_target: int,
                 false_target: int, common_divider: int = 1) -> None:
        self.name = name
        self.items = items
        self.operator = operation_type
        self.operand = operation_num
        self.test_div = test_div
        self.true_target = true_target
        self.false_target = false_target
        self.common_divider = common_divider
        self.inspected_items = 0

    def play(self) -> Generator[tuple, None, None]:
        for _ in range(len(self.items)):
            self.inspected_items += 1
            item = int(self.items.pop())
            item = self.operate(item)
            item = self.divide_by_three(item)
            yield self.throw_item(item)

    def operate(self, item: int) -> int:
        if self.operand == 'old':
            operand: int = item
        else:
            operand: int = int(self.operand)

        if self.operator == '*':
            item *= operand
        elif self.operator == '+':
            item += operand
        else:
            raise NotImplementedError(self.operator)

        return item

    def divide_by_three(self, number: int) -> int:
        # return int(number / 3)  # part 1
        return number % self.common_divider  # part 2

    def test_divisible(self, number: int) -> bool:
        return number % self.test_div == 0

    def throw_item(self, item: int) -> Tuple[int, ...]:
        if self.test_divisible(item):
            monkey: int = self.true_target
        else:
            monkey: int = self.false_target

        return monkey, item

    def receive_item(self, item: int) -> None:
        self.items.append(item)


class MonkeyBusiness:

    def __init__(self, monkeys: List[Monkey], common_divider) -> None:
        self.monkeys = monkeys
        self.common_divider = common_divider
        self.rounds = 0

    def round(self) -> None:
        self.rounds += 1
        for playing_monkey in self.monkeys:
            if self.rounds == 1:
                playing_monkey.common_divider = self.common_divider
            for target_monkey, thrown_item in playing_monkey.play():
                self.monkeys[target_monkey].receive_item(thrown_item)

    def play(self, rounds: int = 20) -> None:
        for _ in range(rounds):
            self.round()

    def show_score(self) -> None:
        activity = [m.inspected_items for m in self.monkeys]
        activity.sort()
        print('Score:', activity[-1] * activity[-2])

    def show_item_holders(self) -> None:
        for i, m in enumerate(self.monkeys):
            print(f'{i}: {m.items}')


if __name__ == '__main__':
    # monkeys, common_divider = Parser('inputs/11_example.in').generate_monkeys()
    monkeys, common_divider = Parser('inputs/11.in').generate_monkeys()
    game = MonkeyBusiness(monkeys, common_divider)
    # game.play(20)
    game.play(10000)
    game.show_score()
