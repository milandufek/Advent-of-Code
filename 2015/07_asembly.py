import sympy
from utils import get_data


DATA = get_data('inputs/07.in')
vars = {}

for line in DATA:
    item = line.split()

    if len(item) == 3:
        src, _, target = item
        if src.isdigit():
            vars[target] = sympy.Integer(int(src))
        elif val := vars.get(src):
            print(src, val)
            vars[target] = sympy.Integer(int(val))
        else:
            vars[target] = sympy.Symbol(src)
    elif len(item) == 4:
        _, src, _, target = item

        if src.isdigit():
            vars[target] = ~sympy.Symbol(src)
        elif val := vars.get(src):
            vars[target] = ~sympy.Integer(int(val))
        else:
            vars[target] = sympy.Symbol(src)
    elif len(item) == 5:
        a, op, b, _, target = item

        if val_a := vars.get(a):
            a = sympy.Symbol(val_a)
        elif a.isdigit():
            a = sympy.Integer(int(a))
        else:
            vars[target] = sympy.Symbol(a)
            continue

        if val_b := vars.get(b):
            b = sympy.Integer(int(val_b))
        elif b.isdigit():
            b = sympy.Integer(int(b))
        else:
            vars[target] = sympy.Symbol(b)
            continue

        # print(f"{' '.join(item)} {a}/{vars.get(a)} {b}/{vars.get(b)}")
        if op == 'AND':
            val = a & b
        elif op == 'OR':
            val = a | b
        elif op == 'LSHIFT':
            val = a << b
        elif op == 'RSHIFT':
            val = a >> b
        else:
            raise Exception(f"Unknown operator '{op}'")

        vars[target] = val
    else:
        raise Exception(f"Unknown entry '{line}'")

print(f"a = {sympy.solve(vars['a'])}")
