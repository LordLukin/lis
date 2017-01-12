from board import *


def read_input(filename):
    with open(filename) as input_file:
        board_size = list(map(int, input_file.readline().split()))

        horizontal_data = []
        for i in range(board_size[0]):
            horizontal_data.append(list(map(int, input_file.readline().split())))
        vertical_data = []
        for i in range(board_size[1]):
            vertical_data.append(list(map(int, input_file.readline().split())))

        return [board_size, horizontal_data, vertical_data]


if __name__ == '__main__':
    [size, horizontal_data, vertical_data] = read_input('input.txt')
    board = Board(size, horizontal_data, vertical_data)
    board.print_board()
    board.mark_intersections(Direction.HORIZONTAL)
    board.mark_intersections(Direction.VERTICAL)
    board.print_board()
