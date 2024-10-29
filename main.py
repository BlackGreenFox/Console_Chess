from figures import *


def initialize_board():
    board = [[None for _ in range(8)] for _ in range(8)]
    board[0] = [Rook((0, 0), True), Knight((1, 0), True), Bishop((2, 0), True), Queen((3, 0), True),
                King((4, 0), True), Bishop((5, 0), True), Knight((6, 0), True), Rook((7, 0), True)]
    board[1] = [Pawn((x, 1), True) for x in range(8)]
    board[6] = [Pawn((x, 6), False) for x in range(8)]
    board[7] = [Rook((0, 7), False), Knight((1, 7), False), Bishop((2, 7), False), Queen((3, 7), False),
                King((4, 7), False), Bishop((5, 7), False), Knight((6, 7), False), Rook((7, 7), False)]
    return board


def print_board(board):
    print("        A       B       C       D       E       F       G       H")
    for y in range(8):
        print("     ------- ------- ------- ------- ------- ------- ------- -------")
        for row in range(3):
            row_str = "   {}| ".format(8 - y) if row == 1 else "    | "
            for x in range(8):
                figure = board[y][x]
                if figure is None:
                    if (x + y) % 2 == 0:
                        cell = "     "
                    else:
                        cell = ". . ."
                else:
                    cell = figure.draw[row]
                row_str += f"{cell} | "
            if row == 1:
                row_str += f"{8 - y}"
            print(row_str)
    print("     ------- ------- ------- ------- ------- ------- ------- -------")
    print("        A       B       C       D       E       F       G       H")


def main():
    board = initialize_board()
    print_board(board)


if __name__ == "__main__":
    main()