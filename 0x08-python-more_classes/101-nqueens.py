#!/usr/bin/python3
"""Solves the N-queens puzzle"""


import sys


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):

    n = len(board)

    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1

            solve_nqueens(board, row + 1)

            board[row][col] = 0


def print_solution(board):
    n = len(board)
    solution = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])

    print(solution)


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    solve_nqueens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
