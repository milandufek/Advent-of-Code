import re
from itertools import product


weapons = {
    'Dagger': {
        'cost': 8,
        'damage': 4,
        'armor': 0,
    },
    'Shortsword': {
        'cost': 10,
        'damage': 5,
        'armor': 0,
    },
    'Warhammer': {
        'cost': 25,
        'damage': 6,
        'armor': 0,
    },
    'Longsword': {
        'cost': 40,
        'damage': 7,
        'armor': 0,
    },
    'Greataxe': {
        'cost': 74,
        'damage': 8,
        'armor': 0,
    },
}

armor = {
    'None': {
        'cost': 0,
        'damage': 0,
        'armor': 0,
    },
    'Leather': {
        'cost': 13,
        'damage': 0,
        'armor': 1,
    },
    'Chainmail': {
        'cost': 31,
        'damage': 0,
        'armor': 2,
    },
    'Splintmail': {
        'cost': 53,
        'damage': 0,
        'armor': 3,
    },
    'Bandedmail': {
        'cost': 75,
        'damage': 0,
        'armor': 4,
    },
    'Platemail': {
        'cost': 102,
        'damage': 0,
        'armor': 5,
    },
}

rings_damage = {
    'None': {
        'cost': 0,
        'damage': 0,
        'armor': 0,
    },
    'Damage +1': {
        'cost': 25,
        'damage': 1,
        'armor': 0,
    },
    'Damage +2': {
        'cost': 50,
        'damage': 2,
        'armor': 0,
    },
    'Damage +3': {
        'cost': 100,
        'damage': 3,
        'armor': 0,
    },
}

rings_armor = {
    'None': {
        'cost': 0,
        'damage': 0,
        'armor': 0,
    },
    'Defense +1': {
        'cost': 20,
        'damage': 0,
        'armor': 1,
    },
    'Defense +2': {
        'cost': 40,
        'damage': 0,
        'armor': 2,
    },
    'Defense +3': {
        'cost': 80,
        'damage': 0,
        'armor': 3,
    },
}

player = {
    'hits': 100,
    'damage': 0,
    'armor': 0,
}

with open('inputs/21.in') as f:
    boss = dict(zip(
        ('hits', 'damage', 'armor'),
        [int(re.findall(r'(\d+)', line)[0]) for line in f.readlines()]))


def get_gold(items):
    get_cost = lambda x: x[0][x[1]]['cost']

    return sum(map(get_cost, zip(
        (weapons, armor, rings_damage, rings_armor), items)))


def get_stats(items):
    stats = list(zip((weapons, armor, rings_damage, rings_armor), items))

    get_armor = lambda x: x[0][x[1]]['armor']
    stat_armor = sum(map(get_armor, stats))

    get_damage = lambda x: x[0][x[1]]['damage']
    stat_damage = sum(map(get_damage, stats))

    return stat_damage, stat_armor


def simulate_game(items):
    gold = get_gold(items)
    p_damage, p_armor = get_stats(items)

    p_hits = player['hits']
    p_damage += player['damage']
    p_armor += player['armor']

    b_hits = boss['hits']
    p_hurt = boss['damage'] - p_armor

    if p_hurt <= 0:
        p_hurt = 1

    b_hurt = p_damage - boss['armor']

    if b_hurt <= 0:
        b_hurt = 1

    for _ in range(player['hits']):
        b_hits -= b_hurt

        if b_hits <= 0:
            return True, gold

        p_hits -= p_hurt

        if p_hits <= 0:
            return False, gold


def main():
    items = product(
        weapons.keys(),
        armor.keys(),
        rings_damage.keys(),
        rings_armor.keys()
    )

    games = [simulate_game(i) for i in items]

    print('#1:', min([gold for outcome, gold in games if outcome is True]))
    print('#2:', max([gold for outcome, gold in games if outcome is False]))


if __name__ == '__main__':
    main()
