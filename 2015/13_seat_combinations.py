from itertools import permutations
from utils import get_data


def parse_data(file: str) -> list:
    persons = set()
    persons.add('Me')  # part 2
    rules = []

    for line in get_data(file):
        # Alice would gain 54 happiness units by sitting next to Bob.
        words = line.split()
        a = words[0]
        b = words[-1].replace('.', '')
        ops = words[2]
        points = int(words[3])
        rules.append((a, ops, points, b))
        persons.add(a)
        persons.add(b)

    tables = list(permutations(persons))

    return tables, rules


def show_score(data: tuple) -> None:
    scores = []
    tables, rules = data

    for table in tables:
        total_points = 0
        for rule in rules:
            a, ops, points, b = rule
            distance = abs(table.index(a) - table.index(b))

            if distance == 1 or distance == len(table) - 1:
                if ops == 'gain':
                    total_points += points
                else:
                    total_points -= points

        scores.append(total_points)

    print(f'Max score: {max(scores)}')


if __name__ == '__main__':
    show_score(parse_data('inputs/13_example.in'))
    show_score(parse_data('inputs/13.in'))
