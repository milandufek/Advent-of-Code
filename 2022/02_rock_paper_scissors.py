from my_utils import get_data


# https://adventofcode.com/2022/day/2

def get_score_1(data: list) -> int:
    points = {
        'A': 1,  # rock
        'B': 2,  # paper
        'C': 3,  # scissors
        'X': 1,  # rock
        'Y': 2,  # paper
        'Z': 3,  # scissors
    }
    score = 0

    for he, _, me in data:
        score += points[me]
        # win
        if (he == 'A' and me == 'Y') \
            or (he == 'B' and me == 'Z') \
            or (he == 'C' and me == 'X'):
            score += 6
        # lost
        elif (he == 'A' and me == 'Z') \
            or (he == 'B' and me == 'X') \
            or (he == 'C' and me == 'Y'):
            pass
        # draw
        else:
            score += 3

    return score


def get_score_2(data: list) -> int:
    points = {
        'A': 1,  # rock
        'B': 2,  # paper
        'C': 3,  # scissors
    }
    score = 0

    for he, _, result in data:
        match result:
            case 'Z':  # win
                score += 6
                if he == 'A':
                    score += points['B']
                elif he == 'B':
                    score += points['C']
                else:
                    score += points['A']
            case 'X':  # lost
                if he == 'A':
                    score += points['C']
                elif he == 'B':
                    score += points['A']
                else:
                    score += points['B']
            case 'Y':  # draw
                score += 3
                score += points[he]

    return score


if __name__ == '__main__':
    data = get_data('inputs/02.in')
    print('Score 1:', get_score_1(data))
    print('Score 2:', get_score_2(data))
