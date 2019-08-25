import cv2
import numpy as np
import argparse
from pprint import pprint

from square import Square
from constants import *


class BoardState:
    """BoardState(processed_img_path, raw_img_path=None)

    The Board object will create the location matrix from the neural
    network processed image.
    """

    def __init__(self, processed_img_path, raw_img_path=None):
        self.raw_img_path = raw_img_path
        self.processed_img_path = processed_img_path

        self.bgr = cv2.imread(self.processed_img_path)
        self.hsv = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2HSV)

        self.squares, self.color_map = self.populate_matrices()

        if DEBUG:
            self.debug()

    def debug(self):
        """debug

        Display pre-processed images, processed images, and individual squares
        and print information regarding pixel counts of each square.
        """

        def show_image(img_resize, window_name):
            cv2.namedWindow(window_name)
            cv2.moveWindow(window_name, 40, 30)
            cv2.imshow(window_name, img_resize)
            cv2.waitKey(0)
            cv2.destroyWindow(window_name)

        squares_flat = np.asarray(self.squares).flatten()

        if SHOW_IMAGES and self.raw_img_path:
            pre_proc_img_resize = cv2.resize(cv2.imread(self.raw_img_path), (0, 0), fx=0.25, fy=0.25)
            show_image(pre_proc_img_resize, "Pre Processed Board Image")

        if SHOW_IMAGES:
            proc_img_resize = cv2.resize(self.bgr, (0, 0), fx=0.5, fy=0.5)
            show_image(proc_img_resize, "Processed Board Image")

        for sqr in squares_flat:
            print(sqr)

            if SHOW_IMAGES:

                # Maintain copy of bgr to to replace
                bgr_copy = proc_img_resize.copy()
                border = cv2.rectangle(bgr_copy, (sqr.ys // 2, sqr.xs // 2), (sqr.ye // 2, sqr.xe // 2),
                                      (0, 0, 255), 5)
                overlay_winname = str(sqr)[:15]
                show_image(border, overlay_winname)

    def populate_matrices(self):
        """populate_matrices

        Initialize square objects for each square piece on board
        and create location matrix from each square object.

        :return list[list], list[list]
        """

        sqr_matrix = [[Square(self, (x, y)) for y in range(8)] for x in range(8)]
        loc_matrix = [[sqr_matrix[i][j].get_piece() for j in range(8)]
                      for i in range(8)]

        sqr_matrix = np.flip(np.flip(sqr_matrix, axis=0), axis=1).tolist()
        loc_matrix = np.flip(np.flip(loc_matrix, axis=0), axis=1).tolist()
        return sqr_matrix, loc_matrix

    def get_color_map(self):
        """get_color_map

        Return the color mapfor the board.

        :return list[list[Piece]]
        """

        return self.color_map

    def __repr__(self):
        return "Board({})".format(self.processed_img_path)

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze image to determine location "
                                                 "of pieces on a green and white chess board")
    parser.add_argument("processed", help="processed image path")
    parser.add_argument("-r", "--raw", help="raw image path")
    args = parser.parse_args()

    board = BoardState(args.processed, args.raw)
    pprint(board.get_color_map())
