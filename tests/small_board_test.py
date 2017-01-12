from unittest import TestCase
from board import Board


class Board1x1Test(TestCase):
    size = [1, 1]

    def test_1x1_black(self):
        horizontal_data = [[1]]
        vertical_data = [[1]]
        cut = Board(self.size, horizontal_data, vertical_data)

        cut.mark_horizontal_intersections()
        self.assertEqual(cut.board[0][0], cut.BLACK)

    def test_1x1_white(self):
        horizontal_data = [[]]
        vertical_data = [[]]
        cut = Board(self.size, horizontal_data, vertical_data)

        with self.assertRaises(LookupError):
            cut.mark_horizontal_intersections()


class Board2x2Test(TestCase):
    size = [2, 2]

    def test_2x2_black(self):
        horizontal_data = [[2], [2]]
        vertical_data = [[2], [2]]
        cut = Board(self.size, horizontal_data, vertical_data)

        cut.mark_horizontal_intersections()
        self.assertEqual(cut.board[0][0], cut.BLACK)
        self.assertEqual(cut.board[0][1], cut.BLACK)
        self.assertEqual(cut.board[1][0], cut.BLACK)
        self.assertEqual(cut.board[1][1], cut.BLACK)

    def test_2x2_diagonal(self):
        horizontal_data = [[1], [1]]
        vertical_data = [[1], [1]]
        cut = Board(self.size, horizontal_data, vertical_data)

        cut.mark_horizontal_intersections()
        self.assertEqual(cut.board[0][0], cut.BLACK)
        self.assertEqual(cut.board[0][1], cut.WHITE)
        self.assertEqual(cut.board[1][0], cut.WHITE)
        self.assertEqual(cut.board[1][1], cut.BLACK)
