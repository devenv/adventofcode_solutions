from unittest import TestCase
from ..solution import Basin, Heightmap, Point

class Test(TestCase):

    def test_lowpoints(self):
        self.assertEquals(Heightmap([[1, 2, 2], [2, 2, 2], [2, 2, 2]]).lowpoints(), [Point(0, 0, 1)])
        self.assertEquals(Heightmap([[2, 1, 2], [2, 2, 2], [2, 2, 2]]).lowpoints(), [Point(0, 1, 1)])
        self.assertEquals(Heightmap([[2, 2, 2], [2, 1, 2], [2, 2, 2]]).lowpoints(), [Point(1, 1, 1)])
        self.assertEquals(Heightmap([[2, 2, 2], [1, 2, 1], [2, 2, 2]]).lowpoints(), [Point(1, 0, 1), Point(1, 2, 1)])

    def test_get_neighbors(self):
        self.assertEquals(Heightmap([[1, 2, 3], [4, 5, 6], [7, 8, 9]])._get_neighbors(0, 0), [2, 4])
        self.assertEquals(Heightmap([[1, 2, 3], [4, 5, 6], [7, 8, 9]])._get_neighbors(0, 1), [1, 3, 5])
        self.assertEquals(Heightmap([[1, 2, 3], [4, 5, 6], [7, 8, 9]])._get_neighbors(0, 2), [2, 6])
        self.assertEquals(Heightmap([[1, 2, 3], [4, 5, 6], [7, 8, 9]])._get_neighbors(1, 1), [4, 6, 2, 8])
        self.assertEquals(Heightmap([[1, 2, 3], [4, 5, 6], [7, 8, 9]])._get_neighbors(2, 2), [8, 6])

    def test_get_basin(self):
        self.assertEquals(Heightmap([[9, 2, 9], [2, 2, 2], [9, 2, 9]]).get_basin(1, 1), [[0, 1, 0], [1, 1, 1], [0, 1, 0]])
        self.assertEquals(Heightmap([[9, 9, 9], [9, 2, 9], [9, 2, 9]]).get_basin(1, 1), [[0, 0, 0], [0, 1, 0], [0, 1, 0]])

    def test_get_basin(self):
        self.assertEquals(Basin([[1, 1, 0], [1, 1, 0], [0, 0, 0]]).get_size(), 4)