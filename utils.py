import os


def get_data(file: str) -> list:
    if not os.path.isfile(file):
        print(f"Input file '{file}' not found")
        return

    with open(file) as f:
        return f.read().splitlines()
