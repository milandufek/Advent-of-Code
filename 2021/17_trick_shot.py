import re
from typing import Generator


# https://adventofcode.com/2021/day/17


class Shooter:

    def __init__(self, target_coordinates: str) -> None:
        min_x, max_x, min_y, max_y = map(int, re.findall(r'-?\d+', target_coordinates.strip()))
        self.target_min_x = min_x
        self.target_max_x = max_x
        self.target_min_y = min_y
        self.target_max_y = max_y
        self.shooter = (0, 0)
        self.target_area = self.get_target_area()

    def get_target_area(self) -> set[tuple[int, int]]:
        return {(x, y)
                for x in range(self.target_min_x, self.target_max_x + 1)
                for y in range(self.target_min_y, self.target_max_y + 1)}

    def shoot_get_max_y(self, velocity: tuple[int, int]) -> int:
        x, y = self.shooter
        vx, vy = velocity
        max_y = 0
        while y > self.target_min_y and x < self.target_max_x:
            x += vx
            if vx > 0:
                vx -= 1
            y += vy
            vy -= 1
            max_y = max(max_y, y)

            if (x, y) in self.target_area:
                return max_y

        return -1

    def shoot(self, velocity: tuple[int, int]) -> bool:
        x, y = self.shooter
        vx, vy = velocity
        while y > self.target_min_y and x < self.target_max_x:
            x += vx
            if vx > 0:
                vx -= 1
            y += vy
            vy -= 1

            if (x, y) in self.target_area:
                return True

        return False

    def get_velocities(self) -> Generator[tuple[int, int], None, None]:
        return ((x, y)
                for x in range(self.target_max_x + 1)
                for y in range(self.target_min_y, 200))  # might need to increase the range for different inputs

    def solve_1(self) -> int:
        return max(self.shoot_get_max_y(velocity) for velocity in self.get_velocities())

    def solve_2(self) -> None:
        return sum(self.shoot(velocity) for velocity in self.get_velocities())


def test_example_1() -> None:
    data = 'target area: x=20..30, y=-10..-5'
    assert Shooter(data).solve_1() == 45

def test_example_2() -> None:
    data = 'target area: x=20..30, y=-10..-5'
    assert Shooter(data).solve_2() == 112


if __name__ == '__main__':
    with open('inputs/17.in') as f:
        data = f.read().strip()
    print('#1:', Shooter(data).solve_1())
    print('#2:', Shooter(data).solve_2())
