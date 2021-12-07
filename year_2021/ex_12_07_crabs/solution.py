from typing import List
from dataclasses import dataclass
from statistics import median


class Crabs:
    positions: List[int]

    def __init__(self, positions):
        self.positions = positions

    def best_target(self):
        best_pos = 0
        best_fuel = None
        for pos in range(min(self.positions), max(self.positions)):
            fuel = self.fuel_consumtion_to(pos)
            if not best_fuel or best_fuel > fuel:
                best_fuel = fuel
                best_pos = pos
        return best_pos

    def fuel_consumtion_to(self, t):
        s = 0
        for pos in self.positions:
            s += self._crab_distance(pos, t)
        return s

    def _crab_distance(self, a, t):
        return (abs(a - t) + 1) * abs(a - t) / 2

    def __repr__(self) -> str:
        return f"{self.positions}"


if __name__ == "__main__":
    with open("year_2021/ex_12_07_crabs/input.txt") as fp:
        input = [line.strip() for line in fp.readlines()]

    crabs = Crabs([int(n) for n in input[0].split(',')])
    print(crabs.best_target())
    print(crabs.fuel_consumtion_to(crabs.best_target()))