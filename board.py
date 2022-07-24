from square import Square
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle



class Board:
    '''
    This class will represent a board, its main goals will be painting board
    '''
    def __init__(self, matrix_of_squares):
        assert isinstance(matrix_of_squares, np.ndarray)
        self.__matrix_of_squares = matrix_of_squares

    def print(self):
        print("Our saper game TO DO!!!")

    def get_shape_of_board(self):
        return self.__matrix_of_squares.shape

    def __iter__(self):
        def iterator():
            for row in self.__matrix_of_squares:
                yield from row
        return iterator()

    def get_neighbour(self, square) -> list:
        x_board, y_board = self.get_shape_of_board()
        x_board -= 1
        y_board -= 1
        x, y = square.get_coordinates()
        lst = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                x_new = x+i
                y_new = y+j
                if (x_new <= x_board) & (0 <= x_new) & (y_new <= y_board) & (0 <= y_new):
                    if (i, j) != (0, 0):
                        lst.append(self.__matrix_of_squares[x_new, y_new])
        return lst

    def count_number_of_mines_around(self, square) -> int:
        return len([sq for sq in self.get_neighbour(square) if sq.if_bomb()])

    def prepare_board(self):
        for square in self:
            if not square.if_bomb():
                nr_of_mines = self.count_number_of_mines_around(square)
                square.set_nr_bombs_around(nr_of_mines)

