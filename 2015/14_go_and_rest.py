import re
from copy import deepcopy
from my_utils import get_data


def go(data: list, sec: int) -> None:
    riders = {}
    nums = re.compile(r'\d+')

    for line in data:
        name = line.split()[0]
        speed, time, rest_time = map(int, nums.findall(line))

        distance = 0
        time_can_go = time
        time_must_rest = rest_time
        for _ in range(sec):

            if time_can_go > 0:
                distance += speed
                time_can_go -= 1

                if time_can_go == 0:
                    time_must_rest = rest_time
                    continue

            if time_must_rest > 0:
                time_must_rest -= 1

                if time_must_rest == 0:
                    time_can_go = time

        riders[name] = distance

    rider, dist = max(riders.items(), key=lambda x: x[1])
    print(f'#1 Winner is {rider} with {dist} Km')


def go_2(data: list, sec: int) -> None:
    riders = {}
    for line in data:
        name = line.split()[0]
        speed, time, rest_time = map(int, re.findall(r'\d+', line))
        riders[name] = {
            'speed': speed,
            'time': time,
            'rest_time': rest_time,
            'distance': 0,
            'points': 0,
        }

    riders_origin = deepcopy(riders)

    i = 0
    while i < sec:
        for name in riders.keys():
            if riders[name]['time'] > 0:
                riders[name]['distance'] += riders[name]['speed']
                riders[name]['time'] -= 1

                if riders[name]['time'] == 0:
                    riders[name]['rest_time'] = riders_origin[name]['rest_time']
                    continue

            if riders[name]['rest_time'] > 0:
                riders[name]['rest_time'] -= 1

                if riders[name]['rest_time'] == 0:
                    riders[name]['time'] = riders_origin[name]['time']

        # TODO refactor - use cycle
        fastest = max(riders.items(), key=lambda x: x[1]['distance'])[0]

        riders[fastest]['points'] += 1
        riders[fastest]['distance'] += 1
        i += 1

    rider, attrs = max(riders.items(), key=lambda x: x[1]['distance'])
    print(f"#2 Winner is {rider} with {attrs['points']} points")


if __name__ == '__main__':
    example = [
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
    ]
    data = get_data('inputs/14.in')
    # go(example, sec=1000)
    # go(data, sec=2503)
    go_2(example, sec=1000)
    # go_2(data, sec=2503)
