import cv2
import numpy as np

from constants import *


class Square:

    def __init__(self, board, location):
        self.board = board

        # Corner to corner pixel location
        self.x, self.y = location

        self.xs, self.ys = self.x * SQUARE_SIZE, self.y * SQUARE_SIZE

        self.xe = self.xs + SQUARE_SIZE
        self.ye = self.ys + SQUARE_SIZE

        # BGR and HSV square images
        self.bgr = self.board.bgr[self.xs: self.xe, self.ys: self.ye]
        self.hsv = self.board.hsv[self.xs: self.xe, self.ys: self.ye]

        #
        self.white_pixels = self.calculate_white_pixels()
        self.green_pixels = self.calculate_green_pixels()

        #
        self.contains_piece = self.detect_piece()

    def __repr__(self):
        return "Square({}, {})".format(self.board, self.location)


    def __str__(self):
        return "Square: {}; White Pixels: {}, Green Pixels: {}, Piece?: {}".format(
            (self.x + 1, self.y + 1), self.white_pixels, self.green_pixels,
            self.contains_piece)


    def calculate_white_pixels(self):
        lower_white = np.array([0, 0, 150])
        upper_white = np.array([128, WHITE_SENSITIVITY, 255])

        white_mask = cv2.inRange(self.hsv, lower_white, upper_white)
        return (white_mask == 255).sum()


    def calculate_green_pixels(self):
        lower_green = np.array([100 - GREEN_SENSITIVITY, 25, 25])
        upper_green = np.array([100 + GREEN_SENSITIVITY, 255, 255])

        green_mask = cv2.inRange(self.hsv, lower_green, upper_green)
        return (green_mask == 255).sum()


    def detect_piece(self):
        piece_exists = (self.white_pixels < WHITE_THRESHOLD) and \
                       (self.green_pixels < GREEN_THRESHOLD)

        return piece_exists


    def get_contains_piece(self):
        return self.contains_piece