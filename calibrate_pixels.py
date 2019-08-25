import sys
from collections import OrderedDict
from IPython import embed

from board import BoardState

b = BoardState(sys.argv[1])
sqrs = b.squares

green_squares = [sqrs[2][1], sqrs[2][3], sqrs[2][5], sqrs[2][7],
                 sqrs[3][0], sqrs[3][2], sqrs[3][4], sqrs[3][6],
                 sqrs[4][1], sqrs[4][3], sqrs[4][5], sqrs[4][7],
                 sqrs[5][0], sqrs[5][2], sqrs[5][4], sqrs[5][6]]

white_squares = [sqrs[2][0], sqrs[2][2], sqrs[2][4], sqrs[2][6],
                 sqrs[3][1], sqrs[3][3], sqrs[3][5], sqrs[3][7],
                 sqrs[4][0], sqrs[4][2], sqrs[4][4], sqrs[4][6],
                 sqrs[5][1], sqrs[5][3], sqrs[5][5], sqrs[5][7]]

black_pieces = sqrs[0] + sqrs[1]

green_pixels = [img.hsv.flatten() for img in green_squares]
white_pixels = [img.hsv.flatten() for img in white_squares]
black_pixels = [img.hsv.flatten() for img in black_pieces]

# Calculate Green Pixels
green = {'h': {}, 's': {}, 'v': {}}

for pixel in green_pixels:
    for h, s, v in zip(*[iter(pixel)]*3):
        green['h'][h] = green['h'].get(h, 0) + 1
        green['s'][s] = green['s'].get(s, 0) + 1
        green['v'][v] = green['v'].get(v, 0) + 1

ordered_green = {'h': OrderedDict(sorted(green['h'].items())),
                 's': OrderedDict(sorted(green['s'].items())),
                 'v': OrderedDict(sorted(green['v'].items()))}

# Calculate White Pixels
white = {'h': {}, 's': {}, 'v': {}}
for pixel in white_pixels:
    for h, s, v in zip(*[iter(pixel)]*3):
        white['h'][h] = white['h'].get(h, 0) + 1
        white['s'][s] = white['s'].get(s, 0) + 1
        white['v'][v] = white['v'].get(v, 0) + 1

ordered_white = {'h': OrderedDict(sorted(white['h'].items())),
                 's': OrderedDict(sorted(white['s'].items())),
                 'v': OrderedDict(sorted(white['v'].items()))}

# Calculate Black Pixels
black = {'h': {}, 's': {}, 'v': {}}
for pixel in black_pixels:
    for h, s, v in zip(*[iter(pixel)]*3):
        black['h'][h] = black['h'].get(h, 0) + 1
        black['s'][s] = black['s'].get(s, 0) + 1
        black['v'][v] = black['v'].get(v, 0) + 1

ordered_black = {'h': OrderedDict(sorted(black['h'].items())),
                 's': OrderedDict(sorted(black['s'].items())),
                 'v': OrderedDict(sorted(black['v'].items()))}

embed()
