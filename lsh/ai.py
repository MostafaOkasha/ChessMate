from chess import uci
from .config import STOCKFISH_PATH


class StockfishAI:
    def __init__(self):
        # Open stockfish engine and run it
        self.engine = uci.popen_engine(STOCKFISH_PATH)
        self.engine.uci()

    def get_ai_uci(self, board):
        self.engine.position(board)
        move = self.engine.go(movetime=3000)
        return move.bestmove.uci()