from chess_engine.fen_generator import board_to_fen
from chess_engine.stockfish_engine import evaluate_fen

board = [
    ['r','n','b','q','k','b','n','r'],
    ['p','p','p','p','p','p','p','p'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['P','P','P','P','P','P','P','P'],
    ['R','N','B','Q','K','B','N','R']
]

fen = board_to_fen(board, side_to_move="w")
score, best_move = evaluate_fen(fen)

print("Generated FEN:", fen)
print("Evaluation:", score)
print("Best move:", best_move)
