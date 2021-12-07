from unittest import TestCase
from year_2021.ex_12_05_vectors.solution import Point, Vector, Board

class Test(TestCase):

    def test_has_point(self):
        self.assertTrue(Vector(Point(1, 1), Point(1, 3)).has_point(Point(1, 2)))
        self.assertFalse(Vector(Point(1, 1), Point(1, 3)).has_point(Point(2, 2)))
        self.assertTrue(Vector(Point(1, 1), Point(3, 3)).has_point(Point(2, 2)))
        self.assertTrue(Vector(Point(0, 0), Point(2, 4)).has_point(Point(1, 2)))
        self.assertTrue(Vector(Point(0, 0), Point(8, 8)).has_point(Point(2, 2)))

    def test_horvertical(self):
        self.assertTrue(Vector(Point(0, 0), Point(0, 2)).horvertical())
        self.assertFalse(Vector(Point(0, 0), Point(1, 2)).horvertical())

    def test_diagonal(self):
        self.assertTrue(Vector(Point(0, 0), Point(2, 2)).diagonal())
        self.assertTrue(Vector(Point(2, 2), Point(1, 1)).diagonal())
        self.assertTrue(Vector(Point(0, 1), Point(1, 0)).diagonal())
        self.assertTrue(Vector(Point(2, 0), Point(0, 2)).diagonal())
        self.assertTrue(Vector(Point(2, 2), Point(3, 1)).diagonal())
        self.assertFalse(Vector(Point(0, 0), Point(1, 2)).diagonal())

    def test_wraps(self):
        self.assertTrue(Vector(Point(0, 0), Point(2, 4)).wraps(Point(1, 2)))
        self.assertFalse(Vector(Point(3, 3), Point(3, 4)).wraps(Point(1, 2)))

    def test_board_add(self):
        board = Board(3, 3)
        board.add(Vector(Point(0, 0), Point(0, 2)))
        board.add(Vector(Point(0, 0), Point(2, 2)))

        self.assertEquals(board.cells,  [[2, 0, 0], [1, 1, 0], [1, 0, 1]])