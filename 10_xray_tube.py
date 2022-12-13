from utils import get_data


# https://adventofcode.com/2022/day/10

class Computer:

    def __init__(self, instructions: list) -> None:
        self.instructions = [x for x in reversed(instructions)]
        self.x_register = 1
        self.cycle = 0
        self.inst_val = 0
        self.inst_eta = 0
        self.measures = {}
        self.cycle_history = []
        self.screen = ''

    def measure_cycle(self):
        if (self.cycle - 20) % 40 == 0:
            self.measures[self.cycle] = self.cycle * self.x_register

    def run_instruction(self) -> None:
        if self.inst_eta == 0:

            if self.inst_val:
                self.x_register += self.inst_val
                self.inst_val = 0

            if not self.instructions:
                self.sum_signals()
                self.show_screen()
                exit()

            instruction = self.instructions.pop()

            if instruction == 'noop':
                self.inst_val = 0
                self.inst_eta = 1
            elif instruction.startswith('addx'):
                val = int(instruction.split(' ')[1])
                self.inst_val = val
                self.inst_eta = 2

        if self.inst_eta > 0:
            self.inst_eta -= 1

    def run(self) -> None:
        while True:
            self.cycle += 1
            self.run_instruction()
            self.draw()
            self.measure_cycle()
            self.cycle_history.append(self.x_register)

    def show_screen(self):
        for screen_line in [self.screen[x:x + 40] for x in [i * 40 for i in range(6)]]:
            print(screen_line)

    def draw(self):
        if (self.cycle - 1) % 40 in range(self.x_register - 1, self.x_register + 2):
            self.screen += '🟩'
        else:
            self.screen += '⬛'

    def sum_signals(self) -> None:
        sum = 0
        for v in self.measures.values():
            sum += v
        print('Measure sum:', sum)


if __name__ == '__main__':
    example = [
        'addx 15',
        'addx -11',
        'addx 6',
        'addx -3',
        'addx 5',
        'addx -1',
        'addx -8',
        'addx 13',
        'addx 4',
        'noop',
        'addx -1',
        'addx 5',
        'addx -1',
        'addx 5',
        'addx -1',
        'addx 5',
        'addx -1',
        'addx 5',
        'addx -1',
        'addx -35',
        'addx 1',
        'addx 24',
        'addx -19',
        'addx 1',
        'addx 16',
        'addx -11',
        'noop',
        'noop',
        'addx 21',
        'addx -15',
        'noop',
        'noop',
        'addx -3',
        'addx 9',
        'addx 1',
        'addx -3',
        'addx 8',
        'addx 1',
        'addx 5',
        'noop',
        'noop',
        'noop',
        'noop',
        'noop',
        'addx -36',
        'noop',
        'addx 1',
        'addx 7',
        'noop',
        'noop',
        'noop',
        'addx 2',
        'addx 6',
        'noop',
        'noop',
        'noop',
        'noop',
        'noop',
        'addx 1',
        'noop',
        'noop',
        'addx 7',
        'addx 1',
        'noop',
        'addx -13',
        'addx 13',
        'addx 7',
        'noop',
        'addx 1',
        'addx -33',
        'noop',
        'noop',
        'noop',
        'addx 2',
        'noop',
        'noop',
        'noop',
        'addx 8',
        'noop',
        'addx -1',
        'addx 2',
        'addx 1',
        'noop',
        'addx 17',
        'addx -9',
        'addx 1',
        'addx 1',
        'addx -3',
        'addx 11',
        'noop',
        'noop',
        'addx 1',
        'noop',
        'addx 1',
        'noop',
        'noop',
        'addx -13',
        'addx -19',
        'addx 1',
        'addx 3',
        'addx 26',
        'addx -30',
        'addx 12',
        'addx -1',
        'addx 3',
        'addx 1',
        'noop',
        'noop',
        'noop',
        'addx -9',
        'addx 18',
        'addx 1',
        'addx 2',
        'noop',
        'noop',
        'addx 9',
        'noop',
        'noop',
        'noop',
        'addx -1',
        'addx 2',
        'addx -37',
        'addx 1',
        'addx 3',
        'noop',
        'addx 15',
        'addx -21',
        'addx 22',
        'addx -6',
        'addx 1',
        'noop',
        'addx 2',
        'addx 1',
        'noop',
        'addx -10',
        'noop',
        'noop',
        'addx 20',
        'addx 1',
        'addx 2',
        'addx 2',
        'addx -6',
        'addx -11',
        'noop',
        'noop',
        'noop',
    ]
    # sc = Computer(example)
    # sc.run()
    data = get_data('inputs/10.in')
    sc = Computer(data)
    sc.run()
