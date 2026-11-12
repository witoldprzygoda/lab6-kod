class TicTacToeBoard:
    def __init__(self):
        # plansza 3 × 3 wypełniona kropkami
        self._board = [["." for _ in range(3)] for _ in range(3)]

    def __getitem__(self, pos):
        """Odczyt pola: board[row, col]."""
        pass  # tu kod; pos to krotka (row, col)

    def __setitem__(self, pos, value):
        """Zapis pola: board[row, col] = value."""
        pass  # tu kod; pos to krotka (row, col)

    def __str__(self):
        return "\n".join(" ".join(row) for row in self._board)


if __name__ == "__main__":
    board = TicTacToeBoard()
    board[0, 0] = "X"
    board[1, 1] = "O"
    board[2, 2] = "X"
    print(board)
