from dataclasses import dataclass
from math import sqrt

from year_2021.utils.input import read_input


@dataclass
class Point:
    x: int
    y: int

    def __repr__(self) -> str:
        return f"{self.x},{self.y}"

@dataclass
class Vector:
    p1: Point
    p2: Point

    @classmethod
    def from_line(cls, line):
        p1, _, p2 = line.split(' ')
        p1_x, p1_y = p1.split(',')
        p2_x, p2_y = p2.split(',')
        return Vector(Point(int(p1_x), int(p1_y)), Point(int(p2_x), int(p2_y)))

    def wraps(self, point):
        # purely for performance improvement
        return (point.x >= self.p1.x and point.x <= self.p2.x or point.x >= self.p2.x and point.x <= self.p1.x) and (point.y >= self.p1.y and point.y <= self.p2.y or point.y >= self.p2.y and point.y <= self.p1.y)

    def horvertical(self):
        return self.p1.x == self.p2.x or self.p1.y == self.p2.y

    def diagonal(self):
        return (self.p2.x - self.p1.x == self.p2.y - self.p1.y) or (self.p1.x + self.p1.y == self.p2.x + self.p2.y)

    def has_point(self, point):
        # slower but more generic than needed in the exercise
        return abs(self._distance(self.p1, point) + self._distance(point, self.p2) - self._distance(self.p1, self.p2)) < 0.00001

    def _distance(self, a, b):
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def __repr__(self) -> str:
        return f"{repr(self.p1)} -> {repr(self.p2)}"

class Board:
    cells = None
    def __init__(self, x, y):
        self.cells = [[0] * x for y in range(0, y)]

    def __repr__(self) -> str:
        return repr(self.cells)

    def add(self, vector: Vector):
        for x in range(0, len(self.cells[0])):
            for y in range(0, len(self.cells)):
                p = Point(x, y)
                if vector.wraps(p) and vector.has_point(p):
                    self.cells[y][x] += 1


if __name__ == "__main__":
    input = read_input()
    all_vectors = [Vector.from_line(line) for line in input]

    vectors = [vector for vector in all_vectors if vector.horvertical()]
    max_x = max(max(vector.p1.x, vector.p2.y) for vector in vectors)
    max_y = max(max(vector.p1.y, vector.p2.y) for vector in vectors)

    board = Board(max_x + 1, max_y + 1)
    length = len(vectors)
    n = 0
    for vector in vectors:
        board.add(vector)
        n += 1
        print(f"{n / length * 100:.2f}%")
    crossings = 0
    for line in board.cells:
        for cell in line:
            if cell > 1:
                crossings += 1
    print(crossings)


    vectors = [vector for vector in all_vectors if vector.diagonal() or vector.horvertical()]
    max_x = max(max(vector.p1.x, vector.p2.y) for vector in vectors)
    max_y = max(max(vector.p1.y, vector.p2.y) for vector in vectors)

    board = Board(max_x + 1, max_y + 1)
    n = 0
    length = len(vectors)
    for vector in vectors:
        board.add(vector)
        n += 1
        print(f"{n / length * 100:.2f}%")
    crossings = 0
    for line in board.cells:
        for cell in line:
            if cell > 1:
                crossings += 1
    print(crossings)