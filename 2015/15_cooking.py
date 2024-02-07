import re
from functools import reduce


# ingredients = {}
ingredients = []
re_numbers = re.compile(r'-?\d+')
re_properties = re.compile(r'[A-Za-z]+')

with open('inputs/15.in') as f:
    # Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5

    for line in f.readlines():
        # properties = re_properties.findall(line)
        # name = properties.pop(0)
        values = list(map(int, re_numbers.findall(line)))
        # ingredients[name] = {k: v for k, v in zip(properties, values)}
        ingredients.append(values)


def get_all_1():
    score = []
    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                l = 100 - i - j - k
                score.append(get_score((i, j, k, l)))

    print('#1:', max(score))


def get_score(amount: tuple) -> int:
    total = 1
    for ing, am in list(zip(ingredients.values(), amount)):
        per_ing = 0
        print(ing, am)
        for val in list(ing.values())[:-1]:
            if val < 0:
                val = 0

            per_ing += val * am

        total *= per_ing

    return total


def mixtures(n, total):
    start = total if n == 1 else 0

    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures(n - 1, left):
                yield [i] + y
        else:
            yield [i]


def score(recipe, max_calories=0):
    proportions = [map(lambda x: x * mul, props) for props, mul in zip(ingredients, recipe)]
    dough = reduce(lambda a, b: list(map(sum, zip(a, b))), proportions)
    calories = dough.pop()
    result = reduce(lambda a, b: a*b, map(lambda x: max(x, 0), dough))

    return 0 if max_calories and calories > max_calories else result



if __name__ == '__main__':
    print(ingredients)
    recipes = mixtures(len(ingredients), 100)
    print(max(map(score, recipes)))

# print max(map(lambda r: score(r, 500), recipes))
