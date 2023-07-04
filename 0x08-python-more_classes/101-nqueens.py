#!/usr/bin/python3
import sys


def position(brd, row, col):
    for m in range(col):
        if brd[row][m] == 1:
            return False

    m = row
    n = col
    while m >= 0 and n >= 0:
        if brd[m][n] == 1:
            return False
        m = m - 1
        n = n - 1

    m = row
    n = col
    while m < N and n >= 0:
        if brd[m][n] == 1:
            return False
        m = m + 1
        n = n - 1
    return True


def crack_n_queens(brd, col):
    if col == N:
        solve = []
        for m in range(N):
            for n in range(N):
                if brd[m][n] == 1:
                    solve.append([m, n])
        solves.append(solve)
        return

    for m in range(N):
        if position(brd, m, col):
            brd[m][col] = 1
            crack_n_queens(brd, col + 1)
            brd[m][col] = 0


def get_solve():
    for solve in solves:
        for row, col in solve:
            print("[{}, {}]".format(row, col), end=' ')
        print()


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

brd = [[0 for i in range(N)] for x in range(N)]

solves = []

crack_n_queens(brd, 0)
get_solve()
