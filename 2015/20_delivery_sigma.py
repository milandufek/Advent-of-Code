from sympy.ntheory import divisors, divisor_sigma


TARGET = 29_000_000


def solve_1_sigma():
    for house in range(1, TARGET):
        presents = divisor_sigma(house) * 10

        if presents >= TARGET:
            print('#1:', house)
            break


def solve_1():
    for house in range(1, TARGET):
        presents = divisors(house)

        if sum(presents) * 10 >= TARGET:
            print('#1:', house)
            break


def solve_2():
    for house in range(1, TARGET):
        presents = divisors(house)

        if sum(p for p in presents if house / p <= 50) * 11 >= TARGET:
            print('#2:', house)
            break


if __name__ == '__main__':
    # solve_1_sigma()
    solve_1()
    solve_2()
