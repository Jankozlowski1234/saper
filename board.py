
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
RED = to_rgb((255, 0, 0))
BLACK = to_rgb((0, 0, 0))

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
MARKED_COLOR = RED
COLOR_BETWEEN_SQUARES = BLACK


class Board:
    '''
    This class will represent a board, its main goals will be painting board
    '''
    def __init__(self, matrix_of_squares, distance_between_squares: float, game):
        assert isinstance(matrix_of_squares, np.ndarray)
        self.__matrix_of_squares = matrix_of_squares
        self.__distance = distance_between_squares
        self.__ax = None
        self.__game = game

    def draw(self, text: str = "", time: int = 0, bombs: int = 0):
        fig, ax = plt.subplots()
        ax.axis('off')
        self.__ax = ax
        x, y = self.get_shape_of_board()
        ax.set(xlim=(-1, x+2), ylim=(-1, y+5))
        ax.add_patch(Rectangle((0, 0), x, y, color=BACKGROUND_COLOR))
        ax.add_patch(Rectangle((self.__distance, self.__distance),
                               x-2*self.__distance, y-2*self.__distance, color=COLOR_BETWEEN_SQUARES))
        ax.text(x * 0.5, y+3, text, fontname="Comic Sans MS")
        ax.text(x * 2 / 3, y + 1, f"Time: {time//60}min {time %60}s", fontname="Comic Sans MS")
        ax.text(1, y + 1, f"Bombs left: {bombs}", fontname="Comic Sans MS")
        for square in self:
            if not square.if_visited():
                x_sq, y_sq = square.get_draw_coordinates()
                ax.add_patch(Rectangle((x_sq, y_sq), 1, 1, color=UNVISITED_SQUARE_COLOR))
                if square.if_marked():
                    ax.add_patch(Circle((x_sq+0.5, y_sq+0.5), 0.5, color=MARKED_COLOR))
            else:
                self.draw_visited(square)
        self.draw_numbers()
        plt.show()

    def draw_visited(self, square):
        x_sq, y_sq = square.get_draw_coordinates()
        self.__ax.add_patch(Rectangle((x_sq, y_sq), 1, 1, color=VISITED_SQUARE_COLOR))
        if square.if_bomb():
            self.__ax.text(x_sq+0.4, y_sq+0.35, "!0!", fontname="Comic Sans MS")
            return
        if square.get_nr_bombs_around() != 0:
            self.__ax.text(x_sq+0.4, y_sq+0.35, str(square.get_nr_bombs_around()), fontname="Comic Sans MS")
        return

    def draw_numbers(self):
        for number, square in enumerate(self.__matrix_of_squares[:, 0]):
            x_sq, y_sq = square.get_draw_coordinates()
            self.__ax.text(x_sq + 0.4, y_sq - 0.65, str(number), fontname="Comic Sans MS")
        for number, square in enumerate(self.__matrix_of_squares[0, :]):
            x_sq, y_sq = square.get_draw_coordinates()
            self.__ax.text(x_sq - 0.6, y_sq + 0.35, str(number), fontname="Comic Sans MS")
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
                        lst.append(self[(x_new, y_new)])
        return lst

    def count_number_of_mines_around(self, square) -> int:
        return len([sq for sq in self.get_neighbour(square) if sq.if_bomb()])

    def visit_around_empty(self, square):
        assert square.if_empty()
        set_to_visit = set()
        lst_of_coordinates_empty_visited = []
        lst_empty_to_visit = [square]
        while lst_empty_to_visit:
            middle = lst_empty_to_visit.pop(0)
            for square in self.get_neighbour(middle):
                x_sq, y_sq = square.get_coordinates()
                set_to_visit.add((x_sq, y_sq))
                if square.if_empty() & ((x_sq, y_sq) not in lst_of_coordinates_empty_visited):
                    lst_empty_to_visit.append(square)
            lst_of_coordinates_empty_visited.append(middle.get_coordinates())
        for coordinates in set_to_visit:
            self[coordinates].visit(True)

    def prepare_board(self):
        for square in self:
            square.add_board(self)
            if not square.if_bomb():
                nr_of_mines = self.count_number_of_mines_around(square)
                square.set_nr_bombs_around(nr_of_mines)

    def __getitem__(self, coordinates: (int, int)):
        return self.__matrix_of_squares[coordinates]