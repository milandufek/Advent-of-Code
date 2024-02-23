import logging
import os


def get_data(file: str) -> list:
    if not os.path.isfile(file):
        print(f"Input file '{file}' not found")
        return

    with open(file) as f:
        return f.read().splitlines()


def get_logger(level: int = logging.INFO) -> logging:
    logger = logging.getLogger()
    logger.setLevel(level)
    formatter = logging.Formatter('[%(asctime)s %(levelname)s ] %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def print_grid(grid: set) -> None:
    max_x = max(x for x, _ in grid)
    max_y = max(y for _, y in grid)
    for y in range(max_y + 1):
        print(''.join('#' if (x, y) in grid else '.' for x in range(max_x + 1)))
