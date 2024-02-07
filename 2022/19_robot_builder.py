import re
from my_utils import get_data

#
# DOESN'T NOT WORK AT ALL...
#
# https://adventofcode.com/2022/day/19


class RobotBuilder:

    def __init__(self, blueprints_file) -> None:
        self.blueprints_file = blueprints_file
        self.minutes = 24
        self.time_remains = self.minutes
        self.RESOURCES_START = {
            'geode': 0,
            'obsidian': 0,
            'clay': 0,
            'ore': 0,
        }
        self.ROBOTS_START = self.RESOURCES_START.copy()
        self.ROBOTS_START['ore'] = 1
        self.ROBOTS = {}
        self.RESOURCES = {}

    def parse_blueprints(self) -> dict:
        blueprints = {}

        for line in get_data(self.blueprints_file):
            bp = list(map(int, re.findall(r'\d+', line)))
            # 0: blueprint number
            # 1: Each ore robot costs 4 ore
            # 2: Each clay robot costs 2 ore
            # 3,4: Each obsidian robot costs 3 ore and 14 clay
            # 5,6: Each geode robot costs 2 ore and 7 obsidian
            blueprints[bp[0]] = {
                'geode': {
                    'ore': bp[5],
                    'obsidian': bp[6],
                },
                'obsidian': {
                    'ore': bp[3],
                    'clay': bp[4],
                },
                'clay': {
                    'ore': bp[2],
                },
                'ore': {
                    'ore': bp[1],
                }
            }

        return blueprints

    def build(self, robot_type: str, blueprint: dict) -> None:
        enough_res = [self.RESOURCES[res] >= amount\
                      for res, amount in blueprint[robot_type].items()]

        if all(enough_res):
            self.ROBOTS[robot_type] += 1

            for res, amount in blueprint[robot_type].items():
                self.RESOURCES[res] -= amount

    def harvest(self) -> None:
        for res_type, amount in self.ROBOTS.items():
            self.RESOURCES[res_type] += amount

    def run(self, blueprint: dict) -> None:
        bid, bp = blueprint
        self.ROBOTS = self.ROBOTS_START.copy()
        self.RESOURCES = self.RESOURCES_START.copy()

        for _ in range(self.minutes):
            self.time_remains -= 1
            self.harvest()
            for robot_type in self.ROBOTS.keys():
                # TODO
                if robot_type in ('geodes', 'obsidian'):
                    self.build(robot_type, bp)

        print(f'#{bid}')
        print('Robots:', self.ROBOTS)
        print('Resources:', self.RESOURCES)

        return self.RESOURCES['geode'] * bid

    def evaluate_score(self) -> None:
        score = 0
        for bp in self.parse_blueprints().items():
            score += self.run(bp)

        print(f'Score #1: {score}')


if __name__ == '__main__':
    RobotBuilder('inputs/19_example.in').evaluate_score()
    # RobotBuilder('inputs/19.in').evaluate_score()
