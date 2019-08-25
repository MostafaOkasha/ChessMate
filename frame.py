import argparse
from pprint import pprint

from neuralchessboard import detect


class Frame:
    """Frame(mode, raw_img, processed_img)

    A frame represents the raw image taken from the camera,
    performs the neural network process.
    """

    def __init__(self, mode, raw_img, processed_img):
        self.raw_img_path = raw_img
        self.processed_img_path = processed_img

        self.nn_args = argparse.Namespace(input=raw_img,
                                          mode=mode,
                                          output=processed_img)
        Frame.process_image(self)

    @staticmethod
    def process_image(self):
        """process_image

        Process the raw image from input path in args
        to the output path in args.
        """

        detect.main(self.nn_args)

    def get_raw_path(self):
        """get_raw_path

        Return the path of the raw image

        :return: str
        """

        return self.raw_img_path

    def get_processed_path(self):
        """get_processed_path

        Return the path of the processed image.

        :return: str
        """

        return self.processed_img_path


if __name__ == "__main__":
    p = argparse.ArgumentParser(description= \
                                    'Find, crop and create FEN from image.')

    p.add_argument('mode', nargs=1, type=str, default="detect", \
                   help='detect | dataset | train')
    p.add_argument('--input', type=str, \
                   help='input image (default: input.jpg)')
    p.add_argument('--output', type=str, \
                   help='output path (default: output.jpg)')

    args = p.parse_args()

    Frame(args.mode, args.input, args.output)
