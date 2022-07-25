from board import Board
from square import Square
import numpy as np
import random as r


GAMES = {"Beginner": (8, 8, 10), "Normal": (16, 16, 40), "Expert": (16, 30, 99)}
NR_OF_ROWS = (8, 24)
NR_OF_COLUMNS = (8, 30)
NR_MIN_OF_BOMBS = 10
DISTANCE_BETWEEN_SQUARES = 0.1 ## square has length 1


class Game:
    def __init__(self):
        self.__name = None
        self.__matrix_of_squares = None
        self.__board = None
        self.__games = GAMES
        self.__mines_left = None

    def main(self):
        nr_rows, nr_columns, nr_mines = self.__beginning()
        self.__create_board(nr_rows, nr_columns, nr_mines)
        self.draw()
        return

    def __beginning(self):
        name = input("Give your Name: ").strip()
        self.__name = name
        string = ""
        i = 1
        list_of_available_names = []
        dict_of_options = {}
        for keys, values in self.__games.items():
            nr_rows, nr_columns, nr_mines = values
            dict_of_options[i] = values
            list_of_available_names.append(str(i))
            string += f"{i}. {keys} level with {nr_rows}x{nr_columns} board and {nr_mines} mines,\n"
            i += 1
        dict_of_options[i] = "Custom"
        list_of_available_names.append(str(i))
        string += f"{i}. Custom game."
        print(string)
        nr_game = input(f"Whith game you want to play, {self.__name}:").strip()
        while nr_game not in list_of_available_names:
            nr_game = input(f"Whith game you want to play, {self.__name}:").strip()
        nr_game = int(nr_game)
        if dict_of_options[nr_game] == "Custom":
            nr_rows, nr_columns, nr_mines = self.__get_custom_game()
            return nr_rows, nr_columns, nr_mines
        return dict_of_options[nr_game]

    def __get_custom_game(self):
        nr_rows = self.__get_number_of(NR_OF_ROWS, "rows")
        nr_columns = self.__get_number_of(NR_OF_COLUMNS, "columns")
        nr_mines = self.__get_number_of((NR_MIN_OF_BOMBS, (nr_columns-1)*(nr_rows-1)), "mines")
        self.__mines_left = nr_mines
        return nr_rows, nr_columns, nr_mines

    def __get_number_of(self, touple: (), name: str):
        nr = input(f"Give number of {name} (between {touple[0]} and {touple[1]}): ").strip()
        while nr not in [str(nr) for nr in range(touple[0], touple[1] + 1)]:
            nr = input(f"Give number of {name} (between {touple[0]} and {touple[1]}): ").strip()
        return int(nr)

    def get_name(self):
        return self.__name

    def __create_board(self, nr_rows: int, nr_columns: int, nr_mines: int):
        list_of_lists = []
        list_for_picking_bombs = []
        for i in range(nr_columns):
            list_of_squares = []
            for j in range(nr_rows):
                coordinates = (i, j)
                draw_coordinates = ((1+DISTANCE_BETWEEN_SQUARES)*i+DISTANCE_BETWEEN_SQUARES,
                                    (1+DISTANCE_BETWEEN_SQUARES)*j+DISTANCE_BETWEEN_SQUARES)
                list_for_picking_bombs.append(coordinates)
                square = Square(coordinates, draw_coordinates)
                list_of_squares.append(square)
            list_of_lists.append(list_of_squares)
        matrix = np.array(list_of_lists)
        self.__matrix_of_squares = matrix
        self.__board = Board(matrix, DISTANCE_BETWEEN_SQUARES)
        coordinates_of_mines = r.sample(list_for_picking_bombs, nr_mines)
        for coordiante in coordinates_of_mines:
            x, y = coordiante
            self.__matrix_of_squares[x, y].give_bomb()
        self.__board.prepare_board()

    def draw(self,text: str = ""):
        self.__board.draw(text)
        return

    def see_squares(self):
        for i in self.__board:
            print(i)


if __name__ == "__main__":
    g = Game()
    g.main()
