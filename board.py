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

    def print_board(self):
        print('-' * self.size_h)
        for row in self.board:
            for item in row:
                print(item, end='')
            print('')

    def mark_horizontal_intersections(self):
        for i, row in enumerate(self.horizontal_data):
            row_size = sum(row) + len(row) - 1
            if row_size == self.size_h:
                self.board[i] = self.full_row_match(row)
            else:
                size_diff = self.size_h - row_size
                for number in row:
                    if number > size_diff:
                        filled_size = number - size_diff
                        for f in range(filled_size):
                            self.board[i][size_diff + f] = self.BLACK

    def full_row_match(self, row):
        output_row = []
        for i in row:
            output_row.extend(self.BLACK * i)
            output_row.append(self.WHITE)
        return output_row
