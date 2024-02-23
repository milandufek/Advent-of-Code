import functools
from my_utils import get_data


# https://adventofcode.com/2015/day/7


OPERATORS = {
    'EQ': lambda x: x(0),
    'NOT': lambda x: ~x(1),
    'AND': lambda x: x(0) & x(2),
    'OR': lambda x: x(0) | x(2),
    'LSHIFT': lambda x: x(0) << x(2),
    'RSHIFT': lambda x: x(0) >> x(2),
}

class AssemblySolver:
    def __init__(self, operators, definitions):
        self.operators = operators
        self.definitions = definitions

    @functools.lru_cache
    def get(self, key) -> None:
        try:
            value = int(key)
        except ValueError:
            cmd: str = self.definitions[key].split(' ')
            op: str = self.parse_operator(cmd)
            argument = functools.partial(self.get_argument, cmd)
            value = self.operators[op](argument)

        return value

    def parse_operator(self, cmd):
        return next((x for x in self.operators if x in cmd), 'EQ')

    def get_argument(self, cmd, index):
        return self.get(cmd[index])

    def replace(self, update):
        return AssemblySolver(self.operators, {**self.definitions, **update})


def parse_input(_input_file):
    pairs = [x.strip().split(' -> ') for x in get_data(_input_file)]
    return {k: v for v, k in pairs}


if __name__ == '__main__':
    _input_data = 'inputs/07.in'
    solver = AssemblySolver(OPERATORS, parse_input(_input_data))
    score_1 = solver.get('a')
    print(f'#1: {score_1}')

    solver = solver.replace({'b': str(score_1)})
    score_2 = solver.get('a')
    print(f'#2: {score_2}')
