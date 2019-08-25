import boto3
import chess
import os
import sys
import lsh

from lsh import ai
from datetime import datetime
from move import Move, prettify_board
from IPython import embed
from gcode import generate_gcode, generate_gcode_move

IRS_FOLDER_PATH = "/home/ubuntu/Desktop/CAPSTONE_R/chess-irs"

class InvalidMoveException(Exception):
    pass


class Client:
    def __init__(self, name):
        self.name = name
        self.BUCKET_NAME = "gamestateimages"

    def get_image(self, filename, d=None):
        s3 = boto3.client(self.name)
        down_path = "{}/{}".format(d, filename) if d else filename

        save_path = "{}/{}".format(IRS_FOLDER_PATH, down_path)

        #s3.Bucket(self.BUCKET_NAME).download_file(down_path, down_path)
        s3.download_file(self.BUCKET_NAME, down_path, save_path)

    def upload_object(self, filename, d=None):
        s3 = boto3.client(self.name)
        s3.upload_file(filename, self.BUCKET_NAME, filename)

def read_fen():
    # try:
    #     f = open("fen/game.fen")
    #     fen = f.read()
    # except FileNotFoundError:
    #     return None
    # finally:
    #     f.close()

    # return fen
    try:
        with open("/home/ubuntu/Desktop/CAPSTONE_R/chess-irs/fen/game.fen", "r") as f:
            return f.read()
    except IOError:
        return None

def write_fen(board):
    f = open("/home/ubuntu/Desktop/CAPSTONE_R/chess-irs/fen/game.fen", "w")
    f.write(board.fen())
    f.close()


def main():
    filename = sys.argv[1]

    # Read saved board state if exists
    existing_board_state = read_fen()
    if not existing_board_state:
        board = chess.Board()
    else:
        board = chess.Board(existing_board_state)

    # Initialize client, grab file from bucket
    client = Client("s3")
    client.get_image(filename, "rawstates")

    # Relative path for raw and processed image
    raw_file_path = "{}/rawstates/{}".format(IRS_FOLDER_PATH, filename)
    processed_file_path = "{}/processedstates/{}".format(
        IRS_FOLDER_PATH, filename.replace("raw", "processed"))

    # print(raw_file_path)
    print("Processed file path:", processed_file_path)

    #Determine move from image
    m = Move(board, raw_file_path, processed_file_path)
    user_move = m.determine_move()

    if user_move is None:
        raise InvalidMoveException("Invalid Move Provided")

    print("User Move:", user_move)

    board.push_uci(user_move.uci())
    computer = ai.StockfishAI()
    computer_move = computer.get_ai_uci(board)
    board.push_uci(computer_move)

    print("Computer Move:", computer_move)

    # Save GCode to txt file
    # gcode_string = generate_gcode_move("a1a2")
    # f = open("inputs.txt", "w")
    # f.write(gcode_string)
    # f.close()
    # client.upload_object("inputs.txt")

    # Write game round to fen
    write_fen(board)


if __name__ == "__main__":
    # gcode_string = generate_gcode_move("b8c8")
    # f = open("inputs.txt", "w")
    # f.write("\n".join(gcode_string))
    # f.close()
    # client = Client("s3")
    # client.upload_object("inputs.txt")
    main()