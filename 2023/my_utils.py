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
