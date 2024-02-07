import json


INPUT: str = ''
with open('inputs/12.in') as f:
    INPUT = json.loads(f.read())


sum = 0

def get_val(item: object) -> None:
    global sum
    if isinstance(item, int):
        sum += item
    elif isinstance(item, dict):
        items = item.items()
        for k, v in items:
            if k == 'red' or v == 'red':
                return
        for _, v in items:
            get_val(v)
    elif isinstance(item, list):
        for val in item:
            get_val(val)


if __name__ == '__main__':
    get_val(INPUT)
    print(f'Sum: {sum}')
