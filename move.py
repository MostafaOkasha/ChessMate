import subprocess
import chess
from IPython import embed

from enums import Piece
from board import BoardState


def _loc(x, y):
    """_loc(int, int) -> int

    >>>_loc(0, 7)
    63
    >>>_loc(7, 0)
    0

    Return the index for the chess library board.
    The orientation of is as follows on a 8x8 grid:
        - (0, 7) is the top right of the board
        - (0, 0) is the top left of the board
        - (7, 0) is the bottom left of the board
        - (7, 7) is the bottom right of the board

    :param x: row of the board
    :param y: col of the board
    :return int: index between [0, 64)
    """

    return 8 * (8 - x) - (8 - y)


def _get_piece(board, i):
    """_get_piece(chess.Board, int) -> Piece

    Return an Enumeration of the square representing
    an Empty Square, Black Piece or White Piece.

    :param board: board state from chess
    :param i: index for square in board
    :return Piece: Piece enumeration
    """

    try:
        return Piece(board.piece_at(i).color)
    except AttributeError:
        return Piece(None)


def generate_color_map(board):
    """generate_color_map(board) -> list[list[Piece]]

    Generate color map with each value in cell represented
    by the Piece enumeration.

    :param board: board state from chess
    :return list[list[Piece]]: 2-D list of Piece Enumerations
    """

    return [[_get_piece(board, _loc(x, y)) for y in range(8)]
            for x in range(8)]

def prettify_board(board):
        """prettify_board

        Return a prettified version of the board to visualize
        the locations of pieces in algebraic notation.

        :return str
        """

        top = f"  a b c d e f g h \n  {'-'*15}\n"
        bottom = f"\n  {'-' * 15}\n  a b c d e f g h"

        numbered_board = [f"{row_num}|{row}|{row_num}" for row, row_num
                          in zip(str(board).split("\n"), range(8, 0, -1))]

        return top + "\n".join(numbered_board) + bottom


class Move:
    """Move(previous_state, new_state_raw_img, new_state_proc_img)

    Represents the move from the previous state which is the truth
    to the new state from a raw image taken.
    """

    def __init__(self, previous_state, new_state_raw_img, new_state_proc_img):
        self.previous_state = previous_state
        self.new_state_raw_img = new_state_raw_img
        self.new_state_proc_img = new_state_proc_img
        self.process_image()

        post_state = BoardState(self.new_state_proc_img)
        self.new_color_map = post_state.get_color_map()

    def process_image(self):
        """process_image

        Process the raw image for the new state.
        This method spawns a shell to execute the frame.py file.
        """

        args = ['python3', '/home/ubuntu/Desktop/CAPSTONE_R/chess-irs/frame.py',
                'detect', '--input', self.new_state_raw_img, '--output',
                self.new_state_proc_img]

        p = subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


    def determine_move(self):
        """determine_move

        Return a list of moves by comparing the color map of
        the new state to the generated color maps of all
        legal moves from the older board state.

        :return list[str]
        """

        moves = []
        for move in self.previous_state.legal_moves:
            board_copy = self.previous_state.copy()
            board_copy.push(move)

            old_color_map = generate_color_map(board_copy)
            if old_color_map == self.new_color_map:
                return move
                #moves.append(move)

        return None


if __name__ == "__main__":
    board = chess.Board()
    import sys
    m = Move(board, sys.argv[1],sys.argv[2])
    print(m)



