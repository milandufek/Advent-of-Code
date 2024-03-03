import re
import math
from collections import defaultdict, deque
from my_utils import get_data


# https://adventofcode.com/2016/day/10


class Bot:
    def __init__(self) -> None:
        self.low: int = None
        self.high: int = None
        self.l_type: str = None
        self.h_type: str = None
        self.chips: list[int] = []

    def get_chip(self, chip: int) -> None:
        if chip not in self.chips:
            self.chips.append(chip)
            self.chips.sort()

    @property
    def ready_to_pass(self) -> bool:
        return len(self.chips) > 1


def parse_input(_input):
    bots = defaultdict(Bot)
    re_nums = re.compile(r'\d+')

    for line in _input:
        t = line.split(' ')

        match t[0]:
            case 'value':
                values = re.findall(re_nums, line)
                chip, bot = map(int, values)
                bots[bot].get_chip(chip)
            case 'bot':
                l_type, h_type = t[5], t[10]
                values = re.findall(re_nums, line)
                bot, low, high = map(int, values)
                bots[bot].low = low
                bots[bot].high = high
                bots[bot].l_type = l_type
                bots[bot].h_type = h_type

    return bots


def solve_1(bots: dict[int, Bot], target: list[int]):
    queue = deque(bot_num for bot_num, bot in bots.items() if bot.ready_to_pass)

    while queue:
        bot_num = queue.popleft()
        bot = bots[bot_num]

        if not bot.ready_to_pass:
            continue

        if bot.chips == target:
            return bot_num

        if bot.l_type == 'bot':
            bots[bot.low].get_chip(bot.chips[0])
            queue.append(bot.low)

        if bot.h_type == 'bot':
            bots[bot.high].get_chip(bot.chips[1])
            queue.append(bot.high)

    return -1


def solve_2(bots: dict[int, Bot]):
    queue = deque(bot_num for bot_num, bot in bots.items() if bot.ready_to_pass)
    outputs = [None] * 3

    while queue:
        bot_num = queue.popleft()
        bot = bots[bot_num]

        if not bot.ready_to_pass:
            continue

        if bot.l_type == 'bot':
            bots[bot.low].get_chip(bot.chips[0])
            queue.append(bot.low)
        elif bot.low < 3:
            outputs[bot.low] = bot.chips[0]

        if bot.h_type == 'bot':
            bots[bot.high].get_chip(bot.chips[1])
            queue.append(bot.high)
        elif bot.high < 3:
            outputs[bot.high] = bot.chips[1]

        if all(o is not None for o in outputs):
            return math.prod(outputs)

    return -1


if __name__ == '__main__':
    _data_input = get_data('inputs/10.in')
    _bots: dict[int, Bot] = parse_input(_data_input)
    print(f'Part 1: {solve_1(_bots, [17, 61])}')
    print(f'Part 2: {solve_2(_bots)}')
