from dataclasses import dataclass
from typing import List

from year_2021.utils.input import read_input


@dataclass
class Octopus:
    power: int

    def __init__(self, power):
        self.power = power
        self.flashed = False
        self.processed = False

    def tick(self):
        if not self.flashed:
            self.power += 1
            if self.power > 9:
                self.power = 0
                self.flashed = True
                return True
        return False

@dataclass
class School:
    octopuses: List[List[Octopus]] = None
    flashes: int = 0

    def load(self, input):
        self.octopuses = [[Octopus(int(power)) for power in line] for line in input]
        self.size = len(self.octopuses) * len(self.octopuses[0])
        return self

    def tick(self):
        old_flashes = self.flashes
        # reset
        for x in range(len(self.octopuses)):
            for y in range(len(self.octopuses[0])):
                self.octopuses[x][y].flashed = False
                self.octopuses[x][y].processed = False

        # tick everyone
        for x in range(len(self.octopuses)):
            for y in range(len(self.octopuses[0])):
                self.tick_octopus(x, y)

        # tick flashed neighbors
        flashed_not_processed = True
        while flashed_not_processed:
            flashed_not_processed = False
            for x in range(len(self.octopuses)):
                for y in range(len(self.octopuses[0])):
                    if self.octopuses[x][y].flashed and not self.octopuses[x][y].processed:
                        flashed_not_processed = True
                        self.octopuses[x][y].processed = True
                        self.tick_octopus(x - 1, y - 1)
                        self.tick_octopus(x - 1, y)
                        self.tick_octopus(x - 1, y + 1)
                        self.tick_octopus(x, y - 1)
                        self.tick_octopus(x, y + 1)
                        self.tick_octopus(x + 1, y - 1)
                        self.tick_octopus(x + 1, y)
                        self.tick_octopus(x + 1, y + 1)
        
        # count flashes
        for x in range(len(self.octopuses)):
            for y in range(len(self.octopuses[0])):
                if self.octopuses[x][y].flashed:
                    self.flashes += 1
        
        return self.flashes - old_flashes == self.size

    def tick_octopus(self, x, y):
        if self._legit_octupus(x, y):
            return self.octopuses[x][y].tick()
        return False

    def _legit_octupus(self, x, y):
        max_x = len(self.octopuses) - 1
        max_y = len(self.octopuses[0]) - 1
        return x >= 0 and x <= max_x and y >= 0 and y <= max_y


if __name__ == "__main__":
    input = read_input()

    school = School()
    school.load(input)
    for _ in range(100):
        school.tick()
    print(school.flashes)

    school = School()
    school.load(input)
    first_flash = 0
    while True:
        first_flash += 1
        if school.tick():
            print(first_flash)
            break