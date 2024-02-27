import re
import math
from typing import Generator


# https://adventofcode.com/2015/day/15


def parse_ingredients(input_file: str) -> list[tuple[int]]:
    re_numbers = re.compile(r'-?\d+')  # Match any number including negative ones.
    with open(input_file) as f:
        ingredients = [tuple(map(int, re_numbers.findall(line)))
                       for line in f.readlines()]

    return ingredients


def recipe_combinations(total: int, pieces: int) -> Generator[tuple[int], None, None]:
    if pieces == 0:
        yield ()
    elif pieces == 1:
        yield (total,)
    else:
        for i in range(total + 1):
            for combination in recipe_combinations(total - i, pieces - 1):
                yield (i,) + combination


def group_ingredients_by_item(items: list[tuple[int]]) -> tuple[tuple[int]]:
    return tuple(zip(*items))


def get_score(ingredients: tuple[int], recipe: tuple[int], calories: int = None) -> int:
    total = []
    ingredients = group_ingredients_by_item(ingredients)

    for item in ingredients:
        sum_per_item = sum(value * amount for value, amount in zip(item, recipe))
        total.append(max(0, sum_per_item))

    current_calories = total.pop()

    if calories and calories != current_calories:
        return 0

    return math.prod(total)


def get_max_score(ingredients: list[tuple[int]], calories: int = None) -> int:
    max_score = max(get_score(ingredients, recipe, calories)
                    for recipe in recipe_combinations(100, 4))

    return max_score


def test_get_max_score():
    _example_ingredients = parse_ingredients('inputs/15_example.in')
    _input_ingredients = parse_ingredients('inputs/15.in')
    calories = 500
    assert get_max_score(_example_ingredients) == 62842880
    assert get_max_score(_input_ingredients) == 18965440
    assert get_max_score(_example_ingredients, calories) == 57600000
    assert get_max_score(_input_ingredients, calories) == 15862900


if __name__ == '__main__':
    _input_file = parse_ingredients('inputs/15.in')
    part_1 = get_max_score(_input_file)
    print(f'Score #1: {part_1}')
    part_2 = get_max_score(_input_file, 500)
    print(f'Score #2: {part_2}')
