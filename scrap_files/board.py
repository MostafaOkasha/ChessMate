import cv2
import sys
import numpy as np
import argparse

from square import Square
from pprint import pprint

from constants import *


class Board:
    def __init__(self, path):
        self.image_path = path
        self.bgr = cv2.imread(self.image_path)
        self.hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)

        self.squares, self.piece_locations = self.populate_matrices()

        if DEBUG:
            self.debug()

    def debug(self):
        squares_flat = np.asarray(self.squares).flatten()

        for sqr in squares_flat:
            print(sqr)

            if SHOW_SQUARES:
                cv2.imshow(str(sqr)[:15], sqr.bgr)
                cv2.waitKey(0)

    def populate_matrices(self):
        sqr_matrix = [[Square(self, (x, y)) for y in range(8)] for x in range(8)]
        loc_matrix = [[sqr_matrix[i][j].get_contains_piece() for j in range(8)]
                      for i in range(8)]

        return sqr_matrix, loc_matrix

    def get_piece_locations(self):
        return self.piece_locations

    def __repr__(self):
        return "Board({})".format(self.image_path)

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":

    # parser = argparse.ArgumentParser(description="Analyze image to determine location "
    #                                              "of pieces on a green and white chess board")
    # parser.add_argument("processed image path", )

    board = Board(sys.argv[1])
    pprint(board.get_piece_locations())
