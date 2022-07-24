class Square():
    '''
    It will represent a one square of a board
    '''
    def __init__(self, coordinates: (), nr: int=0):
        self.__nr_bombs = nr
        self.__if_blind = False  # blind - no number on it
        self.__if_visited = False
        self.__if_marked = False
        self.__coordinates = coordinates

    def get_nr_bombs(self):
        return self.__nr_bombs

    def get_coordinates(self):
        return self.__coordinates

    def if_blind(self):
        return self.__if_blind

    def if_visited(self):
        return self.__if_visited

    def if_marked(self):
        return self.__if_marked

    def __str__(self):
        return f"Square of coordinates {self.__coordinates} and {self.get_nr_bombs()} bombs "

if __name__ == "__main__":
    pass
