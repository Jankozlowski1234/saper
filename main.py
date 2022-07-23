from board import Board
from square import Square
import numpy as np


GAMES = {"Beginner":(8,8,10),"Normal":(16,16,40)}


class Game:
    def __init__(self):
        self.__name = None
        self.__matrix_of_squares = None
        self.__board = None
        self.__games = GAMES

    def main(self):
        nr_rows, nr_columns, nr_mines = self.__beginning()
        return

    def __beginning(self):
        name = input("Give your Name: ").strip()
        self.__name = name
        string = ""
        i = 1
        list_of_available_names = []
        dict_of_options = {}
        for keys,values in self.__games.items():
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
            return (nr_rows, nr_columns, nr_mines)
        return dict_of_options[nr_game]

    def __get_custom_game(self):
        print("TO DO!!!!")
        return (10,20,17)

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    g = Game()
    g.main()