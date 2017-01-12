from enum import Enum


class Direction(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Board(object):

    UNKNOWN = u"\u2591"
    BLACK = u"\u2588"
    WHITE = u" "

    def __init__(self, size, horizontal_data, vertical_data):
        self.size_h = size[0]
        self.size_v = size[1]
        self.horizontal_data = horizontal_data
        self.vertical_data = vertical_data
        self.board = []
        for i in range(self.size_v):
            self.board.append([self.UNKNOWN] * self.size_h)

    def column(self, i):
        return [row[i] for row in self.board]

    def print_board(self):
        print('-' * self.size_h)
        for row in self.board:
            for item in row:
                print(item, end='')
            print('')

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
            for x in range(number):
                internal_row[index - x] = max_val - value
                if index - x - 1 > 0:
                    internal_row[index - x - 1] = self.WHITE
            index -= x + 2
        return internal_row

    def mark_intersections(self, direction):
        if direction == Direction.HORIZONTAL:
            data = self.horizontal_data
            size = self.size_h
        else:
            data = self.vertical_data
            size = self.size_v

        for i, row in enumerate(data):
            if not row:
                raise LookupError("Row cannot be empty")
            row_size = sum(row) + len(row) - 1
            if row_size == size:
                # self.board[i] = self.full_row_match(row)
                row_forward = self.__fill_forward(row)
                row_backward = self.__fill_backward(row)
                for index in range(size):
                    if row_forward[index] == self.WHITE:
                        if direction == Direction.HORIZONTAL:
                            self.board[i][index] = self.WHITE
                        else:
                            self.board[index][i] = self.WHITE
                    elif row_forward[index] == row_backward[index]:
                        if direction == Direction.HORIZONTAL:
                            self.board[i][index] = self.BLACK
                        else:
                            self.board[index][i] = self.BLACK
            else:
                row_forward = self.__fill_forward(row)
                row_backward = self.__fill_backward(row)
                for index in range(size):
                    if row_forward[index] == self.UNKNOWN or row_forward[index] == self.WHITE:
                        continue
                    if row_forward[index] == row_backward[index]:
                        if direction == Direction.HORIZONTAL:
                            self.board[i][index] = self.BLACK
                        else:
                            self.board[index][i] = self.BLACK

    def full_row_match(self, row):
        output_row = []
        for i in row:
            output_row.extend(self.BLACK * i)
            output_row.append(self.WHITE)
        return output_row
