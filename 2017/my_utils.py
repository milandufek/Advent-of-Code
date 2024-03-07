def get_data(file: str) -> list[str]:
    with open(file) as f:
        return f.read().splitlines()
