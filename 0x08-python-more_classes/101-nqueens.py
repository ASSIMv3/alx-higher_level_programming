#!/usr/bin/python3
"""Solves the N-queens puzzle"""


import sys


def nqueens(n):
    """A program that solves the N Queens problem"""

    board = [[i, None] for i in range(n)]  # Create an empty board

    def exists(x, y):
        """Check if a queen already exists in the same column (y)"""
        for i in range(x):
            if board[i][1] == y:
                return True
        return False

    def clear(x):
        """Clear the answers"""
        for i in range(x, n):
            board[i][1] = None

    def reject(x, y):
        """Reject the solution"""
        if exists(x, y):
            return False
        for i in range(x):
            if abs(board[i][1] - y) == abs(i - x):
                return False
        return True

    def solve_nqueens(x):
        """Recursive backtracking function"""
        for y in range(n):
            clear(x)
            if reject(x, y):
                board[x][1] = y
                if x == n - 1:
                    print(board)
                else:
                    solve_nqueens(x + 1)

    solve_nqueens(0)  # Start the recursive process at x = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

