from unittest import TestCase
from board import Board, Direction


class BoardRowTest(TestCase):
    def assertRowEqual(self, board, fields):
        for index, field in enumerate(fields):
            self.assertEqual(field, board.board[0][index])


class Board5x1FullMatchTest(BoardRowTest):
    size = [5, 1]

    def test_1_1_1(self):
        horizontal_data = [[1, 1, 1]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.BLACK, cut.WHITE, cut.BLACK, cut.WHITE, cut.BLACK])

    def test_3_1(self):
        horizontal_data = [[3, 1]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.BLACK, cut.BLACK, cut.BLACK, cut.WHITE, cut.BLACK])

    def test_1_3(self):
        horizontal_data = [[1, 3]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.BLACK, cut.WHITE, cut.BLACK, cut.BLACK, cut.BLACK])

    def test_2_2(self):
        horizontal_data = [[2, 2]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.BLACK, cut.BLACK, cut.WHITE, cut.BLACK, cut.BLACK])

    def test_5(self):
        horizontal_data = [[5]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.BLACK, cut.BLACK, cut.BLACK, cut.BLACK, cut.BLACK])


class Board5x1NotFullTest(BoardRowTest):
    size = [5, 1]

    def test_4(self):
        horizontal_data = [[4]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.BLACK, cut.BLACK, cut.BLACK, cut.UNKNOWN])

    def test_3(self):
        horizontal_data = [[3]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.UNKNOWN, cut.BLACK, cut.UNKNOWN, cut.UNKNOWN])

    def test_2(self):
        horizontal_data = [[2]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN])

    def test_2_1(self):
        horizontal_data = [[2, 1]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.BLACK, cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN])

    def test_1_2(self):
        horizontal_data = [[1, 2]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN, cut.BLACK, cut.UNKNOWN])


class Board7x1NotFullTest(BoardRowTest):
    size = [7, 1]

    def test_4(self):
        horizontal_data = [[4]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN, cut.BLACK, cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN])

    def test_3_1(self):
        horizontal_data = [[3, 1]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.UNKNOWN, cut.BLACK, cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN])

    def test_1_3(self):
        horizontal_data = [[1, 3]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN, cut.UNKNOWN, cut.BLACK, cut.UNKNOWN, cut.UNKNOWN])

    def test_3_2(self):
        horizontal_data = [[3, 2]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.BLACK, cut.BLACK, cut.UNKNOWN, cut.UNKNOWN, cut.BLACK, cut.UNKNOWN])

    def test_2_3(self):
        horizontal_data = [[2, 3]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN, cut.BLACK, cut.UNKNOWN, cut.UNKNOWN, cut.BLACK, cut.BLACK, cut.UNKNOWN])


class Board8x1NotFullTest(BoardRowTest):
    size = [8, 1]

    def test_2_3(self):
        horizontal_data = [[2, 3]]
        cut = Board(self.size, horizontal_data, None)

        cut.mark_intersections(Direction.HORIZONTAL)
        self.assertRowEqual(cut, [cut.UNKNOWN,
                                  cut.UNKNOWN,
                                  cut.UNKNOWN,
                                  cut.UNKNOWN,
                                  cut.UNKNOWN,
                                  cut.BLACK,
                                  cut.UNKNOWN,
                                  cut.UNKNOWN])
