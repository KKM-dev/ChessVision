"""
fen_generator.py

Converts a 2D board matrix into a FEN string.
This module is intentionally decoupled from:
- computer vision
- chess engine logic

Board representation:
- 8x8 list of lists
- uppercase letters = White pieces
- lowercase letters = Black pieces
- '.' represents empty square
"""

def board_to_fen(board, side_to_move="w"):
    """
    Convert board matrix to FEN string (piece placement only).

    Args:
        board (list[list[str]]): 8x8 chess board
        side_to_move (str): 'w' or 'b'

    Returns:
        str: FEN string
    """

    fen_rows = []

    for row in board:
        empty_count = 0
        fen_row = ""

        for square in row:
            if square == ".":
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += square

        if empty_count > 0:
            fen_row += str(empty_count)

        fen_rows.append(fen_row)

    fen_position = "/".join(fen_rows)

    # v1: fixed castling, en-passant, move counters
    fen = f"{fen_position} {side_to_move} KQkq - 0 1"

    return fen
