from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        Determines the winner of a Tic-Tac-Toe game based on the given moves.

        Args:
            moves (List[List[int]]): A list of moves where each move is represented as [row, col].

        Returns:
            str: "A" if Player A wins, "B" if Player B wins, "Draw" if the board is full with no winner, 
                 or "Pending" if the game has not yet been completed.
        """

        # Define the size of the Tic-Tac-Toe board (3x3 grid).
        n = 3
        board = [[0] * n for _ in range(n)]
        
        def check_row(row: int, player_id: int) -> bool:
            """Checks if a player has filled an entire row."""
            return all(board[row][col] == player_id for col in range(n))

        def check_col(col: int, player_id: int) -> bool:
            """Checks if a player has filled an entire column."""
            return all(board[row][col] == player_id for row in range(n))

        def check_diagonal(player_id: int) -> bool:
            """Checks if a player has filled the main diagonal."""
            return all(board[row][row] == player_id for row in range(n))

        def check_anti_diagonal(player_id: int) -> bool:
            """Checks if a player has filled the anti-diagonal."""
            return all(board[row][n - 1 - row] == player_id for row in range(n))
        
        # Player A starts first and is represented as 1, Player B as -1.
        player = 1

        for row, col in moves:
            board[row][col] = player

            # Check if the current move results in a win.
            if (
                check_row(row, player) or
                check_col(col, player) or
                (row == col and check_diagonal(player)) or
                (row + col == n - 1 and check_anti_diagonal(player))
            ):
                return 'A' if player == 1 else 'B'
            
            # Switch player for the next move (1 -> -1, -1 -> 1).
            player *= -1
        
        # If all moves are made but no winner, determine if it's a draw or pending.
        return "Draw" if len(moves) == n * n else "Pending"


def main():
    """Runs example test cases for the Tic-Tac-Toe function."""
    solution = Solution()

    test_cases = [
        ([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]], "A"),
        ([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]], "B"),
        ([[0, 0], [1, 1], [2, 2], [1, 0], [1, 2], [2, 1], [0, 2], [2, 0], [0, 1]], "Draw"),
        ([[0, 0], [1, 1]], "Pending")
    ]

    for moves, expected in test_cases:
        result = solution.tictactoe(moves)
        print(f"Moves: {moves} → Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    main()
