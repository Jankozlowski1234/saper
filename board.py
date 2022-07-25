from square import Square
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle


def to_rgb(touple: (), aplha: float = 1):
    lst = [i/255 for i in touple]
    lst.append(aplha)
    return lst


GREY = to_rgb((128, 128, 128))
BLUE = to_rgb((65, 105, 225))
BEIGE = to_rgb((217, 186, 140))
GREEN = to_rgb((124, 252, 0))
RED = to_rgb((255,0,0))

BACKGROUND_COLOR = GREY
UNVISITED_SQUARE_COLOR = BLUE
VISITED_SQUARE_COLOR = BEIGE
ONE_COLOR = GREEN
TWO_COLOR = GREEN
THREE_COLOR = GREEN
FOUR_COLOR = GREEN
FIVE_COLOR = GREEN
SIX_COLOR = GREEN
BOMB_COLOR = RED

class Board:
    '''
    This class will represent a board, its main goals will be painting board
    '''
    def __init__(self, matrix_of_squares, distance_between_squares: float):
        assert isinstance(matrix_of_squares, np.ndarray)
        self.__matrix_of_squares = matrix_of_squares
        self.__distance = distance_between_squares
        self.__ax = None

    def draw(self, text: str = ""):
        fig, ax = plt.subplots()
        ax.axis('off')
        self.__ax = ax
        x, y = self.get_shape_of_board()
        ax.set(xlim=(-1, x+1), ylim=(-1, y+1))
        ax.add_patch(Rectangle((0, 0), x, y, color=BACKGROUND_COLOR))
        for square in self:
            if not square.if_visited():
                x_sq, y_sq = square.get_draw_coordinates()
                ax.add_patch(Rectangle((x_sq, y_sq), 1, 1, color=UNVISITED_SQUARE_COLOR))
            else:
                self.draw_visited(square)
        plt.show()

    def draw_visited(self,square):
        x_sq, y_sq = square.get_draw_coordinates()
        self.__ax.add_patch(Rectangle((x_sq, y_sq), 1, 1, color=VISITED_SQUARE_COLOR))
        if square.if_bomb():
            self.__ax.text(x_sq, y_sq, "!0!",fontname="Comic Sans MS")
            return
        if square.get_nr_bombs_around() != 0:
            self.__ax.text(x_sq, y_sq, str(square.get_nr_bombs_around()), fontname="Comic Sans MS")
        return

    def get_shape_of_board(self):
        x, y = self.__matrix_of_squares.shape
        return (1+self.__distance)*x+self.__distance, (1+self.__distance)*y+self.__distance

    def __iter__(self):
        def iterator():
            for row in self.__matrix_of_squares:
                yield from row
        return iterator()

    def get_neighbour(self, square) -> list:
        x_board, y_board = self.__matrix_of_squares.shape
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

        for square in self:
            square.visit()