UNKNOWN = u"\u2591"
BLACK = u"\u2588"
WHITE = u" "


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


def mark_horizontal_intersections(horizontal_size, horizontal_data, board):
    for i in range(len(horizontal_data)):
        row = horizontal_data[i]
        row_size = sum(row) + len(row) - 1
        if row_size == horizontal_size:
            board[i] = full_row_match(row)
        else:
            size_diff = horizontal_size - row_size
            for r in row:
                if r > size_diff:
                    filled_size = r - size_diff
                    #board[i] = UNKNOWN * size_diff + BLACK * filled_size + UNKNOWN * size_diff
                    for f in range(filled_size):
                        board[i][size_diff+f] = BLACK


def mark_vertical_intersections(vertical_size, vertical_data, board):
    for i in range(len(vertical_data)):
        col = vertical_data[i]
        col_size = sum(col) + len(col) - 1
        if col_size == vertical_size:
            pass
            #board[i] = full_col_match(col)
        else:
            size_diff = vertical_size - col_size
            for c in col:
                if c > size_diff:
                    filled_size = c - size_diff
                    #board[i] = UNKNOWN * size_diff + BLACK * filled_size + UNKNOWN * size_diff
                    for f in range(filled_size):
                        board[size_diff+f][i] = BLACK


def full_row_match(row):
    output_row = []
    for i in row:
        output_row.extend(BLACK * i)
        output_row.append(WHITE)
    return output_row


def mark_intersections(size, horizontal_data, vertical_data, board):
    mark_horizontal_intersections(size[0], horizontal_data, board)
    #print(transposed_board)
    mark_vertical_intersections(size[1], vertical_data, board)


def build_board(size):
    board = []
    for i in range(size[0]):
        row = []
        for j in range(size[1]):
            row.append(UNKNOWN)
        board.append(row)
    return board


def print_board(board):
    for row in board:
        for item in row:
            print(item, end='')
        print('')


if __name__ == '__main__':
    [size, horizontal_data, vertical_data] = read_input('input.txt')
    board = build_board(size)
    print_board(board)
    #print(horizontal_data)
    #print(vertical_data)
    mark_intersections(size, horizontal_data, vertical_data, board)
    print("----------")
    print_board(board)
