# To continue, please consult the code grid in the manual.
# Enter the code at row 2981, column 3075.

#   |  1   2   3   4   5   6
#---+---+---+---+---+---+---+
# 1 |  1   3   6  10  15  21
# 2 |  2   5   9  14  20
# 3 |  4   8  13  19
# 4 |  7  12  18
# 5 | 11  17
# 6 | 16

FIRST_VAL = 20151125
MULTIPLIER = 252533
DIVIDER = 33554393
MY_ROW = 2981
MY_COL = 3075

val = FIRST_VAL
row = col = max_row = 1

for _ in range(100_000_000):
    val = (val * MULTIPLIER) % DIVIDER

    if row == 1:
        max_row += 1
        row = max_row
        col = 1
    else:
        row -= 1
        col += 1

    if row == MY_ROW and col == MY_COL:
        print(f'row: {MY_COL} col: {MY_ROW} :: {val}')
        break
