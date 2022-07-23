from square import Square
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,Circle



class Board:
    '''
    This class will represent a board, its main goals will be
    '''
    def __init__(self,matrix_of_squares):
        self.__matrix_of_squares = matrix_of_squares

    def print(self):
        print("Our saper")

