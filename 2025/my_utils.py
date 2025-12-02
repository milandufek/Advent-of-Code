def get_data(file_path) -> list[str]:
    with open(file_path) as f:
        return f.read().splitlines()
