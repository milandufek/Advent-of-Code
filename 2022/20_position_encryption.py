from my_utils import get_data


# https://adventofcode.com/2022/day/20


def decrypt(file: str, part: int) -> None:
    decryption_key = 1
    iterations = 1

    if part == 2:
        decryption_key = 811589153
        iterations = 10

    nodes = [(i, int(val) * decryption_key)
             for i, val in enumerate(get_data(file))]
    size = len(nodes)
    buff = nodes.copy()

    for _ in range(iterations):
        for node in nodes:
            _, value = node
            prev_index = buff.index(node)
            buff.remove(node)
            buff.insert(
                (prev_index + value + size - 1) % (size - 1), node
            )

    origin_zero_node = [x for x in nodes if x[1] == 0][0]
    index_of_zero = buff.index(origin_zero_node)

    res = 0
    for i in range(1, 4):
        res += buff[(index_of_zero + i * 1000) % size][1]

    print(f'Sum #{part} ({file}): {res}')


if __name__ == '__main__':
    decrypt('inputs/20_example.in', part=1)
    decrypt('inputs/20.in', part=1)
    decrypt('inputs/20_example.in', part=2)
    decrypt('inputs/20.in', part=2)
