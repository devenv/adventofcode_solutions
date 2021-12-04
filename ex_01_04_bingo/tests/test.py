from unittest import TestCase
from ex_01_04_bingo.solution import Board, Cell, Loader

class Test(TestCase):

    def test_no_bingo(self):
        board = Board([
            [Cell(1), Cell(2, True)],
            [Cell(1, True), Cell(2)],
        ])
        self.assertFalse(board.is_bingo())

    def test_vertical_bingo(self):
        board = Board([
            [Cell(1, True), Cell(2)],
            [Cell(1, True), Cell(2)],
        ])
        self.assertTrue(board.is_bingo())

    def test_horizontal_bingo(self):
        board = Board([
            [Cell(1, True), Cell(2, True)],
            [Cell(1), Cell(2)],
        ])
        self.assertTrue(board.is_bingo())

    def test_mark(self):
        board = Board([
            [Cell(1), Cell(2)],
            [Cell(2), Cell(3)],
        ])
        board.mark(2)
        self.assertEqual(board, Board([
            [Cell(1), Cell(2, True)],
            [Cell(2, True), Cell(3)],
        ]))

    def test_numbers(self):
        input = "1,2,3,4"
        self.assertEqual(Loader().load_numbers(input), [1, 2, 3, 4])

    def test_load_boards(self):
        input = ["1 2", "2 3", "", "3 4", "4 5"]
        self.assertEqual(Loader().load_boards(input), [
            Board([
                [Cell(1), Cell(2)],
                [Cell(2), Cell(3)],
                ]),
            Board([
                [Cell(3), Cell(4)],
                [Cell(4), Cell(5)],
                ]),
        ])
