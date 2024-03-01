def get_data(file: str) -> list:
    with open(file) as f:
        return f.readlines()
