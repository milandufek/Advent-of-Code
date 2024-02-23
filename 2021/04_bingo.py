from my_utils import get_data


# https://adventofcode.com/2021/day/4


def parse_input(_input: list[str]) -> tuple[list[int], list[list[list[int]]]]:
    draws = map(int, _input[0].split(','))

    board = []
    boards = []
    for line in _input[1:][1:]:
        if not line:
            boards.append(board)
            board = []
            continue

        board.append(list(map(int, line.split())))

    boards.append(board)

    return draws, boards


def bingo(board: list[list[int | None]]) -> bool:
    return any(
        all(x is None
            for x in row)
            for row in board
    ) or any(
        all(row[i] is None
            for row in board)
            for i in range(len(board[0]))
    )


def solve_1(_input: list[str]) -> int:
    draws, boards = parse_input(_input)
    for num in draws:
        for board in boards:
            for row in board:
                for x, _ in enumerate(row):
                    if row[x] == num:
                        row[x] = None

            if bingo(board):
                return sum(x or 0 for row in board for x in row) * num

    return -1


def solve_2(_input: list[str]) -> int:
    draws, boards = parse_input(_input)
    num = 0

    for num in draws:
        index = 0
        while index < len(boards):
            board = boards[index]
            for row in board:
                for x, _ in enumerate(row):
                    if row[x] == num:
                        row[x] = None

            if bingo(board):
                last_board = boards.pop(index)
            else:
                index += 1

        if not boards:
            break

    return sum(x or 0 for row in last_board for x in row) * num


if __name__ == '__main__':
    example = get_data('inputs/04_example.in')
    data_input = get_data('inputs/04.in')
    print(f'Example #1: {solve_1(example)}')
    print(f'Score #1: {solve_1(data_input)}')
    print(f'Example #2: {solve_2(example)}')
    print(f'Score #2: {solve_2(data_input)}')
