from enum import Enum
import numpy as np


class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Board(object):

    UNKNOWN = -2
    BLACK = 1
    WHITE = -1

    def __init__(self, size, horizontal_data, vertical_data):
        self.size_h = size[0]
        self.size_v = size[1]
        self.horizontal_data = horizontal_data
        self.vertical_data = vertical_data
        self.board = np.full((self.size_v, self.size_h), self.UNKNOWN, dtype=int)
        self.__check_data()

    def __check_data(self):
        if self.size_h <= 0 or self.size_v <= 0:
            raise ValueError("Size must be positive natural")
        for row in enumerate(self.horizontal_data):
            if not row:
                raise LookupError("Row cannot be empty")
        for col in enumerate(self.vertical_data):
            if not col:
                raise LookupError("Column cannot be empty")

    def solve(self):
        self.mark_intersections(Direction.HORIZONTAL)
        self.mark_intersections(Direction.VERTICAL)
        self.extend_border_markers(Direction.HORIZONTAL)
        self.extend_border_markers(Direction.VERTICAL)
        self.mark_unreachable_fields(Direction.HORIZONTAL)
        self.mark_unreachable_fields(Direction.VERTICAL)
        self.fill_white_when_complete(Direction.HORIZONTAL)
        self.fill_white_when_complete(Direction.VERTICAL)

    def print_board(self):
        unknown = u"\u2591"  # * 2
        black = u"\u2588"  # * 2
        white = u" "  # * 2

        print('+', end='')
        print('-' * self.size_h, end='')
        print('+')
        for row in self.board:
            print('|', end='')
            for item in row:
                if item == self.WHITE:
                    print(white, end='')
                elif item == self.UNKNOWN:
                    print(unknown, end='')
                else:
                    print(black, end='')
            print('|')
        print('+', end='')
        print('-' * self.size_h, end='')
        print('+')

    def __fill_forward(self, row):
        internal_row = [self.UNKNOWN] * self.size_h
        index = 0
        for value, number in enumerate(row):
            for x in range(number):
                internal_row[index + x] = value
                if index + x + 1 < self.size_h:
                    internal_row[index + x + 1] = self.WHITE
            index += number + 1
        return internal_row

    def __fill_backward(self, row):
        internal_row = [self.UNKNOWN] * self.size_h
        max_val = len(row) - 1
        index = self.size_h - 1
        for value, number in enumerate(reversed(row)):
            x = 0
            for x in range(number):
                internal_row[index - x] = max_val - value
                if index - x - 1 > 0:
                    internal_row[index - x - 1] = self.WHITE
            index -= x + 2
        return internal_row

    def mark_intersections(self, direction):
        if direction == Direction.VERTICAL:
            data = self.vertical_data
            size = self.size_v
            self.board = np.transpose(self.board)
        else:
            data = self.horizontal_data
            size = self.size_h

        for i, row in enumerate(data):
            row_size = sum(row) + len(row) - 1
            if row_size == size:
                # self.board[i] = self.full_row_match(row)
                row_forward = self.__fill_forward(row)
                row_backward = self.__fill_backward(row)
                for index in range(size):
                    if row_forward[index] == self.WHITE:
                        self.board[i][index] = self.WHITE
                    elif row_forward[index] == row_backward[index]:
                        self.board[i][index] = self.BLACK
            else:
                row_forward = self.__fill_forward(row)
                row_backward = self.__fill_backward(row)
                for index in range(size):
                    if row_forward[index] == self.UNKNOWN or row_forward[index] == self.WHITE:
                        continue
                    if row_forward[index] == row_backward[index]:
                        self.board[i][index] = self.BLACK

        if direction == Direction.VERTICAL:
            self.board = np.transpose(self.board)

    def extend_border_markers(self, direction):
        if direction == Direction.VERTICAL:
            data = self.horizontal_data  # yes, another dimension
            size = self.size_h
            self.board = np.transpose(self.board)
        else:
            data = self.vertical_data  # yes, another dimension
            size = self.size_v

        self.__mark_beginings(data)
        self.__mark_endings(data, size)

        if direction == Direction.VERTICAL:
            self.board = np.transpose(self.board)

    def __mark_beginings(self, data):
        for i, row in enumerate(data):
            first = row[0]
            markedFromEdge = self.board[0][i] == self.BLACK
            marked = False
            for j in range(first):
                if marked:
                    self.board[j][i] = self.BLACK
                if self.board[j][i] == self.BLACK:
                    marked = True
            if markedFromEdge:
                self.board[j+1][i] = self.WHITE

    def __mark_endings(self, data, size):
        for i, row in enumerate(data):
            last = row[-1]
            markedFromEdge = self.board[-1][i] == self.BLACK
            marked = False
            for j in reversed(range(size - last, size)):
                if marked:
                    self.board[j][i] = self.BLACK
                if self.board[j][i] == self.BLACK:
                    marked = True
            if markedFromEdge:
                self.board[j-1][i] = self.WHITE

    def mark_unreachable_fields(self, direction):
        if direction == Direction.VERTICAL:
            data = self.vertical_data
            size = self.size_v
            self.board = np.transpose(self.board)
        else:
            data = self.horizontal_data
            size = self.size_h

        for i, row in enumerate(data):
            if self.BLACK in self.board[i]:
                if len(row) == 1:
                    filled = np.count_nonzero(self.board[i] == self.BLACK)
                    diff = row[0] - filled
                    for index in reversed(range(size)):
                        if self.board[i][index] == self.BLACK:
                            break
                    first = index + diff + 1
                    if first < self.size_h:
                        for j in range(first, size):
                            self.board[i][j] = self.WHITE
                    # print(i, index, index + diff + 1)
                    for index in range(size):
                        if self.board[i][index] == self.BLACK:
                            break
                    last = index - diff
                    if last > 0:
                        for j in range(last):
                            self.board[i][j] = self.WHITE

        if direction == Direction.VERTICAL:
            self.board = np.transpose(self.board)

    def fill_white_when_complete(self, direction):
        if direction == Direction.VERTICAL:
            data = self.vertical_data
            size = self.size_v
            self.board = np.transpose(self.board)
        else:
            data = self.horizontal_data
            size = self.size_h

        for i, row in enumerate(data):
            if self.__check_if_complete_row(row, self.board[i]):
                for j in range(size):
                    if self.board[i][j] == self.UNKNOWN:
                        self.board[i][j] = self.WHITE

        if direction == Direction.VERTICAL:
            self.board = np.transpose(self.board)

    def __check_if_complete_row(self, row, board_row):
        # think about marking row as complete and not take it for further computations
        filled = 0
        index = 0
        last = len(row)
        for item in board_row:
            if item == self.BLACK:
                filled += 1
            if item == self.WHITE or item == self.UNKNOWN:
                if filled != 0 and filled != row[index]:
                    return False
                elif filled != 0 and filled == row[index]:
                    index += 1
                    if index == last:
                        return True
