class Square:
    '''
    It will represent a one square of a board
    '''
    def __init__(self, coordinates: (), draw_coordinates: (), nr: int = 0):
        self.__nr_bombs_around = nr
        self.__if_blind = False  # blind - no number on it
        self.__if_visited = False
        self.__if_marked = False
        self.__coordinates = coordinates
        self.__if_bomb = False
        self.__draw_coordinates = draw_coordinates

    def get_nr_bombs_around(self):
        return self.__nr_bombs_around

    def get_coordinates(self):
        return self.__coordinates

    def get_draw_coordinates(self):
        return self.__draw_coordinates

    def if_blind(self):
        return self.__if_blind

    def if_visited(self):
        return self.__if_visited

    def if_marked(self):
        return self.__if_marked

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

    def visit(self):
        self.__if_visited = True
        return

    def mark(self):
        self.__if_marked = True
        return


if __name__ == "__main__":
    pass
