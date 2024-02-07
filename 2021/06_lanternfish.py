from collections import Counter, deque

# Initial state: 3,4,3,1,2
# After  1 day:  2,3,2,0,1
# After  2 days: 1,2,1,6,0,8
# After  3 days: 0,1,0,5,6,7,8
# After  4 days: 6,0,6,4,5,6,7,8,8
# After  5 days: 5,6,5,3,4,5,6,7,7,8
# After  6 days: 4,5,4,2,3,4,5,6,6,7
# After  7 days: 3,4,3,1,2,3,4,5,5,6
# After  8 days: 2,3,2,0,1,2,3,4,4,5
# After  9 days: 1,2,1,6,0,1,2,3,3,4,8
# After 10 days: 0,1,0,5,6,0,1,2,2,3,7,8
# After 11 days: 6,0,6,4,5,6,0,1,1,2,6,7,8,8,8
# After 12 days: 5,6,5,3,4,5,6,0,0,1,5,6,7,7,7,8,8
# After 13 days: 4,5,4,2,3,4,5,6,6,0,4,5,6,6,6,7,7,8,8
# After 14 days: 3,4,3,1,2,3,4,5,5,6,3,4,5,5,5,6,6,7,7,8
# After 15 days: 2,3,2,0,1,2,3,4,4,5,2,3,4,4,4,5,5,6,6,7
# After 16 days: 1,2,1,6,0,1,2,3,3,4,1,2,3,3,3,4,4,5,5,6,8
# After 17 days: 0,1,0,5,6,0,1,2,2,3,0,1,2,2,2,3,3,4,4,5,7,8
# After 18 days: 6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8

example = [3,4,3,1,2]
with open('inputs/06.in') as f:
    data = list(map(int, f.read().strip().split(',')))


def reborn(fishes: list, days: int) -> None:
    q = deque(Counter(fishes)[i] for i in range(9))
    for _ in range(days):
        q.rotate(-1)
        q[6] += q[8]

    print(f'Sum ({days} days): {sum(q)}')


def reborn_no_import(fishes: list, days: int) -> None:
    q = [fishes.count(i) for i in range(9)]
    for _ in range(days):
        zero = q.pop(0)
        q[6] += zero
        q.append(zero)

    print(f'Sum ({days} days): {sum(q)}')


if __name__ == '__main__':
    # reborn(example, days=80)
    # reborn(example, days=256)
    print('Part #1')
    reborn(data, days=80)
    print('Part #2')
    reborn(data, days=256)
    reborn_no_import(data, days=256)
    # reborn(data, days=36500)
