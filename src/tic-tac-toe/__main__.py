"""Tic-Tac-Toe game implementation with configurable board size."""

import os
import sys


def clear() -> None:
    """
    Clears the terminal screen.

    Uses 'cls' command for Windows and 'clear' for other platforms.
    """
    os.system("cls" if os.name == "nt" else "clear")


class TicTacToe:
    """
    Tic-Tac-Toe game class with customizable board size.

    Attributes:
        board_max_size (int): Maximum allowed board size
        board_size (int): Current board size
        board (list): 2D game board
        board_len (int): Length of board
        marker_x (int): Player X marker
        marker_o (int): Player O marker
        player (int): Current player's marker
    """

    def __init__(self, board_size):
        """
        Initialize game board and settings.

        Args:
            board_size (int): Size of the game board
        """
        self.board_max_size = 9
        self.board_size = max(3, min(self.board_max_size, board_size))
        self.board = [[0] * self.board_size for _ in range(self.board_size)]
        self.board_len = len(self.board)
        self.marker_x = 1
        self.marker_o = 2
        self.player = self.marker_x

    def get_symbol(self, x, y):
        """
        Get symbol for board position.

        Args:
            x (int): Row index
            y (int): Column index

        Returns:
            str: Symbol to display ('X', 'O', or '-')
        """
        if self.board[x][y] == self.marker_x:
            return "X"

        if self.board[x][y] == self.marker_o:
            return "O"

        return "-"

    def print_board(self):
        """Display current game board state with borders."""
        # Top border
        print("   ", *(str(i + 1) + "  " for i in range(self.board_len)))
        print("  ┌" + "───┬" * (self.board_len - 1) + "───┐")

        # Middle rows
        for i in range(self.board_len):
            # Row content
            print(f"{i + 1} │", end="")
            for j in range(self.board_len):
                print(f" {self.get_symbol(i, j)} │", end="")
            print()

            # Row separator (except last row)
            if i < self.board_len - 1:
                print("  ├" + "───┼" * (self.board_len - 1) + "───┤")

        # Bottom border
        print("  └" + "───┴" * (self.board_len - 1) + "───┘")

    def is_valid_move(self, x, y):
        """
        Check if move is valid.

        Args:
            x (int): Row index
            y (int): Column index

        Returns:
            bool: True if move is valid
        """
        return self.board_len > x >= 0 == self.board[x][y] and 0 <= y < self.board_len

    def place_marker(self, pos):
        """
        Place player's marker on the board.

        Args:
            pos (str): Position string (e.g., "12" for row 1, column 2)

        Returns:
            bool: True if marker was placed successfully
        """
        try:
            if len(pos) != 2:
                raise ValueError("❌ Please enter row and column (e.g., 12)")

            y, x = int(pos[0]) - 1, int(pos[1]) - 1

            if not self.is_valid_move(x, y):
                print("❌ Invalid move! Try again.")
                return False

            self.board[x][y] = self.player
            return True
        except (ValueError, IndexError):
            print("❌ Invalid input! Please enter row and column (e.g., 12)")
            return False

    def full(self):
        """
        Check if board is full.

        Returns:
            bool: True if no empty spaces remain
        """
        return all(cell != 0 for row in self.board for cell in row)

    def switch_player(self):
        """Switch current player between X and O."""
        self.player = self.marker_x if self.player == self.marker_o else self.marker_o

    def check_win(self):
        """
        Check for winning combinations.

        Returns:
            int or None: Winner's marker or None if no winner
        """
        # Horizontal
        for line in self.board:
            if len(set(line)) == 1 and line[0] != 0:
                return line[0]

        # Vertical
        for line in zip(*self.board):
            if len(set(line)) == 1 and line[0] != 0:
                return line[0]

        # Diagonals
        diag1 = [self.board[i][i] for i in range(self.board_len)]
        if len(set(diag1)) == 1 and diag1[0] != 0:
            return diag1[0]
        diag2 = [self.board[self.board_len - (i + 1)][i] for i in range(self.board_len)]
        if len(set(diag2)) == 1 and diag2[0] != 0:
            return diag2[0]

        return None

    def play(self):
        clear()

        """Main game loop handling player turns and game end conditions."""
        while True:
            self.print_board()

            player = "X" if self.player == self.marker_x else "O"
            pos = input(f"🧍 Player {player}'s turn (column+row): ")

            if self.place_marker(pos):
                winner = self.check_win()
                if winner:
                    self.print_board()
                    print(f"🎉 Player {player} wins! 🎉")
                    break

                if self.full():
                    self.print_board()
                    print("😫 It's a tie!")
                    break

                self.switch_player()


def main():
    """Initialize and start the game."""
    size = int(input("🧩 Select board size: "))

    game = TicTacToe(size)
    game.play()

    while input("\n❓ Play again? (y/n): ").lower() in "y":
        game = TicTacToe(size)
        game.play()

    sys.exit()


if __name__ == "__main__":
    main()
