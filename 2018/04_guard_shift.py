from collections import defaultdict
from datetime import datetime
from my_utils import get_data


# https://adventofcode.com/2018/day/4


def solve(data: list[str], part: int = 1) -> int:
    data.sort()
    sleep_times = defaultdict(int)
    minutes_counter = defaultdict(lambda: defaultdict(int))

    for line in data:
        time = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
        action, *args = line.split()[2:]

        if action == 'Guard':
            _id = int(args[0].replace('#', ''))
            time_asleep, time_awake = None, None
        elif action == 'falls':
            time_asleep = time
        elif action == 'wakes':
            time_awake = time
            sleep_times[_id] += (time_awake - time_asleep).seconds // 60
            for minute in range(time_asleep.minute, time_awake.minute):
                minutes_counter[_id][minute] += 1

    if part == 1:
        guard_number, times = max(sleep_times.items(), key=lambda x: x[1])
        best_minute, _ = max(minutes_counter[guard_number].items(), key=lambda x: x[1])
    else:
        guard_number, times = max(minutes_counter.items(), key=lambda x: max(x[1].values()))
        best_minute, _ = max(times.items(), key=lambda x: x[1])

    return guard_number * best_minute


if __name__ == '__main__':
    data_input = get_data('inputs/04.in')
    print(f'Part 1: {solve(data_input)}')
    print(f'Part 2: {solve(data_input, 2)}')
