import chess
import chess.engine
from pathlib import Path

ENGINE_PATH = Path(__file__).resolve().parents[2] / "engine" / "stockfish.exe"

def evaluate_fen(fen: str):
    board = chess.Board(fen)

    with chess.engine.SimpleEngine.popen_uci(str(ENGINE_PATH)) as engine:
        info = engine.analyse(board, chess.engine.Limit(depth=15))
        score = info["score"].white()
        best_move = engine.play(board, chess.engine.Limit(depth=15)).move

    return score, best_move
