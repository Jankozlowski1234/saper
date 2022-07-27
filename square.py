class Square:
    '''
    It will represent a one square of a board
    '''
    def __init__(self, coordinates: (), draw_coordinates: (), nr: int, board, game):
        self.__nr_bombs_around = 0  # blind - no number on it
        self.__if_visited = False
        self.__if_marked = False
        self.__coordinates = coordinates
        self.__if_bomb = False
        self.__draw_coordinates = draw_coordinates
        self.__board = board
        self.__game = game

    def get_nr_bombs_around(self):
        return self.__nr_bombs_around

    def get_coordinates(self):
        return self.__coordinates

    def get_draw_coordinates(self):
        return self.__draw_coordinates

    def if_empty(self):  # blind - no number on it
        if self.if_bomb():
            return False
        return self.__nr_bombs_around == 0

    def if_visited(self):
        return self.__if_visited

    def if_marked(self):
        return self.__if_marked

    def add_board(self, board):
        self.__board = board
        return

    def __str__(self):
        string = f"Square of coordinates {self.__coordinates} and {self.get_nr_bombs_around()} bombs around"
        if self.if_bomb():
            return string + ", and bomb on it"
        return string

    def give_bomb(self):
        self.__if_bomb = True
        return

    def if_bomb(self):
        return self.__if_bomb

    def set_nr_bombs_around(self, nr: int):
        self.__nr_bombs_around = nr
        return

    def visit(self, visit_in_loop=False):
        if self.if_visited():
            return
        self.__if_visited = True
        self.__game.substract_one_from_safe_squares()
        if self.if_bomb():
            return "END"
        if self.if_empty() & (not visit_in_loop):
            self.__board.visit_around_empty(self)

    def mark(self):
        self.__if_marked = True
        return

    def unmark(self):
        self.__if_marked = False
        return


if __name__ == "__main__":
    a = 1
    pass
