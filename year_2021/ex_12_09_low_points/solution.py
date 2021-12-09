from dataclasses import dataclass
import math
from typing import List

from year_2021.utils.input import read_input


@dataclass
class Point:
    x: int
    y: int
    value: int

@dataclass
class Basin:
    heightmap: List[List]

    def get_size(self):
        return sum(n == 1 for line in self.heightmap for n in line)

class Heightmap:
    heightmap: List[List]

    def __init__(self, heigtmap: str):
        self.heightmap = heigtmap

    def lowpoints(self):
        lowpoints = []
        for x in range(0, len(self.heightmap)):
            for y in range(0, len(self.heightmap[0])):
                if self._is_lowpoint(x, y):
                    lowpoints.append(Point(x, y, self.heightmap[x][y]))
        return lowpoints

    def get_basin(self, x, y):
        basin = self._get_basin(x, y, [[-1] * len(self.heightmap[0]) for _ in range(len(self.heightmap))])
        for x in range(len(basin)):
            for y in range(len(basin[0])):
                if basin[x][y] == -1:
                    basin[x][y] = 0
        return Basin(basin)

    def _get_basin(self, x, y, basin):
        if not self._legit_point(x, y) or basin[x][y] != -1:
            return
        if self.heightmap[x][y] == 9:
            basin[x][y] = 0
            return
        basin[x][y] = 1
        self._get_basin(x - 1, y, basin)
        self._get_basin(x + 1, y, basin)
        self._get_basin(x, y - 1, basin)
        self._get_basin(x, y + 1, basin)
        
        return basin
        
    def _is_lowpoint(self, x, y):
        value = self.heightmap[x][y]
        res = all(value < neighbor for neighbor in self._get_neighbors(x, y))
        return res

    def _get_neighbors(self, x, y):
        return list(filter(lambda x: x is not None, [
            self._get(x, y - 1),
            self._get(x, y + 1),
            self._get(x - 1, y),
            self._get(x + 1, y),
        ]))

    def _get(self, x, y):
        if not self._legit_point(x, y):
            return None
        return self.heightmap[x][y]

    def _legit_point(self, x, y):
        max_x = len(self.heightmap) - 1
        max_y = len(self.heightmap[0]) - 1
        return x >= 0 and x <= max_x and y >= 0 and y <= max_y

    def __repr__(self) -> str:
        return f"{self.heightmap}"


if __name__ == "__main__":
    input = read_input()
    digits = [[int(digit) for digit in line] for line in input]
    heightmap = Heightmap(digits)
    lowpoints = heightmap.lowpoints()
    print(sum(point.value + 1 for point in lowpoints))

    basins = []
    for lowpoint in lowpoints:
        basins.append(heightmap.get_basin(lowpoint.x, lowpoint.y))
    sizes = [basin.get_size() for basin in basins]
    top_3_sizes = sorted(sizes)[-3:]
    print(math.prod(top_3_sizes))