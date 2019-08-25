import argparse
import subprocess
import sys
import neural_chessboard.main

class Frame:

    def __init__(self, args):
        self.input_path = args.input
        self.output_path = args.output

    def convert_image(self):
        # args = ['python3 ~/Documents/Projects/GitHub/OpenCVChess/IRS/code/neural_chessboard/main.py', 'detect', '--input', self.input_path,
        #         '--output', self.output_path]
        #
        # sys.path.insert(0, "/Users/robing/Documents/Projects/GitHub/OpenCVChess/IRS/code/neural_chessboard")
        # p = subprocess.Popen(args)
        neural_chessboard.main.detect()


if __name__ == "__main__":
    p = argparse.ArgumentParser(description= \
                                    'Find, crop and create FEN from image.')

    p.add_argument('--input', type=str, \
                   help='input image (default: input.jpg)')
    p.add_argument('--output', type=str, \
                   help='output path (default: output.jpg)')

    args = p.parse_args()

    f = Frame(args)
    f.convert_image()